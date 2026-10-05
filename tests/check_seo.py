"""Verify SEO output against built HTML, not just generator intentions."""
from pathlib import Path
from html.parser import HTMLParser
from xml.etree import ElementTree as ET
from urllib.parse import urlsplit
import json,sys
ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'dist'
SITE='https://www.corkageclub.org'
class Page(HTMLParser):
    def __init__(self):
        super().__init__();self.canonicals=[];self.meta={};self.schema=[];self.text=[];self.links=[];self.ld=False;self.buffer='';self.title=False;self.title_text=''
    def handle_starttag(self,tag,attrs):
        a=dict(attrs)
        if tag=='link' and a.get('rel')=='canonical':self.canonicals.append(a['href'])
        if tag=='meta':self.meta[a.get('name',a.get('property'))]=a.get('content')
        if tag=='script' and a.get('type')=='application/ld+json':self.ld=True;self.buffer=''
        if tag=='title':self.title=True
        if tag=='a':self.links.append(a.get('href',''))
    def handle_data(self,data):
        if self.ld:self.buffer+=data
        else:self.text.append(data)
        if self.title:self.title_text+=data
    def handle_endtag(self,tag):
        if tag=='script' and self.ld:self.schema.append(json.loads(self.buffer));self.ld=False
        if tag=='title':self.title=False

def parse(f):
    page=Page();page.feed(f.read_text());return page
pages={f.relative_to(OUT).as_posix():parse(f) for f in OUT.rglob('*.html')}
assert len(pages)==51
assert len({p.title_text for p in pages.values()})==51
assert len({p.meta['description'] for p in pages.values()})==51
indexable=set()
for path,p in pages.items():
    url=SITE+('/' if path=='index.html' else '/'+path)
    assert p.canonicals==[url],(path,p.canonicals)
    assert p.meta['og:url']==url
    assert p.schema and len(p.schema)==1,path
    graph=p.schema[0]['@graph']
    assert p.schema[0]['@context']=='https://schema.org'
    assert any(x['@type']=='WebSite' for x in graph)
    page=next(x for x in graph if x.get('@id')==url+'#page')
    assert page['description']==p.meta['description']
    assert page['url']==url
    raw=json.dumps(graph)
    for forbidden in ['aggregateRating','reviewRating','datePublished','dateModified','"offers"','"priceRange"']:
        assert forbidden not in raw,(path,forbidden)
    if path!='index.html':
        crumb=next(x for x in graph if x['@type']=='BreadcrumbList')
        assert [x['position'] for x in crumb['itemListElement']]==list(range(1,len(crumb['itemListElement'])+1))
        assert crumb['itemListElement'][-1]['item']==url
    if path=='policies.html':assert p.meta['robots']=='noindex,follow'
    else:
        assert 'noindex' not in p.meta['robots'];indexable.add(url)
    if path.startswith('journal/'):
        article=next(x for x in graph if x['@type']=='Article')
        assert page['@type']=='WebPage' and article['author']['@id']==SITE+'/#organization'
        assert article['mainEntityOfPage']['@id']==page['@id']
        assert page['mainEntity']['@id']==article['@id']
    assert 'googletagmanager' not in ''.join(p.text).lower()
assert len(indexable)==50
sitemap=ET.parse(OUT/'sitemap.xml')
urls=[x.text for x in sitemap.findall('.//{http://www.sitemaps.org/schemas/sitemap/0.9}loc')]
assert len(urls)==len(set(urls))==50
assert set(urls)==indexable
assert not sitemap.findall('.//{http://www.sitemaps.org/schemas/sitemap/0.9}lastmod')
assert (OUT/'robots.txt').read_text()==f'User-agent: *\nAllow: /\n\nSitemap: {SITE}/sitemap.xml\n'
data=json.loads((OUT/'data.json').read_text())
for r in data:
    path=f'restaurants/{r["id"]}.html';p=pages[path];text=' '.join(p.text)
    assert r['policy'] in text,(r['name'],'full policy not in static HTML')
    assert r['fee'] in text
    assert r['source'] in p.links and r['website'] in p.links
    assert r['checked'] in (OUT/path).read_text()
    if r['scope']!='public':assert 'not general permission' in text
    page=next(x for x in p.schema[0]['@graph'] if x.get('@id')==SITE+'/'+path+'#page')
    assert page['about']['@type']=='Restaurant' and page['about']['name']==r['name']
    assert page['citation']==r['source']
    assert path in pages['index.html'].links
    assert path in pages['policies.html'].links
assert '../restaurants/trinity.html' in pages['journal/sunday-table.html'].links
redirects=json.loads((ROOT/'vercel.json').read_text())['redirects']
for host in ['corkageclub.org','corkage.vercel.app']:
    assert any(x.get('has')==[{'type':'host','value':host}] and x['destination']==SITE+'/:path*' and x['permanent'] for x in redirects)
assert any(x['source']=='/index.html' and x['destination']=='/' and x['permanent'] for x in redirects)
print('PASS: 51 unique canonical/title/description sets; 50 sitemap URLs; 42 static, internally linked restaurant guides; JSON-LD/breadcrumbs; explicit policy scope; no fake dates/ratings; production-domain redirects.')
