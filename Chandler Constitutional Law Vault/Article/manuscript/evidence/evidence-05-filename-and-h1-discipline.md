---
section: "05"
fact_type: example
source_path: "Chandler Constitutional Law Vault/PROJECT_PRIMER.md"
verified: true
notes: "The discipline that case_name / topic_name / lecture_title in frontmatter MUST equal the H1 MUST equal the filename stem is the structural commitment that makes wiki-links resolve mechanically. PROJECT_PRIMER lines 39 to 44 fix this. The 'no periods, and not &' rule prevents drift between v. and v, between & and and. Section V uses this as a concrete example of how a one-paragraph rule produces vault-wide consistency the build script can rely on. Cross-references the Lint rubric's filename-convention check in rubric/lint.md."
---

The vault enforces filename, H1, and frontmatter-name agreement as a strict three-way invariant. Cases follow `Cases/Case Name v Party (Year).md`; the frontmatter `case_name` field, the file's H1, and the filename stem must agree with no periods (so `v Madison`, not `v. Madison`) and with `and` rather than `&`. Topics follow `Topics/Topic Name.md`; Lectures follow `Lectures/Lecture Title.md`. The three-way invariant is what lets wiki-links resolve mechanically: a build script can match `[[Cases/Marbury v Madison (1803)]]` to the filename without normalization heuristics. The Lint rubric scores filename, H1, and frontmatter-name agreement as part of its template-enforcement criterion. Section V should describe this as the smallest structural commitment that produces vault-wide consistency the downstream tooling can rely on.

Exact source quote, `Chandler Constitutional Law Vault/PROJECT_PRIMER.md` lines 38 to 45 (File Naming):

> ## File Naming
>
> - Cases: `Cases/Case Name v Party (Year).md` (e.g., `Cases/Marbury v Madison (1803).md`)
> - Topics: `Topics/Topic Name.md`
> - Lectures: `Lectures/Lecture Title.md`
>
> H1 and `case_name` frontmatter must match the filename convention: no periods, "and" not "&".
