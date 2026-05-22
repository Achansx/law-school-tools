---
section: "06"
fact_type: example
source_path: "Chandler Constitutional Law Vault/Templates/Case Brief.md"
verified: true
notes: "The Case Brief template is the prompt contract. The frontmatter schema (case_name, citation, year, court, doctrines, status, midpage_id, source_files, holding-bar fields, citation-meta, authority-lineage) and the nine fixed H2 sections (Memory Jogger, Facts, Procedural History, Judicial Votes, Holding, Analysis with concurrence and dissent breakouts, Hypothetical Applications, Critique, Key Quotations, plus Key Points and Connections and Sources) together specify what every generation pass must produce. The template is loaded into every Ingest and Enrich prompt because the prompt is defined as 'fill in this typed scaffold,' not 'write a brief about Marbury.' Section VI should use this card as the structural evidence that the vault treats prompts as typed-schema fillers rather than free-form requests; the schema is the pedagogical move, because the nine-section structure is itself the canonical law-school case-brief format. Source overlap with Section V's evidence-05-frontmatter-schemas and evidence-05-case-brief-nine-section-standard is real but the framing here is different: Section V uses the schema as the substrate for AI-authored notes; Section VI uses the schema as the prompt's pedagogical commitment."
---

The Case Brief template defines the prompt contract. Its frontmatter schema names eighteen required fields plus the holding-bar block (issue, holding, reasoning, doctrine_family), the citation-meta block (argued, decided, panel, author, vote, disposition), and the authority-lineage block (relies_on, distinguishes, applied_in, overrules, overruled_by). Its body specifies nine fixed H2 sections in fixed order: Memory Jogger, Facts, Procedural History, Judicial Votes, Holding, Analysis (with Majority, Concurrence, Dissent breakouts), Hypothetical Applications, Critique, Key Quotations, plus Key Points, Connections, and Sources. Every Ingest and Enrich run loads this template as part of its prompt; the model is asked to fill the scaffold rather than to write a brief about a case in whatever shape it prefers. The choice is pedagogical, not merely structural: the nine-section sequence is the canonical law-school case-brief format, and committing the prompt to that sequence forces every generated brief to do the same analytical work a student is expected to do when briefing a case by hand.

Exact source quote, `Chandler Constitutional Law Vault/Templates/Case Brief.md` H2 sequence (lines 79 to 173):

> # {{Case Name}}
>
> ## Memory Jogger
> ## Facts
> ## Procedural History
> ## Judicial Votes
> ## Holding
> ## Analysis
> ### Majority Opinion
> ### Concurrence (Author)
> ### Dissent (Author)
> ## Hypothetical Applications
> ### Same-Side (Would come out the same way)
> ### Opposite-Side (Would come out differently)
> ### Fence-Sitter (Genuinely unclear)
> ## Critique
> ## Key Quotations
> ## Key Points
> ## Connections
> ## Sources
