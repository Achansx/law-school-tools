---
id: "05"
title: "Building the Obsidian Vault"
status: ready_for_stitch
target_words: 1100
word_count: 1212
last_phase: polish
draft_status: needs_cite
cite_status: needs_polish
polish_status: ready_for_stitch
last_polish_run: 344
polish_note_run344: "Run-344 Polish closed PI-ER-SENTENCES (Polish leg): split the V.B three-clause-nested YAML-opener second sentence ('The fields cover doctrinal labels, citation metadata, authority lineage, Midpage verification anchors, and a structured holding-bar block (issue, holding, reasoning, doctrine_family) that the deployed site promotes into a banner above the prose.' — list-coordinator-parenthetical-relative-clause structure) into two sentences. Sentence 1 (16 words) carries the four YAML-field categories; sentence 2 (24 words) carries the structured holding-bar block and its deployed-site promotion. Body word_count 1209 -> 1212 (+3 from the 'They also include' connector). Mechanical hygiene clean: zero em dashes added, zero straight ASCII quotes added; curly apostrophes preserved at 'Section VII's' and the new sentence carries no new apostrophe. The split adds no new factual claim, so claims_total holds at 26; provenance_audited reset to false so the next Verify provenance re-audits the post-split V.B prose without disturbing the run-196 4.6 baseline. PI-199 source-assembly divergence (the standing reason this section was already at needs_polish) is unchanged by this tick; the split lands at one site in this source-of-truth and Stitch propagates to full-draft in the natural batch."
polish_note: "Run 194 (Polish) resolved PI-197 (V.D Dong uninterpretable raw means) via the issue's own prescribed fallback: the assessment scale is not verifiable from the source (the Dong arXiv paper is not in-repo and WebFetch is provenance-blocked; the evidence card and workplan carry only the raw means), so the scale-less means 6.37 vs 4.71 were trimmed from prose and the sentence now leads with the construct-named, scale-free statistics ('a large, statistically significant advantage in assessment scores ... (Cohen's d of 0.86, p less than 0.001)'). Footnote [^14] retains the full reported figures (6.37 vs 4.71, p<0.001, d=0.86) for disclosure. Body word_count word-neutral at 1209 (33->33 words on the edited fragment), still within the +/-10% band (ceiling 1210). provenance_audited set false per the verify_routing_reason instruction so the next Verify runs a fresh re-audit over post-PI-197 prose."
stitched_at: 2026-05-17T01:30:00Z
re_stitched_at: 2026-06-03T21:00:00Z
verify_routing_reason: "Verify run 196 (Persona 4, Provenance Auditor) P1 PI-199 (source-assembly divergence): this polished source is the per-section source of truth, but the assembled full-draft.md Section V carries seam content this source lacks - the IV->V '388-file' bridge in V.A, the inline six-case applied_in list in V.B, and refined V.A/V.B/V.C phrasing - a divergence the Stitch phase has deliberately preserved since run 188 (run-188 stitch note: the run-181 seam work was 'preserved rather than overwritten by the more generic polished-file seam'). The fresh re-audit of THIS source (below) is clean (26/26 mapped, 0 unsupported, 4.6, PASSES the 4.5 gate), but the source != assembly mismatch undermines the article's own verifiability standard, so polish_status moves stitched -> needs_polish for reconciliation. Direction is a human/Polish call: back-port the richer full-draft seam into this source, OR (given PI-188 removed the unverifiable 388 count from this source) trim the 388 bridge from the assembly so both converge on the clean source. Until reconciled, do NOT re-confirm Section 05 stitch-ready."
provenance_audited: false
provenance_audited_at: 2026-06-04T13:00:00Z
provenance_score: 4.6
claims_total: 26
claims_mapped: 26
unsupported_claims: []
provenance_audit_note: "Run-196 Verify fresh re-audit of the post-PI-197 polished source: 4.4 -> 4.6 (criteria 5/4/5/5/4). The two run-175 sub-4.5 blockers are gone from THIS source: PI-188 (the V.A 388-count tracing to a not-in-repo filesystem audit with no inline snapshot date) was resolved by removing the count from V.A, lifting numerical_precision 4 -> 5; the V.D Dong scale-uninterpretability (PI-197) was resolved at run 194, scale-free prose with full figures retained in [^14] for disclosure. claim_coverage 5 (26/26 mapped, 0 unsupported; the V.B Critique dual-perspective requirement maps to evidence-06-enrich-critique-balance-prompt.md and cross-confirms at VI.C, the V.C deployed-site search/cross-reference claim maps to evidence-03-recent-tab-and-search-palette.md and Section VIII.B); primary_source_ratio 4 (vault-procedural claims route to the in-repo App. A reproduction, acceptable per criterion 2; external primaries are Dong arXiv:2311.17696 [^14] and Peng arXiv:2408.08921 [^15]); attribution_discipline 5; gap_honesty 4 (the two Section III figure forward-references at [^6]/[^12] still read 'capture pending, see PI-012', an honest hedge but a residual gap). 4.6 >= 4.5 with unsupported_claims empty, so this source PASSES the provenance gate - the first section to clear it. The needs_polish reset above is from the separate PI-199 source-assembly finding, not from the provenance audit."
---

