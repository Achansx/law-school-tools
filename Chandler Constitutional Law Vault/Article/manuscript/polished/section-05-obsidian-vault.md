---
id: "05"
title: "Building the Obsidian Vault"
status: ready_for_stitch
target_words: 1100
word_count: 1209
last_phase: polish
draft_status: needs_cite
cite_status: needs_polish
polish_status: ready_for_stitch
stitched_at: 2026-05-17T01:30:00Z
re_stitched_at: 2026-06-02T15:00:00Z
provenance_audited: true
provenance_audited_at: 2026-06-02T17:00:00Z
provenance_score: 4.4
claims_total: 26
claims_mapped: 26
unsupported_claims: []
provenance_stale_reason: "Run-175 Verify re-audited the run-172/173 prose: score rose 3.8 -> 4.4 (criteria 5/4/5/4/4) as the 388-count inconsistency, the GraphRAG and graph-view overclaims, and the un-attributed curation/review actions all closed, but it cannot clear the 4.5 gate because primary_source_ratio and numerical_precision both turn on PI-188 (the corpus count traces to an internal filesystem audit whose Source Materials corpus is not in-repo, and V.A carries no inline snapshot date) plus three pending-figure forward references (PI-012, PI-V-OBSIDIAN-FIGS). polish_status reset stitched -> needs_polish; Polish-owned targets PI-189 (V.C unbounded 'any doctrinal subject' transfer claim) and PI-013 (V.D Dong effect-size architectural transfer)."
---

# V. Building the Obsidian Vault

## A. From flat folder to typed schema

The vault organizes its content into three primary folders, Cases, Topics, and Lectures, each backed by a canonical template in Templates and a per-page YAML frontmatter schema.[^1] The three folders correspond to three distinct units of legal-pedagogy work: a decided case, a doctrine, and a class session captured as a lecture summary rather than a live transcript. That typing lets the vault behave as a schema, not a folder of prose. Section IV described the input side; Section V describes the layer that translates it into the typed intermediate Section VIII compiles into a website.

The smallest structural commitment is a three-way invariant. Within Cases, the filename, the H1, and the frontmatter case_name field all agree, with no periods, and with the word and rather than an ampersand; the same rule binds Topics and Lectures.[^2] Wiki-links therefore resolve by exact filename match rather than normalization heuristics, so Section VIII’s build script links pages by name without guessing.

## B. The Case Brief as the canonical page type

Every page in Cases opens with a roughly thirty-field YAML frontmatter block before the H1 (Figure 5.1).[^3][^18] The fields cover doctrinal labels, citation metadata, authority lineage, Midpage verification anchors, and a structured holding-bar block (issue, holding, reasoning, doctrine_family) that the deployed site promotes into a banner above the prose. The frontmatter is the load-bearing surface for Section VII’s iteration loop, which operates on typed fields rather than re-parsing prose.

Every Cases page also follows a fixed H2 sequence inherited from the Case Brief template: Memory Jogger, Facts, Procedural History, Judicial Votes, Holding, Analysis (with a required Majority subsection and optional Concurrence and Dissent subsections), Hypothetical Applications (split into Same-Side, Opposite-Side, and Fence-Sitter buckets totaling five hypotheticals), Critique, Key Quotations, Key Points, Connections, and Sources.[^4] The Hypothetical Applications block is the pedagogically distinctive piece. Section VI’s prompting design uses the block to draft exam-style hypotheticals on a known structural shape rather than free-form text, and the professor reviews each draft before it reaches a page. The Critique block’s requirement of both progressive and originalist or textualist perspectives keeps Section VI from looking like content generation alone.

A populated brief shows what the schema produces once Enrich fills the Ingest-time blanks. The *Marbury v. Madison* (1803) brief carries midpage_id 84759, a canonical Midpage URL, and cited_by 3,995 pulled from CourtListener. Its applied_in list names six downstream Supreme Court cases. The doctrine_family field is locked to Separation of Powers, and the holding-bar block is fully populated.[^5] The build script renders the holding bar, citation count, and authority lineage directly off these typed fields, the payoff Section VIII later realizes as a navigable site.[^6]

## C. Topic pages as the synthesis layer

The Topic page is the synthesis form, where the vault stops being a folder of briefs and becomes a knowledge system. The professor decides which Case briefs and Lecture summaries belong on a Topic page, a curation choice recorded in the page’s source_files frontmatter list, not an automated similarity computation. Once the selection is made, the schema enforces the structure: an Overview, a Governing Rule block stating the test in exam-ready language, a Doctrinal Development section walking the cases in analytical order, a Key Cases table, five Hypothetical Applications, an exam-spotting framework, and a Critique.[^7] The synthesis form transfers to any case-and-doctrine course, the architectural lever Section X’s generalization argument pivots on, though Section X.D bounds that reach to courses organized around tagged doctrines and leading cases.

The Judicial Review topic is the canonical example. Its frontmatter key_cases list cites *Marbury* (1803), *Martin v. Hunter’s Lessee* (1816), *The Prize Cases* (1863), and *Youngstown* (1952); its source_files attribution lists three Cases pages and two Lectures pages; the prose stitches them with case back-links.[^8] The provenance trail runs from prose back to source, and that chain is the architectural contrast Section XII later draws between the case study and chatbot-tutor systems.

