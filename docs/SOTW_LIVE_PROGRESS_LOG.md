# SOTW Original Languages | LIVE PROGRESS LOG

**Updated:** 2026-11-07  
**Stage:** Locate accepted normalized public baseline before public index  
**Status:** Full working snapshot ZIP assembled and hash-verified; GitHub snapshot pointer created, but actual ZIP upload pending appropriate storage/access. No production script or deployment.  
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
- **CLARIFICATION:** This thread produced research projections, a ten-entry presentation preview, and a lookup index; the record does not establish that a separate approved full public baseline file was ever created. The owner's zero-marker statement is a settled normalization/presentation expectation, not evidence of a missing file. Do not keep asking the owner to locate one.
- **RELEASE BOUNDARY:** Research-only. No public deployment, production script, canonical-schema replacement, CGBC player modification, or player integration has been authorized.

## NEXT ACTION (one task only)

Build a **deterministic, research-only display projection** from the selected Strong's digital source and the existing typed fields, preserving complete usable source content, Strong's IDs, grammar and provenance. Normalize only display metadata as previously agreed; **do not** import other lexicon definitions, silently remove senses, or claim original-1894 word perfection. Connect the existing lookup index and validate actual displayed attribution metadata. Preserve research source bytes separately. No public deployment or player change.

## UPDATE HISTORY (newest first; append nothing above this heading except new entries)

### 2026-11-07 | Owner authorizes temporary GitHub snapshot storage
- **OWNER DECISION:** Existing repository may hold the complete latest working snapshot at one stable path; no private repository required. Owner accepts public-repository storage risk and intends to delete the snapshot when production scripting is complete.
- **VERIFIED:** Local ZIP exists and SHA-256 is `fcfbe18b121e4e0eee89b20dcfcc5744f439ab982dde17e5166c15dfd4f19f6c`.
- **PENDING:** GitHub ZIP upload itself has not succeeded; connector accepts text or base64 blobs, but current local runtime cannot connect directly to GitHub. The GitHub pointer accurately states this. Upload exact ZIP to `research/snapshots/SOTW_HEBREW_LATEST_WORKING_SNAPSHOT.zip` and verify hash before declaring recoverable from GitHub.
- **CAVEAT:** Replacing/deleting the visible file does not automatically erase old Git history.



### 2026-11-07 | Actual working snapshot assembled, GitHub pointer created
- **VERIFIED:** Built `SOTW_HEBREW_LATEST_WORKING_SNAPSHOT_2026-11-07.zip` (1,836,147 bytes; SHA-256 `fcfbe18b121e4e0eee89b20dcfcc5744f439ab982dde17e5166c15dfd4f19f6c`) containing complete selected digital research, lookup index, normalization reconciliation and manifest with component hashes.
- **VERIFIED:** Created `docs/SOTW_LATEST_WORKING_SNAPSHOT.md` to track the actual working ZIP separately from this progress log.
- **NOT YET UPLOADED:** Actual ZIP bytes are not in GitHub. Do not claim they are. The snapshot includes internal research text and needs an appropriate repository visibility/rights decision before upload.
- **Next:** Upload the ZIP to an approved appropriately controlled stable location, verify hash, and update the pointer; then continue display projection.



### 2026-11-07 | Corrected false missing-file blocker
- **VERIFIED:** Reinspected files from this conversation. `SOTW_HEBREW_PUBLIC_PRESENTATION_POLICY_RESEARCH_2026-11-07.zip` is explicitly a **10-entry sample preview**, with 8,674 source-field records audited, not a complete approved public baseline. `SOTW_STRONGS_DIGITAL_EDITION_RESTORED_RESEARCH_2026-11-07.zip` is a full research record; `SOTW_STRONGS_LOOKUP_RESEARCH_INDEX_2026-11-07.zip` is a research index.
- **CORRECTION:** Earlier checkpoint incorrectly treated an unverified separate 'accepted normalized baseline' as a file the owner needed to find. The owner correctly identified that the work was being performed in this thread. No request for a missing ZIP is warranted.
- **Next:** Produce deterministic normalized display projection from the accepted digital source and typed data, then validate its actual public fields; research-only until specifically authorized.



### 2026-11-07 | Baseline discovery attempt (no replacement)
- **VERIFIED:** Searched current repository code index for `normalized`, `strongs`, `display`, `lexicon`; search returned no matching files. This search outcome does **not** establish repository absence because code indexing may be incomplete.
- **VERIFIED:** Examined mounted `/mnt/data` file names and enumerated members of 35 top-level ZIPs for `normaliz`, `public_display`, `display_candidate`, and `approved_public`. No independently named accepted normalized public baseline was identified. Found the known `SOTW_STRONGS_ONLY_DISPLAY_RESEARCH_CANDIDATE_2026-11-07.zip`, which remains an audit variant, not an approved baseline.
- **BLOCKED:** Cannot safely attach a public search projection until the accepted normalized baseline is positively identified. Do not treat a search miss as proof it never existed.
- **Unchanged:** No data, schema, player, or public deployment modified.
- **Next:** Obtain the accepted baseline's exact repository path/artifact filename or identify it from an owner-provided accepted ZIP, then verify content and SHA before indexing.



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
