from __future__ import annotations

from dataclasses import dataclass

from .git_extract import Commit


@dataclass
class HeuristicSignal:
    name: str
    score: float
    reasoning: str


@dataclass
class HeuristicResult:
    score: float
    signals: list[HeuristicSignal]


def score_message_vs_diff_size(commit: Commit) -> HeuristicSignal:
    total_lines = commit.insertions + commit.deletions
    message_len = len(commit.message.split())
    is_long_message = message_len >= 12
    is_large_diff = total_lines >= 40

    if is_large_diff and is_long_message:
        score = 75.0
        reasoning = (
            f"Large diff ({total_lines} lines) paired with a detailed message "
            f"({message_len} words) — consistent with AI-drafted commit messages "
            f"that narrate the change in full sentences."
        )
    elif is_large_diff and not is_long_message:
        score = 25.0
        reasoning = (
            f"Large diff ({total_lines} lines) with a short message "
            f"({message_len} words) — more typical of a human committing quickly "
            f"without narrating the change."
        )
    elif not is_large_diff and is_long_message:
        score = 55.0
        reasoning = (
            f"Small diff ({total_lines} lines) but a disproportionately detailed "
            f"message ({message_len} words) — could be AI-authored boilerplate, "
            f"but also matches careful human commit discipline."
        )
    else:
        score = 40.0
        reasoning = (
            f"Small diff ({total_lines} lines), short message ({message_len} "
            f"words) — no strong signal either way."
        )
    return HeuristicSignal("message_vs_diff_size", score, reasoning)


def score_commit_timing(commits: list[Commit]) -> dict[str, HeuristicSignal]:
    sorted_commits = sorted(commits, key=lambda c: c.date)
    results: dict[str, HeuristicSignal] = {}
    for i, commit in enumerate(sorted_commits):
        if i == 0:
            results[commit.sha] = HeuristicSignal(
                "commit_timing",
                40.0,
                "First commit in range — no prior commit to compare timing against.",
            )
            continue
        gap = (commit.date - sorted_commits[i - 1].date).total_seconds()
        if gap < 90:
            score = 80.0
            reasoning = (
                f"Only {gap:.0f}s after the previous commit — faster than a "
                f"typical manual edit-test-commit cycle."
            )
        elif gap < 600:
            score = 55.0
            reasoning = (
                f"{gap / 60:.1f} min after the previous commit — plausible for "
                f"either a fast human pass or an AI-assisted one."
            )
        else:
            score = 30.0
            reasoning = (
                f"{gap / 60:.0f} min gap since the previous commit — consistent "
                f"with normal human working pace."
            )
        results[commit.sha] = HeuristicSignal("commit_timing", score, reasoning)
    return results


def score_heuristics(commits: list[Commit]) -> dict[str, HeuristicResult]:
    timing_signals = score_commit_timing(commits)
    results: dict[str, HeuristicResult] = {}
    for commit in commits:
        msg_signal = score_message_vs_diff_size(commit)
        timing_signal = timing_signals[commit.sha]
        combined = (msg_signal.score + timing_signal.score) / 2
        results[commit.sha] = HeuristicResult(combined, [msg_signal, timing_signal])
    return results
