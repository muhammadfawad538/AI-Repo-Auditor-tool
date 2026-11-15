from __future__ import annotations

import json
import subprocess
from dataclasses import dataclass, field
from pathlib import Path

from openai import OpenAI

from .git_extract import Commit, _run
from .heuristics import HeuristicResult
from .llm_judge import DEFAULT_EFFORT, DEFAULT_MODEL, JudgeResult, _build_user_prompt

MAX_FULL_DIFF_CHARS = 12000
MAX_STEPS = 6

SYSTEM_PROMPT = """You are an investigator for an AI-authorship audit tool. Two scoring \
layers disagreed sharply about one git commit: a cheap heuristic layer (commit timing, \
message length vs diff size) and an LLM judge that read the diff. Your job is to resolve \
the disagreement with evidence, not to re-guess from scratch.

Use the tools to gather context the first pass did not have: neighbouring commits (pacing, \
message style, whether this commit is part of a burst), the history of the files touched, \
and the full untruncated diff of specific files. Call 2-4 tools, then call submit_verdict.

Scoring scale (same as the judge): 0-20 hand-written, 21-50 mostly human, 51-80 \
substantial AI involvement, 81-100 almost certainly AI-generated. Remember that clean, \
well-documented code is NOT by itself evidence of AI — disciplined humans write it too. \
Say which layer was closer and cite concrete evidence you actually saw in tool output."""

TOOLS = [
    {
        "type": "function",
        "name": "get_neighbor_commits",
        "description": "Message, size and time gap of up to n commits before and after the commit under investigation.",
        "parameters": {
            "type": "object",
            "properties": {"n": {"type": "integer", "description": "How many on each side (1-5)."}},
            "required": ["n"],
            "additionalProperties": False,
        },
        "strict": True,
    },
    {
        "type": "function",
        "name": "get_file_history",
        "description": "Recent commit history (hash, author, relative date, subject) of one file path touched by this commit.",
        "parameters": {
            "type": "object",
            "properties": {
                "path": {"type": "string", "description": "Repo-relative file path."},
                "limit": {"type": "integer", "description": "Max commits to return (1-15)."},
            },
            "required": ["path", "limit"],
            "additionalProperties": False,
        },
        "strict": True,
    },
    {
        "type": "function",
        "name": "get_full_diff",
        "description": "Full, untruncated diff of one file in the commit under investigation.",
        "parameters": {
            "type": "object",
            "properties": {"path": {"type": "string", "description": "Repo-relative file path."}},
            "required": ["path"],
            "additionalProperties": False,
        },
        "strict": True,
    },
    {
        "type": "function",
        "name": "submit_verdict",
        "description": "Submit the final ruling. Ends the investigation.",
        "parameters": {
            "type": "object",
            "properties": {
                "score": {"type": "integer", "description": "Resolved 0-100 AI-authorship score."},
                "closer_layer": {"type": "string", "enum": ["heuristic", "llm_judge", "neither"]},
                "reasoning": {"type": "string"},
                "evidence": {"type": "array", "items": {"type": "string"}},
            },
            "required": ["score", "closer_layer", "reasoning", "evidence"],
            "additionalProperties": False,
        },
        "strict": True,
    },
]


@dataclass
class InvestigationResult:
    score: float | None
    closer_layer: str
    reasoning: str
    evidence: list[str] = field(default_factory=list)
    steps: list[dict] = field(default_factory=list)
    usage: dict = field(default_factory=dict)
    error: str | None = None


def _touched_files(repo_path: Path, sha: str) -> list[str]:
    out = _run(repo_path, "show", sha, "--format=", "--name-only")
    return [line for line in out.splitlines() if line.strip()]


def _neighbor_commits(commit: Commit, all_commits: list[Commit], n: int) -> str:
    n = max(1, min(n, 5))
    ordered = sorted(all_commits, key=lambda c: c.date)
    idx = next(i for i, c in enumerate(ordered) if c.sha == commit.sha)
    lines = []
    for c in ordered[max(0, idx - n): idx + n + 1]:
        gap_min = (c.date - commit.date).total_seconds() / 60
        marker = ">>" if c.sha == commit.sha else "  "
        subject = c.message.splitlines()[0][:80] if c.message else ""
        lines.append(
            f"{marker} {c.sha[:10]} {gap_min:+.0f} min, +{c.insertions}/-{c.deletions} "
            f"in {c.files_changed} file(s), author={c.author}: {subject}"
        )
    return "\n".join(lines)