# V. Building the Obsidian Vault

## A. From flat folder to typed schema

The vault organizes its content into three primary folders, Cases, Topics, and Lectures, each backed by a canonical template in Templates and a per-page YAML frontmatter schema.[^1] The three folders correspond to three distinct units of legal-pedagogy work: a decided case, a doctrine, and a class session captured as a lecture summary rather than a live transcript. That typing lets the vault behave as a schema, not a folder of prose. Section IV described the input side; Section V describes the layer that translates it into the typed intermediate Section VIII compiles into a website.

The smallest structural commitment is a three-way invariant. Within Cases, the filename, the H1, and the frontmatter case_name field all agree, with no periods, and with the word and rather than an ampersand; the same rule binds Topics and Lectures.[^2] Wiki-links therefore resolve by exact filename match rather than normalization heuristics, so Section VIII’s build script links pages by name without guessing.

## B. The Case Brief as the canonical page type

Every page in Cases opens with a roughly thirty-field YAML frontmatter block before the H1 (Figure 5.1).[^3][^18] The fields cover doctrinal labels, citation metadata, authority lineage, and Midpage verification anchors. They also include a structured holding-bar block (issue, holding, reasoning, doctrine_family) that the deployed site promotes into a banner above the prose. The frontmatter is the load-bearing surface for Section VII’s iteration loop, which operates on typed fields rather than re-parsing prose.

Every Cases page also follows a fixed H2 sequence inherited from the Case Brief template: Memory Jogger, Facts, Procedural History, Judicial Votes, Holding, Analysis (with a required Majority subsection and optional Concurrence and Dissent subsections), Hypothetical Applications (split into Same-Side, Opposite-Side, and Fence-Sitter buckets totaling five hypotheticals), Critique, Key Quotations, Key Points, Connections, and Sources.[^4] The Hypothetical Applications block is the pedagogically distinctive piece. Section VI’s prompting design uses the block to draft exam-style hypotheticals on a known structural shape rather than free-form text, and the professor reviews each draft before it reaches a page. The Critique block’s requirement of both progressive and originalist or textualist perspectives keeps Section VI from looking like content generation alone.

A populated brief shows what the schema produces once Enrich fills the Ingest-time blanks. The *Marbury v. Madison* (1803) brief carries midpage_id 84759, a canonical Midpage URL, and cited_by 3,995 pulled from CourtListener. Its applied_in list names six downstream Supreme Court cases. The doctrine_family field is locked to Separation of Powers, and the holding-bar block is fully populated.[^5] The build script renders the holding bar, citation count, and authority lineage directly off these typed fields, the payoff Section VIII later realizes as a navigable site.[^6]

## C. Topic pages as the synthesis layer

The Topic page is the synthesis form, where the vault stops being a folder of briefs and becomes a knowledge system. The professor decides which Case briefs and Lecture summaries belong on a Topic page, a curation choice recorded in the page’s source_files frontmatter list, not an automated similarity computation. Once the selection is made, the schema enforces the structure: an Overview, a Governing Rule block stating the test in exam-ready language, a Doctrinal Development section walking the cases in analytical order, a Key Cases table, five Hypothetical Applications, an exam-spotting framework, and a Critique.[^7] The synthesis form transfers to any case-and-doctrine course, the architectural lever Section X’s generalization argument pivots on, though Section X.D bounds that reach to courses organized around tagged doctrines and leading cases.

The Judicial Review topic is the canonical example. Its frontmatter key_cases list cites *Marbury* (1803), *Martin v. Hunter’s Lessee* (1816), *The Prize Cases* (1863), and *Youngstown* (1952); its source_files attribution lists three Cases pages and two Lectures pages; the prose stitches them with case back-links.[^8] The provenance trail runs from prose back to source, and that chain is the architectural contrast Section XII later draws between the case study and chatbot-tutor systems.

The wiki-link grammar supporting the synthesis layer is small and fixed. Cross-page links take the form of bracketed folder, filename, and display-text tuples; tags are lowercase and hyphenated and placed at file end; every page carries a source_files frontmatter list in lockstep with a Sources footer enforced by the Lint phase.[^9] The source Obsidian vault renders a graph view natively (Figure 5.2), while the deployed site runs search across pages and surfaces cross-references; the link grammar is mechanical and the provenance trail verifiable, which makes Section VIII’s self-publishing claim an architectural consequence.[^10] Each page also exposes a local graph of its wiki-link neighborhood; its shape varies by node type, from a lone case to a dense doctrinal hub to a multi-doctrine review lecture (Figures 5.3 through 5.8).[^19]

