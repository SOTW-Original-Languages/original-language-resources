# SOTW Canonical Schema v1: Genesis pilot

**Step 1 implemented:** JSON Schema Draft 2020-12 at `schemas/sotw-canonical-v1.schema.json`. The fixture file `examples/sotw-canonical-v1.synthetic.json` is **synthetic only**, not biblical data, and must never be published as source content. The fixture contains a disputed link deliberately to test public exclusion.

## Record types
- `source`: exact edition, source SHA-256, origin, rights declaration and release state.
- `occurrence`: source/witness-specific original-language word occurrence, verse ID, position, surface, optional lemma/root, morphology and **array** of native Strong's IDs.
- `lexicon`: native entry identity, full source-authored definition, optional source-authored short definition, KJV usage separate, Strong's references and provenance.
- `link`: edition-specific English occurrence to original occurrence; explicit mapping method, source evidence, link status and release state. No English verse text stored in this library.

## Publisher invariants (must be implemented and tested in Step 2)
1. Only records marked `approved_public` may be exported. For `link` records, additionally require `status=verified`; candidate, disputed and rejected links are never displayed as asserted associations.
2. Verify every reference resolves to a pinned source/witness/occurrence in the build catalog. Verify hash against actual source bytes, not just schema shape.
3. A Strong's ID is not an occurrence identity, lemma, morphology, or contextual sense. No invented quick definitions. Preserve source-authored alternatives.
4. English edition tokens and texts stay in edition repositories. This schema references their stable IDs only.
5. `release_status` is an explicit gate, not automatically assigned by parsing. Rights and content validation are separate from syntactic JSON Schema validation.
6. Do not infer alignments from matching Strong's IDs. If a link is unresolved, keep evidence internally and exclude that claim from public projection.
7. Use foundation book codes and version-pinned source identities. Schema migration requires versioned compatibility tests.

## Next step
Create ingestion and validation scripts, inspect existing repository schemas and foundation contracts for compatibility, load the **real vetted** Genesis 1:1 source slice, produce validated canonical records and public-exclusion tests, then expand to Genesis 1 and Genesis. No original source archives were moved or deleted in Step 1.
