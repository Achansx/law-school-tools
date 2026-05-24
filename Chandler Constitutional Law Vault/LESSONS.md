# Vault Maintenance Lessons

Accumulated gotchas, workarounds, and patterns discovered across maintenance runs.

**Entry cap: 35.** When at or above the cap, do NOT append new lessons. Log the candidate to `pending_issues` with `type: lesson-candidate` and let the next Consolidate sweep merge duplicates and prune superseded entries.

**Entry shape (60 words max).** Rule, one sentence. **Why:** consequence or root cause. **How to apply:** the concrete check, command, or trigger. _Seen:_ italic footer with up to three dated instances; drop the oldest when adding a fourth.

**Loaded only for content-editing phases.** The scheduled task reads this file during Ingest, Enrich, Expand, and Synthesize. Lint and Verify skip it unless a phase-verify persona specifically needs it.

**Consolidate sweep.** See RUNBOOK.md "Phase: Consolidate (out-of-rotation)". Triggers: 3+ lesson-candidates queued; OR `last_consolidation` missing or >21 days; OR >7 days AND 30+ entries (`sed -n '/^## /,$p' LESSONS.md | grep -c '^\*\*'`, excluding bold header notes).

**Archive policy.** Archived snapshots under `archive/LESSONS_YYYY-MM-DD.md` are append-only and never pruned from disk; entries are merged back into this file on reconciliation passes rather than deleted. The 2026-04-20 reconciliation confirmed every archived lesson is represented here in its current form.

## Source Material Ingestion

**PDF extraction quality varies wildly.** Some PDFs are scanned images with no selectable text; others are well-structured. **Why:** generating a brief from garbled text wastes a full cycle. **How to apply:** spot-check extracted text before creating the page; if extraction fails, log to `pending_issues` rather than writing garbage.

**PPTX slides are outlines, not prose.** Lecture decks are bullets. **Why:** dumping raw slide text produces unreadable lecture pages. **How to apply:** expand bullets into coherent prose; use slide structure to follow the professor's analytical flow.

**Distinguish case readings from lecture slides by filename.** PDFs with case names (e.g. `Marbury_v__Madison.pdf`) are case readings → Case Brief. PPTXs/PDFs with topic names (e.g. `Enumerated Powers New Deal.pptx`) are lectures → Lecture Summary. Supplemental files (rubrics, quiz answers) get skipped.

**Sources footer order must match `source_files` YAML exactly.** PDF first, Midpage second, every time. **Why:** divergent order breaks Lint check 11 and creates a recurring sync defect. **How to apply:** write the footer in the same order as the YAML on first pass. _Seen: 2026-04-22T20:15Z (5 briefs corrected post-hoc)._

**Skip byte-identical `-N` numbered companion PDFs in the auto_apply bucket.** The matcher surfaces files like `foo-1.pdf` next to `foo.pdf`. **Why:** auto-applying duplicates pollutes `source_files`. **How to apply:** before adding any candidate that differs from an existing entry only by a trailing `-N`, compare md5 (or size+mtime) and skip if identical. Durable fix: byte-identity post-filter in `.site/match_sources.py`. _Seen: 2026-04-23 (Michael H, Texas v Johnson)._

## Content Editing

**Match house style: prefer commas, colons, parentheses, sentence breaks over em dashes.** Especially on Topic pages and Synthesize outputs. **Why:** em dashes mismatch user preference and require post-hoc cleanup. **How to apply:** read the file before inserting; draft clean rather than fixing after. _Seen: 2026-04-17T11:00Z (Separation of Powers Topic, 6 dashes corrected)._

**Do not invent case details.** If the vault lacks context, log to `pending_issues` rather than guess. Fabricated holdings are worse than gaps.

**Case briefs must hit the 9-section case-briefer standard.** Memory Jogger, Facts, Procedural History, Judicial Votes, Holding, Analysis (with concurrence/dissent breakouts), Hypothetical Applications, Critique, Key Quotations. Landmarks get full treatment; supporting cases scale down. Each Hypothetical Application must include analysis, not just facts.

**Synthesize prioritizes new Topic pages over revising existing ones when `orphan_links` lists unsynthesized Topics.** **Why:** only creations move the orphan counter down. **How to apply:** before drafting, diff `orphan_links` against `Topics/`; route the run to orphan Topics with the strongest case+lecture anchor support already in place. _Seen: 2026-04-17T17:00Z (Federalism, SDP, P&I; 5.00 weighted)._

**Governing Rule blockquotes on Topic pages must distinguish verbatim opinion text from paraphrased rules.** Verbatim → carries an inline pin-cite URL. Paraphrase → begins with `**Rule:**` or the doctrine name and avoids quotation-style sentence-final phrasing. **Why:** without typographic distinction, readers can't tell verified quotes from editorial restatements. **How to apply:** Lint greps for Governing Rule blockquotes lacking pin-cites and flags for review.