The wiki-link grammar supporting the synthesis layer is small and fixed. Cross-page links take the form of bracketed folder, filename, and display-text tuples; tags are lowercase and hyphenated and placed at file end; every page carries a source_files frontmatter list in lockstep with a Sources footer enforced by the Lint phase.[^9] The source Obsidian vault renders a graph view natively (Figure 5.2), while the deployed site runs search across pages and surfaces cross-references; the link grammar is mechanical and the provenance trail verifiable, which makes Section VIII’s self-publishing claim an architectural consequence.[^10] Each page also exposes a local graph of its wiki-link neighborhood; its shape varies by node type, from a lone case to a dense doctrinal hub to a multi-doctrine review lecture (Figures 5.3 through 5.8).[^19]

## D. Schema doing work prose alone cannot

The doctrine_family field on the Case Brief template carries exactly four values: Federalism, Separation of Powers, Individual Rights, and Justiciability; the same enum binds the area and family fields on Topic Page templates.[^11] The build script reads this one field to drive which color column a case or topic appears under in the four-family grid and to set the holding-bar accent on case pages, the smallest unit of schema doing work prose alone could not.[^12]

The enum is locked. RUNBOOK requires a non-fitting page to be realigned to the nearest canonical value rather than the enum widened in place; widening is a vault-wide change requiring a template-guide edit, a RUNBOOK update, and a build-narrative note.[^13] Section VII picks this up as the kind of explicit constraint that keeps an LLM-assisted system from drifting page by page.

Published work on graph-augmented retrieval supplies the analogy. The Dong et al. controlled study of seventy-six students reported mean scores of 6.37 against 4.71 for a knowledge-graph-augmented retrieval system over pure semantic retrieval, p less than 0.001, Cohen’s d of 0.86,[^14] and the Peng et al. survey defines the canonical GraphRAG workflow as graph-based indexing, graph-guided retrieval, and graph-enhanced generation.[^15] What transfers to the vault is the finding itself, the general value of structured retrieval over flat semantic similarity, not the conversational AI tutor Dong et al. built to deliver it. The vault adopts that structural insight in static-publication form: the link graph and typed frontmatter are curated by hand, and the deployed site serves the graph statically rather than retrieving over it at query time.

## E. The structure is reactive, not designed top-down

The vault’s per-phase rubric architecture and tiered file loading were forced by a token-cost problem the system encountered. Early runs loaded one large rubric covering all six phases, the full LESSONS file, and the entire build narrative on every run, so a Lint run that cared only about structural formatting burned context on Enrich and Verify criteria it would never use. The fix was structural: split the rubric into six per-phase files, skip LESSONS for phases that do not need it, rotate the build narrative monthly, and log no-op phases as one-line entries.[^16]

The area-enum realignment policy is the schema-side companion. The Judicial Review topic was initially assigned an area value of *Federal Judicial Power*, which is not one of the four canonical doctrine_family values; under professorial supervision the page was realigned to Separation of Powers rather than the enum widened in place, and RUNBOOK now codifies that any future drift triggers the same vault-wide process.[^17]

The vault’s schema is therefore a sequence of structural commitments, each forced by a specific failure mode and preserved as a rule the next run obeys. Section VII shows how those lessons feed forward into the maintenance loop.

## Footnotes

[^1]: *See infra* App. A (Vault Architecture and File Layout) (Cases/, Topics/, and Lectures/ as the three first-class content folders, each backed by a canonical template in Templates/; Source Materials/ as read-only input; rubric/ as per-phase scoring criteria; archive/ as rotated narrative logs).

[^2]: *See infra* App. A (Vault Architecture and File Layout) (filename, H1, and frontmatter case_name three-way invariant for Cases, with no periods and “and” rather than “&”; parallel rule for Topics/Topic Name.md and Lectures/Lecture Title.md).

[^3]: *See infra* App. A (Vault Architecture and File Layout) (Case Brief template YAML frontmatter, with approximately thirty fields including doctrines, concepts, citation, argued, decided, author, vote, disposition, midpage_id, midpage_url, cited_by, verified, source_files, issue, holding, reasoning, doctrine_family, relies_on, distinguishes, applied_in, overrules, and overruled_by).

[^4]: *See infra* App. A (Vault Architecture and File Layout) (Case Brief template H2 sequence: Memory Jogger; Facts; Procedural History; Judicial Votes; Holding; Analysis, with required Majority subsection and optional Concurrence and Dissent subsections; Hypothetical Applications, with Same-Side, Opposite-Side, and Fence-Sitter subsections totaling five hypotheticals; Critique; Key Quotations; Key Points; Connections; Sources).

