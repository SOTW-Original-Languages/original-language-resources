# SOTW Original Languages | LIVE PROGRESS LOG

**Updated:** 2026-11-07  
**Stage:** Stage 12C deterministic public-safe Word Study review projection COMPLETE, tests PASS; controlled demo-adapter integration NEXT, not yet authorized for deployment. Private Inspector Stage 11 browser gate separate.
**Status:** Stage 12A lexical source and Stage 12B 66-book accepted word evidence generated a **limited, allowlisted** 24 edition-verse/13 Strong's-entry/51 badge Word Study candidate for Genesis 1:1–3 and John 1:1–3. Exact comparison to accepted public demo v1.2: 24/24 verse texts, 36/36 native badges, 15/15 derived badges, 91/91 source lexical text fields matched after whitespace normalization. Two byte-identical builds, 15/15 regression tests PASS, SHA-locked original source inputs and outputs, zero private raw source records exposed. 26 KB review ZIP created as a conversation download only, not installed in public GitHub. Stage12C schema is **not** the live demo schema; public site/CGBC unchanged.
**Repository:** `SOTW-Original-Languages/original-language-resources`

> **START HERE IN A NEW THREAD.** This is the short, frequently updated work log. For binding decisions and detailed history, read [Durable Decisions](SOTW_DURABLE_DECISIONS_AND_CONTINUITY.md) and [Vetted Sources & Artifacts](SOTW_VETTED_SOURCE_AND_ARTIFACT_INDEX.md). This log does not supersede those records.

## Update rule (until a production script exists)

**At every substantive report-back, update this SAME file in GitHub.** Do not create a new progress file, replace the durable register, or leave the only checkpoint in chat. Use the latest GitHub version and its blob SHA before editing; preserve previous entries. Change the four lines above, update the CURRENT STATE and NEXT ACTION, then **prepend** a short dated entry to the UPDATE HISTORY. Include output ZIP filename, checksum if verified, and GitHub commit when known. Mark facts **VERIFIED**, **OWNER DECISION**, **UNVERIFIED**, or **BLOCKED**. Never call a chat ZIP installed or published.

## CURRENT STATE

