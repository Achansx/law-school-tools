---
case_name: "{{Case Name}}"
citation: "{{Volume}} {{Reporter}} {{Page}}"
year: "{{Year}}"
court: "{{Court}}"
doctrines:
  - "{{Doctrine 1}}"
  - "{{Doctrine 2}}"
concepts:
  - "{{Concept 1}}"
status: "{{good law | superseded | overruled | limited | narrowed}}"
midpage_id: "{{Midpage opinion ID if available}}"
midpage_url: "{{Midpage URL if available}}"
treatment: "{{Neutral | Positive | Negative | Cautionary}}"
cited_by: "{{number of citing cases if known}}"
verified: "{{YYYY-MM-DD}}"
source_files:
  - "{{Source Materials/filename.pdf or Source Materials/Midpage analyzeOpinion (opinionId N)}}"

# Holding-bar fields. The deployed site promotes these into a structured
# banner above the prose. Ingest leaves empty strings / lists; Enrich fills.
# When absent, build.py extracts a fallback from Memory Jogger / Holding.
issue: ""
holding: ""
reasoning: ""
doctrine_family: ""

# Citation metadata. Ingest fills what's on the opinion face; Enrich completes.
argued: ""
decided: ""
panel: ""
author: ""
vote: ""
disposition: ""

# Authority lineage. Ingest leaves empty; Enrich populates from the opinion +
# CourtListener find_cited_cases / find_citing_cases.
relies_on: []
distinguishes: []
applied_in: []
overrules: ""
overruled_by: ""
---

<!--
FRONTMATTER POPULATION GUIDE (delete this comment block when creating a real page)

case_name       Canonical short form, no periods in abbreviations, use "and" not "&". Example: "Brown v Board of Education". Must equal the H1 and the filename stem.
citation        "{Volume} {Reporter} {Page}" with U.S. Reports preferred for SCOTUS. Example: "347 U.S. 483".
year            Integer, no quotes. Year of decision.
court           "U.S. Supreme Court" for SCOTUS. Use standard abbreviations for lower courts ("S.D.N.Y.", "9th Cir.").
doctrines       Canonical doctrinal labels reused across the vault. Before coining a new one, glob Topics/ and existing case briefs for the closest match (avoid "Commerce Clause" vs "Interstate Commerce" drift).
concepts        Finer-grained indexing labels (e.g., "Rational basis review", "Strict scrutiny", "Political question doctrine").
status          Exactly one of: good law | superseded | overruled | limited | narrowed.
midpage_id      From the Midpage analyzeOpinion response. Required before Key Quotations can be filled.
midpage_url     Canonical opinion URL returned by Midpage (not a search-result URL).
treatment       How later cases treat it: Neutral | Positive | Negative | Cautionary.
cited_by        Integer from CourtListener find_citing_cases. Leave unset if unknown; do not guess.
verified        Today's date YYYY-MM-DD. Update whenever frontmatter or holdings are re-confirmed.
source_files    YAML list of raw Source Materials inputs that fed this brief. Use `Source Materials/filename.pdf` for PDFs and slide decks, and `Source Materials/Midpage analyzeOpinion (opinionId N)` for Midpage opinions. Must stay in sync with the ## Sources footer section. In the footer, render file entries as Obsidian wikilinks ([[Source Materials/filename.pdf]]) so the deployed site turns them into direct download links; keep Midpage opinion references as inline code because there is no file on disk to download.

