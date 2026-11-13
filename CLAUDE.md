# CLAUDE.md — AI Usage Authenticity Auditor

## Project in one line
A tool that takes a git repo (or a slice of commit history) and scores how much
of the work was genuinely AI-driven vs. hand-written, by reading commit
patterns, diff structure, and the "texture" of the code itself — then explains
its reasoning per commit, not just a single black-box number.

## Why this project exists (context for Claude Code)
This is being built for a hiring "Quest" at MUST Company for the role
**AI Native Super Engineer**. The brief: pick one real, hard, currently-unsolved
problem, build a working solution in 5 days with AI as the primary way of
working, and document the process (what was tried, what failed, what was
unlearned). The deliverables required at the end are:

- `intent.md` — the problem + plan (written at the start)
- `directive.md` — the final approach/spec, written once the build has shaped up
- A working solution (this repo + a runnable demo)
- A write-up: the problem, what was unlearned, how AI was used, what failed
- A daily AI-usage log (`docs/ai-usage-log.md`)
- A Loom demo (≤5 min)
- A separate career-path video (≤5 min) — not part of this repo's scope

**Important meta-point:** this tool's own subject matter is "how do you tell
genuine AI-driven engineering from superficial AI use" — so the project itself
should be built in a way that would pass its own audit: visible iteration,
real failed attempts kept in the log/commits (not hidden), and a genuine,
inspectable reasoning trail from the LLM, not just a hardcoded heuristic
dressed up as "AI-powered."

## Who's building this
Muhammad Fawad — AI/agentic engineer (Python, LangChain/LangGraph, RAG, agent
systems). Comfortable with FastAPI/CLI tooling, Gradio/Streamlit for quick
demos, and calling LLM APIs directly. No need to over-explain Python basics;
do flag any assumption about API keys, costs, or rate limits before making
many LLM calls in a loop.

## Scope guardrails (keep this shippable in ~3-4 build days)
- **CLI tool first.** `audit <repo_path_or_url> [--since <date>] [--output report.md]`
  Optional minimal web UI (Streamlit/Gradio) only after the CLI works end-to-end
  — nice for the Loom demo, not required for the tool to be "working."
- **Two scoring layers, not one:**
  1. *Heuristic layer* (fast, free, no API calls): commit timing patterns,
     message style/length, diff size vs. message specificity, naming/structure
     consistency, comment density and style.
  2. *LLM judge layer*: for each commit (or a sampled subset if the repo is
     large), send the diff + commit message to an LLM with an explicit rubric
     and ask for an AI-authorship-likelihood score (0-100) **with reasoning**,
     not just a number. This is the layer that makes the tool genuinely
     AI-native rather than a disguised heuristic script — don't cut it to
     save time; cut repo size/sample count instead.
- **Combine, don't average blindly.** Show both sub-scores and the final
  blended score per commit, plus an aggregate repo-level summary. Disagreement
  between the two layers is itself useful signal — surface it, don't hide it.
- **Output must be a real artifact**, not console text only: a Markdown (or
  simple HTML) report per run, with per-commit reasoning, so it's demoable on
  a screen share.
- **Test on real repos** — including at least one that is genuinely
  AI-heavy and one that is genuinely hand-written, ideally repos the user
  already has (their own GitHub) plus 1-2 well-known open-source repos, to
  get a real sense of calibration and failure modes. Document where it's
  wrong — that honesty is part of the deliverable.

## Explicitly out of scope (don't let the build balloon)
- No training a custom classifier model. Rubric-prompted LLM calls + heuristics
  only — that's the honest scope for 5 days.
- No GitHub App / webhook / CI integration. A CLI you run against a local
  clone or repo URL is enough.
- No auth, no multi-user, no persistence/database layer.
- No polished SaaS UI. A clean CLI output + optional single-page Streamlit
  demo is the ceiling here.

## Tech defaults (override if the user says otherwise)
- Python 3.11+, `GitPython` (or raw `git log`/`git show` subprocess calls if
  GitPython is unavailable) for repo/commit extraction.
- Anthropic API (the user's own key, set via env var `ANTHROPIC_API_KEY`) for
  the LLM judge layer. Ask before assuming a specific model name — check
  what's current rather than hardcoding an old one.
- `rich` or plain Markdown for CLI report rendering.
- Keep dependencies minimal — this needs to run on a modest machine with
  no Docker.

## Working agreement for this build
1. Before writing code each session, check `docs/ai-usage-log.md` and append
   a new dated entry as work happens — don't reconstruct it from memory later.
2. When something fails or a first approach is scrapped, say so directly in
   the log and in code comments/commit messages — the write-up needs real
   "what failed" material, and sanitizing the log defeats the point of the
   quest.
3. Prefer small, real commits over one giant commit — the commit history of
   *this* repo is itself part of the demo story.
4. If a design decision changes significantly from `intent.md`, note it;
   that diff becomes part of `directive.md` at the end.