## D. Schema doing work prose alone cannot

The doctrine_family field on the Case Brief template carries exactly four values: Federalism, Separation of Powers, Individual Rights, and Justiciability; the same enum binds the area and family fields on Topic Page templates.[^11] The build script reads this one field to drive which color column a case or topic appears under in the four-family grid and to set the holding-bar accent on case pages, the smallest unit of schema doing work prose alone could not.[^12]

The enum is locked. RUNBOOK requires a non-fitting page to be realigned to the nearest canonical value rather than the enum widened in place; widening is a vault-wide change requiring a template-guide edit, a RUNBOOK update, and a build-narrative note.[^13] Section VII picks this up as the kind of explicit constraint that keeps an LLM-assisted system from drifting page by page.

Published work on graph-augmented retrieval supplies the analogy. The Dong et al. controlled study of seventy-six students reported a large, statistically significant advantage in assessment scores for knowledge-graph-augmented retrieval over pure semantic retrieval (Cohen’s d of 0.86, p less than 0.001),[^14] and the Peng et al. survey defines the canonical GraphRAG workflow as graph-based indexing, graph-guided retrieval, and graph-enhanced generation.[^15] What transfers to the vault is the finding itself, the general value of structured retrieval over flat semantic similarity, not the conversational AI tutor Dong et al. built to deliver it. The vault adopts that structural insight in static-publication form: the link graph and typed frontmatter are curated by hand, and the deployed site serves the graph statically rather than retrieving over it at query time.

## E. The structure is reactive, not designed top-down

The vault’s per-phase rubric architecture and tiered file loading were forced by a token-cost problem the system encountered. Early runs loaded one large rubric covering all six phases, the full LESSONS file, and the entire build narrative on every run, so a Lint run that cared only about structural formatting burned context on Enrich and Verify criteria it would never use. The fix was structural: split the rubric into six per-phase files, skip LESSONS for phases that do not need it, rotate the build narrative monthly, and log no-op phases as one-line entries.[^16]

The area-enum realignment policy is the schema-side companion. The Judicial Review topic was initially assigned an area value of *Federal Judicial Power*, which is not one of the four canonical doctrine_family values; under professorial supervision the page was realigned to Separation of Powers rather than the enum widened in place, and RUNBOOK now codifies that any future drift triggers the same vault-wide process.[^17]

The vault’s schema is therefore a sequence of structural commitments, each forced by a specific failure mode and preserved as a rule the next run obeys. Section VII shows how those lessons feed forward into the maintenance loop.

## Footnotes

[^1]: *See infra* App. A (Input Inventory) § A.3 (Source Material Conventions: Cases/, Topics/, and Lectures/ as the three first-class content folders, each backed by a canonical template in Templates/; Source Materials/ as read-only input); *see also infra* App. C (Obsidian Note Templates) (templates for the three content folders); *see also infra* App. D (Karpathy-Loop Per-Phase Rubric) (rubric/ as per-phase scoring criteria; archive/ as rotated narrative logs).

[^2]: *See infra* App. A (Input Inventory) § A.3 (Source Material Conventions: filename, H1, and frontmatter case_name three-way invariant for Cases, with no periods and “and” rather than “&”; parallel rule for Topics/Topic Name.md and Lectures/Lecture Title.md).

[^3]: *See infra* App. C (Obsidian Note Templates) (Case Brief template YAML frontmatter, with approximately thirty fields including doctrines, concepts, citation, argued, decided, author, vote, disposition, midpage_id, midpage_url, cited_by, verified, source_files, issue, holding, reasoning, doctrine_family, relies_on, distinguishes, applied_in, overrules, and overruled_by).

[^4]: *See infra* App. C (Obsidian Note Templates) (Case Brief template H2 sequence: Memory Jogger; Facts; Procedural History; Judicial Votes; Holding; Analysis, with required Majority subsection and optional Concurrence and Dissent subsections; Hypothetical Applications, with Same-Side, Opposite-Side, and Fence-Sitter subsections totaling five hypotheticals; Critique; Key Quotations; Key Points; Connections; Sources).

[^5]: *See infra* App. C (Obsidian Note Templates) (Case Brief template instantiated as Cases/Marbury v Madison (1803).md, frontmatter snapshot verified April 24, 2026, capturing midpage_id ‘84759’, cited_by 3,995 (sourced from CourtListener find_citing_cases), six-entry applied_in list naming *Martin v. Hunter’s Lessee*, *McCulloch v. Maryland*, *The Prize Cases*, *United States v. Rahimi*, *Cohens v. Virginia*, and *City of Boerne v. Flores*, and doctrine_family Separation of Powers).

