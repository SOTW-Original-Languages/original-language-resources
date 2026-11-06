# Source intake, rights, and release gates

The historical age or public-domain status of an underlying book **does not** by itself establish the redistribution rights or accuracy of a modern digital transcription.

Every imported dataset requires its own source manifest: exact title, source/version/edition, origin URI, retrieval time, SHA-256 of original bytes, source locator, responsible creators, independently recorded rights basis, attribution, transformations, validation evidence, and publication status. Source records must remain pinned after an approved release.

## Release state machine

`not_ingested` → `research` → `validated` → `approved_public`; alternatively `excluded`. Only `approved_public` records may feed public-resource builds. Publication requires BOTH verified content and separately documented redistribution rights. A machine-valid JSON record does not pass either gate by itself.

## Known candidates (NOT release approvals)

- STEPBible Hebrew/Aramaic and Greek original-language, morphology and lexicon tables: pin exact edition, component-specific notices and rights.
- Historical Strong's Hebrew and Greek: distinguish the underlying nineteenth-century work from each digital edition and extensions.
- Webster 1828 English dictionary: verify exact source transcription and modern editorial licensing.
- Greek and Hebrew expanded lexicons: review provenance, quality and licensing independently.
- BibleAquifer BDB digital edition: **excluded from initial public release** under the recorded 2026-11-05 SOTW decision. The historical BDB book is not categorically prohibited; that specific digital edition lacks sufficient resolved provenance/release verification. Do not auto-import it or distribute its content here.

Refer to [bible-foundation's source guidance](https://github.com/Stewards-of-the-Way/bible-foundation/blob/main/docs/sources-and-rights.md). Do not assume a blanket license for this repository or third-party content. Retain per-component CC BY obligations and other notices.

## Release checks

1. Original source byte hashes and edition labels match pinned manifests.
2. Required provenance and rights evidence is present, and a human release decision is recorded.
3. Text/record validation, referential integrity and independent source sampling pass with documented limits.
4. Ambiguous and disputed links retain their status; only verified links generate asserted contextual word associations.
5. Files for public release are reproducible, size-budgeted, and contain no disallowed data.
6. Any schema/version change has compatibility tests and an explicit migration plan.
