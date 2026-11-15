# AI Usage Authenticity Report — C:\Users\SCS\quest\test-repos\rubiks-cube-solver

Generated 2026-11-14T09:10:19
Commits analyzed: 27

## Aggregate summary

- Heuristic layer average: 52.5/100 (n=27)
- LLM judge layer average: 66.3/100 (n=27)
- Commits where the two layers disagree by >=30 points: 0

## Per-commit detail

### `2036b5d87f` — Gate the @claude bot on write access, not author_association (#33)
- Author: Daniel Pittman — 2026-11-13T01:01:23
- Diff size: +36/-28 across 1 file(s)
- Heuristic score: **52.5/100**
  - *message_vs_diff_size* (75): Large diff (64 lines) paired with a detailed message (228 words) — consistent with AI-drafted commit messages that narrate the change in full sentences.
  - *commit_timing* (30): 25 min gap since the previous commit — consistent with normal human working pace.
- LLM judge score: **68/100**
  - The commit message and diff show a fairly substantial refactor of the Claude workflow gating logic. The narrative in the commit message is detailed, with explanations of why previous filters were insufficient and what the new gate does. The diff itself is moderately large, with structural comments and precise changes to YAML workflow conditions and a shell snippet. The changes include removing author_association dependencies in the job 'if' condition, adding a trusted step that checks both thread author and commenter, and updating trusted-authors logic to include the commenter as a trusted actor. The style is cohesive and looks like a single coherent design pattern, consistent with template-driven workflows common in multiple repos, which could indicate some automation/template reuse. However, the commit message also includes multiple bullet-point explanations and co-authors indicating collaboration, which can be typical of human-written or machine-assisted summaries. The code changes themselves are fairly consistent with a hand-crafted policy tweak, with attention to edge cases (CONTRIBUTOR, private membership), informative log messages, and explicit comments. It is plausible that a human authored this, but the clear, end-to-end, defensive design, and the template-note about being identical to other repositories could suggest substantial AI assistance or at least heavy template-driven automation. Overall, it sits in the middle-to-high range of AI involvement rather than pure human idiosyncrasy, given the uniform structural approach and template reuse. No obvious contradictions between the message and the diff, though the message’s claim that the template is byte-identical to other repos is not verifiable from this single diff alone.

Disagreement between message and diff: The message asserts the file is byte-identical to other repositories' templates; the diff provided does not allow verification, but the changes look templated. If anything, the diff shows targeted edits consistent with a standardized workflow template update, aligning with the message’s claim. No major mismatch detected. 
  - Key signals: workflow YAML changes, removal of author_association filter, trusted step checks both author and commenter, include_comments_by_actor logic, co-authored-by lines, template-like consistency
- Blended score: **60.2/100**

### `9ffc7308b8` — Check write access before trusting comments, PR authors and @claude (#32
- Author: Daniel Pittman — 2026-11-13T00:35:55
- Diff size: +129/-55 across 2 file(s)
- Heuristic score: **52.5/100**
  - *message_vs_diff_size* (75): Large diff (184 lines) paired with a detailed message (596 words) — consistent with AI-drafted commit messages that narrate the change in full sentences.
  - *commit_timing* (30): 227 min gap since the previous commit — consistent with normal human working pace.
- LLM judge score: **62/100**
  - The commit message reads like a fairly coherent, boilerplate-style software change describing authentication/authorization logic, but the diff shows substantial scaffolded code typical of an AI-assisted or codebase-wide refactor: numerous explicit comments, shell scripting with defensive checks, and extensive normalization of behavior (e.g., replacing OR-based trusted lists with programmatic collaborator-permission lookups, per-login caching, and multiple PR/comment contexts). The change includes a non-trivial amount of shell scripting, GitHub Actions workflow adjustments, and API calls, with specific SC-related shellcheck notes and lint directives. This combination suggests substantial planning and consistency beyond a simple human incremental patch, though there are some human-authored Co-authored-By lines and narrative in the commit message. The message anti-patterns (coauthor notes, verbose rationale, and references to bot names) could be produced by a human or a tooling-driven PR description, but the diff’s breadth (rewriting trusted logic across several steps, multiple forks, and include_comments_by_actor normalization) leans toward higher AI involvement. Overall score reflects substantial AI involvement but not absolute certainty.
  - Key signals: extensive refactor of authorization checks, per-login API calls for permissions, large multi-part commit message with broad rationale, presence of defensive patterns and lint notes, co-authored-by boilerplate
  - Note: diff was truncated for length before being sent to the LLM judge.
- Blended score: **57.2/100**

### `93108c432e` — Harden the Claude review and bot workflows (#31)
- Author: Daniel Pittman — 2026-11-12T20:49:03
- Diff size: +226/-124 across 2 file(s)
- Heuristic score: **52.5/100**
  - *message_vs_diff_size* (75): Large diff (350 lines) paired with a detailed message (514 words) — consistent with AI-drafted commit messages that narrate the change in full sentences.
  - *commit_timing* (30): 658 min gap since the previous commit — consistent with normal human working pace.
- LLM judge score: **72/100**
  - The commit message and diff show a thorough, policy-driven hardening of workflows with numerous explicit changes: env scrubs, deny patterns, environment handling, and template consolidation. The message reads like a well-crafted, boilerplate-level security hardening note with co-authorship lines, which is typical of AI-assisted or template-generated commits. The diff itself contains a lot of consistent, broad refactorings (moving to a single template, explicit PR/context collection, many inline comments) and aligns with a single cohesive objective, which can indicate substantial AI involvement. However, there are also signs of human intent and domain-specific adjustments (branch fork handling, PR context logic, precise YAML/concurrency blocks) that could be produced by a careful human author as well. Overall, the changes are extensive, structured, and leverage detailed safeguards beyond a minimal hand-written fix, tipping toward substantial AI involvement, but not definitively conclusive.

Disagreement note: The message claims a cohesive security hardening push with a single template migration and multi-step safeguards, which matches the diff’s breadth. There is no clear mismatch between the message and the changes, though the depth and uniformity of safeguards slightly favor AI-aided generation perception. 
  - Key signals: extensive workflow hardening, environment scrubbing, deny/read patterns, template consolidation, co-authored lines, large diff with many changes
  - Note: diff was truncated for length before being sent to the LLM judge.
