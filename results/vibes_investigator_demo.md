# AI Usage Authenticity Report — https://github.com/seanedwards/vibes

**Verdict: Substantial AI Involvement (63.9/100)**
_Based on commit patterns and AI judge reasoning — not a certainty. See Known Limitations in directive.md / README.md before treating this as proof._

<details><summary>What do these labels mean?</summary>

| Score range | Label | Meaning |
|---|---|---|
| 0-20 | Hand-Written | Idiosyncratic style, partial/incremental edits, human-typical shortcuts or typos |
| 21-50 | Mostly Human | Possibly light AI assistance (autocomplete, a snippet), but mostly human-authored |
| 51-80 | Substantial AI Involvement | Unusually complete/consistent structure, textbook-perfect comments, or a message that reads like it was generated with the diff |
| 81-100 | Almost Certainly AI-Generated | Near-complete implementation in one commit, uniform style with no human "mess," over-engineered relative to the stated task |

</details>

Generated 2026-11-15T16:24:40
Commits analyzed: 18

## Aggregate summary

- Heuristic layer average: 59.6/100 (n=18)
- LLM judge layer average: 63.2/100 (n=10)
- Commits where the two layers disagree by >=30 points: 3
- Disagreements investigated by the agent: 3

> ⚠️ **3 commit(s) flagged for disagreement** — the blended score is less trustworthy there; see their detail sections below: `2b614ae601`, `5d64fc2755`, `e1f2d4633f`

## Per-commit detail

### `2b614ae601` — Remove run command from root Justfile
- Author: Sean Edwards — 2025-08-21T11:15:01
- Diff size: +0/-29 across 1 file(s)
- Heuristic score: **55.0/100**
  - *message_vs_diff_size* (55): Small diff (29 lines) but a disproportionately detailed message (33 words) — could be AI-authored boilerplate, but also matches careful human commit discipline.
  - *commit_timing* (55): 4.3 min after the previous commit — plausible for either a fast human pass or an AI-assisted one.
- LLM judge score: **85/100**
  - The commit removes a large, self-contained block implementing a date-prefixed run command in the Justfile. The patch itself is a straightforward, cohesive removal with no complex fixes or partial edits that would suggest mixed hand/AI authorship. The commit message explicitly states it was generated with Claude Code and even includes a Co-Authored-By line, which strongly points to AI-assisted drafting of the commit description. The actual diff matches the description (removing the entire run date block while leaving other targets like list-experiments intact). This alignment between message and diff supports substantial AI involvement in producing the commit (85).
  - Key signals: AI-generated commit note, Large block removal, Consistent diff with stated purpose, No conflicting human-only edits detected
- Resolved score (investigator): **82.0/100**
  - Heuristic and LLM layers disagree by >=30 points — treat this commit's score as uncertain.
- **Investigator ruling: 82/100** (closer layer: llm_judge)
  - The LLM judge’s assessment aligns with available project history and the current commit details: a large, self-contained removal block in Justfile, with an explicit AI-generated commit message and Co-Authored-By line. Tool outputs show: (1) neighboring commits include Claude bot-created entries around this timeframe, indicating existing AI-assisted activity in this area; (2) Justfile history reveals prior AI-influenced rewrites by claude[bot]; (3) the full diff shows removal of an entire run command block and a short, targeted List target, matching a cohesive, single-change pattern rather than scattered edits; (4) the commit message explicitly states it was generated with Claude Code. These signals collectively favor substantial AI involvement, more consistent with the LLM judge’s 85/100 assessment than the heuristic signal. Evidence: neighbor commits, file history, and the patch diff as described above.
  - Evidence: Neighbor commits: 8cf37917f0 (Sean Edwards) and c36dd64be3 (claude[bot]); 2b614ae601 is between Claude bot commits
  - Evidence: File history for Justfile shows Claude bot authored a prior rework
  - Evidence: Full diff shows removal of the entire run date block, consistent with the stated purpose
  - Evidence: Commit message includes 'Generated with Claude Code' and Co-Authored-By: Claude
  - Tool trail:
    1. `get_neighbor_commits(n=2)`
    2. `get_file_history(path=Justfile, limit=5)`
    3. `submit_verdict(score=82)`

### `8196715664` — Restructure Justfile to delegate to experiment-specific justfiles
- Author: claude[bot] — 2025-08-21T11:10:44
- Diff size: +102/-38 across 3 file(s)
- Heuristic score: **52.5/100**
  - *message_vs_diff_size* (75): Large diff (140 lines) paired with a detailed message (67 words) — consistent with AI-drafted commit messages that narrate the change in full sentences.
  - *commit_timing* (30): 59 min gap since the previous commit — consistent with normal human working pace.
