# SOTW Word Study | Public-safe two-passage demonstration

**Owner-approved:** 2026-11-07  
**Public Pages path:** `demo/word-study/`  
**Scope:** Genesis 1:1–3 and John 1:1–3 in BSB, KJV 1769, Noah Webster Bible 1833, and ASV 1901.

## What this demo does

- Switch between two passage groups and four English Bible edition excerpts.
- Clicking any displayed English word performs a direct exact-headword lookup in the already-public `../../webster1828.json` (Webster's 1828 *English dictionary*, **not** the 1833 Bible). Digital transcription CC BY-SA 4.0; full source wording is shown as plain text. The full published dictionary resource is not copied into this demo folder.
- Only verse 1 in BSB and KJV displays a **limited selection of source-native** Strong's associations, using BSB's source original-language table or KJV's native USFM tags. Small badges open a separate selected historical Strong's source-authored concise explanation. Those definitions do **not** choose a passage's contextual sense.
- Webster 1833 and ASV 1901 display Bible text and direct English dictionary lookup **without** automatically promoting KJV-derived candidate Strong's associations.
- ASV samples are checked at runtime against pinned source commit `4179ceb646cf4fed0077760794749821fb989273` in `SOTW-ASV-1901/asv-1901-resources`. If the external request is unavailable, the site displays the bundled, earlier cross-checked ASV sample and tells the reader the verification did not run. If the source disagrees, it reports the mismatch instead of silently using a different text.

## Source and rights boundaries

The *original sources* remain in the owner-held November 5 source archives, not in this public demonstration repository. The source-backed *research excerpt* used to construct this bounded demo was extracted from the SHA-verified `SOTW_RECOVERY_CHECKPOINT_12_BROWSER_HANDOFF_2026-11-07.zip` archive (SHA-256 `d5c7547659bcdc4bca4024e85405b7d4817808e6d2cf2b59570c9392a2f68105`) and its nested Stage 10 private Inspector. **No full private corpus, disputed flags, unpublished word-link candidates, internal audit records or private ZIPs were uploaded.**

Selected original text:

| Resource | Provenance / rights |
|---|---|
| BSB | Archive `SOTW_WordStudy_04_BSB_TEXT_ALIGNMENT_REFERENCES_2026-11-05.zip`; source USFM `bsb_usfm.zip` and native table `bsb_tables.tsv`; BSB publisher dedicated text to public domain on 2023-04-30: https://berean.bible/terms.htm |
| KJV | Archive `SOTW_WordStudy_03_DICTIONARIES_LEXICONS_KJV_WEBSTER_2026-11-05.zip`; original tagged `eng-kjv2006_usfm.zip`. Historical US-public-domain Bible text. |
| Webster 1833 Bible | Same archive; `engwebster_usfm.zip`. Historical Bible edition distinct from Webster 1828 dictionary. |
| ASV 1901 | Independent SOTW ASV public chapter records at `data/asv1901/{genesis,john}/chapters/01.json`, with exact source commit pin above. |
| Historical Hebrew Strong's | James Strong selected digital `strongs-master.zip/strongs-master/hebrew/StrongHebrewG.xml`, XML SHA-256 `1f9659ea208f4c498843a0280dacb1448627c33ca77712642d8705793ab66061`, original publisher's Public Domain declaration accepted in SOTW source decisions. |
| Historical Greek Strong's | James Strong selected v1.9 digital `strongs-dictionary-xml-master/strongsgreek.xml`, XML SHA-256 `91474213b208a4e487d35f85c10e5c90737acc69082dad15dec5431406003545`, CC0. |
| Webster 1828 dictionary | Existing public `webster1828.json` and `LICENSE_WEBSTER_SOURCE.txt`, transcription CC BY-SA 4.0. |

`sample-data.json` carries each Bible source member hash and explicit Strong's digital source locks. The BSB and KJV badges include **only selected first-verse native records**. These are not semantic equivalence claims between editions. The KJV's unusual source tag on “and” (Genesis 1:1) was intentionally not promoted as a contextual word meaning.

## Validation / release boundaries

- **Performed (2026-11-07):** JavaScript syntax PASS; 24 edition-verse records across 2 passages and 4 editions; 36 selected native Strong's badges resolve to 13 separate historical lexical headwords; all tag positions within the verse text; source SHA and sample integrity inspection; no known private audit marker fields in the public JSON.
- **Previously confirmed:** Owner-verified public Webster 1828 standalone dictionary site, all edition selectors and headword behavior.
- **Pending:** Live browser click-through of this **new** Word Study demo (desktop/mobile) and a successful cross-repository ASV fetch in the public browser. Those are NOT counted as already passed. The separate private 66-book Inspector's full Stage 11 browser gate also remains open.

This is an independent, limited **website demo**, not a full Bible hosting pipeline, production-grade lexical database or CGBC Sermon Player integration. Current SOTW durable decisions, original source/rights files, and independent Bible repositories remain authoritative.
