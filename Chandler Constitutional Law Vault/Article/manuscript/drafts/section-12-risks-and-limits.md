---
id: "12"
title: "Risks and Limits"
status: needs_cite
target_words: 800
word_count: 815
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

Magesh and colleagues’ 2025 study in the Journal of Empirical Legal Studies reports that three leading commercial legal retrieval-augmented-generation systems (Lexis+ AI, Westlaw AI-Assisted Research, and Ask Practical Law AI) hallucinate citations at rates between seventeen and thirty-three percent, despite being curated products grounded against proprietary corpora.[CITE: evidence-12-magesh-hallucination-findings] The article does not claim the case study is hallucination-free; it claims the architectural choice front-loads detection and remediation before publication, a coherent response only if the underlying technology poses a quantified problem in systems built on the same family of models. What generalizes from Magesh is the anchor that runtime generation against legal corpora hallucinates at rates incompatible with responsible practice; what does not transfer is the evaluation methodology, because a reviewed static website has no runtime generation surface. Mata v. Avianca, Inc. is the one-sentence reminder that the practitioner-side cost of a no-verify habit is documented and sanctionable, and the pedagogical implication follows: students who internalize that habit through their AI tools will repeat the Schwartz error in practice.[CITE: evidence-12-mata-v-avianca-rule-11-sanctions]

## 12.B The architectural contrast and the discipline that organizes its prose

The risk profile of the case study differs structurally from the chatbot-tutor alternative along four points. On review timing, the case study publishes pages a professor inspected at build time; the chatbot-tutor architecture generates responses at runtime without prior review. On error surface, the case study exposes errors that are stable and citeable to a specific page; the chatbot-tutor architecture exposes errors that are ephemeral. On update mechanism, the case study redeploys under the same review pipeline; the chatbot-tutor architecture re-generates under the same uninspected pipeline. On accountability, a named professor and author own each published page; the chatbot-tutor architecture distributes responsibility across user interactions in ways difficult to audit.[CITE: evidence-12-static-vs-chatbot-risk-architecture] The contrast is not that the case study is risk-free; it is that the risk surface is different in kind. The case study’s own surface has four features: review at scale caps the rate the system can grow; lost interactivity means the static artifact cannot address an unanticipated question; the doctrinal map encodes the professor’s choices, and a student who absorbs it without contesting it loses the live Socratic contest; and publication bake-in raises the cost of correcting errors relative to an ephemeral answer.[CITE: evidence-12-static-vs-chatbot-risk-architecture] The prose discipline this subsection follows is that the verbs naming what the chatbot-tutor architecture does (answers, responds, generates, retrieves, replies, converses) do not slip into the verbs used for the case study’s static artifact, which publishes, indexes, links, surfaces, and organizes pages that a student reads.[CITE: evidence-12-static-not-chatbot-operational-card]

## 12.C Casebook material and the corpus completeness question

The first workplan open-decision risk is copyrighted casebook material. The forward-looking rule is that the public-facing pages work only from professor-prepared slides and notes, public judicial opinions, public constitutional text, statutes, and original hypotheticals, and the corpus in Section IV is composed entirely of those materials. The backward-looking audit of whether any current pages include casebook quotation that would need removal is a per-page inspection pending the professor’s confirmation; the article hedges that status here and records the result once it lands.[CITE: evidence-12-copyrighted-casebook-material-risk] The corpus-completeness implication Section IV.A defers to this section is that Sections V and VIII assert curriculum-grounded retrieval as a load-bearing transfer-of-inference, and if the casebook is not in the corpus, that claim covers only the course-issued layer rather than the full reading load. The architectural answer is that the static-versus-chatbot contrast is sharpest precisely because a reviewed static website does not retrieve casebook text at runtime: the work happens at build time against the curated corpus, and a future replication may ingest casebook excerpts under license without changing the conclusion.[CITE: evidence-12-curriculum-grounding-corpus-incompleteness]

## 12.D Privacy and the snapshot commitment

The second workplan open-decision risk is student work as input. If the professor’s exam answers, office-hours notes, or learning-management-system posts were used as training input, the article carries a separate privacy paragraph naming FERPA-compliant handling, IRB review, and consent and anonymization protocols; if none was used, the article says so explicitly, and the discipline applies as the standard a future replication must meet.[CITE: evidence-12-student-work-as-input-privacy] The deployed site’s analytics surface is the parallel use-side commitment, with Do Not Track respected and session recording disabled per Section VIII. The fourth workplan open-decision risk is the public-site-as-evidence-versus-continuing-experiment question, and the section makes four commitments: tag the source repository at the snapshot date, capture the deployed site at that date through the archive.org Wayback Machine, treat the pair as canonical reference for every quantitative or structural claim, and name continued evolution after that date as the expected posture rather than a constraint.[CITE: evidence-12-public-site-continuing-experiment-snapshot]

## 12.E Equity, accessibility, and the field-level frame

The deployed single-page application presupposes broadband and a modern browser and inherits Netlify’s default accessibility characteristics rather than meeting a specific WCAG level; the hash-route navigation and command-K palette raise untested screen-reader and keyboard questions; the 300-dpi modernized PDFs assume a device capable of high-resolution rendering; Canvas access presupposes institutional enrollment, partially mitigated by the public prose layer; the PostHog configuration respects privacy by design but inherits residual infrastructure exposure. The contribution here is disclosure, not solution, and a replication can address the assumptions with conformance testing this case study did not undertake.[CITE: evidence-12-equity-accessibility-cross-section-convergence] Bond and colleagues’ 2024 meta-review of sixty-six artificial-intelligence-in-higher-education publications calls for greater ethical and methodological rigor across the field, and the section closes by placing the article inside that self-critique: what generalizes is the rigor commitment any system must meet, and what does not transfer is the chatbot-tutor and learning-management-system intervention surface that corpus covers.[CITE: evidence-12-bond-aihed-rigor-frame-risks]
