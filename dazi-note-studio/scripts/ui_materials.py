#!/usr/bin/env python3
"""Query and verify the portable DuMate UI material library (stdlib only)."""
import argparse
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / 'assets/ui-library/manifest.json'

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('command', choices=['list', 'search', 'show', 'verify'])
    parser.add_argument('query', nargs='*')
    args = parser.parse_args()
    data = json.loads(MANIFEST.read_text(encoding='utf-8'))
    items = data['items']
    if args.command == 'verify':
        failures = []
        for item in items:
            file = ROOT / item['path']
            if not file.is_file():
                failures.append({'id': item['id'], 'error': 'missing file'})
            elif hashlib.sha256(file.read_bytes()).hexdigest() != item['sha256']:
                failures.append({'id': item['id'], 'error': 'SHA256 mismatch'})
            if item.get('artifact_path'):
                artifact = ROOT / item['artifact_path']
                if not artifact.is_file() or hashlib.sha256(artifact.read_bytes()).hexdigest() != item['artifact_sha256']:
                    failures.append({'id': item['id'], 'error': 'artifact missing or SHA256 mismatch'})
        print(json.dumps({'count': len(items), 'failures': failures}, ensure_ascii=False, indent=2))
        raise SystemExit(bool(failures))
    if args.command == 'show':
        found = [x for x in items if x['id'] in args.query]
        if not found:
            parser.error('素材ID不存在')
        for item in found:
            print(json.dumps({**item, 'absolute_path': str(ROOT / item['path'])}, ensure_ascii=False, indent=2))
        return
    ranked = []
    for item in items:
        hay = ' '.join([item['id'], item['title'], item['category'], ' '.join(item.get('tags', [])), item.get('scope', '')]).lower()
        score = sum(word.lower() in hay for word in args.query)
        if args.command == 'list' or score or not args.query:
            ranked.append((score, item))
    for score, item in sorted(ranked, key=lambda row: (-row[0], row[1]['id'])):
        print(f"{item['id']} | {item['category']} | {item['title']} | {item['path']}")

if __name__ == '__main__':
    main()
