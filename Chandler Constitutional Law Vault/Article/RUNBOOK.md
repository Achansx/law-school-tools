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

## PROVENANCE-CORRECTION PASS (active 2026-05-30, set by maintainer; removed at re-consolidation)

The EDITORIAL-REVIEW PASS is COMPLETE. This block now drives a small accuracy-correction pass: the author supplied answers to the four professor-only provenance questions, and three require prose changes so the article tells the literal truth about its corpus and its review status. **These are no-fabrication / accuracy fixes — they take priority over everything else until closed.** While present, this block overrides default rotation and selection.

- **Rotation — skip Harvest and Outline.** Effective rotation: **draft -> cite -> polish -> stitch -> verify -> draft ...**. Verify is NOT throttled. Batching is allowed: a single phase tick SHOULD address all open `PI-ER2-*` items it owns. Stitch propagates polished -> full-draft on the very next tick and re-runs the footnote-integrity audit (zero gap/dup/orphan). L-035 three-site discipline (drafts + polished + full-draft) applies. Curly quotes, no em dashes, Bluebook 21st, push protocol unchanged.

- **Author's-understanding framing (applies to all three).** The author supplied these answers and two are hedged. Do NOT assert them as established fact in the professor's voice; phrase as the article's current understanding and, where the prior text called something an "open question," resolve it to "the author's understanding is X" rather than "X is settled." A one-clause "subject to Professor Chandler's confirmation" hedge at the controlling site is appropriate and honest.

- **PI-ER2-REVIEWCLAIM (P0 — accuracy; highest priority).** The draft repeatedly frames the case study as a "reviewed static site" and footnote [^174] asserts "the professor as the gating actor who reviews each page before it is published." **Author's answer: the snapshot pages were NOT professor-reviewed before they went live, though the workflow allows it.** The current wording therefore claims review that did not happen and MUST be corrected. Rules for the reframe:
  - KEEP the architecture argument intact: the site is static (content fixed at build time, not generated at runtime); this RELOCATES hallucination risk from the reader's runtime to a build-time checkpoint; the professor is the *designed* gatekeeper; every page is reviewable, inspectable, and versioned. The static-vs-chatbot contrast in §VIII and §XII is correct and stays.
  - CHANGE every assertion that review *occurred* on the snapshot. Rename the descriptor to "**review-ready static site**" / "reviewable static site" where the current phrase implies completed review. Rewrite [^174] and the §VIII.A load-bearing claim and any abstract/§I.B echo so they describe the gatekeeping *role and capability*, not a completed review of the 198 pages.
  - ADD one honest disclosure sentence (anchor it at §VIII.A and reflect it in the §XII risk discussion and §XIII governance): for the May 2026 snapshot, the pages were published as review-ready drafts and had not yet been individually professor-approved; build-time professor review is the intended workflow the architecture enables, not a completed fact this article can claim. This is a Persona-4 (Provenance Auditor) honesty fix.
  - NEVER claim review that did not happen. The Verify tick's Provenance Auditor MUST re-read §VIII/§XII/§XIII and confirm no residual "was reviewed / reviews each page before publishing" assertion survives.

- **PI-ER2-CASEBOOK (P1).** §IV (body + [^53]) and §XII.C currently call casebook-excerpt ingestion an OPEN question. **Author's answer: the course files were authored by Professor Chandler and did not come from a casebook (no casebook excerpts ingested), as far as the author is aware.** Close the open question: state that the corpus is the professor's own course materials and that casebook excerpts were not ingested (author's understanding, subject to Chandler's confirmation). The §XII.C copyrighted-casebook licensing analysis becomes contingent/secondary — retain a one-sentence "were that understanding ever wrong, the following analysis applies" fallback rather than deleting the analysis outright.

- **PI-ER2-STUDENTWORK (P1).** §XII.D (body + [^54]/[^165]) currently calls student-work ingestion an OPEN question. **Author's answer: no student assessment or submitted work was ingested; the only third-party-authored corpus content is review-session materials prepared by teaching assistants.** Reframe: disclose the TA-prepared review-session materials plainly; note they are teaching aids authored by teaching assistants, which raises an authorship/attribution note, not a student-data/FERPA privacy problem. Resolve the privacy "open question" accordingly (author's understanding, subject to confirmation). Do not overclaim that there are zero privacy considerations; state the narrowed, accurate position.

