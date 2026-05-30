---
id: "06"
title: "Prompting as Pedagogical Design"
status: needs_polish
target_words: 800
word_count: 868
last_phase: verify-provenance
draft_status: needs_polish
cite_status: needs_cite
polish_status: needs_polish
footnotes_count: 13
provenance_audited: true
provenance_score: 4.2
claims_total: 20
claims_mapped: 19
unsupported_claims:
  - claim_text: "VI.B paragraph 2 asserts 'The nine-section sequence is the canonical law-school case-brief format'; the structure traces to the vault's own Templates/Case Brief.md and the PROJECT_PRIMER '9-section case-briefer standard' (evidence-05-case-brief-nine-section-standard.md), but the canonical-national-convention characterization carries no external legal-education authority. Footnotes [^2] and [^3] source only the template's loading and its own field/section schema, not the convention claim."
    paragraph: 2
    reason: requires-primary-source
---

# VI. Prompting as Pedagogical Design

## A. Qian’s typology and the vault as process-based prompting

Yufeng Qian’s systematic review of prompt engineering in education distinguishes technique-based strategies from process-based strategies. Technique-based strategies are single-ask patterns like role-prompting, few-shot examples, and chain-of-thought reasoning. Process-based strategies are multi-step workflows in which each prompt is one move in a longer pedagogical loop. The vault’s prompt library is process-based in Qian’s sense. No single prompt produces a finished artifact; the pedagogical work happens across the six-phase rotation of Ingest, Lint, Enrich, Expand, Synthesize, and Verify, where each phase’s prompt depends on the prior phase’s output. Qian surveys K-12 and general higher-education settings rather than legal education specifically, so the architectural insight imports while the exam-and-Bluebook discipline the vault layers on top is the article’s own contribution.[^1]

## B. The typed schema is the prompt

The Case Brief template is the prompt contract. Its frontmatter schema names eighteen required fields along with the holding-bar block, the citation-metadata block, and the authority-lineage block. Its body specifies nine fixed H2 sections in fixed order, from Memory Jogger through Sources, with Analysis broken out into Majority, Concurrence, and Dissent. Every Ingest and Enrich run loads this template as part of its prompt;[^2] the model is asked to fill the typed scaffold rather than to write a brief about a case in whatever shape it prefers. The choice is pedagogical rather than merely structural. The nine-section sequence is the canonical law-school case-brief format. Committing the prompt to that sequence forces every generated brief to do the same analytical work a student is expected to do when briefing a case by hand. Section V described the same schema as machine-readable substrate for the generated note. Section VI reframes it as the prompt’s pedagogical commitment, since the templates specify both what an AI-authored note must contain and what the prompt producing it must require.[^3]

## C. Prompts as pedagogical commitments: distribution, balance, depth

The Ingest prompt deliberately under-completes the case brief, filling the factual sections at full depth, writing a majority-only Analysis sketch of roughly 150 words, placing one Midpage-verified pin-cited quotation, and leaving every other section as a one-line stub marker.[^4] The rubric’s *scope_discipline* criterion mechanically scores down any brief written at full nine-section depth in a single pass, because finishing the brief on the first read starves the next phase of analytical work. The pedagogy is partly in what the prompt forbids.[^5]

The Enrich prompt for Hypothetical Applications requires five hypos in a fixed distribution (two same-side, two opposite-side, one fence-sitter), each carrying a fact pattern and the reasoning that applies the rule; a fact-pattern-only hypo scores zero. The distributional commitment encodes the law-school exam pedagogy of testing a rule against varying fact patterns at the prompt level.[^6]

The Enrich Critique prompt requires at least one progressive angle and one originalist or textualist angle per enriched brief, with the rubric scoring 3 for one missing and 1 for both missing. The two-angle requirement prevents the prompt from collapsing into whichever interpretive frame the model would default to and encodes the field’s interpretive pluralism at the structural level.[^7]

The Synthesize prompt produces a Topic page in a fixed exam-ready scaffold (Governing Rule blockquote, Doctrinal Development, Key Cases table, the five-hypothetical distribution Enrich uses, How to Spot on an Exam, Critique, Connections), with *exam_readiness* weighted at 0.22 of the run score. Case briefs answer what an opinion holds; Topic pages answer what rule the doctrine produces and how a student deploys it on an exam.[^8]

## D. Verification as pedagogy: Midpage discipline and adversarial reading

The Ingest and Enrich prompts both gate Key Quotations on Midpage verification, requiring confirmation against the indexed opinion rather than the paraphrased PDF the professor distributed. The *Prize Cases* failure documents what happens when the discipline lapses: a modernized PDF silently rewrote Justice Grier’s archaic phrasing, and an Ingest, a Lint, two Enrich, and an Expand pass all reproduced the rewrite because none re-checked against the indexed text; only the adversarial Verify pass returned the actual language. The prompt encodes a practitioner habit as a citation-accuracy commitment at the prompt-design level.[^9]

