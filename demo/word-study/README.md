# SOTW Word Study | Public-safe two-passage demonstration

**Owner-approved:** 2026-11-07  
**Current demo revision:** v1.2, visibly separated concise and expanded Strong’s fields, all-13-entry sample inventory, source metadata and attribution/rights ledger. The v1.1 KJV-derived associations remain unchanged.  
**Public Pages path:** `demo/word-study/`  
**Scope:** Genesis 1:1–3 and John 1:1–3 in BSB, KJV 1769, Noah Webster Bible 1833, and ASV 1901.

## What this demo does

- Switch between two passage groups and four English Bible edition excerpts.
- Clicking any displayed English word performs a direct exact-headword lookup in the already-public `../../webster1828.json` (Webster's 1828 *English dictionary*, **not** the 1833 Bible). Digital transcription CC BY-SA 4.0; full source wording is shown as plain text. The full published dictionary resource is not copied into this demo folder.
- BSB and KJV verse 1 display **selected source-native** Strong's associations. ASV 1901 and Webster Bible 1833 verse 1 also display a **separate, limited set of 15 supported KJV-derived research associations** in visually distinct outlined badges. These are exact unique English-token matches to source-native KJV tags, not the other editions' own original-language tags, nor semantic proof or automatic alignment of the whole Bible.
- Strong's panels now display the **complete selected source fields available for these 13 entries**: source-authored concise explanation; derivation, KJV rendering, and five Hebrew entries' expanded numbered senses. The selected Greek Strong's v1.9 XML does not have a parallel separately numbered long-sense list; supplemental source prose is shown when present. No BDB, STEP or Thayer alternative definition was imported.
- Webster 1833 and ASV 1901 have direct English Webster 1828 lookup, plus only the small independently token-checked Stage 8C/8D association subset. They are labeled **KJV-derived research links**, not native Strong's tags. Ambiguous repeated-word matches and the KJV H853 function-word association on English `and` are omitted; do not infer a John 1:1 `Word` badge from the repeated English surface.
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

`sample-data.json` carries each Bible source member hash and explicit Strong's digital source locks. It contains 36 selected BSB/KJV native badges and 15 distinctly labeled KJV-derived ASV/Webster preview badges. The derived badge provenance is Stage 8C JSONL research `exact_unique_token_in_unchanged_sequence`, followed by Stage 8D structural audit and a fresh check of all 15 display-token positions and exact surfaces. KJV source archive SHA-256 `ce1f526c64c2376f407308c2c23cb2d2fb58efaf5296327d2d8e408c3700650d`; derived target archive SHA-256s `5e385a1a89887849cb07c88ddf4df37708e0fa901b1f1b7f0b8204c153f0a901` (ASV) and `0f3c1122422adba66cf1e0c98e11db117beebbe40994d2d8afb5e80cc84942cf` (Webster). These are supported research associations, not cross-edition semantic equivalence or release approval for entire datasets. The KJV's H853 tag on English `and` was intentionally not promoted as a contextual meaning.

## Validation / release boundaries

- **Performed (2026-11-07, v1.1):** JavaScript syntax PASS; 24 edition-verse records across 2 passages and 4 editions; 36 selected native BSB/KJV Strong's badges and 15 selected independently surface-checked KJV-derived ASV/Webster badges resolve to 13 historical headwords. All 13 include source derivation and KJV rendering, 5 Hebrew entries have source numbered-sense lists, and 8 Greek entries truthfully omit separately numbered extended senses. All badge positions and source references validate. No known private audit marker fields in public JSON. Simulated DOM tests PASS for ASV 3/3 source check, Hebrew expanded fields, a derived badge, Greek field boundaries, and Webster lookup.
- **Previously confirmed:** Owner-verified public Webster 1828 standalone dictionary site, all edition selectors and headword behavior.
- **Owner browser verification of v1 initial release:** Screenshots confirm Genesis KJV Hebrew badge, John BSB Webster 1828 English lookup, John ASV 1901 full verse rendering and pinned source status `3/3 displayed verses match exactly`. These are owner-observed web successes, not a private 66-book Inspector Stage 11 certification.
- **Owner review of v1.1:** Owner reported the newer demo looked good, but the short Strong’s definition was not obvious/visible for comparison. No claim is made that all lexicon source fields or the full 66-book Inspector have been visually accepted.
- **v1.2 validation:** JavaScript syntax PASS, 13/13 sample lexical entries have concise and selected fuller source fields, 5/5 sample Hebrew entries have numbered senses and metadata, 8/8 sample Greek entries expose source Beta Code/pronunciation and explicitly lack a numbered long-sense list; dynamic 13-entry inventory and two distinct Strong’s source cards render in simulated DOM. Simulated UI PASS for both definition layers, Hebrew and Greek metadata, derivation/KJV rendering, native and derived badge labeling, ASV 3/3 check, Webster 1828 lookup and entry-inventory selection. The cached script/data URLs are versioned `v=1.2`.
- **Still pending:** Real desktop/mobile browser acceptance of the new v1.2 inventory and attribution display. The full 66-book private Inspector Stage 11 gate remains separate and not certified.

This is an independent, limited **website demo**, not a full Bible hosting pipeline, production-grade lexical database or CGBC Sermon Player integration. Current SOTW durable decisions, original source/rights files, and independent Bible repositories remain authoritative.

## v1.2 | Full visibility of THIS demo sample and attribution review

The public demo now displays **two distinct, always-visible sections** for each selected Strong's entry: **(1) Strong's concise definition** followed by **(2) Strong's expanded/full source material**. They are distinct, source-authored fields, not editorial summaries or alternatives silently replacing each other. For the five Hebrew preview entries, the second section contains the source's numbered senses. The accepted Greek XML v1.9 source supplies a concise definition, derivation, KJV renderings and optional supplemental prose, **but no separately numbered long-sense list**. The UI states this rather than inventing a missing long definition.

An on-page **“What is actually in this demo?”** section enumerates all **13 selected preview records**, their field presence, source spelling/phonetic/morphological metadata (as encoded), original-language text, historical-source cross-references as unverified metadata, source XML SHA-256 values and, for Hebrew, research entry SHA-256. Clicking an inventory item opens every exposed source field independently of an English verse word. `sample-data.json?v=1.2` is linked for exact byte-level review of the public projection.

**Attribution / rights labels visible in the site:** Historical author James Strong (both Hebrew and Greek); Hebrew OSIS original source-declared Public Domain; Greek v1.9 XML editor Ulrik Sandborg-Petersen and source-declared CC0; Noah Webster historical 1828 author and digital transcription `akaitsurugi/webster1828` CC BY-SA 4.0 with a link to the site's source license and required attribution/share-alike reminder; BSB publisher's public-domain dedication and link; KJV, Webster Bible 1833 and ASV 1901 edition/source provenance, with the independent SOTW ASV repository pin preserved. STEP, BDB, Thayer and TWOT *definition texts* are explicitly **not** part of this demo. A source-native TWOT reference candidate is just a reference code and does not reproduce TWOT. License statements are based on the accepted SOTW source register; additional digital editions must still pass their own release gates.

**Scope warning:** the 13 visible entries are all of THIS website's lexical samples, **not** all 8,674 Hebrew and 5,624 Greek records held in pre-beta research. Private audit flags, full private corpus and any unresolved link candidates remain excluded from public release. The page is a pre-script-production review aid, not proof of full-corpus readiness or a replacement for eventual script, rights and migration testing.
