# SOTW Vetted Sources, Rights Decisions & Artifact Index
**Canonical companion to:** [Durable Decisions & Continuity Register](SOTW_DURABLE_DECISIONS_AND_CONTINUITY.md)  
**Indexed:** 2026-11-06. **Scope:** durable sources and governance, not a work-progress checkpoint.  
**Rule:** All listed acquisitions and the prior vetting effort are **accepted research inputs**. Do not restart source discovery or ask the owner to justify why these were acquired. The separately documented release treatment for each source controls what may be published. A vetted research input is not necessarily a redistributable public corpus.

## Mandatory retrieval order
1. Read [Durable Decisions & Continuity Register](SOTW_DURABLE_DECISIONS_AND_CONTINUITY.md), this index, [Architecture](ARCHITECTURE.md), [Sources & Release](SOURCES_AND_RELEASE.md), [Translation Adapters](TRANSLATION_ADAPTERS.md).
2. Use the four original November 5 source ZIPs and their identical embedded `SHA256_ALL_SOURCE_FILES.json` inventory to recover source bytes. Check hashes, do not recreate archives from third-party websites when the originals exist.
3. Consult the November 6 continuation handoff, locked research slice, private 66-book build and current inspector README for implementation evidence; distinguish old source-priority suggestions from later owner-settled publication decisions.
4. Only if a specific needed file is unavailable, report its **exact name**. Do not reopen the entire research or rights debate.

## Binding owner decisions
- **STEP is comparison, not publication authority.** No STEP Bible dependency is required to publish Strong's definitions, Hebrew/Greek words, or our independent Strong's connections. Do not display STEP TBESH/TBESG glosses in the primary published dictionary. Do not repeat the debate about whether STEP must be credited for independent Strong's connections. If an optional research panel actually reproduces STEP content, retain its component-specific license/attribution. STEP original-language/morphology data, if actually incorporated in any public corpus, still requires its own component-level rights handling; merely relabeling it SOTW does not make it independent.
- **Strong's source selection is settled.** Greek: archived `strongs-dictionary-xml-master.zip`, source-declared CC0. Hebrew: archived `strongs-master.zip` / `StrongHebrewG.xml`, source-declared Public Domain. Owner accepts these publisher declarations as the working publication basis. Reader-facing historical attribution: **James Strong**. Preserve digital provider and byte provenance in the audit manifest; do not reopen historical editorial-rights archaeology without specific contradictory evidence.
- **Definitions:** source-authored complete text; source-authored short fields only when actually present; original KJV translation/usage separate. No AI-authored Quick Meaning passed off as Strong's. Preserve multiple native Strong's tags and all lexicon senses without conflating the two.
- **Edition boundaries:** BSB native original-language associations; KJV native tagged USFM; NWB/Webster Bible 1833 and ASV 1901 only supported KJV-derived associations. Multiple supported tags retained. No fabricated contextual meanings or cross-tradition word surfaces.
- **Other vetted sources are not discarded.** Keep original BSB, ASV, KJV, Webster, STEP, lexicon, and morphology source packages and audit evidence. Historical commentaries are a separate organization and were not part of these four source packages. BibleAquifer BDB digital edition remains excluded from initial public release. Thayer candidate remains flagged for review rather than silently elevated to publication authority.
- **Source-specific release gates remain:** owner acceptance of an archive as research evidence does not override an actual license notice on a different source or automatically authorize public release of all source archives. Preserve original source rights and internal/private flags.

## Original source package inventory (exact archive identity)

These are **Project/conversation archives**, not files presently stored in this public GitHub repository. The SHA-256 values below identify the whole original ZIP. Each of the four source ZIPs contains `START_HERE_SOTW_NEXT_THREAD.md`, `SHA256_ALL_SOURCE_FILES.json` and nested source archives. The embedded hash inventory enumerates and hashes the nested source files.

| Source package | SHA-256 (whole ZIP) | Contents and intended role |
|---|---|---|
| `SOTW_WordStudy_01_ASV_AND_CONTINUITY_2026-11-05.zip` | `17c8f23c45c9bca632ebf7b61d7a2e0fa66b98f06877eb8f07cdcaaead8e4d2b` | ASV historical text and tagged/compared sources: `American-Standard-Version-Bible-master.zip`, `ASV.zip`, `eng-asv_usfm.zip`, `asv.sqlite`, `asvs.sqlite`; previous translation handoff, architecture plan, ASV Strong's comparison report, exact conflicts CSV and comparison JSON |
| `SOTW_WordStudy_02_STEP_ORIGINAL_LANGUAGES_2026-11-05.zip` | `d46671e0f3e75eb2a7a683726f1025f9e68f0e7678332ee1054ae26762600f8f` | `STEPBible-Data-master.zip`; original-language, morphology and extended-Strong's comparison/verification resources; **not primary published dictionary** |
| `SOTW_WordStudy_03_DICTIONARIES_LEXICONS_KJV_WEBSTER_2026-11-05.zip` | `a9fbecc8f08063a227ae94da868dfb4c3ad8b98cc3140c492aba17ef77f423eb` | `strongs-master.zip` (selected Hebrew), `strongs-dictionary-xml-master.zip` (selected Greek), `HebrewLexicon-master.zip` (comparison), `thayers-greek-lexicon-dataset-master.zip` (review candidate), `webster1828-master.zip` (English dictionary), `eng-kjv2006_usfm.zip` (KJV tagged), `engwebster_usfm.zip` (Webster Bible 1833) |
| `SOTW_WordStudy_04_BSB_TEXT_ALIGNMENT_REFERENCES_2026-11-05.zip` | `755fc0d5fc294f6c27b32b2ec07ccf7da355969561fba7b71f95a1dd5de598eb` | `bsb_usfm.zip`, `bsb_usj.zip`, `bsb_usx.zip`, `bsb_tables.tsv`, `bsb_concordance.xlsx`, `bsb_topical_index.xlsx`, `blb.xlsx`, `brb.xlsx`; BSB native text/alignment and references |

