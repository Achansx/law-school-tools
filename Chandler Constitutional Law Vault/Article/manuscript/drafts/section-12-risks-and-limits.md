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

## 12.A The empirical anchor and the practitioner-side consequence

The strongest publicly available empirical anchor is that even well-curated commercial legal retrieval-augmented-generation systems, the kind built specifically for legal research and grounded against proprietary case-law corpora, hallucinate citations at rates between seventeen and thirty-three percent.[CITE: evidence-12-magesh-hallucination-findings] The article leads the section with that finding because the case study is built on the same family of language models the study evaluated. What generalizes from the finding to this article is the quantified insight that runtime text generation is not reliably hallucination-free even under heavy curation; what does not transfer is the implementation surface, because a reviewed static website has no runtime generation step on which a hallucination can occur. The practitioner-side consequence is not hypothetical: a federal district court imposed Rule 11 sanctions on an attorney who filed a brief containing six fabricated, AI-generated case citations.[CITE: evidence-12-mata-v-avianca-rule-11-sanctions] A student who internalizes a no-verify habit through AI tools will carry it into practice, which is one reason a course knowledge system that builds verification into the publication step matters pedagogically.

## 12.B The architectural contrast and the discipline it demands

The section's organizing move is an architectural contrast rather than a claim that the case study is risk-free. A chatbot-tutor produces output at runtime by generating text against a corpus, and a reader sees that output without prior review; the reviewed static website publishes content at build time after professorial inspection, and a reader sees only pages that were inspected before publication.[CITE: evidence-12-static-vs-chatbot-risk-architecture] The contrast holds at four points: review timing (build-time inspection against runtime generation), error surface (an inspected, citeable page against an ephemeral response regenerated each session), update mechanism (a versioned commit and re-deploy under the same review pipeline against an opaque regeneration under none), and accountability (a named professor who owns each page against a system whose responses no one signed). At each point the static architecture concentrates the risk surface where it can be described, audited, and reviewed. That concentration is not the absence of risk. Four features of the static surface deserve honest naming: review at scale caps how fast the system grows, because every page passing inspection costs reviewer time; a static site cannot address a question the professor did not anticipate; the doctrinal structure the system encodes is itself a pedagogical commitment a student may absorb without contest; and an error that survives review and ships to the public site is harder to retract than an ephemeral response.[CITE: evidence-12-static-vs-chatbot-risk-architecture] The discipline the contrast demands is that the chatbot-tutor architecture's vocabulary stays attached to it: the case study publishes, surfaces, indexes, and displays pages a student reads; it does not answer, respond, or converse.[CITE: evidence-12-static-not-chatbot-operational-card]

## 12.C Casebook material and the corpus-completeness question

Two operational risks sit at the input layer. The first is copyrighted casebook material. The forward-looking discipline is that the public-facing pages work only from professor-prepared slides and notes, public judicial opinions, public constitutional text, statutes, and original hypotheticals, and never reproduce verbatim casebook text.[CITE: evidence-12-copyrighted-casebook-material-risk] Whether any page in the existing corpus snapshot currently includes casebook quotation that would need removal before the site is held up as a model is a backward-looking audit pending professorial review. The second risk is what the casebook's absence from the corpus implies for the article's curriculum-grounding claim. Because the case study's curriculum-grounded retrieval covers the course-issued layer (lectures, indexed opinions, reading packets, and professor-authored hypotheticals) rather than the full assigned reading, the curriculum-grounding claim applies to that layer; the static architecture does not require runtime retrieval against the casebook, because its work happens at build time against the corpus the professor authored, and a future replication on another course could ingest casebook excerpts under a license that permits it.[CITE: evidence-12-curriculum-grounding-corpus-incompleteness]

## 12.D Privacy and the snapshot commitment

Two further commitments concern privacy and the durability of the evidence. On privacy, whether the professor's past exam answers, office-hours notes, or LMS posts were used as training input remains a decision for the professor; the discipline the method names, regardless of how that decision lands here, is that any use of student work as input requires FERPA-compliant handling, consent and anonymization, and Institutional Review Board review where appropriate, and the deployed site's analytics is a separate, use-side privacy surface configured with Do Not Track respected and session recording disabled.[CITE: evidence-12-student-work-as-input-privacy] On durability, because a published article will be read long after the manuscript is fixed while the deployed site keeps evolving, the article commits to a snapshot pair: a tagged release of the source repository at the manuscript's snapshot date, an archive.org capture of the deployed pages at that date, a commitment to cite the tagged version rather than the live site, and an explicit posture that continued evolution after the snapshot is expected rather than disclaimed.[CITE: evidence-12-public-site-continuing-experiment-snapshot]

## 12.E Equity, accessibility, and the field-level frame

The section closes on equity, accessibility, and the field. The case study's contribution at this altitude is disclosure rather than solution: the deployed single-page application presupposes broadband and a modern browser, its hash-route and search-palette navigation leaves screen-reader behavior an open testing question, the 300-dpi modernized PDFs assume a capable rendering device, Canvas enrollment gates the input corpus, and the analytics configuration is the privacy-and-equity stance the site already implements.[CITE: evidence-12-equity-accessibility-cross-section-convergence] A meta-systematic review of sixty-six AI-in-higher-education publications calls the field to greater ethics and rigor; that critique applies to any such system, including a reviewed static website, even though the risk surface this catalogue addresses is the static artifact's own rather than the chatbot-tutor and learning-management-system interventions that review predominantly covers.[CITE: evidence-12-bond-aihed-rigor-frame-risks]
