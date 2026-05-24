---
id: appendix-D
title: "Karpathy-Loop Per-Phase Rubric"
status: drafted
words: 999
target_min: 600
target_max: 1000
last_phase: harvest-appendix
source_files:
  - "<vault>/rubric/ingest.md, lint.md, enrich.md, expand.md, synthesize.md, verify.md (vault content-phase rubrics, now present in checkout; criterion names and weights reproduced verbatim in D.2)"
  - "<vault>/PROJECT_PRIMER.md and <vault>/RUNBOOK.md (vault phase rotation; Deploy first-class and Consolidate out-of-rotation placement)"
  - "<vault>/Article/rubric/*.md (article-build rubrics, in repo, reproduced in D.3)"
provenance_note: "The <vault>/rubric/ folder is now present in this checkout, so D.2 is reproduced directly from the six vault content-phase rubric files (ingest.md, lint.md, enrich.md, expand.md, synthesize.md, verify.md): phase goals are summarized from each rubric's preamble and the vault RUNBOOK, and every criterion name and weight is copied verbatim from each rubric's weighted-criteria table. This supersedes the run-119 reconstruction, written when the rubric folder had not been pushed (PI-114, now resolved), which carried only three verbatim criterion rows and left Expand's goal and the Lint/Enrich/Expand criterion bodies unavailable. D.3 (article rubrics) is reproduced in full from the in-repo Article/rubric/*.md files. Nothing in this appendix is invented; the Deploy and out-of-rotation Consolidate rubrics are present in the folder but intentionally excluded as outside the content rotation."
---

# Appendix D: Karpathy-Loop Per-Phase Rubric

## D.1 Concept

Both the vault and the article-build system run a single phase per scheduled tick, and each phase carries its own rubric file loaded only when that phase is active. The design was forced, not chosen. Early vault runs loaded one monolithic rubric covering all six phases, the full lessons file, and the whole build narrative every pass, so a formatting run spent its context budget on enrichment and verification criteria it would never use. The fix was tiered loading: one rubric file per phase, the lessons file skipped where unneeded, and a monthly-rotated narrative. The split also stopped one phase from gaming a shared scoring criterion to flatter its own number at another phase’s expense. Each run scores itself against its phase rubric, appends one line to a rolling scorecard, and records a short narrative entry; together the two artifacts let a reviewer reconstruct the loop’s state at any past tick, which is what makes the loop reviewable rather than opaque.

## D.2 Vault rubrics (six-phase content rotation)

The vault’s content rotation is Ingest, Lint, Enrich, Expand, Synthesize, Verify, then repeat (vault PROJECT_PRIMER); the RUNBOOK adds Deploy as a first-class publish phase after Verify and runs Consolidate out of rotation. Each vault rubric scores weighted criteria 0-to-5 across four columns (Criterion, Weight, Red Flag At, Method), reports a weighted average to one decimal, and trips a hard red flag when a flagged criterion hits its threshold. Every phase also reserves a fixed governance allotment: `scope_discipline` 0.10 and `brevity` 0.05. The goals and weights below are reproduced directly from the vault rubric files (see the provenance note).

| Phase | Goal |
|-------|------|
| Ingest | Produce a skeleton case brief: the factual sections (Memory Jogger, Facts, Procedural History, Judicial Votes, Holding) at depth, exactly one Midpage-verified pin-cited quotation, and a `<!-- ENRICH: -->` marker on every deferred section rather than writing it. |
| Lint | Structural and template enforcement: frontmatter schema, the fixed H2 sequence, filename/H1/frontmatter-name agreement, and `source_files`/`## Sources` parity, fixing only genuinely broken links. |
| Enrich | Resolve the stubbed sections: concurrence and dissent reasoning, five hypotheticals with reasoning, a both-sides critique, additional verified quotations, and connections. |
| Expand | Add cross-references among Cases, Topics, and Lectures, each with a reciprocal link on the target page, plus comparison tables between related doctrines, using CourtListener citation chains to find missing connections. |
| Synthesize | Build a Topic page in the exam-ready scaffold: Governing Rule, Doctrinal Development, Key Cases table, hypotheticals, How to Spot on an Exam, Critique, Connections, with no claim absent from the underlying briefs. |
| Verify | Adversarial three-persona pass (each persona returns at least one finding), holding spot-checks against Midpage, cross-file consistency, and a pending-issue aging sweep. |

