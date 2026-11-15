# AI Usage Authenticity Report — C:\Users\SCS\quest\test-repos\Fawad-Act-angel

Generated 2026-11-14T11:34:56
Commits analyzed: 132

## Aggregate summary

- Heuristic layer average: 37.5/100 (n=132)
- LLM judge layer average: 54.9/100 (n=25)
- Commits where the two layers disagree by >=30 points: 15

## Per-commit detail

### `a23fa2a4f8` — Add README
- Author: Tahir Hameed — 2026-11-13T09:58:42
- Diff size: +74/-0 across 1 file(s)
- Heuristic score: **27.5/100**
  - *message_vs_diff_size* (25): Large diff (74 lines) with a short message (7 words) — more typical of a human committing quickly without narrating the change.
  - *commit_timing* (30): 9823 min gap since the previous commit — consistent with normal human working pace.
- LLM judge score: **68/100**
  - The README.md is unusually complete and polished for a single commit that simply adds a README. It includes a clear project overview, detailed feature flow (Hope Angel, OTP verification, n8n integration), project structure, getting started steps, environment variables, and scripts. The level of consistency (sections, tables, code blocks) and the breadth of operational details (Twilio Verify, PostHog, Clarity, n8n webhooks, etc.) suggest strong tooling-awareness and defensiveness beyond what a minimal hand-written note would entail. This pattern—comprehensive, almost boilerplate-like documentation with precise field lists—is often associated with AI-assisted or generated content, or at least a heavily templated artifact. That said, a competent human could also author this, especially if the project owner values thorough docs from the outset. The commit message is minimal (“Add README”) and does not hint at the depth of content, which creates a mild mismatch between the message and the diff’s magnitude.

Key signals:
- Highly structured sections and a long README with many concrete implementation details (Next.js App Router, Twilio Verify, n8n, PostHog, Clarity) that feel like a pre-existing template or boilerplate.
- Consistent formatting: bulleting, code fences, and a large environment-variables table spanning multiple lines, plus a manifest-like environment example file name mentioned.
- The author in the diff metadata is a Co-Authored-By line in the commit header, which is common in AI-assisted contributions, though not definitive.
- Absence of typos or human idiosyncrasies that would be typical in a quick hand-written README.

Disagreement with message: The commit message is extremely minimal (“Add README”), while the diff content is richly detailed. If anything, the message undersells the actual change. The diff reads like a substantial, polished artifact rather than a tiny addition. 

Recommendation: Likely mixed-origin or AI-assisted drafting, but leaning toward substantial AI involvement or a heavily templated scaffold rather than purely hand-written.
  - Key signals: Co-authored-By: Claude Sonnet 5.5, Extensive, boilerplate-like structure (sections, tables, code blocks), Comprehensive environment variable list, Specific tech stack references (Next.js App Router, Twilio Verify, n8n, PostHog, Clarity), Lack of obvious human typos or idiosyncrasies, Commit message minimal relative to content
- Blended score: **47.8/100**
  - Heuristic and LLM layers disagree by >=30 points — treat this commit's score as uncertain.

### `083de71d6e` — dark theme in through url
- Author: Rahul — 2026-11-06T14:15:22
- Diff size: +72/-8 across 3 file(s)
- Heuristic score: **27.5/100**
  - *message_vs_diff_size* (25): Large diff (80 lines) with a short message (5 words) — more typical of a human committing quickly without narrating the change.
  - *commit_timing* (30): 36 min gap since the previous commit — consistent with normal human working pace.
- LLM judge: not run (sampling or `--no-llm`).

### `f54e6e836e` — Merge branch 'main' of https://github.com/CloudSteer-Technology/act-ange
- Author: Rahul — 2026-11-06T13:38:55
- Diff size: +51/-5 across 1 file(s)
- Heuristic score: **52.5/100**
  - *message_vs_diff_size* (25): Large diff (56 lines) with a short message (5 words) — more typical of a human committing quickly without narrating the change.
  - *commit_timing* (80): Only 73s after the previous commit — faster than a typical manual edit-test-commit cycle.
- LLM judge: not run (sampling or `--no-llm`).

### `52c10e1f82` — nav items text color updated
- Author: Rahul — 2026-11-06T13:37:42
- Diff size: +14/-3 across 2 file(s)
- Heuristic score: **35.0/100**
  - *message_vs_diff_size* (40): Small diff (17 lines), short message (5 words) — no strong signal either way.
  - *commit_timing* (30): 893 min gap since the previous commit — consistent with normal human working pace.
- LLM judge: not run (sampling or `--no-llm`).

### `77aba9040d` — Merge pull request #5 from CloudSteer-Technology/fix/otp-send-abuse-limi
- Author: Tahir Hameed — 2026-11-05T22:44:34
- Diff size: +51/-5 across 1 file(s)
- Heuristic score: **52.5/100**
  - *message_vs_diff_size* (75): Large diff (56 lines) paired with a detailed message (20 words) — consistent with AI-drafted commit messages that narrate the change in full sentences.
  - *commit_timing* (30): 102 min gap since the previous commit — consistent with normal human working pace.
- LLM judge: not run (sampling or `--no-llm`).

### `4d2c92bfc7` — Allow the 18 countries the client approved for OTP codes
- Author: Tahir Hameed — 2026-11-05T21:02:24
- Diff size: +10/-3 across 1 file(s)
- Heuristic score: **42.5/100**
  - *message_vs_diff_size* (55): Small diff (13 lines) but a disproportionately detailed message (52 words) — could be AI-authored boilerplate, but also matches careful human commit discipline.
  - *commit_timing* (30): 356 min gap since the previous commit — consistent with normal human working pace.
- LLM judge score: **68/100**
  - The change expands the allowed country prefixes from a small hard-coded set to a larger, explicit list of 18 prefixes, aligned with Twilio geo permissions. The diff adds a long list of prefixes and updates the error message to a more generic one. The commit message accurately describes the intent and lists the same countries. The code structure is clean and consistent, with explanatory comments. The level of boilerplate and commentary is somewhat verbose (which can suggest AI assistance), but not excessively so. Overall, this appears to be a substantial, well-documented update that could plausibly be authored by a human with some guidance or lightly assisted by tooling; not obviously AI-generated, but the extensive explicit list and canned error wording could be indicative of automated scaffolding in addition to human work.
  - Key signals: expanded explicit list of country prefixes, alignment with Twilio geo permissions, verbose commit message detailing country list, commentary explaining rationale and incident context
- Blended score: **55.2/100**

### `d5be5175da` — Block OTP sends outside US, India and Pakistan and add Twilio Verify rat
- Author: Tahir Hameed — 2026-11-05T15:05:54
- Diff size: +44/-5 across 1 file(s)
- Heuristic score: **52.5/100**
  - *message_vs_diff_size* (75): Large diff (49 lines) paired with a detailed message (72 words) — consistent with AI-drafted commit messages that narrate the change in full sentences.
  - *commit_timing* (30): 1301 min gap since the previous commit — consistent with normal human working pace.
- LLM judge: not run (sampling or `--no-llm`).

### `b6f38cd95c` — merge confilict resolved
- Author: Rahul — 2026-11-04T17:25:19
- Diff size: +1/-1 across 1 file(s)
- Heuristic score: **60.0/100**
  - *message_vs_diff_size* (40): Small diff (2 lines), short message (3 words) — no strong signal either way.
  - *commit_timing* (80): Only 15s after the previous commit — faster than a typical manual edit-test-commit cycle.
- LLM judge: not run (sampling or `--no-llm`).

### `843a9f0dde` — u
- Author: Rahul — 2026-11-04T17:25:04
- Diff size: +1/-1 across 1 file(s)
- Heuristic score: **47.5/100**
  - *message_vs_diff_size* (40): Small diff (2 lines), short message (1 words) — no strong signal either way.
  - *commit_timing* (55): 1.8 min after the previous commit — plausible for either a fast human pass or an AI-assisted one.
- LLM judge: not run (sampling or `--no-llm`).

### `533a77ad54` — merge confilict resolved
- Author: Rahul — 2026-11-04T17:23:19
- Diff size: +1752/-779 across 33 file(s)
- Heuristic score: **27.5/100**
  - *message_vs_diff_size* (25): Large diff (2531 lines) with a short message (3 words) — more typical of a human committing quickly without narrating the change.
  - *commit_timing* (30): 145 min gap since the previous commit — consistent with normal human working pace.
- LLM judge: not run (sampling or `--no-llm`).

### `2e69abb77e` — dark theme fixes
- Author: npltech — 2026-11-04T14:58:48
- Diff size: +153/-46 across 9 file(s)
- Heuristic score: **27.5/100**
  - *message_vs_diff_size* (25): Large diff (199 lines) with a short message (3 words) — more typical of a human committing quickly without narrating the change.
  - *commit_timing* (30): 254 min gap since the previous commit — consistent with normal human working pace.
- LLM judge score: **65/100**
  - The commit includes broad, stylistic and structural edits across multiple files (CSS variables with long, ticket-labeled rationale; new font Inter added via next/font; layout and hero spacing adjustments with extensive in-code commentary). The commit message 'dark theme fixes' is narrowly scoped and does not reflect the breadth of changes, which touch typography, responsive behavior, and layout decisions. The highly verbose, self-descriptive comments (e.g., AAA-UI-DM-WEB-001/004 tickets, detailed rationale about viewport quirks) read like generated guidance or auto-generated notes, which are typical of AI-assisted or heavily templated edits. However, there are still signs of human intent (targeted UI tweaks, obvious QA-oriented notes), so it’s likely mixed-origin rather than fully AI-generated. Overall, the change set is cohesive and unusually thorough for a single small feature, suggesting substantial AI involvement relative to a typical hand-written commit.)
  - Key signals: extensive inline QA/ticket annotations in comments, new font integration (Inter) added with rationale, large CSS variable/documentation edits for theming, wide-ranging layout/hrz adjustments across multiple files, commit message does not map to the scope of changes
  - Note: diff was truncated for length before being sent to the LLM judge.
- Blended score: **46.2/100**
  - Heuristic and LLM layers disagree by >=30 points — treat this commit's score as uncertain.

### `87eb55601a` — dark theme updated
- Author: npltech — 2026-11-04T10:44:57
- Diff size: +6/-3 across 2 file(s)
- Heuristic score: **35.0/100**
  - *message_vs_diff_size* (40): Small diff (9 lines), short message (3 words) — no strong signal either way.
  - *commit_timing* (30): 1394 min gap since the previous commit — consistent with normal human working pace.
- LLM judge: not run (sampling or `--no-llm`).

### `0dd964d372` — dark theme updated
- Author: npltech — 2026-11-03T11:30:28
- Diff size: +391/-334 across 21 file(s)
- Heuristic score: **27.5/100**
  - *message_vs_diff_size* (25): Large diff (725 lines) with a short message (3 words) — more typical of a human committing quickly without narrating the change.
  - *commit_timing* (30): 3655 min gap since the previous commit — consistent with normal human working pace.
- LLM judge: not run (sampling or `--no-llm`).

### `e5db096bdc` — Privacy policy updation.
- Author: Radhikesh Kumar — 2026-10-31T22:35:21
- Diff size: +427/-89 across 1 file(s)
- Heuristic score: **27.5/100**
  - *message_vs_diff_size* (25): Large diff (516 lines) with a short message (3 words) — more typical of a human committing quickly without narrating the change.
  - *commit_timing* (30): 389 min gap since the previous commit — consistent with normal human working pace.
- LLM judge: not run (sampling or `--no-llm`).

### `7586a11298` — dark images added
- Author: npltech — 2026-10-31T16:06:39
- Diff size: +47/-15 across 7 file(s)
- Heuristic score: **27.5/100**
  - *message_vs_diff_size* (25): Large diff (62 lines) with a short message (3 words) — more typical of a human committing quickly without narrating the change.
  - *commit_timing* (30): 274 min gap since the previous commit — consistent with normal human working pace.
