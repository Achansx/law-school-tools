---
id: "12"
title: "Risks and Limits"
status: needs_cite
target_words: 800
word_count: 877
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

## 12.A The lead anchor: hallucination findings and the practitioner-side consequence

The article’s risk argument opens with an empirical anchor. Magesh and colleagues report that leading commercial legal retrieval-augmented-generation systems, including Lexis+ AI, Westlaw AI-Assisted Research, and Ask Practical Law AI, hallucinate citations at rates between seventeen and thirty-three percent, even though each is a well-curated commercial product grounded against proprietary case-law corpora.[CITE: evidence-12-magesh-hallucination-findings] The abstract risk insight transfers to any architecture whose generation surface produces text without prior human review; the specific three-system evaluation methodology does not transfer to a reviewed static website, which has no runtime generation surface for the measured hallucination to occur on. The case study is built on the same family of underlying language models the study evaluated.

Mata v. Avianca, Inc. is the practitioner-side consequence: Rule 11 sanctions for filing six fabricated AI-generated cases are the reminder that hallucination is not hypothetical, and a student who internalizes a no-verify habit through an AI tool will repeat the same error once in practice.[CITE: evidence-12-mata-v-avianca-rule-11-sanctions]

## 12.B The architectural contrast and the discipline that organizes its prose

The architectural contrast holds at four points.[CITE: evidence-12-static-vs-chatbot-risk-architecture] Review timing differs: a chatbot-tutor generates a response at runtime, and the user sees that text without prior professorial inspection, while the reviewed static website publishes pages inspected at build time. Error surface differs: a chatbot error is ephemeral and re-rolled on each session, while a published page is stable, addressable, and revisable through a versioned commit. Update mechanism differs: chatbot output regenerates under an uninspected pipeline, while the website redeploys under the same review pipeline that produced each page. Accountability surface differs: chatbot outputs are signed by no one in particular, while each page of the case study is signed by the professor and the author. The architectural insight transfers across reviewed-static implementations; the specific risk mapping is particular to this case study’s corpus and artifact.

The contrast does not claim that the case study is risk-free; the static architecture concentrates its risk surface in different places. Review scales linearly with vault size, capping how fast the system can grow. A static page cannot adapt to a student’s confusion in real time, so the architecture trades interactivity for the review it gains. The doctrinal structure the case study encodes is the professor’s commitment, and a student who internalizes it uncritically loses the live Socratic contest. Publication bakes errors into a public artifact and raises the cost of correction.[CITE: evidence-12-static-vs-chatbot-risk-architecture]

The section’s prose discipline is that describing the chatbot-tutor architecture stays a description of the contrast architecture and does not import that architecture’s vocabulary into the case study’s surface. The chatbot-tutor architecture answers, responds, generates, retrieves, and converses; the case study publishes, surfaces, indexes, links, and displays.[CITE: evidence-12-static-not-chatbot-operational-card]

## 12.C Casebook material and the corpus completeness question

Workplan §6 names six open decisions; this section takes up four. The first is copyrighted casebook material. The forward-looking rule is that the case study works only from professor-prepared slides and notes, public judicial opinions, public constitutional text, statutes, and original hypotheticals; the backward-looking audit of whether any existing page currently includes casebook quotation that would need to be removed before the site is held up as a model in this Journal remains pending professorial review, and this section reports the rule and the audit status together rather than as separate disclosures.[CITE: evidence-12-copyrighted-casebook-material-risk]

The architectural implication of the casebook exclusion is that the curriculum-grounding claim the article asserts elsewhere applies to the course-issued layer (lecture decks, professor-prepared opinion PDFs, merged reading packets, practice exams, and teaching guides) rather than to the full reading load. A reviewed static website published from a structured corpus does not retrieve the assigned casebook at runtime; a future replication of the method on a different course may ingest casebook excerpts under a license.[CITE: evidence-12-curriculum-grounding-corpus-incompleteness]

## 12.D Privacy and the snapshot commitment

The second open decision is student work as input. If the professor’s past exam answers, office-hours notes, or learning-management-system posts were used as training input, a separate privacy paragraph would land here; if none was used, the section so reports. Either resolution carries a privacy commitment at both surfaces: the input surface, for any future replication that ingests student materials (Family Educational Rights and Privacy Act compliance, Institutional Review Board review where appropriate, consent and anonymization); and the use surface, where the deployed site configures PostHog with Do Not Track respected and session recording disabled.[CITE: evidence-12-student-work-as-input-privacy]

The fourth open decision is the public-site-versus-continuing-experiment question. The section commits to four anchors: a Git tag at the snapshot date, an Internet Archive Wayback Machine capture of the deployed pages on that date, a canonical-reference commitment that the article cites the tagged version rather than the live deployment, and a continued-evolution posture distinguishing the snapshot from the live site’s growth.[CITE: evidence-12-public-site-continuing-experiment-snapshot]

## 12.E Equity, accessibility, and the field-level frame

Four upstream sections defer their equity-and-accessibility argument here. The deployed single-page application presupposes broadband access and a modern browser; hash-route navigation and the command palette leave screen-reader behavior as an open question; the modernized PDFs assume a device with sufficient rendering capacity; Canvas access presupposes institutional enrollment; PostHog inherits whatever residual exposure that infrastructure carries. The contribution here is disclosure rather than solution; a replication can address each item through Web Content Accessibility Guidelines conformance testing, alternative-text discipline, and screen-reader auditing.[CITE: evidence-12-equity-accessibility-cross-section-convergence]

Bond and colleagues provide the field-level ethics-and-rigor frame, reused from Section XI’s methodological-rigor deployment. Their meta-review covers sixty-six predominantly chatbot-tutor and learning-management-system interventions, so the critique applies to any artificial-intelligence-in-higher-education system including reviewed static websites; the risk surface catalogued above is the reviewed-static-artifact’s own.[CITE: evidence-12-bond-aihed-rigor-frame-risks]
