# Directive

## Final architecture

A CLI tool (`audit <repo_path> [--since DATE] [--until DATE] [--output FILE]`)
with an optional Streamlit UI (`app.py`) layered on top of the same core
modules — nothing is duplicated between the two.

Per commit, the pipeline runs:

1. **Extraction** — `extract_commits()` pulls commit metadata and diffs
   from the target repo via git.
2. **Heuristic layer** — `score_heuristics()`: cheap, deterministic
   signals (commit timing patterns, message specificity vs. diff size,
   naming/structure consistency, comment density and style). No API
   calls, no cost.
3. **LLM-judge layer** — `score_with_llm()`: each commit's diff and
   message go to OpenAI's `gpt-5-nano` via the Responses API
   (`client.responses.parse` plus a Pydantic schema), with an explicit
   rubric prompt, and come back as a 0-100 score with written reasoning.
4. **Aggregation** — both layers' scores sit side by side in the
   per-commit report, with a disagreement flag when they diverge by a
   meaningful margin. They're never quietly averaged away.
5. **Output** — a Markdown report from the CLI, or a sortable in-app
   table plus aggregate metrics from the Streamlit UI.

## What changed from intent.md, and why

- **LLM provider: Anthropic → OpenAI's `gpt-5-nano`.** I switched because
  I already had a paid OpenAI subscription. I confirmed `gpt-5-nano` as
  the cheapest GA text model by checking OpenAI's own pricing page
  directly, after an earlier web search turned up unreliable SEO-farm
  results that I caught and threw out rather than trusted.
- **Found and fixed a reasoning-token trap.** `gpt-5-nano` is a reasoning
  model, and it spends hidden "reasoning tokens" out of the same output
  budget as the visible answer. The first real run against a live commit
  came back `status: incomplete` with nothing parsed — 896 of 1024
  tokens had gone to invisible reasoning before it even got to the
  answer. Setting `reasoning: {"effort": "minimal"}` fixed it, and cut
  output tokens by about 7x (1072 → 147) as a bonus.
- **Later moved the default effort from `minimal` to `low`**, on the back
  of a real experiment rather than a guess (see "Known limitations"
  below).
- **Added a `--until` flag.** The CLI originally only filtered commits
  *after* a date. Calibrating against a guaranteed-human baseline
  (pre-2015 Flask commits, from before any AI coding tool existed) meant
  needing "only commits before X," which the tool simply couldn't
  express yet.
- **Added a minimal Streamlit UI (`app.py`)**, installed as an optional
  extra (`[ui]` in `pyproject.toml`) rather than a core dependency — this
  was for the demo recording, not because the CLI on its own wasn't
  enough.

## Added later: Disagreement Investigator (opt-in)

Layer disagreement used to be only flagged. With `--investigate`, a small
tool-using agent (neighbor commits, file history, full diff, then a
submitted verdict, capped at 6 steps) re-examines each flagged commit and
returns a resolved score, which layer was closer, evidence and its full
tool trail. It sometimes surfaces concrete evidence the first pass lacked
and sometimes only confirms the judge; it is not a ground-truth oracle.

## Scoring rubric actually used for the LLM judge

Each commit's diff and message go to `gpt-5-nano` (Responses API,
structured output via a Pydantic schema) with a rubric that asks for a
0-100 AI-authorship-likelihood score plus a short, concrete justification
that has to cite something specific in the diff or message — not a vague
confidence statement. `reasoning.effort` defaults to `low` (see below for
why).

## Known limitations / where it's confidently wrong

- **Disciplined human practice reads as an AI signal.** A real 2010
  commit by Flask's actual creator, Armin Ronacher, consistently scored
  65-72/100 ("substantial AI involvement") across every effort level I
  tried (`minimal`, a repeat `minimal` run, and `low`). The judge's own
  stated reason was a clean docstring, a `versionadded::` marker, and a
  changelog entry — hallmarks of careful professional engineering, not
  of AI generation. This is a genuine, unresolved limitation: right now
  the tool can't tell "too clean because AI wrote it" apart from "too
  clean because a disciplined human wrote it," since both leave the
  same surface signature. I chose not to chase a rubric rewrite to fix
  this inside the quest's timebox, and I'm flagging it here honestly
  instead of papering over it.
- **Calibration separation is weaker than I'd like.** Pre-2015 Flask
  commits (guaranteed human, predating any AI coding tool) did score
  lower than the known AI-heavy `rubiks-cube-solver` repo on both layers
  — heuristic 42.8 vs 52.5, LLM judge 47.6 vs 66.3 — so the direction is
  right. But Flask's average landed in a "mostly human, light AI
  assistance" band rather than down near 0-20, where a true pre-AI
  baseline should sit.
- **An effort-tuning investigation, and where my first guess was wrong.**
  I initially suspected `reasoning.effort: "minimal"` was causing scores
  to cluster on a handful of repeated values instead of spreading across
  0-100. To test that, I re-ran `minimal` a second time on the same 30
  Flask commits — and it came back with mostly *different* scores from
  the first run (16 unique values out of 30, the same spread as `low`).
  The clustering turned out to be ordinary run-to-run model variance, not
  a deterministic effect of the effort setting. My first hypothesis was
  wrong, and it was the re-test that caught that, not more thinking about
  it in the abstract.
  - Comparing `low` against `minimal` on the same 30 commits: the Armin
    Ronacher false positive did **not** resolve at any effort level
    (72 → 68 → 65). A separate, self-contradicting commit — where the
    reasoning said "unlikely AI" but the score was 72 — **did** resolve
    cleanly at `low` (score 22, reasoning now matches the number); a
    fresh `minimal` run only partly improved it (score 60, hedgy
    reasoning rather than a flat contradiction).
  - Cost difference: `low` runs about 46% more expensive than `minimal`
    (~$0.0058 vs ~$0.0040 for 30 calls, mostly from reasoning tokens),
    but both are trivial in absolute terms — under $0.20 per 1,000
    commits either way. Cost wasn't really a factor in this decision.
  - **Decision:** switched the default to `low`, since it fixes the
    contradiction and costs almost nothing extra — while being clear
    that it does not fix the Armin Ronacher-style false positive.

## What I'd do with another week

- Rework the rubric to actually separate "stylistically clean" from
  "AI-generated" — probably needs a few-shot version with contrasting
  examples (disciplined human vs. AI-generated) instead of one generic
  prompt.
- Test against a larger, more varied set of known-ground-truth repos —
  more human baselines from different eras and styles, more AI-heavy
  repos built with different tools — to get real precision/recall
  numbers instead of two data points.
- Consider a lightweight multi-provider option (OpenAI and Anthropic
  side by side), if this were ever heading toward real use. Explicitly
  out of scope for the 5-day build itself.
