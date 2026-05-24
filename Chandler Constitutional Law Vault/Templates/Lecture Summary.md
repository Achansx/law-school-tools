---
lecture_title: "{{Lecture Title}}"
type: "{{lecture | class-recap | review-session}}"
topic_area: "{{e.g., Commerce Clause | Standing | Executive Power}}"
theme: "{{Same as topic_area, used by the timeline legend}}"
week: null   # Integer 1–14 if known. Drives the W## column on the lectures timeline.
cases_discussed:
  - "{{Case Name (Year)}}"
  - "{{Case Name (Year)}}"
cases_covered:
  - "{{Case Name (Year)}}"   # Canonical name for the redesign. Mirror cases_discussed when populating both.
date: "{{YYYY-MM-DD if known}}"
is_current: false   # Set true on the most-recent past lecture so the dashboard surfaces it as "this week".
is_upcoming: false  # Set true on lectures whose date is in the future to render them at 62% opacity with a hollow timeline dot.
verified: "{{YYYY-MM-DD}}"
source_files:
  - "Source Materials/{{filename.pptx or filename.pdf}}"
---

<!--
FRONTMATTER POPULATION GUIDE (delete this comment block when creating a real page)

lecture_title    Human-readable title derived from the slide deck cover or topic banner. Must equal the H1 and filename stem.
type             One of: lecture | class-recap | review-session. No other values.
topic_area       Doctrine or topic covered. Align with an existing Topics/ page name when possible (e.g., "Commerce Clause", "Standing").
theme            Display label for the lectures-timeline legend dot. Almost always equal to topic_area; set explicitly so the deployed site doesn't have to guess.
week             Integer 1–14 if the syllabus week is known (from the deck cover, filename, or the syllabus). Renders as the W## column on the chronological timeline. Leave null when unknown.
cases_discussed  Every case the lecture references. Each entry "{Case Name} ({Year})". Create links even if the Case page does not yet exist; Expand will wire them up.
cases_covered    Canonical name used by the redesign. When both `cases_discussed` and `cases_covered` are present, Synthesize/Verify keep them in sync. New Lecture pages should populate `cases_covered` directly; the build script falls back to `cases_discussed` only for legacy pages.
date             Lecture date YYYY-MM-DD if known from the deck or syllabus. Leave unset if unknown.
is_current       Boolean. Set true on the single most-recent past lecture so the dashboard's "This week in lecture" picks it up. Verify swaps this from one Lecture to the next as the term progresses.
is_upcoming      Boolean. Set true on lectures whose date is in the future; the timeline renders them at 62% opacity with a hollow dot.
verified         Today's date YYYY-MM-DD. Update whenever the summary is re-checked against the source deck.
source_files     YAML list of raw Source Materials inputs. Almost always one entry: the slide deck filename. Use `Source Materials/filename.pptx` or `Source Materials/filename.pdf`. Must stay in sync with the ## Sources footer section. In the footer, render each entry as an Obsidian wikilink ([[Source Materials/filename.pptx]]) so the deployed site turns it into a direct download link.
-->

# {{Lecture Title}}

## Professor Emphasis

Key points the professor stressed. Themes, recurring questions, or analytical frameworks highlighted in the slides.

---

## Lecture Outline

Structured summary of the lecture content, preserving the analytical flow of the slides.

---

## Cases Discussed

| Case | Key Takeaway from Lecture | Full Brief |
|------|--------------------------|------------|
| **Case Name** | What the professor emphasized | [[Cases/Case Name\|Link]] |

---

## Hypotheticals and Class Discussion

Any hypos presented in the slides, practice problems, or discussion prompts. Include the professor's analytical approach if discernible.

---

## Key Takeaways

- Main doctrinal points reinforced
- Exam tips or emphasis signals
- Connections between topics drawn by the professor

---

## Connections

- [[Topics/Related Topic|Related Topic]]
- [[Lectures/Related Lecture|Related Lecture]]

---

## Sources

- [[Source Materials/{{filename.pptx or filename.pdf}}]]

<!-- Use the wikilink form so the deployed site turns this into an
     <a href="source/..."> download link. The build script copies the
     Source Materials folder into /source/ for that purpose. -->


---

#con-law-i #lecture
