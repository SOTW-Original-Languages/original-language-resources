#!/usr/bin/env python3
"""Validate SOTW canonical v1 against pinned Bible Foundation v0.1 contracts."""
import json
import re
from pathlib import Path
from jsonschema import Draft202012Validator

ROOT = Path(__file__).resolve().parents[1]
read = lambda p: json.loads((ROOT / p).read_text(encoding="utf-8"))

def main():
    pin = read("compatibility/foundation-v0.1.snapshot.json")
    foundation = pin["foundation_reference_schema"]
    fixture = pin["foundation_reference_fixture"]
    sotw = read("schemas/sotw-canonical-v1.schema.json")
    records = read("examples/sotw-canonical-v1.synthetic.json")
    Draft202012Validator.check_schema(foundation)
    Draft202012Validator.check_schema(sotw)
    Draft202012Validator(foundation).validate(fixture)
    for rec in records:
        Draft202012Validator(sotw).validate(rec)
    assert pin["foundation_repository"] == "Stewards-of-the-Way/bible-foundation"
    assert all(len(f["blob_sha"]) == 40 and re.fullmatch("[0-9a-f]{40}", f["blob_sha"]) for f in pin["foundation_contracts"])
    # Reference syntax: every valid Foundation ID shape must fit SOTW's verse field.
    fpat = foundation["properties"]["references"]["items"]["properties"]["id"]["pattern"]
    for kind in ("occurrence", "link"):
        spat = sotw["$defs"][kind]["properties"]["verse_id"]["pattern"]
        assert spat == fpat, f"{kind} verse syntax diverges from Foundation"
        for code in ("GEN", "JHN", "LONGBOOK"):
            ref = f"{code}.1.1"
            assert re.fullmatch(fpat, ref) and re.fullmatch(spat, ref)
        for invalid in ("GEN.0.1", "GEN.1.0", "GEN.01.1", "GENESIS 1:1"):
            assert not re.fullmatch(spat, invalid)
    for ref in fixture["references"]:
        assert ref["id"] == f'{fixture["book_code"]}.{ref["chapter"]}.{ref["verse"]}'
        assert ref["verse_text_present"] is False
    assert {"source","occurrence","lexicon","link"}.issubset(sotw["$defs"])
    assert sotw["$defs"]["occurrence"]["properties"]["strongs_ids"]["type"] == "array"
    assert sotw["$defs"]["link"]["properties"]["status"]["enum"] == ["verified","candidate","disputed","rejected"]
    assert "approved_public" in sotw["$defs"]["release"]["enum"]
    assert not any("verse_text" in r for r in records)
    print("PASS: pinned Foundation v0.1 schema and reference fixture")
    print("PASS: SOTW fixture and schema")
    print("PASS: shared Scripture reference syntax including 3-8 character book codes")
    print("PASS: distinct lexical/link records and no translation verse text in fixtures")
    print("LIMIT: source archive hashes, rights, full book catalog, real edition IDs,")
    print("       cross-repository foreign keys and production publication not certified")

if __name__ == "__main__":
    main()