The Verify prompt instantiates three adversarial personas (Staleness Auditor, Contradiction Hunter, Template Enforcer) with a three-row lead-rotation table and a four-row per-persona focus-mutation table, both keyed off the Verify run count.[^10] Each persona must return at least one finding per run; a persona that finds nothing records *persona-produced-nothing* as its own finding. The Verify prompt implements adversarial reading at the prompt level rather than as an external review process. The architecture mirrors moot-court and law-review pedagogy, where work meets readers with different reading commitments rather than a single generic reader.[^11]

## E. Compounding prompts: stub-marker handoffs and LESSONS as iteration memory

Each Ingest skeleton carries `<!-- ENRICH: -->` markers in every section it deliberately did not fill. The Ingest rubric’s *stub_markers_present* criterion scores 5 only when every deferred section carries a stub with a one-sentence description; the Enrich rubric’s *stubs_resolved* criterion, weighted at 0.22, measures the fraction of markers each Enrich run closed. Prompt design here is as much about handoffs between prompts as about any single prompt’s wording.[^12]

LESSONS.md is the prompt-iteration memory file. Each entry follows a fixed schema (Rule, Why, How to apply, Seen) capped at 60 words and 35 entries, loaded only by content-editing phases. Representative amendments include the em-dash typography rule, the no-invented-case-details rule, and the rule added after *Learning Resources, Inc. v. Trump* showed that filling Connections at Ingest seeded broken links. The prompt library compounds rather than restarts.[^13]

## Footnotes

[^1]: Yufeng Qian, *Prompt Engineering in Education: A Systematic Review of Approaches and Educational Applications*, J. Educational Computing Research (Aug. 2025), https://journals.sagepub.com/doi/abs/10.1177/07356331251365189 (last visited May 18, 2026) (distinguishing technique-based prompting strategies (single-ask patterns including role-prompting, few-shot examples, and chain-of-thought reasoning) from process-based prompting strategies (multi-step workflows in which each prompt is one move in a longer pedagogical loop); the vault’s six-phase rotation is process-based in Qian’s sense, with each phase’s prompt depending on the prior phase’s output).

[^2]: *See infra* App. B (Prompt Library) (Case Brief template loaded as part of every Ingest and Enrich prompt as the typed-schema fill contract; appendix capture pending, see PI-035).

[^3]: *See infra* App. C (Obsidian Note Templates) (`Templates/Case Brief.md` frontmatter schema enumerating the eighteen required fields plus the holding-bar block carrying `issue`, `holding`, `reasoning`, and `doctrine_family`, the citation-meta block carrying `argued`, `decided`, `panel`, `author`, `vote`, and `disposition`, and the authority-lineage block carrying `relies_on`, `distinguishes`, `applied_in`, `overrules`, and `overruled_by`; nine fixed H2 sections in fixed order: Memory Jogger, Facts, Procedural History, Judicial Votes, Holding, Analysis with Majority, Concurrence, and Dissent breakouts, Hypothetical Applications, Critique, and Key Quotations, plus Key Points, Connections, and Sources); *see also supra* Section V (Building the Obsidian Vault) (documenting the same schema as the substrate for AI-authored notes; this section reframes the same schema as the prompt’s pedagogical commitment).

[^4]: *See infra* App. B (Prompt Library) (Ingest skeleton-prompt and `<!-- ENRICH: -->` stub-marker convention; appendix capture pending, see PI-035).

[^5]: *See infra* App. D (Karpathy-Loop Per-Phase Rubric) (vault `RUNBOOK.md` Phase: Ingest Step 5 instructing the Ingest prompt to fill Memory Jogger, Facts, Procedural History, Judicial Votes, and Holding at full depth, write a majority-only Analysis sketch of roughly 150 words, place exactly one Midpage-verified pin-cited quotation in Key Quotations, and leave every other section as a one-line `<!-- ENRICH: one-sentence description -->` stub marker; `rubric/ingest.md` *scope_discipline* criterion (weight 0.10) returning 0 and a red flag for any brief written at full nine-section depth during Ingest or for any `verified` field flipped to a today-dated value before Enrich).

[^6]: *See infra* App. D (Karpathy-Loop Per-Phase Rubric) (vault `RUNBOOK.md` Phase: Enrich Step 3 specifying five Hypothetical Applications per brief in a fixed two-same-side, two-opposite-side, one-fence-sitter distribution, each requiring a fact pattern and the reasoning that applies the rule to those facts; `rubric/enrich.md` *hypos_with_reasoning* criterion (weight 0.14) scoring 5 for all five present, 3 for four, 1 for three or fewer, with fact-pattern-only hypos counted as 0 for that slot).

