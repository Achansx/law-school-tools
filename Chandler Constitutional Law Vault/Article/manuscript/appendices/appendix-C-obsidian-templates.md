---
id: appendix-C
title: "Obsidian Note Templates"
status: drafted
words: 776
target_min: 500
target_max: 900
last_phase: harvest-appendix
source_files:
  - "<vault>/Templates/"
  - "<vault>/PROJECT_PRIMER.md (frontmatter conventions section)"
provenance_note: "The <vault>/Templates/ folder was not included in this repository checkout. The schemas below are reconstructed from the verified Section V evidence cards (frontmatter-schemas, case-brief-nine-section-standard, topic-synthesis-form, doctrine-family-enum, wikilink-conventions, filename-and-h1-discipline) and from populated instance pages audited in April 2026 (Marbury v Madison, Judicial Review, Commerce Clause). Each entry names its provenance; nothing here is invented."
---

# Appendix C: Obsidian Note Templates

The vault’s three content folders (`Cases/`, `Topics/`, `Lectures/`) are each backed by a canonical template in `Templates/` that fixes a YAML frontmatter schema and an H2 body sequence. The schemas below are reconstructed from the Section V evidence cards and from populated instance pages, because the `Templates/` source folder was absent from this checkout.

## C.1 Case Brief

- **File path:** `Templates/Case Brief.md`; pages live at `Cases/Case Name v Party (Year).md`.
- **Frontmatter schema** (~30 fields; abbreviated, verbatim from the template):

```yaml
case_name: "{{Case Name}}"
citation: "{{Volume}} {{Reporter}} {{Page}}"
year: "{{Year}}"
doctrines: ["{{Doctrine 1}}"]
concepts: ["{{Concept 1}}"]
status: "{{good law | superseded | overruled | limited | narrowed}}"
midpage_id: "{{Midpage opinion ID}}"
midpage_url: "{{Midpage URL}}"
verified: "{{YYYY-MM-DD}}"
# Holding-bar fields (site renders these as a banner above the prose):
issue: ""
holding: ""
reasoning: ""
doctrine_family: ""   # exactly one of: Federalism | Separation of Powers | Individual Rights | Justiciability
# Authority lineage (Enrich fills from the opinion + CourtListener):
relies_on: []
distinguishes: []
applied_in: []
overrules: ""
overruled_by: ""
```

- **Body structure** (fixed H2 sequence): Memory Jogger (one-sentence essence), Facts, Procedural History, Judicial Votes, Holding, Analysis (Majority required; Concurrence and Dissent optional), Hypothetical Applications (see C.4), Critique (progressive and originalist or textualist views), Key Quotations, Key Points, Connections, Sources.
- **Example wikilink:** `[[Cases/Marbury v Madison (1803)|Marbury v Madison]]`.
- **Pedagogical purpose:** the typed frontmatter lets the site render a holding bar, a citation count, and an authority-lineage graph without parsing prose, while the fixed body sequence guarantees every case is briefed to the same standard.

## C.2 Topic / Doctrine Page

- **File path:** `Templates/Topic Page.md`; pages live at `Topics/Topic Name.md`.
- **Frontmatter schema** (verbatim from the Judicial Review instance):

```yaml
key_cases:
  - "Marbury v Madison (1803)"
  - "The Prize Cases (1863)"
key_lectures:
  - "Marbury v Madison - Judicial Review"
related_topics:
  - "Separation of Powers"
area: ""    # same four-value enum as doctrine_family
family: ""
```

- **Body structure:** Overview, Governing Rule (the test in exam-ready language), Doctrinal Development (cases in analytical order, foundational first, with a back-link to each brief), Key Cases table, Hypothetical Applications (see C.4), exam-spotting framework, Critique.
- **Example wikilink:** `[[Topics/Commerce Clause|Commerce Clause]]`.
- **Pedagogical purpose:** the synthesis form pulls every brief and lecture touching a doctrine into one doctrinal narrative, which is where the vault stops being a folder of briefs and becomes a study system.

## C.3 Lecture Summary

- **File path:** `Templates/Lecture Summary.md`; pages live at `Lectures/Lecture Title.md`. (Schema reconstructed from the populated Marbury lecture instance, not the template file.)
- **Frontmatter schema:**

```yaml
lecture_title: "{{Lecture Title}}"
type: "lecture"
topic_area: "{{Doctrine area}}"
cases_discussed: ["{{Case (Year)}}"]
date: "{{YYYY-MM-DD}}"
verified: "{{YYYY-MM-DD}}"
source_files: ["Source Materials/{{lecture}}.pptx"]
```

- **Body structure:** a Professor Emphasis block (how the professor frames the case in class) followed by a Lecture Outline that walks the session in the order it was delivered.
- **Example wikilink:** `[[Lectures/Marbury v Madison - Judicial Review|Lecture: Marbury v Madison]]`.
- **Pedagogical purpose:** preserves the live-class framing, reading order, and through-lines that the casebook does not carry, so a student who missed a session can recover the professor’s emphasis.

## C.4 Hypothetical Applications block

This is a shared sub-block embedded in both Case and Topic pages, not a standalone template file. It carries five reasoned hypotheticals in three buckets: two Same-Side (the doctrine applied to fresh facts), two Opposite-Side (a single distinguishing fact flips the result), and one Fence-Sitter (genuinely contested). Each closes with a one-sentence Why naming the controlling doctrinal move. It is the vault’s signature exam-preparation affordance.

## C.5 Cross-reference and provenance conventions

- Wiki-links take the form `[[folder/filename|Display Text]]`; the build emits anchor tags from them.
- Tags are lowercase-hyphenated and placed at file end before the closing `---` (`#con-law-i #case`, `#con-law-i #topic`, `#con-law-i #lecture`).
- Every page keeps a `source_files` frontmatter list and a `## Sources` footer in lockstep; Cases and Lectures attribute upward to `Source Materials/`, Topics to the Case and Lecture pages consulted.

*Intentionally excluded:* there is no standalone Hypothetical template (the block lives inside Case and Topic pages), and no aggregation template beyond the Topic synthesis form is present in the evidence.

## Filename and H1 discipline

The vault enforces a strict three-way invariant: the frontmatter name field (`case_name`, `topic_area`, `lecture_title`), the file’s single H1, and the filename stem must all agree, with no periods (`v Madison`, not `v. Madison`) and `and` rather than `&`. This is the smallest structural commitment that produces vault-wide consistency, because it lets the build script resolve `[[Cases/Marbury v Madison (1803)]]` to a file without normalization heuristics. The vault Lint phase scores filename, H1, and frontmatter-name agreement as part of its template-enforcement check.
