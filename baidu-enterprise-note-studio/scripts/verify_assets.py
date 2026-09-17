#!/usr/bin/env python3
"""Validate portable asset references and SHA256; no third-party dependency."""
from pathlib import Path
import hashlib, json, sys
root=Path(__file__).resolve().parents[1]
errors=[];checked=set()
def walk(obj):
    if isinstance(obj,list):
        for item in obj:walk(item)
    elif isinstance(obj,dict):
        for key in ('path','text','output','protected_source'):
            rel=obj.get(key)
            if not isinstance(rel,str) or not rel.startswith(('assets/','references/')):continue
            p=root/rel
            if not p.is_file():errors.append('Missing '+rel);continue
            checked.add(rel)
            if key in ('path','output') and obj.get('sha256'):
                if hashlib.sha256(p.read_bytes()).hexdigest()!=obj['sha256']:errors.append('Hash mismatch '+rel)
        for item in obj.values():walk(item)
for f in (root/'assets').rglob('manifest.json'):walk(json.loads(f.read_text()))
print(f'Checked {len(checked)} asset paths')
for error in errors:print(error)
sys.exit(bool(errors))
