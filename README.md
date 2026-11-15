# AI Usage Authenticity Auditor

Companies are starting to hire and evaluate engineers on "genuine,
daily AI-native use" — but there's no real way to verify that claim
from the outside. A resume, a demo video, or a usage log can all be
written up convincingly after the fact.

This tool reads a git repo's actual commit history and diffs and scores
how AI-driven each commit's work looks — with **written reasoning per
commit**, not a single black-box number.

## How it works

Two scoring layers, kept separate on purpose and shown side by side:

1. **Heuristic layer** (`score_heuristics`) — free, deterministic, no
   API calls. Looks at commit timing gaps and whether the message's
   detail matches the diff's size.
2. **LLM-judge layer** (`score_with_llm`) — sends each commit's diff and
   message to an LLM (OpenAI's `gpt-5-nano` by default) with an explicit
   rubric, and gets back a 0-100 score plus a written justification that
   has to cite something specific in the diff or message.

When the two layers disagree by a wide margin, the report flags it
instead of averaging it away — that disagreement is itself a signal
worth seeing, especially on real, mixed repos rather than clean
all-AI or all-human extremes.

## Setup

```bash
git clone https://github.com/muhammadfawad538/AI-Repo-Auditor-tool.git
cd AI-Repo-Auditor-tool
python -m venv .venv
.venv\Scripts\activate        # Windows
# source .venv/bin/activate   # macOS/Linux

pip install -e .
```

Set your OpenAI key (the LLM-judge layer reads `OPENAI_API_KEY` via
`python-dotenv`):

```bash
echo OPENAI_API_KEY=sk-...> .env
```

Without a key, the tool still runs — it falls back to heuristic-only
scoring and says so plainly.

## CLI usage

```bash
audit <repo_path_or_url> [--since DATE] [--until DATE] [--sample N] [--no-llm] [--model ID] [--output FILE]
```

| Flag | What it does |
|---|---|
| `repo` | Local path or a cloneable git URL |
| `--since` | Only commits *after* this date (e.g. `2024-01-01`) |
| `--until` | Only commits *before* this date (e.g. `2015-01-01`) |
| `--sample N` | Cap the commits sent to the LLM judge to `N`, evenly sampled. Heuristics still run on every matched commit regardless — this only controls LLM cost on large repos |
| `--no-llm` | Heuristics only, skip the LLM judge entirely |
| `--model` | OpenAI model id for the judge (default: `gpt-5-nano`) |
| `--investigate` | Run the investigator agent on commits where the two layers disagree (extra API calls, about 2 per commit) |
| `--max-investigations N` | Cap on how many disagreeing commits the agent investigates (default: 5) |
| `--output` | Markdown report path (default: `report.md`) |

Example:

```bash
audit https://github.com/some-org/some-repo --sample 25 --output results/report.md
```

The report has an aggregate summary (both layers' averages, how many
commits disagreed) followed by a per-commit breakdown with full
reasoning from the LLM judge.

## Streamlit UI (optional)

A thin, one-page wrapper over the same CLI pipeline — no logic
duplicated — for demoing without a terminal.

```bash
pip install -e ".[ui]"
streamlit run app.py
```

Enter a repo path, optional since/until filters, hit **Run Audit**.
You get a sortable table (hash, message, heuristic/LLM/combined
scores, reasoning snippet, disagreement flag), a dropdown to pull up
any single commit's full reasoning, and an aggregate summary.

## Known limitations — read before trusting a score

This is a rubric-prompted LLM opinion plus cheap heuristics, not a
certainty machine, and it has real, tested limitations:

- **It can't reliably tell "AI-generated" apart from "a disciplined
  human who documents well."** A real 2010 commit by Flask's actual
  creator consistently scored 65-72/100 ("substantial AI involvement")
  because of a clean docstring and a changelog entry — not because it
  was AI-written.
- **LLM-judge scores aren't fully reproducible run-to-run.** The same
  commit, same settings, can score differently across separate runs
  (seen swings of 10-50 points in testing). The heuristic layer, being
  pure math, is always identical on the same input.
- **Calibration separation is weaker than ideal.** It correctly scores
  a known-human-only baseline lower than a known-AI-heavy repo on
  average, but the gap isn't as clean as a true verifier would want.

Full detail, the actual test numbers, and what was tried and discarded
are in [`directive.md`](directive.md) and [`Docs/ai-usage-log.md`](Docs/ai-usage-log.md).

## Project docs

- [`intent.md`](intent.md) — the problem and plan, written before the build
- [`directive.md`](directive.md) — the final approach, what changed and why
- [`Docs/ai-usage-log.md`](Docs/ai-usage-log.md) — a day-by-day log of how AI was used, including what failed
- [`Docs/write-up-template.md`](Docs/write-up-template.md) — the full write-up
- [`results/`](results) — real calibration runs against known AI-heavy, known human-only, and real mixed-work repos

## Scope

Built in a short timebox as a CLI-first tool with an optional demo UI.
No training of a custom classifier, no CI/webhook integration, no
auth or persistence — rubric-prompted LLM calls plus heuristics is the
honest scope here, and that's by design, not a shortcut.
