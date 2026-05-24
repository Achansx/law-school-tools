# Scoring Rubric: Consolidate

Out-of-rotation sweep. Score the run against these criteria on a 0-5 scale and take a weighted average rounded to one decimal.

| Criterion | Weight | What a 5 looks like |
|-----------|-------:|---------------------|
| **Candidate processing** | 0.25 | Every `lesson-candidate` in `pending_issues` was either merged into an existing entry or promoted as a new entry. None was silently dropped. |
| **Duplicate detection** | 0.20 | At least one pre-existing duplicate pair was identified and merged. Merges preserve the more specific example or citation. |
| **Staleness pruning** | 0.15 | Every vault path mentioned in LESSONS was glob-checked. Stale references were either updated or the entry was removed with an archive copy. |
| **Cap compliance** | 0.15 | Post-run entry count is at or below 35. If not, a `cap-violation` pending issue exists describing why. |
| **Archive integrity** | 0.10 | A dated `archive/LESSONS_YYYY-MM-DD.md` was written before any edit. Pruned-but-not-superseded entries are recoverable from it. |
| **Pruning discipline** | 0.10 | No more than 5 entries removed in this sweep. If more looked removable, the remainder became `consolidation-review` pending issues. |
| **State hygiene** | 0.05 | `last_consolidation` updated, processed candidates removed from `pending_issues`, `next_phase` NOT advanced. |
| **Brevity** | 0.05 | Every promoted/merged LESSONS.md entry fits the 60-word cap and the `Rule. Why. How to apply. _Seen:_` shape from SKILL.md Step 2.4. Each `_Seen:_` footer carries ≤3 dated instances (drop oldest when adding a fourth). The BUILD_NARRATIVE summary paragraph stays inside the 80-word cap. Any over-cap entry → 0 here AND a `lesson-bloat` red flag. |

## Red flags

- Entry count increased instead of stabilizing or dropping.
- A lesson was deleted with no newer entry covering the same guidance AND no archive copy.
- A new H2 section was created when an existing one would have fit.
- More than 5 entries were removed in one sweep.
- `lesson-candidate` items remain in `pending_issues` after the run.
- `next_phase` was advanced (it should stay untouched so the rotation resumes).

## Regression check

If the post-run entry count is not lower than at the start of the run (and no candidates were promoted), the sweep had no effect and should not be scheduled again for at least 7 days regardless of entry count.