def _file_history(repo_path: Path, sha: str, path: str, limit: int) -> str:
    limit = max(1, min(limit, 15))
    out = _run(repo_path, "log", "--follow", f"-n{limit}", "--format=%h|%an|%ar|%s", sha, "--", path)
    return out.strip() or f"No history found for {path}."


def _full_diff(repo_path: Path, sha: str, path: str) -> str:
    out = _run(repo_path, "show", sha, "--format=", "--", path)
    if not out.strip():
        return f"No diff for {path} in this commit."
    if len(out) > MAX_FULL_DIFF_CHARS:
        return out[:MAX_FULL_DIFF_CHARS] + f"\n... [truncated at {MAX_FULL_DIFF_CHARS} chars] ..."
    return out


def _run_tool(name: str, args: dict, commit: Commit, all_commits: list[Commit], repo_path: Path) -> str:
    try:
        if name == "get_neighbor_commits":
            return _neighbor_commits(commit, all_commits, args["n"])
        if name == "get_file_history":
            return _file_history(repo_path, commit.sha, args["path"], args["limit"])
        if name == "get_full_diff":
            return _full_diff(repo_path, commit.sha, args["path"])
        return f"Unknown tool {name}."
    except subprocess.CalledProcessError as e:
        return f"git error: {(e.stderr or str(e)).strip()[:300]}"


def _opening_message(commit: Commit, repo_path: Path, heuristic: HeuristicResult, judge: JudgeResult) -> str:
    commit_text, _ = _build_user_prompt(commit)
    signals = "\n".join(f"- {s.name} ({s.score:.0f}): {s.reasoning}" for s in heuristic.signals)
    files = ", ".join(_touched_files(repo_path, commit.sha)[:30])
    return (
        f"Commit {commit.sha[:10]} by {commit.author}, {commit.date.isoformat(timespec='minutes')}\n"
        f"Files touched: {files}\n\n"
        f"Heuristic layer score: {heuristic.score:.0f}/100\n{signals}\n\n"
        f"LLM judge score: {judge.score:.0f}/100\nJudge reasoning: {judge.reasoning}\n"
        f"Judge key signals: {', '.join(judge.key_signals)}\n\n{commit_text}"
    )


def investigate_commit(
    commit: Commit,
    all_commits: list[Commit],
    repo_path: Path,
    heuristic: HeuristicResult,
    judge: JudgeResult,
    client: OpenAI | None = None,
    model: str = DEFAULT_MODEL,
    max_steps: int = MAX_STEPS,
) -> InvestigationResult:
    client = client or OpenAI()
    conversation: list = [
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": _opening_message(commit, repo_path, heuristic, judge)},
    ]
    steps: list[dict] = []
    usage = {"input_tokens": 0, "output_tokens": 0, "calls": 0}

    for step in range(max_steps + 1):
        # On the last step the model must stop gathering and rule.
        tool_choice = "required" if step < max_steps else {"type": "function", "name": "submit_verdict"}
        response = client.responses.create(
            model=model,
            reasoning={"effort": DEFAULT_EFFORT},
            max_output_tokens=4096,
            input=conversation,
            tools=TOOLS,
            tool_choice=tool_choice,
        )
        usage["calls"] += 1
        usage["input_tokens"] += response.usage.input_tokens
        usage["output_tokens"] += response.usage.output_tokens
        conversation += response.output

        calls = [item for item in response.output if item.type == "function_call"]
        if not calls:
            return InvestigationResult(
                score=None, closer_layer="neither", reasoning="", steps=steps, usage=usage,
                error=f"model made no tool call (status={response.status})",
            )

        for call in calls:
            args = json.loads(call.arguments)
            if call.name == "submit_verdict":
                steps.append({"tool": "submit_verdict", "args": {"score": args["score"]}, "result": "ruling submitted"})
                return InvestigationResult(
                    score=float(args["score"]),
                    closer_layer=args["closer_layer"],
                    reasoning=args["reasoning"],
                    evidence=args["evidence"],
                    steps=steps,
                    usage=usage,
                )
            output = _run_tool(call.name, args, commit, all_commits, repo_path)
            steps.append({"tool": call.name, "args": args, "result": output[:200]})
            conversation.append({"type": "function_call_output", "call_id": call.call_id, "output": output})

    return InvestigationResult(
        score=None, closer_layer="neither", reasoning="", steps=steps, usage=usage,
        error=f"no verdict after {max_steps} steps",
    )
