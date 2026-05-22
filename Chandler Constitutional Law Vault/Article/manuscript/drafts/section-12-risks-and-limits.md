---
id: "12"
title: "Risks and Limits"
status: needs_cite
target_words: 800
word_count: 855
last_phase: draft
draft_status: needs_cite
cite_status: none
polish_status: none
draft_completed_at: 2026-05-23T07:00:00Z
evidence_cards:
  - evidence-12-magesh-hallucination-findings
  - evidence-12-mata-v-avianca-rule-11-sanctions
  - evidence-12-static-vs-chatbot-risk-architecture
  - evidence-12-static-not-chatbot-operational-card
  - evidence-12-copyrighted-casebook-material-risk
  - evidence-12-curriculum-grounding-corpus-incompleteness
  - evidence-12-student-work-as-input-privacy
  - evidence-12-public-site-continuing-experiment-snapshot
  - evidence-12-equity-accessibility-cross-section-convergence
  - evidence-12-bond-aihed-rigor-frame-risks
  - evidence-12-recurring-sentence-not-here
---

# Section XII. Risks and Limits

## 12.A The lead anchor: hallucination findings and the practitioner-side consequence

Magesh and colleagues’ 2025 study reports that three leading commercial legal retrieval-augmented-generation systems (Lexis+ AI, Westlaw AI-Assisted Research, and Ask Practical Law AI) hallucinate citations at rates between seventeen and thirty-three percent of the time, even though those systems are well-curated commercial products built specifically for legal research against proprietary case-law corpora.[CITE: evidence-12-magesh-hallucination-findings] The article’s case study is built on the same family of underlying language models the cited study evaluates, and the hallucination quantification gives this section’s architectural argument its bite: Section XII does not claim that the case study is hallucination-free, only that the architectural choice front-loads detection and remediation before publication, which matters only if hallucination is a real and quantified problem in the source systems on which the case study runs. Mata v. Avianca, Inc., the Rule 11 sanctions order against an attorney who filed six fabricated AI-generated case citations, is the practitioner-side reminder that hallucination is not a hypothetical concern, and a student who internalizes a no-verify habit through AI tools will repeat that error in practice.[CITE: evidence-12-mata-v-avianca-rule-11-sanctions]

## 12.B The architectural contrast and the discipline that organizes its prose

The risk argument turns on an architectural contrast. A chatbot-tutor produces output at runtime by generating text against a corpus, and the user sees that output without prior professorial review; a reviewed static website produces output at build time by professorial authoring and review, and the user sees only content that was inspected before publication. The contrast holds at four points: review timing (build-time inspection versus runtime generation), error surface (an inspected artifact versus an uninspected response), update mechanism (a re-deploy under the same review pipeline versus a re-generation under the same uninspected pipeline), and accountability surface (a named professor and author own each published page, while no one signs the chatbot’s runtime outputs).[CITE: evidence-12-static-vs-chatbot-risk-architecture]

The contrast is structural, not absolute. The static architecture carries its own risk surface. Review scales differently from generation, so a professor who reviews many pages quickly may miss errors a more deliberate review would catch, which caps the rate at which the system can grow. The static artifact cannot adapt to a specific student’s misunderstanding the way a conversational tutor could in principle. The doctrinal map the system encodes is the professor’s commitment, and a student who internalizes the map without contesting it is not getting the live Socratic contest the live class still owns. Publication bakes errors into a public artifact, which raises the cost of correction relative to a chatbot whose answer is ephemeral.[CITE: evidence-12-static-vs-chatbot-risk-architecture]

The prose discipline that organizes this contrast is that the chatbot-tutor evaluation vocabulary (response quality, conversational coherence, tutor accuracy, engagement turns, dialogue-state tracking) appears here as named features of the contrast architecture, not as vocabulary for the case study’s own surface.[CITE: evidence-12-static-not-chatbot-operational-card]

## 12.C Casebook material and the corpus completeness question

Two open questions from the project workplan converge in this section. The first is copyrighted casebook material: none of the public-facing pages should include verbatim casebook text. The forward-looking discipline is that the case study works only from professor-prepared slides and notes, public judicial opinions, public constitutional text, statutes, and original hypotheticals; the backward-looking audit is that any existing pages on the 198-page snapshot containing casebook quotation would need to be removed before the site is held up as a model in this Journal, and the audit’s status is pending professorial review.[CITE: evidence-12-copyrighted-casebook-material-risk]

The architectural implication of the casebook gap matters because the article elsewhere asserts curriculum-grounded retrieval as a load-bearing transfer of inference. The substantive answer Section XII gives is that the case study’s curriculum-grounding claim covers the course-issued layer of slides, lectures, indexed opinions, and professor-authored hypotheticals; the static architecture does not require runtime retrieval against the casebook; and a future replication of the method on a different course may ingest the casebook under license.[CITE: evidence-12-curriculum-grounding-corpus-incompleteness]

## 12.D Privacy and the snapshot commitment

The second open question is the use of student work as input to the vault. If the professor’s past exam answers, office-hours notes, or LMS posts were used as training input, the article carries a separate privacy paragraph; if none of those materials was used, the section says so explicitly. The publication-side analytics surface is a parallel use-side disclosure: the deployed site’s PostHog configuration respects Do Not Track headers and disables session recording, a discipline a future replication should preserve.[CITE: evidence-12-student-work-as-input-privacy]

The third workplan question is the public-site-as-evidence-versus-continuing-experiment posture. Section XII names four operational commitments: a Git tag at the manuscript’s snapshot date, an archive.org capture of the deployed pages at that date, a canonical-reference rule that the article cites the tagged version rather than the live HEAD, and an explicit continued-evolution-as-intended posture distinguishing that snapshot from the site’s continued growth after submission. The publication-side snapshot is the analogue of the input-corpus snapshot at Section IV.E.[CITE: evidence-12-public-site-continuing-experiment-snapshot]

## 12.E Equity, accessibility, and the field-level frame

By routing convention from four prior cross-section forward-references, this section names five concrete equity-and-accessibility commitments: the deployed single-page application carries a bandwidth-and-browser assumption that excludes students on constrained connections or older devices; the hash-route URL structure is an open accessibility question for screen-reader navigation; the 300-dpi modernized PDFs assume a device with sufficient rendering capacity; the Canvas enrollment gate restricts access to currently enrolled students; and the PostHog analytics configuration is the disclosed equity-and-privacy stance the deployed site already implements.[CITE: evidence-12-equity-accessibility-cross-section-convergence] Bond and colleagues’ 2024 meta-systematic review of artificial-intelligence-in-higher-education frames this article’s risk catalogue inside the field’s own ethics-and-rigor self-critique rather than against it.[CITE: evidence-12-bond-aihed-rigor-frame-risks]