issue           The question presented, ending in "?". One sentence preferred. Distinct from the longer ## Issue section which can develop alternative framings.
holding         The Court's answer, 1–2 sentences. Distinct from the longer ## Holding section. The deployed site's "Case of the Day" and the holding bar both render this verbatim — keep it readable on its own.
reasoning       One-paragraph synthesis of the majority's reasoning (≤3 sentences). Lists the moves (textual / structural / clear-statement / etc.) without recapping the analysis section.
doctrine_family Exactly one of: Federalism | Separation of Powers | Individual Rights | Justiciability. Drives which family color the case page borrows in the holding bar.
argued          ISO date YYYY-MM-DD if known. Leave empty when not on the opinion face.
decided         ISO date YYYY-MM-DD if known.
panel           Free-form list of judges on the panel. Useful for non-SCOTUS where the panel composition matters.
author          Surname of the majority author (e.g. "Gorsuch"). Per curiam opinions: "per curiam".
vote            Vote split as "6-3", "5-4", "9-0", or "per curiam". Use a hyphen, no spaces.
disposition     Brief disposition: "Affirmed", "Reversed", "Reversed and remanded", "Vacated", "S.J. for plaintiffs", etc.
relies_on       List of cases this opinion explicitly leans on. Each entry "{Case Name} ({Year})" matching the corresponding Cases/ filename when one exists.
distinguishes   List of cases this opinion narrows or sets aside without overruling.
applied_in      List of later cases that have applied this rule.
overrules       Single string when this case overrules another; empty otherwise. Format "{Case Name} ({Year})".
overruled_by    Single string when this case has been overruled; empty otherwise.
-->

# {{Case Name}}

## Memory Jogger

> One sentence capturing this case's essence.

---

## Facts

Key facts giving rise to the dispute. Include relevant statutes, regulations, or constitutional provisions. Explain the statutory scheme and specific provisions challenged. Note historical or political context when relevant.

---

## Procedural History

How the case reached the deciding court. Lower court rulings and reasoning. Basis for appeal. Distinguish between rulings on the merits and procedural posture.

---

## Judicial Votes

- **Majority:** Author (joined by ...)
- **Concurrence:** Author (joined by ...)
- **Dissent:** Author (joined by ...)

---

## Holding

Succinct statement of the court's judgment and the rule announced.

---

## Analysis

### Majority Opinion

Reasoning employed by the majority. Key constitutional, statutory, regulatory, or treaty provisions cited. Key precedents and how they were applied. Logical structure of the argument.

### Concurrence (Author)

How it differs from or supplements the majority.

### Dissent (Author)

Counter-reasoning and which premises it rejects.

---

## Hypothetical Applications

### Same-Side (Would come out the same way)

1. **Hypo:** [Fact pattern] **Why:** [Reasoning under the rule]
2. **Hypo:** [Fact pattern] **Why:** [Reasoning under the rule]

### Opposite-Side (Would come out differently)

3. **Hypo:** [Fact pattern] **Why:** [Reasoning under the rule]
4. **Hypo:** [Fact pattern] **Why:** [Reasoning under the rule]

### Fence-Sitter (Genuinely unclear)

5. **Hypo:** [Fact pattern] **Why:** [What makes this hard]

---

## Critique

Scholarly criticism of the opinion(s). Independent analysis of logical weaknesses. Values or premises that would lead to different conclusions. Consider both progressive and originalist/textualist perspectives where relevant.

---

## Key Quotations

> "Important language from the opinion." (Opinion Author)

---

## Key Points

- Doctrinal significance
- How this case relates to or distinguishes related cases
- Exam-relevant observations or professor emphasis
- Individual factors in any multi-part test

---

## Connections

- [[Topics/Related Doctrine|Related Doctrine]]
- [[Cases/Related Case|Related Case]]

---

## Sources

- [[Source Materials/{{filename.pdf}}]]
- `Source Materials/Midpage analyzeOpinion (opinionId N)`  <!-- keep Midpage entries as inline code; they are not files on disk -->

<!-- Use the wikilink form for any entry that points at an actual file in
     Source Materials/. The build script copies that folder into /source/ on
     the deployed site and rewrites these wikilinks into <a href="source/...">
     download links. Midpage opinion records stay as inline code because they
     reference an external opinion ID, not a downloadable file. List one
     bullet per source_files entry; the order should match. -->


---

#con-law-i #case
