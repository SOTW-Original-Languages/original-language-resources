# SOTW Original Languages — Durable Decisions & Continuity Register

**Established:** 2026-11-06  
**Status:** Owner-directed architecture and research-continuity record. This document records owner decisions, including acceptance of the archived Greek CC0 and Hebrew Public Domain declarations as the working rights basis for the selected Strong's publication sources. It is not an independent legal guarantee or a blanket approval of unrelated third-party editions.  
**Scope:** SOTW Original Languages and Word Study Inspector. No CGBC player or other-repository changes.

## Permanent vetted-source index

Read **[SOTW Vetted Sources, Rights Decisions & Artifact Index](SOTW_VETTED_SOURCE_AND_ARTIFACT_INDEX.md)** before questioning any previously acquired source. It lists the four original source bundles, source members, whole-archive SHA-256 values, derived research artifacts, accepted publication roles, STEP's comparison-only role, and private/public boundaries. The archived sources were previously vetted as research inputs; do not demand a new general vetting campaign. **The index is a reference to original archives, not a claim that all source bytes reside in public GitHub.**

## Mandatory new-thread resume procedure

1. Read this register, `docs/SOTW_VETTED_SOURCE_AND_ARTIFACT_INDEX.md`, `docs/ARCHITECTURE.md`, `docs/SOURCES_AND_RELEASE.md`, `docs/TRANSLATION_ADAPTERS.md`, and the current inspector README.
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

## Owner-settled publication and source-retirement rules (2026-11-06)

- **Unresolved evidence is not displayed as a resolved relationship.** If an original-language alignment, lexical association, or interpretive claim requires unresolved evidence-based review, omit that *claim* from the public projection. Preserve the actual source text and undisputed records; do not suppress an entire verse or resource merely because one association is disputed. Do not silently choose a disputed answer. The theologian uses independent research tools and, where available, paid services to investigate; SOTW does not claim to adjudicate those disputes for the reader.
- **Optimized library is the intended durable operating source.** Build deterministic, versioned, validated canonical records from vetted inputs, with full source-authored fields, multiple tags, edition boundaries, licenses, provenance, and traceable transformation rules. Original archives are transitional ingestion inputs, not a required public runtime dependency.
- **Retire original archive copies only after a documented migration gate:** verify complete required field/record coverage; original-source wording and distinctions; hash and source provenance; rights metadata; deterministic rebuild of public projections from optimized canonical records; cross-record integrity; private/public separation; and a recoverable backup of the optimized canonical library and scripts. Document any non-migrated material explicitly. Do not delete originals as part of this decision-register edit. If original bytes are the only way to re-run the *original ingestion* or substantiate a provenance dispute, acknowledge that capability will be lost on deletion; keep an owner-approved archival fallback until that risk is accepted.
- **No unsupported public output:** uncertain links remain internal research evidence, not reader-facing inferred facts. The absence of an association is not a claim that no association exists.

## Owner refinement: original source preservation in the shared foundation (2026-11-06)

- **Prefer retaining vetted original archives** in the existing Stewards of the Way Bible Foundation's source-preservation layer where capacity, access controls, rights, and repository constraints permit. Do not delete them merely because optimized canonical records have been built.
- The SOTW Original Languages repository remains the independently optimized processing and publication library; it should reference foundation originals by stable manifests, exact paths/versions and hashes, not require loading them at runtime.
- Do not assume the foundation currently hosts every archive, or upload private/restricted bytes to public GitHub without an approved storage and rights plan. Large archives may need a suitable artifact store rather than ordinary Git history.
- This preservation preference supersedes any implication that original-source deletion is the intended default. The earlier retirement gate remains a safety minimum **only if the owner later explicitly requests deletion**.

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

## CURRENT WORK HANDOFF — Genesis schema design (2026-11-06)

**Step 1 schema files committed:**
- `schemas/sotw-canonical-v1.schema.json`: JSON Schema Draft 2020-12 with `source`, `occurrence`, `lexicon`, `link` record types and explicit source provenance/release fields.
- `examples/sotw-canonical-v1.synthetic.json`: synthetic-only Genesis 1:1 shaped records including a disputed research-only link. **Not real biblical text or an approved data projection.**
- `docs/SOTW_CANONICAL_SCHEMA_V1.md`: contract explanations and required public exclusion rules.

