"""Public production HTTP verification. Read-only; no Search Console submission."""
import concurrent.futures,json,html,re,urllib.request,urllib.error
from pathlib import Path
from xml.etree import ElementTree as ET
SITE='https://www.corkageclub.org'
def fetch(url):
    with urllib.request.urlopen(url,timeout=25) as r:
        return r.status,r.url,r.headers,r.read().decode()
status,url,headers,robots=fetch(SITE+'/robots.txt')
assert status==200 and f'Sitemap: {SITE}/sitemap.xml' in robots
status,url,headers,xml=fetch(SITE+'/sitemap.xml')
urls=[x.text for x in ET.fromstring(xml).findall('.//{http://www.sitemaps.org/schemas/sitemap/0.9}loc')]
assert len(urls)==len(set(urls))==50
assert all(u.startswith(SITE+'/') for u in urls)
data=json.loads((Path(__file__).resolve().parents[1]/'data.json').read_text())
policies={SITE+'/restaurants/'+r['id']+'.html':r for r in data}
def check(url):
    status,final,headers,text=fetch(url)
    assert status==200 and final==url,(url,status,final)
    assert 'text/html' in headers.get('Content-Type','')
    assert 'noindex' not in headers.get('X-Robots-Tag','').lower()
    assert f'<link rel="canonical" href="{url}">' in text,url
    assert '<meta name="robots" content="index,follow' in text,url
    schema=json.loads(re.search(r'<script type="application/ld\+json">(.*?)</script>',text,re.S)[1])
    assert schema['@context']=='https://schema.org'
    assert any(x.get('url')==url for x in schema['@graph'])
    if url in policies:
        assert policies[url]['policy'] in html.unescape(text),url
    return url
with concurrent.futures.ThreadPoolExecutor(max_workers=6) as pool:
    for url in pool.map(check,urls):print('PASS',url)
_,_,_,text=fetch(SITE+'/policies.html')
assert '<meta name="robots" content="noindex,follow">' in text
class NoRedirect(urllib.request.HTTPRedirectHandler):
    def redirect_request(self,*args,**kwargs):return None
opener=urllib.request.build_opener(NoRedirect)
for origin,path,expected in [
    ('https://corkageclub.org','/restaurants/trinity.html',SITE+'/restaurants/trinity.html'),
    ('https://corkage.vercel.app','/journal/sunday-table.html',SITE+'/journal/sunday-table.html'),
    (SITE,'/index.html?restaurant=trinity',SITE+'/?restaurant=trinity')]:
    try:opener.open(origin+path,timeout=20);raise AssertionError('Missing permanent redirect')
    except urllib.error.HTTPError as e:
        assert e.code in (301,308),(origin,path,e.code)
        target=urllib.parse.urljoin(origin+path,e.headers['Location'])
        assert target==expected,(target,expected)
        print('PASS permanent redirect',origin+path)
for path in ['/AGENTS.md','/scripts/seo.py','/research/2026-09-13/README.md','/restaurants/not-a-real-restaurant.html']:
    try:fetch(SITE+path);raise AssertionError('Unexpected public file or soft 404: '+path)
    except urllib.error.HTTPError as e:assert e.code==404,(path,e.code)
print('PASS: all 50 sitemap pages, 42 full policies, robots, canonical hosts, duplicate-page noindex, permanent redirects with query preservation, private-file and missing-page 404s. Google indexing is not implied.')
