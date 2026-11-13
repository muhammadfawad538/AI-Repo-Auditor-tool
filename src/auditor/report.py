from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime

from .git_extract import Commit
from .heuristics import HeuristicResult
from .llm_judge import JudgeResult

DISAGREEMENT_THRESHOLD = 30.0


@dataclass
class CommitScore:
    commit: Commit
    heuristic: HeuristicResult
    judge: JudgeResult | None


def _blended_score(scored: CommitScore) -> float | None:
    if scored.judge is None or scored.judge.score is None:
        return None
    return round((scored.heuristic.score + scored.judge.score) / 2, 1)


def render_report(scores: list[CommitScore], repo_label: str) -> str:
    lines = [f"# AI Usage Authenticity Report — {repo_label}", ""]
    lines.append(f"Generated {datetime.now().isoformat(timespec='seconds')}")
    lines.append(f"Commits analyzed: {len(scores)}")
    lines.append("")
    lines.append("## Aggregate summary")
    lines.append("")

    avg_heuristic = sum(s.heuristic.score for s in scores) / len(scores)
    lines.append(f"- Heuristic layer average: {avg_heuristic:.1f}/100 (n={len(scores)})")

    judged = [s for s in scores if s.judge is not None and s.judge.score is not None]
    if judged:
        avg_judge = sum(s.judge.score for s in judged) / len(judged)
        disagreements = [
            s for s in judged if abs(s.heuristic.score - s.judge.score) >= DISAGREEMENT_THRESHOLD
        ]
        lines.append(f"- LLM judge layer average: {avg_judge:.1f}/100 (n={len(judged)})")
        lines.append(
            f"- Commits where the two layers disagree by >={DISAGREEMENT_THRESHOLD:.0f} "
            f"points: {len(disagreements)}"
        )
    else:
        lines.append("- LLM judge layer: not run for this report.")
    lines.append("")

    lines.append("## Per-commit detail")
    lines.append("")
    for s in scores:
        c = s.commit
        blended = _blended_score(s)
        lines.append(f"### `{c.sha[:10]}` — {c.message.splitlines()[0][:72]}")
        lines.append(f"- Author: {c.author} <{c.author_email}> — {c.date.isoformat(timespec='seconds')}")
        lines.append(f"- Diff size: +{c.insertions}/-{c.deletions} across {c.files_changed} file(s)")
        lines.append(f"- Heuristic score: **{s.heuristic.score:.1f}/100**")
        for sig in s.heuristic.signals:
            lines.append(f"  - *{sig.name}* ({sig.score:.0f}): {sig.reasoning}")

        if s.judge is None:
            lines.append("- LLM judge: not run (sampling or `--no-llm`).")
        elif s.judge.error:
            lines.append(f"- LLM judge: failed — {s.judge.error}")
        else:
            lines.append(f"- LLM judge score: **{s.judge.score:.0f}/100**")
            lines.append(f"  - {s.judge.reasoning}")
            if s.judge.key_signals:
                lines.append(f"  - Key signals: {', '.join(s.judge.key_signals)}")
            if s.judge.truncated:
                lines.append("  - Note: diff was truncated for length before being sent to the LLM judge.")
            if blended is not None:
                lines.append(f"- Blended score: **{blended}/100**")
            if abs(s.heuristic.score - s.judge.score) >= DISAGREEMENT_THRESHOLD:
                lines.append(
                    "  - Heuristic and LLM layers disagree by "
                    f">={DISAGREEMENT_THRESHOLD:.0f} points — treat this commit's score as uncertain."
                )
        lines.append("")
    return "\n".join(lines)
