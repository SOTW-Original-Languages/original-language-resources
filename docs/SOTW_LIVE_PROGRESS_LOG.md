# SOTW Original Languages | LIVE PROGRESS LOG

**Updated:** 2026-11-07  
**Stage:** Stage 8B complete: BSB source-native original-language alignment; Stage 8 remains partial  
**Status:** Pre-beta Stage 8B complete: 437,587 source-tagged BSB original-language rows built and validated against Stage 7 Strong's; Recovery Checkpoint 5 includes previous Checkpoint 4 and Stage 8B. NWB/ASV and deeper morphology hooks still outstanding. No deployment.  
**Repository:** `SOTW-Original-Languages/original-language-resources`

> **START HERE IN A NEW THREAD.** This is the short, frequently updated work log. For binding decisions and detailed history, read [Durable Decisions](SOTW_DURABLE_DECISIONS_AND_CONTINUITY.md) and [Vetted Sources & Artifacts](SOTW_VETTED_SOURCE_AND_ARTIFACT_INDEX.md). This log does not supersede those records.

## Update rule (until a production script exists)

**At every substantive report-back, update this SAME file in GitHub.** Do not create a new progress file, replace the durable register, or leave the only checkpoint in chat. Use the latest GitHub version and its blob SHA before editing; preserve previous entries. Change the four lines above, update the CURRENT STATE and NEXT ACTION, then **prepend** a short dated entry to the UPDATE HISTORY. Include output ZIP filename, checksum if verified, and GitHub commit when known. Mark facts **VERIFIED**, **OWNER DECISION**, **UNVERIFIED**, or **BLOCKED**. Never call a chat ZIP installed or published.

## CURRENT STATE

- **VERIFIED:** Selected Hebrew Strong's digital OSIS source is `strongs-master.zip / strongs-master/hebrew/StrongHebrewG.xml`, inside `SOTW_WordStudy_03_DICTIONARIES_LEXICONS_KJV_WEBSTER_2026-11-05.zip`. Original XML SHA-256: `1f9659ea208f4c498843a0280dacb1448627c33ca77712642d8705793ab66061`.
- **VERIFIED (2026-11-07 source inspection):** Hebrew OSIS source has 8,674 `lemma`, transliteration (`xlit`), POS, morphology, concise `note type=explanation`, and KJV `note type=translation` fields, plus expanded numbered list items. Stage 7 has now restored these source-authored Hebrew fields in a separate complete research projection, alongside the earlier expanded senses. The selected Greek CC0 XML **v1.9** has now been projected with all 5,624 entries, including source-absent fields and 101 explicit Not Used placeholders. Neither is yet integrated into a public site. Distinct BDB/Thayer/STEP resources remain separate candidates/hooks, not merged Strong's definitions.
- **VERIFIED (research):** 8,674 entries; 24,841 original list items; 21,500 numbered senses and 2,680 proper-name glosses in the selected-content classification. Source language markers: 6,046 Hebrew/Aramaic and 2,628 `x-pn` proper-name markers that must **not** be miscast as a language.
- **OWNER DECISION:** Use the widely distributed, public-domain-designated Strong's digital edition as the practical foundation. Do not rebuild a word-perfect 1894 edition or require a PDF scan comparison. Preserve source and digital editorial provenance. No external STEP, Open Scriptures, TWOT, BDB, or CLBL **alternative dictionary definitions** are to be imported for public display. Owner-settled normalization is closed; **do not reopen the 202-marker attribution audit or strip senses**. Stage 7 retains source-authored content and is research-only, not a new public-normalization approval.
- **VERIFIED (internal research):** A source-attribution audit found 202 explicitly labeled sense items in 178 entries in the raw research record. These are **source/audit markers, not 202 new imported sources or newly proven defects**. The earlier 14-unavailable stripped projection was an audit variant, **not** the approved final display.
- **VERIFIED (research):** `SOTW_STRONGS_LOOKUP_RESEARCH_INDEX_2026-11-07.zip` indexes 8,674 Strong's IDs, 12,457 searchable tokens, 24,180 sense/name-gloss items, and 55 literal cross-reference candidates. These hooks are **not** verified semantic links and the index is **not public-ready**.
- **CLARIFICATION:** This thread produced research projections, a ten-entry presentation preview, and a lookup index; the record does not establish that a separate approved full public baseline file was ever created. The owner's zero-marker statement is a settled normalization/presentation expectation, not evidence of a missing file. Do not keep asking the owner to locate one.
- **RELEASE BOUNDARY:** Research-only. No public deployment, production script, canonical-schema replacement, CGBC player modification, or player integration has been authorized.

