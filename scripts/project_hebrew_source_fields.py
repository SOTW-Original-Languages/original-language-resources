#!/usr/bin/env python3
"""Deterministic OSIS source-field projection, research-only; never guess x-pn language."""
import argparse,collections,hashlib,json,xml.etree.ElementTree as ET
from pathlib import Path
XML_LANG="{http://www.w3.org/XML/1998/namespace}lang"
NS="{http://www.bibletechnologies.net/2003/OSIS/namespace}"
sha=lambda s:hashlib.sha256(s.encode("utf-8")).hexdigest()
def run(source,out):
    entries=json.loads(Path(source).read_text(encoding="utf-8"))
    result=[]; markers=collections.Counter(); note_counts=collections.Counter()
    for item in entries:
        ident=item["native_entry_id"]; raw=item["osis_xml"]
        assert sha(raw)==item["entry_sha256"],ident
        e=ET.fromstring(raw)
        assert e.get("n") and ident=="H"+e.get("n")
        words=[w for w in e if w.tag==NS+"w"]
        assert len(words)==1 and words[0].get("ID")==ident,ident
        w=words[0]; marker=w.get(XML_LANG)
        assert marker in ("heb","arc","x-pn"),(ident,marker)
        markers[marker]+=1
        notes=[]
        for n in e:
            if n.tag==NS+"note":
                kind=n.get("type")
                note_counts[kind]+=1
                notes.append({"type":kind,"source_text":"".join(n.itertext()),"osis_xml":ET.tostring(n,encoding="unicode")})
        result.append({"native_entry_id":ident,"source_language_marker":marker,
            "canonical_language":marker if marker in ("heb","arc") else None,
            "source_marker_is_proper_name":marker=="x-pn",
            "headword":w.get("lemma"),"transliteration":w.get("xlit"),
            "word_attributes":dict(w.attrib),
            "list_xml":[ET.tostring(n,encoding="unicode") for n in e if n.tag==NS+"list"],
            "notes":notes,"source_entry_sha256":item["entry_sha256"],
            "release_status":"research"})
    assert len(result)==len({r["native_entry_id"] for r in result})==8674
    assert dict(markers)=={"heb":5393,"arc":653,"x-pn":2628}
    assert dict(note_counts)=={"exegesis":8670,"explanation":8674,"translation":8674,"x-typo":124}
    target=Path(out);target.mkdir(parents=True,exist_ok=True)
    (target/"source-fields-research.json").write_text(json.dumps(result,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    report={"entries":len(result),"source_language_markers":dict(markers),"note_types":dict(note_counts),
       "proper_name_language_policy":"unknown; source marker x-pn preserved, no invented canonical language",
       "translation_note_policy":"source type retained; not automatically equated to KJV usage",
       "definition_policy":"original OSIS list XML retained; no flattened text certified",
       "release_status":"research"}
    (target/"REPORT.json").write_text(json.dumps(report,indent=2)+"\n",encoding="utf-8")
    print(json.dumps(report,indent=2))
if __name__=="__main__":
    p=argparse.ArgumentParser();p.add_argument("--source",required=True);p.add_argument("--out",required=True)
    a=p.parse_args();run(a.source,a.out)
