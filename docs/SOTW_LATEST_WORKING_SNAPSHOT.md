# SOTW Latest Working Snapshot — canonical handoff pointer

**Date:** 2026-11-07  
**Status:** Owner expressly accepts public-repository snapshot storage and its risks. Snapshot assembled and hash-verified; **ZIP NOT YET UPLOADED TO GITHUB**. Do not claim GitHub contains actual work bytes.  
**Research stage:** Strong's Hebrew selected digital edition + exact-ID/search index; no production script or player changes.

## Latest exact snapshot

- Intended stable GitHub upload location: `research/snapshots/SOTW_HEBREW_LATEST_WORKING_SNAPSHOT.zip` (**NOT PRESENT UNTIL UPLOADED AND VERIFIED**).
- Locally generated upload candidate: `SOTW_HEBREW_LATEST_WORKING_SNAPSHOT_2026-11-07.zip`
- SHA-256: `fcfbe18b121e4e0eee89b20dcfcc5744f439ab982dde17e5166c15dfd4f19f6c`
- Bytes: `1836147`
- Contents: `SNAPSHOT_MANIFEST.json`, `README.md`, and three nested ZIPs: complete 8,674-entry selected digital research record, 8,674-ID/token lookup index, and normalization reconciliation.
- **Owner authorization (2026-11-07):** Owner expressly accepts the risk of keeping this temporary latest working snapshot in the existing public/unlisted GitHub repository, with no private repository needed. This authorizes snapshot storage only, not release of the dictionary as a product. GitHub history may retain old versions even after replacement or deletion. Preserve exact source provenance and do not include unrelated private CGBC corpus.

## Included artifacts (exact SHA-256)

| File | SHA-256 |
| --- | --- |
| `SOTW_STRONGS_DIGITAL_EDITION_RESTORED_RESEARCH_2026-11-07.zip` | `f081696a6610ff939a0608b5a7c2612c05c82008734c72bf2596e187d55c1d7a` |
| `SOTW_STRONGS_LOOKUP_RESEARCH_INDEX_2026-11-07.zip` | `4b46075283a2cc0e27d9fbc4c63a24c9bc489b5bc5513dc9a243bb214692bfac` |
| `SOTW_STRONGS_NORMALIZATION_RECONCILIATION_2026-11-07.zip` | `be6909b1f5cce3b0aa6b9557cc008688ed5766e1801486e0a75c44b26b062b4a` |

## Required checkpoint workflow

1. At each substantive report-back, save the **actual newest working data and code**, not only a summary, into one new ZIP with an embedded manifest and hashes.
2. Use the owner-authorized existing repository. Upload/replace the **same stable path**; do not create dated GitHub snapshot files. Git history will retain prior versions; avoid repeated dated filenames in the repo.
3. Fetch the GitHub-uploaded file or its verified metadata and compare SHA-256 against the local ZIP. Until verified, mark `NOT UPLOADED` and never tell a new thread the file is retrievable from GitHub.
4. Update **this same pointer** with the actual uploaded path, SHA, included artifact versions, and status. Update [Live Progress Log](SOTW_LIVE_PROGRESS_LOG.md) in the same reporting cycle.
5. New threads read this pointer and the [Live Progress Log](SOTW_LIVE_PROGRESS_LOG.md), then retrieve the actual latest snapshot **if its presence is verified**. Read the [Durable Decisions](SOTW_DURABLE_DECISIONS_AND_CONTINUITY.md) and [Vetted Sources](SOTW_VETTED_SOURCE_AND_ARTIFACT_INDEX.md) before changing scope.
6. No public dictionary, player, schema, or production deployment is implied by snapshot storage.

## Immediate next work

Build a deterministic research-only display projection from the selected Strong's digital source and existing typed structures, preserving full useful source material and provenance; connect the current lookup index; validate fields. Do not restart 1894 scan research or external lexicon substitution.
