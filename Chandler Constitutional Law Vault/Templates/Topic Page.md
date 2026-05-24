---
topic_name: "{{Topic Name}}"
area: "{{e.g., Federalism | Separation of Powers | Individual Rights | Justiciability}}"
family: "{{Federalism | Separation of Powers | Individual Rights | Justiciability}}"
constitutional_text: "{{e.g., Article I Section 8 | Fourteenth Amendment Section 1}}"
key_cases:
  - "{{Case Name (Year)}}"
  - "{{Case Name (Year)}}"
key_lectures:
  - "{{Lecture Title}}"
related_topics:
  - "{{Related Topic}}"
exam_tested: "{{true | false}}"
verified: "{{YYYY-MM-DD}}"
source_files:
  - "Cases/{{Case Name (Year)}}.md"
  - "Lectures/{{Lecture Title}}.md"

# Spotlight fields (optional but encouraged). The deployed site renders the
# spotlighted Topic with a two-part-test sidebar and an open-questions list.
two_part_test: []     # List of strings, one per test step. Leave empty if doctrine isn't a multi-prong test.
open_questions: []    # List of strings, one per open question.
---

<!--
FRONTMATTER POPULATION GUIDE (delete this comment block when creating a real page)

topic_name           Short canonical name, Title Case, no trailing punctuation. Must equal the H1 and filename stem. Example: "Commerce Clause", "Standing Doctrine".
area                 Top-level bucket: Federalism | Separation of Powers | Individual Rights | Justiciability. One value, no list.
family               Same four-value enum as `area`. Drives which family color column the Topic appears under in the deployed site's four-family grid. Usually equal to `area`; set explicitly so the site doesn't fall back to build.py's keyword bucketer.
two_part_test        Optional. YAML list of strings, one per test step. Renders as the spotlight sidebar's "The test" ordered list when this Topic is the dashboard / index spotlight. Empty list when the doctrine is not a multi-prong test.
open_questions       Optional. YAML list of strings, one per open question. Renders as the spotlight sidebar's "Open questions" list. Use to capture genuinely open doctrinal points (Loper Bright × MQD, etc.), not exam-hypotheticals.
constitutional_text  Specific anchor: "Article I Section 8 Clause 3", "Fourteenth Amendment Section 1". If none, write "n/a" in quotes.
key_cases            Ordered most-to-least doctrinally central. Each entry "{Case Name} ({Year})". Must have a corresponding Cases/ page before Synthesize can finalize.
                     Placeholder convention: if a canonical case for this Topic does not yet have a Cases/ brief, list it anyway and append an inline YAML comment on
                     the same line, e.g. `- "Gibbons v Ogden (1824)"            # no brief yet, developed in Lectures/Gibbons v Ogden`. Add a block comment
                     directly above the `key_cases:` key noting that listed entries lacking briefs are placeholders awaiting an Ingest run. Lint treats
                     unbriefed entries flagged with the inline comment as acknowledged gaps rather than broken links; Synthesize cannot finalize until the
                     placeholder entries have corresponding Cases/ pages.
key_lectures         Lecture pages where this topic is primarily developed. Each entry is the Lectures/ filename stem (no folder, no extension). Omit or leave empty if no lecture directly maps to the topic. Optional field.
related_topics       Cross-links to other Topics pages. Targets must exist; Lint will flag orphans.
exam_tested          true | false. Derive from lecture emphasis or explicit professor statement. Default false when unknown.
verified             Today's date YYYY-MM-DD. Update whenever the topic is re-checked against its source case briefs.
source_files         YAML list of DIRECT-INPUT Case/ and Lecture/ wiki pages that fed this Topic. Direct inputs only: the briefs and lecture summaries actually consulted to draft this page, not every Case wiki-linked in passing. Each entry is a vault-relative path ending in `.md`, e.g. "Cases/McCulloch v Maryland (1819).md" or "Lectures/Gibbons v Ogden - Commerce Clause Foundations.md". Must stay in sync with the ## Sources footer section. For Topics, this is an attribution trail of upstream wiki pages, not raw Source Materials.
-->

# {{Topic Name}}

## Overview

Governing rule or test. Constitutional text. Historical development. Where this doctrine fits in the Con Law I structure.

---

## Governing Rule

> **Rule:** Statement of the governing rule or test in exam-ready language.

---

## Doctrinal Development

Case-by-case analysis drawing from the case brief pages. Present in analytical order (foundational case first, then refinements, then limitations). Summarize holdings and link back to the case brief for full treatment.

### {{Foundational Case}}

Summary of holding and significance. See [[Cases/Case Name|full brief]].

### {{Refining Case}}

How this case extended or clarified the doctrine. See [[Cases/Case Name|full brief]].

---

## Key Cases

| Case | Year | Holding | Brief |
|------|------|---------|-------|
| **Case Name** | Year | Brief holding | [[Cases/Case Name\|Link]] |
<!-- PIPE ESCAPE: Wikilinks inside a Markdown table cell MUST escape the display-text pipe as `\|` (e.g. `[[Cases/Foo\|Link]]`). An unescaped `|` ends the table cell early and breaks the row. Outside tables (e.g., in the Connections and Sources bullet lists below) the plain `|` form is fine. -->


---

<!--
OPTIONAL SCHEMA-SANCTIONED SECTION: Comparison / Doctrinal Contrast
Between Key Cases and Hypothetical Applications a Topic page MAY insert one or more
H2 sections that supply synthesis tables or cross-topic contrasts. The canonical heading
form is "## Comparison: <descriptor>" (e.g., "## Comparison: MQD versus Nondelegation",
"## Comparison: Enumerated, Implied, and Necessary and Proper", "## Comparison: Palko,
Duncan, McDonald/Timbs Incorporation Formulations"). Author-named variants such as
"## The Asymmetry: A vs B at a Glance" are also permitted in this slot. Insert this H2
only when a comparison meaningfully disambiguates peer topics or cases that readers
commonly conflate. If the comparison would merely restate the Doctrinal Development
section, fold the material into Doctrinal Development instead and omit this slot.

Lint check 1 (template-conformance) explicitly allows any H2 starting with "Comparison:"
in this slot, plus any author-named H2 placed between "## Key Cases" and
"## Hypothetical Applications". The slot is present-or-absent; its internal heading is
not schema-enforced beyond the slot-position rule.

Delete this comment block when creating a real page.
-->

## Hypothetical Applications

### Same-Side

1. **Hypo:** [Fact pattern] **Why:** [Reasoning]
2. **Hypo:** [Fact pattern] **Why:** [Reasoning]

### Opposite-Side

3. **Hypo:** [Fact pattern] **Why:** [Reasoning]
4. **Hypo:** [Fact pattern] **Why:** [Reasoning]

### Fence-Sitter

5. **Hypo:** [Fact pattern] **Why:** [What makes this hard]

---

## How to Spot on an Exam

Trigger facts, common patterns, and the analytical framework to deploy.

---

## Critique

Scholarly criticism and independent analysis. Logical weaknesses, competing values, and open questions. Consider both progressive and originalist/textualist perspectives.

---

## Connections

- [[Topics/Related Topic|Related Topic]]
- [[Cases/Key Case|Key Case]]

---

## Sources

- [[Cases/{{Case Name (Year)}}|{{Case Name (Year)}}]]
- [[Lectures/{{Lecture Title}}|{{Lecture Title}}]]

---

#con-law-i #topic
