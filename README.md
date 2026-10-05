# London Corkage Club

A source-linked London restaurant corkage guide. Warm cream and burgundy styling, searchable directory, scoped policy details and a small undated editorial journal.

## Local preview

Requires Python 3. No application packages or framework are needed.

```sh
python3 scripts/build.py
python3 -m http.server 8768 --bind 127.0.0.1 --directory dist
```

Open http://127.0.0.1:8768. Serve **dist/**, not the repository root. Research notes, tests and internal context are not published.

## Content

- Edit `data.json` for restaurant policies. It contains 42 records: 35 public-dining leads plus 3 event/group, 1 member, 2 discretionary and 1 conflicting-policy record.
- Keep exact restrictions, source links and website access dates. Never infer free corkage from BYO permission or extend a private-event rate to ordinary dining.
- Edit `scripts/build.py` for templates and journal copy. Articles deliberately have no invented publication dates or first-person dining claims.
- Pairings are conditional editorial suggestions. Merchant links are limited wider-area options, not three verified nearest shops or stock guarantees. Do not reintroduce closed Philglas & Swiggot branches.
- The old 19-record directory is available in Git history. Its unverified rates are not carried forward. The research collection is broader than the published directory.
- `scripts/prepare-data.py` is the explicit initial migration, not part of the build. It overwrites `data.json`; do not run it casually after content edits.

## Verification

```sh
python3 scripts/build.py
python3 tests/check_site.py
python3 tests/check_seo.py
node --check script.js
# With a local preview server already running and agent-browser installed:
python3 tests/browser_smoke.py http://127.0.0.1:8768
```

Browser checks cover search, area and arrangement filters, free offers, empty state, keyboard dismissal/focus restoration, deep links, mobile overflow, all four articles and the Google Forms link. No test submits live forms. Source policies remain subject to restaurant confirmation; a passing UI test does not verify current offers.

## Search foundations

- `scripts/restaurant_pages.py` generates 42 static `/restaurants/<id>.html` policy guides. The complete policy, scope, date, source and links are in HTML without JavaScript.
- Restaurant cards are real links, progressively enhanced into quick-view dialogs; modifier-click and no-JavaScript navigation still work. Existing `?restaurant=` bookmarks remain supported.
- `scripts/seo.py` generates unique canonicals and JSON-LD: WebSite, Organization, WebPage/CollectionPage, Article, BreadcrumbList and Restaurant entities described by the guides. No fake ratings, invented publication dates, restaurant ownership claims or corkage-as-meal-price markup.
- `/sitemap.xml` includes the 50 indexable URLs. `/robots.txt` advertises it. Source-check dates are not misused as sitemap lastmod dates.
- `/policies.html` remains accessible but uses `noindex,follow` to avoid indexing the duplicate aggregate. Filter query URLs canonicalise to the homepage; `/index.html` redirects to `/`.
- `python3 tests/check_live_seo.py` checks every production sitemap URL, canonical, static policy, robots, redirects and 404 boundaries. It does not prove Google has indexed the pages.

### Search Console: owner step still required

No Search Console property has been verified or sitemap submitted by this change. The installed Google connector could not access the Search Console API. In https://search.google.com/search-console, select an existing `corkageclub.org` property or verify ownership of `https://www.corkageclub.org/`. Then submit `https://www.corkageclub.org/sitemap.xml` and inspect the homepage plus a restaurant URL such as `/restaurants/trinity.html`. If HTML-tag verification is chosen, supply Google's actual verification tag for a follow-up deploy; never insert a dummy tag. A sitemap and valid schema support discovery but do not guarantee indexing, rankings or rich results. No analytics has been added.

## Deploy

Vercel project: `dljb-projects/corkage`. Canonical production: https://www.corkageclub.org. The apex domain and corkage.vercel.app permanently redirect to this host, preserving paths and queries.

`vercel.json` defines the Python build and `dist` output. Use a focused branch and PR. Run a preview deployment and verify before merging/promoting to production. Deployments and production promotion require owner approval.

Waitlist and restaurant suggestions use the existing external Google Forms. The site makes no claim of submission success and does not store visitor details itself. Google Fonts are loaded externally.
