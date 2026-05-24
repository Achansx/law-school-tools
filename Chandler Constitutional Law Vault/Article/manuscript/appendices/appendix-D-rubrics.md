---
id: appendix-D
title: "Karpathy-Loop Per-Phase Rubric"
status: needs_work
words: 921
target_min: 600
target_max: 1000
last_phase: harvest-appendix
source_files:
  - "<vault>/rubric/*.md (vault rubrics, NOT in this checkout; reconstructed in part from evidence cards)"
  - "<vault>/Article/rubric/*.md (article-build rubrics, in repo, reproduced)"
provenance_note: "The <vault>/rubric/ folder (the six vault-side rubrics) was not included in this repository checkout; only Article/ and Article-Workplan.md were pushed. D.3 (article rubrics) is reproduced in full from the in-repo Article/rubric/*.md files. D.2 (vault rubrics) is reconstructed only as far as the verified Section VI/VII evidence cards carry it: phase goals from evidence-07-six-phase-rotation and the evidence-06 prompt cards; criterion rows quoted verbatim where a card reproduced them (ingest scope_discipline, synthesize exam_readiness, the verify criteria header and adversarial_findings row), with the verify weight list as recorded by evidence-07-scorecard-and-build-narrative. The full per-criterion bodies for Lint, Enrich, and Expand are not captured by any evidence card and are NOT reproduced here; the gap is logged (PI-114). Nothing in this appendix is invented."
---

# Appendix D: Karpathy-Loop Per-Phase Rubric

## D.1 Concept

Both the vault and the article-build system run a single phase per scheduled tick, and each phase carries its own rubric file loaded only when that phase is active. The design was forced, not chosen. Early vault runs loaded one monolithic rubric covering all six phases, the full lessons file, and the entire build narrative every pass, so a structural-formatting run was spending its context budget reading enrichment and verification criteria it would never use. The fix was tiered loading: split the rubric into one file per phase, skip the lessons file for phases that do not need it, and rotate the narrative monthly so the file a run must read stays bounded. The split also closed a second problem, in which one phase could game a shared scoring criterion to flatter its own number while making another phase harder. Each run scores itself against its phase rubric and appends one line to a rolling scorecard; a two-to-four-sentence narrative entry records what changed. The two artifacts together let a reviewer reconstruct the loop's state at any past tick, which is the condition that makes the loop reviewable rather than opaque.

## D.2 Vault rubrics (six-phase rotation)

Rotation: Ingest, Lint, Enrich, Expand, Synthesize, Verify, then repeat. Vault rubrics use a weighted-criteria table (`Criterion | Weight | Red Flag At | Method`) rather than the article's 1-to-5 anchors. The phase goals and the criterion rows below are reproduced only as far as the verified evidence cards carry them; see the provenance note.

| Phase | Goal (sourced) |
|-------|----------------|
| Ingest | Produce a skeleton case brief: fill Memory Jogger, Facts, Procedural History, Judicial Votes, and Holding at depth, a ~150-word majority Analysis sketch, exactly one Midpage-verified pin-cited quotation, and stub the rest with `<!-- ENRICH: -->` markers. |
| Lint | Structural and template enforcement: score filename, H1, and frontmatter-name agreement, and the fixed body sequence. |
| Enrich | Fill the stubbed sections: concurrence and dissent reasoning, the five hypotheticals, both-sides critique, additional quotations, and connections. |
| Expand | *Not captured in available evidence (PI-114).* |
| Synthesize | Build a Topic page in the exam-ready scaffold: Governing Rule blockquote, Doctrinal Development, Key Cases table, five hypotheticals, How to Spot on an Exam, Critique, Connections. |
| Verify | Adversarial three-persona pass (Staleness Auditor, Contradiction Hunter, Template Enforcer); each persona must return at least one finding per run. |

Criterion rows reproduced verbatim from the evidence cards (vault rubric files absent from checkout):

```
# rubric/ingest.md
| scope_discipline | 0.10 | 0 | Verify none of the skeleton briefs were written at 9-section depth. `verified` on every new brief is "pending-enrich". Any brief written at full depth or flipped to today's date during Ingest -> 0 here and a red flag. |

# rubric/synthesize.md
| exam_readiness | 0.22 | 1 | Topic pages touched have Governing Rule, Hypotheticals, and How to Spot on an Exam sections. All -> 5. Any missing -> 2. |

# rubric/verify.md (header + largest-weight row verbatim; remaining weights per evidence-07-scorecard-and-build-narrative)
| Criterion | Weight | Red Flag At | Method |
| adversarial_findings | 0.28 | 0 | Forced-finding count from the three personas. 0 -> 0. 1 to 2 -> 2. 3 to 4 -> 4. 5 or more -> 5. |
# also recorded: holding_verification 0.17, cross_file_consistency 0.15,
# pending_issues_emitted 0.20, pending_issue_aging 0.10, scope_discipline 0.10, brevity 0.05
```

Synthesize also carries a `no_synthesis_drift` criterion (Topic pages introduce no claim absent from the underlying briefs) and Enrich a `scope_discipline` criterion, both named in the cards but not reproduced with weights.

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

The two rubric families answer to the work they score. The vault's phases produce structured artifacts whose quality is largely mechanical (does the brief carry one verified pin cite, do filename, H1, and frontmatter agree), so its rubrics weight named criteria toward a single per-run number and trip a red flag below a hard threshold. The article's phases produce prose whose quality is a matter of judgment (is the voice practitioner-scholarly, does the section earn the next one), so its rubrics drop weights and red-flag thresholds in favor of five 1-to-5 anchor descriptions averaged evenly. What both share is the constraint that produced them: one rubric file per phase, loaded only by its own phase. Running the two systems at once was the test of that principle. The same tiered-loading discipline carried across a structured-artifact task and a long-form-prose task without modification, which is the strongest available evidence that the loop's architecture, not its content, is the transferable contribution.

*Cross-reference:* this appendix supports Section VI (Prompting as Pedagogical Design) and Section VII (Iterative Improvement Under Professorial Control).
