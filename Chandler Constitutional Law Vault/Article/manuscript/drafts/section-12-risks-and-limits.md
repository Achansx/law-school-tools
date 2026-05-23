---
id: "12"
title: "Risks and Limits"
status: needs_cite
target_words: 800
word_count: 978
last_phase: draft
draft_status: needs_cite
draft_completed_at: 2026-05-23T07:00:00Z
flag_for_stitch_trim: true
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

Magesh and colleagues’ 2025 study in the Journal of Empirical Legal Studies, pre-printed as arXiv:2405.20362, evaluates three leading commercial legal retrieval-augmented-generation systems (Lexis+ AI, Westlaw AI-Assisted Research, and Ask Practical Law AI) and reports hallucinated citations between seventeen and thirty-three percent of the time across the three.[CITE: evidence-12-magesh-hallucination-findings] The figure is striking because those systems are not consumer chatbots but well-curated commercial products grounded against proprietary case-law and treatise corpora, and the case study relies on the same underlying language models. The quantification transfers as evidence that production-scale hallucination is real and ineliminable from runtime-generation pipelines; the three-system instrumentation does not, because the case study has no runtime generation surface to measure. Mata v. Avianca, Inc., 678 F. Supp. 3d 443 (S.D.N.Y. 2023), in which Judge Castel imposed Rule 11 sanctions on attorney Steven A. Schwartz for filing six fabricated AI-generated cases, is the practitioner-side companion: a student who internalizes a no-verify habit through any AI tool will repeat the Schwartz error in practice, which is why the architecture described next front-loads verification at publication rather than at runtime.[CITE: evidence-12-mata-v-avianca-rule-11-sanctions]

## 12.B The architectural contrast and the discipline that organizes it

The workplan names a static-site-is-safer-than-chatbot table as this section’s second load-bearing element, and the contrast holds at four axes.[CITE: evidence-12-static-vs-chatbot-risk-architecture] Review timing: the case study inspects every page at build time; the chatbot generates at runtime without prior review. Error surface: case-study errors are stable and citeable to a tagged page, addressable through the pipeline that produced it; chatbot errors are ephemeral and addressable only through corpus or prompt changes that propagate unpredictably. Update mechanism: versioned commits move the case study forward under the same review pipeline; opaque retrieval-and-generation moves the chatbot forward under no comparable review. Accountability: a named professor and author own each published page; a chatbot’s outputs carry no signature any reader can hold accountable.

The reviewed-static-website architecture is not risk-free; it has its own four-feature surface. Review labor scales linearly with vault size and caps growth; a static site cannot answer a question the professor has not anticipated; the doctrinal map the system encodes is the professor’s commitment, and a student who internalizes it without contesting it is not getting the live Socratic contest; and an error that survives review and ships is harder to retract than an ephemeral chatbot answer, which is part of why 12.D names snapshot commitments.

The prose discipline organizing this subsection is that the chatbot-tutor description must remain a description rather than silent vocabulary for the case study’s surface.[CITE: evidence-12-static-not-chatbot-operational-card] The chatbot answers, responds, generates, retrieves, and adapts; the case study publishes, surfaces, indexes, links, and exposes; the two vocabularies do not interchange.

## 12.C Casebook material and the corpus-completeness question

The first open-decision risk is copyrighted casebook material. The forward rule is that the public-facing pages work only from professor-prepared slides and notes, public judicial opinions, public constitutional text, statutes, and original hypotheticals; the backward audit of the 198-page snapshot for any verbatim casebook text remains pending professorial review before the site is held up as a model in this Journal.[CITE: evidence-12-copyrighted-casebook-material-risk] The input-side gap also carries an architectural implication: the article elsewhere asserts curriculum-grounded retrieval as a load-bearing transfer-of-inference, and if the casebook is not in the corpus that claim is structurally incomplete unless the architecture answers the gap.[CITE: evidence-12-curriculum-grounding-corpus-incompleteness] The answer is that curriculum-grounded retrieval here applies to the course-issued layer (lecture decks, professor-prepared opinion PDFs, merged reading packets, practice exams, teaching guides) rather than the full reading load, that the reviewed static architecture does not need to retrieve casebook text at runtime because the work happens at build time against the corpus the professor curated, and that a future replication may ingest casebook excerpts under license without altering this case study’s object.

## 12.D Privacy and the snapshot commitment

The second open-decision risk is student work as input, a privacy pattern at both surfaces. On the input side, whether the professor’s past exam answers, office-hours notes, or LMS posts were used as training input is pending professorial confirmation; if confirmed not used, the section says so explicitly and flags student work as an input the method is capable of using but did not use here and should not use without FERPA-compliant handling, consent and anonymization, and where appropriate Institutional Review Board review.[CITE: evidence-12-student-work-as-input-privacy] On the use side, the deployed site runs PostHog with Do Not Track respected and session recording disabled, as disclosed in Section VIII. The fourth open-decision risk is the public-site-as-evidence-versus-continuing-experiment question, and the section makes four snapshot commitments: a Git tag at the snapshot date; an archive.org Wayback Machine capture of the deployed pages at that date; a canonical-reference commitment that the article cites the tagged version rather than the live HEAD; and a continued-evolution-as-intended posture distinguishing the snapshot from the deployed site’s growth after submission.[CITE: evidence-12-public-site-continuing-experiment-snapshot]

## 12.E Equity, accessibility, and the field-level frame

This section owns the article’s equity-and-accessibility argument by convergence from four prior sections (II, III, IV, and VIII), and names five commitments.[CITE: evidence-12-equity-accessibility-cross-section-convergence] The deployed single-page application presupposes broadband on a modern browser; the hash-route navigation, command-K search palette, and holding-bar banner block are primary navigation surfaces whose screen-reader behavior is an open testing question rather than an asserted WCAG result; the modernized PDFs render at 300 dpi and assume a device capable of high-resolution rendering; the Canvas enrollment gate restricts the input corpus by institutional membership; and the PostHog configuration with Do Not Track respected and session recording disabled is the disclosed privacy stance at the use surface. The contribution here is disclosure rather than solution; a replication can address these assumptions through WCAG testing, alt-text discipline, and screen-reader auditing the case study did not perform. Bond and colleagues’ 2024 meta-systematic review of sixty-six AI-in-higher-education publications, cited at Section XI as the methodological-rigor frame, is also the ethics-and-rigor frame this section inherits; what transfers is the field’s call for honest disclosure and proportional rigor, and what does not is the implementation surface, because Bond’s corpus is predominantly chatbot-tutor and LMS interventions while the artifact here is a reviewed static website with no runtime risk surface of that kind.[CITE: evidence-12-bond-aihed-rigor-frame-risks]
