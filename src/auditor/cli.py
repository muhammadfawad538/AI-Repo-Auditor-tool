from __future__ import annotations

import argparse
import sys
from pathlib import Path

import openai
from dotenv import load_dotenv

from .git_extract import extract_commits, resolve_repo
from .heuristics import score_heuristics
from .investigator import InvestigationResult, investigate_commit
from .llm_judge import DEFAULT_MODEL, JudgeResult, score_with_llm
from .report import DISAGREEMENT_THRESHOLD, CommitScore, render_report


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="audit",
        description="Score a git repo's commit history for AI-driven vs hand-written authorship.",
    )
    parser.add_argument("repo", help="Local repo path or a cloneable git URL")
    parser.add_argument("--since", help="Only consider commits after this date, e.g. 2026-01-01")
    parser.add_argument("--until", help="Only consider commits before this date, e.g. 2015-01-01")
    parser.add_argument("--output", default="report.md", help="Markdown report output path")
    parser.add_argument(
        "--sample",
        type=int,
        default=None,
        help=(
            "Cap the number of commits sent to the LLM judge (evenly sampled "
            "across the matched commits). Heuristics still run on every "
            "matched commit regardless of this flag."
        ),
    )
    parser.add_argument(
        "--no-llm", action="store_true", help="Skip the LLM judge layer entirely (heuristics only)"
    )
    parser.add_argument(
        "--model", default=DEFAULT_MODEL, help=f"OpenAI model id for the LLM judge (default: {DEFAULT_MODEL})"
    )
    parser.add_argument(
        "--investigate",
        action="store_true",
        help="Run the investigator agent on commits where the two layers disagree (extra API calls)",
    )
    parser.add_argument(
        "--max-investigations",
        type=int,
        default=5,
        help="Cap on how many disagreeing commits the agent investigates (default: 5)",
    )
    return parser


def _sample_commits(commits: list, n: int | None) -> list:
    if n is None or n >= len(commits):
        return commits
    if n <= 0:
        return []
    step = len(commits) / n
    return [commits[int(i * step)] for i in range(n)]


def main(argv: list[str] | None = None) -> int:
    load_dotenv()
    args = build_parser().parse_args(argv)

    repo_path = resolve_repo(args.repo)
    commits = extract_commits(repo_path, since=args.since, until=args.until)
    if not commits:
        print("No commits found for the given repo/--since/--until range.", file=sys.stderr)
        return 1

    print(f"Extracted {len(commits)} commit(s) from {args.repo}")
    heuristic_results = score_heuristics(commits)

    judge_results: dict[str, JudgeResult] = {}
    if not args.no_llm:
        llm_commits = _sample_commits(commits, args.sample)
        if args.sample is not None and args.sample < len(commits):
            print(
                f"Sampling {len(llm_commits)} of {len(commits)} commits for the "
                f"LLM judge layer (--sample {args.sample})."
            )
        print(
            f"Calling model '{args.model}' for {len(llm_commits)} commit(s) — "
            f"this makes {len(llm_commits)} API call(s) against OPENAI_API_KEY. "
            f"Use --sample to cap this on large repos, or --no-llm to skip it."
        )
        client = openai.OpenAI()
        for i, commit in enumerate(llm_commits, 1):
            print(f"  [{i}/{len(llm_commits)}] {commit.sha[:10]}")
            try:
                judge_results[commit.sha] = score_with_llm(commit, model=args.model, client=client)
            except openai.AuthenticationError:
                print(
                    "OPENAI_API_KEY missing or invalid — aborting the LLM judge "
                    "layer. Remaining commits will show heuristic scores only.",
                    file=sys.stderr,
                )
                break
            except openai.RateLimitError as e:
                judge_results[commit.sha] = JudgeResult(
                    score=None, reasoning="", key_signals=[], truncated=False, error=f"rate limited: {e}"
                )
            except openai.BadRequestError as e:
                judge_results[commit.sha] = JudgeResult(
                    score=None, reasoning="", key_signals=[], truncated=False, error=f"bad request: {e}"
                )
            except openai.InternalServerError as e:
                judge_results[commit.sha] = JudgeResult(
                    score=None, reasoning="", key_signals=[], truncated=False, error=f"server error: {e}"
                )
            except openai.APIConnectionError as e:
                judge_results[commit.sha] = JudgeResult(
                    score=None, reasoning="", key_signals=[], truncated=False, error=f"connection error: {e}"
                )
            except openai.APIError as e:
                judge_results[commit.sha] = JudgeResult(
                    score=None, reasoning="", key_signals=[], truncated=False, error=f"API error: {e}"
                )

    investigations: dict[str, InvestigationResult] = {}
    if args.investigate:
        flagged = [
            c for c in commits
            if (j := judge_results.get(c.sha)) is not None
            and j.score is not None
            and abs(heuristic_results[c.sha].score - j.score) >= DISAGREEMENT_THRESHOLD
        ][: args.max_investigations]
        if flagged:
            print(
                f"Investigating {len(flagged)} disagreeing commit(s) with the agent — "
                f"roughly 2 API calls each against OPENAI_API_KEY (cap: --max-investigations)."
            )
            client = openai.OpenAI()
            for i, commit in enumerate(flagged, 1):
                print(f"  [{i}/{len(flagged)}] {commit.sha[:10]}")
                try:
                    investigations[commit.sha] = investigate_commit(
                        commit, commits, repo_path,
                        heuristic_results[commit.sha], judge_results[commit.sha],
                        client=client, model=args.model,
                    )
                except openai.APIError as e:
                    investigations[commit.sha] = InvestigationResult(
                        score=None, closer_layer="neither", reasoning="", error=f"API error: {e}"
                    )
        else:
            print("No disagreeing commits to investigate.")

    scores = [
        CommitScore(
            commit=c,
            heuristic=heuristic_results[c.sha],
            judge=judge_results.get(c.sha),
            investigation=investigations.get(c.sha),
        )
        for c in commits
    ]

    report = render_report(scores, repo_label=args.repo)
    output_path = Path(args.output)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(report, encoding="utf-8")
    print(f"Report written to {args.output}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
