#!/usr/bin/env python3
"""Audit every Hebrew Strong's source entry. Requires vetted original archive locally."""
import argparse,collections,hashlib,io,json,zipfile
from pathlib import Path
from xml.etree import ElementTree as E
OUTER_HASH="a9fbecc8f08063a227ae94da868dfb4c3ad8b98cc3140c492aba17ef77f423eb"
NESTED_HASH="b462cb85fd7e825f1ff57d676a8bfbe4eaac2065b657ea71a5e0d9e260cb8c3b"
XML_HASH="1f9659ea208f4c498843a0280dacb1448627c33ca77712642d8705793ab66061"
NS="{http://www.bibletechnologies.net/2003/OSIS/namespace}"
sha=lambda b:hashlib.sha256(b).hexdigest()
def run(archive,output):
    outer=Path(archive).read_bytes();assert sha(outer)==OUTER_HASH
    with zipfile.ZipFile(io.BytesIO(outer)) as z:nested=z.read("source_files/strongs-master.zip")
    assert sha(nested)==NESTED_HASH
    with zipfile.ZipFile(io.BytesIO(nested)) as z:xml=z.read("strongs-master/hebrew/StrongHebrewG.xml")
    assert sha(xml)==XML_HASH
    root=E.fromstring(xml)
    entries=[e for e in root.iter(NS+"div") if e.get("type")=="entry"]
    assert len(entries)==8674
    exceptions=collections.defaultdict(list); children=collections.Counter(); tags=collections.Counter(); attrs=collections.Counter()
    for e in entries:
        n=e.get("n");word=[x for x in e if x.tag==NS+"w"]
        for c in e:children[c.tag.rsplit("}",1)[-1]]+=1
        for node in e.iter():
            tags[node.tag.rsplit("}",1)[-1]]+=1
            for a in node.attrib:attrs[a]+=1
        if len(word)!=1:exceptions["non_single_word"].append(n)
        if not word or word[0].get("ID")!="H"+n:exceptions["mismatched_word_id"].append(n)
        if not any(x.tag==NS+"list" for x in e):exceptions["no_list"].append(n)
        if not any(x.tag==NS+"note" for x in e):exceptions["no_note"].append(n)
        if not any(x.tag==NS+"list" and "".join(x.itertext()).strip() for x in e):exceptions["empty_list"].append(n)
        if not word or not word[0].get("lemma"):exceptions["missing_lemma_attribute"].append(n)
        if not word or not word[0].get("xlit"):exceptions["missing_xlit_attribute"].append(n)
        rendered=E.tostring(e,encoding="unicode")
        if E.canonicalize(rendered)!=E.canonicalize(E.tostring(E.fromstring(rendered),encoding="unicode")):
            exceptions["xml_roundtrip_mismatch"].append(n)
    assert len(set(e.get("n") for e in entries))==8674
    report={"stage":"RESEARCH_SOURCE_FIDELITY","outer_sha256":OUTER_HASH,"nested_sha256":NESTED_HASH,
    "xml_sha256":XML_HASH,"entries_audited":len(entries),"unique_ids":8674,
    "direct_child_counts":dict(children),"all_element_counts":dict(tags),"attribute_counts":dict(attrs),
    "exception_counts":{k:len(v) for k,v in exceptions.items()},"exceptions":dict(exceptions),
    "limitations":["XML subtree round trips are not byte-exact original entry slices",
    "Not a canonical export or full-definition fidelity proof","Not a Genesis textual witness or public alignment validation"]}
    Path(output).write_text(json.dumps(report,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    assert not exceptions, "Source field/structure exceptions detected"
    print("PASS: 8674 source entries; unique IDs; required structural fields; XML round trips")
if __name__=="__main__":
    p=argparse.ArgumentParser();p.add_argument("--outer",required=True);p.add_argument("--report",required=True)
    a=p.parse_args();run(a.outer,a.report)
