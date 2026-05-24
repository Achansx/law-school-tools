---
id: appendix-B
title: "AI Tooling — Prompts, Skills, and Plugins"
status: drafted
words: 1272
target_min: 1200
target_max: 1800
last_phase: harvest-appendix
last_run_at: 2026-05-28T17:00:00Z
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
provenance_note: >
  Vault-side source files (vault rubrics, vault RUNBOOK, vault LESSONS, plugin
  manifests) are not present in the article repository, which carries only
  Article/ and Article-Workplan.md. Per the project lesson on absent-source
  appendices, the verbatim excerpts below are reconstructed from the verified
  Section VI and VII evidence cards (each card carries the exact source quote
  and a verified flag), and the article-side prompts are quoted from in-repo
  Article/RUNBOOK.md. Each entry is tagged with its provenance.
---

# Appendix B: AI Tooling — Prompts, Skills, and Plugins

This appendix is reference material, not argument. It documents the prompts, skills, and connectors used to build the Constitutional Law vault and to write this paper. Every entry is labeled [vault], [article], or [both], and carries a provenance pointer. The recursion is intentional: this appendix documents the tooling that includes the harvest-appendix sub-task that wrote it.

## B.1 Prompts

### B.1.a Vault construction prompts (six-phase rotation) [vault]

The vault runs one phase per scheduled tick through a fixed rotation. Each phase has a procedure in the vault RUNBOOK and a separate scoring rubric.

> Ingest -> Lint -> Enrich -> Expand -> Synthesize -> Verify -> repeat
> (provenance: PROJECT_PRIMER, via evidence-07-six-phase-rotation)

| Phase | Prompt does | Provenance (evidence card) |
|-------|-------------|----------------------------|
| Ingest | Produces a deliberately under-completed skeleton brief; stubs everything else | evidence-06-ingest-skeleton-prompt |
| Lint | Structural and frontmatter hygiene pass | evidence-07-six-phase-rotation |
| Enrich | Resolves stubs: hypotheticals, dual-angle critique, added quotations | evidence-06-enrich-hypotheticals / -critique-balance |
| Expand | Adds connections, downstream links, target-existence checks | evidence-06-stub-marker-prompt-handoff |
| Synthesize | Builds exam-ready Topic pages from two-or-more briefs plus a lecture | evidence-06-synthesize-exam-readiness-prompt |
| Verify | Three adversarial personas, each forced to return a finding | evidence-06-verify-persona-prompts |

The pedagogical commitments live in the prompt text. Selected verified excerpts follow.

**Ingest under-completion** (vault RUNBOOK, Ingest Step 5; via evidence-06-ingest-skeleton-prompt):

```
- Fill at full depth ONLY: Memory Jogger, Facts, Procedural History,
  Judicial Votes, and Holding.
- Write a majority-only Analysis sketch of roughly 150 words.
- Put exactly one Midpage-verified pin-cited quotation in Key Quotations.
- Stub the remaining sections with single-line
  <!-- ENRICH: {one-sentence description} --> markers.
```

**Enrich distributional requirements** (vault RUNBOOK, Enrich Step 3; via evidence-06 cards):

```
- Hypothetical Applications: five hypos total (2 same-side, 2 opposite-side,
  1 fence-sitter). Each hypo needs fact pattern + reasoning.
- Critique: at least one progressive angle and one originalist/textualist
  angle, each grounded in a published critique or signposted argument.
```

**Enrich cardinal rule on verification** (vault RUNBOOK, Enrich; via evidence-06-midpage-quote-verification-prompt):

```
Never invent details; every filled stub traces to a PDF, a Midpage result,
or a web-search citation; Key Quotations are Midpage-verified text with
pin-cite URLs or they do not go in.
```

**The typed schema as the prompt contract** (vault Templates/Case Brief.md; via evidence-06-typed-schema-as-prompt). Every Ingest and Enrich run loads this nine-section H2 scaffold and is asked to fill it rather than to write a brief in whatever shape it prefers:

```
Memory Jogger / Facts / Procedural History / Judicial Votes / Holding /
Analysis (Majority, Concurrence, Dissent) / Hypothetical Applications
(Same-Side, Opposite-Side, Fence-Sitter) / Critique / Key Quotations /
Key Points / Connections / Sources
```

**Verify forced-finding** (vault PERSONAS.md; via evidence-06-verify-persona-prompts). Three personas (Staleness Auditor, Contradiction Hunter, Template Enforcer) run every pass, with run-count-keyed lead rotation:

```
Each must return at least one concrete finding per run. If a persona
genuinely finds nothing, it records `persona-produced-nothing` as its
own finding.
```

### B.1.b Article construction prompts (this paper’s meta-system) [article]

This paper is written by a second scheduled task with its own rotation, documented verbatim in the in-repo Article RUNBOOK. One phase runs per tick; the dispatcher reads state, honors gates, executes, scores, and advances.

> Harvest -> Outline -> Draft -> Cite -> Polish -> Stitch -> Verify -> repeat
> (provenance: Article/PROJECT_PRIMER.md)

