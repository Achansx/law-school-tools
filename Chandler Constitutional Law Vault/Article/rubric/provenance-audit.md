# Rubric: Provenance Audit

Score each criterion 1 to 5. Apply when the Verify phase runs the provenance-audit sub-task on a single polished section.

The audit asks: does every factual claim in this section trace to a primary source or an evidence card? The article's central thesis is that AI systems should be inspectable and verifiable. This rubric measures whether the article itself meets that standard.

## What counts as a "factual claim"

- Numbers (page counts, percentages, dates, file counts, citation counts, run counts)
- Attributed quotations (direct or paraphrased)
- Named statistics (Magesh hallucination rates, Bond meta-review findings)
- Named events (Karpathy autoresearch release, Mata v. Avianca sanctions)
- Statements about what the vault contains or what the system did
- Comparisons (X vs Y) that imply measurement
- Procedural claims (the system uses X, the rotation is Y, the gate requires Z)

What does NOT count: argument transitions, rhetorical framings, opinions, hedges ("perhaps," "may"), restatements of the article's own thesis.

## 1. Claim coverage

- 1: <70% of factual claims have a mapped source (evidence card or footnote).
- 3: 70-89% mapped.
- 5: >=95% of factual claims have a mapped source. Unmapped claims are explicitly listed in `unsupported_claims` with a reason.

## 2. Primary-source ratio

- 1: <50% of mapped claims trace to a primary source (court opinion, original paper, original announcement, repository).
- 3: 50-79% trace to primary; rest cite secondary.
- 5: >=90% trace to primary sources. Internal vault artifacts (LESSONS, rubrics) only cited via appendix references, never as standalone authority for a factual claim in prose.

## 3. Attribution discipline

- 1: Quotations or attributed views without named source.
- 3: Most attribution present; a few "as some have noted" or "research suggests" style anonymizations.
- 5: Every attributed view names the author and a year; every quotation has a pin cite or line anchor.

## 4. Numerical precision

- 1: Numbers given without source or with conflicting values across sections.
- 3: Numbers sourced but some lack the source-as-of date.
- 5: Every number has a source AND a snapshot date. Numbers consistent across sections (Section IV's "198 pages" matches Section VIII's, etc.).

## 5. Gap honesty

- 1: Section reads as if everything is sourced when it isn't (the audit found gaps but the prose doesn't flag them).
- 3: Some gaps flagged inline ("see Appendix X for fuller treatment") but unsupported_claims list incomplete.
- 5: Every unmapped claim is in `unsupported_claims` with a `reason` field (one of: `evidence-gap`, `not-yet-harvested`, `requires-primary-source`, `intentional-conjecture`). The prose reads as if the audit happened, which it did.

## Exit conditions

- Section's polished frontmatter gets:
  - `provenance_audited: true`
  - `provenance_score: <average of 5 criteria, 0-5>`
  - `claims_total: <int>`
  - `claims_mapped: <int>`
  - `unsupported_claims: [...]` (list of objects with `claim_text`, `paragraph`, `reason`)
- Claim manifest gets appended: `manuscript/claim-manifest.jsonl` gains one entry per claim found in this section.
- If `provenance_score >= 4.5` AND `unsupported_claims` is empty (or all entries have `reason: intentional-conjecture` flagged for human review), the section passes audit.
- If `provenance_score < 4.5` OR unmapped claims exist with `reason` other than `intentional-conjecture`, the section returns to `polish_status: needs_polish` with the unmapped claims as targets for the next Cite/Polish cycle.

## Submission gate

Submission_ready will not flip until:
1. Every section has `provenance_audited: true`
2. Every section has `provenance_score >= 4.5`
3. Total `unsupported_claims` across all sections is zero (or all flagged `intentional-conjecture` with human acceptance)

This is the hard gate. The article's claim is that AI systems can be made verifiable. The article itself has to be verifiable.