## NEXT ACTION (one task only)

**Stage 8C: Evidence-supported KJV-derived NWB/Webster Bible 1833 and ASV 1901 occurrence links.** Read original Bible text/source comparison artifacts and preserve all supported native KJV tag arrays; do not assume word equivalence across translations or assert unresolved alignments. Keep BSB source-native 8B and KJV source-native 8A independent. After Stage 8C, implement source-credited original-language morphology hooks. Owner needs only latest Recovery Checkpoint 5 plus original source archives. No deployment.

## UPDATE HISTORY (newest first; append nothing above this heading except new entries)

### 2026-11-07 | OWNER CORRECTION: Webster 1828 dictionary directly available for ALL Bible translations
- **OWNER DECISION (supersedes prior Webster navigation design):** Webster 1828 is a general historical English dictionary accessible by direct headword lookup from every displayed Bible translation (BSB, KJV, Webster 1833 Bible, ASV 1901). Do **not** require routing via Webster 1833 Bible, KJV, or Strong's before opening a Webster 1828 dictionary entry.
- **AUTHORSHIP/HISTORICAL INFERENCE:** Webster published his dictionary in 1828 before his KJV-based Bible revision in 1833. Shared author and chronological order reasonably support a working hypothesis that earlier lexical research informed the Bible revision, but do not document individual intended senses. Preserve this as historical inference, not an attested statement by Webster.
- **STRONG'S PIPELINES:** Keep BSB's own native alignment and KJV's native Strong's tags. Build KJV-text-comparison-derived supported Strong's associations separately for ASV 1901 and Webster 1833. No custom theological inference protocol for Webster 1833.
- **DICTIONARY PIPELINE:** Translation English word -> normalized direct Webster 1828 headword lookup -> display complete source-authored senses and provenance. Same reusable lookup service for all four editions. Do not equate English dictionary senses with Hebrew/Greek Strong's definitions or claim contextual disambiguation without evidence.
- **SUPERSEDES:** Prior proposed mandatory chain Webster 1833 -> Webster 1828 -> Strong's, and any suggestion that only Webster 1833 has direct Webster dictionary access. Stage 8C remains next. Checkpoint 5 remains current; no source or deployment change made.



### 2026-11-07 | Owner confirms Webster author-paired Bible and Dictionary linkage
- **OWNER DIRECTION:** Treat Noah Webster's 1833 Bible revision and 1828 English Dictionary as a complementary author-paired study path, using existing original archives rather than new source discovery or speculative interpretive protocols.
- **EXACT SOURCES:** `SOTW_WordStudy_03_DICTIONARIES_LEXICONS_KJV_WEBSTER_2026-11-05.zip / source_files/engwebster_usfm.zip` (Webster 1833 Bible); same parent archive / `source_files/webster1828-master.zip` (Webster 1828 Dictionary). Distinct provenance and source hashes retained.
- **PIPELINE:** KJV source-native Strong's tags -> verified KJV/Webster 1833 word correspondence -> Webster 1833 English surface -> normalized, source-preserving Webster 1828 dictionary headword lookup. Headword match is lexical navigation, NOT proof of contextual sense, historical authorial intent, or direct original-language equivalence. Preserve full dictionary senses and ambiguities.
- **STATUS:** Architectural refinement, not yet implemented. Stage 8C remains next; Recovery Checkpoint 5 remains latest.



### 2026-11-07 | Owner refines Stage 8C: KJV textual alignment bridge for ASV and Webster 1833
- **OWNER DIRECTION:** Favor a straightforward, source-evidenced KJV-to-ASV and KJV-to-Webster Bible 1833 word-alignment workflow over newly invented logical/interpretive protocols. Reuse KJV native Strong's tags as the initial reference for both related translations.
- **HISTORICAL PRECISION:** ASV 1901 descends through the English Revised Version from the KJV revision tradition; Webster 1833 is a KJV revision. Neither is to be labeled a word-for-word identical KJV text or assumed to preserve every KJV word/tag.
- **IMPLEMENTATION RULE:** Compare corresponding verses and actual word surfaces; carry all native KJV Strong's tags only across verified unchanged or unambiguous word correspondences. Record exact source/target tokens, verse, method, source tag array, confidence/evidence and unresolved cases. No invented original-language tag for an unmatched ASV/NWB word; no speculative theological sense selection. BSB source-native links remain independent.
- **DISTINCTION:** Noah Webster's **1833 Bible** is the translation being aligned here; Noah Webster's **1828 Dictionary** remains a separate later lexical resource, not a Bible translation.
- **STATUS:** Owner-approved method refinement only; Stage 8C not yet executed. Current Recovery Checkpoint 5 remains latest.



