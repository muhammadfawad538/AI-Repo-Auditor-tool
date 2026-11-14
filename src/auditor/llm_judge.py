from __future__ import annotations

from dataclasses import dataclass

from openai import OpenAI
from pydantic import BaseModel

from .git_extract import Commit

DEFAULT_MODEL = "gpt-5-nano"
DEFAULT_EFFORT = "low"
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


class JudgeSchema(BaseModel):
    score: int
    reasoning: str
    key_signals: list[str]


@dataclass
class JudgeResult:
    score: float | None
    reasoning: str
    key_signals: list[str]
    truncated: bool
    error: str | None = None
    usage: dict | None = None


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
    client: OpenAI | None = None,
    effort: str = DEFAULT_EFFORT,
) -> JudgeResult:
    client = client or OpenAI()
    user_prompt, truncated = _build_user_prompt(commit)

    response = client.responses.parse(
        model=model,
        max_output_tokens=2048,
        reasoning={"effort": effort},
        input=[
            {"role": "system", "content": RUBRIC},
            {"role": "user", "content": user_prompt},
        ],
        text_format=JudgeSchema,
    )

    parsed = response.output_parsed
    if parsed is None:
        raise RuntimeError(f"model returned no parsed output (status={response.status})")

    usage = response.usage
    return JudgeResult(
        score=float(parsed.score),
        reasoning=parsed.reasoning,
        key_signals=parsed.key_signals,
        truncated=truncated,
        usage={
            "input_tokens": usage.input_tokens,
            "output_tokens": usage.output_tokens,
            "reasoning_tokens": usage.output_tokens_details.reasoning_tokens,
            "total_tokens": usage.total_tokens,
        },
    )
