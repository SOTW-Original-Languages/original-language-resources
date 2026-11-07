# SOTW Original Languages — Durable Decisions & Continuity Register

**Established:** 2026-11-06  
**Status:** Owner-directed architecture and research-continuity record. This document records owner decisions, including acceptance of the archived Greek CC0 and Hebrew Public Domain declarations as the working rights basis for the selected Strong's publication sources. It is not an independent legal guarantee or a blanket approval of unrelated third-party editions.  
**Scope:** SOTW Original Languages and Word Study Inspector. No CGBC player or other-repository changes.

## Mandatory new-thread resume procedure

1. Read this register, `docs/ARCHITECTURE.md`, `docs/SOURCES_AND_RELEASE.md`, `docs/TRANSLATION_ADAPTERS.md`, and the current inspector README.
2. Inspect the latest GitHub files/commits and available original source archives and hashes before proposing new research or rebuilding anything.
3. Distinguish **owner-settled design**, **verified implemented state**, **unverified historical claim**, and **open release gate**. Do not turn a missing citation into a reversal of an owner decision.
4. Resume only the smallest unresolved task. Preserve research findings and original source provenance; no blanket restart.
5. Update this register with date, evidence paths, decision, and outstanding work after consequential changes. Do not claim installation or public deployment from a chat-only document.

## Owner-settled decisions (do not casually reopen)

- **Independent SOTW-owned original-language and lexicon library.** STEP is not a required runtime, alignment authority, publication source, or source of permission for independent Strong's links. STEP and modern XML editions can be used for comparison/verification; if their content is actually reproduced, comply with the particular source's terms.
- **Historical Strong's is the intended primary published lexicon**, credited to James Strong and the correct original Hebrew/Greek dictionary/edition. **Selected source decision (2026-11-06):** use the archived Greek `strongs-dictionary-xml-master.zip` edition under its stated CC0 dedication and the archived Hebrew `strongs-master.zip` / `StrongHebrewG.xml` edition under its embedded Public Domain declaration as the publication foundation. Accept those source-publisher declarations as sufficient working rights evidence; do not demand reconstruction of every historical editorial contribution. Preserve the source notices and hashes. This acceptance does not transfer to unrelated XML editions or content.
- **Do not synthesize, truncate, or rewrite definitions for convenience.** Display source-authored short fields, full historical definitions, and translation/usage fields distinctly and accurately. If a short field is not in the selected source, label it absent, not AI-supplied. Previously created editorial Quick Meaning is not authoritative historical Strong's text.
- **All source-attested Strong's tags must survive.** Model an English word's native tags as an array; never silently collapse legitimate multiple tags. Multiple dictionary senses/subentries are distinct from multiple native word tags. A lexicon's expanded subentry (e.g. STEP H1254A/B) must not be represented as an independently native KJV tag.
- **Translation precedence:** BSB retains its own native author/source original-language alignment. KJV retains native KJV USFM Strong's tagging, including multiple IDs. NWB (Webster Bible 1833) and ASV 1901 may use evidence-supported KJV-derived associations, retaining all supported tags; do not invent or publicly assert unresolved alignments. Preserve original texts, variant readings and provenance.
- **Dictionary is not contextual exegesis.** Show all source-authored meanings/alternatives without asserting each applies in a selected passage. Preserve lexical uncertainty.
- **Provenance vs reader attribution:** Reader-facing attribution should foreground James Strong for independently sourced historical Strong's text. Internal audit must retain the exact digital source, edition, original-byte hash, transformations, and rights basis. Any legally required modern provider attribution remains if that provider's content is used.
- **One shared SOTW lexical resource library**, not a repository per dictionary; independent translation and historical-commentary repositories remain separate. No production player integration without specific owner authorization.
- **BDB decision remains closed:** BibleAquifer digital BDB excluded from initial public release; do not reopen without owner instruction.

## What was actually verified (as of 2026-11-06)