- **VERIFIED (2026-11-07, Stage 12C):** Implemented deterministic `scripts/build_public_safe_projection_stage12c.py` consuming SHA-verified Stage12A complete lexical fields and Stage12B accepted native/derived adapter outputs. Strict public field allowlist generated `outputs/public_safe_review_candidate.json` (SHA-256 **`0f6a4fdb8295f743511a8d11e5c9f2bd186789821c1c418aedc1e6b3c11b8f99`**) with exactly the accepted demo v1.2 sample: Genesis 1:1–3 and John 1:1–3 in BSB/KJV/Webster1833/ASV, **24 edition-verse records**, 13 selected Strong's lexical entries (five Hebrew, eight Greek), 36 original BSB/KJV native demo badges and 15 exact accepted KJV-derived ASV/Webster badges. **All 91** selected headword/transliteration/short/numbered-sense/derivation/KJV-rendering/supplemental lexical field fingerprints match approved GitHub demo blob `a2cb4a4cd1303efb63c3583f43a3e0a76023b9fc`; wording independently sourced from Stage12A, not copied from the fixture. Raw KJV tag ordinal and BSB source line **NOT** conflated with approved demo English display-word positions; derived 0-based target token and surface verified directly from Stage12B. Full original 12A/12B manifest SHA checks and three owner-held predecessor ZIP SHA checks PASS. Two complete Stage12C builds byte-identical; 15/15 unit/regression tests PASS, including altered lexical word, incorrect derived token, source-only/private-field exclusion and output corruption detection. Output manifest SHA-256 `48879c119b72315e9a809b0e0ae7a7fd89cdc63c279794b3322bb18392c6775e`. No new source or word-link audit; source rights and provenance remain owner-accepted.
- **LATEST PRIVATE/REVIEW INCREMENTAL (2026-11-07):** `SOTW_STAGE12C_PUBLIC_SAFE_REVIEW_PROJECTION_2026-11-07.zip`, **26,247 bytes**, SHA-256 **`d2a6a5758d0d7f87dd1d1ae3e2d7537ab5cc678b55bb1469b83a594b39909e2c`**; 11 ZIP entries, CRC PASS, all 10 payload member SHA checks PASS. Contains standard-library processor, two pinned approved-demo comparison fixtures, 15-test suite, small candidate JSON, comparison report, deterministic manifest, SHA manifest, README and QA report. This is a **conversation artifact only**, not installed in public GitHub, not a replacement for Recovery Checkpoint 12, not Stage13. Candidate JSON schema is separate from existing `demo/word-study/sample-data.json`; **no public demo file overwritten**. No CGBC changes or private corpora uploaded.
- **VERIFIED (2026-11-07, Stage 12B):** Deterministic owner-approved source processor `scripts/build_bible_word_adapters_stage12b.py` consumes SHA-locked Recovery Checkpoint 12 Stage 8A–8D source records and Stage 12A lexicon ID index. Original source records preserved intact inside typed private edition-specific JSONL envelopes, with canonical book.chapter.verse reference, source/target locators, multiple-tag support and valid `strongs:H/G` IDs. Source partitions: 313,395 KJV native verse tags, 437,587 BSB native tagged original-language rows, 223,941 ASV KJV-derived and 247,165 Webster Bible 1833 KJV-derived associations = **1,222,088 supported/native records**. Additional 418 KJV pre-verse heading tags retain `verse_id: null`; 1,052 explicit withheld cases remain **unlinked** (993 multi-token/compound, 59 cursor-unmapped). Full preserved adapter input count = **1,223,558**. BSB native morphology retained only in BSB source index; no transfer into other editions. BSB accepted Genesis 2:1 source row `verse_number_in_source: '32'` preserved rather than mistaken for canonical verse. Stage 8B indexed 437,587 tagged rows from its wider 754,647 original table rows, not all BSB English tokens. All Stage 12A lexical IDs resolve; no contextual/sense claims introduced. 66 books. 120,090 seek-indexed edition verse groups. QA: 14/14 regression tests PASS, 2 full byte-identical builds, complete file/byte-range SHA checks and 1,244 decoded verse groups spotchecked. Output manifest SHA-256 `96af7c8e26509dc28001ea1cebeb99504ca6143af33ff26d1bb491b878203c61`.
- **PRIVATE INCREMENTAL PACKAGE VERIFIED (2026-11-07):** `SOTW_STAGE12B_PRIVATE_EDITION_WORD_ADAPTERS_2026-11-07.zip`, **56,646,092 bytes**, SHA-256 **`7c3a04ceca0174e178a3f299503b86a9ac8169e1da5893f5d6fd6c9a68f36e90`**, 14 ZIP members, CRC PASS, 13 recorded payload-member SHA-256/size checks PASS. It contains original-source-preserving processed JSONL partitions, direct verse lookup, source-only BSB morphology index, deterministic manifest, processor, 14-test suite, README, QA report and package member SHA manifest. Conversation download only; **NOT** uploaded to public GitHub or incorporated into full recovery ZIP. Keep Checkpoint 12 and Stage 12A private separately. No source/rights re-review, public site code, CI/schema, or CGBC changes.
- **VERIFIED (2026-11-07, Stage 12A):** Full-field deterministic private source processor `scripts/build_lexical_stage12a.py` executed against `SOTW_RECOVERY_CHECKPOINT_12_BROWSER_HANDOFF_2026-11-07.zip` (SHA-256 `d5c7547659bcdc4bca4024e85405b7d4817808e6d2cf2b59570c9392a2f68105`). Pinned Stage 7 member hashes checked before build; 8,674 H IDs and 5,624 G IDs retained in source-complete records and deterministic direct lookup index with full original Stage 7 object preserved per record, including `x-pn`, historical text segments, source claims and Greek `Not Used`. Source-report presence vs nonblank differences **H5223** (empty derivation text) and **G2022** (empty concise text) preserved explicitly; nothing invented/removed. 8/8 tests PASS; two builds byte-identical; all 14,298 output record offsets and SHA verified; SHA manifest `8aedd305ea08cb4f9c63181f23410cd268f0cc91a05d2dfd5444257e8fe1ba95`. No new copyright vetting or global word-link audit performed.
- **LATEST INCREMENTAL WORKING PACKAGE (not full recovery, 2026-11-07):** `SOTW_STAGE12A_PRIVATE_FULL_FIELD_PROCESSING_2026-11-07.zip`, **3,648,653 bytes**, SHA-256 **`1112a0c62543e2cfea16042ebc64979cce0f36ff6da5e853c6600e973b219072`**. Contains runnable standard-library script and 8-test suite, full privately generated 14,298 record JSONL results, lookup offsets, deterministic manifest, usage notes, QA report and per-member SHA manifest. ZIP CRC and 10 included member hashes PASS. This is an owner-downloadable conversation artifact, **not yet stored in GitHub**. Do not upload entire ZIP or private JSONL to public repo. Recovery Checkpoint 12 remains the latest complete development handoff; not Checkpoint 13.
- **OWNER DECISION (2026-11-07, settled):** The owner has inspected v1.2 in the real browser and says the display looks good. Existing word-link evidence, its sourcing and provenance are sufficient and trusted. All existing deliberately chosen SOTW sources and their documented rights are **approved and accepted**; no blanket re-vetting or reapproval prerequisite before Bible script development. Preserve source-specific attribution and licenses already accepted (including Webster 1828 CC BY-SA 4.0), preserve unresolved/not-native distinctions, and review only concrete defects or genuinely new sources/uses. These decisions are recorded in Durable Decisions, not a claim that private data has been released.
- **VERIFIED (2026-11-07, Word Study demo v1.2):** Following owner feedback that the short Strong's wording was not visibly differentiated, the public `/demo/word-study/` now shows explicit always-present **(1) source-authored concise** and **(2) expanded/full source material** sections; Hebrew's five sample entries display source-numbered expanded senses, Greek's eight sample entries truthfully indicate there is no separately numbered Greek long-sense list in the selected v1.9 XML. Derivation, KJV renderings, supplemental source notes, original-language encoded attributes and source provenance remain individually visible. The `#source-review` audit area enumerates all 13 selected sample entries and field availability, two selected source/XML hashes, publisher/digital editorial attribution and per-resource rights; it explains the wider 8,674 Hebrew / 5,624 Greek private research scope is NOT displayed. No STEP/BDB/Thayer/TWOT definitions copied. No new word alignments or private corpus uploaded. Source-level + syntax checks PASS, mocked DOM clicks PASS for both Strong's layers, 13-entry inventory, attribution, ASV 3/3, derived badge and Webster. **NEW v1.2 live browser/mobile owner acceptance PENDING**.
- **VERIFIED (2026-11-07, owner v1 browser screenshots):** Public `/demo/word-study/` loads, Genesis 1 KJV native H8064 badge opens a Hebrew Strong's panel, John 1 BSB English `beginning` opens Webster 1828 with source row, and John 1 ASV 1901 displays all three verses with pinned GitHub source `3/3` exact-match status. These are specific owner-observed public demo checks; they do not prove every translation/badge or the private 66-book Inspector passed.
- **VERIFIED (2026-11-07, v1.1 targeted public-demo repair):** From SHA-matched Checkpoint 12 Stage 7 selected original Strong's projections, updated all 13 displayed lexicon entries with actual selected-source derivation and KJV rendering; five Hebrew entries also have original numbered expanded senses; the eight Greek entries have no falsely invented long numbered list and preserve source-authored supplemental notes when present. Added 15 ASV1901 / WEBSTER1833 **KJV-derived research-association** badges on Genesis 1:1 and John 1:1, in distinct outline style, from Stage 8C exact-unique matching and Stage 8D token audit, each independently matched to exact displayed English surface; 36 BSB/KJV native badges remain unchanged. Excluded H853 on English `and`, and ambiguous repeated words including John 1:1 `Word`. No new alternative lexicons imported and no semantic equivalence implied. JavaScript syntax, integrity count and simulated UI checks PASS. v1.1 live browser user acceptance **PENDING**.
- **VERIFIED (2026-11-07, GitHub source):** Owner-approved separate `demo/word-study/` uploaded: `index.html`, `app.js`, `sample-data.json`, and `README.md`. It previews `GEN.1.1`–`GEN.1.3` and `JHN.1.1`–`JHN.1.3` in BSB, KJV1769, WEBSTER1833 and ASV1901 (24 edition-verse records). 36 explicitly native BSB/KJV Strong's source link badges resolve to 13 selected historically sourced lexical headwords. Any English word can request existing root `../../webster1828.json`; ASV runtime checks the separately published pinned chapter data with transparent fallback. BSB/KJV/Webster excerpts are limited source-backed archived data. No private corpus, unresolved linkage promotion, or production player edit.
- **VALIDATED (new demo, 2026-11-07):** JavaScript syntax PASS; 24 verse IDs and all 36 native source link positions checked; all H/G badges resolve; sensitive/private marker scan of public sample JSON PASS; browser-like simulated DOM test PASS for edition switching, Genesis→John selection, selected Strong's panel, Webster exact-headword panel and pinned ASV 3/3 sample comparison. **NOT YET TESTED:** actual live GitHub Pages new-demo load, cross-origin ASV request in owner browser, desktop/mobile presentation, and private 66-book Stage 11 end-to-end browser test. The earlier public Webster homepage was owner-verified separately.
- **VERIFIED (2026-11-07 local Stage 11 preparation):** `SOTW_STAGE11_MAC_TEST_LAUNCHER_2026-11-07.zip` is a separate **test-only convenience helper**, 5,569 bytes, SHA-256 `9a79648b2d438e8dbdfaa16c034dd2dbc2584f2ffd65089cc029d9f835637dba`; it contains no private corpus. Local self-test verified Checkpoint 12 SHA/ZIP, extracted the nested private Stage 10 Inspector, and started its loopback-only HTTP viewer. This environment still blocks Chromium navigation; **no Playwright browser PASS**. The Mac runner is untested on the owner's machine until the owner executes it. Not Checkpoint 13.
- **VERIFIED (GitHub commit `c06c9ad9b7863ce85acd1fae09b3f20fa4bc0dfc`):** Public-safe static Webster 1828 demo files `index.html`, `webster1828.json`, `LICENSE_WEBSTER_SOURCE.txt`, and `README_UPLOAD.txt` are at repository root. GitHub Pages is serving `https://sotw-original-languages.github.io/original-language-resources/` following owner switch from `/docs` to `/(root)`. This public demo is a direct dictionary headword lookup, **not** the private verse-click Inspector or Strong's integration.
- **OWNER-VERIFIED (2026-11-07 public website smoke test):** Owner opened the live page, showed ASV 1901 `grace` lookup with 62,388 loaded searchable headwords and source-attributed dictionary entry, and subsequently confirmed checking the remaining BSB/KJV/Webster 1833 selectors plus suggested `love`, `faith`, `covenant`, and nonexistent-headword cases successfully. These are owner-reported browser checks, not an independently executed private Stage 11 browser test or a corpus-wide audit.
- **RECOVERY VERIFIED (2026-11-07):** Local `SOTW_RECOVERY_CHECKPOINT_12_BROWSER_HANDOFF_2026-11-07.zip` bytes rechecked, 86,109,814 bytes, SHA-256 `d5c7547659bcdc4bca4024e85405b7d4817808e6d2cf2b59570c9392a2f68105`, ZIP CRC PASS. This remains the latest complete development recovery; no new consolidated checkpoint was created for the separately deployed public demo.
- **VERIFIED:** Selected Hebrew Strong's digital OSIS source is `strongs-master.zip / strongs-master/hebrew/StrongHebrewG.xml`, inside `SOTW_WordStudy_03_DICTIONARIES_LEXICONS_KJV_WEBSTER_2026-11-05.zip`. Original XML SHA-256: `1f9659ea208f4c498843a0280dacb1448627c33ca77712642d8705793ab66061`.
- **VERIFIED (2026-11-07 source inspection):** Hebrew OSIS source has 8,674 `lemma`, transliteration (`xlit`), POS, morphology, concise `note type=explanation`, and KJV `note type=translation` fields, plus expanded numbered list items. Stage 7 has now restored these source-authored Hebrew fields in a separate complete research projection, alongside the earlier expanded senses. The selected Greek CC0 XML **v1.9** has now been projected with all 5,624 entries, including source-absent fields and 101 explicit Not Used placeholders. Neither is yet integrated into a public site. Distinct BDB/Thayer/STEP resources remain separate candidates/hooks, not merged Strong's definitions.
- **VERIFIED (research):** 8,674 entries; 24,841 original list items; 21,500 numbered senses and 2,680 proper-name glosses in the selected-content classification. Source language markers: 6,046 Hebrew/Aramaic and 2,628 `x-pn` proper-name markers that must **not** be miscast as a language.
- **OWNER DECISION:** Use the widely distributed, public-domain-designated Strong's digital edition as the practical foundation. Do not rebuild a word-perfect 1894 edition or require a PDF scan comparison. Preserve source and digital editorial provenance. No external STEP, Open Scriptures, TWOT, BDB, or CLBL **alternative dictionary definitions** are to be imported for public display. Owner-settled normalization is closed; **do not reopen the 202-marker attribution audit or strip senses**. Stage 7 retains source-authored content and is research-only, not a new public-normalization approval.
- **VERIFIED (internal research):** A source-attribution audit found 202 explicitly labeled sense items in 178 entries in the raw research record. These are **source/audit markers, not 202 new imported sources or newly proven defects**. The earlier 14-unavailable stripped projection was an audit variant, **not** the approved final display.
- **VERIFIED (research):** `SOTW_STRONGS_LOOKUP_RESEARCH_INDEX_2026-11-07.zip` indexes 8,674 Strong's IDs, 12,457 searchable tokens, 24,180 sense/name-gloss items, and 55 literal cross-reference candidates. These hooks are **not** verified semantic links and the index is **not public-ready**.
- **CLARIFICATION:** This thread produced research projections, a ten-entry presentation preview, and a lookup index; the record does not establish that a separate approved full public baseline file was ever created. The owner's zero-marker statement is a settled normalization/presentation expectation, not evidence of a missing file. Do not keep asking the owner to locate one.
- **RELEASE BOUNDARY:** Only the isolated public-safe static Webster 1828 dictionary demo is deployed. The private Inspector, full Bible texts, internal research, Strong's integrations, production scripts, canonical schema replacement, CGBC player modifications and player integrations remain outside that release; no authorization for those deployments is implied.