- LLM judge: not run (sampling or `--no-llm`).

### `f8aadede32` — updated themes
- Author: npltech — 2026-10-31T11:33:09
- Diff size: +1/-1 across 1 file(s)
- Heuristic score: **60.0/100**
  - *message_vs_diff_size* (40): Small diff (2 lines), short message (2 words) — no strong signal either way.
  - *commit_timing* (80): Only 21s after the previous commit — faster than a typical manual edit-test-commit cycle.
- LLM judge score: **28/100**
  - The diff shows a tiny, likely manual bug fix: removing an stray '1' after a removeEventListener call. The rest of the code is standard React/TS cleanup. The commit message says 'updated themes', which has no relation to this change, suggesting a mismatched or generic message rather than a cohesive commit note. This combination suggests the change is probably human-corrected rather than a fully AI-generated big fix. The small, local nature of the edit and the odd stray character are human-like clues.
  - Key signals: tiny bug fix (stray character) in analytics-gate.tsx, commit message not aligned with code change, no large, AI-like boilerplate or exhaustive scaffolding, standard React/TypeScript pattern without unusual abstractions
- Blended score: **44.0/100**
  - Heuristic and LLM layers disagree by >=30 points — treat this commit's score as uncertain.

### `2447a70232` — u
- Author: npltech — 2026-10-31T11:32:48
- Diff size: +1/-1 across 1 file(s)
- Heuristic score: **47.5/100**
  - *message_vs_diff_size* (40): Small diff (2 lines), short message (1 words) — no strong signal either way.
  - *commit_timing* (55): 7.2 min after the previous commit — plausible for either a fast human pass or an AI-assisted one.
- LLM judge: not run (sampling or `--no-llm`).

### `6eac05945e` — dark theme implemented
- Author: npltech — 2026-10-31T11:25:34
- Diff size: +1537/-636 across 32 file(s)
- Heuristic score: **27.5/100**
  - *message_vs_diff_size* (25): Large diff (2173 lines) with a short message (3 words) — more typical of a human committing quickly without narrating the change.
  - *commit_timing* (30): 1088 min gap since the previous commit — consistent with normal human working pace.
- LLM judge: not run (sampling or `--no-llm`).

### `a4b928e869` — Merge branch 'main' of https://github.com/CloudSteer-Technology/act-ange
- Author: npltech — 2026-10-30T17:17:21
- Diff size: +359/-72 across 9 file(s)
- Heuristic score: **40.0/100**
  - *message_vs_diff_size* (25): Large diff (431 lines) with a short message (5 words) — more typical of a human committing quickly without narrating the change.
  - *commit_timing* (55): 1.7 min after the previous commit — plausible for either a fast human pass or an AI-assisted one.
- LLM judge: not run (sampling or `--no-llm`).

### `2d831e16b8` — title updated
- Author: npltech — 2026-10-30T17:15:37
- Diff size: +2/-2 across 2 file(s)
- Heuristic score: **35.0/100**
  - *message_vs_diff_size* (40): Small diff (4 lines), short message (2 words) — no strong signal either way.
  - *commit_timing* (30): 1632 min gap since the previous commit — consistent with normal human working pace.
- LLM judge: not run (sampling or `--no-llm`).

### `4c8175b421` — Merge pull request #4 from CloudSteer-Technology/fix/share-your-mission-
- Author: Tahir Hameed — 2026-10-29T14:03:32
- Diff size: +359/-72 across 9 file(s)
- Heuristic score: **52.5/100**
  - *message_vs_diff_size* (75): Large diff (431 lines) paired with a detailed message (14 words) — consistent with AI-drafted commit messages that narrate the change in full sentences.
  - *commit_timing* (30): 977 min gap since the previous commit — consistent with normal human working pace.
- LLM judge: not run (sampling or `--no-llm`).

### `8dc5a0a60a` — Fix Hope Angel form validation and draft reset
- Author: Tahir Hameed — 2026-10-28T21:46:34
- Diff size: +359/-72 across 9 file(s)
- Heuristic score: **27.5/100**
  - *message_vs_diff_size* (25): Large diff (431 lines) with a short message (8 words) — more typical of a human committing quickly without narrating the change.
  - *commit_timing* (30): 3271 min gap since the previous commit — consistent with normal human working pace.
- LLM judge score: **72/100**
  - The changes show a cohesive, multi-file update aimed at tightening validation and adding draft handling. In route.ts, there are concrete validation improvements (meaningful content checks, URL validation, and explicit error messages) plus a small behavioral note about optional fields. In the UI component, there is a larger structural change: pulling in hasMeaningfulContent, draft save/load/clear utilities, and a defensive approach to priorities with a fallback list and an API fetch. The edits are both substantial and well-documented with targeted comments (e.g., AAA-HA-009) and a fallback path for the priority options. This reads like deliberate, well-considered changes rather than a tiny bugfix or purely auto-generated snippet.

Agreement or mismatch between message and diff: The commit message mentions fixing form validation and draft reset, which matches the changes in both server-side validation and client-side draft utilities imports and usage. The diff implies more than a minimal fix (e.g., meaningful content checks, URL validation, and a fetch with a fallback for priorities), which aligns with the message but suggests a broader scope than a tiny patch. No clear mismatch between message and changes, though the message could undersell the breadth (these are substantial validation and UI draft enhancements).

Key signals:
- Server route.ts includes new imports for content/URL validation and changes to required fields logic.
- Client UI adds draft utilities and a dynamic priority-options fetch with a fallback array.
- Presence of defensive comments, feature-flag-like notes (AAA-HA-009), and explicit user-facing messages. }{
  - Key signals: new validation utilities, URL/meaningful content checks, draft save/load imports, priority options fetch with fallback, detailed user messages
  - Note: diff was truncated for length before being sent to the LLM judge.
- Blended score: **49.8/100**
  - Heuristic and LLM layers disagree by >=30 points — treat this commit's score as uncertain.

### `76f0174480` — updated1
- Author: npltech — 2026-10-26T15:15:35
- Diff size: +1/-1 across 1 file(s)
- Heuristic score: **60.0/100**
  - *message_vs_diff_size* (40): Small diff (2 lines), short message (1 words) — no strong signal either way.
  - *commit_timing* (80): Only 10s after the previous commit — faster than a typical manual edit-test-commit cycle.
- LLM judge: not run (sampling or `--no-llm`).

### `c70dd10a19` — updated
- Author: npltech — 2026-10-26T15:15:25
- Diff size: +6/-1 across 1 file(s)
- Heuristic score: **35.0/100**
  - *message_vs_diff_size* (40): Small diff (7 lines), short message (1 words) — no strong signal either way.
  - *commit_timing* (30): 11 min gap since the previous commit — consistent with normal human working pace.
- LLM judge: not run (sampling or `--no-llm`).

### `272bb08c73` — Merge branch 'main' of https://github.com/CloudSteer-Technology/act-ange
- Author: npltech — 2026-10-26T15:04:30
- Diff size: +28/-5 across 1 file(s)
- Heuristic score: **60.0/100**
  - *message_vs_diff_size* (40): Small diff (33 lines), short message (5 words) — no strong signal either way.
  - *commit_timing* (80): Only 16s after the previous commit — faster than a typical manual edit-test-commit cycle.
- LLM judge: not run (sampling or `--no-llm`).

### `36a2a714f8` — shareable icon added
- Author: npltech — 2026-10-26T15:04:14
- Diff size: +6/-0 across 2 file(s)
- Heuristic score: **35.0/100**
  - *message_vs_diff_size* (40): Small diff (6 lines), short message (3 words) — no strong signal either way.
  - *commit_timing* (30): 15731 min gap since the previous commit — consistent with normal human working pace.
- LLM judge: not run (sampling or `--no-llm`).

### `a26536e99a` — Store Email-channel leads in our own DB alongside the existing enquiry h
- Author: Tahir Hameed — 2026-10-15T16:52:59
- Diff size: +28/-5 across 1 file(s)
- Heuristic score: **42.5/100**
  - *message_vs_diff_size* (55): Small diff (33 lines) but a disproportionately detailed message (12 words) — could be AI-authored boilerplate, but also matches careful human commit discipline.
  - *commit_timing* (30): 412 min gap since the previous commit — consistent with normal human working pace.
- LLM judge score: **72/100**
  - The diff shows a coherent, well-integrated feature: adding email-channel data flow into a separate DB via an intake webhook, while preserving existing Call/WhatsApp behavior. The changes include: restructuring the early configuration validation to account for email channel, expanded error messaging, and a new data_only lead storage block with a defensive try/catch. The commit message describes the feature at a high level, which matches the code intent. The comments are unusually verbose and explanatory (e.g., about data_only and the two pipelines), which can be indicative of AI assistance or a very cautious human reviewer. The patch is self-contained, with consistent naming and minimal stylistic churn beyond what the feature requires. Overall, it’s plausible a human added this with careful consideration, but the thoroughness and uniformity of the changes suggest some AI-assisted drafting or a template-driven approach. 

Disagreement between message and diff: The commit message is concise and high-level, while the diff has detailed operational changes (explicitly handling data_only, multiple environments, expanded error text). There’s no clear mismatch, just the message underselling the breadth of changes (the diff implements a new data storage path for email leads and refactors validation accordingly).
  - Key signals: new data_only intake call, email channel handling expanded, expanded error messages, verbose inline comments, consistent naming and structure
- Blended score: **57.2/100**

### `b1ce9f77f6` — Merge branch 'main' of https://github.com/CloudSteer-Technology/act-ange
- Author: npltech — 2026-10-15T10:01:29
- Diff size: +109/-3 across 2 file(s)
- Heuristic score: **52.5/100**
  - *message_vs_diff_size* (25): Large diff (112 lines) with a short message (5 words) — more typical of a human committing quickly without narrating the change.
  - *commit_timing* (80): Only 61s after the previous commit — faster than a typical manual edit-test-commit cycle.
- LLM judge: not run (sampling or `--no-llm`).

### `f6dd49a168` — hero content updated
- Author: npltech — 2026-10-15T10:00:28
- Diff size: +2/-2 across 1 file(s)
- Heuristic score: **35.0/100**
  - *message_vs_diff_size* (40): Small diff (4 lines), short message (3 words) — no strong signal either way.
  - *commit_timing* (30): 743 min gap since the previous commit — consistent with normal human working pace.
- LLM judge: not run (sampling or `--no-llm`).

### `19c1a6422f` — Fix Share Your Mission form validation and draft persistence
- Author: Tahir Hameed — 2026-10-14T21:37:45
- Diff size: +109/-3 across 2 file(s)
- Heuristic score: **27.5/100**
  - *message_vs_diff_size* (25): Large diff (112 lines) with a short message (9 words) — more typical of a human committing quickly without narrating the change.
  - *commit_timing* (30): 311 min gap since the previous commit — consistent with normal human working pace.
- LLM judge: not run (sampling or `--no-llm`).

### `44bbaf4643` — employee keyword replaced with specialist
- Author: npltech — 2026-10-14T16:27:02
- Diff size: +17/-17 across 9 file(s)
- Heuristic score: **35.0/100**
  - *message_vs_diff_size* (40): Small diff (34 lines), short message (5 words) — no strong signal either way.
  - *commit_timing* (30): 1867 min gap since the previous commit — consistent with normal human working pace.
- LLM judge: not run (sampling or `--no-llm`).

### `bfb36e5ebf` — title description updated
- Author: npltech — 2026-10-13T09:20:31
- Diff size: +6/-6 across 1 file(s)
- Heuristic score: **35.0/100**
  - *message_vs_diff_size* (40): Small diff (12 lines), short message (3 words) — no strong signal either way.
  - *commit_timing* (30): 1271 min gap since the previous commit — consistent with normal human working pace.
- LLM judge score: **55/100**
  - The commit primarily updates static metadata strings across multiple parts of the layout: title, description, and openGraph/twitter metadata values. The changes are cohesive and marketing-forward, with consistent phrasing across title/description, openGraph, and twitter sections. This pattern is typical of hand-edited copy updates, but the breadth and uniformity of the new copy could also be produced by a copywriting prompt or AI-assisted tooling. The commit message itself is minimal (“title description updated”) which underreports the scope of the diff, a minor tell that human authorship could be understated. Overall, the changes are not technically complex or functionally novel, and there are no obvious defensive programming additions. While the wording is polished and consistent, that alone doesn't decisively indicate AI generation, but the uniform boilerplate across several fields hints at an AI-assisted touch more than a casual human edit. 

Disagreement note: The commit message suggests a small change, but the diff shows a broader, uniform rewrite of metadata text. If one assumes AI assistance, the message undersells the extent of the change; if taken as purely human, the uniformity could reflect a script-based update. No explicit indicators of heavy AI-generated code structure are present, so it sits in the middle range.
  - Key signals: uniform metadata rewrite across multiple fields, consistent marketing copy style, no code logic changes, commit message underreports scope
- Blended score: **45.0/100**

### `260a8bd18d` — ui issues fixed
- Author: npltech — 2026-10-12T12:09:47
- Diff size: +248/-37 across 5 file(s)
- Heuristic score: **27.5/100**
  - *message_vs_diff_size* (25): Large diff (285 lines) with a short message (3 words) — more typical of a human committing quickly without narrating the change.
  - *commit_timing* (30): 4438 min gap since the previous commit — consistent with normal human working pace.
- LLM judge: not run (sampling or `--no-llm`).

### `a1af901acb` — navbar hover effect fixed
- Author: npltech — 2026-10-09T10:11:59
- Diff size: +7/-2 across 1 file(s)
- Heuristic score: **35.0/100**
  - *message_vs_diff_size* (40): Small diff (9 lines), short message (4 words) — no strong signal either way.
  - *commit_timing* (30): 1424 min gap since the previous commit — consistent with normal human working pace.
- LLM judge: not run (sampling or `--no-llm`).

### `0a927a1303` — seperate page added for share your mission form
- Author: npltech — 2026-10-08T10:28:28
- Diff size: +65/-53 across 3 file(s)
- Heuristic score: **27.5/100**
  - *message_vs_diff_size* (25): Large diff (118 lines) with a short message (8 words) — more typical of a human committing quickly without narrating the change.
  - *commit_timing* (30): 1436 min gap since the previous commit — consistent with normal human working pace.
- LLM judge: not run (sampling or `--no-llm`).

### `fab6384890` — navbar updated
- Author: npltech — 2026-10-07T10:32:14
- Diff size: +43/-8 across 1 file(s)
- Heuristic score: **27.5/100**
  - *message_vs_diff_size* (25): Large diff (51 lines) with a short message (2 words) — more typical of a human committing quickly without narrating the change.
  - *commit_timing* (30): 1427 min gap since the previous commit — consistent with normal human working pace.
- LLM judge: not run (sampling or `--no-llm`).

### `9bc0d531cf` — hover effect glitch in menu bar fixed
- Author: npltech — 2026-10-06T10:45:08
- Diff size: +31/-2 across 1 file(s)
- Heuristic score: **35.0/100**
  - *message_vs_diff_size* (40): Small diff (33 lines), short message (7 words) — no strong signal either way.
  - *commit_timing* (30): 11 min gap since the previous commit — consistent with normal human working pace.
- LLM judge score: **72/100**
  - The commit introduces a substantial, self-contained workaround for a hover bug during scrolling: tracking last known cursor position, re-testing which row is actually under the cursor on scroll, and adjusting the tooltip accordingly. The code includes multiple new helper pieces (lastMouseRef, updateTooltipAtCursor, updated onScroll and onMouseMove handlers, and adjusted onMouseEnter logic) plus thorough explanatory comments. This level of defensive, UX-focused handling and the cohesive integration across event handlers suggests substantial AI-like structuring (a highly polished, textbook approach) rather than a minimal hand-written tweak. The commit message is concise and accurate, matching a non-trivial behavioral fix, but the code style and completeness hint at AI assistance or a very careful pattern-following style. Overall, falls in 51-80, leaning toward substantial AI involvement.)
  - Key signals: new helper tracking cursor (lastMouseRef), updateTooltipAtCursor function added, onScroll now calls updateTooltipAtCursor, onMouseMove updates lastMouseRef, onMouseEnter enhanced to set lastMouseRef and show tooltip, extensive explanatory comments about hover handling during scroll