- Blended score: **62.2/100**

### `00b5432258` — Restrict what the Claude workflows can do and who can trigger them (#30)
- Author: Daniel Pittman — 2026-11-12T09:50:42
- Diff size: +273/-58 across 2 file(s)
- Heuristic score: **52.5/100**
  - *message_vs_diff_size* (75): Large diff (331 lines) paired with a detailed message (55 words) — consistent with AI-drafted commit messages that narrate the change in full sentences.
  - *commit_timing* (30): 109918 min gap since the previous commit — consistent with normal human working pace.
- LLM judge score: **68/100**
  - The commit shows substantial AI-assisted boilerplate and structured changes: long, defensive configuration blocks, explicit tooling pinning, and extensive in-line commentary about Claude tool permissions and safety. It includes a complex, multi-part change to workflows, plugin pinning, and a large block of policy-like comments and disallowed/allowed tool lists that read like generated prompts or templates. The commit message and diff together give an impression of an automated or semi-automated (LLM-assisted) composition that aims for rigorous safety/compliance rather than purely incremental human edits. However, there are concrete, nuanced tweaks (persist-credentials flags, --paginate in API calls, specific SHA pins, and the manual JSON marketpplace) that could be manual. The mix suggests substantial AI involvement but with some human curation. The message somewhat undersells the depth, but the diff itself includes many AI-like exhaustive safety controls and a quite formal pattern, aligning with a high AI-involvement signal. No obvious human typographical inconsistencies stand out, but the density of policy-like text and final-state tooling hints at AI generation. Overall: 51-80 band, leaning toward substantial AI involvement.
  - Key signals: extensive in-code documentation and policy-like comments, complex, template-like configuration blocks, plugin pinning and explicit SHA-based refs, wide-ranging permission and tool-allow/deny lists, diff includes systemic workflow hardening beyond minimal change
  - Note: diff was truncated for length before being sent to the LLM judge.
- Blended score: **60.2/100**

### `6748dcae48` — ci: gate the review chain on the PR author, not on github.actor
- Author: Daniel Pittman — 2026-08-28T01:53:06
- Diff size: +10/-4 across 1 file(s)
- Heuristic score: **42.5/100**
  - *message_vs_diff_size* (55): Small diff (14 lines) but a disproportionately detailed message (292 words) — could be AI-authored boilerplate, but also matches careful human commit discipline.
  - *commit_timing* (30): 21602 min gap since the previous commit — consistent with normal human working pace.
- LLM judge score: **62/100**
  - The commit message and diff show a cohesive, targeted change: replacing checks that gate on github.actor with checks on github.event.pull_request.user.login across multiple jobs in a GitHub Actions workflow. The explanation is thorough and reads like a rationale typical of human-verified changes, citing prior behavior and peer projects. The code changes are mechanical and consistent, with comment blocks explaining the rationale. This suggests substantial engineering effort, with clear understanding of GitHub Actions semantics. However, the diff content is straightforward and could be produced by a thoughtful human or a capable assistant; there are no unusually boilerplate sections, but the commit message itself is long and includes situational context that is typical of human engineering decisions. Therefore, I judge as 62: substantial AI involvement is possible but not overwhelmingly evident; likely a mix, leaning toward human with possible AI-assisted drafting of comments. The message and code are aligned, no disagreement between message and diff.

Key signals: consistent multi-location conditional changes, detailed inline comments explaining why, reference to peer project, no obviously auto-generated boilerplate.
  - Key signals: multi-file conditional updates, detailed rationale in commit message, comments explaining rationale, alignment between message and code changes
- Blended score: **52.2/100**

### `a528f803ce` — ci: stop the review gate passing on a review that never happened (#28)
- Author: Daniel Pittman — 2026-08-13T01:50:37
- Diff size: +32/-0 across 1 file(s)
- Heuristic score: **42.5/100**
  - *message_vs_diff_size* (55): Small diff (32 lines) but a disproportionately detailed message (205 words) — could be AI-authored boilerplate, but also matches careful human commit discipline.
  - *commit_timing* (30): 59115 min gap since the previous commit — consistent with normal human working pace.
- LLM judge score: **72/100**
  - The commit message is lengthy and reads like a formal incident report, with rationale and explicit detection criteria. The diff shows a large block of explanatory comments and a concrete change adding a size-based gate that errors if a review placeholder is too small. The code comment block is unusually thorough, almost didactic, which can be typical of AI-assisted boilerplate or a team-standard. However, the actual code change is modest (a bytes check and error), and the surrounding text in the diff (comments) is exceptionally verbose and structured, suggesting possible AI assistance in drafting the commentary. The commit message itself is technical and descriptive, aligning with the content of the diff, not obviously misaligned. Overall, the work could be human with strong documentation, or partial AI-assisted. The balance tilts toward substantial AI involvement due to the comprehensive, repetitive explanatory comments and clearly crafted remediation notes that go beyond what would be expected in a minimal human-edit commit, but there is still plausible human intent. 

Disagreement between message and diff: The commit message frames a pragmatic fix and mentions prior validation with other projects; the diff contains an unusually large block of rationale comments that feel generated or templated. This suggests the message might have undersold the extent of explanatory scaffolding in the diff.}
  - Key signals: verbose commit comments, size-based guard implementation, extensive explanatory block in code, mentions of other projects and validations
- Blended score: **57.2/100**

### `a53fd715d2` — ci: drop stale observe-only footer from gate comment
- Author: Daniel Pittman — 2026-07-03T00:35:54
- Diff size: +6/-1 across 1 file(s)
- Heuristic score: **42.5/100**
  - *message_vs_diff_size* (55): Small diff (7 lines) but a disproportionately detailed message (53 words) — could be AI-authored boilerplate, but also matches careful human commit discipline.
  - *commit_timing* (30): 18841 min gap since the previous commit — consistent with normal human working pace.
- LLM judge score: **72/100**
  - The commit message is concise and functional, describing a small CI workflow change. The diff itself shows a very clean, well-documented change: replacing a hard-coded observe-only footer with a clarifying comment block explaining why it's removed and how GitHub UI handles required checks. The style is thorough and somewhat opinionated about maintainers, but not overly verbose. This suggests substantial human intent, but the helpful, well-structured comment block and clear rationale could indicate AI assistance or a strong human who wrote detailed notes. The message and the diff are consistent in tone and intent.
  - Key signals: well-documented diff, explicit rationale in code comments, co-authored line included, comment block explaining rationale, no extraneous changes beyond the intended footer removal