## NEXT ACTION (one task only)

**Stage 12D: design and test a versioned, isolated Word Study demo data adapter for the Stage 12C candidate, without replacing the working GitHub Pages site.** Ensure generated public-safe `stage12c` verse/lexicon/link fields can map exactly to the current `demo/word-study/sample-data.json` reader contract, preserving visible Strong's short/full, source/rights ledger, native/derived badge display, ASV pin and Webster 1828 external dictionary. Test mock DOM and fail closed on any missing/ambiguous display anchor; compare all 24 verses / 51 approved badges / 13 entries. Only after independent validation and owner approval may a controlled demo upload occur. Incremental Bible scale-out follows with separate edition storage and rights notices; maintain private Stage 11 browser gate and CGBC isolation.

## UPDATE HISTORY (newest first; append nothing above this heading except new entries)

### 2026-11-07 | Stage 12C COMPLETE: deterministic public-safe review projection, 15/15 QA PASS
- **IMPLEMENTED:** Python standard-library `build_public_safe_projection_stage12c.py` with strict output-field allowlist. Inputs are independently hashed 12A and 12B output manifests/files plus owner-approved v1.2 demo snippet reference; optionally validates all three original predecessor ZIP SHA-256 identities. No newly invented word links, new source rights interpretation, reprocessing of accepted Stage8 link evidence, or private raw source projection.
- **EXACT OWNER-DEMO MATCH:** 24/24 verse text samples, **36/36 native and 15/15 supported KJV-derived** approved display badges, **13/13 Strong's IDs**, and **91/91 selected original lexical fields** match accepted GitHub `demo/word-study/sample-data.json` blob `a2cb4a4cd1303efb63c3583f43a3e0a76023b9fc`. The 91-field fingerprinting is a comparison aid; original Stage12A SHA-256 locks remain authoritative data integrity. Native KJV tagged-word ordinal, BSB source line, and derived ASV/Webster 0-based English token positions remain separately typed; no contextual-sense or English-word equivalence invented.
- **QA:** 2 full builds byte-identical for candidate, report and manifest; **15/15 tests PASS**, including source/rights metadata, exact words/anchors, excluded alternative lexicons, no private fields, altered lexical definition rejection, wrong derived-token-position rejection, original versus derived status and output tamper detection. Candidate SHA-256 `0f6a4fdb8295f743511a8d11e5c9f2bd186789821c1c418aedc1e6b3c11b8f99`; manifest SHA-256 `48879c119b72315e9a809b0e0ae7a7fd89cdc63c279794b3322bb18392c6775e`.
- **DELIVERED INCREMENTAL PRIVATE/REVIEW ZIP:** `SOTW_STAGE12C_PUBLIC_SAFE_REVIEW_PROJECTION_2026-11-07.zip`, 26,247 bytes, SHA-256 `d2a6a5758d0d7f87dd1d1ae3e2d7537ab5cc678b55bb1469b83a594b39909e2c`. Outer ZIP CRC, 10 member SHA hashes PASS; source code/tests/fixtures/review candidate only, **not** source corpora or recovery. This is a conversation download only, not uploaded to GitHub.
- **UNCHANGED:** Existing published Webster homepage and Word Study demo, separate ASV repository, locked source/evidence decisions, Stage12A/B private packages, complete Recovery Checkpoint12, CGBC production. New candidate schema **cannot** be dropped into the existing demo unadapted. Private 66-book Inspector Stage11 browser gate remains open.
- **NEXT:** Stage 12D compatibility adapter with strict no-silent-substitution checks; validate against working demo, request specific approval before deploying changed Pages files.