[^6]: *See infra* Section III (Case Study: A Constitutional-Law Knowledge System) (figure showing the holding-bar block rendered as a structured banner above case prose on the deployed site; figure capture pending, see PI-012).

[^7]: *See infra* App. C (Obsidian Note Templates) (Topic Page template structure: Overview; Governing Rule; Doctrinal Development; Key Cases table; Hypothetical Applications; exam-spotting framework; Critique).

[^8]: *See infra* App. C (Obsidian Note Templates) (Topic Page template instantiated as Topics/Judicial Review.md, frontmatter key_cases list naming *Marbury v. Madison* (1803), *Martin v. Hunter’s Lessee* (1816), *The Prize Cases* (1863), and *Youngstown Sheet and Tube Co. v. Sawyer* (1952); source_files attribution to three Cases pages and two Lectures pages; case back-links at every case introduction in the Doctrinal Development section).

[^9]: *See infra* App. C (Obsidian Note Templates) (wiki-link grammar [[folder/filename|Display Text]]; lowercase-hyphenated tags at file end; source_files frontmatter in lockstep with the Sources footer section, enforced by the Lint phase as a structural check).

[^10]: *See infra* fig. 5.2 (source Obsidian vault graph view rendering cross-page wiki-links as an interactive node graph, a working view in the author’s Obsidian editing environment rather than a feature of the deployed reader-facing site; captured from the source Obsidian vault May 26, 2026).

[^11]: *See infra* App. C (Obsidian Note Templates) (Case Brief template doctrine_family field locked to one of four values: Federalism, Separation of Powers, Individual Rights, or Justiciability; same enum binds the Topic Page template’s area and family fields).

[^12]: *See infra* Section III (Case Study: A Constitutional-Law Knowledge System) (figure showing the deployed site’s four-family grid index, with each column color-driven by the doctrine_family field on Case Brief and Topic Page templates; figure capture pending, see PI-012).

[^13]: *See infra* App. D (Karpathy-Loop Per-Phase Rubric) (enum realignment policy in vault RUNBOOK.md, requiring a non-fitting page to be realigned to the nearest canonical value; widening the enum requires a template-guide edit, a RUNBOOK.md update, and a one-paragraph BUILD_NARRATIVE entry).

[^14]: Chenxi Dong, Yimin Yuan, Kan Chen, Shupei Cheng & Chujie Wen, *How to Build an Adaptive AI Tutor for Any Course Using Knowledge Graph-Enhanced Retrieval-Augmented Generation (KG-RAG)*, arXiv:2311.17696 (Feb. 12, 2025), https://arxiv.org/abs/2311.17696 (last visited May 16, 2026) (controlled study of seventy-six students reporting knowledge-graph-augmented retrieval mean assessment score 6.37 against 4.71 for pure semantic retrieval; p < 0.001; Cohen’s *d* = 0.86; the study delivered that gain through an adaptive conversational AI tutor, the runtime architecture the vault does not adopt).

[^15]: Boci Peng, Yun Zhu, Yongchao Liu, Xiaohe Bo, Haizhou Shi, Chuntao Hong, Yan Zhang & Siliang Tang, *Graph Retrieval-Augmented Generation: A Survey*, arXiv:2408.08921 (Aug. 15, 2024), https://arxiv.org/abs/2408.08921 (last visited May 16, 2026) (defining the canonical GraphRAG workflow as graph-based indexing, graph-guided retrieval, and graph-enhanced generation).

[^16]: *See infra* App. D (Karpathy-Loop Per-Phase Rubric) (per-phase rubric file split into six phase-specific files; tiered file loading skipping LESSONS for phases that do not need it; monthly rotation of the BUILD_NARRATIVE file; one-line logging for no-op phase runs).

[^17]: *See infra* App. D (Karpathy-Loop Per-Phase Rubric) (Topics/Judicial Review.md area field initially assigned *Federal Judicial Power*, realigned to Separation of Powers per the canonical four-value enum; vault RUNBOOK.md codification of the realignment process for future drift).

[^18]: *See infra* fig. 5.1 (*Marbury v. Madison* (1803) case brief open in Obsidian Live Preview, the typed-properties panel rendering the YAML frontmatter as structured fields, including case_name, citation, doctrine_family, midpage_id, source_files, and a six-entry applied_in list; captured from the source Obsidian vault May 26, 2026).

[^19]: *See infra* figs. 5.3–5.8 (local-graph captures from the source Obsidian vault, May 26, 2026, covering each node type twice: *Marbury v. Madison* and *Brown v. Board of Education* (cases), the Commerce Clause and Substantive Due Process (topics), and two review lectures, each showing the distinct wiki-link relationship cluster that layer of the corpus produces).
