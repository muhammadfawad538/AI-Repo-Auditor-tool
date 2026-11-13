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

<!-- Template for each entry:

## YYYY-MM-DD

**Did:** (what got built/changed)

**AI usage:** (what Claude drafted vs. what was hand-written/edited, and why)

**Failed / scrapped:** (name it plainly if something didn't work)

**Next:** (what's queued for next session)

-->
