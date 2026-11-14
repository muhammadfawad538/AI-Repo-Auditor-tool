# Write-up: AI Usage Authenticity Auditor

## The problem

Companies — including this one, explicitly, through this very quest — are
now hiring and evaluating engineers on "genuine, daily AI-native use," but
there's no real way to verify that claim from the outside. A resume, a
Loom, or a usage log can all be written up convincingly after the fact.
Commit histories are the closest thing to ground truth, but no working
tool reads a repo's commits and diffs and gives an honest, *explained*
assessment of how AI-driven the work actually was — most attempts would
either be a naive heuristic script wearing an "AI-powered" label, or a
black-box score with no reasoning behind it.

## What I unlearned

- **That a single scoring layer would be "AI-native" enough.** The design
  only became honest once I split it into a heuristic layer and an
  LLM-judge layer shown *separately*, with disagreement between them
  surfaced rather than averaged away — a single blended score would have
  hidden exactly the kind of signal (a tool confidently wrong) that
  matters most here.
- **That more reasoning effort means better accuracy, without testing it.**
  I initially assumed `reasoning.effort: "minimal"` was the cause of
  scores clustering on repeated values instead of spreading naturally. I
  re-ran the same 30 commits at `minimal` a second time specifically to
  test that assumption, and the scores came back mostly different anyway
  — the clustering was just model variance, not an effort-setting
  artifact. I was wrong, and the fix wasn't more reasoning about the
  hypothesis, it was running the actual experiment.
- **That calibration could be skipped or faked.** It would have been easy
  to run the tool once, get a plausible-looking number, and call it done.
  Testing it against a repo I know is AI-heavy and a repo I know is
  genuinely human-only (pre-2015 Flask commits, from before AI coding
  tools existed) is what actually surfaced the tool's real behavior —
  including a genuine false positive I wouldn't have found otherwise.

## How I used AI

AI (primarily Claude Code, with OpenAI's `gpt-5-nano` as the scoring
engine inside the tool itself) was the default way of building this, not
an occasional aid: scaffolding the CLI and extraction logic, iterating on
the rubric prompt for the LLM-judge layer, debugging the reasoning-token
issue, running and interpreting the effort-level comparison experiment,
building and testing the Streamlit UI (including catching a real
`use_container_width` deprecation via Streamlit's own `AppTest` harness
rather than me eyeballing the code), and writing most of the day-to-day
log entries in `docs/ai-usage-log.md` as the work happened. I reviewed and
directed each step rather than hand-writing the implementation myself.

## What failed

- **A real bug, not a hypothetical one.** The first live LLM-judge call
  came back `status: incomplete` with nothing parsed. `gpt-5-nano` had
  spent 896 of 1024 output tokens on hidden reasoning tokens before it
  ever got to the actual answer. Fixed by setting `reasoning.effort`
  explicitly.
- **A wrong hypothesis, caught by testing it.** See "What I unlearned"
  above — the effort-tuning theory for score clustering turned out to be
  wrong once I actually re-ran the experiment.
- **An unresolved false positive.** A genuine 2010 commit by Flask's
  actual creator, Armin Ronacher, consistently scores 65-72/100
  ("substantial AI involvement") across every effort level I tested. The
  LLM judge's stated reasoning names a clean docstring, a
  `versionadded::` marker, and a changelog entry as its evidence —
  disciplined professional practice, not an AI signal. I did not fix this
  within the timebox; it's documented as an open limitation in
  `directive.md` rather than hidden.
- **The scores themselves aren't fully reproducible.** Re-running the
  exact same effort setting on the exact same 30 commits a second time
  produced mostly different individual scores (the same commit moved from
  72 to 68 on one re-run, 72 to 60 on another). This is what exposed the
  wrong hypothesis above in the first place, but it's also a limitation
  in its own right: one audit run is a sample, not a fixed measurement,
  and a second run on an unchanged repo can plausibly come back looking
  different.

## What it does now

A CLI (`audit <repo> [--since] [--until] [--output]`) and an optional
Streamlit UI that both run the same two-layer pipeline: a free heuristic
pass plus an LLM-judge pass with explicit reasoning, producing a
per-commit report and an aggregate repo score, with layer disagreement
surfaced rather than hidden. Calibrated against a known AI-heavy repo
(scores meaningfully higher) and a known human-only baseline (scores
meaningfully lower, though not as cleanly separated as ideal) — with the
gap and its cause documented honestly rather than smoothed over.

## What I'd do with another week

Rework the rubric to separate disciplined human style from AI-generation
signal (likely needs contrasting few-shot examples), calibrate against a
larger, more varied set of known-ground-truth repos to get real
precision/recall numbers instead of two data points, and measure
run-to-run variance directly by repeating the same commit set multiple
times per setting, rather than trusting a single sample.