- Blended score: **53.5/100**
  - Heuristic and LLM layers disagree by >=30 points — treat this commit's score as uncertain.

### `6b9c445e82` — ui fixes on hope angle page
- Author: npltech — 2026-10-06T10:34:21
- Diff size: +148/-37 across 4 file(s)
- Heuristic score: **27.5/100**
  - *message_vs_diff_size* (25): Large diff (185 lines) with a short message (6 words) — more typical of a human committing quickly without narrating the change.
  - *commit_timing* (30): 3836 min gap since the previous commit — consistent with normal human working pace.
- LLM judge: not run (sampling or `--no-llm`).

### `4d115f85cf` — updated
- Author: npltech — 2026-10-03T18:38:37
- Diff size: +2/-2 across 1 file(s)
- Heuristic score: **47.5/100**
  - *message_vs_diff_size* (40): Small diff (4 lines), short message (1 words) — no strong signal either way.
  - *commit_timing* (55): 2.9 min after the previous commit — plausible for either a fast human pass or an AI-assisted one.
- LLM judge: not run (sampling or `--no-llm`).

### `329f225122` — Merge branch 'main' of https://github.com/CloudSteer-Technology/act-ange
- Author: npltech — 2026-10-03T18:35:46
- Diff size: +29/-29 across 2 file(s)
- Heuristic score: **52.5/100**
  - *message_vs_diff_size* (25): Large diff (58 lines) with a short message (5 words) — more typical of a human committing quickly without narrating the change.
  - *commit_timing* (80): Only 20s after the previous commit — faster than a typical manual edit-test-commit cycle.
- LLM judge: not run (sampling or `--no-llm`).

### `ce0c2a9487` — content updated on main
- Author: npltech — 2026-10-03T18:35:26
- Diff size: +163/-159 across 3 file(s)
- Heuristic score: **27.5/100**
  - *message_vs_diff_size* (25): Large diff (322 lines) with a short message (4 words) — more typical of a human committing quickly without narrating the change.
  - *commit_timing* (30): 35 min gap since the previous commit — consistent with normal human working pace.
- LLM judge: not run (sampling or `--no-llm`).

### `4d18c34100` — updated nav
- Author: npltech — 2026-10-03T18:00:06
- Diff size: +1/-1 across 1 file(s)
- Heuristic score: **35.0/100**
  - *message_vs_diff_size* (40): Small diff (2 lines), short message (2 words) — no strong signal either way.
  - *commit_timing* (30): 48 min gap since the previous commit — consistent with normal human working pace.
- LLM judge: not run (sampling or `--no-llm`).

### `ce6603b46c` — known source added for get-started page
- Author: npltech — 2026-10-03T17:12:11
- Diff size: +55/-10 across 5 file(s)
- Heuristic score: **27.5/100**
  - *message_vs_diff_size* (25): Large diff (65 lines) with a short message (6 words) — more typical of a human committing quickly without narrating the change.
  - *commit_timing* (30): 21 min gap since the previous commit — consistent with normal human working pace.
- LLM judge score: **72/100**
  - The commit introduces a cohesive feature with multiple files touched: get-started page knows about sources, persona entries now carry explicit ctaHref/closingCtaHref, environment/types adjusted, and dev tooling (Playwright) added. The changes are substantial and well-structured, with deliberate inline comments explaining URL/source handling. This level of completeness and cross-file consistency suggests notable AI assistance or at least a high degree of boilerplate/patterns (e.g., consistent ctaHref usage across personas, explicit notes about Next.js trailingSlash behavior). However, the work does not appear to be an obviously auto-generated all-at-once dump; there are human-readable notes and targeted fixes. So it sits in a region of substantial AI involvement but not to the extreme (not a fully dump-like AI-generated single-commit). The commit message itself is concise and underplays the breadth of changes, which is a mismatch with the diff scope.
  - Key signals: Multiple file edits across app/get-started/page.tsx and lib/personas.ts, Explicit KNOWN_SOURCES array expanded to five values with rationale, Inline comments detailing URL/query handling and next.config.trailingSlash behavior, New fields ctaHref and closingCtaHref added for several personas, Next-env.d.ts amended to include root-params.d.ts import, DevDependency @playwright/test added and corresponding lockfile/packaging updates, Commit message short and generic compared to the breadth of diff
  - Note: diff was truncated for length before being sent to the LLM judge.
- Blended score: **49.8/100**
  - Heuristic and LLM layers disagree by >=30 points — treat this commit's score as uncertain.

### `28626a9977` — hire an angel version 2 dropdown implemented
- Author: npltech — 2026-10-03T16:50:55
- Diff size: +190/-3 across 1 file(s)
- Heuristic score: **27.5/100**
  - *message_vs_diff_size* (25): Large diff (193 lines) with a short message (7 words) — more typical of a human committing quickly without narrating the change.
  - *commit_timing* (30): 104 min gap since the previous commit — consistent with normal human working pace.
- LLM judge: not run (sampling or `--no-llm`).

### `a5b3879154` — The Share Your Mission form now submits to the Act Angel AI WEB backend.
- Author: Radhikesh Kumar — 2026-10-03T15:06:56
- Diff size: +29/-29 across 2 file(s)
- Heuristic score: **52.5/100**
  - *message_vs_diff_size* (75): Large diff (58 lines) paired with a detailed message (260 words) — consistent with AI-drafted commit messages that narrate the change in full sentences.
  - *commit_timing* (30): 214 min gap since the previous commit — consistent with normal human working pace.
- LLM judge: not run (sampling or `--no-llm`).

### `ccc08c85d5` — nav bar hire an angel dropdown multiple ui versions added
- Author: npltech — 2026-10-03T11:33:13
- Diff size: +781/-0 across 2 file(s)
- Heuristic score: **27.5/100**
  - *message_vs_diff_size* (25): Large diff (781 lines) with a short message (10 words) — more typical of a human committing quickly without narrating the change.
  - *commit_timing* (30): 2514 min gap since the previous commit — consistent with normal human working pace.
- LLM judge: not run (sampling or `--no-llm`).

### `933d2ea416` — updated hire angel menu items
- Author: npltech — 2026-10-01T17:38:43
- Diff size: +6/-5 across 1 file(s)
- Heuristic score: **35.0/100**
  - *message_vs_diff_size* (40): Small diff (11 lines), short message (5 words) — no strong signal either way.
  - *commit_timing* (30): 13 min gap since the previous commit — consistent with normal human working pace.
- LLM judge: not run (sampling or `--no-llm`).

### `b10369975d` — updated
- Author: npltech — 2026-10-01T17:25:58
- Diff size: +22/-12 across 3 file(s)
- Heuristic score: **35.0/100**
  - *message_vs_diff_size* (40): Small diff (34 lines), short message (1 words) — no strong signal either way.
  - *commit_timing* (30): 14 min gap since the previous commit — consistent with normal human working pace.
- LLM judge score: **75/100**
  - The commit includes several substantial UI/UX tweaks across two components and a type definition file, plus a vague commit message. The changes exhibit unusually uniform structure, with many in-depth inline explanations for UI decisions (e.g., LiveDemoSection and MobileNav alterations) that go beyond what a typical hand-edited patch would require for a minor update, suggesting AI involvement in drafting comments or even code patterns. The behavioral changes (dynamic className based on persona, 2-row card layout on desktop, hover effects, and typography tweaks) are coherent and comprehensive, and the next-env.d.ts change (switching to dev/types/routes.d.ts) reads like a targeted fix that might come from tooling or automated guidance. However, the commit message 'updated' is extremely generic and under-describes the substantial changes, which is inconsistent with the magnitude of the diff and hints at AI-generated or assisted content for the patch notes more than a human-authored summary would. Overall, the diff shows substantial AI involvement in both code structure and commentary, with a mismatch between a minimal message and a large, well-structured diff.

