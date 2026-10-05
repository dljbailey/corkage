# Corkage Club — Project Context

## Product

Corkage Club helps people find the best restaurants in London that allow diners to bring their own wine for a corkage fee.

The core experience is a trusted, easy-to-browse guide to London restaurants with corkage policies. It should help someone answer:

- Which good London restaurants accept corkage?
- How much is the corkage fee?
- Are there restrictions, such as particular days or bottle limits?
- Where is the restaurant and how can I book or contact it?

The site also introduces the Corkage Club: a community for wine enthusiasts interested in enjoying special bottles at excellent restaurants.

## Audience

- London diners who own or collect wine
- Wine enthusiasts looking for restaurants where they can bring a special bottle
- People planning memorable meals, from informal dinners to special occasions

## Product principles

1. **Trustworthy information** — corkage policies can change, so accuracy and freshness matter more than the size of the directory.
2. **Great restaurants first** — this is a curated guide to worthwhile dining experiences, not merely a complete list of venues offering corkage.
3. **Fast discovery** — users should be able to find relevant restaurants quickly by area and understand the fee and restrictions at a glance.
4. **Wine without pretension** — the experience should feel knowledgeable and discerning, but welcoming.
5. **Mobile-friendly** — restaurant discovery will often happen while users are making plans on their phones.

## Current implementation

This is a static HTML, CSS, and JavaScript website with a dependency-free Python build.

- `scripts/build.py` — page templates, undated editorial articles, sitemap and robots; generates `dist/`
- `scripts/restaurant_pages.py` — 42 static restaurant policy pages
- `scripts/seo.py` — canonical URLs and honest, source-consistent structured data
- `data.json` — canonical published policy records, scope, sources and editorial suggestions
- `script.js` — directory search, filters and accessible restaurant dialogs
- `styles.css` — shared styling
- `research/` — working research, not served by the website
- `tests/check_site.py` — build/data/internal-link regression checks
- `tests/check_seo.py` — canonical, sitemap, structured-data and crawlable-content checks
- `tests/check_live_seo.py` — public production HTTP/redirect verification
- `tests/browser_smoke.py` — real-browser checks via installed agent-browser CLI
- `vercel.json` — Vercel builds into `dist/`; only that directory is public

Build with `python3 scripts/build.py`. Serve `dist/`, never the repository root. `scripts/prepare-data.py` records the initial migration and is not part of normal builds; rerunning it overwrites data.json.

Canonical production is https://www.corkageclub.org. Maintain real HTML links to restaurant pages even when enhancing them with dialogs. Never invent ratings, publication dates or Search Console verification. Read README.md for the outstanding Search Console owner step. No analytics is installed.

Waitlist and suggestion links open the existing Google Forms. Do not claim a submission succeeded from this site, and do not submit test data to live forms. Public-dining records are shown by default; seven special-scope records remain explicitly separated. Editorial guides are undated, with no fabricated historical publication dates.

## Data expectations

Restaurant records should make the following clear wherever the information is available:

- Restaurant name
- Area
- Address and postcode
- Food or restaurant style
- Corkage fee
- Detailed corkage policy or restrictions
- Website and contact details
- When the corkage information was last verified
- Source or verification method

Never invent or infer a corkage policy. If information has not been verified, label it clearly.

## Voice and design direction

The product should feel curated, elegant, warm, and distinctly London. Copy should be concise and useful. Avoid generic luxury language, wine snobbery, and unnecessary complexity.

## Current scope

The confirmed scope is London. Do not expand to other cities or assume a particular membership, pricing, booking, or restaurant-partnership model without a product decision.