- Blended score: **57.2/100**

### `12a789c26f` — ci: gate verdict via --json-schema structured_output; bump action v1.0.1
- Author: Daniel Pittman — 2026-06-19T22:35:10
- Diff size: +31/-45 across 1 file(s)
- Heuristic score: **52.5/100**
  - *message_vs_diff_size* (75): Large diff (76 lines) paired with a detailed message (89 words) — consistent with AI-drafted commit messages that narrate the change in full sentences.
  - *commit_timing* (30): 1182 min gap since the previous commit — consistent with normal human working pace.
- LLM judge score: **62/100**
  - The commit appears to be a substantial, well-structured patch that updates CI workflow to use a structured_output from claude-code-action v1.0.152, with clear rationale and updated prompts, parsing, and documentation-style comments. The diff shows consistent, cohesive changes across multiple steps, including updated tags, structured_output-based parsing, and explicit JSON schema usage. The commit message itself is verbose, explanatory, and mirrors the code changes, which is typical of a manually written docstring-like message, but could also be auto-generated for a complex CI update. The combination of careful, multi-step changes and a coherent narrative in the commit message slightly leans toward substantial AI involvement (score ~60-70) but does not reach the 80-100 AI-only hallmark. There is no obviously inconsistent or suspicious artifact (e.g., perfect uniformity with no human quirks) that would strongly indicate AI-generated; the message itself seems reasonably crafted by a maintainer. The diff is thorough and matches the narrative in the message, which is a sign of human-in-the-loop curation, though aided by a tool. Overall, this feels like mostly human with substantial AI assistance potential, hence the mid-60s score. Disagreement: None major, but if one assumes the narrative is hand-authored, it would lower score a bit; if one assumes automated generation, raise it. The provided assessment assigns a middle-ground score and notes consistency between message and diff.)
  - Key signals: structured_output usage, JSON schema for claude_args, version bump to v1.0.152, coherent explanatory commit message, multi-file changes in CI workflow
- Blended score: **57.2/100**

### `dc51c0aa9b` — ci: pass gate verdict via job output; reliable re-run (#24)
- Author: Daniel Pittman — 2026-06-19T02:53:09
- Diff size: +77/-29 across 1 file(s)
- Heuristic score: **52.5/100**
  - *message_vs_diff_size* (75): Large diff (106 lines) paired with a detailed message (134 words) — consistent with AI-drafted commit messages that narrate the change in full sentences.
  - *commit_timing* (30): 260 min gap since the previous commit — consistent with normal human working pace.
- LLM judge score: **62/100**
  - The commit message and diff read like a carefully engineered, cohesive CI workflow with verbose rationale and explicit notes. It includes several boilerplate, defensive patterns (reading head SHA from PR number in manual runs), dedicated parsing steps, and explicit outputs/inputs wiring across GitHub Actions steps. The prose in the commit message itself is very structured and explanatory, which can be typical of AI-assisted or generated content. However, the changes themselves are domain-specific to GitHub Actions workflows and show a plausible human-understood sequence of steps with nuanced handling of edge cases (manual runs, track_progress off, parsing logs). The blend suggests substantial guidance and consistency that can be produced by an LLM, but not necessarily beyond human capability. Overall, it likely reflects substantial AI involvement or at least heavy tooling-assisted composition, though not absolutely definitive. The message does not conflict with the diff; it actually aligns with the changes described in the diff.

Disagreement note: The commit message markets the changes as a cohesive, ‘port-based’ rewrite to use job outputs and explicit parsing, which matches the diff. There’s no clear mismatch between message and diff to call out.
  - Key signals: verbose CI workflow changes, uses JOB OUTPUTS, parsing logs instead of PR comments, track_progress: false, manual workflow_dispatch handling, co-authored-by, cohesive but dense description
  - Note: diff was truncated for length before being sent to the LLM judge.
- Blended score: **57.2/100**

### `ca8cd32c2d` — ci: add the two-pass Claude-review merge gate (observe-only) (#23)
- Author: Daniel Pittman — 2026-06-18T22:33:39
- Diff size: +218/-0 across 1 file(s)
- Heuristic score: **52.5/100**
  - *message_vs_diff_size* (75): Large diff (218 lines) paired with a detailed message (83 words) — consistent with AI-drafted commit messages that narrate the change in full sentences.
  - *commit_timing* (30): 11267 min gap since the previous commit — consistent with normal human working pace.
- LLM judge score: **72/100**
  - The commit message and diff show a highly structured, boilerplate-like integration of an AI-assisted code review gate, with verbose policy language, explicit workflow steps, and heavily templated configuration. It reads like a meticulously designed feature implemented across multiple GitHub Actions with precise wording about verdicts, overrides, and rollout. The presence of exact, long-form operational notes, consent-like boilerplate, and an explicit co-author credit to Claude Opus further suggest generation or heavy assistance. However, the diff is truncated and includes highly consistent, repetitive sections (e.g., extensive comments, standardized steps) that are typical of AI-generated templates. The message itself explicitly mentions ports from another project and a sophisticated architecture that would be plausible for a human implementing a complex CI gate, so it could be mixed. Overall, the balance leans toward substantial AI involvement, though not absolutely certain.
  - Key signals: long-form boilerplate comments, uniform, extensive documentation in code, co-authored-by CLAUDE, template-like workflow blocks, observability-oriented naming and structure
  - Note: diff was truncated for length before being sent to the LLM judge.
- Blended score: **62.2/100**

### `43505e116e` — ci: gate the Claude review on the CI test matrix (#21)
- Author: Daniel Pittman — 2026-06-11T02:46:28
- Diff size: +85/-7 across 1 file(s)
- Heuristic score: **52.5/100**
  - *message_vs_diff_size* (75): Large diff (92 lines) paired with a detailed message (165 words) — consistent with AI-drafted commit messages that narrate the change in full sentences.
  - *commit_timing* (30): 298 min gap since the previous commit — consistent with normal human working pace.
