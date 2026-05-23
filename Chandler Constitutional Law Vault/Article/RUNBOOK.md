# JLE Article — Runbook

Step-by-step phase instructions. Read this plus `PROJECT_PRIMER.md`, the current phase rubric, and the current month's `BUILD_NARRATIVE` at the start of every run.

## Dispatcher protocol (every run)

1. Read `Article/.article-state.json`. Identify `current_phase` and `gates`.
2. If any gate has `awaiting_human: true`, log one line to `BUILD_NARRATIVE` and stop. Do not advance.
3. Otherwise, load `Article/rubric/<current_phase>.md` and `Article/LESSONS.md`.
3a. **Scaffold-first priority (active until first-pass completion).** Before applying any in-phase section-selection heuristic, check whether any of sections 01, 10, 12, 13, 14 still have `evidence_status: none`. If yes, **the active phase MUST work on the lowest-numbered such untouched section first**, overriding any "lowest ratio" or "needs_work" rule below. This applies to Harvest, Outline, Draft, Cite, and Polish. It lifts automatically when every section has reached at least `cite_status: needs_polish` once. The rotation should not loop over already-developed sections while any of these five are at `none`.
4. Execute the phase per the section below.
5. Score the run against the rubric (1 to 5 per criterion). Append one JSON line to `Article/.article-scores.jsonl` with: `{timestamp, phase, scores, notes}`.
6. Append any new lessons to `Article/LESSONS.md` (cap at 50; if at cap, drop the lowest-impact entry first).
7. Advance `current_phase` to the next in rotation; if last phase reached, wrap to first.
8. Append a 2 to 4 sentence entry to `BUILD_NARRATIVE_YYYY-MM.md` describing what changed.
9. **Cost-log append (every run).** Append one JSON line to `Article/manuscript/cost-log.jsonl`:
   `{"timestamp": "<ISO 8601>", "run_count": <int>, "phase": "<phase>", "model": "<model id>", "files_read": <int>, "files_written": <int>, "words_generated": <approx int — count words in new/edited prose excluding state files and JSONL appends>, "notes": "<one short sentence>"}`
   This data is the source for Section IX (Cost and Labor). Honesty here is the article's argument; do not estimate when you can count.
10. If the cumulative state suggests the article is submission-ready, set `gates.submission_ready.awaiting_human = true` (see Stitch and Verify exit conditions).

## Phase: Harvest

**Goal:** Build or refresh evidence cards in `manuscript/evidence/`. One card per atomic fact / quotation / statistic the article needs.

**Per-run scope:** Pull evidence for one section that the state file lists as `evidence_status: needs_work` or `none`. Update `.article-state.json` per-section `evidence_status` to `populated` when the section has at least 6 cards.

**Procedure:**

1. Read the target section row in `PROJECT_PRIMER.md` to recall its purpose.
2. Read `Article-Workplan.md` annotated bibliography for that section.
3. Walk the listed vault sources: vault Cases, Topics, Lectures, email-to-chandler-*, archive/vault-blog-post-draft.md, LESSONS.md, rubric files.
4. For each fact you want to use, write `manuscript/evidence/evidence-NN-slug.md` with frontmatter: `section, fact_type (quotation | statistic | example | argument | citation), source_path or source_url, verified (bool), notes`. Body: the fact in 1 to 3 sentences plus the exact source quote.
5. For external facts (Magesh hallucination rates, Karpathy autoresearch details, Bond meta-review), pull from WebFetch only if the bibliography entry has a URL and the URL is stable. Mark `verified: true` only after reading the source page.
6. Log gaps (claims the article makes that have no evidence yet) to `pending_issues` in state.

**Exit:** Section advances when `evidence_status: populated` and at least one piece of evidence exists for every claim listed in `Article-Workplan.md` section commentary.

## Phase: Outline

**Goal:** For one section, produce or refresh `manuscript/outlines/outline-NN-slug.md`. The outline is the spine of subsequent Draft runs.

**Abstract sub-task (highest priority within Outline).** Before applying the procedure below, check `.article-state.json` `abstract.status`. If it is `none` or `needs_work`:

