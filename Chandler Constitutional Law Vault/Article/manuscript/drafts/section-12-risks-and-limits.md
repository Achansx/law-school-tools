---
id: "12"
title: "Risks and Limits"
status: needs_cite
target_words: 800
word_count: 876
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

The strongest publicly available empirical anchor for the article’s risk argument leads the section. Magesh and colleagues report that three leading commercial legal retrieval-augmented-generation systems (Lexis+ AI, Westlaw AI-Assisted Research, and Ask Practical Law AI) hallucinate citations at rates between seventeen and thirty-three percent, despite each system being curated for legal research and grounded against proprietary corpora.[CITE: Magesh et al. 2025, J. Empirical Legal Studies, https://onlinelibrary.wiley.com/doi/full/10.1111/jels.12413, pre-print arXiv:2405.20362; per L-022 and L-043 verify both candidate paths via WebSearch and prefer the published-journal URL when both resolve; per L-024 add a transfer-of-inference clause naming that the hallucination rate generalizes to chatbot-tutor architectures with runtime generation and does not transfer to a reviewed static website with no runtime generation surface] The anchor matters because Section XII does not claim the case study is hallucination-free; it claims that the architectural choice front-loads detection and remediation at build time, and that asymmetry only carries weight if runtime hallucination in those source systems is real and quantified. The practitioner-side consequence is documented and sanctionable: Mata v. Avianca remains the canonical reminder that fabricated AI-generated citations carry Rule 11 cost in federal court, and a course knowledge system that habituates citation verification at the case-brief level is one architectural response to that habit migration.[CITE: Mata v. Avianca, Inc., 678 F. Supp. 3d 443 (S.D.N.Y. 2023) (Castel, J.); per L-019 verify against a primary reporter and per L-004 check Midpage analyzeOpinion only if the opinion is quoted in body prose; per L-010 the citation lands as a one-sentence reminder rather than as a retold story; per L-024 the transfer-of-inference clause names the abstract pedagogical insight that generalizes (verification habits trained in school migrate to practice) and the specific posture that does not (a sanctioned federal-district-court filing is one realization of the underlying risk, not a claim that this case study creates the same risk)]

## 12.B The architectural contrast and the discipline that organizes its prose

The architectural contrast operates along four axes. Review timing distinguishes a chatbot-tutor system that generates a response at runtime from a reviewed static website whose every page was professorially inspected before publication. Error surface distinguishes a system whose mistakes are ephemeral and re-rolled each session from a system whose mistakes ship as a stable, addressable page. Update mechanism distinguishes opaque retrieval-and-generation against a corpus from versioned commits to a Git repository under the same review pipeline. Accountability surface distinguishes a system whose outputs no individual signed from a published page whose author and reviewing professor are named.[CITE: Sajja et al. 2023, 20 Int'l J. Educ. Tech. Higher Educ. art. 42, cross-section reuse via Section VIII note 15 per L-034 with original URL-liveness verification recorded at the Section VIII Cite tick; per L-024 the transfer-of-inference clause at this section names the abstract architectural insight that generalizes (review timing and error surface differ structurally between architectures) and the specific risk-catalogue mapping that does not transfer (this case study's particular artifact and corpus)]

The static-website architecture has its own risk surface, enumerated here in four named features. Review at scale is a discipline that scales linearly with vault size and caps the rate at which the system can grow. Lost interactivity is a real pedagogical loss, because a static page cannot answer a question the professor has not anticipated. Structural pedagogical commitment is the doctrinal map the system encodes as the professor’s commitment, one students need to contest in live class rather than internalize from the page alone. Publication bake-in raises the cost of correcting an error that survives review and ships to the public site relative to an ephemeral answer.

A prose discipline organizes the section’s vocabulary. The chatbot-tutor architecture answers, generates, retrieves, and adapts; the case study’s architecture publishes, indexes, links, organizes, and reviews. The two vocabularies do not interchange.

## 12.C Casebook material and the corpus completeness question

