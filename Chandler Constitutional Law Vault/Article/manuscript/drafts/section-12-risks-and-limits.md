---
id: "12"
title: "Risks and Limits"
status: needs_cite
target_words: 800
word_count: 849
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

Magesh and colleagues evaluated three leading commercial legal retrieval-augmented-generation systems (Lexis+ AI, Westlaw AI-Assisted Research, and Ask Practical Law AI) and reported that each hallucinated legal citations at rates between seventeen and thirty-three percent.[CITE: evidence-12-magesh-hallucination-findings] The finding is the strongest publicly available empirical anchor for this article’s risk argument, because the three evaluated products are well-curated commercial tools built specifically for legal research rather than consumer chatbots, and the high rate persists despite that curation. What generalizes from the cited evaluation to this article’s setting is the quantification of runtime hallucination as a real and measurable phenomenon in legal-language-model output; what does not transfer is the implementation surface, because a reviewed static website has no runtime generation surface for that hallucination to occur on. The practitioner-side consequence is documented in Mata v. Avianca, Inc., the Rule 11 sanctions order against an attorney who filed six fabricated AI-generated cases.[CITE: evidence-12-mata-v-avianca-rule-11-sanctions] A student who internalizes a no-verify habit through AI tools in law school will repeat the Schwartz error once she reaches practice.

## 12.B The architectural contrast and the discipline that organizes its prose

The case study is a reviewed static website on which every page was professorially inspected before publication; the chatbot-tutor alternative generates responses at runtime against a corpus, and the user sees the generated text without prior professorial review. The contrast holds along four axes: review timing (build-time inspection versus runtime generation), error surface (an inspected artifact versus an uninspected response), update mechanism (a versioned re-deploy under the same review pipeline versus a re-generation under the same uninspected pipeline), and accountability surface (a named professor and author own each published page versus the system itself appearing to own each response).[CITE: evidence-12-static-vs-chatbot-risk-architecture] At each axis the static architecture concentrates the risk surface where the article can describe and audit it; the chatbot architecture distributes that surface across every user interaction.

The contrast is not a claim that the case study is risk-free. The reviewed-static-website architecture has its own four-feature surface: review at scale grows linearly with vault size and caps the rate at which the system can responsibly expand; the published page is limited to what its author anticipated, a pedagogical loss the chatbot architecture would handle differently; the doctrinal map the system encodes is the professor’s commitment, and a student who internalizes it uncritically loses some of the live Socratic contest; and publication bakes errors into a public artifact harder to retract than an ephemeral chatbot answer.[CITE: evidence-12-static-vs-chatbot-risk-architecture]

The prose discipline that supports the contrast is that the description of the chatbot-tutor architecture must remain a description rather than silently importing that architecture’s verbs into the case study’s surface: the chatbot architecture answers, responds, and adapts, while the case study publishes, indexes, and links.[CITE: evidence-12-static-not-chatbot-operational-card]

## 12.C Casebook material and the corpus completeness question

The first of the workplan’s open-decision risks is copyrighted casebook material. The forward-looking discipline rule is that the case study works only from professor-prepared slides and notes, public judicial opinions, public constitutional text, statutes, and original hypotheticals, and that none of the public-facing pages includes verbatim casebook text. The backward-looking audit of the existing pages for casebook quotation that would need to be removed before the site is held up as a model in this Journal is pending professorial review at the time of submission.[CITE: evidence-12-copyrighted-casebook-material-risk]

The architectural implication is that the article’s curriculum-grounded retrieval claim covers the course-issued layer (lecture decks, professor-prepared opinion PDFs, merged reading packets, practice exams, teaching guides) rather than the full reading load. The static architecture does not require runtime retrieval against the casebook, because the work happens at build time against the corpus the professor has authored or curated; a future replication of the method on a different course may ingest casebook excerpts under a license that permits it.[CITE: evidence-12-curriculum-grounding-corpus-incompleteness]

## 12.D Privacy and the snapshot commitment

The second open-decision risk is student work as input. Whether the professor’s past exam answers, office-hours notes, or learning-management-system posts were used as training input to the vault is an input-side privacy question pending professorial confirmation, and the deployed site’s PostHog analytics, configured to respect Do Not Track and to disable session recording, is the parallel use-side privacy surface this article already discloses.[CITE: evidence-12-student-work-as-input-privacy]

The fourth open-decision risk is the snapshot question. Because the deployed site continues to evolve after submission, the article commits to a Git tag at the manuscript’s snapshot date, an archive.org capture of the deployed pages at that date, a canonical-reference posture in which the article cites the tagged version rather than the live HEAD, and an explicit acknowledgment that continued evolution after the snapshot is the intended posture rather than a defect.[CITE: evidence-12-public-site-continuing-experiment-snapshot]

## 12.E Equity, accessibility, and the field-level frame

The deployed single-page application presupposes broadband access and a modern browser; its hash-route navigation carries open screen-reader testing questions; the modernized opinion PDFs rendered at three-hundred-dpi assume a device with rendering capacity many readers have but not all do; Canvas enrollment gates the input corpus to currently enrolled students; and the PostHog configuration described above is the disclosed equity-and-privacy posture the deployed site implements.[CITE: evidence-12-equity-accessibility-cross-section-convergence] Bond and colleagues’ meta-systematic review of sixty-six artificial-intelligence-in-higher-education publications calls for ethical and methodological rigor across the field; this article’s risk catalogue takes up that call for a reviewed-static-artifact intervention whose surface differs from the chatbot-tutor and learning-management-system corpus the cited meta-review predominantly covers.[CITE: evidence-12-bond-aihed-rigor-frame-risks]
