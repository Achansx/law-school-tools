# Rubric: Synthesize

Scale: 5 exemplary, 4 solid, 3 acceptable, 2 below expectations, 1 serious, 0 failure. Weighted average rounded to one decimal.

| Criterion | Weight | Red Flag At | Method |
|-----------|--------|-------------|--------|
| topic_pages_created_or_updated | 0.27 | 0 | Topic pages created or substantively updated. 0 -> 0. 1 -> 3. 2 -> 4. 3 or more -> 5. |
| exam_readiness | 0.22 | 1 | Topic pages touched have Governing Rule, Hypotheticals, and How to Spot on an Exam sections. All -> 5. Any missing -> 2. |
| no_synthesis_drift | 0.23 | 0 | Topic pages do not introduce claims absent from underlying case briefs. Yes -> 5. Any drift -> 0. |
| key_cases_table_current | 0.18 | 1 | Key Cases tables include all relevant cases from the vault. All -> 5. One missing -> 3. More -> 1. |
| scope_discipline | 0.10 | 0 | Synthesize stayed inside its declared scope — Topic page authoring and Key Cases tables sourced from existing brief content. No new Cases or Lectures created (Ingest), no Cases enriched in passing (Enrich), no cross-link cascade across unrelated pages (Expand). The set of files_edited is dominated by `Topics/`. Strict scope -> 5. One adjacent edit (e.g., a brief's `cited_by` updated to reflect the new Topic page) -> 4. Brief content rewritten or new Case page created -> 0 AND a red flag. |
| brevity | 0.05 | 0 | This run's CHANGELOG entry stays inside the 120-word cap and uses the fixed shape from SKILL.md Step 2.3 (Did/Found/Files/Score/State bullets, optional fenced JSON extras — no prose paragraphs). The BUILD_NARRATIVE paragraph stays inside the 80-word cap. Compliant on both -> 5. One overflow under 50% over cap -> 3. Either overflow over 50% over OR per-phase JSON extras rendered as prose -> 0 AND a red flag. |
