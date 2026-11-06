# SOTW Original Language & Lexicon Library — architecture seed 0.1

## Role and boundaries

This is the **dedicated resource repository** of the independent GitHub organization `SOTW-Original-Languages`. It is a consumer of the shared interoperability rules in [Stewards-of-the-Way/bible-foundation](https://github.com/Stewards-of-the-Way/bible-foundation), not a replacement for that foundation.

Keep separate organizations/repositories for ASV 1901, KJV 1769, BSB, Webster Bible 1833, and historical commentaries. English translation verse text and translation-specific English token spans belong to their own editions; they are **not** copied into the shared lexicon collection.

The four layers are: (1) source manifests and immutable independently preserved originals; (2) authoritative approved original-language and dictionary records; (3) evidence-backed, edition-specific connections; (4) reproducibly generated reader/search projections. A display tool never becomes the authoritative source.

## Stable identities

- Reference: `GEN.1.1` and `JHN.1.1`, following the pinned book-code catalog in bible-foundation.
- Edition verse: `ASV1901:GEN.1.1`, `KJV1769:GEN.1.1`, `BSB:GEN.1.1`, `WEBSTER1833:GEN.1.1`.
- Strong's IDs: `strongs:H1254` or `strongs:G3056`, with the script prefix. Do not silently normalize variants or conflate Strong's numbering with an individual lexicon's headword IDs.
- Dictionary entry: `lexicon:<resource-id>:<native-entry-id>`; the source's native ID remains recorded.
- Original-language occurrence: opaque, source-and-text-edition-specific ID, bound to a pinned textual witness and exact location. It is **not** an English character offset or Strong's number.
- An English token occurrence ID is edition-specific; it must carry an explicit source/edition, verse ID, token/span ID and verified relationship to any original-language occurrence.
- Root, lemma, lexical entry, inflected form, morphology and contextual sense are separate concepts.

## Links and evidence

Links between an English word and an original-language token may be `verified`, `candidate`, `disputed`, or `rejected`, with source evidence. A dictionary candidate is **never** equivalent to a verified contextual sense. Preserve alternate textual traditions and KJV/ASV textual differences rather than forcing common alignment.

## Public/restricted separation

No restricted source archive, internal research transcript, publisher-licensed corpus or unapproved lexicon content should be added to a public GitHub repository. Public source manifests may reference lawful source locations and hashes but should not include private file paths or secrets. Maintain original source byte hashes outside GitHub when necessary.

No automatic publication or production integrations. CGBC's independent production player and sermon knowledge are out of scope.

## First implementation objective

A verified end-to-end test slice of original-language occurrences plus ASV/KJV/BSB *link evidence* on a small passage. Webster Bible 1833 uses the same adapter contract later; Webster 1828 is a distinct English **dictionary**, not that Bible translation. No inferred alignment is approved just because a Strong's number matches.
