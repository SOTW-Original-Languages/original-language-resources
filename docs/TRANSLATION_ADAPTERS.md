# Translation-specific adapters

The common translation editions are `ASV1901`, `KJV1769`, `BSB`, and `WEBSTER1833`. These are contract IDs, **not evidence that word alignments have been ingested or verified**.

Each adapter is maintained or generated from its *own* translation repository. Store verse ID, edition ID, immutable verse-text source identity/checksum, English occurrence or exact span ID, original-language text edition and occurrence ID, mapping method, original source locators, cross-check evidence, and link status.

A common Strong's number does **not** establish that two English words have the same contextual usage. KJV may follow different readings than STEPBible's base witness; preserve differing textual witnesses and unavailable alignments explicitly.

Existing ASV chapter content and its supplied/special spans must remain unchanged; add independent versioned mapping files. The KJV USFM tagging and BSB table-derived links are candidates for intake now, not automatically trusted verified alignments. Webster 1833 can be wired later using the same interface.

Example adapters in `examples/` are intentionally synthetic, contain **no Bible verse text or true word-level assertion**, and must never be read by a public release pipeline.
