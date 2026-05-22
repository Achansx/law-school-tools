---
section: "05"
fact_type: example
source_path: "Chandler Constitutional Law Vault/Templates/Case Brief.md"
verified: true
notes: "The four-bucket doctrine_family enum (Federalism, Separation of Powers, Individual Rights, Justiciability) is the structural commitment that lets the build script render a four-family grid on the deployed site's index page. This is the smallest unit of 'schema doing work the prose alone could not': a single typed field per case promotes to a color column. The realignment policy in RUNBOOK explicitly forbids inline enum widening — the bucket set is a vault-wide commitment, not a per-page choice. Section V should describe this as the example of a schema decision producing visible structure on the site."
---

The Case Brief template's `doctrine_family` field carries one of exactly four values: Federalism, Separation of Powers, Individual Rights, or Justiciability. The same enum is used on the Topic Page template's `area` and `family` fields. The build script reads this field directly: it drives which color column a case or topic appears under in the deployed site's four-family grid, and it controls the holding-bar accent color on case pages. The enum is locked: RUNBOOK requires a page that does not fit any existing value to be realigned to the nearest canonical value rather than widened in place. Widening is a vault-wide change requiring an explicit edit to the template guide, a RUNBOOK update, and a BUILD_NARRATIVE note.

Exact source quote, `Chandler Constitutional Law Vault/Templates/Case Brief.md` line 65 (population guide):

> doctrine_family Exactly one of: Federalism | Separation of Powers | Individual Rights | Justiciability. Drives which family color the case page borrows in the holding bar.

Exact source quote, `Chandler Constitutional Law Vault/RUNBOOK.md` enum realignment policy paragraph:

> **Enum realignment policy.** When a page's `area` or other enum-typed field does not fit any existing enum value (example: Judicial Review initially assigned `area: "Federal Judicial Power"`, which is not one of Federalism | Separation of Powers | Individual Rights | Justiciability), REALIGN the page to the nearest canonical value; do NOT widen the enum inline. Widening the enum is a vault-wide change that requires editing the template's inline guide, updating this RUNBOOK if the enum is mentioned here, and a one-paragraph BUILD_NARRATIVE note explaining the reason.