### 2026-11-07 | Stage 12B private 66-book word-link adapter pipeline COMPLETE: 14/14 QA PASS
- **IMPLEMENTED / OWNER-TRUSTED INPUT:** Deterministic Python-standard-library Stage 12B script reads SHA-locked Recovery Checkpoint 12 Stage 8A native KJV, 8B native BSB, 8C supported ASV/Webster 1833 and 8D withheld/morphology; resolves all tags via the separately preserved Stage 12A 14,298-lexicon ID index. No source-vetting or blanket link-audit rerun. Full raw source object retained for every output row.
- **COUNTS:** Native KJV 313,395 verse tags; native BSB tagged source-table rows 437,587; ASV supported KJV-derived 223,941; Webster 1833 supported KJV-derived 247,165. **1,222,088** native/supported link records. Separate **418** pre-verse KJV headings (`verse_id: null`) and **1,052** explicitly withheld sources (993 compounds and 59 cursor failures), never converted into new verse links. **1,223,558** total preserved record envelopes. Source 8B original whole table has 754,647 rows; 437,587 is its source-tagged projection, not full BSB English word coverage.
- **SOURCE FIDELITY:** Preserved distinct **KJV tagged-word ordinal**, **BSB original source-table line and form/parsing**, and **ASV/Webster 0-based English target token index**; no fabricated original-language source occurrence or contextual semantics. Retained Genesis 2:1 BSB source's `verse_number_in_source='32'` verbatim while canonical key is `GEN.2.1`. BSB morphology remains source-only; no cross-edition inheritance.
- **QA:** 2 complete output builds have identical manifest + 8 file hashes; 14/14 tests PASS for source/ZIP SHA pins, 66-book coverage, linked/withheld partitions, 120,090 verse-group byte-offset index/size cover, 1,244 content spotchecks, native/derived separation, preserved headings, wrong-source and corruption rejection. Output manifest SHA-256 `96af7c8e26509dc28001ea1cebeb99504ca6143af33ff26d1bb491b878203c61`.
- **PRIVATE PACKAGE:** `SOTW_STAGE12B_PRIVATE_EDITION_WORD_ADAPTERS_2026-11-07.zip`, 56,646,092 bytes, SHA-256 `7c3a04ceca0174e178a3f299503b86a9ac8169e1da5893f5d6fd6c9a68f36e90`; ZIP CRC PASS and 13 member hashes PASS. Contains 14 files including complete processed link streams, offsets, script, tests, manifests and README. **Not** installed in public GitHub; owner downloads privately. This is *incremental*, not a new full recovery Checkpoint 13.
- **UNCHANGED:** Owner-accepted source decisions and attribution; Stage 12A private full lexical build; Recovery Checkpoint 12 full original evidence; public Webster and Word Study demos; independent ASV and other Bible repositories; CGBC player. Private Stage 11 browser certification remains separate.
- **NEXT:** Stage 12C safe deterministic public/owner-demo output projection, start with two passage examples and strict field allowlist, then scale only with versioned release conditions. No private corpus upload.