**Work completed:** schema, fixture and regression validator script committed; 18/18 direct structural checks passed against fetched GitHub records. The validator at `scripts/validate_canonical_v1.py` uses `jsonschema` Draft 2020-12 and includes 7 invalid-record tests plus disputed-link public-exclusion checks. **Not yet completed:** execution of that Python validator in a checked-out GitHub workspace (its presence alone is not a passing run), compatibility audit against all existing schemas/foundation catalogs, real Genesis 1:1 ingestion, ingestion/build scripts, or data upload. Do not call the entire Genesis pipeline complete.

**Next action:** GitHub Actions workflow `.github/workflows/validate-sotw-canonical-v1.yml` has now been committed (commit `33edf4e53a2a02fc9d3fc9d0ee9c08af38f91be7`) to execute the Draft 2020-12 validator on push and manual dispatch. **Certification is PENDING until an actual successful workflow/job log is verified.** The available commit-workflow lookup returned no PR-triggered runs, which is not evidence of a pass or fail. Obtain the run via GitHub Actions UI or a suitable workflow-run listing, then log its conclusion. Also compare pinned foundation IDs and existing schema paths. Compare pinned foundation IDs and existing schema paths, and correct any conflicts. Then ingest the previously vetted real Genesis 1:1 slice with source-hash verification. Follow with Genesis 1 and full Genesis. Do not re-vet source selection or reopen STEP as a required publication source.

**Publication invariant:** candidate/disputed/rejected links must not appear as verified public associations, even if the underlying record passes JSON Schema. Original archives should be preserved in the Bible Foundation where feasible; no source files moved or deleted.

## SCHEMA CI RESULT — owner-provided GitHub Actions evidence (2026-11-06)

**PASS: Automated canonical-v1 schema test job.** Owner supplied a GitHub Actions screenshot showing green completed steps for checkout, Python setup, dependency installation, `python scripts/validate_canonical_v1.py`, post-run steps, and job completion. This is user-provided visible evidence of a successful job, not an independently retrieved full run log or run ID. The earlier push-trigger commit was `17421062cc5e0c0f473b094e5df882eab28714b1`; screenshot does not establish its exact run SHA.

**Certification scope:** JSON Schema Draft 2020-12 syntax and the synthetic fixtures, invalid-record tests, and publication-exclusion policy covered by the committed validator passed in CI. **Not certified:** interoperability with pinned Bible Foundation schemas/IDs, real Genesis source hashes and coverage, provenance/right-to-publish evidence on real records, or ingestion pipeline correctness. Those remain required before real source publication.

**Next work:** Verify Foundation compatibility, then ingest and validate source-backed Genesis 1:1 records with preserved original-source hashes and exact evidence; expand to Genesis 1 and full Genesis only after that gate. No need to rerun source-selection or STEP discussions.

## FOUNDATION COMPATIBILITY BUILD CHECKPOINT (2026-11-06)

**Built and committed, awaiting CI result:** `compatibility/foundation-v0.1.snapshot.json` (live fetched Foundation v0.1 reference schema/fixture and source blob SHAs), `scripts/validate_foundation_compatibility.py`, `docs/SOTW_FOUNDATION_COMPATIBILITY_V1.md`, and `.github/workflows/verify-foundation-compatibility.yml`. Corrected `schemas/sotw-canonical-v1.schema.json` verse-ID pattern to Foundation's 3–8 character book codes and positive chapter/verse numbering.

**Next action:** Open GitHub Actions workflow `verify-foundation-compatibility.yml`; confirm both canonical and Foundation validators pass, capture run evidence, and update this checkpoint. Do **not** call it certified before that evidence. Then verify actual pinned full book-code catalog if available and begin real Genesis 1:1 source-byte/hash validation. Foundation presently advertises an architecture seed/reference-only v0.1 contract; do not mistake that for a complete book or lexical catalog.

## FOUNDATION COMPATIBILITY CI PASS — owner screenshot (2026-11-06)

