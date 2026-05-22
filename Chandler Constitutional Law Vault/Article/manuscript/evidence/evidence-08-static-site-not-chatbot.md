---
section: "08"
fact_type: argument
source_path: "Chandler Constitutional Law Vault/archive/vault-blog-post-draft.md"
verified: true
notes: "The static-versus-chatbot architectural choice as a Section VIII setup for Section XII. Per L-003 the case study is never described as a chatbot, tutor that converses, or interactive assistant. Section VIII names the architectural choice (markdown source → JSON artifact → SPA shell, no model in the request path) and points forward to Section XII for the risk argument. This card pulls from the blog draft's framing of the rotation phases as the surface that handles AI quality issues and from the workplan's Sajja et al. positioning as a chatbot contrast. The Sajja URL is deferred to Cite per L-019 — workplan bibliography has the URL, but Harvest does not retry WebFetch and Cite will use WebSearch per L-022. This is the single most load-bearing card in the Section VIII set because it establishes the architectural posture the rest of the article depends on."
---

Section VIII's most load-bearing claim is the architectural one: the case study is a reviewed static site, not a chatbot. No LLM sits in the request path. The published page is a stable HTML and JSON artifact, written and verified by the rotation phases at publish time, served by the CDN without further model inference. Risk lives in the build pipeline, where it can be caught by Verify and held back by the Deploy entry guard; risk does not live in the response a student gets when they open a page. This framing distinguishes the case study from contemporaneous AI-in-education systems that are chatbots answering questions at runtime, the architectural contrast the workplan's annotated bibliography names with Sajja et al. (2023) and that Section XII develops with the Magesh et al. hallucination findings. Section VIII names the architectural choice and points forward to Section XII for the risk argument; the L-003 rule against chatbot framing applies here at full strength.

Exact source quote, `Chandler Constitutional Law Vault/archive/vault-blog-post-draft.md` lines 4 to 5 (the system as a phased rotation that handles quality control before publication, not at request time):

> The goal was a cross-referenced Obsidian wiki where every major case has a structured brief, every doctrine has a synthesis page, and every lecture is summarized with the professor's framing preserved. Maintained automatically every 30 minutes by a scheduled task that rotates through six phases: Ingest new materials, Lint for structural integrity, Enrich for substantive depth, Expand for cross-references, Synthesize for doctrine pages, and Verify to catch regressions.

And `Chandler Constitutional Law Vault/Article-Workplan.md` lines 200 to 200 (Sajja et al. as the chatbot contrast):

> **Ramteja Sajja, Yusuf Sermet, David M. Cwiertny & Ibrahim Demir, *Platform‑independent and curriculum‑oriented intelligent assistant for higher education*, 20 Int'l J. Educational Tech. Higher Educ., Art. 42 (2023).** A working example of a curriculum‑specific AI assistant. Use as a contrast in Section III: their system is a chatbot that answers students' questions; ours is a reviewed static site that students browse. Different risk profile, different pedagogical commitments. https://link.springer.com/article/10.1186/s41239-023-00412-7.

Per L-019, the Sajja URL is recorded `verified: false` and URL liveness is deferred to the Cite phase, which will use WebSearch per L-022 before falling back to archive.org.
