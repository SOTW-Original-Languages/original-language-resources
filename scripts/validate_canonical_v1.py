#!/usr/bin/env python3
"""Validate SOTW canonical v1 schema, synthetic fixtures, and exclusion policy.

Run: python -m pip install jsonschema>=4.18
     python scripts/validate_canonical_v1.py
No source files are downloaded and no public release is performed.
"""
import copy
import json
from pathlib import Path

from jsonschema import Draft202012Validator

ROOT = Path(__file__).resolve().parents[1]
SCHEMA = ROOT / "schemas/sotw-canonical-v1.schema.json"
FIXTURES = ROOT / "examples/sotw-canonical-v1.synthetic.json"


def public_eligible(record):
    return record["release_status"] == "approved_public" and (
        record["kind"] != "link" or record["status"] == "verified"
    )


def main():
    schema = json.loads(SCHEMA.read_text(encoding="utf-8"))
    records = json.loads(FIXTURES.read_text(encoding="utf-8"))
    Draft202012Validator.check_schema(schema)
    validator = Draft202012Validator(schema)
    assert isinstance(records, list) and len(records) == 4
    for record in records:
        validator.validate(record)

    def reject(name, changed):
        errors = list(validator.iter_errors(changed))
        assert errors, f"{name}: invalid record was accepted"

    bad = copy.deepcopy(records[1])
    bad["strongs_ids"] = ["strongs:H1", "strongs:H1"]
    reject("duplicate Strong's tags", bad)

    bad = copy.deepcopy(records[1])
    bad["strongs_ids"] = ["strongs:X123"]
    reject("invalid Strong's namespace", bad)

    bad = copy.deepcopy(records[1])
    bad["verse_id"] = "GENESIS 1:1"
    reject("invalid verse ID", bad)

    bad = copy.deepcopy(records[1])
    bad["extra_unapproved_field"] = True
    reject("unknown field", bad)

    bad = copy.deepcopy(records[2])
    bad["full_definition"] = ""
    reject("empty full definition", bad)

    bad = copy.deepcopy(records[3])
    bad["evidence"] = []
    reject("link missing evidence", bad)

    bad = copy.deepcopy(records[0])
    bad["sha256"] = "not-a-hash"
    reject("invalid source hash", bad)

    assert not any(public_eligible(record) for record in records)
    for status in ("candidate", "disputed", "rejected"):
        bad = copy.deepcopy(records[3])
        bad["status"] = status
        bad["release_status"] = "approved_public"
        validator.validate(bad)  # syntactically valid, but never publishable
        assert not public_eligible(bad), f"{status} leaked to public"
    good = copy.deepcopy(records[3])
    good["status"] = "verified"
    good["release_status"] = "approved_public"
    validator.validate(good)
    assert public_eligible(good)

    print("PASS: Draft 2020-12 schema valid")
    print("PASS: 4 synthetic fixtures valid")
    print("PASS: 7 negative-schema cases rejected")
    print("PASS: 3 unresolved link statuses excluded from public projection")
    print("PASS: verified+approved link eligible (policy only)")
    print("NOTE: no source-byte, foundation-ID, real Genesis, or rights audit performed")


if __name__ == "__main__":
    main()

# CI trigger: execute the pinned canonical-v1 validation suite (2026-11-06).
