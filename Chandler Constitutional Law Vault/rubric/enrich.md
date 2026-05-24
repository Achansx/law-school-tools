# Rubric: Enrich (analytical depth)

Scale: 5 exemplary, 4 solid, 3 acceptable, 2 below expectations, 1 serious, 0 failure. Weighted average rounded to one decimal.

Enrich converts Ingest-produced skeletons into finished 9-section briefs. Each criterion measures the analytical work that fills in the `<!-- ENRICH: -->` stubs Ingest left behind. If Enrich inherits zero stubs because Ingest overreached, log a pending issue instead of forcing a score.

| Criterion | Weight | Red Flag At | Method |
|-----------|--------|-------------|--------|
| stubs_resolved | 0.22 | 0 | Fraction of `<!-- ENRICH: -->` markers in-scope briefs that were replaced with substantive prose. 100% on 3+ briefs -> 5. 80 to 99% -> 4. 50 to 79% -> 3. Below 50% -> 1. |
| concurrence_and_dissent | 0.18 | 0 | Concurrence and dissent Analysis actually reason through the opinion's interpretive move, not just list which justices joined. Every concurrence and dissent present in the opinions covered -> 5. One missing reasoning block -> 3. Two or more -> 1. |
| hypos_with_reasoning | 0.14 | 0 | Five hypos per brief (2 same-side, 2 opposite-side, 1 fence-sitter), each with fact pattern AND reasoning. All five on each enriched brief -> 5. Four on any brief -> 3. Three or fewer -> 1. Fact-pattern-only hypos count as 0 for that slot. |
| critique_balance | 0.13 | 0 | Critique section carries at least one progressive and one originalist/textualist angle per enriched brief, each grounded in a cite or clearly signposted argument. Both present on every brief -> 5. Missing one angle on any brief -> 3. Both missing anywhere -> 1. |
| midpage_quotes_added | 0.09 | 0 | Verified Key Quotations added beyond the single Ingest quote. 2 to 3 more per brief -> 5. 1 more per brief -> 3. Zero added -> 1. |
| no_fabrication | 0.09 | 0 | All new content traces to a source PDF, Midpage result, or web-search citation. Any unsourced claim -> 0 here AND a red flag. |
| verified_flip_discipline | 0.05 | 0 | `verified` was flipped to today's date ONLY after every stub on the brief was resolved. Unresolved stubs remaining on a brief whose `verified` was advanced -> 0 here and a red flag. |
| scope_discipline | 0.10 | 0 | Enrich stayed inside its declared scope — analytical depth on briefs flagged `verified: "pending-enrich"`, ordered by skeleton-inventory burndown. No new pages created (creation belongs to Ingest or Synthesize), no Topic page rewrites (those belong to Synthesize), no cross-page link cascade (that belongs to Expand). The set of files_edited matches the run's declared scope. Strict scope -> 5. One adjacent edit (e.g., a one-line cross-link added in passing, with note) -> 3. Brief written from scratch in Enrich, or Topic page rewritten -> 0 AND a red flag. |
| brevity | 0.05 | 0 | This run's CHANGELOG entry stays inside the 120-word cap and uses the fixed shape from SKILL.md Step 2.3 (Did/Found/Files/Score/State bullets, optional fenced JSON extras — no prose paragraphs). The BUILD_NARRATIVE paragraph stays inside the 80-word cap. Compliant on both -> 5. One overflow under 50% over cap -> 3. Either overflow over 50% over OR per-phase JSON extras rendered as prose -> 0 AND a red flag. |

## Red flags

- `stubs_resolved` below 50% on any brief marked `verified: today`.
- Concurrence or dissent filled in with vote tallies instead of reasoning.
- Hypotheticals written as fact patterns with no "Why" reasoning.
- Critique section carrying only one ideological angle when both exist in the literature or are independently defensible.
- Any unsourced claim introduced during Enrich.
- Enrich scope included briefs without `verified: "pending-enrich"` when unfinished skeletons were available (skeleton inventory is burned down first).
- `cited_by` populated with an implausibly low number from CourtListener without a follow-up pending issue.
- Enrich created a brand-new page (Ingest's job) or rewrote a Topic page (Synthesize's job).

## Regression check

Compare to the rolling median over the last five Enrich runs on `.run-scores.jsonl`. Delta greater than 1.0 below median adds `regression-vs-median` to red flags. If the regression is explained by inheriting fully-finished briefs rather than skeletons (i.e., nothing to do), the explanation goes in the CHANGELOG entry for the run and the next Ingest should be reviewed for scope creep.