- LLM judge score: **72/100**
  - The commit shows a cohesive, multi-file restructuring with consistent patterns across new Justfiles for two experiments and a centralized Justfile routing run commands by date prefix. The run command includes defensive behavior (find experiment, list available ones on failure), dependency management via asdf, and delegation to per-experiment Justfiles, which reads like a well-engineered, boilerplate-heavy solution typical of AI-assisted, template-driven work. The messages in the commit description align with a thorough, design-heavy change (delegation to experiment-specific justfiles, asdf integration, removal of monolithic commands), and the code reflects that: explicit per-experiment Justfiles, a date-based run wrapper, and explicit setup/test/build commands. This level of completeness and consistency across files suggests substantial tooling guidance or AI assistance beyond a casual human edit.

However, there are some human-like signs too (co-authored-by, PR-61 style wording, and the presence of comments and varied formatting that could come from a developer). The content is not garbled and is generally plausible for a hand-crafted change, so it’s not an extreme AI-flag. Overall, the diff reads as a substantial, well-structured refactor with strong scaffolding, leaning toward substantial AI involvement, but not absolutely definitive.)
  - Key signals: multi-file restructuring, per-experiment Justfiles, date-prefix run wrapper, asfd integration in run, defensive error handling in run, cohesive, boilerplate-like comments, uniform style across new files
- Blended score: **62.2/100**

### `7127142019` — Add .mcp.json configuration for just-mcp integration
- Author: claude[bot] — 2025-08-21T11:10:44
- Diff size: +12/-0 across 1 file(s)
- Heuristic score: **67.5/100**
  - *message_vs_diff_size* (55): Small diff (12 lines) but a disproportionately detailed message (27 words) — could be AI-authored boilerplate, but also matches careful human commit discipline.
  - *commit_timing* (80): Only 0s after the previous commit — faster than a typical manual edit-test-commit cycle.
- LLM judge: not run (sampling or `--no-llm`).

### `b777b3e6e8` — Simplify workflow by removing redundant tool setup steps
- Author: Sean Edwards — 2025-08-21T11:10:44
- Diff size: +0/-15 across 1 file(s)
- Heuristic score: **67.5/100**
  - *message_vs_diff_size* (55): Small diff (15 lines) but a disproportionately detailed message (49 words) — could be AI-authored boilerplate, but also matches careful human commit discipline.
  - *commit_timing* (80): Only 0s after the previous commit — faster than a typical manual edit-test-commit cycle.
- LLM judge score: **85/100**
  - The commit message explicitly states AI generation: “🤖 Generated with Claude Code” and a Claude co-author line. The diff itself is a clean, uniform refactor that removes multiple conditional setup steps and relies solely on asdf-vm for tool management, which is a small, self-contained change consistent with an automated or guidance-driven patch. The message and the diff are aligned: the patch implements exactly what's described (removing Rust/Ruby setup and extra dependencies, relying on .tool-versions). The highly structured, boilerplate nature of the diff (selective removals, maintaining a single install-from-.tool-versions step, no added complex logic) also supports AI-generated style.

Potential disagreement signals: none significant. There is a minor possibility of a human author using an AI-assisted template (given the deliberate structure and the explicit AI generation tag), but the strongest indicators are the explicit AI-generated tag and co-author line, which overwhelmingly point to AI involvement.

Key signals: AI-generated tag in commit message, Co-Authored-By Claude line, uniform removal of setup steps, minimal new logic, single remaining step using asdf-vm.]
  - Key signals: AI-generated tag in commit message, Co-Authored-By line, Removal of conditional tool setups, Single remaining asdf-vm install step, No new complex logic introduced
- Blended score: **76.2/100**

### `5f4ad368ae` — Add demo-specific .tool-versions and expand artifact collection
- Author: Sean Edwards — 2025-08-21T11:10:44
- Diff size: +6/-0 across 3 file(s)
- Heuristic score: **67.5/100**
  - *message_vs_diff_size* (55): Small diff (6 lines) but a disproportionately detailed message (61 words) — could be AI-authored boilerplate, but also matches careful human commit discipline.
  - *commit_timing* (80): Only 0s after the previous commit — faster than a typical manual edit-test-commit cycle.