Key signals:
- LiveDemoSection uses a dynamic className with a template string and explicit variant logic; adds inline comments explaining UI pairing logic.
- MobileNav changes: grid layout moved from 3 cols with responsive tweaks to a fixed 3-col grid with richer hover/transition styling and larger avatar/text sizing; added group-hover scale and animation classes.
- Extensive inline commentary describing design rationale and references to external concepts (e.g., 11x.ai nav), which is atypical for a human-only patch and more characteristic of AI-assisted commentary.
- next-env.d.ts modification is targeted and non-trivial, indicating an environment/tooling fix that could come from generated guidance.
- Commit message is generic and does not reflect the scope of changes, which often happens with AI-generated patches.

Disagreement between message and diff: The message “updated” does not hint at the breadth of UI/UX changes and rationale-heavy comments visible in the diff, and thus undersells the work. The diff itself shows cohesive, template-like patterns and extensive comments that feel AI-influenced rather than a minimal human patch.
  - Key signals: dynamic className with persona variant, 3-column grid with 2-row wrap, hover transitions and avatar scaling, extensive inline design rationale comments, generic commit message vs substantial diff
- Blended score: **55.0/100**
  - Heuristic and LLM layers disagree by >=30 points — treat this commit's score as uncertain.

### `48c556b363` — Merge branch 'main' of https://github.com/CloudSteer-Technology/act-ange
- Author: npltech — 2026-10-01T17:12:00
- Diff size: +231/-24 across 3 file(s)
- Heuristic score: **52.5/100**
  - *message_vs_diff_size* (25): Large diff (255 lines) with a short message (5 words) — more typical of a human committing quickly without narrating the change.
  - *commit_timing* (80): Only 20s after the previous commit — faster than a typical manual edit-test-commit cycle.
- LLM judge: not run (sampling or `--no-llm`).

### `250e613d2d` — navbar updated
- Author: npltech — 2026-10-01T17:11:40
- Diff size: +0/-39 across 1 file(s)
- Heuristic score: **35.0/100**
  - *message_vs_diff_size* (40): Small diff (39 lines), short message (2 words) — no strong signal either way.
  - *commit_timing* (30): 46 min gap since the previous commit — consistent with normal human working pace.
- LLM judge: not run (sampling or `--no-llm`).

### `8bee1a3b84` — Fixed the crash: share-your-mission-form.tsx had a dangling setMailtoHre
- Author: Radhikesh Kumar — 2026-10-01T16:25:35
- Diff size: +25/-112 across 2 file(s)
- Heuristic score: **65.0/100**
  - *message_vs_diff_size* (75): Large diff (137 lines) paired with a detailed message (197 words) — consistent with AI-drafted commit messages that narrate the change in full sentences.
  - *commit_timing* (55): 9.6 min after the previous commit — plausible for either a fast human pass or an AI-assisted one.
- LLM judge: not run (sampling or `--no-llm`).

### `e1073a8196` — Merge branch 'main' of https://github.com/CloudSteer-Technology/act-ange
- Author: Radhikesh Kumar — 2026-10-01T16:15:58
- Diff size: +350/-65 across 12 file(s)
- Heuristic score: **40.0/100**
  - *message_vs_diff_size* (25): Large diff (415 lines) with a short message (5 words) — more typical of a human committing quickly without narrating the change.
  - *commit_timing* (55): 2.1 min after the previous commit — plausible for either a fast human pass or an AI-assisted one.
- LLM judge: not run (sampling or `--no-llm`).

### `02c6cdf3c4` — Merge branch 'main' of https://github.com/CloudSteer-Technology/act-ange
- Author: Radhikesh Kumar — 2026-10-01T16:13:52
- Diff size: +353/-146 across 7 file(s)
- Heuristic score: **27.5/100**
  - *message_vs_diff_size* (25): Large diff (499 lines) with a short message (5 words) — more typical of a human committing quickly without narrating the change.
  - *commit_timing* (30): 1112 min gap since the previous commit — consistent with normal human working pace.
- LLM judge score: **68/100**
  - The diff shows a substantial and cohesive rewrite of a complex form with new TypeScript types, validation logic, and UI state handling. Elements that feel AI-assisted include (1) a complete field validation layer with FieldName union type, isValidUrl, validateField, and a FieldError component, (2) a generalized fieldClass function with error vs okBorder branches, (3) a dedicated MISSION_EMAIL constant and a fairly opinionated flow description in comments, (4) structured fieldValues object and onChange/onBlur handlers with consistent setter usage, and (5) refactored class name constants and a consistent, defensive approach to user feedback. The changes are unusually uniform and thorough for a single commit, with explicit typing and edge-case handling (URL validation, email regex, blur/live validation). This strongly suggests AI-assisted generation or heavy scaffolding. While a human could produce this, the density and consistency of the validation logic and types are more indicative of tooling help or an LLM-generated scaffold.

Commit message vs. diff: The message mentions merging from main and a narrative of the form’s purpose, but the diff reveals a redesigned, validation-rich form (backend submission path in comments, URL checks, etc.). The message underplays the structural and behavioral enhancements visible in the code, which aligns with a mixed or AI-influenced change rather than a small manual tweak.
  - Key signals: type-safe field validation, FieldName union type, isValidUrl + validateField, FieldError component, fieldValues mapping for all fields, fieldClass function with error styling, extensive UI state handling and comments
  - Note: diff was truncated for length before being sent to the LLM judge.
- Blended score: **47.8/100**
  - Heuristic and LLM layers disagree by >=30 points — treat this commit's score as uncertain.

### `299a1f4615` — Wire the NPO intake form to a real backend, alongside the mailto brief
- Author: Tahir Hameed — 2026-09-30T21:42:15
- Diff size: +156/-1 across 3 file(s)
- Heuristic score: **52.5/100**
  - *message_vs_diff_size* (75): Large diff (157 lines) paired with a detailed message (74 words) — consistent with AI-drafted commit messages that narrate the change in full sentences.
  - *commit_timing* (30): 712 min gap since the previous commit — consistent with normal human working pace.
- LLM judge: not run (sampling or `--no-llm`).

### `4497913256` — Merge branch 'main' of https://github.com/CloudSteer-Technology/act-ange
- Author: npltech — 2026-09-30T09:50:14
- Diff size: +147/-16 across 7 file(s)
- Heuristic score: **52.5/100**
  - *message_vs_diff_size* (25): Large diff (163 lines) with a short message (5 words) — more typical of a human committing quickly without narrating the change.
  - *commit_timing* (80): Only 16s after the previous commit — faster than a typical manual edit-test-commit cycle.
- LLM judge: not run (sampling or `--no-llm`).

### `3f22a6082f` — hire an angel dropdown menu ui fixes
- Author: npltech — 2026-09-30T09:49:58
- Diff size: +13/-8 across 2 file(s)
- Heuristic score: **35.0/100**
  - *message_vs_diff_size* (40): Small diff (21 lines), short message (7 words) — no strong signal either way.
  - *commit_timing* (30): 736 min gap since the previous commit — consistent with normal human working pace.
- LLM judge: not run (sampling or `--no-llm`).

### `34eb0e0f96` — Restore API-safe trailing-slash handling via proxy.ts
- Author: Tahir Hameed — 2026-09-29T21:33:53
- Diff size: +52/-17 across 2 file(s)
- Heuristic score: **52.5/100**
  - *message_vs_diff_size* (75): Large diff (69 lines) paired with a detailed message (62 words) — consistent with AI-drafted commit messages that narrate the change in full sentences.
  - *commit_timing* (30): 83 min gap since the previous commit — consistent with normal human working pace.
- LLM judge: not run (sampling or `--no-llm`).

### `e48a269147` — Fix the trailing-slash redirect looping every page to itself
- Author: Tahir Hameed — 2026-09-29T20:10:54
- Diff size: +16/-37 across 2 file(s)
- Heuristic score: **27.5/100**
  - *message_vs_diff_size* (25): Large diff (53 lines) with a short message (9 words) — more typical of a human committing quickly without narrating the change.
  - *commit_timing* (30): 88 min gap since the previous commit — consistent with normal human working pace.
- LLM judge: not run (sampling or `--no-llm`).

### `c7f6c35ae6` — Open Hope Angel outbound calls with a fixed greeting
- Author: Tahir Hameed — 2026-09-29T18:43:15
- Diff size: +36/-5 across 4 file(s)
- Heuristic score: **27.5/100**
  - *message_vs_diff_size* (25): Large diff (41 lines) with a short message (9 words) — more typical of a human committing quickly without narrating the change.
  - *commit_timing* (30): 41 min gap since the previous commit — consistent with normal human working pace.
- LLM judge score: **72/100**
  - The commit shows a cohesive feature addition: introducing a controlled source parameter (source = 'hope-angel') across frontend and backend to steer outbound calls/WhatsApp opening. There are multiple files updated with consistent handling: API route validates source, frontend passes source down to components, and a known-sources whitelist is enforced on both client and server. The comments are explicit and instructional, with defensive checks and the explicit mention of how the source affects the AI/opening line. This pattern suggests substantial, deliberate engineering with clear structure and documentation, which leans toward substantial AI involvement or at least guidance-driven development. However, the changes are reasonably scoped and include hand-authored rationale and integration notes that feel like human-driven design intent, making it unlikely to be purely AI-generated from a single prompt. Overall: substantial AI involvement is plausible, but not definitive as fully AI-generated; more likely a mix or AI-assisted with human polish. The commit message itself is concise and generic, not overfitting to the diff, which aligns with mixed authorship rather than an AI-only commit.
  - Key signals: consistent cross-file plumbing for a new 'source' parameter, whitelist validation on server/client, comments describing design intent, pass-through in UI component props and API payload
- Blended score: **49.8/100**
  - Heuristic and LLM layers disagree by >=30 points — treat this commit's score as uncertain.

### `52491f81ac` — Fix resend sending the same OTP code + stop the trailing-slash redirect 
- Author: Tahir Hameed — 2026-09-29T18:02:07
- Diff size: +96/-10 across 4 file(s)
- Heuristic score: **52.5/100**
  - *message_vs_diff_size* (75): Large diff (106 lines) paired with a detailed message (16 words) — consistent with AI-drafted commit messages that narrate the change in full sentences.
  - *commit_timing* (30): 202 min gap since the previous commit — consistent with normal human working pace.
- LLM judge: not run (sampling or `--no-llm`).

### `e908f24b5c` — the person pages hero section updated
- Author: npltech — 2026-09-29T14:40:33
- Diff size: +5/-5 across 1 file(s)
- Heuristic score: **35.0/100**
  - *message_vs_diff_size* (40): Small diff (10 lines), short message (6 words) — no strong signal either way.
  - *commit_timing* (30): 97 min gap since the previous commit — consistent with normal human working pace.
- LLM judge: not run (sampling or `--no-llm`).

### `eab3c2ef46` — Updated AdminOrganizationCreate.tsx the same way: outer form is now a re
- Author: Radhikesh Kumar — 2026-09-29T13:03:23
- Diff size: +149/-60 across 2 file(s)
- Heuristic score: **52.5/100**
  - *message_vs_diff_size* (75): Large diff (209 lines) paired with a detailed message (48 words) — consistent with AI-drafted commit messages that narrate the change in full sentences.
  - *commit_timing* (30): 1280 min gap since the previous commit — consistent with normal human working pace.
- LLM judge: not run (sampling or `--no-llm`).