1. Load `rubric/abstract.md`.
2. Read the workplan's thesis (§1 of `Article-Workplan.md`), PROJECT_PRIMER's thesis sentence, and any existing `manuscript/abstract.md`.
3. Draft or revise `manuscript/abstract.md` toward 240–260 words. Score against `rubric/abstract.md`.
4. Update state: `abstract.status` (to `needs_work` if scores <4 anywhere; `ready_for_review` if all >=4 and word count in [225,275]; `ready_for_human_review` after three consecutive runs at avg >=4.5 with no substantive edits), `abstract.words`, `abstract.last_score`.
5. Append the abstract score to `.article-scores.jsonl` with `phase: "outline-abstract"`.
6. THIS COUNTS AS THE OUTLINE RUN. Advance the phase to Draft as normal. Do not also do a section outline in the same run.

If `abstract.status` is `ready_for_review` or `ready_for_human_review`, skip the sub-task and proceed to the section-outline procedure below.

**Procedure (section outline):**

1. Pick the section with `outline_status: needs_work` whose `evidence_status` is `populated`.
2. Read all evidence cards for that section.
3. Build a heading-level outline: section H1, three to five H2 subsections, two to four bullet points per H2.
4. Beside each bullet, in `[evidence: evidence-NN-slug]` brackets, name the evidence card(s) that support it.
5. Beside each subsection heading, write a word budget summing to the section's target in PROJECT_PRIMER.
6. End the outline file with a `## Open questions` block listing anything the section cannot yet say without more research.
7. Set `outline_status: ready_for_draft` on the section.

**Exit:** Outline file exists, every bullet has an evidence pointer, word budgets sum within 10 percent of section target.

## Phase: Draft

**Goal:** Write or expand the prose of one section.

**Procedure:**

1. Pick the section with `outline_status: ready_for_draft` and lowest `draft_words / target_words` ratio.
2. Read its outline and all referenced evidence cards.
3. Write in the house voice (see PROJECT_PRIMER). One sentence per idea. Prose, not bullets, except where the professor's outline explicitly calls for a table.
4. Cite inline using placeholder `[CITE: source_path or url]`. Bluebook formatting happens in Cite phase, not here.
5. Save to `manuscript/drafts/section-NN-slug.md`. Update its frontmatter `word_count`, `last_phase: draft`, `draft_status`.
6. Do not exceed the section's word budget by more than 15 percent. If over, stop and flag for Stitch to trim.
7. Set `draft_status: needs_cite` when the section is structurally complete (every outline bullet covered).

**Critical:** Never invent a fact, quotation, statistic, case holding, or citation. If the outline points to evidence the draft phase cannot find, leave a `[TODO: evidence needed for X]` marker and log to `pending_issues`.

## Phase: Cite

**Goal:** Replace `[CITE: ...]` placeholders with Bluebook 21st footnotes.

**Procedure:**

1. Pick a section with `draft_status: needs_cite`.
2. For each `[CITE: ...]` placeholder:
   - Identify the source type (case, statute, book, article, web).
   - Construct Bluebook 21st form.
   - For web sources, verify URL liveness via WebFetch (HEAD or short GET). If dead, find an archive.org capture and use that.
   - For case citations, prefer the highest-priority reporter; pin cites where the proposition is page-specific.
3. Save footnotes inline as numbered Markdown footnotes (`[^1]`) with the full citation in a `## Footnotes` block at file end.
4. Verify no claim in the prose lacks a footnote. Add `[TODO: cite needed]` markers for orphans and log to `pending_issues`.
5. Set `cite_status: needs_polish`.

**Critical:** No "personal communication" or "internal log" cites in published prose. If a fact comes from the vault's internal artifacts only, either move that fact to an appendix or rewrite the claim in terms the article can support with a public source.

## Phase: Polish

**Goal:** Per-section style pass. Voice unity. Mechanical hygiene.

**Procedure:**

1. Pick a section with `cite_status: needs_polish`.
2. Run the style checklist:
   - No em dashes. Rewrite using commas, parentheses, semicolons, or sentence splits.
   - No straight ASCII quotes. Convert all `"` and `'` to curly equivalents.
   - Voice: practitioner-scholarly, JLE-idiomatic. Cut any sentence that reads as product announcement or tech-enthusiast.
   - One idea per sentence; tighten any sentence over 35 words unless deliberate.
   - Active voice unless the actor is unknowable.
   - First-person singular (I) only in narrative passages about the project; third-person elsewhere.
   - Verify the section's word count is within plus or minus 10 percent of target; if not, flag for Stitch.
3. Save to `manuscript/polished/section-NN-slug.md`.
4. Set `polish_status: ready_for_stitch`.

## Phase: Stitch

**Goal:** Cross-section consistency. The seam-fixer.

**Adaptive mode (interim vs. final).** Before procedure: read `.article-state.json` and count sections where `polish_status` is either `ready_for_stitch` or `stitched`.