- `docs/ARCHITECTURE.md` defines four layers: original source manifests, approved lexical records, evidence-backed translation links, and generated display projections.
- `docs/SOURCES_AND_RELEASE.md` requires exact-source provenance and explicit `approved_public` status before public redistribution; historical public-domain status alone is not a blanket digital-transcription release approval.
- Original source archive `SOTW_WordStudy_03_DICTIONARIES_LEXICONS_KJV_WEBSTER_2026-11-05.zip` contains `source_files/strongs-master.zip`, `source_files/HebrewLexicon-master.zip`, `source_files/strongs-dictionary-xml-master.zip`, `source_files/thayers-greek-lexicon-dataset-master.zip`, `source_files/webster1828-master.zip`, KJV USFM and Webster 1833 USFM, and a source-hash inventory. The selected Greek CC0 and Hebrew `StrongHebrewG.xml` Public Domain declarations are accepted by the owner as the working publication rights basis; the other archives remain comparison or separate source candidates.
- `SOTW_Original_Languages_Build_Continuation_Handoff_2026-11-06.pdf` explicitly says **do not restart the historical source search**; aim for historical author/edition attribution while respecting any applicable digital source obligations.
- `docs/inspector/README.md` documents the current v2.3 three-passage public inspection preview, its historical Strong's excerpts, editorial Quick Meaning, STEP CC BY glosses, source-native BSB/KJV distinctions, and limited KJV-derived NWB/ASV links. The existing public viewer is **not** the final owner-approved lexicon publication architecture.
- Earlier inspector research build covers 66 books privately; the public site currently samples only Genesis 1:1, John 1:1, and Romans 10:9. Never publish internal flags, disputed links, restricted definitions, or private research files by copying the private build wholesale.

## Accepted Strong's source decision and remaining implementation tasks

**Owner acceptance, 2026-11-06:** The archived Greek edition's CC0 declaration and the archived Hebrew `StrongHebrewG.xml` embedded Public Domain declaration are accepted as the project's working basis for publishing the corresponding Strong's text. Reader-facing attribution should identify **James Strong**; retain exact digital-source and license provenance in the internal manifest. Do **not** reopen a general historical-rights audit or require independent proof of every modern edit absent specific contrary evidence. Do not reproduce a separate provider's content while silently removing attribution required by that separate edition.

1. Locate/record exact selected archive member paths, byte hashes and source declarations in the publication manifest. This is implementation traceability, **not** a prerequisite to re-litigate the publisher's declaration.
2. Inspect the selected files' actual full definition, short field (if present), lemma/transliteration and KJV usage fields. Never manufacture a missing short definition.
3. Update source release metadata consistently with `docs/SOURCES_AND_RELEASE.md` using the accepted declarations and ordinary validation checks. The decision register alone does not deploy or alter the release state machine.
4. Update the inspector in a separately authorized change: display source-authored Strong's text, remove editorial Quick Meaning from authoritative display, and make STEP optional research comparison rather than a dependency.
5. Validate multiple-tag arrays, BSB/KJV native source boundaries, KJV-derived NWB/ASV support and public/private separation before expanding public data.

## Avoid these recurring mistakes

- Do not say the STEP brief gloss is required to display a Hebrew/Greek word or its independent Strong's relationship.
- Do not treat STEP's extended IDs as extra native KJV tags.
- Do not equate Strong's historical public-domain book with every digital XML edition.
- Do not attribute AI-authored Quick Meaning to James Strong.
- Do not insist on re-researching the entire lexicon because one source decision or field is not yet documented.
- Do not infer that a private 66-book build has been approved for public release.

## Change log

- **2026-11-06 (owner follow-up):** Accepted archived Greek Strong's CC0 and Hebrew `StrongHebrewG.xml` Public Domain source declarations as the working publication basis; James Strong is the reader-facing historical attribution. No repeated historical-editorial-rights audit absent contradictory evidence. Retain internal provider provenance and update release manifests during implementation. Decision-record update only; no inspector or source-data deployment.
- **2026-11-06:** Initial register created following owner report of repeated loss of decisions across threads. Read-only reconciliation of existing GitHub architecture, source/release policy, inspector README, archived source filenames, and continuation handoff. No change to production data, inspector, schemas, or other repositories.

## Continuity rule

**Evidence first; reopen only a documented contradiction.** Owner decisions govern the intended design, while release rights and source provenance remain independently verifiable requirements. Preserve both without substituting one for the other.