- LLM judge: not run (sampling or `--no-llm`).

### `2b13c6f1a6` — Replace Just action with ASDF for tool management
- Author: Sean Edwards — 2025-08-21T11:10:44
- Diff size: +3/-2 across 2 file(s)
- Heuristic score: **67.5/100**
  - *message_vs_diff_size* (55): Small diff (5 lines) but a disproportionately detailed message (42 words) — could be AI-authored boilerplate, but also matches careful human commit discipline.
  - *commit_timing* (80): Only 0s after the previous commit — faster than a typical manual edit-test-commit cycle.
- LLM judge score: **72/100**
  - The diff shows a clean, cohesive refactor: replacing a setup-just step with asdf-based tool management and adding a .tool-versions file. The workflow, file addition, and version pinning are all consistent and minimal, which could be produced by a human, but several signals point to AI involvement: the commit message explicitly states the work was “Generated with Claude Code” and includes a Co-Authored-By line from Claude. The message aligns unusually well with the exact changes (e.g., replacing the step name, swapping actions, and introducing ASDF with a single tool-versions entry), suggesting an autogenerated or assisted write. The code structure is clean with defensive-looking comments/labels in the message, which is often characteristic of AI-generated blurb. However, there is no obviously wrong logic, and the changes are small and deterministic, so it’s not definitive, just leaning AI-assisted.

Key signals:
- Commit message explicitly claims AI-generated generation with Claude Code.
- Highly aligned, boilerplate-like changes (rename of step, update to asdf install action, addition of .tool-versions) resemble templates used by AI code completion.
- No visible human-style typos or inconsistent formatting; the diff is tidy and conventional.
- Co-Authored-By line referencing Claude further reinforces AI authorship cues.

Disagreement between message and diff: The message emphasizes “ASDF for tool management” and a broad workflow upgrade, which the diff confirms in a very targeted way. There is no substantial discrepancy, but the message’s provenance claim is the strongest hint toward AI involvement that isn’t derivable from the code alone.

Likelihood bands: 51-80 would be substantial AI involvement; given the explicit AI-generation tags, I assign 72.
  - Key signals: explicit AI-generation tag in commit message, consistent AI-like templating in changes, co-author line naming an AI, use of asdf-vm for tool management in a minimal, boilerplate fashion
- Blended score: **69.8/100**

### `8cf37917f0` — Add Manual Just Runner GitHub workflow
- Author: Sean Edwards — 2025-08-21T11:10:44
- Diff size: +57/-0 across 1 file(s)
- Heuristic score: **77.5/100**
  - *message_vs_diff_size* (75): Large diff (57 lines) paired with a detailed message (38 words) — consistent with AI-drafted commit messages that narrate the change in full sentences.
  - *commit_timing* (80): Only 0s after the previous commit — faster than a typical manual edit-test-commit cycle.
- LLM judge: not run (sampling or `--no-llm`).

### `c36dd64be3` — Add Justfile with comprehensive commands for test bench repository
- Author: claude[bot] — 2025-08-21T11:10:44
- Diff size: +77/-0 across 1 file(s)
- Heuristic score: **77.5/100**
  - *message_vs_diff_size* (75): Large diff (77 lines) paired with a detailed message (49 words) — consistent with AI-drafted commit messages that narrate the change in full sentences.
  - *commit_timing* (80): Only 0s after the previous commit — faster than a typical manual edit-test-commit cycle.
- LLM judge score: **72/100**
  - The commit presents a coherent, fairly feature-complete Justfile meant to orchestrate a multi-language experiment bench. The diff shows a single, self-contained addition with consistent formatting and multi-step workflows (setup, test, build, clean, run-experiment, list-experiments, create-experiment, validate, info). The commit message aligns with the changes and mentions CLAUDE.md guidelines, which the Justfile enforces (validate target, info output). The structure is polished: default help, cross-language checks (Cargo.toml for Rust, hello.rb for Ruby), dynamic experiment handling, and validation hooks. This level of completeness and style is more characteristic of AI-assisted or generated templates than typical small human edits, though a skilled developer could also author it. The message and diff align reasonably well, with no obvious mismatch. Some cues (verbose, defensive checks, broad command coverage) tilt toward higher AI involvement, but there are no obvious errors or over-engineered edge-case handling beyond the scope of the task.)
  - Key signals: comprehensive Justfile with multi-language support, uniform command structure (setup/test/build/clean/run-experiment/list-experiments), defensive scripting patterns (conditional cargo/ruby runs), validation and info commands referencing CLAUDE.md, cohesive commit message mirroring the changes