## Structural Integrity

**Obsidian rendering is strict on tables and horizontal rules.** Pipe tables need a `|---|---|` separator after the header; `---` separators need blank lines above and below. **Why:** missing separators stop tables rendering and turn HRs into heading underlines. **How to apply:** add the separator/blank lines and confirm in preview before closing.

**Filename, H1, frontmatter, H2 banners, BUILD_NARRATIVE H2 headings, and YAML closing delimiters must match templates exactly.** Six places template exactness shows up:
1. Filename: drop periods in "v.", use "and" not "&" (e.g. `Cases/McCulloch v Maryland (1819).md`).
2. H1 equals filename stem.
3. Frontmatter `case_name`/`topic_name`/`lecture_title` equals H1 (minus year for cases).
4. H2 banners copied verbatim from `Templates/*.md`, never paraphrased (e.g. `## Hypotheticals and Class Discussion`, not `## Hypotheticals`).
5. BUILD_NARRATIVE run blocks need `## {timestamp} — {Phase} ({label})` H2; heading-less appends become invisible to the Obsidian outline.
6. Closing YAML `---` must be on its own line. The `pdf"---` / `pptx"---` glued-delimiter defect is a recurring Ingest bug Lint must grep for.

**How to apply:** Ingest copies banners character-for-character; Lint normalizes any divergence; every phase prefixes its BUILD_NARRATIVE append with a proper H2. _Seen: 2026-04-17T14:00Z (4 lectures, `## Hypotheticals` banner); 2026-04-24T03:41Z and 04:13Z (Loving, Sherbert, Dames and Moore glued YAML)._

## Cross-References

**One link per reference per file.** Wiki-link the first mention only; keep subsequent mentions plain.

