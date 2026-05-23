---
id: "12"
title: "Risks and Limits"
status: needs_cite
target_words: 800
word_count: 0
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

The section’s lead empirical anchor is Magesh and colleagues’ 2025 study in the Journal of Empirical Legal Studies, which evaluates three leading commercial legal retrieval-augmented-generation systems (Lexis+ AI, Westlaw AI-Assisted Research, and Ask Practical Law AI) and finds that each hallucinates legal citations at rates between seventeen and thirty-three percent.[CITE: evidence-12-magesh-hallucination-findings] The case study uses the same family of language models, and the architectural argument below is intelligible only against that quantified problem. Section XII does not claim the case study is hallucination-free; it claims the architecture front-loads detection and remediation before publication, which only matters if hallucination is a real and measured problem.

The practitioner-side consequence anchor is Mata v. Avianca, Inc., the 2023 S.D.N.Y. opinion imposing Rule 11 sanctions for filing six fabricated AI-generated cases.[CITE: evidence-12-mata-v-avianca-rule-11-sanctions] A student who internalizes a no-verify habit through AI tools will repeat the Schwartz error in practice; the case study’s architecture is built to prevent that habit at the publication step rather than the inference step.

## 12.B The architectural contrast and the discipline that organizes its prose

The case study is a reviewed static website where every page was professorially inspected before publication; the chatbot-tutor alternative generates responses at runtime against a corpus and presents them without prior professorial review.[CITE: evidence-12-static-vs-chatbot-risk-architecture] The contrast runs along four axes: review timing (publication-time professorial pass versus runtime generation), error surface (errors stable and citeable to a specific page versus ephemeral and re-rolled each session), update mechanism (versioned commits versus opaque retrieval-and-generation), and accountability surface (a named professor versus a system whose outputs no one signed).

The contrast does not claim that the case study is risk-free. The case study’s own risk surface carries four named features: review-scale (the discipline scales linearly with vault size and caps growth rate), lost-interactivity (a static site cannot answer a question the professor has not anticipated), structural-pedagogical-commitment (a student who internalizes the encoded doctrinal map without contesting it is not getting the live Socratic contest), and publication-bake-in (an error that survives review and ships to the public site is harder to retract than an ephemeral chatbot answer).[CITE: evidence-12-static-vs-chatbot-risk-architecture] Naming those risks honestly is what gives the contrast credibility under a skeptical reading.

The subsection’s discipline is that the description of the chatbot-tutor contrast remains a description rather than silently importing its vocabulary into the case study’s own surface.[CITE: evidence-12-static-not-chatbot-operational-card] Response quality, conversational coherence, tutor accuracy, engagement turns, and dialogue-state tracking appear as named features of the contrast architecture, not as silent vocabulary for the case study’s risk surface.

## 12.C Casebook material and the corpus completeness question

The first open-decision risk is copyrighted casebook material. The forward-looking discipline rule is that the case study works only from professor-prepared slides and notes, public judicial opinions, public constitutional text, statutes, and original hypotheticals; no public-facing page may include verbatim casebook text.[CITE: evidence-12-copyrighted-casebook-material-risk] The backward-looking audit of the existing 198-page snapshot for any casebook quotation that would need to be removed is pending professorial review, and the article does not assert either presence or absence of casebook quotation until that audit closes.

Sections V and VIII assert curriculum-grounded retrieval as a load-bearing transfer-of-inference, but if the casebook is not in the corpus the curriculum-grounding architectural claim is structurally incomplete on the input side.[CITE: evidence-12-curriculum-grounding-corpus-incompleteness] The architectural answer is that the case study’s curriculum-grounding claim covers the course-issued layer of slides, lectures, indexed opinions, and professor-authored hypotheticals; the static architecture requires no runtime retrieval against the casebook, and a future replication on a different course may ingest the casebook under license.

## 12.D Privacy and the snapshot commitment

The second open-decision risk is student work as input. If past exam answers, office-hours notes, or LMS posts were used as input, the article includes a separate privacy paragraph naming the discipline rules; if none was used, Section XII says so explicitly.[CITE: evidence-12-student-work-as-input-privacy] The publication-side analytics surface is the parallel use-side commitment: the deployed site’s PostHog configuration respects Do-Not-Track signals and disables session recording, disclosed in Section VIII.

The fourth open-decision risk is the public-site-as-evidence-versus-continuing-experiment question. The section names four concrete snapshot commitments: a Git tag at the manuscript’s snapshot date, an archive.org capture at that date, a canonical-reference rule that the article cites the tagged version rather than the live HEAD, and an explicit continued-evolution-as-intended posture distinguishing the snapshot from later growth.[CITE: evidence-12-public-site-continuing-experiment-snapshot] The publication-side snapshot is the publication-altitude analogue of Section IV.E’s input-corpus snapshot, and a JLE reviewer can verify the manuscript against a specific tagged release rather than chasing a moving deployed site.

## 12.E Equity, accessibility, and the field-level frame

Section XII owns the article’s equity-and-accessibility argument by routing convention from prior Verify findings on Sections VIII, III, IV, and II, and names five commitments: the deployed single-page-application carries a bandwidth-and-browser assumption that excludes students on constrained connections or older devices; the hash-route URL structure is an open accessibility question for screen-reader navigation; the 300-dpi modernized PDF assumes a device with sufficient rendering capacity; the Canvas enrollment gate restricts access to currently enrolled students; and the PostHog Do-Not-Track-respected analytics configuration is the disclosed equity-and-privacy stance.[CITE: evidence-12-equity-accessibility-cross-section-convergence] The closing frame is Bond and colleagues’ 2024 meta-systematic review of sixty-six artificial-intelligence-in-higher-education publications, deployed at the ethics-and-rigor altitude distinct from Section XI’s methodological-rigor altitude.[CITE: evidence-12-bond-aihed-rigor-frame-risks] What transfers is the meta-review’s ethics-and-rigor critique of any AI-in-higher-education system, including reviewed static websites; what does not transfer is the chatbot-tutor and LMS-integration implementation surface Bond’s corpus predominantly covers. The closing posture places the article inside the field’s own self-critique rather than against it.
