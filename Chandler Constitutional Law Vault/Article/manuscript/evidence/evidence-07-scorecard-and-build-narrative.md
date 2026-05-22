---
section: "07"
fact_type: argument
source_path: "Chandler Constitutional Law Vault/rubric/verify.md"
verified: true
notes: "The run-by-run scorecard and the rolling BUILD_NARRATIVE are the loop's audit trail and are what distinguish a reviewable loop from an opaque one. Each Verify run (and by symmetry each Lint, Enrich, Expand, Synthesize, Deploy run) scores itself against a per-phase rubric of weighted criteria (rubric/verify.md weights adversarial_findings 0.28, holding_verification 0.17, cross_file_consistency 0.15, pending_issues_emitted 0.20, pending_issue_aging 0.10, scope_discipline 0.10, brevity 0.05; each criterion has a red-flag threshold below which the run is flagged for human review). The score is appended to .run-scores.jsonl as a single JSON line per run. A second artifact, BUILD_NARRATIVE_YYYY-MM.md, carries a 2-to-4-sentence prose entry per run describing what changed and what was learned. The two artifacts together let a reviewer reconstruct the loop's state at any past moment: the scorecard for measurable phase quality and the narrative for the structural-decision context the score alone cannot carry. The article's argument is that this audit trail is what makes the loop reviewable rather than opaque, which is the condition for a JLE-publishable methodology rather than a Silicon Valley demo. The article's own writing system replicates the same architecture (Article/.article-scores.jsonl and Article/BUILD_NARRATIVE_YYYY-MM.md). Per L-029 in the article's own LESSONS the prose narrative may carry deliberate procedural sentences over 35 words when their primary work is enumerating the rotation's stages; the audit-trail framing is one such enumeration."
---

The loop carries two paired artifacts the rotation writes on every tick. The scorecard, `.run-scores.jsonl`, holds one JSON line per run, each line containing the active phase, the weighted criteria scores, the red-flag list if any, and the timestamp; the per-phase rubric defines the weights and the red-flag thresholds. The rolling narrative, `BUILD_NARRATIVE_YYYY-MM.md`, holds a two-to-four-sentence prose entry per run describing what the phase actually did and what was learned. The two artifacts together let a reviewer reconstruct the loop's state at any past moment: the scorecard for measurable phase quality and the narrative for the structural context the score cannot carry by itself.

Exact source quote, `Chandler Constitutional Law Vault/rubric/verify.md` lines 5 to 7 (the criteria header and the largest-weight criterion):

> | Criterion | Weight | Red Flag At | Method |
> |-----------|--------|-------------|--------|
> | adversarial_findings | 0.28 | 0 | Forced-finding count from the three personas. 0 -> 0. 1 to 2 -> 2. 3 to 4 -> 4. 5 or more -> 5. |
