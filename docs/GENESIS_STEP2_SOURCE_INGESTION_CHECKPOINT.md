# Step 2: Genesis ingestion pilot started (2026-11-06)

**Actual original bytes accessed:** locally mounted `SOTW_WordStudy_03_DICTIONARIES_LEXICONS_KJV_WEBSTER_2026-11-05.zip` (SHA-256 `a9fbecc8f08063a227ae94da868dfb4c3ad8b98cc3140c492aba17ef77f423eb`). Nested `source_files/strongs-master.zip` SHA-256 `b462cb85fd7e825f1ff57d676a8bfbe4eaac2065b657ea71a5e0d9e260cb8c3b`; original member `strongs-master/hebrew/StrongHebrewG.xml` SHA-256 `1f9659ea208f4c498843a0280dacb1448627c33ca77712642d8705793ab66061`.

**First bounded extraction:** five source-authored Hebrew Strong's dictionary entries H7225, H1254, H430, H8064, H776 were parsed from the original OSIS XML and saved locally as `lexicon-research.json` with a `source-lock.json`. This is **research-only**, not a published data release or proof of occurrence alignment. Full original XML bytes are still in the vetted archive. These dictionary entries are not original-language *occurrence* records, and must not be described as such.

**Important preservation limitation:** The first local prototype flattens source `list` and `note` text into labeled strings; it does not yet guarantee lossless preservation of all original OSIS markup, editorial attributes, references and notes. Therefore it is **not the final canonical importer** and should not be scaled until a lossless source-fields preservation method and round-trip tests are implemented.

**Next:** verify the five pilot records against the live canonical JSON Schema; build a reproducible source parser with raw entry markup or lossless structural representation, source-authored field fidelity tests, exact provenance and hash assertions; then independently identify an approved original-language textual witness for Genesis 1:1 before creating occurrence records. STEP TAHOT is research comparison only, not an automatic published witness or alignment authority. KJV/BSB native tags remain edition-specific evidence. Do not create public word alignments without verification. Keep the original archives in the Foundation preservation plan.

**No GitHub data shards or production runtime integrations were installed by this pilot.**
