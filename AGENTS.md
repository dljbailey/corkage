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

This is currently a static HTML, CSS, and JavaScript website with no build step.

- `index.html` — restaurant directory
- `club.html` — club membership proposition and waitlist
- `about.html` — philosophy and contact information
- `data.json` — restaurant records and corkage details
- `script.js` — restaurant rendering, filtering, details, and suggestions
- `waitlist.js` — waitlist form behaviour
- `styles.css` — site styling

Restaurant suggestions and waitlist registrations are currently submitted to Google Forms.

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
