# Intent

## Problem
Companies (including this one, explicitly) are now hiring and evaluating
engineers on "genuine, daily AI-native use" — but there is no real way to
verify that claim from the outside. A resume, a Loom video, or a usage log
can all be written up convincingly after the fact. Commit histories are the
closest thing to ground truth, but nobody has a working tool that reads a
repo's commit history and diff content and gives an honest, explained
assessment of how AI-driven the work actually was.

This is a real, currently-unsolved problem — and it's the exact problem this
quest is implicitly asking me to prove I've solved for myself.

## What I'm building
**AI Usage Authenticity Auditor** — a CLI tool that takes a git repository
and produces a per-commit and aggregate score for how likely each piece of
work was AI-driven, with human-readable reasoning for each score (not a
black-box number).

Two scoring layers, combined and shown separately:
1. **Heuristic signals** (cheap, deterministic): commit timing patterns,
   message specificity vs. diff size, structural/naming consistency, comment
   density and style shifts.
2. **LLM judge** (the actually "AI-native" part): each commit's diff + message
   is sent to an LLM with an explicit rubric, returning a 0-100 score and a
   short explanation of what in the diff drove that score.

The two layers are shown side by side, including where they disagree — that
disagreement is itself useful signal, and hiding it would make the tool less
honest than the thing it's trying to audit.

## Why this problem, why now
- It's genuinely hard: AI-authored and human-authored code increasingly look
  alike at the surface level; a good signal has to look at process (commit
  shape, timing, iteration pattern) as well as content.
- It's real: every hiring pipeline doing exactly what this quest is doing
  would benefit from a tool like this, including the one evaluating me.
- It's AI-native by construction: the core judgment layer *is* an LLM call
  with a reasoning rubric — not a heuristic script wearing an AI label.
- It's scoped to ship: CLI + two scoring layers + a Markdown report is
  buildable and testable in days, not weeks.

## What "done" looks like for day 1 (today)
- Repo scaffolded, `CLAUDE.md` + this file committed.
- Git-log/diff extraction working end-to-end on a real repo.
- First pass of the heuristic layer scoring at least one signal.
- First LLM-judge call working on at least one real commit, end to end.

## Risks / open questions going in
- Calibration: no ground truth exists for "AI vs. human" commits at scale.
  Plan: test against repos I know the real answer for (my own history,
  including commits I know were heavily AI-assisted vs. not), plus a couple
  of public repos, and be explicit in the write-up about where it's
  confidently right vs. guessing.
- Cost/rate limits: scoring every commit in a large repo via LLM calls could
  be slow/expensive. Plan: support `--since` and sampling, and say so plainly
  rather than silently truncating.
- This is explicitly a heuristic-plus-LLM-opinion tool, not a certainty
  machine — the output needs to say that about itself.
