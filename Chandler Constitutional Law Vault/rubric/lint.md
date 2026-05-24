# Rubric: Lint

Scale: 5 exemplary, 4 solid, 3 acceptable, 2 below expectations, 1 serious, 0 failure. Weighted average rounded to one decimal.

Lint measures structural integrity that Lint can actually affect. Orphan wiki-links (forward-references to pages that have not been ingested yet) are NOT Lint's to close — they wait for Ingest or Synthesize — and scoring Lint against them produces a red-flag every run that trains the system to ignore all flags. The `broken_links_fixed` criterion below is scoped to genuinely broken targets (typos, renamed files, stem mismatches) and weighted accordingly.

| Criterion | Weight | Red Flag At | Method |
|-----------|--------|-------------|--------|
| structural_fixes | 0.27 | 0 | Count of structural issues resolved this run: missing frontmatter delimiters, missing required fields, H1/filename disagreement, missing table separator rows, tag casing, horizontal-rule spacing, frontmatter enum drift. 0 structural issues found AND none introduced -> 5 (nothing to fix is an exemplary state). 1 to 3 fixed -> 4. 4 to 8 fixed -> 5. 9 or more -> 5 with a scope-concern note in `notes`. |
| pending_issues_cleared | 0.18 | 0 | Fraction of Lint-scope pending issues cleared this run. Issues whose `type` is content-level (e.g., `low_cited_by`, `fact-check-needed`) or Ingest-level (`orphan_links` where targets do not yet exist) are NOT in Lint scope and do not count against this ratio. Ratio of in-scope issues cleared times 5. |
| template_enforcement | 0.18 | 1 | Pages touched that now match the canonical template (frontmatter schema, H2 order, filename/H1/frontmatter name convention). 100% -> 5. 90% -> 4. Below 80% -> 2. |
| broken_links_fixed | 0.04 | -- | Genuine broken wiki-links resolved (target filename no longer exists, stem mismatch, renamed page). Forward-references to pages that have not been ingested yet are NOT broken links and do not count. 0 genuine broken links found AND 0 introduced -> 5 (this is the expected steady state). 1 or more fixed -> 5. Any introduced -> 0 AND a red flag. |
| source_attribution_sync | 0.13 | 1 | `source_files` frontmatter list and `## Sources` footer agree on every touched page. Same paths, same order. Missing footer when frontmatter lists sources, or missing frontmatter when footer has a Sources block, counts as a mismatch. 100% aligned -> 5. One mismatch repaired in place -> 4. One or more mismatches left unrepaired -> 1. Any page missing BOTH frontmatter and footer source attribution (post-backfill era) -> 0 AND a red flag. |
| no_net_regressions | 0.10 | 0 | Lint did not introduce new broken links, frontmatter errors, template violations, or source-attribution desyncs. Yes -> 5. Any introduced -> 0. |
| scope_discipline | 0.10 | 0 | Lint stayed inside its declared scope — structural fixes only. No content authoring (no enrich-style stub resolution, no synthesize-style topic page creation), no out-of-scope page touches outside the run's declared file list, no opportunistic "while I was here" rewrites. The CHANGELOG entry's files_edited count matches the declared scope. Strict scope -> 5. One out-of-scope edit (with note explaining why) -> 3. Two or more out-of-scope edits OR any content authoring -> 0 AND a red flag. |
| brevity | 0.05 | 0 | This run's CHANGELOG entry stays inside the 120-word cap and uses the fixed shape from SKILL.md Step 2.3 (Did/Found/Files/Score/State bullets, optional fenced JSON extras — no prose paragraphs). The BUILD_NARRATIVE paragraph stays inside the 80-word cap. Compliant on both -> 5. One overflow under 50% over cap -> 3. Either overflow over 50% over OR per-phase JSON extras rendered as prose -> 0 AND a red flag. |

## Red flags

- A new broken link or frontmatter error was introduced during this run.
- `broken_links_fixed` scored 0 because orphan forward-references were miscounted as broken links (this is the pre-refactor false positive and should no longer appear — if it does, the scorer is still using the old definition).
- Template enforcement dropped below 80% on touched pages.
- A pending issue is content-level or Ingest-level but the scorer counted it against Lint's `pending_issues_cleared` ratio.
- Lint "fixed" orphan forward-references by deleting them instead of leaving them for the phase that can resolve them (Ingest or Synthesize).
- A touched page is missing `source_files` frontmatter or `## Sources` footer, OR the two are out of sync, AND Lint did not repair the mismatch.
- Lint authored content (resolved an `<!-- ENRICH: -->` stub, drafted a topic page, wrote analysis) — that work belongs to Enrich, Expand, or Synthesize.
- CHANGELOG entry rendered phase-specific extras as prose paragraphs instead of the fixed-shape bulleted form + optional fenced JSON block.

## Regression check

Compare to the rolling median over the last five Lint runs. Delta greater than 1.0 below median adds `regression-vs-median` to red flags. Lint is a steady-state phase: a well-maintained vault should produce low issue counts and high structural_fixes/template_enforcement scores consistently. A sustained drop usually signals either upstream scope creep (Ingest producing malformed pages) or a new class of drift the rubric does not yet cover — investigate rather than normalize.