### `ad2d1b0253` — hope ange page updated
- Author: npltech — 2026-09-28T15:42:55
- Diff size: +295/-143 across 6 file(s)
- Heuristic score: **27.5/100**
  - *message_vs_diff_size* (25): Large diff (438 lines) with a short message (4 words) — more typical of a human committing quickly without narrating the change.
  - *commit_timing* (30): 78 min gap since the previous commit — consistent with normal human working pace.
- LLM judge: not run (sampling or `--no-llm`).

### `8514ddac44` — u
- Author: npltech — 2026-09-28T14:25:01
- Diff size: +1/-2 across 1 file(s)
- Heuristic score: **35.0/100**
  - *message_vs_diff_size* (40): Small diff (3 lines), short message (1 words) — no strong signal either way.
  - *commit_timing* (30): 899 min gap since the previous commit — consistent with normal human working pace.
- LLM judge score: **28/100**
  - The diff shows a small, targeted change: swapping two import paths in next-env.d.ts from ".next/types/" to ".next/dev/types/" and removing two lines in favor of one. This is a minimal, mechanical edit typical of hand-tweaked config adjustments. The commit message is a single letter/character “u,” which is not descriptive and more resembles a rushed or accidental commit rather than a semantically meaningful, generated message. The combination suggests mostly human work with a tiny, straightforward tweak rather than a fully AI-generated, boilerplate-heavy commit. The message does not align with an AI-generated pattern (which would typically include a clearer, structured description). 

Disagreement between message and diff: The message is extremely terse and uninformative, while the diff represents an intentional path adjustment in a config file. The diff itself is not large or complex enough to imply heavy AI-generation, but the mismatch is in the commit message’s lack of context and apparent accidental nature. 
  - Key signals: tiny diff, path import changes, odd commit message 'u'
- Blended score: **31.5/100**

### `962ce2e336` — Minor fixes
- Author: Radhikesh Kumar — 2026-09-27T23:25:44
- Diff size: +45/-44 across 2 file(s)
- Heuristic score: **27.5/100**
  - *message_vs_diff_size* (25): Large diff (89 lines) with a short message (2 words) — more typical of a human committing quickly without narrating the change.
  - *commit_timing* (30): 36 min gap since the previous commit — consistent with normal human working pace.
- LLM judge: not run (sampling or `--no-llm`).

### `9829d9a6fc` — Requested changes.
- Author: Radhikesh Kumar — 2026-09-27T22:49:49
- Diff size: +631/-257 across 6 file(s)
- Heuristic score: **27.5/100**
  - *message_vs_diff_size* (25): Large diff (888 lines) with a short message (2 words) — more typical of a human committing quickly without narrating the change.
  - *commit_timing* (30): 115 min gap since the previous commit — consistent with normal human working pace.
- LLM judge: not run (sampling or `--no-llm`).

### `868d58c413` — ACTANGEL_EMAIL_ASSISTANT_ID
- Author: Radhikesh Kumar — 2026-09-27T20:55:18
- Diff size: +956/-98 across 10 file(s)
- Heuristic score: **27.5/100**
  - *message_vs_diff_size* (25): Large diff (1054 lines) with a short message (1 words) — more typical of a human committing quickly without narrating the change.
  - *commit_timing* (30): 7571 min gap since the previous commit — consistent with normal human working pace.
- LLM judge: not run (sampling or `--no-llm`).

### `9a3b5dbdea` — made dropdaown menu opaque
- Author: npltech — 2026-09-22T14:44:46
- Diff size: +18/-3 across 1 file(s)
- Heuristic score: **35.0/100**
  - *message_vs_diff_size* (40): Small diff (21 lines), short message (4 words) — no strong signal either way.
  - *commit_timing* (30): 1251 min gap since the previous commit — consistent with normal human working pace.
- LLM judge: not run (sampling or `--no-llm`).

### `d0f175fa5c` — phone number added
- Author: npltech — 2026-09-21T17:53:34
- Diff size: +6/-0 across 1 file(s)
- Heuristic score: **47.5/100**
  - *message_vs_diff_size* (40): Small diff (6 lines), short message (3 words) — no strong signal either way.
  - *commit_timing* (55): 5.9 min after the previous commit — plausible for either a fast human pass or an AI-assisted one.
- LLM judge score: **55/100**
  - The change is a small, straightforward UI tweak: adding a tel: link and display text for a phone number in an existing contact page. The commit message is generic and descriptive of the change. The code style is clean but not unusually regimented or boilerplate-heavy, suggesting a human-made edit with routine UI adjustments. There are no signs of overly exhaustive defensive coding or unusual structure that would indicate heavy AI generation. The diff aligns with the simple commit message.
  - Key signals: small UI change, tel: link added, minor styling/structure consistency, no complex logic or boilerplate, commit message matches change
- Blended score: **51.2/100**

### `e74f87ebe4` — tools section icons updated
- Author: npltech — 2026-09-21T17:47:42
- Diff size: +61/-23 across 16 file(s)
- Heuristic score: **27.5/100**
  - *message_vs_diff_size* (25): Large diff (84 lines) with a short message (4 words) — more typical of a human committing quickly without narrating the change.
  - *commit_timing* (30): 133 min gap since the previous commit — consistent with normal human working pace.
- LLM judge: not run (sampling or `--no-llm`).

### `606b6e0596` — tools section updated
- Author: npltech — 2026-09-21T15:34:34
- Diff size: +309/-43 across 17 file(s)
- Heuristic score: **27.5/100**
  - *message_vs_diff_size* (25): Large diff (352 lines) with a short message (3 words) — more typical of a human committing quickly without narrating the change.
  - *commit_timing* (30): 3190 min gap since the previous commit — consistent with normal human working pace.
- LLM judge: not run (sampling or `--no-llm`).

### `ad072ded84` — ui update of all your tools section
- Author: npltech — 2026-09-19T10:24:45
- Diff size: +48/-168 across 15 file(s)
- Heuristic score: **27.5/100**
  - *message_vs_diff_size* (25): Large diff (216 lines) with a short message (7 words) — more typical of a human committing quickly without narrating the change.
  - *commit_timing* (30): 1200 min gap since the previous commit — consistent with normal human working pace.
- LLM judge: not run (sampling or `--no-llm`).

### `e58bab10ab` — updated circular ring section
- Author: npltech — 2026-09-18T14:25:06
- Diff size: +2/-3 across 1 file(s)
- Heuristic score: **35.0/100**
  - *message_vs_diff_size* (40): Small diff (5 lines), short message (4 words) — no strong signal either way.
  - *commit_timing* (30): 293 min gap since the previous commit — consistent with normal human working pace.
- LLM judge: not run (sampling or `--no-llm`).

### `9e9a041619` — hire an angel 4 pages hero section blank space covered
- Author: npltech — 2026-09-18T09:32:34
- Diff size: +14/-2 across 1 file(s)
- Heuristic score: **35.0/100**
  - *message_vs_diff_size* (40): Small diff (16 lines), short message (10 words) — no strong signal either way.
  - *commit_timing* (30): 13 min gap since the previous commit — consistent with normal human working pace.
- LLM judge score: **45/100**
  - The changes are surgically targeted UI tweaks: adding a new inline-block card for 'Business Outcome' with a dense, highly descriptive comment about responsive behavior, and temporarily commenting out a similar card. The code style (Tailwind-like classes) and the presence of inline explanations in the code suggest careful refinement typical of human edits, though the comments are unusually thorough. The commit message is vague and doesn’t clearly describe the UI adjustments, which is more characteristic of a human-focused commit note. Overall, the work reads as largely human with possible lightweight tooling aid, not a fully AI-generated all-at-once commit.
  - Key signals: new inline-block card with detailed inline comment, commented-out block of previously used markup, verbose, self-explanatory inline comments about responsive behavior, vague commit message not outlining specific UI changes
- Blended score: **40.0/100**

### `325cc7a96d` — ui issues fixed
- Author: npltech — 2026-09-18T09:19:16
- Diff size: +8/-1 across 1 file(s)
- Heuristic score: **35.0/100**
  - *message_vs_diff_size* (40): Small diff (9 lines), short message (3 words) — no strong signal either way.
  - *commit_timing* (30): 1341 min gap since the previous commit — consistent with normal human working pace.
- LLM judge: not run (sampling or `--no-llm`).

### `5d4eee3d3e` — ui updates
- Author: npltech — 2026-09-17T10:58:40
- Diff size: +241/-208 across 19 file(s)
- Heuristic score: **27.5/100**
  - *message_vs_diff_size* (25): Large diff (449 lines) with a short message (2 words) — more typical of a human committing quickly without narrating the change.
  - *commit_timing* (30): 801 min gap since the previous commit — consistent with normal human working pace.
- LLM judge: not run (sampling or `--no-llm`).

### `2e6c1f8b13` — email updated
- Author: npltech — 2026-09-16T21:37:43
- Diff size: +12/-12 across 6 file(s)
- Heuristic score: **47.5/100**
  - *message_vs_diff_size* (40): Small diff (24 lines), short message (2 words) — no strong signal either way.
  - *commit_timing* (55): 9.2 min after the previous commit — plausible for either a fast human pass or an AI-assisted one.
- LLM judge: not run (sampling or `--no-llm`).

### `9e8fc39b3d` — Merge branch 'staging'
- Author: npltech — 2026-09-16T21:28:34
- Diff size: +1256/-315 across 22 file(s)
- Heuristic score: **52.5/100**
  - *message_vs_diff_size* (25): Large diff (1571 lines) with a short message (3 words) — more typical of a human committing quickly without narrating the change.
  - *commit_timing* (80): Only 59s after the previous commit — faster than a typical manual edit-test-commit cycle.
- LLM judge: not run (sampling or `--no-llm`).

### `0495ae06e6` — changes updated
- Author: npltech — 2026-09-16T21:27:35
- Diff size: +151/-118 across 5 file(s)
- Heuristic score: **27.5/100**
  - *message_vs_diff_size* (25): Large diff (269 lines) with a short message (2 words) — more typical of a human committing quickly without narrating the change.
  - *commit_timing* (30): 165 min gap since the previous commit — consistent with normal human working pace.
- LLM judge: not run (sampling or `--no-llm`).

### `79612b2666` — updated live preview image
- Author: npltech — 2026-09-16T18:43:03
- Diff size: +43/-13 across 2 file(s)
- Heuristic score: **27.5/100**
  - *message_vs_diff_size* (25): Large diff (56 lines) with a short message (4 words) — more typical of a human committing quickly without narrating the change.
  - *commit_timing* (30): 34 min gap since the previous commit — consistent with normal human working pace.
- LLM judge score: **68/100**
  - The diff includes a substantial refactor of the live preview image handling: adding new Backdrop/Feather constants, changing the animation keyframes values, and a fairly large restructuring of the JSX for the Live Demo photo to use a dedicated backdrop, masking, and a more complex responsive frame. The CSS includes extended comments describing the Ken Burns-like motion and the rationale for motion ranges. The commit message itself (“updated live preview image”) is terse and does not reflect the depth of changes, which suggests the message underreports the scope.

Indicators suggesting AI assistance (relative to human-only work):
- Extremely thorough, consistent commentary in CSS and explanatory in-code comments (with explicit numeric motion ranges and design rationale).
- A cohesive, end-to-end small feature that touches CSS, assets (backdrop/feather textures), and DOM structure in a single commit, which is a common pattern for AI-assisted or template-driven changes.
- The new constants (PHOTO_BACKDROP, PHOTO_FEATHER) and the masking trick (maskImage) are relatively intricate and show a level of patterning that can accompany AI-generated code templates.

Indicators suggesting human work (or mixed):
- The commit message is minimal and does not describe the breadth of changes, which is more typical of a hand-crafted commit that the author forgot to update with a descriptive message or an initial AI-generated patch subsequently edited by a human.
- Some stylistic consistency could be human-driven as well (idiosyncratic phrasing in comments is still within human norms).