Complete criterion set and weights (verbatim from the vault rubric files):

| Phase | Weighted criteria (weight) |
|-------|----------------------------|
| Ingest | files_processed 0.15; classification_accuracy 0.10; skeleton_completeness 0.20; stub_markers_present 0.15; scope_discipline 0.10; midpage_verification 0.10; source_attribution 0.10; backfill_coverage 0.10; brevity 0.05 |
| Lint | structural_fixes 0.27; pending_issues_cleared 0.18; template_enforcement 0.18; broken_links_fixed 0.04; source_attribution_sync 0.13; no_net_regressions 0.10; scope_discipline 0.10; brevity 0.05 |
| Enrich | stubs_resolved 0.22; concurrence_and_dissent 0.18; hypos_with_reasoning 0.14; critique_balance 0.13; midpage_quotes_added 0.09; no_fabrication 0.09; verified_flip_discipline 0.05; scope_discipline 0.10; brevity 0.05 |
| Expand | cross_references_added 0.27; reciprocal_links 0.22; comparison_tables 0.18; citation_chain_used 0.23; scope_discipline 0.10; brevity 0.05 |
| Synthesize | topic_pages_created_or_updated 0.27; exam_readiness 0.22; no_synthesis_drift 0.23; key_cases_table_current 0.18; scope_discipline 0.10; brevity 0.05 |
| Verify | adversarial_findings 0.28; holding_verification 0.17; cross_file_consistency 0.15; pending_issues_emitted 0.20; pending_issue_aging 0.10; scope_discipline 0.10; brevity 0.05 |

In each phase the largest-weight criterion names its purpose (Lint `structural_fixes` 0.27, Verify `adversarial_findings` 0.28). Many criteria carry a red flag at 0 or 1, so a single failure floors the run regardless of the weighted average. The Deploy rubric (`deploy.md`) and the out-of-rotation Consolidate rubric live in the same folder but are intentionally excluded here, as the article’s argument concerns the content phases.

## D.3 Article-build rubrics (seven phases plus two sub-tasks)

Rotation: Harvest, Outline, Draft, Cite, Polish, Stitch, Verify. Each rubric scores five criteria 1 to 5, unweighted, reported as an average. Criterion names are verbatim from `Article/rubric/<phase>.md`.

| Phase / sub-task | Five criteria |
|------------------|---------------|
| Harvest | Section targeting; Source diversity; Traceability; Non-duplication; Gap logging |
| Outline | Structural fidelity; Evidence binding; Word budgeting; Argument granularity; Open-question discipline |
| Draft | Argument structure; Evidence use; Voice; Fabrication discipline; Word-budget compliance |
| Cite | Coverage; Bluebook form; URL liveness; Primary-source discipline; Internal-cite hygiene |
| Polish | Mechanical hygiene; Voice consistency; Sentence tightness; First-person discipline; Section coherence |
| Stitch | Terminology unity; Fact consistency; Recurring-sentence placement; Transition quality; Word count and assembly |
| Verify | Persona coverage; Forced-finding compliance; Finding specificity; Suggested-fix quality; State routing |
| Abstract (Outline sub-task) | Thesis clarity; Method visibility; Case-study framing; Honest scoping; Word discipline and JLE voice |
| Appendix (Harvest sub-task) | Source fidelity; Completeness; Replicability; Reference usability; Word discipline |

## D.4 What we changed and why

The two rubric families answer to the work they score. The vault’s phases produce structured artifacts whose quality is largely mechanical (does the brief carry one verified pin cite, do filename, H1, and frontmatter agree), so its rubrics weight named criteria toward a single per-run number and trip a red flag below a hard threshold. The article’s phases produce prose whose quality is a matter of judgment, so its rubrics drop weights and thresholds in favor of five 1-to-5 anchors averaged evenly. What both share is the constraint that produced them: one rubric file per phase, loaded only by that phase. Running both systems at once tested that principle: the same tiered-loading discipline carried across a structured-artifact task and a long-form-prose task without modification, the strongest available evidence that the loop’s architecture, not its content, is the transferable contribution.

*Cross-reference:* supports Section VI (Prompting as Pedagogical Design) and Section VII (Iterative Improvement Under Professorial Control).