- Blended score: **74.8/100**

### `5f5a9cebd9` — Implement review feedback: add optional name argument and update documen
- Author: claude[bot] — 2025-08-21T10:11:42
- Diff size: +11/-2 across 2 file(s)
- Heuristic score: **55.0/100**
  - *message_vs_diff_size* (55): Small diff (13 lines) but a disproportionately detailed message (43 words) — could be AI-authored boilerplate, but also matches careful human commit discipline.
  - *commit_timing* (55): 2.8 min after the previous commit — plausible for either a fast human pass or an AI-assisted one.
- LLM judge: not run (sampling or `--no-llm`).

### `341bc18015` — Create Claude Code GitHub Actions demo with README and Ruby Hello World 
- Author: claude[bot] — 2025-08-21T10:11:42
- Diff size: +59/-0 across 3 file(s)
- Heuristic score: **77.5/100**
  - *message_vs_diff_size* (75): Large diff (59 lines) paired with a detailed message (62 words) — consistent with AI-drafted commit messages that narrate the change in full sentences.
  - *commit_timing* (80): Only 0s after the previous commit — faster than a typical manual edit-test-commit cycle.
- LLM judge score: **82/100**
  - The commit contains a cohesive, self-contained demo package with multiple MD files and a Ruby script. The README contents read like crafted documentation with explicit claims about AI-assisted generation, end-to-end AI workflow, and project conventions, which is characteristic of AI-generated or heavily assisted code/documentation. The structure is unusually uniform: a root README, a per-experiment folder with its own README, and a simple hello.rb. The verbose, boilerplate-like explanations (What is this?, Running the Demo, About This Demo) and the explicit assertion that AI assisted creation are typical of AI-generated content rather than a casual, incremental human edit. The commit message also explicitly references Claude Code GitHub Actions and AI demos, aligning with the diff content. There is no obvious human idiosyncrasy or inconsistent style in the diff that would contradict AI authorship, though a human could have produced it; the balance leans toward substantial AI involvement. 
  - Key signals: AI-generated style in README content, explicit statements about AI assistance, highly cohesive, boilerplate documentation, uniform project structure with minimal code complexity, co-author metadata typical of collaborative AI-assisted commits
- Blended score: **79.8/100**

### `7c7e6b2f82` — Remove Claude code review workflow
- Author: Sean Edwards — 2025-08-21T10:08:52
- Diff size: +0/-78 across 1 file(s)
- Heuristic score: **52.5/100**
  - *message_vs_diff_size* (75): Large diff (78 lines) paired with a detailed message (13 words) — consistent with AI-drafted commit messages that narrate the change in full sentences.
  - *commit_timing* (30): 30 min gap since the previous commit — consistent with normal human working pace.
- LLM judge score: **32/100**
  - The change is a simple removal of a single GitHub Actions workflow file. The diff is clean and conventional, with no AI-specific structure or unusual breadth. The commit message, however, explicitly states it was 'Generated with Claude Code' and includes a Claude co-author line, which strongly signals AI-generation in the message metadata. There is no evidence in the code diff of AI-generated boilerplate or defensive patterns; the content is a straightforward removal. The pairing suggests mild AI involvement in the commit message (not in the code), hence a modest AI-usage score. If anything, the message appears to overstate AI authorship relative to the minimal code change.

Discrepancy noted: commit message claims Claude-assisted generation, while the actual diff is a minimal, human-scale change with no AI-crafted logic or structure in the code portion.
  - Key signals: diff is a straightforward file deletion, commit message claims Claude Code generation, co-authored-by Claude present, no AI-like code patterns in the diff
- Blended score: **42.2/100**

### `bac3740393` — Update GitHub Actions workflow to skip Claude-authored PRs
- Author: Sean Edwards — 2025-08-21T09:39:17
- Diff size: +5/-5 across 1 file(s)
- Heuristic score: **42.5/100**
  - *message_vs_diff_size* (55): Small diff (10 lines) but a disproportionately detailed message (43 words) — could be AI-authored boilerplate, but also matches careful human commit discipline.
  - *commit_timing* (30): 32 min gap since the previous commit — consistent with normal human working pace.
- LLM judge: not run (sampling or `--no-llm`).