Overall: the changes are substantial and stylistically polished, leaning toward a high likelihood of AI-assisted or generated scaffolding, but not unequivocally AI-generated. The mismatch between the brief commit message and the breadth of edits is a notable signal. I rate 68 to reflect substantial AI involvement without claiming near-certainty.
  - Key signals: large CSS/TSX refactor in a single commit, verbose, structured comments explaining design choices, new constants for visual styling (PHOTO_BACKDROP, PHOTO_FEATHER), masking and animation customization beyond minimal requirements, commit message under-describes the changes
- Blended score: **47.8/100**
  - Heuristic and LLM layers disagree by >=30 points — treat this commit's score as uncertain.

### `b021c2d019` — profile images made zoomed out
- Author: npltech — 2026-09-16T18:08:38
- Diff size: +4/-4 across 1 file(s)
- Heuristic score: **35.0/100**
  - *message_vs_diff_size* (40): Small diff (8 lines), short message (5 words) — no strong signal either way.
  - *commit_timing* (30): 48 min gap since the previous commit — consistent with normal human working pace.
- LLM judge: not run (sampling or `--no-llm`).

### `c5d689d971` — update live preview card
- Author: npltech — 2026-09-16T17:20:24
- Diff size: +116/-106 across 1 file(s)
- Heuristic score: **27.5/100**
  - *message_vs_diff_size* (25): Large diff (222 lines) with a short message (4 words) — more typical of a human committing quickly without narrating the change.
  - *commit_timing* (30): 173 min gap since the previous commit — consistent with normal human working pace.
- LLM judge: not run (sampling or `--no-llm`).

### `b5ea9eb59e` — new Progress with Purpose page created
- Author: npltech — 2026-09-16T14:27:37
- Diff size: +187/-0 across 2 file(s)
- Heuristic score: **27.5/100**
  - *message_vs_diff_size* (25): Large diff (187 lines) with a short message (6 words) — more typical of a human committing quickly without narrating the change.
  - *commit_timing* (30): 152 min gap since the previous commit — consistent with normal human working pace.
- LLM judge: not run (sampling or `--no-llm`).

### `211fafa322` — ui updates implemented
- Author: npltech — 2026-09-16T11:55:50
- Diff size: +12/-6 across 1 file(s)
- Heuristic score: **35.0/100**
  - *message_vs_diff_size* (40): Small diff (18 lines), short message (3 words) — no strong signal either way.
  - *commit_timing* (30): 23 min gap since the previous commit — consistent with normal human working pace.
- LLM judge: not run (sampling or `--no-llm`).

### `704b5ed414` — ui fixes completed
- Author: npltech — 2026-09-16T11:33:17
- Diff size: +145/-70 across 5 file(s)
- Heuristic score: **27.5/100**
  - *message_vs_diff_size* (25): Large diff (215 lines) with a short message (3 words) — more typical of a human committing quickly without narrating the change.
  - *commit_timing* (30): 124 min gap since the previous commit — consistent with normal human working pace.
- LLM judge score: **65/100**
  - The diff shows a cohesive, multi-file UI polish with substantive structural changes (new Live Demo section animation, responsive grid tweaks, a reusable pillClass utility, and a custom ping-sm animation inserted into globals.css). There are thorough comments explaining UI decisions and animation behavior, plus consistent refactors across page.tsx, contact page, and hire-an-angel components. This level of consistency and documentation is more than a typical small human patch and resembles patterns sometimes produced or heavily assisted by AI coding tools that generate boilerplate, utilities, and verbose comments intended for maintainability.

Specific signals:
- Introduction of a new pillClass(active) helper with template-literal classes and boolean-driven styling, used to style scenario/channel pills.
- Addition of a new LivePreview section with a Ken Burns-style animation (live-preview-motion) and an animate-[live-preview-motion_9s_ease-in-out_infinite] class, plus related DOM structure adjustments and explanatory comments.
- Creation of a smaller ping animation (ping-sm) in globals.css with a detailed comment block describing its purpose and usage, which is unusually thorough for a single commit.
- Reworking of layouts to use min-h constraints and to switch from fixed aspect-square cards to stretch-enabled grid, including added id="live-preview" and scroll-mt utilities.
- Consistent update of contact mailto links across multiple files to angel@actangel.com, indicating a targeted, global change rather than isolated edits.

Disagreement between message and diff: The commit message “ui fixes completed” is very generic and does not hint at the breadth and depth of the changes seen in the diff (new components, animations, and CSS helpers). The diff reads like a substantial, cohesive feature or overhaul rather than a minor fix, which slightly under-reports the magnitude of changes in the message.
  - Key signals: new pillClass(active) helper, Live preview Ken Burns animation (live-preview-motion), ping-sm keyframes added in globals.css, layout/grid and card adjustments, global mailto address changes to angel@actangel.com
  - Note: diff was truncated for length before being sent to the LLM judge.
- Blended score: **46.2/100**
  - Heuristic and LLM layers disagree by >=30 points — treat this commit's score as uncertain.

### `f376e76bfc` — u
- Author: npltech — 2026-09-16T09:29:29
- Diff size: +1/-3 across 2 file(s)
- Heuristic score: **35.0/100**
  - *message_vs_diff_size* (40): Small diff (4 lines), short message (1 words) — no strong signal either way.
  - *commit_timing* (30): 1358 min gap since the previous commit — consistent with normal human working pace.
- LLM judge: not run (sampling or `--no-llm`).

### `13a6422d76` — update
- Author: npltech — 2026-09-15T10:51:37
- Diff size: +1/-0 across 1 file(s)
- Heuristic score: **35.0/100**
  - *message_vs_diff_size* (40): Small diff (1 lines), short message (1 words) — no strong signal either way.
  - *commit_timing* (30): 12 min gap since the previous commit — consistent with normal human working pace.
- LLM judge: not run (sampling or `--no-llm`).

### `641fc02b86` — Merge branch 'main' into staging
- Author: npltech — 2026-09-15T10:39:39
- Diff size: +419/-136 across 2 file(s)
- Heuristic score: **52.5/100**
  - *message_vs_diff_size* (25): Large diff (555 lines) with a short message (5 words) — more typical of a human committing quickly without narrating the change.
  - *commit_timing* (80): Only 31s after the previous commit — faster than a typical manual edit-test-commit cycle.
- LLM judge: not run (sampling or `--no-llm`).

### `d9a9029bdc` — second animation removed
- Author: npltech — 2026-09-15T10:39:08
- Diff size: +420/-138 across 3 file(s)
- Heuristic score: **27.5/100**
  - *message_vs_diff_size* (25): Large diff (558 lines) with a short message (3 words) — more typical of a human committing quickly without narrating the change.
  - *commit_timing* (30): 5429 min gap since the previous commit — consistent with normal human working pace.
- LLM judge: not run (sampling or `--no-llm`).

### `799fa400e7` — 4 persona pages updated
- Author: npltech — 2026-09-11T16:10:07
- Diff size: +300/-104 across 14 file(s)
- Heuristic score: **27.5/100**
  - *message_vs_diff_size* (25): Large diff (404 lines) with a short message (4 words) — more typical of a human committing quickly without narrating the change.
  - *commit_timing* (30): 37 min gap since the previous commit — consistent with normal human working pace.
- LLM judge score: **78/100**
  - The commit contains a substantial, self-contained feature addition: a full LiveDemoSection with interactive UI, new constants (CHANNELS, PHONE_GLYPH_PATH), a reusable CtaButtons component, and narrative comments explaining design choices. The diff reflects large, cohesive functionality rather than a tiny patch. The commit message (‘4 persona pages updated’) is generic and doesn’t reflect the scale of the code change, which suggests the message underreports the work. While a human could author this, the breadth, consistency, and explanatory comments are very aligned with a template-driven or AI-assisted expansion, making it plausible that AI assisted or generated a significant portion of the code. There are no obvious typos or egregious inconsistencies, but the level of polish and breadth across a single commit hints at AI involvement more than routine manual edits.
  - Key signals: Large, cohesive feature implemented in a single commit (LiveDemoSection, CHANNELS, PHONE_GLYPH_PATH, CtaButtons)., Verbose, instructional/block comments describing design decisions and references (e.g., detailed docstring-like comment for LiveDemoSection)., Uniform, modular React/TSX patterns with plenty of UI state handling and styled components, typical of auto-generated templates., New typed data usage (Persona, PersonaId) and explicit types for props, indicating a well-structured addition., Commit message is generic and underrepresents the scope of the diff.
  - Note: diff was truncated for length before being sent to the LLM judge.
- Blended score: **52.8/100**
  - Heuristic and LLM layers disagree by >=30 points — treat this commit's score as uncertain.

### `a9a0dc60e5` — navbar updated
- Author: npltech — 2026-09-11T15:33:33
- Diff size: +177/-57 across 4 file(s)
- Heuristic score: **27.5/100**
  - *message_vs_diff_size* (25): Large diff (234 lines) with a short message (2 words) — more typical of a human committing quickly without narrating the change.
  - *commit_timing* (30): 56 min gap since the previous commit — consistent with normal human working pace.
- LLM judge: not run (sampling or `--no-llm`).

### `787e26abc6` — staging branch updated
- Author: npltech — 2026-09-11T14:37:22
- Diff size: +1/-1 across 1 file(s)
- Heuristic score: **60.0/100**
  - *message_vs_diff_size* (40): Small diff (2 lines), short message (3 words) — no strong signal either way.
  - *commit_timing* (80): Only 76s after the previous commit — faster than a typical manual edit-test-commit cycle.
- LLM judge: not run (sampling or `--no-llm`).

### `9b693719a9` — staging branch update testing
- Author: npltech — 2026-09-11T14:36:06
- Diff size: +1/-1 across 1 file(s)
- Heuristic score: **35.0/100**
  - *message_vs_diff_size* (40): Small diff (2 lines), short message (4 words) — no strong signal either way.
  - *commit_timing* (30): 12 min gap since the previous commit — consistent with normal human working pace.
- LLM judge: not run (sampling or `--no-llm`).

### `ef510bad7f` — staging branch created
- Author: npltech — 2026-09-11T14:23:56
- Diff size: +1/-1 across 1 file(s)
- Heuristic score: **60.0/100**
  - *message_vs_diff_size* (40): Small diff (2 lines), short message (3 words) — no strong signal either way.
  - *commit_timing* (80): Only 28s after the previous commit — faster than a typical manual edit-test-commit cycle.
- LLM judge: not run (sampling or `--no-llm`).

### `c17bc089b5` — updates
- Author: npltech — 2026-09-11T14:23:28
- Diff size: +1/-1 across 1 file(s)
- Heuristic score: **35.0/100**
  - *message_vs_diff_size* (40): Small diff (2 lines), short message (1 words) — no strong signal either way.
  - *commit_timing* (30): 1251 min gap since the previous commit — consistent with normal human working pace.
- LLM judge: not run (sampling or `--no-llm`).

### `6357eec87a` — Merge pull request #3 from CloudSteer-Technology/feature/WhatsApp
- Author: Radhikesh Kumar — 2026-09-10T17:32:01
- Diff size: +53/-16 across 4 file(s)
- Heuristic score: **27.5/100**
  - *message_vs_diff_size* (25): Large diff (69 lines) with a short message (8 words) — more typical of a human committing quickly without narrating the change.
  - *commit_timing* (30): 84 min gap since the previous commit — consistent with normal human working pace.
- LLM judge score: **0/100**
  - Insufficient data to judge the AI involvement. The provided text only contains a vague merge commit message and the words 'Diff:' with no actual diff content. Without the code changes, we cannot assess structure, comments, error handling, or any other telltale signs of AI-generated code. The commit message itself is a generic merge PR title and does not reflect substantive description.
  - Key signals: no diff content, generic merge message, no changed files or code patterns seen
- Blended score: **13.8/100**