### 2026-11-07 | Stage 12A COMPLETE: deterministic private Strong's full-field processing; 8/8 QA PASS
- **IMPLEMENTED AND EXECUTED:** Owner-approved source/evidence baseline reused from SHA-verified Recovery Checkpoint 12, nested Stage 7 Hebrew and Greek full-field projections; no source re-vetting. Standard-library `build_lexical_stage12a.py` verifies exact Checkpoint SHA, exact Stage 7 output hashes and reported coverage, then serializes each **complete unchanged source record object** into a private line-by-line envelope with stable `strongs:Hn/Gn` IDs, selected source XML hash, accepted provenance and no public-release claim.
- **OUTPUT COUNTS:** 8,674 Hebrew + 5,624 Greek = **14,298** IDs, direct seek index with per-record offsets/lengths/SHA-256, and deterministic manifest. Hebrew 21,500 numbered senses, 2,680 proper-name glosses, 24,841 raw list items, 2,628 `x-pn` proper-name-category markers preserved; Greek 101 `Not Used` placeholders. Source presence does not guarantee nonblank: `H5223` derivation and `G2022` concise explanation are present but empty, faithfully preserved.
- **QA:** Two full builds generated byte-for-byte identical private outputs and manifest. 8/8 tests passed: pinned checkpoint, full coverage, deterministic reproducibility, rich source preservation, Greek placeholder, blank-but-present fields, corrupt output rejection, wrong input SHA rejection. Re-read all **14,298** pointers and hashes PASS. Manifest SHA-256 `8aedd305ea08cb4f9c63181f23410cd268f0cc91a05d2dfd5444257e8fe1ba95`.
- **DELIVERED (downloadable private incremental):** `SOTW_STAGE12A_PRIVATE_FULL_FIELD_PROCESSING_2026-11-07.zip`, 3,648,653 bytes, SHA-256 `1112a0c62543e2cfea16042ebc64979cce0f36ff6da5e853c6600e973b219072`, 10 members, outer CRC and member SHA checks PASS. Includes script, tests, private full working records, lookup, QA/manifest/README. This ZIP exists as conversation artifact **not as a GitHub file**. Its source remains Checkpoint 12, not a replacement full recovery ZIP.
- **RELEASE BOUNDARIES:** No public lexical corpus upload, repo code upload, new source-rights decision, semantic meaning invention, data/word-link correction, public demo change, browser certification, CGBC player edit, or deployment. Existing owner-approved source and link evidence trusted.
- **NEXT:** Stage 12B edition-aware deterministic adapters using accepted Stage 8A–8D evidence and Stage 12A private full-field lookup; preserve source distinctions, linked/unlinked states and stable hashes.

### 2026-11-07 | Owner confirms source selection, rights and word-link evidence are accepted; script engineering next
- **OWNER DECISION:** All currently selected SOTW source packages were deliberately chosen and source rights already vetted, approved and accepted. Existing word-link sourcing/provenance/evidence is sufficient and trusted. Stop treating source selection, generic rights re-review or global Stage 8C/8D alignment re-audit as blockers for deterministic script work.
- **OWNER BROWSER REVIEW:** Owner's screenshot shows the v1.2 13-entry source/attribution overview displaying correctly and owner says it looks good. Do not over-interpret this as a comprehensive test of the private 66-book Inspector or each full-source entry.
- **CONTINUITY:** Durable Decisions updated with settled selection/rights and linkage decisions. Preserve the approved license conditions and credited sources (notably Webster 1828 CC BY-SA 4.0), precise source hashes and evidence status. No source modifications, new imports, schema changes or production deployment.
- **NEXT:** Begin deterministic full-library processing-script design and validation plan using accepted source/evidence inputs; focus on field coverage, transform integrity, reproducibility, safe publishing projections and attribution carry-through. Only investigate specifically observed failures or genuinely new scope. Private Stage 11 browser test remains open.

### 2026-11-07 | Public Word Study v1.2: unambiguous concise/expanded fields plus 13-entry attribution inspector
- **OWNER REQUEST:** Display both Strong's concise and expanded/full source material, make every already-prepared *sample* field inspectable, and show proper historical author/digital editor/source attribution so rights can be reviewed before automated Bible-wide production. The owner noticed the short wording was not clearly visible in v1.1.
- **IMPLEMENTED:** Revised only `demo/word-study/app.js`, `index.html`, `sample-data.json`, `README.md`. Each badge or inventory entry shows a prominent **1. concise definition** and separate **2. expanded/full source material**, plus derivation, KJV renderings, optional supplemental note, source-script/transliteration/encoded metadata, literal references as *unverified reference metadata*, provenance and rights. v1.2 cache-versioned JS/data URLs avoid stale client scripts. The catalogue lists all 13 demo entries and shows field presence, not an invented full corpus.
- **CREDIT/RIGHTS DISPLAY:** James Strong historical author for both selected digital Strong’s editions; selected Hebrew OSIS source-declared Public Domain; Greek XML v1.9 source-declared CC0 plus Ulrik Sandborg-Petersen digital editor; Noah Webster 1828 historical work and `akaitsurugi/webster1828` CC BY-SA 4.0 digital transcription/source license; BSB publisher public-domain dedication; KJV/Webster 1833/ASV edition and source provenance. Explicitly **no imported STEP, BDB, Thayer or TWOT definition text**; a source-native TWOT reference candidate is not a definition.
- **BOUNDARIES:** Five Hebrew preview examples have original numbered senses; eight Greek examples have no separately numbered long-sense list in the chosen Greek XML and are labelled accordingly. The private Stage 7 research projection contains 8,674 Hebrew and 5,624 Greek entries; **the public demo exposes only 13 approved sample records, NOT those entire corpora**. No new associations or production changes. Previous source-selection decisions and recovery Checkpoint 12 remain unchanged.
- **VALIDATION:** Public sample JSON parse/schema/13-entry field inventory PASS; original-language encoded metadata presence 5/5 Hebrew and 8/8 Greek; JavaScript syntax PASS; simulated browser DOM interactions PASS for Hebrew concise+full, Greek concise+truthful absent long list, inventory/attribution panels, ASV 3/3, ASV-derived H badge and Webster 1828. **Real v1.2 browser/mobile owner retest PENDING**.
- **NEXT:** Owner inspect `/demo/word-study/#source-review` and examples, confirm field/attribution presentation before authorizing any broader batch script work. Checkpoint 12 retained; CGBC untouched.

