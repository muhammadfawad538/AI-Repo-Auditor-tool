from __future__ import annotations

import json
from dataclasses import dataclass

import anthropic

from .git_extract import Commit

DEFAULT_MODEL = "claude-opus-5-5"
MAX_DIFF_CHARS = 8000

RUBRIC = """You are auditing a single git commit to judge how likely it is that \
the code change was substantially AI-generated (e.g. by an LLM coding assistant) \
versus hand-written by a human, or some mix of both.

Score 0-100, where:
- 0-20: almost certainly hand-written — idiosyncratic style, incremental or \
  partial edits, inconsistent formatting, human-typical shortcuts or typos.
- 21-50: mostly human, possibly with light AI assistance (autocomplete, a snippet).
- 51-80: substantial AI involvement — unusually complete/consistent structure, \
  verbose or textbook-perfect comments, defensive code beyond what the stated \
  purpose needs, or a commit message that reads like it was generated alongside \
  the diff.
- 81-100: almost certainly AI-generated — a near-complete implementation in a \
  single commit, uniform style with no human "mess", exhaustive error handling \
  for cases the commit doesn't call for, or a mismatch between a terse task and \
  an extensively engineered solution.

Judge the diff and message together, and call out any disagreement between them \
(e.g. the message undersells or oversells the diff). Be specific: cite lines, \
naming, or structural choices you actually see, not generic impressions."""

JUDGE_SCHEMA = {
    "type": "object",
    "properties": {
        "score": {"type": "integer", "minimum": 0, "maximum": 100},
        "reasoning": {"type": "string"},
        "key_signals": {"type": "array", "items": {"type": "string"}},
    },
    "required": ["score", "reasoning", "key_signals"],
    "additionalProperties": False,
}


@dataclass
class JudgeResult:
    score: float | None
    reasoning: str
    key_signals: list[str]
    truncated: bool
    error: str | None = None


def _build_user_prompt(commit: Commit) -> tuple[str, bool]:
    diff = commit.diff
    truncated = len(diff) > MAX_DIFF_CHARS
    if truncated:
        diff = diff[:MAX_DIFF_CHARS] + "\n... [diff truncated for length] ..."
    return (
        f"Commit message:\n{commit.message}\n\n"
        f"Diff{' (truncated)' if truncated else ''}:\n{diff}"
    ), truncated


def score_with_llm(
    commit: Commit,
    model: str = DEFAULT_MODEL,
    client: anthropic.Anthropic | None = None,
) -> JudgeResult:
    client = client or anthropic.Anthropic()
    user_prompt, truncated = _build_user_prompt(commit)

    response = client.messages.create(
        model=model,
        max_tokens=1024,
        system=RUBRIC,
        messages=[{"role": "user", "content": user_prompt}],
        output_config={"format": {"type": "json_schema", "schema": JUDGE_SCHEMA}},
    )

    text = next(b.text for b in response.content if b.type == "text")
    data = json.loads(text)
    return JudgeResult(
        score=float(data["score"]),
        reasoning=data["reasoning"],
        key_signals=data["key_signals"],
        truncated=truncated,
    )
