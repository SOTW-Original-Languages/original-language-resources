# SOTW Original Languages | LIVE PROGRESS LOG

**Updated:** 2026-11-07  
**Stage:** Stage 1/5 corrected locally; Stage 2 next  
**Status:** Pre-beta Stage 1 corrected research projection generated locally with no 202-marker filtering; Checkpoint 0 remains last complete recovery ZIP. Stage 2 next.  
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

### 2026-11-07 | Stage 6: original local Word Study resources rediscovered and verified
- **VERIFIED:** Original private 66-book inspector, public-safe shell, Webster/KJV/Strong's/lexicon source bundle, ASV continuity bundle and Hebrew Recovery Checkpoint 1 are all present locally. All five source ZIP CRC checks PASS. SHA-256s and member inventories recorded in `SOTW_STAGE6_RESOURCE_RECONNECTION_2026-11-07.zip` (downloadable conversation artifact; not stored in GitHub).
- **DISTINCTION:** NWB/Webster 1833 is a Bible edition in the original inspector; Webster 1828 is a separate historical English dictionary source. Original Bible order: BSB, KJV, NWB/Webster 1833, ASV 1901.
- **NEXT:** Stage 7 inspect the archived Webster 1828 source schema and build a separate headword lookup resource with provenance. Preserve private research data and do not deploy.



### 2026-11-07 | Stage 5/5 COMPLETE: Recovery Checkpoint 1
- **VERIFIED ZIP:** `SOTW_HEBREW_RECOVERY_CHECKPOINT_1_STAGE5_2026-11-07.zip`, 3,286,760 bytes, SHA-256 `9d37881c29febe4071fded3b2c4d4252fb07c428af8d301ae32db25830d8ecca`.
- **CONTENTS:** Nested original Checkpoint 0 ZIP unchanged; corrected Stage 1 (8,674 entries), Stage 2 forward/reverse lexical indexes, Stage 3 search engine/tests, Stage 4 evaluation, manifest with individual SHA-256s, README and `verify_checkpoint.py`. Earlier rejected exclusion-based Stage 1 deliberately omitted.
- **VALIDATION:** ZIP CRC integrity PASS; per-file manifest SHA-256 PASS; nested Checkpoint 0 archive PASS; Stage 3 unit tests 9/9 PASS; Stage 4 regression checks 52/52 PASS. All runnable using Python standard library after extraction.
- **OWNER ACTION:** Download and retain the ZIP; reupload it to the next thread. This GitHub entry stores checkpoint metadata, **not** the ZIP bytes. Do not claim owner has downloaded until confirmed.
- **NEXT CYCLE:** Resume pre-beta work from this ZIP. Do not reopen settled 202-marker normalization, scan comparisons or source selection; no player integration or deployment without owner request.



### 2026-11-07 | Stage 4/5: search evaluation completed
- **VERIFIED:** 52/52 bounded regression checks PASS for exact IDs, unknown IDs, stopwords, deterministic ranking, valid postings, search limits, and representative English lexical queries. Evaluation script: `SOTW_HEBREW_STAGE4_2026-11-07/evaluate_search.py`; report: `STAGE4_REPORT.json`.
- **VERIFIED:** Stage 2 raw index contains 106 numeric-only tokens and 23 single-character tokens; Stage 3 ordinary keyword parser filters these. They remain in research indexes; no source data altered.
- **LIMITS:** Lexical search only, no stemming/fuzzy spelling, Hebrew morphology, or theological inference. Corrected Stage 1 is a pre-beta research projection, not independent certification of prior public-normalized edition.
- **NEXT:** Stage 5/5 package complete owner-downloadable recovery ZIP including Checkpoint 0 plus Stages 1 corrected, 2, 3, and 4, with integrity manifest and runnable smoke tests. No production/player integration.



