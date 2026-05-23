# Rubric: Abstract

Score each criterion 1 to 5. Apply when the Outline phase is drafting or refreshing `manuscript/abstract.md`.

## 1. Thesis clarity

- 1: Reader cannot state the article's argument after reading the abstract.
- 3: Argument visible but mixed with descriptive scaffolding.
- 5: Argument is the first or second sentence, in one clean clause.

## 2. Method visibility

- 1: No mention that the article describes a method, only that an artifact exists.
- 3: Method mentioned in passing.
- 5: The method (AI plus structured notes plus iterative expert review) is named and positioned as the contribution.

## 3. Case study framing

- 1: Reads as a product description of the Constitutional Law website.
- 3: Case study present but overshadows the method claim.
- 5: Case study explicitly framed as illustration; the contribution is the replicable method, not the artifact.

## 4. Honest scoping

- 1: Implies learning-outcomes claims, or implies generality not demonstrated.
- 3: Scope hedged but unevenly (one section escapes the hedge).
- 5: Explicitly disclaims learning-outcomes measurement (per workplan §5) and signals the limits of generalization (per Section X).

## 5. Word discipline and JLE voice

- 1: Outside 225 to 275 words, or reads as a tech announcement.
- 3: Within range, voice mixed (some product-launch sentences).
- 5: 240 to 260 words, practitioner-scholarly throughout, no em dashes or straight ASCII quotes.

## Exit conditions

- `abstract.status: ready_for_review` when all five criteria score 4 or above and `abstract.words` is within 225 to 275.
- `abstract.status: ready_for_human_review` when the rubric average is 4.5+ on three consecutive Outline-abstract runs without substantive edits. The professor reviews the abstract before further Outline runs continue on body sections. This is a gate hint, not an auto-gate — the Outline phase logs to BUILD_NARRATIVE and continues; the human flips the gate.
