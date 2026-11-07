# Hebrew Strong's | Plain-file working state

**Status:** INCOMPLETE UPLOAD. No ZIP is required in this directory. The four source-derived JSON files have **not** yet been transferred to GitHub. Do not treat this directory as a recoverable full research snapshot until all files exist and validation passes.

## Fixed paths

- `data/strongs_digital_selected_research.json` — 8,674 selected digital-edition entries, source provenance, full typed fields
- `indexes/lookup_by_strongs.json` — ID lookup
- `indexes/token_to_strongs.json` — search token index
- `indexes/literal_reference_hooks.json` — unverified literal references
- `WORKING_FILES_MANIFEST.json` — SHA-256 generated after all files are present

These are **research-only** files, not an approved public dictionary. Keep source data and public display projections separate.

## One-command validation

From repository root: `python3 scripts/validate_hebrew_working_files.py`

At every substantive checkpoint: update changed regular files at the same paths, validate, then update `docs/SOTW_LIVE_PROGRESS_LOG.md`. No dated snapshot archives. The repository's commit history preserves earlier file versions.

**Current limitation:** The GitHub connector can write text content but cannot automatically read the multi-megabyte JSON files in the separate local workspace. Until the four files are transferred, the progress log must say **INCOMPLETE UPLOAD**. No claims of completed transfer.