**PASS (defined automated scope):** Owner provided a GitHub Actions screenshot titled `Verify SOTW Bible Foundation co...`, showing `Successful in 8s`, green completion checks for checkout, Python setup, dependency installation, `python scripts/validate_canonical_v1.py`, `python scripts/validate_foundation_compatibility.py`, and job completion. This establishes a successful run of the configured tests against the pinned Foundation v0.1 snapshot. Screenshot does not supply run URL, run ID, exact SHA, or full logs; do not claim those were independently retrieved.

**Step 1 status:** COMPLETE for canonical v1 synthetic-schema and pinned Foundation v0.1 compatibility checks. **Not certified:** full 66-book code catalog, actual Hebrew/Greek source bytes, translation foreign keys, real Genesis word associations, provenance and public release rights. Those are Phase 2 / real Genesis ingestion gates.

**Resume next:** inspect the vetted original-source package index, retrieve actual Genesis 1:1 source material and verify byte hashes, map into canonical occurrence/lexicon/link records without promoting disputed associations, validate and audit output before expanding to Genesis 1 and Genesis. Do not restart source selection, rights debates or STEP primacy discussions.

## Change log

- **2026-11-06 (Foundation CI pass):** Owner screenshot confirms successful 8-second GitHub Actions job running both canonical and Foundation compatibility validators. Step 1 complete within pinned/synthetic contract scope; real-source checks remain.
- **2026-11-06 (Foundation compatibility):** Pinned live Foundation reference contract, added compatibility verifier and CI workflow, corrected verse-ID regex. CI outcome not yet observed.
- **2026-11-06 (CI evidence):** Owner supplied screenshot of successful GitHub Actions schema-validation job, including validator step. Synthetic/schema CI PASS; Foundation compatibility and real-source validation still pending.
- **2026-11-06 (certification attempt):** Added GitHub Actions schema-validation workflow; no successful execution evidence retrieved yet. Status remains pending, not certified. Container network could not access GitHub raw files; do not substitute reconstructed data for actual repository bytes.
- **2026-11-06 (validation preparation):** 18/18 fetched-schema structural checks passed; committed standards-based Draft 2020-12 validator with negative and public-exclusion tests. Python validator not yet executed in a checked-out repository; do not claim full validation passed.
- **2026-11-06 (Step 1 implementation):** Committed canonical v1 schema, synthetic fixture and schema contract documentation. Automated validation and real Genesis ingestion remain next tasks.
- **2026-11-06 (work handoff):** Owner requested a scan-friendly checkpoint for the start of Step 1 (Genesis canonical schema). Architecture, adapters and release rules inspected. Schema, fixtures and scripts **not yet committed**. Resume at schema implementation, not source re-vetting.
- **2026-11-06 (owner refinement):** Prefer preserving original vetted archives in the existing Bible Foundation where feasible; optimized SOTW library remains independent. No source files moved or deleted.
- **2026-11-06 (owner pipeline policy):** Settled non-display of unresolved evidence-based claims and conditional retirement of original source archives after a complete, verified optimized-canonical migration. No data deletion or deployment performed.
- **2026-11-06 (source continuity):** Added permanent vetted-source/artifact index with four original source-package SHA-256 hashes, derived research artifacts, stable repository roles, and explicit STEP comparison-only / Strong's primary-publication decisions. Index is metadata only, not an upload of private archives.
- **2026-11-06 (owner follow-up):** Accepted archived Greek Strong's CC0 and Hebrew `StrongHebrewG.xml` Public Domain source declarations as the working publication basis; James Strong is the reader-facing historical attribution. No repeated historical-editorial-rights audit absent contradictory evidence. Retain internal provider provenance and update release manifests during implementation. Decision-record update only; no inspector or source-data deployment.
- **2026-11-06:** Initial register created following owner report of repeated loss of decisions across threads. Read-only reconciliation of existing GitHub architecture, source/release policy, inspector README, archived source filenames, and continuation handoff. No change to production data, inspector, schemas, or other repositories.

## Continuity rule

**Evidence first; reopen only a documented contradiction.** Owner decisions govern the intended design, while release rights and source provenance remain independently verifiable requirements. Preserve both without substituting one for the other.