### `5d64fc2755` — Update Hello World CLI based on review feedback
- Author: claude[bot] — 2025-08-21T09:39:17
- Diff size: +2/-2 across 2 file(s)
- Heuristic score: **67.5/100**
  - *message_vs_diff_size* (55): Small diff (4 lines) but a disproportionately detailed message (32 words) — could be AI-authored boilerplate, but also matches careful human commit discipline.
  - *commit_timing* (80): Only 0s after the previous commit — faster than a typical manual edit-test-commit cycle.
- LLM judge score: **35/100**
  - The changes are small and targeted: updating a single print statement and a .gitkeep description. This is consistent with a human making a quick tweak after a review, rather than a large AI-generated rewrite. The .gitkeep description contains a deliberate misspelling ('Hell World FooBar' instead of 'Hello World FooBar'), which could reflect manual edits or a human-typed note rather than an auto-generated, perfectly polished commit. The presence of a co-author and a conventional commit structure fits human or small-team workflow. However, the diff itself is clean and minimal, which leaves room for light AI assistance, but the changes don’t exhibit the highly-engineered structure or exhaustive handling that would push the score higher.

Key signals:
- Minimal diff: only two files touched with a single-line code change and a one-line description change.
- Typo in description ('Hell World' vs 'Hello World') and odd phrasing in the commit message and .gitkeep description.
- Co-authored-by line present, common in human collaboration.
- No complex logic, error handling, or scaffolding beyond a trivial print statement update.

  - Key signals: tiny, incremental change, co-authored-by present, typo/misspelling in description, no complex logic or structure
- Resolved score (investigator): **68.0/100**
  - Heuristic and LLM layers disagree by >=30 points — treat this commit's score as uncertain.
- **Investigator ruling: 68/100** (closer layer: heuristic)
  - The commit shows a tiny, targeted change but a surprisingly verbose commit message and rapid sequencing after the prior commit, which aligns with heuristic signals of potentially AI-assisted drafting. The LLM judge notes are plausible but the diffs remain minimal (two files touched: a one-line code change and a one-line description change). The co-authored-by line suggests collaboration, not necessarily AI generation. The surrounding commit history indicates this is part of a small burst of bot-driven activity, but the actual diff content is not complex. Therefore, the heuristic cues are stronger in this case, though not definitive.
  - Evidence: Tiny diff: two files touched, a single-line code change and a one-line description change
  - Evidence: Commit message long and formal despite small change
  - Evidence: Commit timing: 0s after previous commit indicating quick iteration
  - Evidence: Co-authored-by present (Sean Edwards) suggesting collaboration rather than a large AI rewrite
  - Evidence: File history shows bot-authored commits nearby and a pattern of bot activity
  - Tool trail:
    1. `get_neighbor_commits(n=2)`
    2. `get_file_history(path=2025-08-21 Hello World CLI/src/main.rs, limit=5)`
    3. `get_file_history(path=2025-08-21 Hello World CLI/.gitkeep, limit=5)`
    4. `submit_verdict(score=68)`

### `776a6275af` — Add experiment structure and Hello World CLI
- Author: claude[bot] — 2025-08-21T09:39:17
- Diff size: +14/-0 across 4 file(s)
- Heuristic score: **67.5/100**
  - *message_vs_diff_size* (55): Small diff (14 lines) but a disproportionately detailed message (36 words) — could be AI-authored boilerplate, but also matches careful human commit discipline.
  - *commit_timing* (80): Only 0s after the previous commit — faster than a typical manual edit-test-commit cycle.
- LLM judge: not run (sampling or `--no-llm`).

### `7ca3d1c22d` — Merge pull request #2 from seanedwards/add-claude-github-actions-1755748
- Author: Sean Edwards — 2025-08-21T09:07:08
- Diff size: +142/-0 across 2 file(s)
- Heuristic score: **40.0/100**
  - *message_vs_diff_size* (25): Large diff (142 lines) with a short message (11 words) — more typical of a human committing quickly without narrating the change.
  - *commit_timing* (55): 5.7 min after the previous commit — plausible for either a fast human pass or an AI-assisted one.
- LLM judge score: **25/100**
  - The available data is extremely limited: only a merge commit message and no actual diff. The message itself is generic and boilerplate-like, describing adding a GitHub Workflow for Claude Code, which is a common human-driven DevOps task. Without the diff, there is no code structure, style, or defensive patterns to evaluate. The absence of implementation details makes it hard to infer AI-generation likelihood. The commit type (merge PR) and standard phrasing could be either human or AI-assisted, but the lack of substantive content keeps the risk assessment at a low level of confidence.