### 2026-11-07 | Stage 3/5: executable Strong's search engine
- **VERIFIED:** Created `SOTW_HEBREW_STAGE3_2026-11-07/search_engine.py` (SHA-256 `fbb0b0c781f3ec7eaa155ad1471cedd3bdc86829d96565568177e198f180385b`) and `test_search_engine.py` (SHA-256 `427c139ebe3741090a96bf307070eb2a9ecb07c9a9104b9adfa9ae13064a65d7`).
- **VERIFIED:** 9/9 unit tests passed: 8,674 entries, exact Strong ID lookup and leading zeros, unknown IDs, stopword and numeric filtering, father and multiword search, stable ranking, no index mutation.
- **LIMIT:** Pre-beta lexical search only; no inferred semantic/theological links, fuzzy spelling, morphology, or integrated beta UI. Original source fields and settled normalization unchanged.
- **RECOVERY:** Actual Stage 3 code and report are downloadable conversation artifacts; GitHub log is metadata only. Owner-downloaded Checkpoint 0 is still last complete ZIP. Stage 5 ZIP due after two more stages, or early if continuity risk.
- **Next:** Stage 4/5: relevance and edge-case evaluation, stabilize search interface and document behavior.



### 2026-11-07 | Stage 2/5: display-derived search indexes completed
- **VERIFIED:** Corrected Stage 1 projection SHA-256 `0ddf649c80b3c03a836298f0b6d8b0ea3b7afc811eae3245ea3e579b872ab2b9` has 8,674 unique entries and retains 21,500 definitions and 2,680 name glosses without reapplying the settled source-attribution filter.
- **VERIFIED:** Generated `SOTW_HEBREW_STAGE2_2026-11-07/display_token_to_strongs.json` (SHA-256 `db484f19205b663ebba426d7318505b9a519cca6735ac7548c42ebddf7917d87`) and `display_tokens_by_strongs.json` (SHA-256 `fccf6cebd18bc390447b6a3ca26d6a6b35f61275e65d3b6306557cfc7269f7e6`). 12,999 tokens, 114,253 token-entry links, forward/reverse consistency PASS.
- **VERIFIED:** Compared with original internal index: 553 new-only tokens, 11 old-only tokens. Numeric and short-fragment tokens need reader-search tests; no public release claim.
- **RECOVERY:** GitHub log is updated, but large working JSON remains in local Stage 1/2 files; owner-downloaded Checkpoint 0 is the last full ZIP. Next full recovery ZIP due after Stage 5 or sooner for continuity risk.
- **Next:** Stage 3/5, test exact Strong's lookup, token matching, ranking and edge cases; do not reopen normalization audit.



### 2026-11-07 | Stage 1 corrected: source content retained
- **VERIFIED:** Generated `SOTW_HEBREW_STAGE1_CORRECTED_2026-11-07/strongs_display_research_projection.json`: 8,674 unique Strong's IDs, 21,500 definition items, 2,680 proper-name glosses, 637 grammar labels, and original remaining typed fields retained. SHA-256 `0ddf649c80b3c03a836298f0b6d8b0ea3b7afc811eae3245ea3e579b872ab2b9`.
- **CORRECTION:** No source items were filtered by the settled 202-marker audit. The earlier exclusion-based Stage 1 candidate is superseded. Original source research and audit metadata remain in Checkpoint 0.
- **SCOPE:** This is a pre-beta development projection, not independent proof of a previously accepted final normalized public edition. Actual JSON exists in conversation files, not GitHub.
- **RECOVERY:** Owner's Checkpoint 0 ZIP is the last full recovery; corrected Stage 1 file must be included in the next checkpoint.
- **Next:** Stage 2/5, generate search projection from the corrected display fields and validate against existing internal token index.



