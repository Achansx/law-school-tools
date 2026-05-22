# Rubric: Harvest

Score each criterion 1 to 5. Total reported as average. Append result to `.article-scores.jsonl`.

## 1. Section targeting

- 1: Pulled evidence for an arbitrary or already-saturated section.
- 3: Pulled evidence for a section flagged `needs_work`.
- 5: Pulled evidence for the section with the highest gap-to-target ratio.

## 2. Source diversity

- 1: All evidence cards point to the same source file.
- 3: Two or three distinct sources cited.
- 5: Four or more distinct sources across vault and external (where appropriate).

## 3. Traceability

- 1: Evidence cards lack source paths or URLs.
- 3: Source paths present; verification flag inconsistent.
- 5: Every card has source path or URL, verification flag set, and exact quoted excerpt where applicable.

## 4. Non-duplication

- 1: More than half of new cards duplicate existing cards.
- 3: Some overlap; new cards add value.
- 5: All new cards add genuinely new facts.

## 5. Gap logging

- 1: No `pending_issues` updates despite obvious gaps.
- 3: Some gaps logged.
- 5: Every claim the section will make that is not yet evidenced is logged with a specific gap description.
