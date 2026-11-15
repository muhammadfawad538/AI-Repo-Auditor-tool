# AI Usage Log

Real-time log, appended to as work happens — not reconstructed afterward.
Each entry: date, what was done, how AI was used (drafted vs. hand-edited,
what was trusted on first pass vs. needed rework), and anything that failed
or was scrapped.

---

## 2026-11-13

**Did:** Scaffolded the project end to end — `audit` CLI (argparse), git
extraction (`git_extract.py`, GitPython + subprocess fallback), heuristic
layer (`heuristics.py`, two signals: message-length-vs-diff-size and
inter-commit timing), LLM judge layer (`llm_judge.py`, `claude-opus-5-5`
via `output_config.format` json_schema for structured score + reasoning),
and the Markdown report generator (`report.py`). Ran it against
`muhammadfawad538/5-Day-Remote-AI-OS-Sprint` (4 commits): heuristics-only
pass worked end to end; full pass (heuristics + LLM judge) also ran
end to end mechanically, but every LLM call came back as a 400 — see
"Failed" below.

**AI usage:** Claude Code wrote essentially all of the scaffold in this
session (modules, CLI, report renderer) from the scope in CLAUDE.md. Before
writing the LLM-judge module it loaded the `claude-api` skill rather than
guessing a model name, since training-data model IDs and SDK shapes (e.g.
`output_config.format`, the 1.x SDK surface) are stale — confirmed the
installed `anthropic` SDK is 2.8.0, well past the API shape it would have
guessed from memory.

**Failed / scrapped:**
- `.env` initially had the key stored as `ANTHROPIC-API-KEY` (hyphen) —
  silently wrong, since `os.environ.get("ANTHROPIC_API_KEY")` would have
  returned `None` with no error until the LLM layer ran. Caught by
  inspecting variable *names* in `.env` without reading the key value, and
  renamed to the underscore form CLAUDE.md specifies.
- `Docs/ai-usage-log.md` had been created by copy-pasting the write-up
  template — same content, wrong file. Replaced with an actual dated-entry
  log format before this entry was written.
- First end-to-end LLM judge run against the real test repo failed on
  every commit: `invalid_request_error — Your credit balance is too low
  to access the Anthropic API.` The code path itself worked correctly
  (the 400 was caught by the `APIStatusError` branch and recorded per-commit
  as a judge failure in the report, instead of crashing the run or silently
  dropping the commit) — this was a real-world billing gap, not a bug.
  Confirms the error-handling chain is doing its job, but the LLM layer is
  still unverified against a real successful response.

**Next:** Once API credits are available, re-run the full audit against
this repo (and at least one larger/more AI-heavy repo) to see real LLM
judge scores and reasoning, and check calibration against known AI-assisted
vs. hand-written commits.

---

## 2026-11-14

**Did:** Swapped the LLM judge layer from Anthropic to OpenAI, since the
Anthropic account's credit balance blocked yesterday's attempt and the
user had an OPENAI_API_KEY ready instead. Picked `gpt-5-nano` after
checking OpenAI's official pricing page directly — confirmed it as the
cheapest GA text model ($0.05/$0.40 per 1M tokens) per an explicit ask to
minimize token cost, rather than guessing a model name. Re-ran the full
audit (heuristics + LLM judge) against
`muhammadfawad538/5-Day-Remote-AI-OS-Sprint` end to end successfully —
first real, non-error LLM judge output this project has produced.

