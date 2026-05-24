---
id: appendix-B
title: "AI Tooling — Prompts, Skills, and Plugins"
status: none
words: 0
target_min: 1200
target_max: 1800
last_phase: none
subsections:
  - B.1: "Prompts (vault and article)"
  - B.2: "Claude Code skills"
  - B.3: "Plugins and MCP connectors"
source_files:
  # Vault tooling
  - "<vault>/rubric/*.md"
  - "<vault>/LESSONS.md"
  - "<vault>/RUNBOOK.md"
  - "<vault>/.scheduled-task-prompt.md (if extracted)"
  # Article-build tooling (this paper's own meta-system)
  - "<vault>/Article/rubric/*.md"
  - "<vault>/Article/LESSONS.md"
  - "<vault>/Article/RUNBOOK.md"
  - "claude.ai routine config (JLE Article Maintenance)"
  # Plugins/connectors
  - "Claude Code plugin manifests for installed legal plugins"
  - "MCP connector list (Midpage, etc.)"
---

# Appendix B: AI Tooling — Prompts, Skills, and Plugins

<!-- TODO (Harvest appendix tick): Three subsections. Distinguish vault-building from article-building tooling throughout. Label each entry "[vault]" or "[article]" or "[both]".

## B.1 Prompts

Reference material for prompts used to build the Constitutional Law vault AND to write this paper. Document the prompt, its phase, what it does, and one example invocation.

### B.1.a Vault construction prompts (per the six-phase rotation)

For each of: Ingest, Lint, Enrich, Expand, Synthesize, Verify:
  - Prompt text (verbatim, in code block)
  - Phase rubric criteria (1-5 scale per criterion)
  - Critical lessons learned (selected entries from vault LESSONS.md)

### B.1.b Article-building prompts (the paper's own meta-system)

For each of: Harvest, Outline, Draft, Cite, Polish, Stitch, Verify, plus the dispatcher and gate logic:
  - Prompt text from <vault>/Article/RUNBOOK.md
  - The scheduled-task prompt run by the claude.ai routine
  - The abstract sub-task prompt
  - The appendix sub-task prompt (this very task)

## B.2 Claude Code skills

List of skills used in vault construction and article writing. For each:
- Skill name
- Source (built-in, plugin, custom)
- Purpose
- Example trigger
- [vault] / [article] / [both]

Notable categories:
- **GSD skills** for project orchestration (used for early vault scaffolding)
- **Legal research skills** in the law-student and ip-legal plugins (case-brief, search_cases_by_concept)
- **Vault maintenance skill** (vault-maintenance:maintain-vault) [vault]
- **Anthropic core skills** (scheduled-task-bootstrap, docx, pdf, content-research-writer) [both]
- **Article maintenance** (the scheduled task running this paper) [article]

## B.3 Plugins and MCP connectors

For each installed plugin or MCP connector used in vault or article work:
- Name
- Source URL or marketplace
- Tools it exposes
- What it was used for in the vault or article
- [vault] / [article] / [both]

Categories to cover:
- **Legal plugins** (law-student, ip-legal, commercial-legal, etc.) — most are vault-related
- **Descrybe Legal Engine** (case search, quotation verification) [vault]
- **Midpage Legal Research** MCP (analyzeOpinion, findInOpinion, search) [both — vault use + article cite verification]
- **CourtListener** MCP for citation chains [vault]
- **WebFetch / WebSearch** built-in [both]
- **Anthropic connectors** (Gmail, Calendar, IFTTT) — note which were actually invoked
- **Netlify** MCP for site deploy [vault]
- **Google Drive** if used for any document handoff [if applicable]

Note on the recursive nature: this appendix documents tools that include the tools used to write this appendix. That is intentional. The article's method describes the system, the appendix exposes the system, the system wrote the appendix.

Footnote anchors: Sections III (case study), VI (prompting as pedagogical design), VII (iterative improvement) all cite this appendix.
-->