| Phase | Directive (paraphrased from Article/RUNBOOK.md) | Provenance |
|-------|-------------------------------------------------|------------|
| Harvest | One evidence card per atomic fact; verified flag required | Article/RUNBOOK.md, Phase: Harvest |
| Outline | Heading spine with an `[evidence: ...]` pointer on every bullet | Article/RUNBOOK.md, Phase: Outline |
| Draft | House-voice prose; inline `[CITE: ...]` placeholders only | Article/RUNBOOK.md, Phase: Draft |
| Cite | Replace placeholders with Bluebook 21st footnotes; verify URL liveness | Article/RUNBOOK.md, Phase: Cite |
| Polish | No em dashes, curly quotes, voice unity, one idea per sentence | Article/RUNBOOK.md, Phase: Polish |
| Stitch | Cross-section consistency; adaptive interim vs. final assembly | Article/RUNBOOK.md, Phase: Stitch |
| Verify | Three personas, forced findings, P1-deferral until first pass | Article/RUNBOOK.md, Phase: Verify |

Two prompt-level sub-tasks ride inside the rotation. The Outline phase carries an abstract sub-task (draft toward 240 to 260 words, score against rubric/abstract.md, advance to review after three stable runs). The Harvest phase carries an appendix sub-task that fires once all fourteen sections reach `evidence_status: populated`; it selects the lowest-letter unfinished appendix and reproduces or writes it. The scheduled-task prompt run by the claude.ai routine also encodes the push-to-master protocol that keeps each tick off the ephemeral branch, the never-fabricate rule, and the gate logic that flips submission readiness to await a human and never submits. This very appendix is the appendix sub-task’s output, so the prompt that produced it is itself an entry in the table above.

## B.2 Claude Code skills

The two scheduled-task rotations are the repeatable agent routines that drive the project end to end; both are verifiable from in-repo artifacts. The Midpage verification protocol functions as a reused sub-routine invoked across phases.

| Routine | Source | Purpose | Label | Provenance |
|---------|--------|---------|-------|------------|
| Vault maintenance rotation | Scheduled task | Six-phase build and upkeep of the Con Law vault | [vault] | evidence-07-six-phase-rotation |
| Article maintenance rotation | Scheduled task | Seven-phase authoring of this paper | [article] | Article/RUNBOOK.md |
| Midpage quote-verification protocol | Sub-routine | Confirm every quotation against the indexed opinion | [both] | evidence-06-midpage-quote-verification-prompt; Article/LESSONS.md L-004 |

Intentionally excluded: the appendix scaffold names additional Claude Code skill categories used during early scaffolding and research (GSD project-orchestration skills, legal-research plugin skills such as case-brief and search_cases_by_concept, and Anthropic core skills such as scheduled-task-bootstrap, docx, pdf, and content-research-writer). Their manifests live in the Claude configuration outside the article repository and are not captured in the evidence cards, so they are listed here by category for completeness rather than reproduced; the article does not assert a verified invocation it cannot source.

## B.3 Plugins and MCP connectors

Connectors below are verified-invoked: each appears in an evidence card or LESSONS entry recording an actual call and its result.

| Connector | Tools used | Used for | Label | Provenance |
|-----------|-----------|----------|-------|------------|
| Midpage Legal Research (MCP) | search, findInOpinion, analyzeOpinion | Quote verification against indexed opinions; the Prize Cases / Grier catch | [both] | evidence-03/-06/-07; Article/LESSONS.md L-004 |
| CourtListener (MCP) | find_citing_cases, find_cited_cases | Citation chains; `cited_by` and `applied_in` frontmatter | [vault] | evidence-05-machine-readable-frontmatter-values; Workplan |
| Netlify (MCP) | manage-form-submissions (get/delete); netlify-deploy-services-updater (fallback) | Page-feedback intake loop; demoted deploy fallback that consumes build minutes | [vault] | evidence-08-feedback-form-loopback; evidence-09-netlify-cli-zero-build-minutes |
| WebFetch / WebSearch (built-in) | Fetch, search | Cite-phase URL liveness; live-site confirmation | [both] | Article/LESSONS.md L-022/L-052; evidence-01-corpus-snapshot-and-live-url |

The canonical deploy path is the Netlify CLI direct upload, preferred precisely because it does not consume Netlify build minutes; the Netlify MCP path is the documented fallback (provenance: evidence-09-netlify-cli-zero-build-minutes, DEPLOY.md Step 2).

Intentionally excluded: other legal plugins named in the scaffold (for example a case-search engine beyond Midpage and CourtListener) are not reproduced because no evidence card records a verified call. The Anthropic connectors available in the environment (Gmail, Google Calendar, IFTTT) were not invoked for vault or article work; the system never emails the professor, by design, so the Gmail connector in particular is present but deliberately unused.

The recursion noted at the top is real: the article’s method describes the system, this appendix exposes the system, and the system wrote this appendix. Sections III, VI, and VII cite this appendix.