[^7]: *See infra* App. D (Karpathy-Loop Per-Phase Rubric) (vault `RUNBOOK.md` Phase: Enrich Step 3 requiring at least one progressive angle and one originalist-or-textualist angle in the Critique section per enriched brief, each grounded in a published critique or a clearly signposted independent argument; `rubric/enrich.md` *critique_balance* criterion (weight 0.13) scoring 5 for both angles present on every brief, 3 if one angle is missing on any brief, 1 if both are missing anywhere).

[^8]: *See infra* App. C (Obsidian Note Templates) (`Templates/Topic Page.md` specifying a Governing Rule blockquote stating the rule in exam-ready prose with the controlling case attached inline, Doctrinal Development walking the case-by-case progression with the foundational case first, a Key Cases pipe table, Hypothetical Applications in the same five-hypothetical two-same-two-opposite-one-fence distribution Enrich uses for case briefs, How to Spot on an Exam, Critique, and Connections); *see also infra* App. D (Karpathy-Loop Per-Phase Rubric) (`rubric/synthesize.md` *exam_readiness* criterion (weight 0.22) scoring 5 only when every touched Topic page carries Governing Rule, Hypotheticals, and How to Spot on an Exam at minimum; vault `RUNBOOK.md` Phase: Synthesize requiring a topic to qualify when at least two case briefs plus one lecture cover it).

[^9]: *See infra* App. D (Karpathy-Loop Per-Phase Rubric) (vault `RUNBOOK.md` Phase: Enrich cardinal rule providing that Key Quotations are Midpage-verified text with pin-cite URLs or they do not enter the vault; `rubric/ingest.md` *midpage_verification* criterion (weight 0.10) scoring 5 only when each new case brief carries exactly one Midpage-verified pin-cited quote with populated `midpage_id` and `midpage_url` fields; vault verify-against-the-indexed-opinion rule with the *Prize Cases* failure story as its dated instance, recording that an Ingest pass, a Lint pass, two Enrich passes, and an Expand pass each reproduced the modernized phrasing because none re-checked against the indexed opinion, and only the adversarial Verify pass returned the actual language); *see also infra* Section VII (Iterative Improvement Under Professorial Control) (developing the iteration narrative from the *Prize Cases* failure into a durable prompt amendment).

[^10]: *See infra* App. B (Prompt Library) (Verify-phase persona prompts with three-row lead-rotation table and four-row per-persona focus-mutation table, both keyed off `state.verify_run_count`; appendix capture pending, see PI-035).

[^11]: *See infra* App. D (Karpathy-Loop Per-Phase Rubric) (`PERSONAS.md` instantiating Staleness Auditor, Contradiction Hunter, and Template Enforcer as the three Verify-phase personas, each required to return at least one finding per run and to record *persona-produced-nothing* as its own finding if it finds nothing; lead-rotation table keyed off `state.verify_run_count % 3` rotating which persona’s findings are listed and loaded first; per-persona focus-mutation table keyed off `state.verify_run_count % 4`, deliberately offset from the lead cycle so that lead-and-focus pairings change every run rather than locking into a twelve-run loop).

[^12]: *See infra* App. D (Karpathy-Loop Per-Phase Rubric) (`rubric/ingest.md` *stub_markers_present* criterion (weight 0.15) scoring 5 when every deferred section across the batch carries a `<!-- ENRICH: one-sentence description -->` marker at minimum on concurrence reasoning, dissent reasoning, all five Hypothetical Applications, both Critique angles, additional Key Quotations, and Connections; `rubric/enrich.md` *stubs_resolved* criterion (weight 0.22) scoring 5 only when 100 percent of `<!-- ENRICH: -->` markers in three or more in-scope briefs were replaced with substantive prose; vault Connections-stub rule providing that Ingest skeletons must always carry an ENRICH stub in Connections rather than pre-filled wiki-links, added after the *Learning Resources, Inc. v. Trump* skeleton seeded broken links by filling Connections at Ingest and bypassing Expand’s target-existence check).

[^13]: *See infra* App. D (Karpathy-Loop Per-Phase Rubric) (vault prompt-iteration memory in a fixed entry schema (Rule, Why, How to apply, Seen) capped at 60 words and 35 total entries with an out-of-rotation Consolidate sweep; tiered-loading rule loading the lessons file at the start of every content-editing run (Ingest, Enrich, Expand, Synthesize) and skipping it during Lint and Verify unless a phase-verify persona specifically needs it; representative entries including the em-dash typography rule mirroring the Polish-rubric house-style rule at the prompt level, the do-not-invent-case-details rule restating the fabrication-discipline rule, and the Ingest-skeletons-Connections-stub rule added after *Learning Resources, Inc. v. Trump* showed the broken-link failure mode); *Learning Resources, Inc. v. Trump* is cited here as a vault iteration-history artifact rather than for any judicial holding, and the cited lessons entry is the source of the case-name reference. The vault filename convention drops the period after “v” and is normalized to Bluebook “v.” in published prose per L-015.
