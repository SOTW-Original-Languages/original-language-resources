#!/usr/bin/env python3
"""Validate research-only lexical records against exact checked-out canonical schema."""
import argparse, collections, hashlib, json, sys
from pathlib import Path
from jsonschema import Draft202012Validator

def main():
    p=argparse.ArgumentParser()
    p.add_argument('--schema',required=True)
    p.add_argument('--records',required=True)
    p.add_argument('--report',required=True)
    a=p.parse_args()
    schema_bytes=Path(a.schema).read_bytes()
    schema=json.loads(schema_bytes)
    Draft202012Validator.check_schema(schema)
    records=json.loads(Path(a.records).read_text(encoding='utf-8'))
    validator=Draft202012Validator(schema)
    errors=[]; ids=set(); languages=collections.Counter()
    for index,record in enumerate(records):
        rid=record.get('id')
        if rid in ids: errors.append({'index':index,'id':rid,'error':'duplicate id'})
        ids.add(rid); languages[record.get('language')]+=1
        if record.get('release_status')!='research': errors.append({'index':index,'id':rid,'error':'not research-only'})
        for error in validator.iter_errors(record):
            errors.append({'index':index,'id':rid,'path':list(error.absolute_path),'error':error.message})
    report={'schema_sha256':hashlib.sha256(schema_bytes).hexdigest(),
      'schema_git_blob_sha1':hashlib.sha1(b'blob '+str(len(schema_bytes)).encode()+b'\0'+schema_bytes).hexdigest(),
      'records':len(records),'languages':dict(languages),'unique_ids':len(ids),
      'errors':len(errors),'error_examples':errors[:25],
      'scope':'Full checked-out Draft 2020-12 schema; research-only eligible records, not x-pn'}
    Path(a.report).write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(report,indent=2))
    return 1 if errors else 0
if __name__=='__main__':sys.exit(main())