- **PI-ER2-VAULTCOST (P1 — substantial standalone §IX rewrite; give it its own draft+cite cycle, do NOT cram with other items).** §IX currently reports the *article-writing* loop's cost, which is the wrong (and stale) figure for a method paper, and the author has decided §IX must report **vault-construction cost** instead and DROP the article-writing cost. Source the figures from `Chandler Constitutional Law Vault/.run-scores.jsonl` (the vault's own run log; readable from the repo root, NOT under Article/). Reliably computable and verified by the maintainer — use these exact figures (recompute from the log as a cross-check; if your count differs, investigate, do not guess): **255 vault runs over Apr 16 – May 8, 2026 (22 days)**; phase distribution **ingest 35, enrich 24, expand 29, synthesize 30, lint 34, verify 34, consolidate 10, deploy 59** (sum 255); deliverable **198 pages (92 briefs, 27 topics, 79 lectures)** at ~92% coverage. **NOT available:** per-run wall-clock/token/dollar cost (only 6 of 255 runs logged wall-clock) — so claim NO compute-hours and NO dollar figure; state that limitation plainly (same honesty discipline the article already uses). Rewrite §IX (Table 9.1 + IX.A/B/C/E prose + footnotes [^120]/[^121]/[^132]/[^133]) so the cost table is the vault build, the unfalsifiability framing points at vault cost, and the article-writing-loop cost is REMOVED (at most a one-sentence footnote noting this paper was produced by a comparable loop, with a pointer to the companion note). Update Appendix E the same way: replace the stale E.2 "article-writing cost (runs 66-119)" with the vault-construction cost section; fix the E.5 caveats accordingly. NEVER fabricate a cost number; only report what `.run-scores.jsonl` supports. The article-writing loop's own numbers now live in `Article/packet-2026-05-30/04-How-This-Article-Was-Written.docx` (a packet companion), so §IX does not need them.

- **Re-consolidation exit.** When PI-ER2-REVIEWCLAIM, PI-ER2-CASEBOOK, and PI-ER2-STUDENTWORK are all resolved and propagated to full-draft (integrity green), STOP and signal for re-freeze. Do not set submission_ready. The system still does not submit to JLE and does not email the professor.

## Phase: Harvest

**Goal:** Build or refresh evidence cards in `manuscript/evidence/`. One card per atomic fact / quotation / statistic the article needs.

**Appendix sub-task (active when all main sections are populated).** Before the main procedure, check section evidence status. If EVERY one of sections 01–14 has `evidence_status: populated` AND at least one entry in `.article-state.json` `appendices` has `status` of `none` or `needs_work`:

1. Load `rubric/appendix.md`.
2. Pick the lowest-letter appendix entry from `appendices` with `status: none` or `needs_work` (alphabetical: A, then B, then C…).
3. Read the appendix scaffold (`manuscript/appendices/appendix-<X>-<slug>.md`) including its frontmatter `source_files` list.
4. Read each source file listed. For aggregation appendices (A, B, D, E), the contents are the appendix material — reproduce them with structure, captions, and the labels described in the scaffold TODO comment. For writing appendices (C, F), use the scaffold's TODO comment as the outline and write the prose.
5. Replace the TODO comment with finished content. Update the appendix frontmatter: `status` (`drafted` if all rubric criteria score >=4 and word count is within `target_min`/`target_max`; `needs_work` otherwise), `words` (actual count), `last_phase: harvest-appendix`.
6. Update `.article-state.json` `appendices.<X>` to mirror frontmatter.
7. Append the appendix score to `.article-scores.jsonl` with `phase: "harvest-appendix"`.
8. THIS COUNTS AS THE HARVEST RUN. Advance the phase to Outline as normal. Do not also do section evidence in the same run.

The appendix sub-task takes precedence over scaffold-first ONLY when scaffold-first has nothing left to do (all 14 sections at evidence_status: populated). Until then, scaffold-first wins.

**Per-run scope (main section Harvest):** Pull evidence for one section that the state file lists as `evidence_status: needs_work` or `none`. Update `.article-state.json` per-section `evidence_status` to `populated` when the section has at least 6 cards.

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
   - Total word count is between 10,000 and 14,000 (raised from 12,000 on 2026-05-25 with Section XI/XII earmark; see PROJECT_PRIMER).