The first of the workplan’s open-decision risks is copyrighted casebook material. The forward-looking discipline rule is that no public-facing page includes verbatim casebook text; the deployed pages work only from the professor’s own slides and notes, public judicial opinions, public constitutional text, statutes, and original hypotheticals. The backward-looking audit of whether any existing page on the corpus snapshot currently includes casebook quotation that would need to be removed before the site is held up as a model is pending professorial review.[CITE: forward reference to App. A (Article Project Architecture) (Workplan §6.1 Open-Decision Protocol subsection); see same-section open-issues footnote tracking the backward audit per the article's own pending-issue convention]

The architectural implication of a casebook gap on the input side bears on the curriculum-grounding claim the article makes elsewhere. The case study’s curriculum-grounded retrieval applies to the course-issued layer rather than to the full reading load that includes the assigned casebook. The static-versus-chatbot contrast is sharpest precisely because the case study does not retrieve casebook text at runtime: a reviewed static website published from a structured corpus does not require ingesting the full reading list, because the work happens at build time against what the professor authored or curated. A future replication may ingest casebook excerpts under license; the case study’s object remains the course-issued layer.

## 12.D Privacy and the snapshot commitment

The second of the workplan’s open-decision risks is student work as input. If the professor’s past exam answers, office-hours notes, or LMS posts were used as training input to the vault, the article carries a separate privacy paragraph naming FERPA-compliant handling, consent and anonymization protocols, and Institutional Review Board review where appropriate; if none of those materials was used, the article says so explicitly.[CITE: forward reference to App. A (Workplan §6.2 Open-Decision Protocol subsection); see same-section open-issues footnote tracking the input-status confirmation] The use-side surface is parallel: the deployed site’s analytics is configured with Do Not Track respected and session recording disabled, and use-pattern data collected from current readers is the publication-side privacy surface that pairs with the input-side rule.[CITE: cross-reference to Section VIII (From Vault to Website) note carrying the PostHog deployment configuration per L-034 cross-section verification reuse]

The fourth open-decision risk is the public-site-as-evidence-versus-continuing-experiment question. The article commits to four operational guardrails: a Git tag at the manuscript snapshot date, a Wayback Machine capture of the deployed pages at that date, a canonical-reference rule under which the article cites the tagged version rather than the live HEAD, and an explicit continued-evolution-as-intended posture distinguishing the snapshot from the live site’s later growth.[CITE: forward reference to App. A (Workplan §6.4 Snapshot-Discipline Protocol subsection); see also supra Section IV (The Input Corpus) (Snapshot-Disclosure-Paragraph subsection) for the input-corpus analogue at the parallel altitude]

## 12.E Equity, accessibility, and the field-level frame

Section XII owns the article’s equity-and-accessibility argument consolidated from prior Verify findings at Sections II, III, IV, and VIII. The substantive treatment names five commitments rather than claiming a solution: the deployed single-page application presupposes broadband and a modern browser; the navigation, search-palette, and banner surfaces have screen-reader behavior that remains an open testing question; the modernized PDFs are rendered at three hundred dots per inch and assume a device capable of high-resolution rendering; Canvas enrollment gates the input corpus by course membership; and PostHog analytics respects Do Not Track and disables session recording. The article’s contribution here is the disclosure rather than the solution.

Bond and colleagues’ meta-systematic review of sixty-six artificial-intelligence-in-higher-education publications concludes that the field needs more ethics and rigor, and Section XII inherits that frame at the ethics-and-rigor altitude distinct from Section XI’s methodological-rigor altitude.[CITE: Bond et al. 2024, 21 Int'l J. Educ. Tech. Higher Educ. art. 4, cross-section reuse via Section XI note 8 per L-034 with original URL-liveness verification recorded at the Section XI Cite tick; per L-024 the transfer-of-inference clause at this section names that the field-level call for honest risk disclosure generalizes to the present catalogue, and that the implementation surface does not transfer because Bond's sixty-six-publication corpus is built predominantly on chatbot-tutor and learning-management-system interventions while this article catalogues a reviewed-static-website artifact]