### 2026-11-07 | Owner browser findings addressed in Word Study public demo v1.1, extended-source and derived badges
- **OWNER-OBSERVED v1 PASS (scope limited):** Screenshots of deployed demo show functioning Genesis KJV H8064 Hebrew Strong’s panel, John BSB `beginning` Webster 1828 entry, John ASV source `3/3` exact pinned verse comparison. Owner noted selected Strong’s displayed only concise explanations and ASV/Webster 1833 lacked Strong’s badges.
- **TARGETED SOURCE REPAIR:** Using SHA-verified Checkpoint 12 nested Stage 7 selected Strong’s research projections, added actual source derivation and KJV rendering for all 13 sample lexical entries; five Hebrew entries additionally expose their original numbered senses. Greek selected CC0 v1.9 XML has no equivalent separately numbered long-sense list; no false one or imported BDB/Thayer/STEP meaning was added. Selected source spelling and historical quirks preserved.
- **KJV-DERIVED PREVIEW LINK EVIDENCE:** Stage 8C Stage 8D research independently checked against displayed target word positions. 15 source-supported exact-unique matches on ASV/Webster Genesis 1:1 and John 1:1 now appear as **outlined KJV-derived research associations**, distinct from the 36 native BSB/KJV badges. Exclude KJV H853 on English `and` and repeated ambiguous English word surfaces including John 1:1 `Word`; no fabricated contextual meaning or 66-book release certification.
- **GITHUB CODE:** Updated `demo/word-study/sample-data.json`, `app.js`, `index.html`, `README.md` with independent source locks and explicit method. Same path, prior commits retained as rollback. No new database sidecar or private source upload.
- **CHECKS:** 24 edition-verses, 13 historical lexical entries, 5 Hebrew expanded records, 8 Greek records without numbered long list, 36 source-native and 15 separate KJV-derived badges: structural checks PASS. JavaScript syntax PASS. Simulated DOM checks PASS for Hebrew expanded fields, Greek field boundary, derived badge evidence notice, Webster lookup and pinned ASV 3/3 status. **New v1.1 real browser tests PENDING**, including mobile.
- **PRESERVED:** Existing root Webster dictionary homepage, original source archives, Checkpoint 12 SHA-256 `d5c7547659bcdc4bca4024e85405b7d4817808e6d2cf2b59570c9392a2f68105`, independent ASV repository and CGBC production. Private Inspector Stage 11 still open.
- **NEXT:** Owner visually verify new long-source panels and outlined ASV/Webster research badges in deployed web demo; repair actual issues only.

### 2026-11-07 | Public-safe Word Study demo committed (Genesis 1 / John 1); owner live browser check next
- **OWNER-APPROVED:** Build and upload a separate public-safe website demo rather than treating a Mac-only private browser runner as the only route to visible UI testing. Keep ASV as the sole independently hosted full Bible edition; other translation text is a minimal source-backed sample, not full deployment.
- **GITHUB FILES:** `demo/word-study/index.html`, `app.js`, `sample-data.json`, `README.md`. Original root `index.html` and `webster1828.json` untouched; no CGBC integration or production script changes.
- **VERIFIED STATIC/MOCK INTERACTION:** JavaScript syntax PASS; 24 edition-verse records, 13 limited Strong's historical source headwords, 36 selected source-native BSB/KJV link badges with valid positions; no known internal private markers in public JSON. Simulated UI checked 3/3 pinned-ASV text comparisons, BSB Strong's panel, Webster headword lookup, and Genesis/John navigation: PASS. Full source hashes/rights and limitations are documented in the demo README.
- **PUBLIC PATH:** `https://sotw-original-languages.github.io/original-language-resources/demo/word-study/` (expected Pages URL). **NOT YET LIVE BROWSER VERIFIED** by owner or independent browser; no real mobile/browser PASS claimed.
- **PRESERVED:** Owner-verified standalone Webster homepage remains separate. The private 66-book Inspector Stage 11 browser test is still open; its recovery package remains `SOTW_RECOVERY_CHECKPOINT_12_BROWSER_HANDOFF_2026-11-07.zip` with SHA-256 `d5c7547659bcdc4bca4024e85405b7d4817808e6d2cf2b59570c9392a2f68105`; no Checkpoint 13 created.
- **NEXT:** Owner tests the new public demo (all editions, both passages, English words, H/G badges, ASV source status and mobile) and sends observed failures for targeted repair.

### 2026-11-07 | Stage 11 private Mac browser-test launcher packaged (test-only)
- **VERIFIED (local):** Revalidated unchanged Recovery Checkpoint 12 SHA-256 and ZIP CRC. Extracted the nested Stage 10 private Inspector and successfully started its loopback-only HTTP viewer; no source/data modifications.
- **BLOCKED (this environment):** Chromium still returns `net::ERR_BLOCKED_BY_ADMINISTRATOR` on navigation, including a simple data URL. This is not a browser PASS, and private Stage 11 remains open.
- **CREATED (not deployed):** `SOTW_STAGE11_MAC_TEST_LAUNCHER_2026-11-07.zip` (5,569 bytes, SHA-256 `9a79648b2d438e8dbdfaa16c034dd2dbc2584f2ffd65089cc029d9f835637dba`). Contains `RUN_STAGE11_MAC.command`, `run_stage11.py`, `README_FIRST.txt` only; derives its private local test inputs from the owner-held Checkpoint 12 ZIP, does not publish any corpus or replace the original Stage 11 test. Archive ZIP CRC and Python syntax PASS. Mac end-to-end run is **NOT YET OWNER-VERIFIED**.
- **UNCHANGED:** Checkpoint 12 remains the latest full recovery. Public Webster Pages deployment remains a separate owner-verified standalone dictionary demo. No CGBC production change.
- **NEXT:** Owner runs the local Mac helper with Checkpoint 12, completes visual edge checks and returns `STAGE11_RESULTS.json` for evidence-based Stage 11 completion or targeted repair.

