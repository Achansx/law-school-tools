# Con Law Wiki -- Run Scorecard Rubric

Scoring criteria for each phase of the vault maintenance rotation. Every run is scored 0 to 5 per criterion, weighted, and appended to `.run-scores.jsonl`. Red flags trigger pending issues for the next Lint cycle.

Scoring scale: 5 = exemplary, 4 = solid, 3 = acceptable with minor gaps, 2 = below expectations, 1 = serious problem, 0 = failure mode.

---

### Ingest

| Criterion | Weight | Red Flag At | Method |
|-----------|--------|-------------|--------|
| files_processed | 0.25 | 0 | Source files successfully turned into wiki pages. 0 -> 0. 1 -> 2. 2 to 3 -> 4. 4 to 5 -> 5. |
| classification_accuracy | 0.25 | 1 | Files correctly classified (case reading vs lecture vs supplemental). Self-graded with evidence: cite one tricky classification and why it was resolved that way. |
| brief_completeness | 0.30 | 1 | Case briefs created this run have all 9 sections at least stubbed. All sections present -> 5. 1 missing -> 3. 2 or more missing -> 1. |
| midpage_verification | 0.20 | 0 | Fraction of case briefs that had holdings/quotes verified via Midpage. 100% -> 5. 50% -> 3. 0% -> 1. |

### Lint

| Criterion | Weight | Red Flag At | Method |
|-----------|--------|-------------|--------|
| broken_links_fixed | 0.30 | 0 | Count of broken wiki-links resolved. 0 -> 0. 1 to 2 -> 3. 3 to 5 -> 4. 6 or more -> 5. |
| pending_issues_cleared | 0.25 | 0 | Fraction of pending issues cleared this run. Ratio times 5. |
| template_enforcement | 0.25 | 1 | Pages touched that now match the template. 100% -> 5. 90% -> 4. Below 80% -> 2. |
| no_net_regressions | 0.20 | 0 | Lint did not introduce new broken links or template violations. Yes -> 5. Any introduced -> 0. |

### Enrich

| Criterion | Weight | Red Flag At | Method |
|-----------|--------|-------------|--------|
| sections_deepened | 0.30 | 0 | Case brief sections brought up to the 9-section standard. 0 -> 0. 1 to 3 -> 3. 4 to 6 -> 4. 7 or more -> 5. |
| midpage_quotes_added | 0.25 | 0 | Verified Key Quotations added with pin-cite URLs. 0 -> 1. 1 to 2 -> 3. 3 or more -> 5. |
| no_fabrication | 0.25 | 0 | All new content is traceable to a source PDF, Midpage, or web search. Yes -> 5. Any unsourced claim -> 0. |
| hypos_and_critique | 0.20 | 0 | Hypothetical Applications and Critique sections meaningfully filled. Ratio of enriched briefs with both sections times 5. |

### Expand

| Criterion | Weight | Red Flag At | Method |
|-----------|--------|-------------|--------|
| cross_references_added | 0.30 | 0 | New wiki-links between Cases, Topics, and Lectures. 0 -> 0. 1 to 3 -> 3. 4 or more -> 5. |
| reciprocal_links | 0.25 | 1 | Every new outgoing link has a reciprocal in the target page. All -> 5. Any missing -> 2. |
| comparison_tables | 0.20 | 0 | New or updated comparison tables between related doctrines. 0 -> 2. 1 -> 4. 2 or more -> 5. |
| citation_chain_used | 0.25 | 0 | CourtListener find_cited_cases or find_citing_cases used to discover missing vault connections. Yes -> 5. No -> 2. |

### Synthesize

| Criterion | Weight | Red Flag At | Method |
|-----------|--------|-------------|--------|
| topic_pages_created_or_updated | 0.30 | 0 | Topic pages created or substantively updated. 0 -> 0. 1 -> 3. 2 -> 4. 3 or more -> 5. |
| exam_readiness | 0.25 | 1 | Topic pages touched have Governing Rule, Hypotheticals, and How to Spot on an Exam sections. All -> 5. Any missing -> 2. |
| no_synthesis_drift | 0.25 | 0 | Topic pages do not introduce claims absent from underlying case briefs. Yes -> 5. Any drift -> 0. |
| key_cases_table_current | 0.20 | 1 | Key Cases tables include all relevant cases from the vault. All -> 5. One missing -> 3. More -> 1. |

### Verify

| Criterion | Weight | Red Flag At | Method |
|-----------|--------|-------------|--------|
| adversarial_findings | 0.35 | 0 | Forced-finding count from the three personas. 0 -> 0. 1 to 2 -> 2. 3 to 4 -> 4. 5 or more -> 5. |
| holding_verification | 0.20 | 1 | Sample of case briefs had holdings spot-checked against Midpage. All correct -> 5. One inaccuracy -> 3. More -> 1. |
| cross_file_consistency | 0.20 | 0 | Inter-page contradictions flagged (same case described differently in two pages). 0 -> 2. 1 or more with evidence -> 5. |
| pending_issues_emitted | 0.25 | 1 | Every finding yielded a pending issue for the next phase. All -> 5. Any unlogged -> 2. |
