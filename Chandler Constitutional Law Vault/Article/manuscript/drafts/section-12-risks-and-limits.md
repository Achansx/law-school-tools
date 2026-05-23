---
id: "12"
title: "Risks and Limits"
status: needs_cite
target_words: 800
word_count: 880
last_phase: draft
draft_status: needs_cite
cite_status: none
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

The strongest available empirical anchor for this section is the finding by Magesh and colleagues that leading commercial legal retrieval-augmented-generation systems hallucinate citations between seventeen and thirty-three percent of the time, even though Lexis+ AI, Westlaw AI-Assisted Research, and Ask Practical Law AI are well-curated products grounded against proprietary case-law and treatise corpora.[CITE: evidence-12-magesh-hallucination-findings] The case study uses the same family of underlying language models the evaluation measured. The claim is not that the case study is hallucination-free; it is that the architecture front-loads detection and remediation before publication, a posture that matters only because hallucination is a quantified problem in the source systems. The practitioner-side consequence is documented in Mata v. Avianca, Inc., where Judge Castel imposed Rule 11 sanctions on a lawyer who filed a brief containing six fabricated AI-generated case citations.[CITE: evidence-12-mata-v-avianca-rule-11-sanctions] A student who internalizes a no-verify habit in law school will repeat the Schwartz error in practice; a system that habituates verification at the case-brief level matters pedagogically because the alternative trains the wrong reflex.

## 12.B The architectural contrast and the discipline that organizes its prose

The contrast that organizes the rest of the section runs along four axes. The chatbot-tutor architecture generates responses at runtime against a corpus, and the user sees the text without prior professorial review; the reviewed static website publishes pages whose every line was professorially inspected before publication. The contrast is build-time inspection against runtime generation along the review-timing axis, a stable citeable artifact against an ephemeral re-rolled response along the error-surface axis, a versioned commit against opaque retrieval along the update-mechanism axis, and a named professor and author against a system whose outputs no one signed along the accountability-surface axis.[CITE: evidence-12-static-vs-chatbot-risk-architecture]

The contrast is structural rather than absolute, and naming the case study’s own risk surface is what gives the contrast credibility. Review at scale: each page passing professorial inspection caps the rate at which the system can grow. Lost interactivity: a static site cannot answer a question the professor has not anticipated, a pedagogical loss the chatbot architecture would address differently. Structural pedagogical commitment: the doctrinal map the system encodes is the professor’s commitment, and a student who internalizes the map without contesting it is not getting the live Socratic contest. Publication bake-in: an error that survives review and ships to the public site is harder to retract than an ephemeral chatbot answer.[CITE: evidence-12-static-vs-chatbot-risk-architecture]

Prose discipline organizes this subsection’s vocabulary. The chatbot-tutor architecture answers, responds, generates, retrieves, replies, converses, and adapts; the case study publishes, surfaces, indexes, links, displays, organizes, and reviews. The two vocabularies describe different architectures and do not interchange.[CITE: evidence-12-static-not-chatbot-operational-card]

## 12.C Casebook material and the corpus completeness question

Two of the workplan’s open decisions concern the input corpus’s relationship to copyrighted casebook material. The forward-looking rule is that none of the public-facing pages should include verbatim casebook text, and the case study works only from professor-prepared slides and notes, public judicial opinions, public constitutional text, statutes, and original hypotheticals. The backward-looking audit of the existing deployed pages for any inadvertent casebook quotation remains pending professorial review at the manuscript’s snapshot date.[CITE: evidence-12-copyrighted-casebook-material-risk]

The architectural implication of the casebook’s absence from the corpus is that the curriculum-grounded retrieval claim the article develops elsewhere applies to the course-issued layer (lecture decks, opinion PDFs, reading packets, practice exams, teaching guides) rather than the full reading load. The static-versus-chatbot contrast is sharpest precisely because the case study does not retrieve casebook text in response to a runtime query: the work happens at build time against the curated corpus, and a future replication on a different course may ingest the casebook under license without changing the architectural object.[CITE: evidence-12-curriculum-grounding-corpus-incompleteness]

## 12.D Privacy and the snapshot commitment

The privacy pattern runs along two surfaces. At the input surface, whether the professor’s past exam answers, office-hours notes, or learning-management-system posts were used as training input remains a pending professorial confirmation; the discipline a future replication should follow if it ingests student work is FERPA-compliant handling, Institutional-Review-Board review where appropriate, consent and anonymization protocols, and separate retention rules. At the use surface, the deployed site runs PostHog analytics configured with Do Not Track respected and session recording disabled, as Section VIII’s deployment record describes.[CITE: evidence-12-student-work-as-input-privacy]

The deployed site is a continuing experiment whose pages will keep evolving after submission, and the section commits to four anchors so the manuscript and the artifact stay synchronized: a Git tag at the snapshot date, an archive.org Wayback Machine capture of the deployed pages at that date, a canonical-reference commitment that the article cites the tagged version rather than the live HEAD, and an explicit continued-evolution-as-intended posture that distinguishes the snapshot from the live site’s later growth.[CITE: evidence-12-public-site-continuing-experiment-snapshot]

## 12.E Equity, accessibility, and the field-level frame

The deployed single-page application presupposes a bandwidth-and-browser configuration that excludes students on constrained connections; the hash-route navigation leaves an open question for screen-reader behavior; the high-resolution modernized PDFs assume a device with sufficient rendering capacity; Canvas enrollment gates the input corpus to currently enrolled students; and the PostHog configuration is the deployed site’s disclosed privacy-and-equity posture.[CITE: evidence-12-equity-accessibility-cross-section-convergence] The contribution at this altitude is the disclosure rather than the solution; a replication on a different course can address these assumptions through WCAG conformance testing, alt-text discipline, and screen-reader auditing. Bond and colleagues’ meta-systematic review concludes that the field of artificial intelligence in higher education needs more ethics and rigor; what generalizes from their predominantly chatbot-tutor and learning-management-system corpus to the reviewed static website studied here is the call for honest risk disclosure, not the intervention surface.[CITE: evidence-12-bond-aihed-rigor-frame-risks]