[^5]: *See infra* App. A (Vault Architecture and File Layout) (frontmatter snapshot of Cases/Marbury v Madison (1803).md, verified April 24, 2026, capturing midpage_id ‘84759’, cited_by 3,995 (sourced from CourtListener find_citing_cases), six-entry applied_in list naming *Martin v. Hunter’s Lessee*, *McCulloch v. Maryland*, *The Prize Cases*, *United States v. Rahimi*, *Cohens v. Virginia*, and *City of Boerne v. Flores*, and doctrine_family Separation of Powers).

[^6]: *See infra* Section III (Case Study: A Constitutional-Law Knowledge System) (figure showing the holding-bar block rendered as a structured banner above case prose on the deployed site; figure capture pending, see PI-012).

[^7]: *See infra* App. A (Vault Architecture and File Layout) (Topic Page template structure: Overview; Governing Rule; Doctrinal Development; Key Cases table; Hypothetical Applications; exam-spotting framework; Critique).

[^8]: *See infra* App. A (Vault Architecture and File Layout) (Topics/Judicial Review.md frontmatter key_cases list naming *Marbury v. Madison* (1803), *Martin v. Hunter’s Lessee* (1816), *The Prize Cases* (1863), and *Youngstown Sheet and Tube Co. v. Sawyer* (1952); source_files attribution to three Cases pages and two Lectures pages; case back-links at every case introduction in the Doctrinal Development section).

[^9]: *See infra* App. A (Vault Architecture and File Layout) (wiki-link grammar [[folder/filename|Display Text]]; lowercase-hyphenated tags at file end; source_files frontmatter in lockstep with the Sources footer section, enforced by the Lint phase as a structural check).

[^10]: *See infra* fig. 5.2 (source Obsidian vault graph view rendering cross-page wiki-links as an interactive node graph, a working view in the author’s Obsidian editing environment rather than a feature of the deployed reader-facing site; captured from the source Obsidian vault May 26, 2026).

[^11]: *See infra* App. A (Vault Architecture and File Layout) (Case Brief template doctrine_family field locked to one of four values: Federalism, Separation of Powers, Individual Rights, or Justiciability; same enum binds the Topic Page template’s area and family fields).

[^12]: *See infra* Section III (Case Study: A Constitutional-Law Knowledge System) (figure showing the deployed site’s four-family grid index, with each column color-driven by the doctrine_family field on Case Brief and Topic Page templates; figure capture pending, see PI-012).

[^13]: *See infra* App. A (Vault Architecture and File Layout) (enum realignment policy in vault RUNBOOK.md, requiring a non-fitting page to be realigned to the nearest canonical value; widening the enum requires a template-guide edit, a RUNBOOK.md update, and a one-paragraph BUILD_NARRATIVE entry).

[^14]: Chenxi Dong, Yimin Yuan, Kan Chen, Shupei Cheng & Chujie Wen, *How to Build an Adaptive AI Tutor for Any Course Using Knowledge Graph-Enhanced Retrieval-Augmented Generation (KG-RAG)*, arXiv:2311.17696 (Feb. 12, 2025), https://arxiv.org/abs/2311.17696 (last visited May 16, 2026) (controlled study of seventy-six students reporting knowledge-graph-augmented retrieval mean assessment score 6.37 against 4.71 for pure semantic retrieval; p < 0.001; Cohen’s *d* = 0.86; the study delivered that gain through an adaptive conversational AI tutor, the runtime architecture the vault does not adopt).

[^15]: Boci Peng, Yun Zhu, Yongchao Liu, Xiaohe Bo, Haizhou Shi, Chuntao Hong, Yan Zhang & Siliang Tang, *Graph Retrieval-Augmented Generation: A Survey*, arXiv:2408.08921 (Aug. 15, 2024), https://arxiv.org/abs/2408.08921 (last visited May 16, 2026) (defining the canonical GraphRAG workflow as graph-based indexing, graph-guided retrieval, and graph-enhanced generation).

[^16]: *See infra* App. A (Vault Architecture and File Layout) (per-phase rubric file split into six phase-specific files; tiered file loading skipping LESSONS for phases that do not need it; monthly rotation of the BUILD_NARRATIVE file; one-line logging for no-op phase runs); *see also infra* App. D (Build-System Correspondence and Internal Drafts) (vault build-narrative entries describing the architectural transition from a single monolithic rubric to per-phase rubrics).

[^17]: *See infra* App. A (Vault Architecture and File Layout) (Topics/Judicial Review.md area field initially assigned *Federal Judicial Power*, realigned to Separation of Powers per the canonical four-value enum; vault RUNBOOK.md codification of the realignment process for future drift).

[^18]: *See infra* fig. 5.1 (*Marbury v. Madison* (1803) case brief open in Obsidian Live Preview, the typed-properties panel rendering the YAML frontmatter as structured fields, including case_name, citation, doctrine_family, midpage_id, source_files, and a six-entry applied_in list; captured from the source Obsidian vault May 26, 2026).

[^19]: *See infra* figs. 5.3–5.8 (local-graph captures from the source Obsidian vault, May 26, 2026, covering each node type twice: *Marbury v. Madison* and *Brown v. Board of Education* (cases), the Commerce Clause and Substantive Due Process (topics), and two review lectures, each showing the distinct wiki-link relationship cluster that layer of the corpus produces).