**AI usage:** Claude Code did the research (official OpenAI pricing page,
Responses API docs) and the full code swap. Caught its own mistake before
it reached the user: an initial web search for "OpenAI pricing 2026"
returned SEO-farm pages inventing plausible-sounding model names (e.g.
fictional-looking "GPT-6 Astra/Sol/Luna" branding); flagged that as
unreliable rather than reporting it, and went to platform.openai.com
directly instead. (The official page also listed real `gpt-6-*` models
with the same naming pattern, so the tier naming itself turned out to be
real — but the lesson holds: don't trust aggregator pricing pages over
the vendor's own docs.)

**Failed / scrapped:**
- First `gpt-5-nano` call against the real repo returned `status:
  incomplete` with no parsed output — looked like a parsing bug at first.
  Root cause (confirmed by inspecting `response.usage`): `gpt-5-nano` is a
  reasoning model that spends hidden "reasoning tokens" out of the same
  `max_output_tokens` budget before writing the visible answer — 896 of
  1024 tokens went to invisible reasoning on a test call, leaving nothing
  for the actual JSON. This is a real, non-obvious cost trap for anyone
  defaulting to a "nano"/reasoning-tier model without reading the usage
  breakdown — the sticker price per token looks cheap but hidden
  reasoning tokens are billed as output tokens at the same rate.
- Fixed by setting `reasoning: {"effort": "minimal"}`, which dropped
  reasoning tokens to 0 and cut total output tokens for an identical test
  call from 1072 to 147 (~7x). This was a strict win for this task, not a
  quality tradeoff we're still evaluating — scoring/reasoning quality on
  the test commits looked just as coherent at minimal effort.

**Next:** Watch for score drift if `reasoning.effort` turns out to matter
on harder/ambiguous commits later — current test set is only 4 commits
from one small repo, not enough to say minimal effort holds up at scale.

---

## 2026-11-14 (calibration run)

**Did:** Ran the real calibration test intent.md called for: a known
AI-heavy repo vs. a known human-only ground-truth baseline, both supplied
by the user from `C:\Users\SCS\quest\test-repos\`.
- `rubiks-cube-solver` (vibe-coded with Claude Code): full 27-commit
  history, both layers, all 27 sent to the LLM judge.
- `flask`, filtered to commits before 2015-01-01 (predates any AI coding
  assistant): 2122 commits scored by heuristics, 30 evenly sampled for
  the LLM judge to control cost.
Had to add a `--until` flag first — the CLI only supported `--since`
(commits *after* a date), with no way to bound the human-only baseline
to "before AI tools existed."

Results (`results/rubiks_report.md`, `results/flask_report.md`):
- rubiks-cube-solver: heuristic avg 52.5/100, LLM judge avg 66.3/100,
  0 of 27 commits disagreed between layers by >=30 points.
- flask (pre-2015): heuristic avg 42.8/100, LLM judge avg 47.6/100,
  11 of 30 sampled commits disagreed by >=30 points.

**Calibration verdict:** Directionally correct but weaker than hoped.
flask scored lower than rubiks-cube-solver on both layers, so the tool
isn't random — but flask's LLM-judge average (47.6) sits in the
rubric's "mostly human, light AI assistance" band, not down near 0-20
where a human-only baseline should land, and several individual
pre-2015 Flask commits still scored in the 58-72 ("substantial AI
involvement") range.

**Failed / scrapped — real calibration problems, not bugs:**
- **False positive, misattributed cause:** commit `952967fcab` (Armin
  Ronacher, Flask's actual creator, 2010) scored 72/100. The judge's own
  reasoning named the real cause: a clean docstring, a `versionadded::`
  marker, and a CHANGES entry — i.e. it read *disciplined, professional
  OSS documentation practice* as an AI-authorship signal. This is a
  direct hit on the thing this whole project is supposed to be able to
  tell apart (genuine engineering discipline vs. AI generation) and the
  tool currently can't.
- **Reasoning text contradicts its own score:** commit `06ed3e1e88` (a
  1-line typo fix, 2010) — the judge's reasoning literally says "72
  indicates substantial AI involvement is unlikely," then reports 72,
  which is squarely in the rubric's "substantial AI involvement" band.
  The written reasoning and the number it attached to that reasoning
  don't agree.
- **Score clustering:** across the 30 sampled flask commits, LLM judge
  scores repeatedly land on a small set of exact values (62 appears 8
  times, 25 four times, 28 four times, 15 twice, 42 twice, 58 twice)
  rather than spreading across the 0-100 range. Suspect this is a cost
  of `reasoning.effort: "minimal"` (flagged as a risk in yesterday's
  entry): at minimal effort the model may be pattern-matching to a
  handful of template-like verdicts instead of discriminating
  per-commit. Haven't yet re-run the same sample at a higher effort
  level to confirm — that's the natural next experiment, at a measured
  extra cost.

**Next:** Try `reasoning.effort: "low"` or `"medium"` on the same 30
flask commits and see whether the score spread widens and the Armin
Ronacher false positive corrects — that would confirm the clustering
is a minimal-effort artifact rather than a model limitation. Also worth
trying a repo known to be AI-heavy from a less "vibe-coding" context,
since rubiks-cube-solver is itself an unusually clean, well-labeled
example (explicit `CLAUDE.md`, `AI_COLLABORATION_NOTE.md` references).

---

## 2026-11-14 (effort-level A/B test)

**Did:** Ran the follow-up the previous entry queued: re-scored the
*same* 30 flask commits at `reasoning.effort: "low"`, then re-ran
`"minimal"` on the identical 30 commits too (not reusing the first
run's numbers) so the comparison would be a genuinely matched pair
rather than comparing against stale numbers. Added an `effort=` kwarg to
`score_with_llm()` and a `usage` field on `JudgeResult` to make this
testable and to capture exact token counts per call — committed, since
it's a small, generically useful addition, not just throwaway test
code. The one-off comparison script itself stayed in the scratch
directory, not the repo, since it's not part of the shipped CLI.

**Results:**
- Mean score dropped from 41.5 (matched `minimal` re-run) to 29.5
  (`low`) — a real, meaningful shift further into the "mostly human"
  band on average.
- Cost: `minimal` = 30 calls / 25,775 total tokens / ~$0.0040;
  `low` = 30 calls / 30,302 total tokens (5,760 of them hidden
  reasoning tokens vs. 0 at minimal) / ~$0.0058. Low effort costs
  ~46% more than minimal — still trivially cheap in absolute terms
  (under $0.20 per 1,000 commits either way).
- The self-contradicting commit (`06ed3e1e88`) resolved cleanly at low
  effort: score 22, reasoning "too trivial to strongly indicate AI
  generation" — consistent with the number this time. At minimal
  effort in *this* re-run it scored 60 with hedging, self-questioning
  reasoning ("leans toward substantial AI involvement? Not strongly:
  ... Therefore, score around 60") — wobbly, but not the flat
  contradiction seen in the original run (which had scored it 72).
- The Armin Ronacher false positive (`952967fcab`) did **not**
  resolve: 72 (original run) -> 68 (matched minimal re-run) -> 65
  (low). It drifted down slightly but never crossed out of the
  rubric's "substantial AI involvement" (51-80) band at any effort
  level tested. The judge's stated reason stayed the same across all
  three runs: the clean docstring, `versionadded::` marker, and CHANGES
  entry. This looks like a genuine rubric/model limitation, not
  something effort tuning fixes.

**Correction to the previous entry's hypothesis — important:** the
"score clustering" flagged last time (62 x8, 25 x4, 28 x4, ...) does
**not** reproduce as an effort-level effect. This matched re-run shows
**16 unique values out of 30 for *both* minimal and low** — identical
diversity. Re-running `minimal` itself on the same 30 commits a second
time produced mostly different scores from the first `minimal` run
(e.g. `952967fcab`: 72 -> 68; `06ed3e1e88`: 72 -> 60; several others
shifted 10-25 points). So the earlier clustering was most likely
ordinary run-to-run sampling variance in the model, not a deterministic
side effect of `reasoning.effort: "minimal"`. Worth stating plainly:
**this tool's LLM-judge scores are not fully reproducible run-to-run,
even with identical settings on identical input.** That's a real
limitation to disclose in the write-up, independent of which effort
level is used.

**Next:** Given cost is a non-issue either way, switch the default to
`"low"` for the real signal-quality improvement (resolves at least one
clear self-contradiction) — but don't oversell it: it did not fix the
Armin Ronacher false positive, and run-to-run variance means any single
comparison run could look better or worse than this one by chance. A
fairer test would average several repeated runs per effort level
rather than trusting one sample of 30 each.

---

## 2026-11-14 (switched the default)

**Did:** Changed `DEFAULT_EFFORT` in `llm_judge.py` from `"minimal"` to
`"low"`, so every future `audit` run uses `low` unless something
overrides it later. Reasoning: the A/B test above showed `low` resolves
a genuine self-contradiction (reasoning said "unlikely AI," score said
72) that `minimal` produced, and the cost difference is negligible in
absolute terms (~$0.19 vs ~$0.13 per 1,000 commits — both trivially
cheap). Did not switch anything else: `low` left the one known false
positive (the disciplined-human-commit-read-as-AI case) unresolved, so
that stays a documented, open limitation rather than something this
change claims to fix.

---

## 2026-11-14 (third test repo — a real mixed-work project)

**Did:** Ran the tool against a third repo,
`muhammadfawad538/Fawad-Act-angel` — a real client project, not a
clean "known AI-heavy" or "known human-only" calibration extreme like
the first two test repos. 132 commits total; heuristics ran on all of
them, 25 sampled for the LLM judge.

**Results:** Heuristic avg 37.5/100, LLM judge avg 54.9/100 — and the
highest layer-disagreement rate seen so far: 15 of 25 sampled commits
(60%) disagreed by >=30 points, vs. 0% on rubiks-cube-solver and ~37%
on Flask. That tracks: a repo with a real mix of quick UI tweaks, merge
commits, and some substantial AI-assisted changes is exactly the
messy middle case the two-layer design exists for, as opposed to the
two cleaner extremes tested so far.

Two concrete examples worth keeping for the write-up/demo:
- `b10369975d` ("updated", 1-word message): heuristic 35, LLM judge 75.
  The judge caught something the heuristic layer structurally can't —
  extensive inline design-rationale comments and a cohesive, template-like
  UI pattern that reads AI-influenced, under a commit message that
  undersells the change entirely.
- `f8aadede32` ("updated themes", 1-line diff): heuristic 60, LLM judge
  28 — the *heuristic* layer was arguably wrong here, not the judge. It
  scored high mostly because the commit landed 21 seconds after the
  previous one (its timing signal reads fast gaps as AI-like), but the
  diff was a one-character stray-typo fix the LLM judge correctly read
  as an ordinary human correction with a mismatched commit message.
  Useful reminder that the heuristic layer's signals are heuristics, not
  ground truth either — it can be the wrong one in a disagreement, not
  just a sanity check against the LLM.

**Next:** Good candidate repo for the Loom demo specifically because
it's messier and more realistic than the other two — the two-layer
disagreement story is more visible here than on either clean extreme.

## YYYY-MM-DD

**Did:** (what got built/changed)

**AI usage:** (what Claude drafted vs. what was hand-written/edited, and why)

**Failed / scrapped:** (name it plainly if something didn't work)

**Next:** (what's queued for next session)

-->

## 2026-11-15 — Disagreement Investigator agent + privacy fix

**Did:** Added `src/auditor/investigator.py`, a tool-using agent that runs
only on commits where the heuristic and LLM-judge layers disagree by >=30
points. Tools: `get_neighbor_commits`, `get_file_history`, `get_full_diff`,
`submit_verdict` (OpenAI Responses API function calling, gpt-5-nano, hard
cap of 6 steps). Wired into the CLI (`--investigate`,
`--max-investigations`), the report (resolved score + tool trail per
commit) and the Streamlit UI (checkbox, "Resolved (agent)" column, trail in
the commit detail). Opt-in, because it adds API calls (~2 per commit).
Planned first in plan mode and picked over a generic "chat with your repo"
box, which would look like exactly the superficial AI use this tool is
meant to catch.

**AI usage:** Claude proposed the two options (investigator vs chat panel),
I picked the investigator; Claude wrote the module and integration, I
redirected the end-to-end test to a third-party repo
(seanedwards/vibes) instead of my own.

**Results (real runs, ~$0.001 per investigation):**
- `f8aadede32` (Fawad-Act-angel): agent fetched the actual diff, found the
  stray `1` after `removeEventListener`, sided with the LLM judge (30).
  Good case: it surfaced concrete evidence.
- `b10369975d`: mostly confirmed the judge (72). Honest read: a
  confirmation, not a discovery.
- seanedwards/vibes (3 investigated): 2 sided with the judge, 1 with the
  heuristic (`5d64fc2755`, resolved 68). That last ruling's reasoning is
  soft ("not definitive") and leaned on the heuristic's 0-second-gap
  signal, which we already know can be wrong. Not a showcase example.
- On that repo many commit messages literally say "Generated with Claude
  Code", so judge and agent leaned on a declaration, not code texture.

**Failed / caught:** The first CLI run of the investigator was cancelled
and redirected by me mid-way. Separately, the generated report was
printing every commit author's email (a stranger's on vibes); removed
emails from `render_report` and stripped them from the existing
`results/*.md` files. Note: emails of earlier committed reports still
exist in git history.

**Next:** Decide whether the investigator is worth showing in the Loom
or just the verdict + legend; consider logging per-run variance of
rulings, as with the judge.
