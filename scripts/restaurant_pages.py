"""Standalone, crawlable policy guides using only the published source-backed dataset."""
from datetime import date
from html import escape
from seo import restaurant_path

def render(record, records, labels):
    r=record
    e=lambda value: escape(str(value),quote=True)
    checked=date.fromisoformat(r['checked']).strftime('%d %B %Y').lstrip('0')
    special=r['scope']!='public'
    title=f'{r["name"]} corkage in {r["neighbourhood"]}'
    if special:
        title=f'{r["name"]} corkage: {labels[r["scope"]].lower()}'
    description=f'{r["name"]}, {r["neighbourhood"]}: {r["fee"]}. {labels[r["scope"]]}. Read the conditions and official source before booking.'
    other=[x for x in records if x['id']!=r['id'] and x['area']==r['area'] and x['scope']=='public'][:3]
    pairs='<ul>'+''.join(f'<li>{e(p)}</li>' for p in r['pairings'])+'</ul>' if r['pairings'] else '<p>We have not verified enough of the current menu to recommend a wine style. Ask the restaurant before choosing your bottle.</p>'
    shops=''.join(f'<li><a href="{e(m["url"])}" target="_blank" rel="noopener noreferrer">{e(m["name"])} ↗</a><br>{e(m["address"])}</li>' for m in r['merchants'])
    related=''.join(f'<li><a href="/{restaurant_path(x)}">{e(x["name"])} corkage</a> · {e(x["neighbourhood"])}</li>' for x in other)
    body=f'''<main id="main"><article class="article restaurant-guide"><header><p class="eyebrow">{e(r['neighbourhood'])} · London</p><h1>{e(r['name'])}<br><em>Corkage guide.</em></h1><p class="article-deck">{e(r['cuisine'])}</p><span class="status {'special' if special else ''}">{e(labels[r['scope']])}</span></header><div class="prose"><section class="policy-summary"><h2>{e(r['fee'])}</h2><p>{e(r['policy'])}</p><p class="small-note">Official website source checked <time datetime="{e(r['checked'])}">{checked}</time>. This is not a personal confirmation from the restaurant.</p></section><p class="policy-warning">{'This is a special arrangement, not general permission to bring wine. ' if special else ''}Policies and promotions can change. Agree the full corkage charge and conditions with the restaurant before your visit.</p><div class="detail-source"><a class="button" href="{e(r['website'])}" target="_blank" rel="noopener noreferrer">Restaurant website ↗</a><a class="text-link" href="{e(r['source'])}" target="_blank" rel="noopener noreferrer">Official policy source ↗</a></div><p class="small-note">The source may open a PDF. We are an independent guide, not the restaurant or its booking agent.</p><h2>Before you book</h2><p>Tell the restaurant the wine’s name, vintage, bottle size and quantity. Ask whether the charge includes service, whether your wine is already on the list, and whether the policy applies to your chosen room and service. An unspecified fee or limit is unknown, not free or unlimited.</p><h2>A bottle to consider</h2>{pairs}<p class="small-note">Editorial wine-style suggestions, conditional on the food you choose. Not restaurant advice, guaranteed dishes or merchant stock.</p><h2>Wine shops to plan around</h2><p>These are wider-area options, not a nearest-shop ranking. Some require a separate journey. Confirm the branch’s current hours, stock and collection arrangements.</p><ul class="merchant-list">{shops}</ul><h2>More {e(r['area'].lower())} London corkage guides</h2><ul>{related}</ul><p><a href="/">Browse all London corkage restaurants →</a></p><p><a href="/journal/the-corkage-checklist.html">Read the five-minute corkage checklist →</a></p><p class="small-note">Something changed? <a href="/about.html#how-we-check">Read how we check policies and send a correction.</a></p></div></article></main>'''
    restaurant={'@type':'Restaurant','name':r['name'],'url':r['website'],
                'description':f'{r["name"]} in {r["neighbourhood"]}, London. {labels[r["scope"]]} corkage evidence; see the guide for restrictions.'}
    if not r['cuisine'].startswith('Menu to check'):
        restaurant['servesCuisine']=r['cuisine']
    # Not Offer/Product/Review markup: a corkage fee is not a restaurant price range,
    # and this independent guide is not the restaurant's own business website.
    return title,description,body,{'about':restaurant,'citation':r['source']}
