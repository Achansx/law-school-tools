---
id: "12"
title: "Risks and Limits"
status: needs_cite
target_words: 800
word_count: 830
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

## 12.A The lead anchor: hallucination findings and the practitioner-side consequence

Magesh and colleagues’ 2025 study in the Journal of Empirical Legal Studies (pre-print arXiv:2405.20362) reports that leading commercial legal retrieval-augmented-generation systems, Lexis+ AI, Westlaw AI-Assisted Research, and Ask Practical Law AI, hallucinate citations at rates between seventeen and thirty-three percent.[CITE: evidence-12-magesh-hallucination-findings] The finding is the strongest publicly available empirical anchor for the section because the case study runs on the same family of underlying language models the study evaluates; what generalizes is the quantification of a runtime hallucination surface in well-curated commercial legal systems, and what does not transfer is the implementation surface, because the case study has no runtime generation surface at all. Judge Castel’s Rule 11 sanctions order in Mata v. Avianca, Inc., 678 F. Supp. 3d 443 (S.D.N.Y. 2023), for a brief containing six fabricated AI-generated citations is the one-sentence practitioner-side consequence: hallucination is not hypothetical, and students who internalize a no-verify habit through AI tools will carry that habit into practice.[CITE: evidence-12-mata-v-avianca-rule-11-sanctions]

## 12.B The architectural contrast and the discipline that organizes its prose

The case study is a reviewed static website whose every page passed professorial inspection before publication; the chatbot-tutor alternative, exemplified by Sajja and colleagues’ curriculum-grounded intelligent assistant, generates responses at runtime against a corpus, and the user sees that text without prior review.[CITE: evidence-12-static-vs-chatbot-risk-architecture] The contrast lives along four axes: review timing (build-time inspection versus runtime generation), error surface (stable errors citeable to a specific page versus ephemeral errors re-rolled each session), update mechanism (versioned commits versus opaque retrieval-and-generation), and accountability surface (a named professor versus a system whose outputs no one signed). The contrast does not claim the case study is risk-free; the risk surface differs in kind and lives in different parts of the pipeline, and the case study’s own surface has four features the section names honestly: review-scale (every page passing professorial review caps the rate the system can grow), lost-interactivity (a static site cannot answer a question the professor has not anticipated), structural-pedagogical-commitment (the doctrinal map the system encodes is the professor’s commitment, and a student who internalizes it without contest does not get the live Socratic event), and publication-bake-in (an error that ships to the public site is harder to retract than an ephemeral chatbot answer). The prose discipline holds the chatbot-tutor evaluation vocabulary, response quality, conversational coherence, tutor accuracy, engagement turns, and dialogue-state tracking, to the contrast architecture’s column; the case study publishes, surfaces, indexes, links, displays, exposes, organizes, structures, reviews, and audits, and the two vocabularies do not interchange.[CITE: evidence-12-static-not-chatbot-operational-card]

## 12.C Casebook material and the corpus completeness question

The first of the workplan’s open-decision risks is copyrighted casebook material, and the section names two discipline rules together: the forward-looking rule, that the case study works only from professor-prepared slides and notes, public judicial opinions, public constitutional text, statutes, and original hypotheticals, and the backward-looking audit, that any existing public-facing page currently containing casebook quotation must be removed before the site is held up as a model in this Journal; the audit’s status is pending professorial review.[CITE: evidence-12-copyrighted-casebook-material-risk] The architectural implication of the casebook’s exclusion from the input corpus is that the case study’s curriculum-grounded retrieval applies to the course-issued layer, lecture decks, professor-prepared opinion PDFs, merged reading packets, practice exams, and teaching guides, rather than to the full reading load; the static-versus-chatbot contrast holds sharpest precisely because a reviewed static website published from a structured corpus does not need to ingest the assigned casebook at runtime, and a future replication on a different course may ingest casebook excerpts under license.[CITE: evidence-12-curriculum-grounding-corpus-incompleteness]

## 12.D Privacy and the snapshot commitment

The second open-decision risk is student work as input: whether the professor’s past exam answers, office-hours notes, or learning-management-system posts were used as training input is pending professorial confirmation, and the section names the privacy pattern at both input and use surfaces so a future replication knows the discipline regardless of how this case’s input decision lands; the deployed site’s PostHog analytics, with Do Not Track respected and session recording disabled per the Section VIII record, is the parallel use-side surface.[CITE: evidence-12-student-work-as-input-privacy] The fourth open-decision risk is the public-site-as-evidence-versus-continuing-experiment question, and the section names four concrete snapshot commitments: a Git tag at the manuscript’s snapshot date, an archive.org Wayback Machine capture of the deployed pages at that date, a canonical-reference commitment that the article cites the tagged version rather than the live HEAD, and a continued-evolution-as-intended posture that distinguishes the snapshot the article relies on from the live site’s growth after submission.[CITE: evidence-12-public-site-continuing-experiment-snapshot]

## 12.E Equity, accessibility, and the field-level frame

The equity-and-accessibility argument lives here by routing from four prior Verify ticks on Sections VIII, III, IV, and II, and the section names the single-page application’s bandwidth-and-browser assumption, the hash-route and command-K palette’s open screen-reader-testing question, the 300-dpi modernized PDFs’ rendering-capacity assumption, the Canvas enrollment gate on the input corpus, and the PostHog analytics configuration as the disclosed equity-and-privacy stance.[CITE: evidence-12-equity-accessibility-cross-section-convergence] Bond and colleagues’ meta-systematic review, the field-level frame Section XI deploys for methodological rigor, this section inherits for ethics-and-rigor: the AIHEd call for honest risk disclosure applies to any AI-in-higher-education system, and the risk surface this catalogue addresses is the reviewed-static-artifact’s own, distinct from Bond’s chatbot-tutor and LMS corpus.[CITE: evidence-12-bond-aihed-rigor-frame-risks]