### 2026-11-07 | Public Webster 1828 GitHub Pages deployed and owner-smoke-tested; Stage 11 private test remains open
- **VERIFIED (GitHub):** Commit `c06c9ad9b7863ce85acd1fae09b3f20fa4bc0dfc` added root `index.html`, `webster1828.json`, `LICENSE_WEBSTER_SOURCE.txt` and `README_UPLOAD.txt`. Owner changed GitHub Pages source from `main:/docs` to `main:/(root)`. The public demo appeared at `https://sotw-original-languages.github.io/original-language-resources/`.
- **OWNER-VERIFIED (public browser smoke test):** Screenshot shows `ASV 1901` + `grace` returning a source-authored Webster 1828 entry after loading 62,388 headwords. Owner reports completing the other translation selector and suggested lookup/missing-headword checks successfully. This test covers direct headword lookup only; it does not test verse-click navigation or Strong's in the private Inspector.
- **RECOVERY RECHECK:** `SOTW_RECOVERY_CHECKPOINT_12_BROWSER_HANDOFF_2026-11-07.zip`, 86,109,814 bytes, SHA-256 `d5c7547659bcdc4bca4024e85405b7d4817808e6d2cf2b59570c9392a2f68105`; ZIP CRC PASS. Checkpoint 12 remains current; no new recovery ZIP needed for this documentation-only milestone.
- **BLOCKED / UNCHANGED:** Private Stage 11 owner-local Playwright browser test remains unexecuted/uncertified; no private 66-book corpus upload, production script, new public Strong's/translation link assertions, or CGBC player modification.
- **NEXT:** Execute the Checkpoint 12 `SOTW_STAGE11_BROWSER_HANDOFF_2026-11-07.zip` test against the private Inspector on an owner-controlled localhost browser, save JSON results, inspect mobile and edge cases, and repair only demonstrated failures.

### 2026-11-07 | Stage 11 browser follow-up: navigation restriction reproduced; Checkpoint 12 test handoff
- **REPRODUCED:** Playwright Chromium navigation returned `net::ERR_BLOCKED_BY_ADMINISTRATOR` for localhost, local file and even data: page. No browser PASS asserted and no source/UI modification.
- **CREATED:** Owner-local Playwright script `test_browser.py` tests four translation cards, Webster 1828 word clicks for BSB/KJV/Webster 1833/ASV, Strong's + Webster panel coexistence, license visibility and JavaScript errors; emits machine-readable PASS/FAIL/BLOCKED results. README includes manual visual and missing-word tests. Script syntax compilation PASS; real browser execution remains blocked in this environment.
- **LATEST RECOVERY:** `SOTW_RECOVERY_CHECKPOINT_12_BROWSER_HANDOFF_2026-11-07.zip`, 86,109,814 bytes, SHA-256 `d5c7547659bcdc4bca4024e85405b7d4817808e6d2cf2b59570c9392a2f68105`; contains complete Checkpoint 11 plus test-only handoff. ZIP CRC PASS. Original source archives remain separate.
- **NEXT:** Owner-local real-browser validation, then targeted fixes only. No deployment.



### 2026-11-07 | Stage 11 verification: 14/14 supported checks PASS; browser navigation BLOCKED
- **LIVE API:** Tested local loopback Python server against Webster 1828 `love` headword for BSB, KJV, Webster 1833 and ASV 1901, casefold, missing headword and invalid edition: PASS. Local site serves. UI static wiring shows four translation order, clickable English words, separate Strong's action, safe plain-text rendering, CC BY-SA attribution and loopback-only binding: PASS. Total **14 passed checks**.
- **NOT VERIFIED:** Playwright Chromium navigation to localhost returned `net::ERR_BLOCKED_BY_ADMINISTRATOR`. Browser click/visual test therefore **BLOCKED** (15th check), not passed. No release certification and no UI code change; owner-machine browser validation remains necessary.
- **LATEST RECOVERY:** `SOTW_RECOVERY_CHECKPOINT_11_STAGE11_VERIFICATION_2026-11-07.zip`, **86,105,977 bytes**, SHA-256 `0b97a5c22214dc99b2f14688f60a6257ad8df73095b6c3edb9b987c7f4534d5d`. Includes nested complete Checkpoint 10 and Stage 11 report/README ZIP; CRC checks PASS. Original archives separate. Private inspector must not be published wholesale.
- **NEXT:** Complete real browser validation in a permitted environment and address actual defects only. No deployment.



### 2026-11-07 | Stage 10 COMPLETE: private local Webster 1828 inspector integration; Checkpoint 10
- **IMPLEMENTED:** Extended original 66-book private inspector, preserving its existing `site/data/` and Strong's evidence behavior. All English words in BSB, KJV, Webster 1833 and ASV are clickable for a direct Webster 1828 exact-headword lookup, independent of Strong's. Existing Strong's-linked words retain their Strong's detail action and additionally open the Webster dictionary panel. Definitions served from Stage 9 SQLite by a loopback-only Python endpoint `/api/webster`; source HTML rendered as plain text, not injected as markup. Source edition is validated; no stemming, sense selection or inferred Strong's tags.
- **VERIFIED:** 7/7 Python integration checks passed: direct dictionary lookup for each edition, case normalization, missing-word response, invalid edition rejection, and safe plain-text output. Original private inspector assets and 66-book dataset retained. No real browser interaction regression was performed yet; Stage 11 will check it. Original private inspector's existing candidate links were not overwritten by Stage 8C research candidates.
- **RIGHTS/SECURITY:** Webster digital source CC BY-SA 4.0 attribution included. Stage 10 archive contains private research data/internal flags and is **NOT safe to upload to public GitHub**. No public player integration or deployment.
- **LATEST SINGLE RECOVERY:** `SOTW_RECOVERY_CHECKPOINT_10_STAGE10_2026-11-07.zip`, **86,104,077 bytes**, SHA-256 `13e43a45d80f3099d84f21d9343557ba1256b64e2e753d313ecb2896c02a3653`. Includes complete nested Checkpoint 9 and full private Stage 10 inspector ZIP (42,195,576 bytes, SHA-256 `be139703902c317f635e39c78367f4b848edf67304afeef8a891d4fb7fd5bf5e`). Both ZIP CRC checks PASS. Original source archives remain separately owner-held.
- **NEXT:** Stage 11 local browser smoke test and targeted repair. No deployment.



