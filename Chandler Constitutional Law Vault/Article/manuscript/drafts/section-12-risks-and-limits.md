---
id: "12"
title: "Risks and Limits"
status: needs_cite
target_words: 800
word_count: 879
last_phase: draft
draft_status: needs_cite
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

## 12.A The empirical anchor and the practitioner consequence

A risk catalogue for this project has to begin with the empirical record. Magesh and colleagues report that the leading commercial legal research tools, Lexis+ AI, Westlaw AI-Assisted Research, and Ask Practical Law AI, hallucinate citations between seventeen and thirty-three percent of the time, though each is a well-curated retrieval system built for legal work.[CITE: evidence-12-magesh-hallucination-findings] What generalizes is that runtime generation against a curated legal corpus does not eliminate hallucination; what does not transfer is the evaluation instrumentation, because a reviewed static website has no runtime generation surface for hallucination to occur on. The article does not claim the case study is error-free, only that the architecture front-loads detection and correction before any page ships. The consequence is sanctionable: in *Mata v. Avianca*, a federal court imposed Rule 11 sanctions on an attorney who filed a brief containing six fabricated cases a chatbot generated, which carries forward that the verification habit matters in practice, not only in the classroom, though the case study creates no comparable exposure.[CITE: evidence-12-mata-v-avianca-rule-11-sanctions] A student who internalizes a no-verify habit through an AI tool will repeat it in practice, which is why the architecture habituates verification at the publication step.

## 12.B The architectural contrast and the discipline that organizes it

The workplan calls for a static-site-is-safer-than-chatbot comparison, and the contrast holds along four axes.[CITE: evidence-12-static-vs-chatbot-risk-architecture] A chatbot tutor generates a response at runtime and the reader sees that text without prior review; the case study publishes pages a professor inspected first. Review timing sets build-time professorial inspection against runtime generation with no human in the loop. Error surface sets an inspected artifact, whose errors are stable and citeable, against responses whose errors are ephemeral and re-rolled each session. Update mechanism sets versioned Git commits against opaque retrieval and generation. Accountability sets a named professor who owns each published page against a system whose responses no one signed.

The contrast is structural rather than absolute, and the static architecture carries its own risks. Review scales differently from generation, so inspecting every page caps how fast the corpus can grow. A published page cannot anticipate a question the professor did not foresee, a loss of interactivity a conversational architecture handles differently. The doctrinal map the pages encode is the professor’s commitment, and a student who absorbs it without contesting it forgoes the live Socratic contest. An error that survives review and ships is harder to retract than an ephemeral response. Throughout, the section keeps each architecture in its own vocabulary: the contrast architecture generates, retrieves, and converses, while the case study publishes, surfaces, indexes, and displays.

## 12.C Casebook material and the corpus-completeness question

The first of the workplan’s open decisions for the professor is copyrighted casebook material, and the section pairs a forward rule with a backward audit. The forward rule is a structural commitment: the public pages work only from professor-prepared slides and notes, public judicial opinions, public constitutional text, statutes, and original hypotheticals, none of which is casebook prose.[CITE: evidence-12-copyrighted-casebook-material-risk] The backward audit, whether any existing page on the snapshot corpus quotes casebook text that would need removal before the site is held up as a model, remains pending professorial review, and if it finds quotation the remediation is removal. A related implication falls on the input side: the article asserts curriculum-grounded retrieval as a load-bearing claim, yet if the casebook is not in the corpus that claim is incomplete.[CITE: evidence-12-curriculum-grounding-corpus-incompleteness] The architectural answer is that the case study’s curriculum grounding covers the course-issued layer, not the full reading load, and the static architecture needs no runtime retrieval against the casebook; a future course could ingest casebook excerpts under license.

## 12.D Privacy and the snapshot commitment

The second open decision is student work as input. If past exam answers, office-hours notes, or learning-management posts were used to build the vault, the article owes a separate privacy paragraph; if none was, the section says so and names the discipline a replication would need: FERPA-compliant handling, Institutional Review Board review, consent, and anonymization.[CITE: evidence-12-student-work-as-input-privacy] The use side is a parallel surface: the deployed site’s analytics run with Do Not Track respected and session recording disabled, as Section VIII discloses. The fourth open decision is the public site as evidence against continuing experiment, and the section commits to four safeguards: a Git tag at the snapshot date, an archive.org capture of the deployed pages, a canonical-reference rule that cites the tagged version rather than the live deployment, and an explicit posture that continued evolution after submission is intended.[CITE: evidence-12-public-site-continuing-experiment-snapshot] These let a reviewer verify the manuscript against a fixed release.

## 12.E Equity, accessibility, and the field-level frame

The section owns the article’s equity-and-accessibility argument, and its contribution is disclosure rather than solution. The deployed single-page application assumes broadband and a modern browser; the hash-route navigation leaves screen-reader behavior an open question; the modernized 300-dpi PDFs assume a capable rendering device; the Canvas enrollment gate restricts the input corpus to enrolled students; and the analytics configuration is the disclosed privacy-and-equity stance.[CITE: evidence-12-equity-accessibility-cross-section-convergence] A replication could close these with conformance testing and screen-reader auditing the case study did not perform. Bond and colleagues’ meta-review of sixty-six higher-education studies calls the field to greater ethics and rigor.[CITE: evidence-12-bond-aihed-rigor-frame-risks] What transfers is that critique, which applies to any artificial-intelligence system in higher education including a reviewed static website; what does not is the chatbot-tutor and learning-management corpus the review predominantly covers, a surface this catalogue does not occupy. The honest posture sits inside that self-critique rather than against it.
