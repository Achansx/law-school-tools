---
section: "03"
fact_type: example
source_path: "Chandler Constitutional Law Vault/Cases/Marbury v Madison (1803).md"
verified: true
notes: "The wiki-link cluster that turns the three content folders into a navigable graph for student browsing. The Marbury page closes with a Connections block of fifteen outbound wiki-links spanning four Topics, seven other Cases, and three Lectures, with each link rendered as a clickable badge in the deployed shell. Section III's walkthrough uses this as the proof that the student is not stuck on the page they landed on — every page is an entry to a doctrinal neighborhood. The wiki-link grammar itself (`[[folder/filename|Display Text]]`) is documented in Section V's evidence-05-wikilink-conventions.md; this card covers what the grammar produces on a populated page as a student-facing navigation surface. Pairs with PI-027 because the Obsidian-style graph view of these clusters is one of the workplan §3.2 screenshot needs."
---

Every populated Case, Topic, and Lecture page in the vault closes with a Connections block that lists every other page touching the same doctrine, case family, or pedagogical thread. The Marbury v Madison (1803) Case brief's Connections block lists fifteen outbound wiki-links: four Topics (Judicial Review, Political Question Doctrine, Separation of Powers, Executive Power), seven other Cases (Martin v Hunter's Lessee, McCulloch v Maryland, Youngstown, The Prize Cases, Rahimi, Cohens v Virginia, City of Boerne v Flores, Trump v United States), and three Lectures (Marbury, Enumerated Powers - New Deal, Martin v Hunter's Lessee). Each entry is rendered as a clickable badge in the deployed shell; clicking carries the student to the linked page through the same hash-route navigation that powers the top-nav. The Marbury page's specific cluster is illustrative rather than maximal — a student following the Judicial Review Topic page through Marbury, then through Martin v Hunter's Lessee, then through Cohens v Virginia, traces the doctrinal arc from 1803 through 1816 through 1821 across three Case briefs and back into the Topic synthesis without ever opening the Cases index. Section III walks this graph as the proof that the deployed site has reading paths above the page level, and the wiki-link cluster is what makes those paths navigable rather than implicit.

Exact source excerpt, `Chandler Constitutional Law Vault/Cases/Marbury v Madison (1803).md` lines 170 to 186 (Connections block, abbreviated to the first nine entries):

> ```
> ## Connections
>
> - [[Topics/Judicial Review|Judicial Review]]
> - [[Topics/Political Question Doctrine|Political Question Doctrine]]
> - [[Topics/Separation of Powers|Separation of Powers]]
> - [[Topics/Executive Power|Executive Power]] (Marbury's ministerial/discretionary distinction is the doctrinal seed for reviewability of executive action; the line between "ministerial duty assigned by law" and "political act only politically examinable" structures every modern executive-power case)
> - [[Cases/Martin v Hunter's Lessee (1816)|Martin v Hunter's Lessee (1816)]], the structural completion of Marbury that Marshall's opinion deliberately leaves open; the direction is forward, with Story in Martin carrying Marbury's "province and duty" reasoning into the question Marbury expressly did not reach, namely SCOTUS appellate review of state courts on federal questions.
> - [[Cases/McCulloch v Maryland (1819)|McCulloch v Maryland (1819)]] (Marshall's expansive constitutional interpretation carried forward; both opinions use the "we are expounding a constitution" principle)
> - [[Cases/Youngstown Sheet and Tube Co v Sawyer (1952)|Youngstown]] (political question doctrine developed; Jackson's framework continues Marbury's project of defining constitutional limits on executive power)
> - [[Cases/The Prize Cases (1863)|The Prize Cases]] (political question doctrine applied to presidential determination of belligerency)
> ```
