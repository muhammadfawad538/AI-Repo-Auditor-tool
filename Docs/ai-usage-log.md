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

<!-- Template for each entry:

## YYYY-MM-DD

**Did:** (what got built/changed)

**AI usage:** (what Claude drafted vs. what was hand-written/edited, and why)

**Failed / scrapped:** (name it plainly if something didn't work)

**Next:** (what's queued for next session)

-->
