---
id: "13"
title: "Institutional Implications"
status: needs_polish
target_words: 500
word_count: 549
last_phase: verify-provenance
cite_status: needs_polish
polish_status: needs_polish
footnotes_count: 9
provenance_audited: true
provenance_audited_at: 2026-05-31T18:00:00Z
provenance_audit_run: 280
provenance_score: 4.0
provenance_score_prior: 3.8
provenance_audit_run_prior: 139
claims_total: 16
claims_mapped: 15
unsupported_claims:
  - claim_text: "Whether a versioned, citable, publicly served course artifact counts as scholarship is itself contested, and the institution must decide whether to treat it as teaching infrastructure or as scholarship for review and promotion."
    paragraph: 3
    reason: requires-primary-source
provenance_note_run280: "Run-280 Verify Provenance Auditor re-audit, first re-audit since the run-139 baseline (3.8 across 4/3/4/5/3 against pre-run-235 Cite + pre-run-236 Polish 12-claim scan with 1 unsupported_claim on the MIT Press joint-publisher claim that the run-235 Cite closed by adding the MIT News [^1] anchor for the 2022 series). Re-scored 4/3/4/5/4 = 4.0 against the post-run-235 / post-run-236 polished prose, a +0.2 lift from the 3.8 baseline driven by criterion 5 gap_honesty 3 -> 4 on the run-236 XIII.C 'contested' recognition flag and XIII.D capacity-gap flag both reading as explicit gap-flagging. claims_total expanded 12 -> 16 (four new factual claims the run-139 baseline missed: XIII.A complementary-not-competing structural claim, XIII.B three-actor library/ID/IT enumeration, XIII.C versioned-commit operational claim, XIII.C 'counts as scholarship is itself contested' claim-of-contestation); claims_mapped 11 -> 15 (15/16 = 93.75% mapped); unsupported_claims 0 -> 1 (one new entry: XIII.C contestation claim with reason requires-primary-source; asserts contestation as a state of the field without naming whom it is contested between or anchoring to Boyer 1990 / Sturm & Guinier / ABA Standard 405 / SoTL-in-law literature). Criterion breakdown: claim_coverage 4 (hold at 4 with the expanded-scan 93.75% ratio sitting in the same 90-94% interpolation zone the run-139 11/12 = 91.67% ratio held); primary_source_ratio 3 (1 of 9 footnotes external primary at [^1] opencasebook.org / news.mit.edu / cali.org, structural synthesis ceiling); attribution_discipline 4 ([^4] partial-anchor on the XIII.B library/ID/IT three-actor enumeration with [^4] forward-referencing Section VIII only for IT hosting; [^6] cross-section anchor target slightly misaligned with XIII.C versioned-commit + named-reviewer operational claim forwarding to Section XII when Section VII / VIII would be the natural anchor); numerical_precision 5 (only numerical claim is MIT Press / Harvard 2022 series launch, anchored to MIT News April 26, 2022 URL with last-visited snapshot); gap_honesty 4 (XIII.C explicit 'contested' / 'stays open' flag and XIII.D capacity-gap flag both gap-flagging; 4-band deduction is the run-280 unsupported_claim addition for the XIII.C contestation claim the prose treats as a settled fact of contestation). 4.0 < 4.5, so polish_status reverts ready_for_stitch -> needs_polish per rubric/provenance-audit.md exit; PI-224 (XIII.B scholarship-of-teaching anchor), PI-225 (XII -> XIII seam + supra-XII dependence), PI-166 re-confirm (XIII.C recognition-framing leg), PI-095 re-confirm (XIII.D student-side accessibility leg), and the new XIII.C contestation unsupported_claim closing path are the next-up Polish targets. Provenance audit run state: last_audit_section / last_reaudit_section 09 -> 13; reaudit_count 11 -> 12; sections_audited stays 14; global_unsupported_open 14 -> 15."
provenance_note: "Last audited Verify run 139 (2026-05-30); provenance_audited reset to false by run-235 Cite tick because the XIII.A platform-vs-series prose and the footnote [^1] verification anchors materially changed (PI-168 resolved, PI-092 swept for this section). Run-236 Polish added two new internal supra footnotes pointing to Section XII: [^2] for the AI-tutor / adaptive-courseware architectural alternative (PI-167) and [^8] for the institutional capacity-gap access constraint (PI-095). Footnote [^1] re-verified live in run 235 (opencasebook.org via WebSearch, news.mit.edu via WebFetch, cali.org via WebFetch). Run-280 Verify Provenance Auditor re-audit re-scored 4/3/4/5/4 = 4.0 (+0.2 from the 3.8 baseline); see provenance_note_run280 above."
---

# XIII. Institutional Implications

## A. The open-educational-resource landscape and complementary positioning

