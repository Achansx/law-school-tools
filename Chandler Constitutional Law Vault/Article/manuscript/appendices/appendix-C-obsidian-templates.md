---
id: appendix-C
title: "Obsidian Note Templates"
status: drafted
words: 898
target_min: 500
target_max: 900
last_phase: harvest-appendix
source_files:
  - "<vault>/Templates/Case Brief.md"
  - "<vault>/Templates/Topic Page.md"
  - "<vault>/Templates/Lecture Summary.md"
  - "<vault>/PROJECT_PRIMER.md (Conventions, File Naming)"
provenance_note: "Reproduced from the three canonical template files in <vault>/Templates/ (now present in the repository checkout) plus the vault PROJECT_PRIMER conventions. Field lists and body sequences are quoted directly from those template files; nothing here is invented. Supersedes the prior reconstruction drafted when the Templates/ folder was absent."
---

# Appendix C: Obsidian Note Templates

The vault’s three content folders (`Cases/`, `Topics/`, `Lectures/`) are each backed by a canonical template in `Templates/` that fixes a YAML frontmatter schema and an ordered H2 body sequence. The templates are the schema source of truth; the build script and the vault Lint phase enforce conformance against them.

## C.1 Case Brief

- **Template:** `Templates/Case Brief.md`; pages live at `Cases/Case Name v Party (Year).md`.
- **Frontmatter** (28 fields, grouped as in the template):

```yaml
# Identity and indexing
case_name: ""        # equals the H1 and filename stem; no periods, "and" not "&"
citation: ""
year: ""
court: ""
doctrines: []
concepts: []
status: ""           # good law | superseded | overruled | limited | narrowed
treatment: ""        # Neutral | Positive | Negative | Cautionary
cited_by: ""         # integer from CourtListener; never guessed
midpage_id: ""
midpage_url: ""
verified: ""         # YYYY-MM-DD
source_files: []
# Holding-bar fields (rendered as a banner above the prose)
issue: ""
holding: ""
reasoning: ""
doctrine_family: ""  # Federalism | Separation of Powers | Individual Rights | Justiciability
# Citation metadata (Ingest fills the opinion face; Enrich completes)
argued: ""
decided: ""
panel: ""
author: ""
vote: ""             # "6-3", "9-0", "per curiam"
disposition: ""
# Authority lineage (Enrich fills from CourtListener)
relies_on: []
distinguishes: []
applied_in: []
overrules: ""
overruled_by: ""
```

- **Body (fixed H2 order):** Memory Jogger, Facts, Procedural History, Judicial Votes, Holding, Analysis (Majority required; Concurrence and Dissent optional), Hypothetical Applications (see C.4), Critique (progressive and originalist or textualist views), Key Quotations, Key Points, Connections, Sources.
- **Purpose:** the typed holding-bar and authority-lineage fields let the site render a structured banner and a citation graph without parsing prose; the fixed body order briefs every case to one standard.

## C.2 Topic / Doctrine Page

- **Template:** `Templates/Topic Page.md`; pages live at `Topics/Topic Name.md`.
- **Frontmatter** (12 fields):

```yaml
topic_name: ""           # equals the H1 and filename stem
area: ""                 # Federalism | Separation of Powers | Individual Rights | Justiciability
family: ""               # same four-value enum; drives the four-family grid column
constitutional_text: ""  # e.g. "Article I Section 8 Clause 3"; "n/a" if none
key_cases: []            # ordered most-to-least central
key_lectures: []
related_topics: []
exam_tested: ""          # true | false
verified: ""
source_files: []         # upstream Case/ and Lecture/ pages, not raw Source Materials
two_part_test: []        # optional spotlight "The test" list
open_questions: []       # optional spotlight "Open questions" list
```

- **Body (H2 order):** Overview, Governing Rule (the test in exam-ready language), Doctrinal Development (cases foundational-first, each back-linked to its brief), Key Cases table, an optional `## Comparison: <descriptor>` slot, Hypothetical Applications (see C.4), How to Spot on an Exam, Critique, Connections, Sources.
- **Purpose:** the synthesis form pulls every brief and lecture touching a doctrine into one doctrinal narrative, which is where the vault stops being a folder of briefs and becomes a study system.

## C.3 Lecture Summary

- **Template:** `Templates/Lecture Summary.md`; pages live at `Lectures/Lecture Title.md`.
- **Frontmatter** (12 fields):

```yaml
lecture_title: ""    # equals the H1 and filename stem
type: ""             # lecture | class-recap | review-session
topic_area: ""       # align with an existing Topics/ page name
theme: ""            # timeline-legend label; usually equals topic_area
week: null           # integer 1-14; drives the W## timeline column
cases_discussed: []
cases_covered: []    # canonical list used by the site redesign
date: ""
is_current: false    # true on the most-recent past lecture
is_upcoming: false   # true on future lectures (hollow timeline dot)
verified: ""
source_files: []     # usually one slide deck in Source Materials/
```

- **Body (H2 order):** Professor Emphasis, Lecture Outline, Cases Discussed table, Hypotheticals and Class Discussion, Key Takeaways, Connections, Sources.
- **Purpose:** preserves the live-class framing, reading order, and timeline position the casebook does not carry, so a student who missed a session can recover the professor’s emphasis.

## C.4 Hypothetical Applications block

A shared H2 embedded in both the Case and Topic pages, not a standalone template file. It carries five reasoned hypotheticals in three buckets: two Same-Side (the rule applied to fresh facts), two Opposite-Side (a single distinguishing fact flips the result), and one Fence-Sitter (genuinely contested). Each pairs a `**Hypo:**` fact pattern with a `**Why:**` line naming the controlling doctrinal move. It is the vault’s signature exam-preparation affordance.

## C.5 Cross-reference and provenance conventions

- Wiki-links take the form `[[folder/filename|Display Text]]`; the build emits anchor tags from them. Inside a table cell the display pipe must be escaped (`[[Cases/Foo\|Link]]`).
- Tags are lowercase-hyphenated and placed at file end before the closing `---` (`#con-law-i #case`, `#con-law-i #topic`, `#con-law-i #lecture`).
- Every page keeps its `source_files` frontmatter and its `## Sources` footer in lockstep. Cases and Lectures attribute upward to `Source Materials/` and render those entries as wikilinks the build rewrites into download links; Midpage opinion records stay as inline code because no file sits on disk. Topics attribute instead to the Case and Lecture pages consulted.
- The filename, the single H1, and the frontmatter name field (`case_name`, `topic_name`, `lecture_title`) must all agree, with no periods (`v Madison`, not `v. Madison`) and `and` rather than `&`. This three-way invariant lets the build resolve `[[Cases/Marbury v Madison (1803)]]` without normalization heuristics, and the Lint phase scores the agreement.

*Intentionally excluded:* there is no standalone Hypothetical template (the block lives inside the Case and Topic pages), and no aggregation template beyond the Topic synthesis form exists in `Templates/`.