**Asymmetric Connections need a post-Enrich reciprocity audit.** **Why:** Ingest writes one-way Connections (A→B, not B→A); Enrich-from-lecture briefs and Lecture→Case links extend the asymmetry. **How to apply:** as Expand's opening move, walk each new brief's Connections and verify reciprocity; annotate Lecture↔Case reciprocals with the direction of reference. _Seen: 2026-04-17T16:00Z (Palko, Duncan, Timbs, Martin v Hunter's Lessee → 7 reciprocals fixed)._

**Wiki-link targets must match the full filename stem, not the visible alias.** **Why:** Obsidian renders a broken link cleanly when the alias looks right (e.g. `[[Cases/Bruen (2022)|Bruen]]` works visually even if no file matches the stem). **How to apply:** before inserting any `[[link]]`, glob the target stem; or run `grep -o '\[\[Cases/[^|]*' -r Cases/ | sort -u` and cross-check against `ls Cases/`.

**Ingest skeletons must always carry an ENRICH stub in Connections, not pre-filled wiki-links.** **Why:** filling Connections at Ingest bypasses Expand's target-existence check and seeds broken links. **How to apply:** drop a `<!-- ENRICH: ... -->` marker noting intended connections; let Expand verify and add. _Seen: Learning Resources Inc v Trump (4 wiki-links, 3 to non-existent files)._

**Key Quotations drift across files — grep before closing a quote correction.** **Why:** the same canonical quote often appears in a brief AND in Topic pages; correcting one place leaves the others stale. **How to apply:** `grep -rn "<distinctive phrase>" <vault-root>` for a fragment unique enough to catch every copy, patch every hit, grep again. Applies to Enrich, Verify, Synthesize. _Seen: Prize Cases ("formally"→"solemnly", "by its character"→"by its accidents") fixed in brief, had to be re-applied to War Powers Topic._

## Absolute Paths

**Always use absolute paths directly. Never glob for the vault root or plugin skills folder.** Globbing with relative or `**/` patterns regularly fails to find these locations. Direct paths:

- **Vault root (file tool):** `/Users/alan/Library/Mobile Documents/com~apple~CloudDocs/Projects/claude/Chandler Constitutional Law Vault`
- **Vault root (bash):** derive via `find /sessions -maxdepth 3 -name 'Chandler Constitutional Law Vault' -type d | head -1`. The `/sessions/...` prefix changes between sessions; never hardcode it.
- **vault-maintenance plugin skills:** `/Users/alan/Library/Application Support/Claude/local-agent-mode-sessions/f2444ed0-6dc2-46fc-ad70-8d07f325fccb/e8303104-cf83-46a4-b6e6-b5c3e6677dac/rpm/plugin_01T6tZ2Tk7CA5qZaAtAErx6g/skills/vault-maintenance/references/`
- **adversarial-verify skill:** `/Users/alan/Library/Application Support/Claude/local-agent-mode-sessions/f2444ed0-6dc2-46fc-ad70-8d07f325fccb/e8303104-cf83-46a4-b6e6-b5c3e6677dac/rpm/plugin_01HbQhHXd8tJaTkoD28mZnhY/skills/adversarial-verify/SKILL.md`
- **Per-phase rubrics:** `<vault>/rubric/<phase>.md` (legacy `RUBRIC.md` archived at `rubric/_archive-RUBRIC-all-phases.md`).
- **Templates:** `<vault>/Templates/`
- **Source Materials:** `<vault>/Source Materials/`

The session-scoped portion may change between sessions. If a path fails, re-derive via `find /sessions -maxdepth 5 -name 'phase-verify.md' 2>/dev/null`.

## Environment and Tooling

**Edit tool requires exact string matching.** Always Read a file immediately before editing. **Why:** stale context causes Edit to fail. **How to apply:** Read → Edit; if many edits, re-read between batches.

**Batch size matters; PPTX extraction writes one file per deck.** Process 10–15 files per phase max. **Why:** larger batches risk context overflow; combined PPTX stdout exceeds bash response limits (~130k chars / 8 decks). **How to apply:** install via `pip install python-pptx --break-system-packages`; write each deck to `outputs/pptx_{stem}.txt`; read each with offset/limit.

**PDF reads have a ~20-page limit per request.** For longer docs, read in page ranges; large merged PDFs need multiple passes.

**Enrich budget outcomes (no-op or schema-sweep-only) are valid signals, not bugs.** **Why:** caught-up corpus produces a no-op (zero `<!-- ENRICH: -->` stubs, zero `pending-enrich` briefs); the mandatory 10-case schema sweep consuming the whole tick produces sweep-only (no analytical-stub time left). **How to apply:** record the outcome, advance `next_phase` to expand, do not widen scope. Two consecutive same-shape runs trigger review: no-op routes to a `Source Materials/` check; sweep-only routes to the RUNBOOK split proposal (enrich-schema vs enrich-analytical variants — schema tick when priority queue empty AND strong-bucket score=6/7 set ≥5 cases; analytical tick caps the sweep at 3 cases). _Seen: 2026-04-17T00:09Z (no-op x2); 2026-05-01T04:43Z and T12:09Z (sweep-only x3 in 24h, regression-test set)._

**`next_phase` must advance after every phase run.** **Why:** stale value causes the wrong phase to re-run. **How to apply:** after writing state, confirm `next_phase` does not equal the phase just completed; if it does, treat as a state-sync bug and rewrite. Exception: failed Deploy intentionally keeps `next_phase: deploy` for retry. _Seen: 2026-04-22 (Verify ran twice on different files)._

**Clear `.phase-in-progress` via truncate, not `rm`.** The marker lives on iCloud and carries a flag that blocks `rm` (Python and bash both fail with "Operation not permitted") but permits truncate/overwrite. **How to apply:** clear with `: > .phase-in-progress` (or Python `open(path, 'w').close()`); marker-read logic must treat 0-byte/malformed-JSON as "no phase in progress". RUNBOOK marker-remove uses truncate. _Seen: 2026-04-24 (Verify 15:14Z, Deploy 15:51Z both blocked rm)._

## Legal Research Tools

**Midpage `analyzeOpinion` returns `treatment.citedBy` counts.** More reliable than CourtListener's `find_citing_cases`, which paginates without a total in the response body.

**Midpage `treatment` is usually Neutral, not Positive, for landmark cases.** **Why:** foundational cases get cited on both sides. **How to apply:** never assume Positive — always verify with Midpage. _Seen: McCulloch, Youngstown, Heller, Prize Cases all classified Neutral._

**Midpage and CourtListener share opinion IDs for historical SCOTUS cases.** A Midpage ID resolves directly in CourtListener `find_cited_cases`/`find_citing_cases` without separate lookup. CourtListener text search may miss pre-1900 cases that exist by ID — bypass text search and query by shared opinion ID. _Seen: Prize Cases (87541) zero text-search hits, immediate ID resolution; same for McCulloch (85272), Youngstown (105018)._

**`analyzeOpinion` is the escalation tool when `findInOpinion` fails, and the right first call on pre-1900 opinions.** `findInOpinion` does keyword/near-exact search and breaks on OCR artifacts; `analyzeOpinion` uses AI semantic location and finds passages despite distortion. **How to apply:** if `findInOpinion` returns zero for text you believe is in the opinion — or the opinion is pre-1900 — call `analyzeOpinion` with a targeted question before logging unverifiable. _Seen: Youngstown Jackson "sinister and alarming" (lines=649) recovered after two prior `findInOpinion` zeros._

**Creating a case brief from vault-internal lecture content is a valid Enrich strategy when an orphan link exists and detail suffices.** **Why:** a lecture covering all 9 sections plus Midpage metadata produces a better brief than raw PDF extraction would, without waiting for the next Ingest cycle. **How to apply:** create at Enrich if the lecture hits all 9 sections; wait for Ingest if the lecture is a stub.

**Modernized PDFs are preferred reading; never extract Key Quotations from them or from the reporter syllabus.** **Why:** modernized text silently updates archaic phrasing; the syllabus presents the same trap (clean-looking but verbatim-different). **How to apply:** at Ingest, call `analyzeOpinion` for the precise quotation and pin-cite, copy returned text verbatim. At Verify, call `analyzeOpinion` (not `findInOpinion`) and compare word-for-word. _Seen: Fulton v City of Philadelphia (syllabus's "creating a mechanism" instead of body's "providing a mechanism for individualized exemptions")._

**Expand requires CourtListener citation calls; substitute Midpage `analyzeOpinion` and dock one point when CourtListener is unavailable.** **Why:** prose-only Expand runs score ~0.7 lower because `citation_chain_used` craters; CourtListener surfaces connections prose misses. **How to apply:** every Expand makes ≥1 CourtListener call per in-scope case, OR documents in run notes why the citation chain was already exhausted. Fallback: if CourtListener tools aren't surfaced, use Midpage `analyzeOpinion` for prior-authority signals and citing-case names; dock `citation_chain_used` by 1. _Seen: 2026-04-22T06:00Z (VMI, Hernandez, Geduldig via Midpage substitute, scored 4 not 5)._

**Youngstown's concurrent opinion structure has three tiers.** Black wrote the opinion of the Court; Frankfurter and Douglas joined AND wrote separate concurrences expanding their reasoning; Jackson, Burton, and Clark concurred in the judgment only via separate opinions. Vinson dissented, joined by Reed and Minton. **How to apply:** when briefing cases with this structure, distinguish (a) joined the opinion, (b) joined and wrote separately, (c) concurred in judgment only. _Seen: Frankfurter's "I join his opinion because I thoroughly agree" (Verify 2026-04-17T12:00Z)._

**Ingest combined cap = 10 across new files + Step 8 backfills, even in burst mode.** Backfill budget = `max(0, 10 - new_files_count)`. Exception: when Steps 1–7 produce zero new files, the backfill-only ceiling rises to 15. **Why:** crossing the cap triggers `scope_discipline 0` (run score 4.5 instead of 5.0). _Seen: 2026-04-22T18:45Z (8 new + 3 backfill = 11 → red flag)._

## Deployment

**Deploy: prefer `fast_deploy.py`; CLI cold-start risks the 45s cap; `--no-build` is required; never use naive urllib; verify SPA pages via `pages.json`, not the index.html shell; account-credit exhaustion is non-recoverable without human action.** Five patterns:
1. `.site/fast_deploy.py` walks `dist/`, POSTs the manifest, uploads only required bytes, calls finalize. Completes in ~6s, fits inside the 45s cap. First-choice path in `DEPLOY.md` ahead of the CLI.
2. CLI cold-start (`npx -y netlify-cli deploy`) regularly exceeds 45s during sandbox-wake npx priming. Use `fast_deploy.py` first; CLI is fallback only. Always pass `--no-build` even when `netlify.toml` has `command = ""`, otherwise the CLI errors with "Error while running build".
3. Do NOT re-implement the digest API with naive urllib that POSTs a manifest and PUTs files without finalize: Netlify needs a finalize signal that the public REST docs don't describe; naive scripts produce zombie deploys stuck in `state=uploading`.
4. SPA hash-routed sites (e.g. `constitutionallaw.netlify.app/#/p/<id>`) return the same `index.html` shell on every page-id GET, so DEPLOY.md Step 3.5a's literal "title in body" check fails 8/8 on a healthy deploy. Verify titles by matching the live `pages.json` id+title against the local manifest, not by string-searching the response body.
5. HTTP 403 "Account credit usage exceeded" on POST /sites/{id}/deploys is an external block, not a code defect. Build still succeeds; upload aborts before any deploy record is created (no zombie cleanup). Live `manifest.json` returns 503 with `usage_exceeded` until human adds credits or upgrades. RUNBOOK guard: when `consecutive_same_type_failures>=3` AND `type=deploy-credit-blocked`, log a one-line CHANGELOG note and SKIP the fast_deploy POST until credits are restored, to avoid burning wall clock on a foreseeably-failing call.
_Seen: zombie deploys (IDs 69e808…, 69e808…, 69e809…); 2026-05-01T03:41Z and T10:14Z (fast_deploy.py path used after CLI cold-cache 45s timeout); 2026-05-01T10:14Z (3.5a SPA semantics surfaced); 2026-05-07T18:41Z, T19:11Z, T19:42Z (credit-block 3-strike threshold, build 131/53/97/281 each, upload blocked)._