### `366d47bc28` — Email functionality implementation.
- Author: Radhikesh Kumar — 2026-09-10T16:08:08
- Diff size: +50/-13 across 2 file(s)
- Heuristic score: **27.5/100**
  - *message_vs_diff_size* (25): Large diff (63 lines) with a short message (3 words) — more typical of a human committing quickly without narrating the change.
  - *commit_timing* (30): 268 min gap since the previous commit — consistent with normal human working pace.
- LLM judge: not run (sampling or `--no-llm`).

### `7a8dd76d63` — Merge branch 'main' of https://github.com/CloudSteer-Technology/act-ange
- Author: Radhikesh Kumar — 2026-09-10T11:40:23
- Diff size: +304/-90 across 8 file(s)
- Heuristic score: **27.5/100**
  - *message_vs_diff_size* (25): Large diff (394 lines) with a short message (7 words) — more typical of a human committing quickly without narrating the change.
  - *commit_timing* (30): 2976 min gap since the previous commit — consistent with normal human working pace.
- LLM judge: not run (sampling or `--no-llm`).

### `b2c867f3a4` — code merged with npl_dev
- Author: npltech — 2026-09-08T10:04:35
- Diff size: +1/-2 across 1 file(s)
- Heuristic score: **47.5/100**
  - *message_vs_diff_size* (40): Small diff (3 lines), short message (4 words) — no strong signal either way.
  - *commit_timing* (55): 3.2 min after the previous commit — plausible for either a fast human pass or an AI-assisted one.
- LLM judge: not run (sampling or `--no-llm`).

### `5eaeaba296` — Merge branch 'main' into npl_dev
- Author: npltech — 2026-09-08T10:01:24
- Diff size: +581/-374 across 5 file(s)
- Heuristic score: **27.5/100**
  - *message_vs_diff_size* (25): Large diff (955 lines) with a short message (5 words) — more typical of a human committing quickly without narrating the change.
  - *commit_timing* (30): 1166 min gap since the previous commit — consistent with normal human working pace.
- LLM judge: not run (sampling or `--no-llm`).

### `f5ffcfa2e8` — content updated on hire an angel pages
- Author: npltech — 2026-09-07T14:35:24
- Diff size: +303/-88 across 7 file(s)
- Heuristic score: **27.5/100**
  - *message_vs_diff_size* (25): Large diff (391 lines) with a short message (7 words) — more typical of a human committing quickly without narrating the change.
  - *commit_timing* (30): 177 min gap since the previous commit — consistent with normal human working pace.
- LLM judge score: **72/100**
  - The commit contains multiple cohesive, large-scale updates across several pages (updating metadata titles/descriptions, adding a shared tagline block, gating content rendering with hasLandingContent, and extensive inline comments explaining SEO copy provenance). The changes look unusually uniform and document-driven (e.g., exact SEO copy from a client PDF, verbose notes about page structure, and a consistent gating mechanism to avoid half-empty content). This level of breadth and template-like consistency suggests substantial AI assistance in generation or templating, rather than a purely human, small-scale hand edit. The commit message itself is fairly generic (“content updated on hire an angel pages”) and does not reflect the breadth and explicit, copy-paste SEO content changes visible in the diff, which is a mismatch between message and content magnitude. 

Key signals: 
- Multiple files updated in a uniform pattern (titles/descriptions per page, comments about source PDFs).
- Explicitly verbatim-like SEO copy and client-provided notes embedded in code comments.
- Structural scaffolding (hasLandingContent gating, shared tagline) that reads like a design/template approach rather than a one-off tweak.
- The narrative in comments (references to a PDF and exact wording) feels auto-generated or semi-automated to ensure consistency across pages.

Disagreement note: The commit message under-represents the scope (it doesn’t hint at multi-file metadata rewrites, gating logic, or the addition of a shared tagline) which is clearly visible in the diffs.  

