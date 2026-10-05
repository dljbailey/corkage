"""Search metadata for the public static site. No analytics or invented ratings/dates."""
import json
from html import escape
from urllib.parse import quote

SITE = 'https://www.corkageclub.org'
NAME = 'London Corkage Club'

def canonical(path):
    return SITE + ('/' if path == 'index.html' else '/' + quote(path, safe='/-._'))

def restaurant_path(record):
    return f'restaurants/{record["id"]}.html'

def metadata(title, description, path, page_type='WebPage', extra=None, noindex=False):
    url = canonical(path)
    organisation = {'@type': 'Organization', '@id': SITE+'/#organization', 'name': NAME, 'url': SITE+'/'}
    website = {'@type': 'WebSite', '@id': SITE+'/#website', 'name': NAME, 'url': SITE+'/', 'publisher': {'@id': organisation['@id']}, 'inLanguage': 'en-GB'}
    page = {'@type': 'WebPage' if page_type == 'Article' else page_type, '@id': url+'#page', 'url': url, 'name': title,
            'description': description, 'isPartOf': {'@id': website['@id']},
            'publisher': {'@id': organisation['@id']}, 'inLanguage': 'en-GB'}
    crumbs = [{'@type': 'ListItem', 'position': 1, 'name': 'Restaurants', 'item': SITE+'/'}]
    if path.startswith('journal/'):
        crumbs.append({'@type': 'ListItem', 'position': 2, 'name': 'Journal', 'item': canonical('journal.html')})
    if path != 'index.html':
        crumbs.append({'@type': 'ListItem', 'position': len(crumbs)+1, 'name': title, 'item': url})
    graph = [organisation, website, page]
    if page_type == 'Article':
        article = {'@type': 'Article', '@id': url+'#article', 'url': url,
                   'headline': title, 'description': description, 'inLanguage': 'en-GB',
                   'author': {'@id': organisation['@id']}, 'publisher': {'@id': organisation['@id']},
                   'mainEntityOfPage': {'@id': page['@id']}}
        graph.append(article)
        page['mainEntity'] = {'@id': article['@id']}
    if len(crumbs) > 1:
        breadcrumb = {'@type': 'BreadcrumbList', '@id': url+'#breadcrumb', 'itemListElement': crumbs}
        graph.append(breadcrumb)
        page['breadcrumb'] = {'@id': breadcrumb['@id']}
    if extra:
        page.update(extra)
    # Escape '<' so editorial strings can never close a script element.
    structured = json.dumps({'@context': 'https://schema.org', '@graph': graph}, ensure_ascii=False).replace('<', '\\u003c')
    robots = 'noindex,follow' if noindex else 'index,follow,max-image-preview:large'
    return f'<link rel="canonical" href="{escape(url, quote=True)}"><meta name="robots" content="{robots}"><meta property="og:url" content="{escape(url, quote=True)}"><meta property="og:site_name" content="{NAME}"><meta property="og:locale" content="en_GB"><script type="application/ld+json">{structured}</script>'

def item_list(items):
    return {'@type': 'ItemList', 'numberOfItems': len(items), 'itemListElement': [
        {'@type': 'ListItem', 'position': i+1, 'url': canonical(path), 'name': name}
        for i, (name, path) in enumerate(items)]}