Legal education already supports open educational resources. The Harvard Law School Library Innovation Lab operates H2O Open Casebooks, the MIT Press and Harvard Law School Library jointly launched an open casebook series built on the H2O platform in 2022, and CALI’s eLangdell Press distributes openly licensed casebooks and course materials.[^1] A course knowledge system is complementary to that infrastructure rather than a competing channel. The architectural alternative is the runtime AI tutor or adaptive courseware; this method chooses the reviewed static site instead.[^2] H2O and eLangdell publish the texts, while this method publishes the structure around them: the typed schema, the doctrinal map, the verified-source links, and the navigable course graph. A school that adopts the method adds a structural layer the existing projects do not provide rather than displacing them. The open-resource commitment to reusable, openly licensed materials carries across; the object of publication does not. H2O and eLangdell publish finished casebook texts under license; a course knowledge system publishes structure and links over a professor’s own slides, public opinions, and original hypotheticals.

## B. Who builds and who sustains: faculty labor and institutional roles

The method’s labor is professor-led but institutionally supported, and that split is the institutional implication. The cost-and-labor accounting shows that the build is tractable for a single professor working with a scheduled assistant and that deployment runs on near-zero-cost static hosting. The figures live in Section IX rather than here.[^3] Sustaining the work across a faculty and across course offerings is a different matter, because it implicates roles the individual professor cannot carry alone. The library stewards an open-resource catalog, instructional design partners on the schema and its pedagogy, and information technology hosts and version-controls the build pipeline.[^4] What this section names is artifact-building labor; teaching with the artifact remains the professor’s classroom craft. A course knowledge system is therefore best read as faculty scholarship of teaching coupled with institutional stewardship, not as an unfunded individual burden.

## C. Governance, control, and recognition

At institutional scale the professor’s role as the gating actor becomes an explicit governance question: who reviews each page, who maintains the vault, and who is accountable for the public artifact.[^5] The reviewed-static-website architecture is what makes the governance posture inspectable. Every page ships from a versioned commit and is accountable to a named professor who reviewed it before publication. The chain of responsibility traces to a named pre-publication human reviewer in a way a runtime system’s generations do not.[^6] The recognition question follows. Whether a versioned, citable, publicly served course artifact counts as scholarship is itself contested, and the institution must decide whether to treat it as teaching infrastructure or as scholarship for review and promotion. That decision stays open, but the inspectable, versioned artifact makes either form of recognition assessable: a reviewer can read what was published and trace who reviewed it.

## D. What the institution must decide

Adoption is opt-in and method-first. An institution adopts the method rather than the constitutional-law artifact: the typed schema, the verified-source discipline, the professorial gating, and the phase rotation. This adoption is consistent with the claim that the structure transfers while its constitutional-law content does not.[^7] The institutional implication is a modest, replicable infrastructure investment offered as an invitation rather than a mandate, subject to a capacity gap in library, instructional-design, and information-technology stewardship that Section XII develops.[^8] What an institution must decide is whether to extend that invitation, a choice the conclusion takes up.[^9]

## Footnotes

[^1]: H2O Open Casebooks, Harvard Law School Library Innovation Lab, https://opencasebook.org (last visited May 28, 2026) (URL verified live in this Cite run; open platform for making, sharing, and remixing openly licensed casebooks released under a Creative Commons BY-NC-SA license and built on the public-domain case corpus); *see also* *The MIT Press and Harvard Law School Library Launch New Series Offering High-Quality, Affordable Law Textbooks*, MIT News (Apr. 26, 2022), https://news.mit.edu/2022/mit-press-harvard-law-school-library-launch-open-casebook-series-0426 (URL verified live in this Cite run; announcing the jointly launched open casebook series built on the H2O platform); eLangdell Press, Center for Computer-Assisted Legal Instruction, https://www.cali.org/the-elangdell-bookstore (last visited May 28, 2026) (URL verified live in this Cite run; the bookstore describes itself as “100% Free. Creative Commons licensed. Peer-reviewed.” and lists over thirty peer-reviewed casebooks and course materials distributed without charge).

[^2]: *See supra* Section XII (Risks and Limits) (developing the architectural contrast between the reviewed-static-site posture and the runtime LMS-integrated AI-tutor and adaptive-courseware alternative, and the rationale for the static posture as the institutional architectural choice this method makes).

[^3]: *See supra* Section IX (Cost and Labor: The Honest Accounting) (build tractable for a single professor working with a scheduled assistant, with deployment running on near-zero-cost static hosting; the cost-and-labor figures and master table are developed in that section rather than here).

[^4]: *See supra* Section VIII (From Vault to Website) (versioned build pipeline and static-site deployment that information technology hosts and version-controls as custodian).

[^5]: *See supra* Section VII (Iterative Improvement Under Professorial Control) (the professor as the gating actor who reviews each page before it is published).

[^6]: *See supra* Section XII (Risks and Limits) (contrasting a reviewed static artifact shipped from a versioned commit with a runtime system whose generated responses are not traceable to a named pre-publication reviewer).

[^7]: *See supra* Section X (Generalization Beyond Constitutional Law) (the method, schema, verified-source discipline, and phase rotation transfer across doctrinal courses while the constitutional-law content does not).

[^8]: *See supra* Section XII (Risks and Limits) (institutional capacity gap as an access constraint: library, instructional-design, and information-technology stewardship are unevenly distributed across institutions, so the “modest, replicable” framing overstates for under-resourced schools).

[^9]: *See infra* Section XIV (Conclusion) (taking up whether the institution extends the adoption invitation).
