# Bible Foundation compatibility verification: v0.1 → SOTW v1

This check is intentionally **narrow**. The Foundation currently supplies a reference-only v0.1 contract, not a completed original-language catalog. Its live contract files and blob SHAs were fetched and recorded in `compatibility/foundation-v0.1.snapshot.json`. The snapshot includes the exact Foundation reference schema and synthetic John 1:1–5 fixture for reproducible offline CI.

Run `python scripts/validate_foundation_compatibility.py` after installing `jsonschema>=4.18,<5`. The test verifies Foundation and SOTW JSON Schema validity, Scripture reference syntax, fixtures, nonzero chapter/verse numbers, and distinct original-language records. The SOTW verse-ID regex was corrected to the Foundation's 3–8 character book-code contract, rather than the prior three-character-only pattern.

**Important:** The Foundation snapshot is pinned by Git blob SHAs, not guaranteed to be the latest live state indefinitely. A later foundation change requires explicit review and snapshot refresh. No full 66-book catalog has been certified. This test does not certify real source bytes, licenses, complete edition mappings, original-language witness identity, or translation alignment. Public release still requires the separate SOTW rights and evidence gates. No CGBC or other runtime integration is authorized.
