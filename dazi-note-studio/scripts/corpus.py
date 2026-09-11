#!/usr/bin/env python3
"""Search the portable, original DuMate reference corpus. Standard library only."""
import argparse
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest='command', required=True)
    search = sub.add_parser('search')
    search.add_argument('terms', nargs='+', help='Separate scene/function/output terms with spaces')
    search.add_argument('--limit', type=int, default=10)
    show = sub.add_parser('show')
    show.add_argument('code', help='Note code such as A023, or page code A023P03')
    sub.add_parser('verify')
    args = parser.parse_args()
    notes = json.loads((ROOT / 'assets/corpus/manifest.json').read_text())
    if args.command == 'verify':
        pages = [p for n in notes for p in n['pages']]
        failures = []
        for p in pages:
            path = ROOT / p['path']
            if not path.is_file() or hashlib.sha256(path.read_bytes()).hexdigest() != p['sha256']:
                failures.append(p['code'])
        result = {'notes': len(notes), 'pages': len(pages), 'failed': failures}
        print(json.dumps(result, ensure_ascii=False))
        raise SystemExit(bool(failures) or len(notes) != 96 or len(pages) != 451)
    if args.command == 'show':
        found = False
        for n in notes:
            if n['code'] == args.code or any(p['code'] == args.code for p in n['pages']):
                found = True
                item = dict(n)
                item['pages'] = [dict(p, absolute_path=str(ROOT / p['path'])) for p in n['pages']
                                 if len(args.code) == 4 or p['code'] == args.code]
                print(json.dumps(item, ensure_ascii=False, indent=2))
        if not found:
            parser.error('Unknown note/page code')
        return
    results = []
    terms = [t.casefold() for t in args.terms]
    for n in notes:
        title, body = n['title'].casefold(), n['body'].casefold()
        hits = []
        for p in n['pages']:
            ocr = p.get('ocr', '').casefold()
            matched = [t for t in terms if t in ocr]
            if matched:
                at = min(ocr.find(t) for t in matched)
                hits.append({'code': p['code'], 'terms': matched, 'path': str(ROOT / p['path']),
                             'excerpt': p.get('ocr', '')[max(0, at-45):at+220]})
        score = sum(8*(t in title)+4*(t in body) for t in terms) + sum(len(p['terms']) for p in hits)
        if score:
            results.append({'code': n['code'], 'title': n['title'], 'score': score, 'pages': hits})
    results.sort(key=lambda r: (-r['score'], r['code']))
    print(json.dumps({'notice': 'Keyword matches are leads, not proof of task equivalence. Open originals.',
                      'matches': results[:args.limit]}, ensure_ascii=False, indent=2))

if __name__ == '__main__':
    main()
