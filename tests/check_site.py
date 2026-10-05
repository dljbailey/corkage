"""Static build/data/link regression checks. Run after scripts/build.py."""
from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlsplit, unquote
from collections import Counter
import json
ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'dist'
data=json.loads((OUT/'data.json').read_text())
assert len(data)==42
assert len({r['id'] for r in data})==42
assert Counter(r['scope'] for r in data)=={'public':35,'events':3,'members':1,'discretion':2,'clarify':1}
assert sum(bool(r['freeOffer']) for r in data)==8
assert all(r['checked']=='2026-09-13' for r in data)
assert not any(r['name'] in ['Bandol','The Camberwell Arms','Parsons'] for r in data)
assert all('philglas' not in json.dumps(r).lower() for r in data)
byname={r['name']:r for r in data}
assert '70cl' in byname['A. Wong']['policy']
assert '50% of average value' in byname['Fallow']['policy']
assert byname['Trivet']['scope']=='members' and not byname['Trivet']['freeOffer']
assert 'fee' in byname['Tayyabs']['fee'] and 'free' not in byname['Tayyabs']['fee'].lower()
for r in data:
    for url in [r['source'],r['website']]+[m['url'] for m in r['merchants']]:
        assert urlsplit(url).scheme=='https',url
    assert all(r[k] for k in ['id','name','neighbourhood','area','fee','policy','source','website'])
class Page(HTMLParser):
    def __init__(self):super().__init__();self.links=[];self.ids=[];self.headings=0;self.titles=0
    def handle_starttag(self,tag,attrs):
        a=dict(attrs)
        if tag=='h1':self.headings+=1
        if tag=='title':self.titles+=1
        if 'id' in a:self.ids.append(a['id'])
        for key in ['href','src']:
            if key in a:self.links.append(a[key])
pages={}
for f in OUT.rglob('*.html'):
    p=Page();p.feed(f.read_text());pages[f.resolve()]=p
    assert p.headings==1,(f,p.headings)
    assert p.titles==1,f
    assert len(p.ids)==len(set(p.ids)),f
    assert 'data.js' not in f.read_text(),f
    assert 'datePublished' not in f.read_text(),f
for f,p in pages.items():
    for link in p.links:
        url=urlsplit(link)
        if url.scheme or url.netloc:continue
        target=((OUT/unquote(url.path).lstrip('/')) if url.path.startswith('/') else (f.parent/unquote(url.path))).resolve() if url.path else f
        if target.is_dir(): target=target/'index.html'
        assert target.is_relative_to(OUT.resolve()),(f,link)
        assert target.exists(),(f,link)
        if url.fragment and target in pages:assert url.fragment in pages[target].ids,(f,link)
assert len(list((OUT/'journal').glob('*.html')))==4
assert len(list((OUT/'restaurants').glob('*.html')))==42
assert not (OUT/'research').exists()
assert not (OUT/'AGENTS.md').exists()
print(f'PASS: 42 policies, 35 public / 7 special, 8 public offers, {len(pages)} HTML pages, all internal files and anchors, no historical article dates or closed merchants.')