3. Assemble the full draft into `manuscript/full-draft.md` in section order.
4. Update `.article-state.json` `manuscript.total_words`, `manuscript.last_stitched_at`.
5. Set `stitch_status: ready_for_verify` and per-section `polish_status: stitched`.

**Submission-readiness exit:** Set `gates.submission_ready.awaiting_human = true` and stop the rotation **only if all of**:

1. Main-text word count in `manuscript/full-draft.md` is within **10,000 to 14,000** (raised from 12,000 on 2026-05-25; appendices NOT counted; Section XI/XII earmark per PROJECT_PRIMER).
2. All 14 sections have `polish_status: stitched`.
3. All 6 appendices (`appendices.A` through `appendices.F`) have `status: drafted` or `polished`.
4. Most recent Verify run reported zero P0 and zero P1 findings against the main draft.
5. **Provenance audit complete and clean.** Every polished section has `provenance_audited: true` AND `provenance_score >= 4.5`. Across all 14 sections, total open `unsupported_claims` is zero (entries flagged `reason: intentional-conjecture` with explicit human acceptance do not count against the gate).
6. **Appendix provenance fields present.** Every appendix in `manuscript/appendices/` has a `provenance_note` field in its frontmatter, OR its source files are all present in this repo and the appendix consequently doesn't need a provenance note (Appendix A, post-rerun, is the model).

Appendices ship as separate online supplements per JLE practice. They are NOT assembled into `manuscript/full-draft.md`. They live as individual files in `manuscript/appendices/` and are submitted alongside the main manuscript via Scholastica's supplement upload.

**The verifiability principle.** The article's central thesis is that AI systems can be made verifiable and inspectable. The article itself must meet that standard. Criterion 5 is the operational test: every factual claim in the prose traces to an evidence card, a primary source footnote, or an explicit acceptance of conjecture. No factual sentence escapes scrutiny.

## Phase: Verify

**Goal:** Adversarial three-persona pass. Forced findings. The phase that catches what other phases miss.

**Procedure:**

1. Read `Article/PERSONAS.md`.
2. For each of the four personas (JLE Editor, Pedagogy Traditionalist, AI-in-Education Researcher, Provenance Auditor), read the full draft and return at least one finding. P0 (must fix before submission), P1 (should fix), P2 (nice to fix). Each persona MUST return at least one finding; "looks fine" is not acceptable.

**Provenance audit sub-task (Provenance Auditor's primary work product).** The Provenance Auditor does not just produce findings — it produces a per-section provenance audit. On each Verify run:

1. Load `rubric/provenance-audit.md`.
2. Pick the lowest-numbered polished section with `provenance_audited: false` (or absent) in its frontmatter. If all 14 are audited, re-audit the section with the lowest `provenance_score`.
3. For that section, scan the polished prose for factual claims per the criteria in `rubric/provenance-audit.md`. For each claim:
   - Search `manuscript/evidence/` for a card supporting it. If found, link to the card by filename.
   - Else, search the polished section's footnotes for a primary-source citation supporting it. If found, link to the footnote number.
   - Else, log to `unsupported_claims` with a `reason` field.
4. Append one JSONL line per claim to `manuscript/claim-manifest.jsonl`:
   `{"timestamp": "<ISO 8601>", "section": "<NN>", "paragraph": <int>, "claim_text": "<text>", "support_type": "<evidence-card | footnote | unmapped>", "support_ref": "<path or footnote-N>", "reason": "<if unmapped>"}`
5. Update the section's polished-file frontmatter: `provenance_audited: true`, `provenance_score: <0-5>`, `claims_total`, `claims_mapped`, `unsupported_claims`.
6. Score the provenance audit run against `rubric/provenance-audit.md` and append to `.article-scores.jsonl` with `phase: "verify-provenance"`.
7. If `provenance_score < 4.5` or any `unsupported_claims` has reason other than `intentional-conjecture`, set the section's `polish_status: needs_polish` so the next Polish/Cite cycle picks up the gaps.

The provenance audit is the Provenance Auditor's role; the other three personas still produce their own findings as before. A Verify tick that does both general findings AND the provenance audit is one tick (do not split into two).
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