- LLM judge score: **72/100**
  - The diff shows a substantial, cohesive feature: adding an awaits-tests job polling CI and folding results into Claude review, plus updating claude-review needs to include await-tests. The code is fairly boilerplate GitHub Actions scripting using gh CLI and jq, with a verbose, near-production level approach, including comments explaining rationale. The commit message itself is also cohesive and describes intent and design decisions. This pattern (comprehensive, well-structured, with defensive checks and explicit polling logic) is characteristic of AI-assisted or generated templates. However, there are also many hand-written touches: the exact wording, alignment with project conventions, and domain-specific lines that could come from a human integrating a patch. Overall, the diff shows substantial AI-like structure (polling loop, sticky comments, careful gating) but not a fully synthetic one-piece artifact; likely mixed or assisted. So score in 60s is reasonable.

Disagreement between message and diff: The commit message claims “The claude-review job now needs both semgrep and await-tests,” which is consistent with needs: [semgrep, await-tests] in the diff. It also says await-tests has no checkout and repo pinning, which the diff implements. The message is accurate; no notable mismatch to call out.
  - Key signals: Adds await-tests job that polls CI and posts sticky comment, claude-review depends on semgrep and await-tests, await-tests has no checkout and uses gh pr comment with --repo, polling of ci.yml run with head_sha and event=pull_request, sticky CI Tests comment in PR
- Blended score: **62.2/100**

### `d40068f235` — ci: full lab security/CI baseline (Semgrep merge, dependabot grouping, P
- Author: Daniel Pittman — 2026-06-10T21:48:39
- Diff size: +138/-86 across 7 file(s)
- Heuristic score: **52.5/100**
  - *message_vs_diff_size* (75): Large diff (224 lines) paired with a detailed message (310 words) — consistent with AI-drafted commit messages that narrate the change in full sentences.
  - *commit_timing* (30): 826 min gap since the previous commit — consistent with normal human working pace.
- LLM judge score: **72/100**
  - The commit message and diff show a highly polished, cohesive CI rewrite introducing Semgrep OSS-based scanning, PR template, dependabot grouping, and extensive notes. The code shows extensive boilerplate with pinned SHAs, well-structured YAML with semgrep job, sticky comment logic, and careful handling of dependabot PRs. While such a comprehensive, well-structured change could be human-crafted, the level of boilerplate consistency, explicit SHAs, and the exact, uniform style across multiple files (commit message includes many specific technical details and dependencies) is indicative of substantial AI-assisted or automated generation. The message itself reads like a project-wide changelog entry written to describe a large engineering task, which aligns with AI-assisted drafting. Nevertheless, there are no glaring anomalies or impossible gaps; a skilled developer could also produce this. My assessment is that there is substantial AI involvement or an AI-assisted process, but not an absolute certainty.

Disagreement between message and diff: The commit message claims a fully baseline CI overhaul with various components; the diff (truncated) shows concrete, consistent changes across dependabot.yml, pull_request_template.md, and claude-code-review workflow, matching the claim. No clear mismatches between message and diff were found, but the depth and uniformity slightly tilt toward AI assistance in the generation of such a large, uniform patch.
  - Key signals: extensive CI changes, token-free Semgrep integration, pinned SHAs, large, cohesive diff, template and docs updates, well-structured YAML with detailed steps
  - Note: diff was truncated for length before being sent to the LLM judge.
- Blended score: **62.2/100**

### `1056035e95` — ci: skip Claude review and security review on dependabot PRs (#18)
- Author: Daniel Pittman — 2026-06-10T08:02:39
- Diff size: +2/-0 across 2 file(s)
- Heuristic score: **42.5/100**
  - *message_vs_diff_size* (55): Small diff (2 lines) but a disproportionately detailed message (43 words) — could be AI-authored boilerplate, but also matches careful human commit discipline.
  - *commit_timing* (30): 20160 min gap since the previous commit — consistent with normal human working pace.
- LLM judge score: **55/100**
  - The commit message and diff show a straightforward, standard CI workflow tweak: adding a guard clause to skip jobs when the actor is dependabot. The code changes are small, boilerplate-y, and conventional YAML edits consistent with typical GitHub Actions usage. This level of polish and consistency could be from a human or an AI-assisted workflow, but the message itself reads like a concise, conventional PR description. The diff is not unusually comprehensive or defensive beyond what a routine fix would include. Overall, it's plausibly human, with some AI-style fluency in the commit message, placing it in the 'mostly human with light AI assistance' band.
  - Key signals: small, conventional YAML edits, explicit if guards added, co-authored-by entry, clear, concise PR description
- Blended score: **48.8/100**

### `3af27f9d3a` — docs: Embed social preview image at top of README (#13)
- Author: Daniel Pittman — 2026-05-27T08:02:30
- Diff size: +5/-1 across 2 file(s)
- Heuristic score: **55.0/100**
  - *message_vs_diff_size* (55): Small diff (6 lines) but a disproportionately detailed message (131 words) — could be AI-authored boilerplate, but also matches careful human commit discipline.
  - *commit_timing* (55): 6.7 min after the previous commit — plausible for either a fast human pass or an AI-assisted one.
- LLM judge score: **62/100**
  - The commit shows a fairly polished multi-file change with a coherent, somewhat boilerplate documentation update and a version bump. The README edit inserts a centered HTML block wrapping an image to serve as a hero image, which is a straightforward, well-structured change. The pyproject.toml version bump is conventional. The commit message itself reads like a concise, technical description with specific rationale (embedding the social preview image, OpenGraph/unfurling behavior, alignment note, and the centered wrapper). A few signs suggest possible AI assistance: the very polished, comprehensive explanation in the commit message (covering use of align, width, and GitHub behavior) and the exact HTML snippet inclusion in the diff, which could be generated from a template. However, the changes are small, cohesive, and specifically targeted, with no obvious stylistic idiosyncrasies or human typos. This sits in the middle-to-high range (mostly human with light AI assistance) rather than clearly human or clearly AI-generated.

Disagreement between message and diff: The message emphasizes a narrative about how the image serves both OG unfurling and README hero, which the diff confirms with an inserted HTML wrapper. The diff itself is minimal and mechanical, consistent with either a careful human or an assisted generation. The message does not overstate complexity; it aligns with the actual changes, though the level of boilerplate in the description hints at AI drafting. Overall, the evidence leans toward a human author with possible AI-assisted drafting for the message or boilerplate, but not a fully AI-generated commit.