### 2026-11-07 | Stage 8B complete: BSB source-native alignment and Recovery Checkpoint 5
- **VERIFIED:** Original `SOTW_WordStudy_04_BSB_TEXT_ALIGNMENT_REFERENCES_2026-11-05.zip / source_files/bsb_tables.tsv` parsed: 754,647 table rows, 437,587 source-tagged original-language word records, 294,728 Hebrew, 4,728 Aramaic, 138,131 Greek. 31,102 explicit VerseId anchors overall, including 31,023 on tagged rows; 406,564 tagged rows inherit same-verse source anchor with strict verse-number boundary. No unanchored tagged records, malformed columns, or unexpected languages. 437,587/437,587 Strong's references resolve against Stage 7 dictionaries.
- **IMPORTANT SOURCE BOUNDARY:** BSB USFM/USJ/USX text has no inline Strong's word tags; BSB-native alignments originate in the source table, not KJV USFM. Preserve source row, Hebrew/Greek spelling, transliteration, compact/expanded parsing, source BSB English cell, and original verse anchor. This does not assert each sense applies to its verse. No inferred word alignment, no public release, no player change.
- **LATEST RECOVERY:** `SOTW_RECOVERY_CHECKPOINT_5_STAGE8B_2026-11-07.zip`, 27,942,305 bytes, SHA-256 `2397eac84985393216bd8a61ce7371960437d52b8638b015f7f3d50ebcec0e14`. Contains complete nested Checkpoint 4 plus Stage 8B compressed dataset, deterministic build, cross-check validator, report and README. ZIP CRC, member hashes and nested archive integrity PASS. Original source ZIPs remain separate.
- **NEXT:** Stage 8C supported KJV-derived NWB/Webster 1833 and ASV links, then morphology. No deployment.



### 2026-11-07 | Stage 8A complete: KJV source-native Strong's occurrence index and Recovery Checkpoint 4
- **VERIFIED:** Parsed original archived `eng-kjv2006_usfm.zip` (SHA-256 `ce1f526c64c2376f407308c2c23cb2d2fb58efaf5296327d2d8e408c3700650d`) across 66 books. 313,813 tagged word occurrences, 313,813 source-attested tag associations, 29,699 distinct verse keys with tagged words; 418 additional source-tagged pre-verse heading words retained without fabricated verse anchors. Zero unmatched Strong's IDs against Stage 7 H/G dictionaries; zero parser errors. Original source attribute and per-word tag array preserved.
- **SCOPE:** No multiple-tag occurrences found in this particular USFM source; parser models an array and does not collapse tags. Untagged words are not aligned by inference. No morphology claims. This is not BSB native alignment and not NWB/ASV derived mapping.
- **LATEST RECOVERY ZIP:** `SOTW_RECOVERY_CHECKPOINT_4_STAGE8A_2026-11-07.zip`, 8,976,183 bytes, SHA-256 `c8908fe6261905b174f51c341529ab535dd62a41f59c45d1d7ba1015f6b95a95`. Contains full nested Checkpoint 3 plus Stage 8A dataset, script, report and README. CRC, file SHA-256 and nested checkpoint ZIP checks PASS. Original source archives are not duplicated; owner download required.
- **NEXT:** Stage 8B BSB native source alignment, then supported NWB/ASV associations and morphology. Stage 8 overall remains IN PROGRESS. No public/player integration.



