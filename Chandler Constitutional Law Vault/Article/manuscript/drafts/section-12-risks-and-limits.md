---
id: "12"
title: "Risks and Limits"
status: needs_cite
target_words: 800
word_count: 878
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
draft_completed_at: 2026-05-23T07:00:00Z
---

# Section XII. Risks and Limits

## 12.A The empirical anchor and the practitioner-side consequence

The strongest publicly available finding for the article’s risk argument is Magesh and colleagues’ 2025 evaluation of leading commercial legal retrieval-augmented-generation systems, which reports that Lexis+ AI, Westlaw AI-Assisted Research, and Ask Practical Law AI hallucinate legal citations between seventeen and thirty-three percent of the time despite the curation that distinguishes those products from consumer chatbots.[CITE: evidence-12-magesh-hallucination-findings] What generalizes to this article is the quantification of hallucination in systems built on the same family of underlying language models the case study uses; what does not transfer is the instrumentation, because the case study has no runtime generation surface for hallucination to occur on. The practitioner-side consequence is *Mata v. Avianca, Inc.*, the Schwartz Rule 11 sanctions order in the Southern District of New York, which records the cost of a no-verify habit when an attorney files six fabricated AI-generated cases.[CITE: evidence-12-mata-v-avianca-rule-11-sanctions] A student who internalizes a no-verify habit through an AI tool will repeat the Schwartz error in practice, and a course knowledge system whose case briefs habituate verification at the source-quotation level is one architectural answer to that pedagogical exposure.

## 12.B The architectural contrast and the discipline that organizes its prose

The article’s risk argument turns on an architectural contrast. A chatbot-tutor architecture generates responses at runtime against a corpus, and the student reads the generated text without prior professorial inspection; the case study is a reviewed static website whose every page was professorially inspected before publication.[CITE: evidence-12-static-vs-chatbot-risk-architecture] The contrast holds along four axes: review timing (build-time versus runtime), error surface (an inspected artifact versus an uninspected response), update mechanism (re-deploy under the review pipeline versus re-generation without it), and accountability surface (a named professor who owns each page versus a system whose outputs no one signed).

The contrast is structural rather than absolute, and the static architecture has its own risk surface. Review scaling is the first feature: a professorial pass over every page is a discipline whose throughput caps the rate at which the corpus can grow. Lost interactivity is the second: a static artifact cannot respond to a question the professor did not anticipate. Structural-pedagogical commitment is the third: the doctrinal map the system encodes is the professor’s commitment, and a student who internalizes it without contesting it forgoes the live Socratic contest. Publication bake-in is the fourth: an error that survives review and ships to the public site is harder to retract than an ephemeral chatbot answer.

The vocabulary of one architecture does not interchange with the vocabulary of the other; the chatbot-tutor architecture answers, responds, generates, and tracks state, while the case study’s architecture publishes, surfaces, indexes, and reviews.[CITE: evidence-12-static-not-chatbot-operational-card]

## 12.C Casebook material and the corpus-completeness question

The forward-looking discipline is that no public-facing page carries verbatim casebook text; the case study works only from professor-prepared slides and notes, public judicial opinions, public constitutional text, statutes, and original hypotheticals.[CITE: evidence-12-copyrighted-casebook-material-risk] The backward-looking audit, whether any pages on the corpus snapshot currently include casebook quotation that must be removed before the site is held up as a model, is a per-page inspection the professor must conduct; this article reports its status as pending professorial review.

The architectural implication of casebook exclusion is the more interesting question. Curriculum-grounded retrieval is a transfer-of-inference the article asserts at the input layer, and the case study’s curriculum-grounded layer is the course-issued layer (lecture decks, professor-prepared opinion PDFs, reading packets, practice exams, teaching guides) rather than the full reading load.[CITE: evidence-12-curriculum-grounding-corpus-incompleteness] The contrast is sharper for that reason: a reviewed static website published from a structured corpus does not retrieve casebook text at runtime, because the work happens at build time against the corpus the professor authored or curated. A future replication on a different course may ingest casebook excerpts under license; the architectural claim here applies to the layer the case study actually operates on.

## 12.D Privacy and the snapshot commitment

The case study’s privacy surface lives at both input and use. On the input side, this article hedges whether any student work (past exam answers, office-hours notes, learning-management-system posts) was used as training input to the vault; the discipline rule is that any system ingesting such work needs FERPA-compliant handling, Institutional Review Board review when appropriate, and consent, anonymization, and retention protocols.[CITE: evidence-12-student-work-as-input-privacy] On the use side, the deployed site’s analytics are configured with Do Not Track respected and session recording disabled, as Section VIII discloses.

The publication snapshot is a separate commitment a reviewer can verify against. The article commits to four anchors: a tagged release on the source repository at the manuscript’s snapshot date, a Wayback Machine capture of the deployed pages on the same date, a canonical-reference commitment to the tagged version rather than to the live deployment, and the posture that continued evolution after the snapshot is the intended state rather than a defect.[CITE: evidence-12-public-site-continuing-experiment-snapshot]

## 12.E Equity, accessibility, and the field-level frame

The deployed site is a JSON-loaded single-page application served from Netlify, presupposing broadband network access and a modern browser. Hash-route navigation, the command-K search palette, and the holding-bar banner block are primary navigation surfaces whose screen-reader behavior is an open testing question. The 300-dpi modernized opinion PDFs assume devices capable of rendering high-resolution image content, and the Canvas enrollment gate restricts the input corpus to currently enrolled students.[CITE: evidence-12-equity-accessibility-cross-section-convergence] The contribution at this altitude is disclosure rather than solution. Bond and colleagues’ 2024 meta-systematic review calls for more methodological and ethical rigor in artificial-intelligence-in-higher-education research, and this article places its risk catalogue inside that field-level self-critique rather than against it.[CITE: evidence-12-bond-aihed-rigor-frame-risks]
