---
section: "05"
fact_type: statistic
source_path: "Chandler Constitutional Law Vault/Article-Workplan.md"
source_url: "https://arxiv.org/abs/2311.17696"
verified: false
notes: "External anchor for Section V's claim that schema (not prose alone) is what makes AI-authored notes pedagogically reusable. The workplan bibliography records that Dong, Yuan, Chen, Cheng, and Wen show knowledge graphs outperformed pure semantic RAG in a controlled study of 76 students (mean scores 6.37 vs 4.71, p<0.001, Cohen's d=0.86). The article should deploy this as the external comparison for the Obsidian vault. URL verification deferred to the Cite phase per L-005; WebFetch in this scheduled-task run is blocked by provenance, mirroring the PI-005 situation in Section 04. The Cite phase will verify URL liveness and may need an archive.org capture if the arXiv link drifts."
---

The Dong et al. KG-RAG paper (arXiv:2311.17696, v7 published Feb. 12, 2025) is the external anchor for Section V's claim that schema is the load-bearing element of an AI-authored knowledge base, not prose quality alone. Per the workplan bibliography, Dong, Yuan, Chen, Cheng, and Wen ran a controlled study of 76 students comparing a knowledge-graph-augmented retrieval system against pure semantic RAG and found mean scores of 6.37 versus 4.71 (p<0.001, Cohen's d=0.86 — a large effect by conventional thresholds). The article should deploy this as the external evidence that structuring a corpus through a schema (whether automatic knowledge graph extraction or manual Obsidian wiki-linking) produces meaningfully better pedagogical retrieval than treating the corpus as a flat semantic embedding space.

Exact source quote, `Chandler Constitutional Law Vault/Article-Workplan.md` annotated bibliography entry under "Knowledge graphs and RAG for education (Sections V, VI, VIII)":

> **Chenxi Dong, Yimin Yuan, Kan Chen, Shupei Cheng & Chujie Wen, *How to Build an Adaptive AI Tutor for Any Course Using Knowledge Graph‑Enhanced Retrieval‑Augmented Generation (KG‑RAG)*, arXiv:2311.17696 (v7, Feb. 12, 2025).** Knowledge graphs outperformed pure semantic RAG in a controlled study (76 students; mean scores 6.37 vs. 4.71, p<0.001, Cohen's d=0.86). Deploy in Section V to support the claim that *schema* (not just prose) is what makes AI‑authored notes pedagogically reusable. https://arxiv.org/abs/2311.17696.

Verification gap: URL liveness was not checked in this Harvest run because WebFetch refused the URL by provenance (the URL appears in the workplan but not in a user message). Cite phase needs to confirm and, if dead, substitute an archive.org capture. Same provenance failure pattern as Section 04's PI-005.
