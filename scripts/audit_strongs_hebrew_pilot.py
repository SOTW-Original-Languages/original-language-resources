#!/usr/bin/env python3
"""Audit a locally generated Hebrew Strong's pilot against the original archive.

Requires original archive supplied by the owner. No source archive is committed to GitHub.
"""
import argparse, hashlib, io, json, zipfile
from pathlib import Path
from xml.etree import ElementTree as ET
from jsonschema import Draft202012Validator

MEMBER="strongs-master/hebrew/StrongHebrewG.xml"
NESTED="source_files/strongs-master.zip"
EXPECTED={"outer":"a9fbecc8f08063a227ae94da868dfb4c3ad8b98cc3140c492aba17ef77f423eb",
"nested":"b462cb85fd7e825f1ff57d676a8bfbe4eaac2065b657ea71a5e0d9e260cb8c3b",
"xml":"1f9659ea208f4c498843a0280dacb1448627c33ca77712642d8705793ab66061"}
IDS=["H7225","H1254","H430","H8064","H776"]
NS="{http://www.bibletechnologies.net/2003/OSIS/namespace}"
sha=lambda b:hashlib.sha256(b).hexdigest()

def audit(archive, schema, generated):
    outer=Path(archive).read_bytes()
    assert sha(outer)==EXPECTED["outer"],"original archive hash changed"
    with zipfile.ZipFile(io.BytesIO(outer)) as z: nested=z.read(NESTED)
    assert sha(nested)==EXPECTED["nested"],"nested archive hash changed"
    with zipfile.ZipFile(io.BytesIO(nested)) as z: original=z.read(MEMBER)
    assert sha(original)==EXPECTED["xml"],"original XML hash changed"
    root=ET.fromstring(original)
    original_entries={f'H{e.attrib["n"]}':e for e in root.iter(NS+"div")
                      if e.attrib.get("type")=="entry" and e.attrib.get("n","").isdigit()}
    records=json.loads((Path(generated)/"lexicon-research.json").read_text(encoding="utf-8"))
    preserved=json.loads((Path(generated)/"preserved-osis-entries.json").read_text(encoding="utf-8"))
    assert [r["native_entry_id"] for r in records]==IDS
    assert [p["native_entry_id"] for p in preserved]==IDS
    validator=Draft202012Validator(json.loads(Path(schema).read_text(encoding="utf-8")))
    for r,p in zip(records,preserved):
        validator.validate(r)
        ident=r["native_entry_id"]
        assert r["release_status"]=="research"
        assert r["provenance"]["source_sha256"]==EXPECTED["xml"]
        assert r["strongs_ids"]==["strongs:"+ident]
        assert sha(p["osis_xml"].encode("utf-8"))==p["entry_sha256"]
        # Canonical XML equivalence is stricter than text-only equivalence;
        # it compares the source entry subtree, not the original byte span.
        expected=ET.canonicalize(ET.tostring(original_entries[ident],encoding="unicode"))
        actual=ET.canonicalize(p["osis_xml"])
        assert expected==actual, f"OSIS subtree changed: {ident}"
    print("PASS: 3 pinned original-source hashes")
    print("PASS: 5 canonical lexical records validated against supplied schema")
    print("PASS: 5 preserved OSIS subtrees match original XML canonicalization")
    print("PASS: all entries remain research-only")
    print("NOT TESTED: full lexicon, Hebrew textual witness, verse occurrences, public links")

if __name__=="__main__":
    p=argparse.ArgumentParser()
    p.add_argument("--outer",required=True);p.add_argument("--schema",required=True);p.add_argument("--generated",required=True)
    a=p.parse_args();audit(a.outer,a.schema,a.generated)