- **Interim stitch (count < 14):** Skip the word-count, recurring-sentence, and submission-readiness checks. Assemble the sections that exist into `manuscript/full-draft.md` in section order, with a top-of-file note: `*Interim assembly: <N> of 14 sections. Not submission-ready.*` Still run terminology, cross-reference, and seam-transition checks on the sections that exist. Update `manuscript.total_words` and `manuscript.last_stitched_at`. Score the run normally — **do NOT noop just because some sections are missing**. The Verify phase needs something to read.
- **Final stitch (count == 14):** Run the full procedure below.

**Procedure (final stitch only):**

1. Read all `manuscript/polished/section-*.md` files plus the abstract.
2. Run consistency checks:
   - Terminology unified (e.g., "course knowledge system" vs. "knowledge graph" used per PROJECT_PRIMER voice rules).
   - Facts consistent across sections (page counts, dates, numbers).
   - Recurring sentence appears exactly three times in approved spots (intro, VII/VIII seam, conclusion).
   - Internal cross-references resolve correctly.
   - Transitions at section seams read smoothly; rewrite weak transitions in place.
   - Total word count is between 10,000 and 12,000.
3. Assemble the full draft into `manuscript/full-draft.md` in section order.
4. Update `.article-state.json` `manuscript.total_words`, `manuscript.last_stitched_at`.
5. Set `stitch_status: ready_for_verify` and per-section `polish_status: stitched`.

**Submission-readiness exit:** If word count is in range AND all sections have `polish_status: stitched` AND prior Verify run reported zero P0/P1 findings, set `gates.submission_ready.awaiting_human = true` and stop the rotation.

## Phase: Verify

**Goal:** Adversarial three-persona pass. Forced findings. The phase that catches what other phases miss.

**Procedure:**

1. Read `Article/PERSONAS.md`.
2. For each of the three personas, read the full draft and return at least one finding. P0 (must fix before submission), P1 (should fix), P2 (nice to fix). Each persona MUST return at least one finding; "looks fine" is not acceptable.
3. Append findings to `manuscript/verify-findings.md` with persona, severity, location (section, paragraph), description, suggested fix.
4. **Status-reset rules (P1 deferral until first-pass completion):**
   - P0 findings ALWAYS reset the affected section's status: to `needs_draft` if substantive, `needs_polish` if cosmetic.
   - P1 findings: check `.article-state.json` — have all 14 sections reached at least `cite_status: needs_polish` once? If **NO**, P1 findings are LOGGED to `pending_issues` but do NOT reset section status. The first-pass scaffold of missing sections takes priority over polishing existing sections to mirror finish. If **YES**, P1 findings reset section status as before (`needs_polish` for style, `needs_draft` for substantive).
   - P2 findings always log only; never reset status.
5. Update `.article-state.json` `verify.last_run` and `verify.new_findings_count`. Record the count of *deferred* P1s separately in `verify.deferred_p1_count` so the system can re-enforce them once the deferral lifts.
6. If zero P0 and zero P1 findings AND Stitch's previous-run report was clean AND all 14 sections are `polish_status: stitched`, the system is ready for the submission gate.

## State machine rules

- `current_phase` advances strictly through the rotation; no skipping.
- A no-op run (nothing to harvest, no outlines to refresh, etc.) still advances the phase and logs `noop: true` to the scorecard; it does not score against the rubric. **Note:** Stitch noop is restricted by the adaptive-mode rule in the Stitch section — interim assembly counts as a real run.
- The state file's `pending_issues` is append-only within a run; entries clear only when the phase that fixes them sets `resolved_at`.
- **Pending-issue archival.** When a pending_issue's `status` flips to `resolved` or `outline-addressed`, the resolving phase MOVES the entry from `.article-state.json` `pending_issues` into `.article-state.archive.json` `archived_pending_issues` in the same run. The live state file should not accumulate closed work. If `.article-state.json` ever exceeds 150 KB, the next dispatcher run audits `pending_issues` and migrates any non-open entries it finds.
- If LESSONS.md grows past 50 entries, the oldest low-impact entry (lowest `impact_score` field) is dropped.

## Stop conditions

- `gates.submission_ready.awaiting_human = true`: stop and wait.
- Any gate with `awaiting_human = true`: stop and wait.
- Three consecutive runs scoring under 2.0 on the same phase: log a critical lesson and stop; wait for human review.
- Catastrophic state-file corruption: write `.article-state.json.broken-YYYY-MM-DD` and stop; do not attempt to repair automatically.