Specific examples from the diff: 
- Metadata changes across four pages (titles and descriptions) with uniform new phrasing.
- New comments referencing exact SEO copy and a client PDF (e.g., // SEO copy is the client's exact wording ... and // Title and description are the client's exact SEO copy from requirements/...).
- Introduction of a shared tagline paragraph in the landing content and gating logic with hasLandingContent. 
  - Key signals: multi-file SEO metadata updates, verbose inline comments referencing client docs, landing content gating, shared landing tagline
  - Note: diff was truncated for length before being sent to the LLM judge.
- Blended score: **49.8/100**
  - Heuristic and LLM layers disagree by >=30 points — treat this commit's score as uncertain.

### `dca75e276b` — Merge branch 'main' of https://github.com/CloudSteer-Technology/act-ange
- Author: Radhikesh Kumar — 2026-09-07T11:38:07
- Diff size: +437/-597 across 8 file(s)
- Heuristic score: **40.0/100**
  - *message_vs_diff_size* (25): Large diff (1034 lines) with a short message (7 words) — more typical of a human committing quickly without narrating the change.
  - *commit_timing* (55): 5.9 min after the previous commit — plausible for either a fast human pass or an AI-assisted one.
- LLM judge: not run (sampling or `--no-llm`).

### `75d2d635aa` — pnpm-lock.yaml — resolves next to 16.3.4 (matches package.json's ^16.3.4
- Author: Radhikesh Kumar — 2026-09-07T11:32:13
- Diff size: +230/-193 across 3 file(s)
- Heuristic score: **52.5/100**
  - *message_vs_diff_size* (75): Large diff (423 lines) paired with a detailed message (42 words) — consistent with AI-drafted commit messages that narrate the change in full sentences.
  - *commit_timing* (30): 16 min gap since the previous commit — consistent with normal human working pace.
- LLM judge: not run (sampling or `--no-llm`).

### `c8a48e0b25` — minar changes
- Author: Radhikesh Kumar — 2026-09-07T11:16:41
- Diff size: +352/-182 across 3 file(s)
- Heuristic score: **27.5/100**
  - *message_vs_diff_size* (25): Large diff (534 lines) with a short message (2 words) — more typical of a human committing quickly without narrating the change.
  - *commit_timing* (30): 6837 min gap since the previous commit — consistent with normal human working pace.
- LLM judge: not run (sampling or `--no-llm`).

### `9321581f79` — Merge pull request #2 from CloudSteer-Technology/npl_dev
- Author: Radhikesh Kumar — 2026-09-02T17:19:19
- Diff size: +33/-13 across 2 file(s)
- Heuristic score: **27.5/100**
  - *message_vs_diff_size* (25): Large diff (46 lines) with a short message (11 words) — more typical of a human committing quickly without narrating the change.
  - *commit_timing* (30): 144 min gap since the previous commit — consistent with normal human working pace.
- LLM judge: not run (sampling or `--no-llm`).

### `1f00dab8c4` — Never Miss Another Lead animation line updated
- Author: npltech — 2026-09-02T14:55:13
- Diff size: +1/-1 across 1 file(s)
- Heuristic score: **60.0/100**
  - *message_vs_diff_size* (40): Small diff (2 lines), short message (7 words) — no strong signal either way.
  - *commit_timing* (80): Only 12s after the previous commit — faster than a typical manual edit-test-commit cycle.
- LLM judge score: **25/100**
  - The diff shows a tiny, likely manual cleanup: removing an erroneous character '1' after a closing div in a UI component. The commit message claiming an “animation line updated” suggests a broader change to an animation line, but the actual diff is a minimal cleanup with no substantive logic or animation changes. This points to a human making a small polish rather than AI-generated code or a large, systematically authored change. The message and diff are somewhat misaligned in scope: the message implies a feature/animation tweak, while the patch is a trivial fix.
  - Key signals: tiny diff, removal of stray character, no substantive logic change, commit message misalignment with actual change
- Blended score: **42.5/100**
  - Heuristic and LLM layers disagree by >=30 points — treat this commit's score as uncertain.

### `c3669f45ea` — Never Miss Another Lead animation line updated
- Author: npltech — 2026-09-02T14:55:01
- Diff size: +1/-1 across 1 file(s)
- Heuristic score: **47.5/100**
  - *message_vs_diff_size* (40): Small diff (2 lines), short message (7 words) — no strong signal either way.
  - *commit_timing* (55): 5.5 min after the previous commit — plausible for either a fast human pass or an AI-assisted one.
- LLM judge: not run (sampling or `--no-llm`).

### `c10a7fbd57` — Never Miss Another Lead animation line updated
- Author: Rahul — 2026-09-02T14:49:32
- Diff size: +33/-13 across 2 file(s)
- Heuristic score: **27.5/100**
  - *message_vs_diff_size* (25): Large diff (46 lines) with a short message (7 words) — more typical of a human committing quickly without narrating the change.
  - *commit_timing* (30): 137 min gap since the previous commit — consistent with normal human working pace.
- LLM judge: not run (sampling or `--no-llm`).

### `f41fc4298e` — Minor Fixes
- Author: Tahir Hameed — 2026-09-02T12:32:11
- Diff size: +4/-350 across 2 file(s)
- Heuristic score: **27.5/100**
  - *message_vs_diff_size* (25): Large diff (354 lines) with a short message (2 words) — more typical of a human committing quickly without narrating the change.
  - *commit_timing* (30): 909 min gap since the previous commit — consistent with normal human working pace.
- LLM judge: not run (sampling or `--no-llm`).

### `475d326521` — Merge branch 'main' of https://github.com/CloudSteer-Technology/act-ange
- Author: Radhikesh Kumar — 2026-09-01T21:23:26
- Diff size: +1575/-719 across 29 file(s)
- Heuristic score: **40.0/100**
  - *message_vs_diff_size* (25): Large diff (2294 lines) with a short message (7 words) — more typical of a human committing quickly without narrating the change.
  - *commit_timing* (55): 1.6 min after the previous commit — plausible for either a fast human pass or an AI-assisted one.
- LLM judge: not run (sampling or `--no-llm`).

### `67af31a1de` — Project name changes
- Author: Radhikesh Kumar — 2026-09-01T21:21:49
- Diff size: +3/-2 across 2 file(s)
- Heuristic score: **35.0/100**
  - *message_vs_diff_size* (40): Small diff (5 lines), short message (3 words) — no strong signal either way.
  - *commit_timing* (30): 1575 min gap since the previous commit — consistent with normal human working pace.
- LLM judge score: **25/100**
  - The diff shows small, targeted changes: adding an import in next-env.d.ts and changing the project name in package-lock.json. These are typical manual edits for a renaming/refactor rather than a large AI-generated implementation. The commit message is concise and generic, which is common for hand-made refactors. There are no unusually uniform patterns, defensive patterns, or extensive scaffolding that would strongly indicate AI generation. The changes themselves are straightforward and low-risk, consistent with human-driven project rename adjustments.
  - Key signals: small diffs, renaming package name, no large boilerplate or exhaustive handling, import addition that seems incidental to environment typing
- Blended score: **30.0/100**

### `3d61dac56c` — Add tracking for form validation failures, OTP send/resend failures, and
- Author: Tahir Hameed — 2026-08-31T19:06:31
- Diff size: +25/-6 across 1 file(s)
- Heuristic score: **42.5/100**
  - *message_vs_diff_size* (55): Small diff (31 lines) but a disproportionately detailed message (12 words) — could be AI-authored boilerplate, but also matches careful human commit discipline.
  - *commit_timing* (30): 38 min gap since the previous commit — consistent with normal human working pace.
- LLM judge: not run (sampling or `--no-llm`).

### `dc13aa1d7c` — Fix pnpm-lock.yaml out of sync with posthog-js dependency, unblocking de
- Author: Tahir Hameed — 2026-08-31T18:28:04
- Diff size: +100/-0 across 1 file(s)
- Heuristic score: **27.5/100**
  - *message_vs_diff_size* (25): Large diff (100 lines) with a short message (10 words) — more typical of a human committing quickly without narrating the change.
  - *commit_timing* (30): 14 min gap since the previous commit — consistent with normal human working pace.
- LLM judge: not run (sampling or `--no-llm`).

### `566bcfefe3` — Merge pull request #1 from CloudSteer-Technology/develop
- Author: Tahir Hameed — 2026-08-31T18:14:20
- Diff size: +64/-5 across 5 file(s)
- Heuristic score: **77.5/100**
  - *message_vs_diff_size* (75): Large diff (69 lines) paired with a detailed message (17 words) — consistent with AI-drafted commit messages that narrate the change in full sentences.
  - *commit_timing* (80): Only 49s after the previous commit — faster than a typical manual edit-test-commit cycle.
- LLM judge: not run (sampling or `--no-llm`).

### `8fab3e7729` — Add PostHog event tracking for CTA clicks, form funnel, and time-on-page
- Author: Tahir Hameed — 2026-08-31T18:13:31
- Diff size: +64/-5 across 5 file(s)
- Heuristic score: **27.5/100**
  - *message_vs_diff_size* (25): Large diff (69 lines) with a short message (11 words) — more typical of a human committing quickly without narrating the change.
  - *commit_timing* (30): 6875 min gap since the previous commit — consistent with normal human working pace.
- LLM judge: not run (sampling or `--no-llm`).

### `77c61bb3e2` — Add Microsoft Clarity and PostHog analytics, fix Done button doing nothi
- Author: Tahir Hameed — 2026-08-26T23:38:33
- Diff size: +78/-10 across 4 file(s)
- Heuristic score: **52.5/100**
  - *message_vs_diff_size* (75): Large diff (88 lines) paired with a detailed message (13 words) — consistent with AI-drafted commit messages that narrate the change in full sentences.
  - *commit_timing* (30): 430 min gap since the previous commit — consistent with normal human working pace.
- LLM judge: not run (sampling or `--no-llm`).

### `1e2ecf40bd` — Fix channel-aware success screen, add WhatsApp auto-redirect, add missin
- Author: Tahir Hameed — 2026-08-26T16:28:23
- Diff size: +39/-4 across 1 file(s)
- Heuristic score: **27.5/100**
  - *message_vs_diff_size* (25): Large diff (43 lines) with a short message (11 words) — more typical of a human committing quickly without narrating the change.
  - *commit_timing* (30): 32 min gap since the previous commit — consistent with normal human working pace.
- LLM judge score: **68/100**
  - The diff shows a cohesive feature set: a new WhatsApp redirect, channel-aware success messaging, and a Terms link. The changes are well-scoped and consistent: adding a WhatsApp constant, opening a new window directly in the click handler to avoid popup blockers, conditional rendering for different channels, and updating the UI copy. The code style is clean and defensive (try/catch, explicit rel attributes, etc.). This level of polish suggests some consideration beyond a trivial patch, but not an obviously full AI-generated monolith: the changes are targeted, with sensible comments and straightforward React/TSX patterns. There’s no obvious mismatch between the commit message and the code, though the message’s wording is concise while the code includes a few explanatory comments that feel human-written.

Key signals:
- WhatsApp link constant with encodeURIComponent usage
- Direct window.open in click handler to avoid popup blockers (explicit reasoning in comments)
- Added Terms of Service link in UI with proper rel attributes
- Channel-aware success screen sections (Call, WhatsApp, Email) with tailored copy and a fallback action for WhatsApp
- Commit message aligns with the actual changes; no overt boilerplate or misalignment

  - Key signals: WhatsApp link constant WHATSAPP_LINK, window.open in click handler with comments about popup blockers, Terms of Service link added in UI, Channel-aware success screen with conditional blocks for Call/WhatsApp/Email, Commit message accurately describes fixes
- Blended score: **47.8/100**
  - Heuristic and LLM layers disagree by >=30 points — treat this commit's score as uncertain.

### `dcbd359d35` — Audit fixes
- Author: Radhikesh Kumar — 2026-08-26T15:56:00
- Diff size: +230/-190 across 2 file(s)
- Heuristic score: **27.5/100**
  - *message_vs_diff_size* (25): Large diff (420 lines) with a short message (2 words) — more typical of a human committing quickly without narrating the change.
  - *commit_timing* (30): 205 min gap since the previous commit — consistent with normal human working pace.
- LLM judge: not run (sampling or `--no-llm`).

### `58e0ee0762` — contact, get started, and 4 persona pages added
- Author: northern — 2026-08-26T12:31:10
- Diff size: +687/-549 across 18 file(s)
- Heuristic score: **27.5/100**
  - *message_vs_diff_size* (25): Large diff (1236 lines) with a short message (8 words) — more typical of a human committing quickly without narrating the change.
  - *commit_timing* (30): 189 min gap since the previous commit — consistent with normal human working pace.
- LLM judge: not run (sampling or `--no-llm`).

### `f73e1e655d` — email updated
- Author: northern — 2026-08-26T09:21:48
- Diff size: +6/-6 across 3 file(s)
- Heuristic score: **35.0/100**
  - *message_vs_diff_size* (40): Small diff (12 lines), short message (2 words) — no strong signal either way.
  - *commit_timing* (30): 970 min gap since the previous commit — consistent with normal human working pace.
- LLM judge: not run (sampling or `--no-llm`).

### `e6369f8c42` — behind-the-angels page heading updated
- Author: northern — 2026-08-25T17:11:27
- Diff size: +36/-38 across 3 file(s)
- Heuristic score: **27.5/100**
  - *message_vs_diff_size* (25): Large diff (74 lines) with a short message (4 words) — more typical of a human committing quickly without narrating the change.
  - *commit_timing* (30): 69 min gap since the previous commit — consistent with normal human working pace.
- LLM judge: not run (sampling or `--no-llm`).

### `7b240eae78` — pragaraph updated on behind the angles page
- Author: northern — 2026-08-25T16:02:15
- Diff size: +2/-3 across 1 file(s)
- Heuristic score: **35.0/100**
  - *message_vs_diff_size* (40): Small diff (5 lines), short message (7 words) — no strong signal either way.
  - *commit_timing* (30): 22 min gap since the previous commit — consistent with normal human working pace.
- LLM judge score: **28/100**
  - The changes are a minor, human-sounding rewrite of a paragraph in the UI text. It swaps a few phrases and adds attributes like ‘innovative’ and changes punctuation. This is the kind of small, manual copy-edit likely done by a human during content refinement. The commit message itself contains a couple of typos and vague wording ('pragaraph updated on behind the angles page'), which doesn’t align well with the precise, content-specific edit in the diff, suggesting the message underrepresents the actual change. There are no structural or logic changes that would indicate AI-generated code, and no extensive error handling or boilerplate.
  - Key signals: small text/content edit, no new logic or boilerplate, commit message misspells/underdetails change
- Blended score: **31.5/100**

### `8542f1b1cb` — footer ui updated
- Author: northern — 2026-08-25T15:40:02
- Diff size: +84/-84 across 3 file(s)
- Heuristic score: **27.5/100**
  - *message_vs_diff_size* (25): Large diff (168 lines) with a short message (3 words) — more typical of a human committing quickly without narrating the change.
  - *commit_timing* (30): 17 min gap since the previous commit — consistent with normal human working pace.
- LLM judge: not run (sampling or `--no-llm`).

### `fcb5dd02c2` — new pages - terms and privacy added
- Author: northern — 2026-08-25T15:22:33
- Diff size: +637/-200 across 15 file(s)
- Heuristic score: **27.5/100**
  - *message_vs_diff_size* (25): Large diff (837 lines) with a short message (7 words) — more typical of a human committing quickly without narrating the change.
  - *commit_timing* (30): 279 min gap since the previous commit — consistent with normal human working pace.
- LLM judge: not run (sampling or `--no-llm`).

### `cc7da808f1` — Merge branch 'main' of https://github.com/CloudSteer-Technology/act-ange
- Author: northern — 2026-08-25T10:44:00
- Diff size: +1/-1 across 1 file(s)
- Heuristic score: **47.5/100**
  - *message_vs_diff_size* (40): Small diff (2 lines), short message (5 words) — no strong signal either way.
  - *commit_timing* (55): 4.5 min after the previous commit — plausible for either a fast human pass or an AI-assisted one.
- LLM judge: not run (sampling or `--no-llm`).

### `eb73088a32` — text updated
- Author: northern — 2026-08-25T10:39:31
- Diff size: +7/-7 across 2 file(s)
- Heuristic score: **35.0/100**
  - *message_vs_diff_size* (40): Small diff (14 lines), short message (2 words) — no strong signal either way.
  - *commit_timing* (30): 676 min gap since the previous commit — consistent with normal human working pace.
- LLM judge: not run (sampling or `--no-llm`).

### `a3a9416127` — Address Update
- Author: Northern Planet LLC — 2026-08-24T23:23:52
- Diff size: +1/-1 across 1 file(s)
- Heuristic score: **47.5/100**
  - *message_vs_diff_size* (40): Small diff (2 lines), short message (2 words) — no strong signal either way.
  - *commit_timing* (55): 2.6 min after the previous commit — plausible for either a fast human pass or an AI-assisted one.
- LLM judge score: **28/100**
  - The change is a small, cosmetic front-end tweak: wrapping the address text in an anchor tag with specific styling and an extra link element around it. The commit message 'Address Update' matches a minimal, manual style tweak rather than a large AI-generated refactor. Code style is conventional, with typical tailwind class usage. There are no verbose defensive patterns or complex restructuring that would suggest heavy AI generation. The message and diff align as a small, likely human-edited tweak.
  - Key signals: minor UI text/edit, no new complex logic, conventional classNames, commit message generic but aligned with small change
- Blended score: **37.8/100**

### `5833388806` — Address Added at the Footer.
- Author: Northern Planet LLC — 2026-08-24T23:21:17
- Diff size: +1/-1 across 1 file(s)
- Heuristic score: **35.0/100**
  - *message_vs_diff_size* (40): Small diff (2 lines), short message (5 words) — no strong signal either way.
  - *commit_timing* (30): 465 min gap since the previous commit — consistent with normal human working pace.
- LLM judge: not run (sampling or `--no-llm`).

### `2738af7fdb` — policy link updated for new page
- Author: northern — 2026-08-24T15:36:45
- Diff size: +1/-1 across 1 file(s)
- Heuristic score: **60.0/100**
  - *message_vs_diff_size* (40): Small diff (2 lines), short message (6 words) — no strong signal either way.
  - *commit_timing* (80): Only 45s after the previous commit — faster than a typical manual edit-test-commit cycle.
- LLM judge: not run (sampling or `--no-llm`).

### `7c345785e0` — policy link updated
- Author: northern — 2026-08-24T15:36:00
- Diff size: +1/-1 across 1 file(s)
- Heuristic score: **47.5/100**
  - *message_vs_diff_size* (40): Small diff (2 lines), short message (3 words) — no strong signal either way.
  - *commit_timing* (55): 8.2 min after the previous commit — plausible for either a fast human pass or an AI-assisted one.
- LLM judge: not run (sampling or `--no-llm`).

### `c206d6d372` — target blank added on cookies policies link
- Author: Rahul — 2026-08-24T15:27:48
- Diff size: +4/-1 across 4 file(s)
- Heuristic score: **35.0/100**
  - *message_vs_diff_size* (40): Small diff (5 lines), short message (7 words) — no strong signal either way.
  - *commit_timing* (30): 69 min gap since the previous commit — consistent with normal human working pace.
- LLM judge: not run (sampling or `--no-llm`).

### `b2608de7a0` — Initilizaton
- Author: Radhikesh Kumar — 2026-08-24T14:18:47
- Diff size: +22050/-0 across 132 file(s)
- Heuristic score: **32.5/100**
  - *message_vs_diff_size* (25): Large diff (22050 lines) with a short message (1 words) — more typical of a human committing quickly without narrating the change.
  - *commit_timing* (40): First commit in range — no prior commit to compare timing against.
- LLM judge: not run (sampling or `--no-llm`).
