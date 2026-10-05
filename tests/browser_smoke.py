"""Real browser checks using the installed agent-browser CLI. No form submissions."""
import subprocess,sys,json
from urllib.parse import urlsplit
BASE=(sys.argv[1] if len(sys.argv)>1 else 'http://127.0.0.1:8768').rstrip('/')
SESSION='corkage-seo-smoke'
def run(*args):
    p=subprocess.run(['agent-browser','--session',SESSION,'--json',*args],capture_output=True,text=True,timeout=45)
    if p.returncode:raise RuntimeError(p.stdout+p.stderr)
    try:
        result=json.loads(p.stdout)
        if result.get('success') is False:raise RuntimeError(str(result))
    except json.JSONDecodeError:pass
    if args[0]=='open' and urlsplit(args[1]).path in ('','/','/index.html'):
        run('wait','--fn','document.documentElement.dataset.directoryReady === "true"')
    if args==('press','Escape'):
        # Native dialog close is queued; wait for its close handler, not an arbitrary delay.
        run('wait','--fn','!document.querySelector("dialog")?.open && !new URL(location.href).searchParams.has("restaurant")')
    return p.stdout
count=0
def check(js,label):
    global count
    run('eval',f'(() => {{ if (!({js})) throw new Error({json.dumps(label)}); return "PASS"; }})()')
    count+=1;print('PASS',label)
run('open',BASE+'/')
run('wait','--fn','document.querySelector("#result-count").textContent.includes("35 restaurants")')
check('document.querySelectorAll(".restaurant-card:not([hidden])").length===35','35 default public listings')
check('document.querySelector(".restaurant-card:not([hidden]) h3").textContent==="A. Wong"','visual and DOM alphabetical order')
run('fill','#search','clapham')
check('document.querySelectorAll(".restaurant-card:not([hidden])").length===4','neighbourhood search')
run('fill','#search','zznotarestaurant')
check('!document.querySelector("#empty").hidden','empty state')
run('focus','#clear-search')
run('press','Enter')
run('wait','--fn','document.querySelectorAll(".restaurant-card:not([hidden])").length===35')
run('select','#area','West')
check('document.querySelectorAll(".restaurant-card:not([hidden])").length===5','West area filter')
run('click','button[type=reset]')
run('wait','--fn','document.querySelectorAll(".restaurant-card:not([hidden])").length===35')
run('check','#free')
check('document.querySelectorAll(".restaurant-card:not([hidden])").length===8','8 public free offers; excludes member benefit')
run('uncheck','#free')
run('select','#scope','all')
check('document.querySelectorAll(".restaurant-card:not([hidden])").length===42','all 42 visible')
for scope,expected in [('events',3),('members',1),('discretion',2),('clarify',1)]:
    run('select','#scope',scope)
    check(f'document.querySelectorAll(".restaurant-card:not([hidden])").length==={expected}',scope+' filter')
run('click','[data-restaurant="angler"]')
check('document.querySelector("dialog").open && document.querySelector("#detail-content").textContent.includes("contradiction")','Angler warning inside real dialog')
run('press','Escape')
check('!document.querySelector("dialog").open && document.activeElement.dataset.restaurant==="angler"','Escape closes and focus returns')
run('open',BASE+'/?restaurant=trinity')
run('wait','--fn','document.querySelector("dialog").open')
check('document.querySelector("#detail-content").textContent.includes("No corkage Upstairs")','deep link opens Trinity with restrictions')
run('press','Escape')
check('!new URL(location.href).searchParams.has("restaurant")','close removes detail URL')
run('set','viewport','390','844')
run('open',BASE+'/')
check('document.documentElement.scrollWidth<=innerWidth','mobile directory has no horizontal overflow')
run('click','[data-restaurant="a-wong"]')
check('document.querySelector("dialog").open && document.querySelector("#detail-content").textContent.includes("70cl")','mobile dialog retains literal bottle-size caveat')
run('press','Escape')
for path in ['journal.html','journal/sunday-table.html','journal/pair-the-sauce.html','journal/the-corkage-checklist.html','journal/a-better-bottle-a-better-evening.html','club.html','about.html','policies.html']:
    run('open',BASE+'/'+path)
    check('document.querySelector("h1")!==null && document.documentElement.scrollWidth<=innerWidth',path+' renders on mobile')
run('open',BASE+'/?restaurant=trinity')
run('focus','#detail-content a[href="restaurants/trinity.html"]')
run('press','Enter')
run('wait','--url','**/restaurants/trinity.html')
check('document.querySelector("h1").textContent.includes("Trinity") && document.body.textContent.includes("No corkage Upstairs")','dialog-to-full-guide navigation')
for slug,scope_text in [('trinity','Public dining'),('brawn','Private / group events'),('trivet','Members only'),('darbys','Ask management first'),('angler','Policy needs clarification'),('petersham-nurseries-restaurant','Ask management first')]:
    run('open',BASE+'/restaurants/'+slug+'.html')
    check(f'document.querySelector("main").textContent.includes({json.dumps(scope_text)}) && document.documentElement.scrollWidth<=innerWidth',slug+' page preserves scope on mobile')
    check(f'document.querySelector("link[rel=canonical]").href === "https://www.corkageclub.org/restaurants/{slug}.html"',slug+' canonical')
    check('JSON.parse(document.querySelector("script[type=\\"application/ld+json\\"]").textContent)["@graph"].some(x=>x["@type"]==="BreadcrumbList")','valid JSON-LD breadcrumbs')
run('screenshot','/tmp/corkage-seo-restaurant-mobile.png')
run('open',BASE+'/index.html?restaurant=trinity')
check('document.querySelector("dialog").open','legacy restaurant URL still opens its policy')
run('press','Escape')
run('open',BASE+'/?q=Clapham')
check('document.querySelector("link[rel=canonical]").href==="https://www.corkageclub.org/"','filtered directory canonical remains homepage')
run('open',BASE+'/club.html')
check('document.querySelector("#join a").href.includes("/viewform") && document.querySelector("#join a").target==="_blank"','waitlist opens actual Google form; no fake success')
run('open',BASE+'/')
run('screenshot','/tmp/corkage-mobile-smoke.png')
run('set','viewport','1440','1000')
run('screenshot','/tmp/corkage-desktop-smoke.png')
print(f'PASS: {count} real-browser assertions against {BASE}. No outbound forms submitted.')
run('close')
