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

The strongest publicly available empirical anchor for this section is the Magesh study, which evaluates three leading commercial legal retrieval-augmented-generation systems (Lexis+ AI, Westlaw AI-Assisted Research, and Ask Practical Law AI) and finds that each hallucinates legal citations at rates between seventeen and thirty-three percent, despite heavy curation. [CITE: evidence-12-magesh-hallucination-findings] What generalizes to the architectural argument here is the demonstration that hallucination in legal AI is real, quantified, and persistent; what does not generalize is the instrumentation, because Magesh inspected three commercial chatbot-style products rather than a reviewed static website. The practitioner-side consequence is documented in *Mata v. Avianca, Inc.*, where Judge Castel imposed Rule 11 sanctions on a lawyer who filed a brief containing six fabricated AI-generated citations. [CITE: evidence-12-mata-v-avianca-rule-11-sanctions] The pedagogical inference is that a student who internalizes a no-verify habit through AI tools will eventually repeat that error in practice; what does not transfer is the litigation posture, because the case study creates no filing surface for unreviewed AI output.

## 12.B The architectural contrast and the discipline that organizes its prose

The article’s reply to the runtime hallucination problem is architectural rather than mitigative. The case study is a reviewed static website on which every page was professorially inspected before publication; the chatbot-tutor alternative, of which Sajja and colleagues’ curriculum-grounded intelligent assistant is the representative case, generates responses at runtime against a corpus, and the student sees the generated text without prior professorial review. [CITE: evidence-12-static-vs-chatbot-risk-architecture] The contrast holds along four axes: review timing (build-time inspection versus runtime generation), error surface (publication of an inspected artifact versus generation of an uninspected response), update mechanism (re-deploy under review versus re-generation without review), and accountability surface (a named professor and author own each published page, where chatbot outputs are signed by no one).

The contrast is structural, not absolute. The reviewed-static-website architecture has its own risk surface, which the section names honestly: review scale (page-by-page inspection scales linearly with vault size and caps growth), lost interactivity (a static page cannot answer a question the professor has not anticipated), structural pedagogical commitment (the doctrinal map encodes the professor’s choices, and a student who internalizes it without contesting it loses the live Socratic contest), and publication bake-in (an error that survives review is harder to retract than an ephemeral chatbot answer). [CITE: evidence-12-static-vs-chatbot-risk-architecture]

A drafting discipline organizes the prose. The chatbot-tutor architecture answers, responds, generates, retrieves, and converses; the reviewed-static-website architecture publishes, surfaces, indexes, links, organizes, and audits. The two vocabularies do not interchange. [CITE: evidence-12-static-not-chatbot-operational-card]

## 12.C Casebook material and the corpus completeness question

The first of four open decisions named here is copyrighted casebook material. The forward-looking discipline rule is that the case study works only from professor-prepared slides and notes, public judicial opinions, public constitutional text, statutes, and original hypotheticals; the backward-looking audit of the existing deployed pages for any residual casebook quotation remains pending professorial review. [CITE: evidence-12-copyrighted-casebook-material-risk] The two halves work together because the input discipline is only as credible as the audit that confirms it across the pages already published.

A related architectural commitment follows. The article elsewhere asserts curriculum-grounded retrieval as a load-bearing transfer-of-inference; if the assigned casebook sits outside the corpus, the claim is structurally incomplete on the input side. The substantive answer is that curriculum-grounding here applies to the course-issued layer (lecture decks, professor-prepared opinion PDFs, merged reading packets, practice exams, teaching guides), and the static architecture does not require runtime retrieval against the casebook to do its work; a future replication on a different course may ingest casebook excerpts under a license that permits it. [CITE: evidence-12-curriculum-grounding-corpus-incompleteness]

## 12.D Privacy and the snapshot commitment

The second open decision is student work as input. If the professor’s past exam answers, office-hours notes, or LMS posts were used as training input, a privacy paragraph would be required at both Section IV and here; if no such material was used, the discipline rule (FERPA-compliant handling, consent, anonymization, separate retention) is named so that any replication on a different course knows the commitment. The parallel use-side surface is the deployed-site analytics configuration disclosed at Section VIII (PostHog, with Do Not Track respected and session recording disabled). [CITE: evidence-12-student-work-as-input-privacy]

The fourth open decision is the public-site-as-evidence-versus-continuing-experiment question. The article commits to four steps: a Git tag at the snapshot date, an archive.org capture of the deployed pages on that date, a canonical-reference commitment to cite the tagged release rather than the live deployment, and an explicit posture that continued evolution of the site is intended rather than an unaddressed drift. [CITE: evidence-12-public-site-continuing-experiment-snapshot]

## 12.E Equity, accessibility, and the field-level frame

The section closes by owning the article’s equity and accessibility argument, which four earlier sections defer here. Five commitments follow: the deployed single-page application presupposes broadband and a modern browser; the hash-route navigation, command-K search, and holding-bar banner remain open testing questions for screen-reader behavior; the 300-dpi modernized PDFs assume sufficient rendering capacity; Canvas gating restricts access by enrollment; and the PostHog analytics configuration is the deployed site’s disclosed equity-and-privacy stance. [CITE: evidence-12-equity-accessibility-cross-section-convergence] Bond and colleagues’ 2024 meta-systematic review of sixty-six AI-in-higher-education publications calls the field to greater ethical and methodological rigor. [CITE: evidence-12-bond-aihed-rigor-frame-risks] What transfers is the field-level commitment to honest disclosure; what does not transfer is the chatbot-tutor and LMS-integration implementation surface Bond’s corpus predominantly covers.
