#!/usr/bin/env python3
"""Zero-dependency checks of contracts and explicitly synthetic fixtures. NOT a full JSON Schema engine."""
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
schemas = {name: json.loads((ROOT / "schemas" / f"{name}.schema.json").read_text(encoding="utf-8")) for name in ("source-manifest","lexical-entry","word-link")}
fixture = json.loads((ROOT / "examples/NOT_FOR_PUBLICATION.fixture.json").read_text(encoding="utf-8"))
assert fixture["fixture_only"] is True
assert all(schema["$schema"].endswith("2020-12/schema") for schema in schemas.values())
def check(obj, schema):
    assert isinstance(obj, dict)
    assert set(schema["required"]).issubset(obj.keys())
    assert set(obj).issubset(schema["properties"])
    for key, value in obj.items():
        p = schema["properties"][key]
        if "const" in p: assert value == p["const"], key
        if "enum" in p: assert value in p["enum"], key
        if "pattern" in p and value is not None: assert re.fullmatch(p["pattern"], value), key
        kind = p.get("type")
        if kind and not isinstance(kind, list):
            assert isinstance(value, {"object":dict,"array":list,"string":str,"integer":int}[kind]), key
    return True
assert check(fixture["source_manifest"], schemas["source-manifest"])
assert check(fixture["lexical_entry"], schemas["lexical-entry"])
assert check(fixture["word_link"], schemas["word-link"])
assert fixture["source_manifest"]["publication_status"] != "approved_public"
assert fixture["lexical_entry"]["publication_status"] != "approved_public"
assert fixture["word_link"]["status"] == "candidate"
assert fixture["word_link"]["english_occurrence_id"].startswith("synthetic")
assert fixture["lexical_entry"]["source_id"] == fixture["source_manifest"]["source_id"]
assert fixture["word_link"]["evidence"][0]["source_id"] == fixture["source_manifest"]["source_id"]
assert not list((ROOT / "data").rglob("*")) if (ROOT/"data").exists() else True
print("PASS: 3 schema definitions and explicitly non-public synthetic fixture; no source data ingested")
