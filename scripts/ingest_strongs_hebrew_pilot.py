#!/usr/bin/env python3
"""Source-locked Hebrew Strong's pilot. No publication or occurrence claims."""
import argparse, hashlib, io, json, zipfile
from pathlib import Path
from xml.etree import ElementTree as ET
from jsonschema import Draft202012Validator

OUTER="SOTW_WordStudy_03_DICTIONARIES_LEXICONS_KJV_WEBSTER_2026-11-05.zip"
NESTED="source_files/strongs-master.zip"
MEMBER="strongs-master/hebrew/StrongHebrewG.xml"
EXPECTED={
 "outer":"a9fbecc8f08063a227ae94da868dfb4c3ad8b98cc3140c492aba17ef77f423eb",
 "nested":"b462cb85fd7e825f1ff57d676a8bfbe4eaac2065b657ea71a5e0d9e260cb8c3b",
 "xml":"1f9659ea208f4c498843a0280dacb1448627c33ca77712642d8705793ab66061"}
IDS=["H7225","H1254","H430","H8064","H776"]
NS="{http://www.bibletechnologies.net/2003/OSIS/namespace}"
sha=lambda b:hashlib.sha256(b).hexdigest()
def run(outer,schema_path,out):
    outer_bytes=Path(outer).read_bytes()
    assert sha(outer_bytes)==EXPECTED["outer"],"Outer ZIP mismatch"
    with zipfile.ZipFile(io.BytesIO(outer_bytes)) as z: nested=z.read(NESTED)
    assert sha(nested)==EXPECTED["nested"],"Nested ZIP mismatch"
    with zipfile.ZipFile(io.BytesIO(nested)) as z: xml=z.read(MEMBER)
    assert sha(xml)==EXPECTED["xml"],"Source XML mismatch"
    root=ET.fromstring(xml)
    entries={f'H{e.attrib["n"]}':e for e in root.iter(NS+"div") if e.attrib.get("type")=="entry" and e.attrib.get("n","").isdigit()}
    schema=json.loads(Path(schema_path).read_text(encoding="utf-8"))
    Draft202012Validator.check_schema(schema)
    validator=Draft202012Validator(schema)
    records=[];preserved=[]
    for ident in IDS:
        e=entries[ident]
        w=next((x for x in e.iter(NS+"w") if x.attrib.get("ID")==ident),None)
        assert w is not None,ident
        # Flatten only for the required canonical summary field; full structured OSIS retained separately.
        definition=" ".join(" ".join(x.itertext()).strip() for x in e if x.tag in (NS+"list",NS+"note")).strip()
        assert definition
        record={"kind":"lexicon","schema_version":"1.0.0","id":"lexicon:strongs-hebrew:"+ident,
        "resource_id":"strongs-hebrew","native_entry_id":ident,"language":"heb",
        "headword":w.attrib.get("lemma"),"transliteration":w.attrib.get("xlit"),
        "short_definition":None,"full_definition":definition,"kjv_usage":None,
        "strongs_ids":["strongs:"+ident],
        "provenance":{"source_id":"strongs-hebrew-osis-locked","source_locator":MEMBER+"#entry-n="+ident,
                      "source_sha256":EXPECTED["xml"]},"release_status":"research"}
        validator.validate(record)
        # ElementTree serialization retains complete XML node structure, attributes, text, and tails.
        node=ET.tostring(e,encoding="unicode")
        parsed=ET.fromstring(node)
        assert ET.canonicalize(ET.tostring(parsed,encoding="unicode"))==ET.canonicalize(node)
        records.append(record)
        preserved.append({"native_entry_id":ident,"osis_xml":node,"entry_sha256":sha(node.encode("utf-8"))})
    out=Path(out);out.mkdir(parents=True,exist_ok=True)
    (out/"lexicon-research.json").write_text(json.dumps(records,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    (out/"preserved-osis-entries.json").write_text(json.dumps(preserved,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    (out/"source-lock.json").write_text(json.dumps({"stage":"RESEARCH_ONLY","source_archive":OUTER,
        "nested_archive":NESTED,"xml_member":MEMBER,"sha256":EXPECTED,"entry_ids":IDS,
        "limitations":["Serialized entry subtree preserves XML infoset, not exact original byte spans",
        "Canonical full_definition is a lossy reading summary; preserved OSIS is required",
        "No original-language verse witness or alignment verified"]},indent=2)+"\n",encoding="utf-8")
    print("PASS: all 3 pinned source hashes; 5 canonical schema records; 5 OSIS subtree round trips")
if __name__=="__main__":
    ap=argparse.ArgumentParser();ap.add_argument("--outer",required=True);ap.add_argument("--schema",required=True);ap.add_argument("--out",required=True)
    a=ap.parse_args();run(a.outer,a.schema,a.out)