### 2026-11-07 | Stage 9 COMPLETE: Webster 1828 direct lookup and Checkpoint 9
- **VERIFIED SOURCE:** Original source bundle `SOTW_WordStudy_03_DICTIONARIES_LEXICONS_KJV_WEBSTER_2026-11-05.zip` (SHA-256 `a9fbecc8f08063a227ae94da868dfb4c3ad8b98cc3140c492aba17ef77f423eb`), nested `source_files/webster1828-master.zip` (SHA-256 `be9bb797197a878a42a95d2fd63e14cfd3af25a4dc300a6aab4de99a59e48be5`), `webster1828-master/webster1828.csv` (SHA-256 `5ba9750ae13e3938441721d00677f8eacf45b63bd631639de247155892e54fb0`). Digital source LICENSE is **CC BY-SA 4.0**; preserve source attribution/share-alike conditions. Original historical book status does not erase digital transcription license.
- **IMPLEMENTED:** 62,391 two-column source-authored headword/HTML-definition rows, 62,388 normalized lookup keys; duplicate headwords retained as separate rows. 586 unfinished source rows excluded from authoritative lookup (not deleted from owner originals). Source-authored HTML preserved as CSV text, not converted into invented senses.
- **DIRECT LOOKUP:** Research-only SQLite and `lookup.py` for BSB, KJV, WEBSTER_1833 and ASV_1901, with exact casefold/whitespace/curly-apostrophe normalization. No KJV or Strong's dependency, no guessed stemming or contextual sense selection. 7/7 automated tests PASS. HTML requires sanitization before public browser display. No UI integration or deployment yet.
- **LATEST ONE-ZIP RECOVERY:** `SOTW_RECOVERY_CHECKPOINT_9_STAGE9_2026-11-07.zip`, **43,907,559 bytes**, SHA-256 **`483b98a391a042bb22bfe107f7efb9544cde90a72686bd9a042402cc55ccd661`**. Contains complete nested Checkpoint 8 plus Stage 9 SQLite, scripts, tests, source license, source README, manifest and verifier hashes. Outer ZIP CRC, embedded checkpoint hash and Stage 9 file hashes PASS. Original archives remain separate.
- **NEXT:** Stage 10 private inspector test integration for four translations, no deployment.



### 2026-11-07 | Stage 8E: targeted withheld compound-word evidence; Checkpoint 8
- **VERIFIED:** Examined all 1,052 Stage 8D withheld source-tag rows; 36 exact duplicate evidence rows, 1,016 distinct withheld cases. 924 distinct cases have a unique literal KJV phrase; 742 have unique exact phrase in KJV and Webster 1833, and 734 in KJV and ASV 1901. 46 cases have no exact KJV phrase and 46 have multiple KJV phrase locations; original 59 out-of-order cases are not automatically resolved. Counts are evidence candidates, not newly established Strong's word links.
- **CONSERVATIVE RULE:** Multiword KJV surface tagged once cannot be split into separate source-attested tags per token. Stage 8C candidate link files are unchanged. No public promotion or release.
- **LATEST ONE-ZIP RECOVERY:** `SOTW_RECOVERY_CHECKPOINT_8_STAGE8E_2026-11-07.zip`, 36,962,499 bytes, SHA-256 `672a7c6bd1ac3e6d146debe6b606208e83ae9b73bd2e48ea8e1f5fac51437428`. Includes full nested Checkpoint 7 and Stage 8E builder, 1,016-row evidence catalog, report and README. Outer CRC, hashes and nested Checkpoint 7 CRC PASS. Original source archives separate.
- **NEXT:** Stage 9 Webster 1828 dictionary direct English-word lookup across all four Bible editions. No deployment.



### 2026-11-07 | Stage 8D complete: source-to-token audit, BSB morphology index, Checkpoint 7
- **VERIFIED:** Independently reconstructed original KJV, ASV and Webster 1833 USFM verse tokens and checked every Stage 8C candidate link: **247,165 Webster 1833 + 223,941 ASV 1901 = 471,106** source/target token position, surface, exact-match and uniqueness checks; **zero structural mismatches**. This does not certify contextual semantic equivalence or public release.
- **WITHHELD:** Reproduced 1,052 withheld KJV source tags, classified 993 compound/multi-token surfaces and 59 no match after cursor; kept full withheld record list. No tags invented or force-mapped.
- **MORPHOLOGY:** Indexed source-attested BSB native parsing from 437,587 Stage 8B word rows into **67,257 distinct Strong's ID / language / parsing combinations**; 291 rows have no parsing. Index is evidence of BSB original-language morphology, not grammar automatically transferred to KJV, ASV or Webster.
- **LATEST OWNER ZIP:** `SOTW_RECOVERY_CHECKPOINT_7_STAGE8D_2026-11-07.zip`, **36,926,653 bytes**, SHA-256 **`cece2a523d4860d31be40180ad6cb03956451d95c5b8e1dc9f252f02d417979b`**. Nested full Checkpoint 6 plus Stage 8D audit/build scripts, results, withheld list, morphology index, README and SHA manifest. ZIP CRC, all member SHA hashes, nested Checkpoint 6 CRC PASS. Original source ZIPs not duplicated.
- **NEXT:** Stage 8E targeted evidence-backed compound-word recovery, then Webster 1828 dictionary direct lookup across all four editions. No public deployment or player changes.



### 2026-11-07 | Stage 8C research build: KJV bridge to Webster 1833 and ASV; Checkpoint 6
- **VERIFIED:** Parsed original archived KJV, Webster 1833 Bible and ASV 1901 USFM. Source-native KJV tagged occurrences from Stage 8A; source-native BSB Stage 8B unchanged. Compared 29,699 tagged KJV verse keys against each target. Conservative method uses only unchanged sequence-aligned English tokens with **exactly one occurrence of that surface in both verses**; no fuzzy or theological inference.
- **RESEARCH OUTPUT:** 247,165 Webster 1833 and 223,941 ASV 1901 candidate KJV-derived Strong's links, each with verse, both token surfaces/positions, native tag array, method, source/target archive hashes and derived provenance. Withheld 14,036 changed/unmatched and 51,142 repeated-word occurrences for Webster; 39,284 changed/unmatched and 49,118 repeated for ASV. 1,052 KJV tagged source occurrences could not be safely placed in reconstructed KJV verse token order and were withheld from projection.
- **VERIFIED VALIDATION:** Both compressed outputs read successfully; record counts, unique target token locations, equal normalized word surfaces, nonempty Strong's arrays, and count partitions PASS. **NOT RELEASE-CERTIFIED:** source-to-token reconstruction and USFM markup edge cases require independent audit; candidate alignment is not contextual semantic proof. No public or player change.
- **LATEST RECOVERY ZIP:** `SOTW_RECOVERY_CHECKPOINT_6_STAGE8C_2026-11-07.zip`, 36,222,342 bytes, SHA-256 `5c112d61d66693962975eaf27d4663833920ce99889b80393b1dc27ead32978f`. Contains nested complete Checkpoint 5 plus Stage 8C compressed records, deterministic builder, validator, report, README and SHA manifest. Outer ZIP CRC, all member hashes and nested Checkpoint 5 ZIP CRC PASS. Original source ZIPs not duplicated.
- **NEXT:** Stage 8D audit ambiguous source-to-token cases and source-backed morphology hooks; Webster 1828 direct lookup for all translations follows. No deployment.



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
