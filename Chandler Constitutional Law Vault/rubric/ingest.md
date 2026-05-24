# Rubric: Ingest (skeleton pass)

Scale: 5 exemplary, 4 solid, 3 acceptable with minor gaps, 2 below expectations, 1 serious problem, 0 failure. Weighted average rounded to one decimal.

Ingest produces skeleton briefs, not finished ones. A run that writes a full 9-section analysis during Ingest is NOT a higher-quality run — it starves Enrich of work and is penalized under `scope_discipline`.

| Criterion | Weight | Red Flag At | Method |
|-----------|--------|-------------|--------|
| files_processed | 0.15 | 0 | New source files successfully turned into skeleton wiki pages (Steps 1 to 7). 0 with backfill present -> 3 (acceptable on slow run). 1 to 3 -> 3. 4 to 7 -> 4. 8 to 10 -> 5. Above 10 -> 4 (over-cap; the new-file ceiling is 10 even when the backfill-only ceiling is 15). 0 with no backfill either -> 0. |
| classification_accuracy | 0.10 | 1 | Files correctly classified (case reading vs lecture vs supplemental). Self-graded with evidence: cite one tricky classification and why it was resolved that way. N/A on a pure-backfill run. |
| skeleton_completeness | 0.20 | 1 | Factual sections (Memory Jogger, Facts, Procedural History, Judicial Votes, Holding) populated at full depth on every new case brief. All present -> 5. 1 to 2 missing across the batch -> 3. 3+ missing -> 1. N/A on a pure-backfill run. |
| stub_markers_present | 0.15 | 0 | Every deferred section has a `<!-- ENRICH: one-sentence description -->` marker (at minimum: concurrence, dissent, Hypothetical Applications, Critique, additional Key Quotations, Connections). All stubs present across all new briefs -> 5. Missing on one brief -> 3. Missing on two or more -> 1. N/A on a pure-backfill run. |
| scope_discipline | 0.10 | 0 | Verify none of the skeleton briefs were written at 9-section depth. `verified` on every new brief is `"pending-enrich"`. Any brief written at full depth or flipped to today's date during Ingest -> 0 here and a red flag. Backfill that touched MORE cases than the per-run cap allowed -> 0 here as well. |
| midpage_verification | 0.10 | 0 | Each new case brief carries exactly one Midpage-verified pin-cited quote and populated `midpage_id`/`midpage_url`. 100% -> 5. 50% -> 3. 0% -> 1. N/A on a pure-backfill run. |
| source_attribution | 0.10 | 1 | Every new page has a `source_files` YAML list in frontmatter and a matching `## Sources` footer section. Entries use `Source Materials/filename.ext` for PDFs/decks (rendered as wikilinks in the footer) or `Source Materials/Midpage analyzeOpinion (opinionId N)` for Midpage-only inputs (kept as inline code in the footer). Frontmatter and footer must list the same paths in the same order. 100% of new pages correct -> 5. One page missing one side -> 3. Two or more pages missing either side -> 1. Any frontmatter/footer mismatch -> 0. |
| backfill_coverage | 0.10 | 0 | Backfill (Step 8) was attempted, the matcher's `auto_apply` bucket was applied to in-scope cases, the `review_needed` and empty buckets generated pending issues, and Midpage placeholders were correctly evicted from cases that gained file-on-disk sources. Track two numbers in the run narrative: cases_touched_this_run and vault_coverage_pct = (cases with at least one file-on-disk source) / (total cases). Coverage must be monotonically non-decreasing across runs unless the source inventory shrank. Cap consumed AND coverage advanced -> 5. Cap consumed but coverage flat (every match was already applied last run) -> 4. Cap unused on a non-empty review/empty bucket -> 3. Backfill skipped on a run where Steps 1 to 7 produced fewer than 8 touches -> 1. Coverage regressed without source-inventory shrink -> 0 and a red flag. |
| brevity | 0.05 | 0 | This run's CHANGELOG entry stays inside the 120-word cap and uses the fixed shape from SKILL.md Step 2.3 (Did/Found/Files/Score/State bullets, optional fenced JSON extras — no prose paragraphs). The BUILD_NARRATIVE paragraph stays inside the 80-word cap. Compliant on both -> 5. One overflow under 50% over cap -> 3. Either overflow over 50% over OR per-phase JSON extras rendered as prose -> 0 AND a red flag. |

## Red flags

- A new case brief has `verified` set to today's date during Ingest (it must be `"pending-enrich"`).
- Any new case brief has a written concurrence analysis, dissent analysis, filled Critique, or filled Hypothetical Applications. Those belong to Enrich.
- Zero `<!-- ENRICH: -->` markers across the batch, or markers present but without a one-sentence description.
- Ingest ran without cycle gating: fewer than 6 non-ingest phase-history entries since the previous Ingest run AND less than 2 hours since the most recent `.ingested-files.json` timestamp. The phase should have been skipped with a CHANGELOG note.
- More than 10 files processed in one run via Steps 1 to 7. The higher cap on new-file processing is 8 to 10, not unlimited. Backfill (Step 8) honors the same cap as a "cases touched" budget UNLESS Steps 1 to 7 produced zero touches, in which case the backfill-only ceiling is 15 (mechanical work, no analytical depth competing for attention). A run with 0 new files and 11 to 15 backfill touches is in scope; a run with 1 or more new files and a combined total above 10 is over-cap.
- Any new page is missing `source_files` in frontmatter or `## Sources` in the footer, or the two are out of sync. Source attribution is not optional — a page without provenance fails the run.
- Backfill (Step 8) was skipped on a run where Steps 1 to 7 produced fewer than 5 touches AND the most recent `/tmp/case_source_matches.json` shows non-empty `auto_apply` or `review_needed` buckets. The cap budget should have been spent on backfill.
- A case gained a file-on-disk source via backfill but a `Source Materials/Midpage analyzeOpinion (opinionId N)` placeholder was not evicted from `source_files` and the `## Sources` footer. Eviction is mandatory — duplicate provenance from a real file plus a Midpage placeholder is the exact pattern this policy was designed to clear.
- A case had `midpage_id` or `midpage_url` removed from frontmatter during backfill. Those are verification metadata; only the `Source Materials/Midpage ...` placeholder string should be evicted.

## Regression check

If a previous Ingest run was flagged for scope creep (full-depth briefs) and this run repeats the pattern, add `ingest-scope-creep-repeat` to red flags and log a `lesson-candidate` pending issue describing the recurrence.

If two consecutive Ingest runs report flat `vault_coverage_pct` while the matcher's `auto_apply` bucket is non-empty, add `backfill-stalled` to red flags and log a `lesson-candidate` pending issue. The most likely cause is that Step 8.2 is silently failing to write into `source_files`; investigate before the next run.