**Original sources are authoritative evidence; later preview JSON is not a substitute.** The November 5 START_HERE files contain older candidate source-priority language, including STEP prominence. Where inconsistent, the November 6 owner decisions above supersede that older display/source-priority recommendation, **without erasing the acquired STEP archive or its legitimate research use**.

## Derived research and viewer artifact index (not public source archives)

| Exact artifact | SHA-256 | Nature / safe-use boundary |
|---|---|---|
| `SOTW_Original_Languages_Build_Continuation_Handoff_2026-11-06.pdf` | See Project original | Source decisions, repository separation, architecture, release safeguards and source package descriptions; historical snapshot, not override of later decisions |
| `SOTW_GEN1_JHN1_SOURCE_LOCKED_RESEARCH_SLICE_2026-11-06.zip` | `b10411475a319669ea68e7676f4e98e671ed9325099ce49e7b667ad3aff43c2a` | 17 entries: audit/source locks, SHA manifest, release verdict, schemas, source manifests, research records, build and validation scripts for Genesis 1:1 and John 1:1 |
| `SOTW_WORD_STUDY_PRIVATE_INSPECTOR_ALL_66_BOOKS_2026-11-06.zip` | `521f6905abb5877cde467e10f7fe2ff6a7b463cd62280ba2ab71a6249a70263b` | 675 ZIP entries: research JSON by book/edition, verse-text shards, private `internal_flags`, catalog, build diagnostics, scripts, inspector assets. **PRIVATE**. Never upload wholesale to public GitHub or expose flags/disputes. |
| `SOTW_WORD_STUDY_PUBLIC_VIEWER_SHELL_ONLY_2026-11-06.zip` | `dbd9c0b2da428af4fef8213ec2572c14be2c2861e89d0465e880359cd495f907` | Four-file viewer shell and deployment README; no approval for bulk private data release |
| `SOTW_WORD_STUDY_BROWSER_PREVIEW_2026-11-06.html` | See Project original | Offline prototype; not canonical lexical source |
| `docs/inspector/README.md` | Live GitHub | Current **v2.3**, three-passages-only public preview; source display contains historical editorial Quick Meaning and optional STEP glosses from earlier demonstration. **Current UI is not the settled target publication design.** |

The private 66-book research build and the four large original source ZIPs are **not mirrored into the public repository by this index**. This document makes their names, roles, and hashes discoverable. Do not assert that a GitHub-only checkout contains their bytes. A future thread needs access to the Project originals or an owner-approved private archival location. Do not put restricted/private source bytes in a public GitHub commit.

## Stable external repository responsibilities

- [SOTW Original Languages](https://github.com/SOTW-Original-Languages/original-language-resources): lexical library contracts, source decision register, inspector and safe projections.
- [Stewards Bible Foundation](https://github.com/Stewards-of-the-Way/bible-foundation): shared IDs, interoperability and source/rights contracts.
- [SOTW ASV 1901](https://github.com/SOTW-ASV-1901/asv-1901-resources): ASV corpus and its own edition assets.
- [SOTW Historical Commentaries](https://github.com/SOTW-Historical-Commentaries/historical-commentary-resources): separate commentary resources; not the lexicon source.
- KJV, BSB and Webster 1833 remain distinct translation-source domains, even where their local originals are included in the archived ZIPs. Do not assume unverified repository names.

## New-thread decision priority
**Current owner decision register > this source index > source-specific embedded license declarations and pinned original evidence > earlier handoffs' implementation suggestions > old public inspector UI.** This ordering is for **project intent and workflow**; it does not waive external legal obligations or authorize inventing data. New threads must not re-litigate vetted acquisitions or STEP publication rationale without concrete new contrary evidence.

## Index maintenance
On new source acquisition or replacement, add exact archive/file identity, hash, provenance, role and release treatment here, without discarding old audit history. Processed outputs can be re-scanned from source archives; this document intentionally focuses on durable sources and decisions, not a weekly work-state ledger.

## 2026-11-07 | New bounded public Word Study demo (distinct from archived Inspector)

- **Current public demo files:** `demo/word-study/index.html`, `demo/word-study/app.js`, `demo/word-study/sample-data.json`, and `demo/word-study/README.md` in `SOTW-Original-Languages/original-language-resources`. GitHub Pages expected path: `/original-language-resources/demo/word-study/`.
- **Source basis:** Previously owner-vetted November 5 Bible source archives through verified Checkpoint 12 private Inspector source locks; two sample passages, three verses each, four English Bible editions. ASV also cross-referenced against the independent public SOTW ASV chapter files pinned at commit `4179ceb646cf4fed0077760794749821fb989273`. Source-byte hashes are recorded in the demo's public JSON/README.
- **Scope and safety:** 36 *selected native* BSB/KJV Strong's links to 13 selected James Strong historical entries, not unpublished semantic/cross-edition candidates. Webster 1828 exact headword lookup uses the existing root public dictionary, not a new dictionary release. No private 66-book JSON, internal flags, STEP glosses or unresolved research associations were uploaded. This limited demo does not replace or certify the historical `docs/inspector/` v2.3 preview, the private Stage 10 Inspector, or a future complete translation publication.
- **QA status:** Source and simulated UI checks PASS; new demo's live browser/mobile owner acceptance PENDING. The separate standalone Webster homepage was already owner browser-tested.

