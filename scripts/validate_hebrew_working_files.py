#!/usr/bin/env python3
"""Validate a plain-file Strong's research workspace. Standard library only."""
import argparse, hashlib, json, pathlib, sys

REQUIRED = (
    "data/strongs_digital_selected_research.json",
    "indexes/lookup_by_strongs.json",
    "indexes/token_to_strongs.json",
    "indexes/literal_reference_hooks.json",
)
def sha(path):
    h = hashlib.sha256()
    with path.open("rb") as f:
        for block in iter(lambda: f.read(1024 * 1024), b""):
            h.update(block)
    return h.hexdigest()
def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--root",default="research/hebrew-strongs")
    args=ap.parse_args()
    root=pathlib.Path(args.root)
    missing=[name for name in REQUIRED if not (root/name).is_file()]
    if missing:
        print("INCOMPLETE: required plain files missing:", *missing, sep="\n  ")
        return 2
    data=json.loads((root/REQUIRED[0]).read_text(encoding="utf-8"))
    ids=[x["strongs_id"] for x in data]
    if len(data)!=8674 or len(set(ids))!=len(ids):
        print("FAIL: expected 8674 unique Strong's entries")
        return 1
    lookup=json.loads((root/REQUIRED[1]).read_text(encoding="utf-8"))
    if set(lookup)!=set(ids):
        print("FAIL: lookup IDs do not match research entries")
        return 1
    manifest={"status":"research_only_not_publication_cleared","entry_count":len(data),
              "files":{name:{"bytes":(root/name).stat().st_size,"sha256":sha(root/name)}
                       for name in REQUIRED}}
    (root/"WORKING_FILES_MANIFEST.json").write_text(json.dumps(manifest,indent=2)+"\n",encoding="utf-8")
    print("PASS: 8674 entries, matching lookup IDs, file hashes recorded")
    return 0
if __name__=="__main__":
    sys.exit(main())
