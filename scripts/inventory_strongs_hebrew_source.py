#!/usr/bin/env python3
"""Inventory the complete vetted Hebrew Strong's OSIS source without publishing it."""
import argparse,collections,hashlib,io,json,zipfile
from pathlib import Path
from xml.etree import ElementTree as ET
OUTER_HASH="a9fbecc8f08063a227ae94da868dfb4c3ad8b98cc3140c492aba17ef77f423eb"
NESTED_HASH="b462cb85fd7e825f1ff57d676a8bfbe4eaac2065b657ea71a5e0d9e260cb8c3b"
XML_HASH="1f9659ea208f4c498843a0280dacb1448627c33ca77712642d8705793ab66061"
NESTED="source_files/strongs-master.zip"
MEMBER="strongs-master/hebrew/StrongHebrewG.xml"
NS="{http://www.bibletechnologies.net/2003/OSIS/namespace}"
sha=lambda b:hashlib.sha256(b).hexdigest()
def main():
    p=argparse.ArgumentParser();p.add_argument("--outer",required=True);p.add_argument("--report",required=True);a=p.parse_args()
    outer=Path(a.outer).read_bytes();assert sha(outer)==OUTER_HASH
    with zipfile.ZipFile(io.BytesIO(outer)) as z: nested=z.read(NESTED)
    assert sha(nested)==NESTED_HASH
    with zipfile.ZipFile(io.BytesIO(nested)) as z: xml=z.read(MEMBER)
    assert sha(xml)==XML_HASH
    root=ET.fromstring(xml)
    entries=[e for e in root.iter(NS+"div") if e.get("type")=="entry"]
    ids=[e.get("n") for e in entries]
    assert all(x and x.isdigit() for x in ids)
    assert len(ids)==len(set(ids)), "Duplicate source-native IDs"
    counts=collections.Counter(child.tag.rsplit("}",1)[-1] for e in entries for child in e)
    missing_word=[n for n,e in zip(ids,entries) if not any(x.tag==NS+"w" and x.get("ID")=="H"+n for x in e)]
    empty_def=[n for n,e in zip(ids,entries) if not any(x.tag in (NS+"list",NS+"note") and "".join(x.itertext()).strip() for x in e)]
    report={"stage":"RESEARCH_SOURCE_INVENTORY","archive_sha256":OUTER_HASH,"nested_sha256":NESTED_HASH,"xml_sha256":XML_HASH,
    "entry_count":len(entries),"unique_native_ids":len(set(ids)),"first_id":ids[0],"last_id":ids[-1],
    "direct_child_tag_counts":dict(sorted(counts.items())),"missing_matching_word_ids":missing_word,
    "missing_reading_content_ids":empty_def,
    "limitations":["Counts describe this source edition only, not canon completeness or publishability",
    "No full canonical export, original-language textual witness, or translation alignment is certified"]}
    Path(a.report).parent.mkdir(parents=True,exist_ok=True)
    Path(a.report).write_text(json.dumps(report,indent=2)+"\n",encoding="utf-8")
    print("PASS: 3 source hashes; entries",len(entries),"unique IDs",len(set(ids)))
    print("Missing matching word IDs:",len(missing_word),"missing reading content:",len(empty_def))
if __name__=="__main__":main()