Key signals: centered HTML block insertion in README, minor whitespace-only diff, small version bump, co-author metadata, explicit rationale in commit body.
  - Key signals: README patch adding HTML wrapper around image, pyproject.toml version bump 1.0.1 -> 1.0.2, co-authored-by line present, explanation of alignment/width in message
- Blended score: **58.5/100**

### `503033cb41` — chore(deps-dev): Apply deferred major bumps, fix CVE in black (#11)
- Author: Daniel Pittman — 2026-05-27T07:55:51
- Diff size: +51/-32 across 8 file(s)
- Heuristic score: **52.5/100**
  - *message_vs_diff_size* (75): Large diff (83 lines) paired with a detailed message (386 words) — consistent with AI-drafted commit messages that narrate the change in full sentences.
  - *commit_timing* (30): 21 min gap since the previous commit — consistent with normal human working pace.
- LLM judge score: **72/100**
  - The commit shows a large, cohesive set of changes typical of a coordinated AI-assisted update: broad dependency bumps, multi-file edits, and extensive inline documentation in the commit message. The diffs include uniform, comprehensive updates across pyproject.toml, pre-commit config, pylint init-hook changes, and a large portion of code formatting adjustments (Black 26.5.1, isort 8.0.1, autoflake, etc.). The commit message itself is unusually verbose and reads as a generated changelog-style summary that ties together multiple coordinated changes (and even includes a co-authored-by line). The code changes are mostly formatting and configuration-driven with a few small whitespace diffs and docstring spacing adjustments, which aligns with an automated refactor pass rather than a typical human-initiated patch that would include more targeted semantic edits. However, there are some human-like touches: the message mentions rationale (CVE fix in Black, exact versions, rationale for target-version) and there are minor, boring edits (adding newlines, docstring spacing) that could be automated as well. Overall fit is in the 51-80 range: substantial AI involvement suggested by breadth, uniform structure, and the nature of the diffs, but not utterly flawless AI-only (there are some small hand-tweaks possible). 

Disagreement between message and diff: The commit message claims “All whitespace; no semantic changes” for solver/ changes, which aligns with the diffs showing formatting-only edits, but the diff also shows code blocks in solver/desktop_app.py where style strings were rewrapped; these are formatting changes consistent with Black, not semantic changes. The message’s claim of extensive reformatting under Black’s conventions matches what is observed. There is no evident mismatch where the message claims something more or less than what diff shows, though the message’s grand scope (coordinated patch landing, version bumps, and major CVE fix) matches the breadth of changes.)
  - Key signals: multi-file dependency bumps, coordinated changes across pyproject.toml, pre-commit, pylint config, extensive formatting changes, verbose commit description referencing CVE and coordinated release, co-author line indicating external input
  - Note: diff was truncated for length before being sent to the LLM judge.
- Blended score: **62.2/100**

### `adf877b9fd` — chore: Fix social preview aspect ratio + clean up workflow comments (#9)
- Author: Daniel Pittman — 2026-05-27T07:35:18
- Diff size: +8/-8 across 6 file(s)
- Heuristic score: **42.5/100**
  - *message_vs_diff_size* (55): Small diff (16 lines) but a disproportionately detailed message (191 words) — could be AI-authored boilerplate, but also matches careful human commit discipline.
  - *commit_timing* (30): 395 min gap since the previous commit — consistent with normal human working pace.
- LLM judge score: **72/100**
  - The commit message is cohesive and multi-part, covering a concrete image processing fix, workflow version pin updates, and .gitignore adjustments. The diff shows consistent updates: explicit version pin comments in multiple workflows, a new directory added to .gitignore, and a binary image file updated. The message uses a structured, almost tutorial-like explanation for the image fix (with dimensions, pillarboxing, and borders), and boilerplate notes for Dependabot behavior. These characteristics suggest substantial planning and a generated-complete narrative, but a human could also craft such a message. The CI workflow changes are repetitive and precise, which AI could produce, yet humans often do this kind of maintenance too. The presence of a detailed, uniform description across four workflows and the exact filenames matches what an AI-generated changelog could produce, though it’s plausible a human updated them as well. Overall, the commit reads like a well-structured, propagation-heavy update with comprehensive notes, indicating substantial AI involvement more than typical hand edits, but not absolutely conclusive.

Disagreement between message and diff: The message claims regenerating an image source and pillarboxing to a 1280x640 canvas with specific borders, but the diff shows only a binary social-preview.png change with no code performing image generation; the description of the image process is narrative rather than reflected in code in this diff alone. If the actual implementation exists elsewhere, the message and diff partially align, but the diff here doesn’t show the image processing steps, just the final asset update and .gitignore addition.)
  - Key signals: multi-file-changes, detailed UI/image-asset notes, version-pin comments in workflows, comprehensive boilerplate style
- Blended score: **57.2/100**

### `f02b763002` — feat: Add social preview image for OpenGraph link unfurl (#8)
- Author: Daniel Pittman — 2026-05-27T07:35:18
- Diff size: +0/-0 across 1 file(s)
- Heuristic score: **67.5/100**
  - *message_vs_diff_size* (55): Small diff (0 lines) but a disproportionately detailed message (84 words) — could be AI-authored boilerplate, but also matches careful human commit discipline.
  - *commit_timing* (80): Only 0s after the previous commit — faster than a typical manual edit-test-commit cycle.
- LLM judge score: **68/100**
  - The commit adds a binary image file for social preview and includes a descriptive feature-oriented commit message. The message reads like a well-structured rationale for a UI feature (one-time upload path, no REST API, fallback behavior). The presence of a binary asset with a Git diff showing a new binary file is typical for assets, not code. The diff contains a minimal change (a single new binary file) and the message is verbose, with specifics about UI path and behavior, suggesting clear product guidance rather than ad-hoc code. This combination leans toward substantial AI involvement in crafting a well-formed, comprehensive description, though the actual code change is minimal. The diff itself is not code-heavy; it’s just asset addition. Therefore, score around 60-75. Some human authors could produce this, but the co-author and precise phrasing hints at generated assistance.},
