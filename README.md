# SOTW Original Language & Lexicon Resources

The independent **SOTW-Original-Languages** organization's shared, source-verified Hebrew, Biblical Aramaic, Greek, Strong's, morphology, lexicon, and historical English-dictionary resource library.

**Current status: architecture seed 0.1. NO real dictionary, original-language corpus, translation text, or word-alignment records are included or approved by this initialization.** The example records are fictional and must never be published as biblical evidence.

## Starting points

- [Architecture and shared identifiers](docs/ARCHITECTURE.md)
- [Source rights and publication gates](docs/SOURCES_AND_RELEASE.md)
- [ASV, KJV, BSB, Webster 1833 translation adapters](docs/TRANSLATION_ADAPTERS.md)
- [Implementation sequence](docs/BUILD_SEQUENCE.md)
- JSON Schema 2020-12 contracts in `schemas/`: source manifest, lexical entry, word link
- Explicitly synthetic `examples/NOT_FOR_PUBLICATION.fixture.json`
- Zero-dependency fixture smoke test: `python3 scripts/validate.py`

## What lives where

- **[Stewards-of-the-Way/bible-foundation](https://github.com/Stewards-of-the-Way/bible-foundation):** canonical Scripture ID and source-rights interoperability standards.
- **[SOTW-ASV-1901/asv-1901-resources](https://github.com/SOTW-ASV-1901/asv-1901-resources):** ASV original text and related edition resources, untouched by this repository.
- **Other translation organizations:** own their KJV, BSB and Webster Bible texts and edition-specific English occurrences.
- **[SOTW-Historical-Commentaries](https://github.com/SOTW-Historical-Commentaries):** independent commentary collection, not included in this library.
- **This repository:** future approved original-language records, Strong's, morphology, and dictionaries with evidence-backed links.

## Rights and publication

No blanket third-party license is asserted. Each source has its own provenance, rights evidence, pinned SHA-256 and approval status. No public ingestion of unapproved BDB: the candidate BibleAquifer digital BDB edition is **excluded from the initial public release** under the recorded SOTW 2026-11-05 decision. Do not equate matching Strong's numbers or candidate lexicon links with verified contextual word meanings.

This repository is a data foundation, **not** a deployed website, API, public reader, or GitHub Pages service. Production integrations, including the independently governed CGBC Sermon Player, require separately authorized changes.
