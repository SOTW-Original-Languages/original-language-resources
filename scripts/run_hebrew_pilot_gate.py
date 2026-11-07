#!/usr/bin/env python3
"""Run the committed Hebrew pilot importer and independent audit using the repository schema.
Original ZIP stays outside GitHub. This command refuses missing or modified source files.
Usage:
 python scripts/run_hebrew_pilot_gate.py --outer /path/to/SOTW_WordStudy_03_DICTIONARIES_LEXICONS_KJV_WEBSTER_2026-11-05.zip --out /tmp/sotw-hebrew-pilot
"""
import argparse,subprocess,sys
from pathlib import Path
def main():
    p=argparse.ArgumentParser()
    p.add_argument("--outer",required=True)
    p.add_argument("--out",required=True)
    a=p.parse_args()
    root=Path(__file__).resolve().parents[1]
    schema=root/"schemas/sotw-canonical-v1.schema.json"
    importer=root/"scripts/ingest_strongs_hebrew_pilot.py"
    audit=root/"scripts/audit_strongs_hebrew_pilot.py"
    for item in (schema,importer,audit,Path(a.outer)):
        if not item.is_file():p.error("Required file missing: "+str(item))
    out=Path(a.out).resolve()
    if out==root or root in out.parents:p.error("Refusing to write generated research artifacts inside repository")
    subprocess.run([sys.executable,str(importer),"--outer",a.outer,"--schema",str(schema),"--out",str(out)],check=True)
    subprocess.run([sys.executable,str(audit),"--outer",a.outer,"--schema",str(schema),"--generated",str(out)],check=True)
    print("PASS: complete 5-entry importer + independent audit against checked-out canonical schema")
    print("RESEARCH ONLY: no public release, no textual witness or alignment certification")
if __name__=="__main__":main()