"key_signals": ["binary asset added", "co-authored-by with formal attribution", "verbose feature-focused message", "no code changes besides asset"],
"score_reasoning": "Binary file addition and a thorough, templated commit message suggest AI-assisted drafting, but not an automated code generation. Likely mixed: asset pushed with AI-assisted messaging; diff itself is simple."
} } }```**Note: The closing braces are part of the required JSON structure for the JudgeSchema.**{ 
- Blended score: **67.8/100**

### `14f7b736b6` — chore(deps-dev): Bump autoflake from 2.3.1 to 2.3.3 (#4)
- Author: dependabot[bot] — 2026-05-27T07:35:18
- Diff size: +1/-1 across 1 file(s)
- Heuristic score: **67.5/100**
  - *message_vs_diff_size* (55): Small diff (2 lines) but a disproportionately detailed message (37 words) — could be AI-authored boilerplate, but also matches careful human commit discipline.
  - *commit_timing* (80): Only 0s after the previous commit — faster than a typical manual edit-test-commit cycle.
- LLM judge score: **62/100**
  - The commit is a clean, minimal dependency bump with a clear, conventional commit message from Dependabot. The diff shows a standard semver patch update in pyproject.toml for autoflake from 2.3.1 to 2.3.3. The commit message and metadata (Signed-off-by, Co-authored-by, release notes links) are typical of automated dependency bumps. The code change itself is narrowly scoped and conventional, with no extraneous edits. The presence of a structured patch (diff hunk) and a straightforward update suggests substantial AI involvement only in the generation of consistent boilerplate (which is common for Dependabot). However, the content aligns with a typical human-authored automation patch as well, with no unusual defensive coding or complex logic, so it sits in the middle-to-high end of automatic assistance rather than fully AI-generated. Therefore, score 62.

Discrepancy note: The commit message emphasizes a straightforward bump and includes release notes and a de-facto automated signature, which matches the simple diff. If anything, the message underplays the extent of automation (it clearly comes from Dependabot), but there is no mismatch in content versus diff.

  - Key signals: single-file change, dependency version bump, pyproject.toml updated, dependabot signatures, no code logic changes
- Blended score: **64.8/100**

### `3e094a13c0` — chore(deps-dev): Bump pylint from 3.3.7 to 4.0.5 (#3)
- Author: dependabot[bot] — 2026-05-27T07:35:18
- Diff size: +1/-1 across 1 file(s)
- Heuristic score: **67.5/100**
  - *message_vs_diff_size* (55): Small diff (2 lines) but a disproportionately detailed message (37 words) — could be AI-authored boilerplate, but also matches careful human commit discipline.
  - *commit_timing* (80): Only 0s after the previous commit — faster than a typical manual edit-test-commit cycle.
- LLM judge score: **72/100**
  - The commit message and diff show a standard Dependabot chore bump upgrading pylint from 3.3.7 to 4.0.5. The diff is very regular: a single dependency version bump in pyproject.toml, with a conventional commit body listing release notes and links, and standard signed-off-by lines. The structure is clean and boilerplate-ish, typical of AI-assisted generated commits, but could also be human. Key signals: uniform formatting, explicit semver-major update note, and the exact same pattern as many automated PRs. The message adequately describes the change and includes Dependabot metadata. Potential human involvement is plausible given the explicit listing of release notes and commit-style body, but the diff itself is minimal and highly aligned with automated tooling. Overall leaning toward substantial AI involvement, but not absolute. Disagreement between message and diff: the message is generic dependabot chore while the diff reflects a major version bump which is consistent with the message but could be more concise; no mismatch detected between message intent and code change beyond typical automated style.
  - Key signals: single-file change, pyproject.toml dependency bump, dependabot signed-off lines, standard release notes/commit metadata, semver-major update label
- Blended score: **69.8/100**

### `4f1e32ab0b` — chore(deps): Bump actions/checkout from 4.2.2 to 6.0.2 (#2)
- Author: dependabot[bot] — 2026-05-27T07:35:18
- Diff size: +4/-4 across 4 file(s)
- Heuristic score: **67.5/100**
  - *message_vs_diff_size* (55): Small diff (8 lines) but a disproportionately detailed message (39 words) — could be AI-authored boilerplate, but also matches careful human commit discipline.
  - *commit_timing* (80): Only 0s after the previous commit — faster than a typical manual edit-test-commit cycle.
- LLM judge score: **62/100**
  - The commit shows a clean, boilerplate dependency bump with consistent diffs across multiple YAML workflow files. The commit message and diff are unusually thorough for a typical hand-edited change, including explicit references to release notes and a uniform update to many workflow files, plus a signed-off Dependabot-like author. It reads like a generated/templated change typical of automated dependency maintenance. However, the content is fairly mechanical and focused on updating a single dependency, with standard formatting and no custom logic, which still leaves room for human review. The presence of multiple files updated in lockstep and the exact SHA pin replacements suggest automated tooling.

Disagreement between message and diff: The commit message presents as a straightforward dependency bump with some boilerplate details, which aligns with the automated style. There is no obvious mismatch. If anything, the message could be even more AI-sounding by explicitly stating automated tooling; but it already includes Dependabot-like signs. So no clear oversell/undersell.

Key signals:
- Uniformly updated uses: actions/checkout to a new v6.0.2 across several workflows
- Precise SHA references for previous and new versions
- Signed-off-by and Dependabot authors in metadata
- The diff edits are repetitive and mechanical across multiple files
- The changelog references and update-type lines typical of generated PRs
  - Key signals: uniform diffs across multiple files, explicit SHA pins, Dependabot-like metadata, mechanical, repetitive edits across workflows
- Blended score: **64.8/100**

### `5883fd3c29` — chore(deps): Bump actions/setup-python from 5.3.0 to 6.2.0 (#1)
- Author: dependabot[bot] — 2026-05-27T07:35:18
- Diff size: +1/-1 across 1 file(s)
- Heuristic score: **67.5/100**
  - *message_vs_diff_size* (55): Small diff (2 lines) but a disproportionately detailed message (37 words) — could be AI-authored boilerplate, but also matches careful human commit discipline.
  - *commit_timing* (80): Only 0s after the previous commit — faster than a typical manual edit-test-commit cycle.
- LLM judge score: **62/100**
  - The commit shows a clean, standard dependency bump with a clear, well-documented changelog: a conventional Dependabot chore message, explicit release notes links, and a straightforward diff updating a single GitHub Actions workflow step. The diff content is small, precise (switching the actions/setup-python reference from a specific v5.3.0 SHA to a v6.2.0 SHA), and the commit message adheres to typical automated tooling formats. This level of completeness and consistency is indicative of AI-assisted or generated-then-reviewed tooling usage, but not conclusive. The presence of Dependabot authors and a standard release note pattern leans toward automated tooling. However, the diff is a minimal, mechanical change and the prose in the commit message is boilerplate-like, which is more characteristic of AI-generated or bot-assisted commits than a highly idiosyncratic human change. Overall: more likely AI-assisted/substantial automation rather than pure human tangibility, but not unequivocally AI-generated.

Disagreement between message and diff: The commit message is a generic chore with structured metadata, which matches the mechanical nature of the diff. There is no explicit human-centric rationale beyond dependency bump; the message undersells the extent of automation signals a bit (e.g., no handwritten TODOs, no personalized notes). The diff lines themselves are very concise and mechanical, aligning with automated tooling.

Key signals: Dependabot authorship, semantic version bump, explicit SHA references, single-file, one-line diff change, boilerplate workflow update.
  - Key signals: Dependabot, chore(deps), v5.3.0 to v6.2.0, single-file change, actions/setup-python SHA refs
- Blended score: **64.8/100**

### `2b92a0fac7` — chore: Bootstrap OSS hardening — CI, Claude reviews, governance, pyproje
- Author: Daniel Pittman — 2026-05-27T01:00:34
- Diff size: +639/-122 across 14 file(s)
- Heuristic score: **52.5/100**
  - *message_vs_diff_size* (75): Large diff (761 lines) paired with a detailed message (349 words) — consistent with AI-drafted commit messages that narrate the change in full sentences.
  - *commit_timing* (30): 62 min gap since the previous commit — consistent with normal human working pace.
- LLM judge score: **68/100**
  - The diff shows a large, cohesive onboarding of OSS hardening with many boilerplate, policy files, and pinned actions. The commit message describes multiple broad governance and tooling changes. The diff content itself is extremely uniform, with many new files that are standard in structure (CI workflow, CODEOWNERS, dependabot, etc.), clear naming, and exhaustive coverage. That level of completeness and boilerplate, especially the Claude workflows with detailed explanations, suggests substantial AI assistance or a generated template. However, the commit also includes plausible, specific implementation choices (e.g., exact action SHAs, specific branch protection notes, pyproject migration notes) that a human could compose. The combination of unusually uniform structure, extensive scaffolding, and a single commit addressing a wide governance bootstrap weighs toward substantial AI involvement or at least heavy template-driven generation. The commit message itself reads very deliberately as a governance/package bootstrap summary, consistent with the diff.

Disagreement between message and diff: The message calls out incremental/directed changes (e.g., ‘this is the last direct-to-main commit’) whereas the diff shows a wholesale bootstrap of OSS governance and packaging, with many new files. The message’s tone is planning-oriented, while the diff is execution-heavy with many concrete files; this mismatch could indicate a generated plan attached to an implemented scaffolding. If anything, the diff aligns with heavy automation more than a purely human incremental update.

Key signals:
- Large number of new files with precise content (CODEOWNERS, dependabot, multiple workflow YAMLs) in one commit
- Extensive, boilerplate-like commentary in workflow steps and notes that resemble generated templates
- Pinning SHAs for actions and very prescriptive CI steps typical of generated scaffolds
- Co-Authored-By line typical of generated collaboration boilerplate
- The README/CONTRIBUTING style and SECURITY.md details read like standard governance templates

  - Key signals: massive scaffolding in a single commit, SHA-pinned actions and boilerplate workflows, detailed governance/docs content injected as code, co-authored-by with AI-like attribution
  - Note: diff was truncated for length before being sent to the LLM judge.
- Blended score: **60.2/100**

### `e8b7dc3dd4` — fix: Move web server from port 5000 to 5001
- Author: Daniel Pittman — 2026-05-26T23:58:52
- Diff size: +9/-9 across 3 file(s)
- Heuristic score: **42.5/100**
  - *message_vs_diff_size* (55): Small diff (18 lines) but a disproportionately detailed message (50 words) — could be AI-authored boilerplate, but also matches careful human commit discipline.
  - *commit_timing* (30): 332716 min gap since the previous commit — consistent with normal human working pace.
- LLM judge score: **72/100**
  - The commit shows a cohesive, multi-file port update moving the web server from port 5000 to 5001. The changes are comprehensive across README, run scripts, and the Flask app startup logic, with consistent references to port 5001. This suggests non-trivial, intentional engineering and likely AI-assisted drafting or heavy templating, given uniform port updates and explicit comments. However, the work does not appear to be fully auto-generated end-to-end: there is a readable, human-oriented commit message and coherent, targeted edits across multiple files without obviously odd boilerplate or over-engineering. The message aligns with the diff content, describing the port shift and affected files. There is a potential slight mismatch in a few lines where README wording is updated to reflect a single port (local vs. localhost) but still consistent with the change. Overall: substantial AI involvement is plausible (score ~70), but not definitive AI-only.
  - Key signals: multi-file port change, consistent port 5001 across code, scripts, and docs, cohesive updates with explanatory commit message, no obviously synthetic or gratuitous commentary in code, diff shows blanket port replacement without large refactor
- Blended score: **57.2/100**

### `d5b50f6668` — Update README.md
- Author: Daniel Pittman — 2025-10-07T22:43:01
- Diff size: +1/-1 across 1 file(s)
- Heuristic score: **35.0/100**
  - *message_vs_diff_size* (40): Small diff (2 lines), short message (2 words) — no strong signal either way.
  - *commit_timing* (30): 3641 min gap since the previous commit — consistent with normal human working pace.
- LLM judge score: **55/100**
  - The diff shows a small, plausible human-origin edit: modifying a README clone URL from a placeholder to a specific user repository. This is a typical manual tweak in documentation. The commit message 'Update README.md' is generic and aligns with such a minor change. There is no evidence of extensive scaffolding, defensive coding, or verbose auto-generated content. The change is minimal and could be produced by a human, or by an assistant with a simple edit. The message and diff are consistent in suggesting a small, targeted update rather than a large AI-generated overhaul.
  - Key signals: tiny, targeted README edit, commit message generic, no accompanying large code changes or comments, URL change typical of manual config
- Blended score: **45.0/100**

### `3762630227` — feat: Complete 6-phase Rubik's Cube Solver development
- Author: Daniel Pittman — 2025-10-05T10:01:32
- Diff size: +12900/-108 across 48 file(s)
- Heuristic score: **52.5/100**
  - *message_vs_diff_size* (75): Large diff (13008 lines) paired with a detailed message (902 words) — consistent with AI-drafted commit messages that narrate the change in full sentences.
  - *commit_timing* (30): 48013 min gap since the previous commit — consistent with normal human working pace.
- LLM judge score: **68/100**
  - The commit message is extremely comprehensive, boilerplate-like, and reads like an AI-generated project overview. It includes phase-by-phase summaries, an extensive feature list, architecture diagrams in prose, and an inflated test/metrics section that matches a ‘produced by an AI demonstration’ pattern. The diff shows a lot of large-scale changes including .gitattributes, .gitignore modifications, pre-commit config with heavily commented sections, and a CLAUDE.md file, all of which resemble an auto-generated educational showcase. The presence of a long, template-like narrative in the commit body, references to Claude Code, and an explicit note about AI generation in the footer strongly suggest AI authoring. However, the commit also contains plausible normal changes (lint config tweaks, project scaffolding, some realistic content in .gitignore). This mix indicates substantial AI involvement, but not necessarily 100% AI: some human authoring could be mixed in, given the realistic project scaffolding. Thus score in the 51–80 band aligns: substantial AI-assisted structure and narrative, with concrete but plausible manual edits sprinkled in. Potential misalignment: the message explicitly claims 12,884 lines and production-grade 6-phase workflow; the diff excerpt is truncated and includes a CLAUDE.md that looks like an AI-created artifact, which corroborates the claim of AI involvement.

Disagreement note: If one expected a tighter, more terse commit message from a hand-written change set, this diff/messaging deviates toward a generated educational narrative. The message oversells AI involvement relative to the small shown diff portion, but overall aligns with a heavily AI-assisted commit.

  - Key signals: long, boilerplate summary, CLAUDE.md mention, extensive phase-by-phase breakdown, pre-commit and .gitignore rework, diff includes templated educational narrative pieces
  - Note: diff was truncated for length before being sent to the LLM judge.
- Blended score: **60.2/100**

### `961542b73c` — Initial setup of repository to give starting point for LLM to use
- Author: Daniel Pittman — 2025-09-02T01:48:55
- Diff size: +1169/-0 across 14 file(s)
- Heuristic score: **65.0/100**
  - *message_vs_diff_size* (75): Large diff (1169 lines) paired with a detailed message (12 words) — consistent with AI-drafted commit messages that narrate the change in full sentences.
  - *commit_timing* (55): 8.1 min after the previous commit — plausible for either a fast human pass or an AI-assisted one.
- LLM judge score: **62/100**
  - The commit includes a broad scaffolding setup: .gitattributes, .gitignore with extensive Python/project ignores, a .idea IDE config, a pre-commit config with multiple tools, and some small IDE-specific files. The diff shows a lot of boilerplate files that are typical of an initial repository bootstrap rather than hand-tuned feature work. The commit message describes 'Initial setup of repository to give starting point for LLM to use', which aligns with this kind of broad scaffolding.

Indicators of AI-involvement beyond casual human work:
- The .gitignore and .gitattributes contents are unusually comprehensive and generic, almost template-like rather than tailored to a specific project.
- Inclusion of many IDE config placeholders and .pre-commit.yaml with multiple tools configured in a very standard way.
- A consistent, almost textbook structure for initial repo setup rather than incremental domain-specific edits.

However, it is not utterly uniform and could be a careful human who wants a clean starting point. The message claims starting point for LLM to use, which matches the scaffolding: it provides formatting rules, ignores, and tooling presets to make an LLM-assisted coding environment deterministic.

Disagreement between message and diff: The commit message is brief and generic, while the diff contains a broad, multi-file bootstrap. The message underestimates the breadth (should reflect the scope: repo bootstrap including IDE and pre-commit tooling). If anything, the diff suggests more AI-like boilerplate than a minimal human boot.

Key signals:
- presence of .gitattributes with line-ending normalization rules across many file types – boilerplate templates
- massive .gitignore with many common Python projects settings
- .pre-commit-config.yaml with multiple standardized hooks and wording matches generic templates
- .idea/ and IDE-specific xml, which is common in templates but less likely in carefully curated human commits unless specifically intended
- commit message generic but match to setting up a “starting point” for an LLM to use

  - Key signals:  boilerplate .gitattributes, extensive .gitignore template, pre-commit config with standard hooks, IDE configs included, generic commit message
  - Note: diff was truncated for length before being sent to the LLM judge.
- Blended score: **63.5/100**

### `e2f0e91542` — Initial commit
- Author: Daniel Pittman — 2025-09-02T01:40:50
- Diff size: +21/-0 across 1 file(s)
- Heuristic score: **40.0/100**
  - *message_vs_diff_size* (40): Small diff (21 lines), short message (2 words) — no strong signal either way.
  - *commit_timing* (40): First commit in range — no prior commit to compare timing against.
- LLM judge score: **62/100**
  - The commit is an 'Initial commit' that adds a standard MIT license file. The diff shows a clean, boilerplate license text with conventional formatting and no accompanying code changes. The message is minimal and generic, not indicating AI involvement. However, the content of the diff (a complete MIT license block) is typical of boilerplate templates generated by tools or common practices; the uniformity and absence of human-like quirks could suggest tooling assistance. The mismatch to the task’s typical human handwriting is low; the commit could be authored by a human or an initial project setup possibly aided by templates. The lack of any code, tests, or nuanced changes reduces the evidentiary signals for heavy AI generation. Overall, the evidence leans toward mostly human with possible light tool assistance, hence a moderate score around 60. The commit message undersells AI involvement (it’s just 'Initial commit' while the diff is a clean license block); the message and diff are somewhat mismatched in signaling AI usage, but not strongly.

Key signals:
- Single, boilerplate license addition (common in both human and AI workflows) 
- Very clean, standard formatting with no stylistic idiosyncrasies
- Commit message generic; no AI-style explanatory notes
- No code logic or complex changes to infer AI structuring or defensive patterns

  - Key signals: boilerplate license text, minimal commit message, no code logic, clean, standard formatting
- Blended score: **51.0/100**
