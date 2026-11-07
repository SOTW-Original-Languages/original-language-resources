# SOTW Original Languages | LIVE PROGRESS LOG

**Updated:** 2026-11-07  
**Stage:** Hebrew Strong's dictionary research and lookup indexing  
**Status:** Research artifacts built; public normalized baseline not yet independently located. No production script or deployment.  
**Repository:** `SOTW-Original-Languages/original-language-resources`

> **START HERE IN A NEW THREAD.** This is the short, frequently updated work log. For binding decisions and detailed history, read [Durable Decisions](SOTW_DURABLE_DECISIONS_AND_CONTINUITY.md) and [Vetted Sources & Artifacts](SOTW_VETTED_SOURCE_AND_ARTIFACT_INDEX.md). This log does not supersede those records.

## Update rule (until a production script exists)

**At every substantive report-back, update this SAME file in GitHub.** Do not create a new progress file, replace the durable register, or leave the only checkpoint in chat. Use the latest GitHub version and its blob SHA before editing; preserve previous entries. Change the four lines above, update the CURRENT STATE and NEXT ACTION, then **prepend** a short dated entry to the UPDATE HISTORY. Include output ZIP filename, checksum if verified, and GitHub commit when known. Mark facts **VERIFIED**, **OWNER DECISION**, **UNVERIFIED**, or **BLOCKED**. Never call a chat ZIP installed or published.

## CURRENT STATE

- **VERIFIED:** Selected Hebrew Strong's digital OSIS source is `strongs-master.zip / strongs-master/hebrew/StrongHebrewG.xml`, inside `SOTW_WordStudy_03_DICTIONARIES_LEXICONS_KJV_WEBSTER_2026-11-05.zip`. Original XML SHA-256: `1f9659ea208f4c498843a0280dacb1448627c33ca77712642d8705793ab66061`.
- **VERIFIED (research):** 8,674 entries; 24,841 original list items; 21,500 numbered senses and 2,680 proper-name glosses in the selected-content classification. Source language markers: 6,046 Hebrew/Aramaic and 2,628 `x-pn` proper-name markers that must **not** be miscast as a language.
- **OWNER DECISION:** Use the widely distributed, public-domain-designated Strong's digital edition as the practical foundation. Do not rebuild a word-perfect 1894 edition or require a PDF scan comparison. Preserve source and digital editorial provenance. No external STEP, Open Scriptures, TWOT, BDB, or CLBL **alternative dictionary definitions** are to be imported for public display. The owner has said the normalized display attribution count was already zero; **locate and verify that accepted baseline instead of reopening the audit**.
- **VERIFIED (internal research):** A source-attribution audit found 202 explicitly labeled sense items in 178 entries in the raw research record. These are **source/audit markers, not 202 new imported sources or newly proven defects**. The earlier 14-unavailable stripped projection was an audit variant, **not** the approved final display.
- **VERIFIED (research):** `SOTW_STRONGS_LOOKUP_RESEARCH_INDEX_2026-11-07.zip` indexes 8,674 Strong's IDs, 12,457 searchable tokens, 24,180 sense/name-gloss items, and 55 literal cross-reference candidates. These hooks are **not** verified semantic links and the index is **not public-ready**.
- **UNVERIFIED:** The owner-accepted zero-marker normalized public artifact has not been positively identified among the compared packages. Do not claim its contents, regenerate it from an audit variant, or overwrite it.
- **RELEASE BOUNDARY:** Research-only. No public deployment, production script, canonical-schema replacement, CGBC player modification, or player integration has been authorized.

## NEXT ACTION (one task only)

**Locate the accepted normalized public dictionary baseline** in current GitHub files or available original artifact inventory. Record exact path, SHA-256/blob SHA, schema/fields, and whether public attribution markers are indeed zero. Then connect the existing ID/token lookup index to **that accepted baseline** without changing source content. If unavailable, report exactly where searched and what file is missing. Do not restart rights vetting or 1894 reconstruction.

## UPDATE HISTORY (newest first; append nothing above this heading except new entries)

### 2026-11-07 | Lookup index checkpoint
- **VERIFIED:** Research lookup index created: `SOTW_STRONGS_LOOKUP_RESEARCH_INDEX_2026-11-07.zip`. Counts: 8,674 IDs; 12,457 terms; 24,180 sense/name-gloss items; 55 candidate hooks.
- **GitHub continuity commit:** `2ca8bf0db32052a7679f62592f02b06b1193a2f5`.
- **Open:** Accepted normalized public baseline not found/verified. No production deployment.

### 2026-11-07 | Normalization reconciliation
- **VERIFIED:** Raw research record versus stripped audit variant reconciled; 202 labeled items explain the difference, zero mismatch in that *audit variant*. This is **not** proof that the separate accepted normalized baseline was found.
- **Artifact:** `SOTW_STRONGS_NORMALIZATION_RECONCILIATION_2026-11-07.zip`.
- **GitHub continuity commit:** `5397a521dbccc5c320b0b4071fe18612ccbd2141`.

### 2026-11-07 | Practical digital-edition policy restored
- **OWNER DECISION:** No full 1894 scan comparison, no speculative deletion of usable source material, and no imported alternative lexicon definitions. Preserve source and distinguish internal audit from public display.
- **Artifact:** `SOTW_STRONGS_DIGITAL_EDITION_RESTORED_RESEARCH_2026-11-07.zip`.
- **GitHub continuity commit:** `6ca8af68d20cd264bebdbc2e22548ed327ef8f3a`.

## Repeatable report-back template

Copy and insert immediately **under UPDATE HISTORY** after each substantive result:

```markdown
### YYYY-MM-DD | Short milestone
- **VERIFIED / OWNER DECISION / UNVERIFIED / BLOCKED:** What actually changed or was checked.
- **Evidence:** GitHub path + commit/blob SHA, or artifact filename + verified SHA-256.
- **Counts/tests:** Actual results, with scope.
- **Unchanged:** What was NOT deployed or altered.
- **Next:** One specific action.
```

**Safety check before every GitHub edit:** fetch latest file + SHA, edit in place, commit with a descriptive message, then fetch again to confirm. If another change landed meanwhile, reconcile instead of overwriting. Once a production script exists, this file can become its human-readable milestone journal.