### 2026-11-07 | Stage 7 COMPLETE; Recovery Checkpoint 3 created
- **VERIFIED:** Built complete source-field projections for 8,674 Hebrew/Aramaic Strong's IDs and 5,624 Greek Strong's IDs (14,298 total). Hebrew: 8,674 concise explanations, 8,674 KJV rendering fields, 8,670 exegesis notes, 21,500 selected expanded senses, 2,680 proper-name glosses, and all 24,841 original source list items preserved. Greek: 5,523 headwords, 5,507 concise definitions, 5,522 KJV rendering fields, 5,510 derivations, 101 explicit Not Used placeholders, 324 supplemental source-prose entries.
- **CRITICAL EDITION BOUNDARY:** Selected Greek is **`strongs-dictionary-xml-master.zip / strongsgreek.xml` v1.9 (2019, CC0)**, XML SHA-256 `91474213b208a4e487d35f85c10e5c90737acc69082dad15dec5431406003545`, **not** the older v1.4 Greek file bundled in the Hebrew ZIP. Hebrew selected XML SHA-256 `1f9659ea208f4c498843a0280dacb1448627c33ca77712642d8705793ab66061`. Owner-accepted source declarations retained.
- **VERIFIED:** 31/31 automated Stage 7 checks passed. Includes runnable source-hash-checking ingestion, H/G Strong's ID lookup, original-language scripts/transliterations, pronunciation where sourced, source exegesis/derivation, rich inline refs, no fabricated Greek long-sense list, and provenance report. No other lexicon definitions imported and no reopened 202-marker audit.
- **NEW ONE-ZIP RECOVERY:** `SOTW_RECOVERY_CHECKPOINT_3_THROUGH_STAGE7_2026-11-07.zip`, **6,055,276 bytes**, SHA-256 **`fbd77e7078c1913fc1f077f4d8689d8a42da9f54b02674a2ffc1708c123993d5`**. Contains complete nested Checkpoint 2 plus Stage 7 data/scripts/tests, hashes and verifier. ZIP CRC, all 12 member hashes, nested checkpoint and Stage 7 tests PASS. It does **not** duplicate original source ZIPs or the private inspector. Owner must download it; not a GitHub upload or deployment.
- **NEXT:** Stage 8 source-attested word occurrence, multiple-tag and morphology hooks, then Webster 1828. No production player change.



### 2026-11-07 | Owner reorders Stage 7: Hebrew and Greek Strong's before Webster
- **OWNER DIRECTION:** Finish the original-language Hebrew/Greek foundation before adding Noah Webster's 1828 English dictionary. Earlier Stage 7 Webster plan is superseded; Webster remains queued, not canceled.
- **VERIFIED from archived original Strong's sources:** Hebrew `StrongHebrewG.xml` has 8,674 entry headwords, concise explanation notes, KJV rendering notes, lemma, transliteration, POS, morph and expanded sense lists. Current Stage 1 corrected projection only retained expanded sense/gloss fields, so it is **not a complete Strong's entry presentation**. Greek XML contains 5,624 entries and distinct `strongs_def`, `kjv_def`, derivation and Greek forms; not yet built.
- **FIELD DESIGN:** Concise Strong's explanation and KJV rendering are separate fields; expanded Hebrew senses are another source layer, not automatically a matching Greek 'long Strong's' field. Longer BDB/Thayer entries, when separately sourced and cleared, must remain distinct source-credited lexicon records.
- **NEXT:** Stage 7 complete Hebrew concise/original-script fields and Greek Strong's entries with validation, then original-language occurrence/morphology hooks and later Webster 1828. Recovery Checkpoint 2 remains current; no new ZIP yet.



### 2026-11-07 | Recovery Checkpoint 2 created through Stage 6
- **OWNER CONTINUITY RULE:** In new threads owner can supply original source archives plus exactly ONE latest recovery ZIP. Do not require separate incremental Stage 6 inventory ZIP.
- **VERIFIED:** `SOTW_RECOVERY_CHECKPOINT_2_THROUGH_STAGE6_2026-11-07.zip`, 3,291,131 bytes, SHA-256 `a4cbdbfd4b138a0d4c31e3d99ccb1485e33885d1c3f05a271db9149c64c364fa`.
- **CONTENTS:** Nested complete Recovery Checkpoint 1 (includes original Checkpoint 0, corrected Stages 1–4 and Stage 5 manifest) plus Stage 6 resource reconnection inventory. Outer manifest and `verify_recovery.py` included; archive CRC and SHA validation PASS.
- **EXCLUSIONS:** Original source ZIPs and the private inspector/public shell are not duplicated in this small recovery ZIP. Owner supplies them separately as original sources when needed. Stage 7 Webster integration is not yet built.
- **NEXT:** Stage 7 build Webster 1828 lookup using original preserved source, distinct from Webster 1833 Bible. Continue updating progress log every completed stage; next full recovery after about five stages or sooner for continuity risk.



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
