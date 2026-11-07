# Word Study Inspector — public test v2 (2026-11-06)

Public URL: https://sotw-original-languages.github.io/original-language-resources/inspector/

## Scope
This is a **three-passage, source-backed preview** for Genesis 1:1, John 1:1, and Romans 10:9. It is **not** the 66-book online corpus. The full research corpus remains separate. Public files: `index.html`, `data-preview.js`, this README.

- Translation order: BSB, KJV, NWB (Webster Bible 1833), ASV 1901.
- BSB: original-language source table with surface forms, transliterations, morphology, original-word order and English renderings.
- KJV: source-native Strong's tags.
- NWB and ASV: supported KJV-derived display candidates only. **No internal disagreement records or unresolved links are included.**
- Strong's: 30 historical Hebrew/Greek headwords with **concise, source-derived quick definitions** alongside longer source-credited historical definitions or clearly marked usage excerpts. Quick definitions are editorial summaries, not quoted source fields or passage-specific meanings.
- Webster 1828: 19 selected historical English headword/sense excerpts. The 1828 dictionary is **not** the Webster 1833 Bible.
- STEP Bible TBESH (Hebrew) and TBESG (Greek): **23 uniquely mapped source `Gloss` records only**, source-file hashes and CC BY 4.0 attribution included. The TBESH `Meaning` column is explicitly excluded: its header asks projects to obtain permission from Online Bible before reuse. Multiple extended Strong's subentries are not silently merged.
- No BDB, Thayer candidate corpus, private flags, analytics or CGBC Sermon Player integration.

## Source archives and attribution
- **BSB native tables:** `bsb_tables.tsv`, SHA-256 `aa2a9a0f004d015738cd1839c7c56c3be2549e0d4f4537090c2017268c223c60`. The excerpt contains only selected verses and rows.
- **Hebrew Strong's:** [Open Scriptures HebrewLexicon](https://github.com/openscriptures/HebrewLexicon), `HebrewStrong.xml`, digital edition CC BY 4.0, with attribution to the Open Scriptures Hebrew Bible Project. Original archive SHA-256 `907bcdcd507b40b962364b45426ace48a4aa44f3cff505ccc64e2f6b9d538375`.
- **Greek Strong's:** [morphgnt / Ulrik Sandborg-Petersen Strong's Greek XML](https://github.com/morphgnt/strongs-dictionary-xml), CC0. Archive SHA-256 `e71ac0e53c72ae7b8ad71ab93ae441a3afe63a280058643e4df85c65b5f240bc`.
- **STEP Bible TBESH/TBESG:** [STEPBible-Data Lexicons](https://github.com/STEPBible/STEPBible-Data/tree/master/Lexicons), created by STEP Bible based on work at Tyndale House Cambridge, CC BY 4.0 for the published STEP `Gloss` column. TBESH source file SHA-256 `464dccadd95fd8620dd05fa0d7a4caba58ec3c4d5db3ebf38e43d046ca25b591`; TBESG source file SHA-256 `312f723d7b8ef263bbdfb0451c9b8057125804dfff390b6f8544cff2a84b57f4`; nested STEP archive SHA-256 `512fb89c2e817f4043eb0dad7f8e6466cc5e63edb39361a277180028dae0c6ae`. The TBESH `Meaning` column is based on Online Bible's abridged BDB and is **not** included because its file requires separate permission. Example citation: STEP Bible / Tyndale House Cambridge, *TBESH*, `H8064`, `Gloss` = “heaven”, CC BY 4.0, source file SHA-256 `464dcc...`.
- **Webster 1828:** [akaitsurugi/webster1828](https://github.com/akaitsurugi/webster1828), digital transcription CC BY-SA 4.0. Archive SHA-256 `be9bb797197a878a42a95d2fd63e14cfd3af25a4dc300a6aab4de99a59e48be5`. Excerpts are selected from the transcription and shortened or punctuated for compact display; the source transcription's license and attribution apply to adapted excerpts.

## Quality gates performed
- Three Scripture passages with four English edition texts each.
- 47 BSB original-language rows retained in native original-word order.
- 30 unique Strong's identifiers resolved to Hebrew or Greek lexical records, each with a nonempty short gloss.
- 23 uniquely mapped STEP Bible short glosses, each with exact extended Strong's ID, source field, license and source-file hash; 7 Strong's IDs with multiple STEP extended subentries intentionally receive no STEP gloss in this preview.
- 19 Webster 1828 headword excerpts available for English lookup.
- Every published KJV/NWB/ASV link position matches the intended English token in the corresponding verse.
- All published Strong's IDs resolve to an excerpted lexicon record.
- Public `data-preview.js` contains no internal flags, conflict counts, or private audit records.
- Inline JavaScript syntax checked against the published file.

These are structural and provenance checks, **not** scholarly adjudication or full textual verification.

## Change control
- v1 fallback: Git commit `c011080f2ecf4d89c4b386f135d5deab9a153193`.
- v2 preview data commit: `b6cd5cc8bf31ea8eec78d10721eeb6e52c5f7cd8`.
- v2 viewer commit: `b4518f00ad7d5d887c95056efb3ec0bc51341058`.
- v2.1 quick definitions: data `85eef3d7271eacb0f9f98e2f5c22c53af42481f9`; UI `b87d4fbc41dcc9219c4252793a02bc82659e901f`.
- v2.2 STEP source glosses and UI labels: data `d198110170a3a423bf875b57554bfee423c0680b`; UI `8bafb14d5df5102cba49bacd0ceb58d623fab54e`.
- v2.1 cache and Webster visibility fix: UI `2e7e1b4edca0a0dffe79bdad2b8e59184b9b89ce`. Adds a version-pinned data URL to avoid stale JavaScript and displays selected-word Webster 1828 excerpts beside the Strong's definitions, when the sampled English headword is available.
- This site is isolated under `docs/inspector/`. No changes to CGBC or the separate Bible translation repositories.

## Next expansion
Build public-safe, book-sharded study projections from the existing private research bundle and complete Strong's/Webster datasets, retaining source license metadata and excluding unresolved NWB/ASV associations. Validate the release files separately before hosting the full 66-book viewer.