### 2026-11-07 | Owner correction: stop reopening the settled 202-marker audit
- **OWNER DECISION REAFFIRMED:** The 202 markers are original digital-source research/audit metadata, **not 202 unresolved public normalization defects**. The normalized final issues were already resolved. Do not strip senses or re-run attribution review merely because these markers exist in source archives.
- **CORRECTION:** Stage 1's conservative reader projection excluded 202 items and left 14 entries without display definitions. This is a **regressive audit-derived variant**, not accepted final normalized display. Mark it research-only/rejected for reader projection; do not use it as Stage 2 input.
- **NEXT:** Reconcile Stage 1 against the owner-settled normalized display treatment, preserving usable source definitions. Do not reopen historical 1894 scans or third-party dictionary sourcing. If the exact earlier normalized output is not separately saved, build the correct projection from existing source without treating 202 as unresolved defects; verify actual output fields rather than repeating the audit.



### 2026-11-07 | Stage 1/5 completed: deterministic research display projection
- **VERIFIED:** Generated 8,674-entry `strongs_display_research_projection.json` (SHA-256 `deb05f625d7900cf7d3a939a8dc1e7312b78de089631fdeeee1ee0106bd99eba`), with report and README in `SOTW_HEBREW_STAGE1_2026-11-07/`.
- **VERIFIED:** Exact Strong's ID match for 8,674 research and lookup records. 202 explicitly attribution-marked source items in 178 entries are tracked and excluded from the **new conservative reader projection**, while retained in Checkpoint 0 original research. 14 entries have no reader-facing definition or name gloss under this conservative rule.
- **CAUTION:** This is **not** the previously claimed owner-approved zero-marker normalized public baseline. Search tokens still come from the internal research index and are not cleared for reader-facing use. Do not overwrite the original source with the projection.
- **RECOVERY:** Owner-downloaded Checkpoint 0 remains the last complete recovery ZIP. Stage 1 data are separate until next checkpoint; download them if thread continuity is at risk.
- **Next:** Stage 2/5, verify field completeness and clean search-token display projection without losing source information.



### 2026-11-07 | Owner clarifies pre-beta status and recovery cadence
- **OWNER DECISION:** SOTW Original Languages is **pre-beta**. There is **no production player** at present. Stop describing this work as if a deployed player exists; continue building and testing the pre-beta system.
- **OWNER DECISION:** GitHub progress log updates after each completed stage; produce a verified, downloadable full-working-files recovery ZIP approximately every five stages and earlier for risky changes or thread continuity. Owner confirmed downloading the existing `SOTW_HEBREW_LATEST_WORKING_SNAPSHOT_2026-11-07.zip` as recovery checkpoint 0.
- **Next:** Stage 1 of 5, deterministic complete Hebrew Strong's research/display projection from existing source; no restart of prior source research.



### 2026-11-07 | Partial direct upload of working JSON
- **VERIFIED:** Uploaded `research/hebrew-strongs/indexes/literal_reference_hooks.json` as a normal GitHub file: 55 source-literal reference candidates, all explicitly unverified. Commit `ac34adb924d0c6e89f80dc5fa6f891749232bb77`.
- **PENDING:** Three large regular JSON files (`data/strongs_digital_selected_research.json`, `indexes/lookup_by_strongs.json`, `indexes/token_to_strongs.json`) are not uploaded. Local container cannot resolve github.com; connector writes GitHub text but cannot read local container files, so a reliable bulk transfer is still unavailable.
- **Next:** Transfer those three exact files without modifying content; run validator; update manifest. Do not claim a complete GitHub snapshot yet.



### 2026-11-07 | Owner replaces ZIP checkpoint plan with regular files
- **OWNER DECISION:** No ZIP snapshots. Store and update the actual Strong's research JSON and indexes at stable GitHub paths, plus scripts. Each report-back updates changed files and then the log.
- **VERIFIED:** Added `research/hebrew-strongs/README.md` documenting exact four file paths and research-only boundaries. Added `scripts/validate_hebrew_working_files.py` to check 8,674 unique IDs, matching lookup IDs, and generate SHA-256 manifest.
- **INCOMPLETE UPLOAD:** The four multi-megabyte JSON files have **not** been transferred to GitHub. Do not imply a new thread can yet recover full research data from the repository.
- **Next:** Transfer the four original JSON files to the stable paths, run validator, then proceed with display projection. The old ZIP snapshot plan is superseded.



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