If there were a diff, I would look for: uniform AI-like patterns, exhaustive edge-case coverage, and consistent verbose comments to push toward a higher AI-generated likelihood. As-is, this reads like a routine integration task that humans commonly perform.
  - Key signals: merge commit message, no diff to inspect, generic task description
- Blended score: **32.5/100**

### `1ccaa0f7f4` — "Claude Code Review workflow"
- Author: Sean Edwards — 2025-08-21T09:01:25
- Diff size: +78/-0 across 1 file(s)
- Heuristic score: **52.5/100**
  - *message_vs_diff_size* (25): Large diff (78 lines) with a short message (4 words) — more typical of a human committing quickly without narrating the change.
  - *commit_timing* (80): Only 2s after the previous commit — faster than a typical manual edit-test-commit cycle.
- LLM judge: not run (sampling or `--no-llm`).

### `e1f2d4633f` — "Claude PR Assistant workflow"
- Author: Sean Edwards — 2025-08-21T09:01:23
- Diff size: +64/-0 across 1 file(s)
- Heuristic score: **27.5/100**
  - *message_vs_diff_size* (25): Large diff (64 lines) with a short message (4 words) — more typical of a human committing quickly without narrating the change.
  - *commit_timing* (30): 17 min gap since the previous commit — consistent with normal human working pace.
- LLM judge score: **72/100**
  - The commit adds a complete GitHub Actions workflow file for integrating Claude with PRs and issues. The file is highly structured, with many precise YAML fields, conditional triggers, permissions, and a long list of commentary-style options that resemble boilerplate templates often produced by AI design tools. The commit message is concise and generic, while the diff contains a near-fully fleshed-out workflow with sensible defaults and optional parameters, suggesting substantial tooling assistance. The thoroughness (e.g., explicit permissions, model option, trigger_phrase, assignee_trigger, allowed_tools, custom_instructions, claude_env) points toward AI-generated or AI-assisted composition.
  - Key signals: New .github/workflows/claude.yml file, Comprehensive, boilerplate-like workflow with many optional fields and comments, Use of anthropics/claude-code-action@beta with structured inputs, Explicit permissions and read-only intent for various GitHub objects, Optional commented blocks for model selection, trigger phrases, allowed tools, and custom instructions, Commit message is generic while the diff shows a highly-engineered workflow
- Resolved score (investigator): **75.0/100**
  - Heuristic and LLM layers disagree by >=30 points — treat this commit's score as uncertain.
- **Investigator ruling: 75/100** (closer layer: llm_judge)
  - The commit adds a new .github/workflows/claude.yml that is a comprehensive GitHub Actions workflow for Claude integration. The diff reveals a near-engineered, boilerplate-style workflow with many optional fields (model, trigger_phrase, assignee_trigger, allowed_tools, custom_instructions, claude_env) and explicit permissions. This level of boilerplate and configurability, along with a generic commit message, is more characteristic of AI-assisted design than a handwritten entry. Neighbor commits show a sequence of Claude-related workflow work, suggesting a pattern of tooling integration. In contrast, the heuristic layer’s short message for a large diff and decently spaced timing aligns with generic human behavior but fails to explain the highly structured, multi-option diff. Therefore, the LLMS judgment is closer to truth on AI involvement, supported by concrete diff features.
  - Evidence: Diff shows new, fully-formed claude.yml with many optional settings and comments
  - Evidence: Explicit annotations for model, trigger_phrase, assignee_trigger, allowed_tools, custom_instructions, claude_env
  - Evidence: Use of anthropics/claude-code-action@beta and secrets
  - Evidence: Commit message generic but diff is highly-engineered
  - Tool trail:
    1. `get_neighbor_commits(n=2)`
    2. `get_file_history(path=.github/workflows/claude.yml, limit=5)`
    3. `get_full_diff(path=.github/workflows/claude.yml)`
    4. `submit_verdict(score=75)`

### `84100f6717` — Initial commit: Add CLAUDE.md with project setup
- Author: Sean Edwards — 2025-08-21T08:44:10
- Diff size: +55/-0 across 1 file(s)
- Heuristic score: **57.5/100**
  - *message_vs_diff_size* (75): Large diff (55 lines) paired with a detailed message (15 words) — consistent with AI-drafted commit messages that narrate the change in full sentences.
  - *commit_timing* (40): First commit in range — no prior commit to compare timing against.
- LLM judge: not run (sampling or `--no-llm`).
