# Research: Corkage Club — North, East, South and City lane

## Summary
50 distinct restaurant candidates are preserved below. **16 have fetched official evidence of some corkage provision**, but this includes one private-hire-only policy, one paid-membership benefit and one entirely discretionary policy: these are not 16 unrestricted public BYO restaurants. Several historical directory prices are wrong; substantial contact, menu and address gaps remain, so this is a research ledger, not publication-ready directory data.

**Checked/accessed: 2026-09-13, Europe/London**, confirmed by supervisor from host clock. This is an access date, not the date a restaurant personally reconfirmed its policy. No restaurant was contacted. Historical input: `/Users/danielbailey/Documents/Code/corkage/data.json`, read only. Existing IDs appear where applicable; `new` means no existing record in that file.

### Reading the evidence
- `official-confirmed`: fetched official text establishes the specified provision, strictly within the scope described. Does not guarantee availability at a future reservation.
- `official-no`: explicit official refusal for ordinary non-member customers.
- `third-party-only`: fetched outside reporting, not current restaurant confirmation.
- `not-published`: no usable current general policy in the successfully checked pages, not a claim about every page of the website and never permission.
- `inaccessible`: the relevant site/page could not be read adequately. Never interpreted as policy absence.
- **S** = search-result lead only, explicitly not fetched-page proof. **H** = historical repo field, still unverified. An exact quote about cuisine/contact does not establish corkage.
- Pages checked are listed in each record. Some readable extraction omitted important footer/accordion content; for Luca, Darby's and several others, raw official HTML was fetched and checked separately. HTML entities are decoded in quotations.
- Pairings are **editorial wine-style suggestions**, not restaurant advice or assertions about current bottles/stock. Where only a broad cuisine is evidenced, the food reasoning is conditional. Where cuisine evidence was insufficient, pairings are deliberately withheld instead of invented.
- Merchant links resolve to the reusable directory. Ordered selections balance quality and neighbourhood relationship; not an exhaustive top-three claim. No distances or walking times were calculated. Wider travel is explicitly flagged.

## Counts and priority
| Status | Count | Record numbers |
|---|---:|---|
| official-confirmed | 16 | 1–8, 14, 15, 25, 34, 36, 45, 48, 50 |
| official-no | 1 | 24 |
| third-party-only | 2 | 9, 30 |
| not-published | 23 | 13, 16–18, 21, 23, 26–29, 32–33, 35, 37–44, 46–47 |
| inaccessible | 8 | 10–12, 19–20, 22, 31, 49 |
| closed | 0 | None of the final 50 classified closed |
| **Total** | **50** | **1–50, one Hawksmoor branch only** |

**First editorial shortlist:** Noble Rot Lamb's Conduit, Chez Bruce, Trinity, Luca, Cabotte, Hawksmoor Borough, The Clove Club, Da Terra, Sune, Restaurant Story and The French Table. This prioritises established food/wine credentials and usable official policy evidence, not Michelin status alone. Tayyabs remains a deliberate informal destination exception rather than an upscale room. Brawn and Trivet need their restricted scope displayed prominently. Planque is useful negative evidence, not a public BYO recommendation.

## Numbered restaurant ledger

### 1. Hawksmoor Borough
- **Repo ID:** `hawksmoor`, resolved from group entry to **Borough** only. Borough/London Bridge; **16 Winchester Walk, SE1 9AQ**. [Official branch](https://thehawksmoor.com/locations/borough/).
- **Status: official-confirmed.** £5 per bottle all day Monday; £25 per cork Tuesday–Sunday, any wine/style/bottle size. Group page: **“At all of our restaurants corkage all day on Mondays is only £5”** and **“Our corkage fee, Tuesday to Sunday, here at Hawksmoor is £25.”** [Policy](https://thehawksmoor.com/wine-club/). Borough explicitly repeats “every monday, all day – £5 corkage.”
- **Scope:** group statement covers its other restaurants; do not create additional counts. Other London branch applicability is group-level evidence, not separate branch checks. The historical multiple-location address should be replaced by Borough's named address if publishing this record.
- **Cuisine evidence:** branch calls itself a “steak and seafood” restaurant. **Editorial:** mature Cabernet-led Bordeaux for beef; Northern Rhône Syrah for char; saline Chardonnay for seafood.
- **Retailers:** [M10 Bedales](#m10) first, in Borough Market; [M9 Amathus City](#m9), across the river for broader fine-wine sourcing; [M11 Shrine Lamb's Conduit](#m11), a wider central-London purchase, not nearby. A third fetched-and-verified immediate-neighbourhood shop was not established.
- **Checked:** branch and group wine-club pages, 2026-09-13. Contact email not needed to establish policy; not researched separately.

### 2. Tayyabs
- **Repo ID:** `tayyabs`. Whitechapel; **83–89 Fieldgate Street, E1 1JU (H)**. [Official](https://www.tayyabs.co.uk/).
- **Status: official-confirmed, BYO permission only.** **“Bring your own bottle and enjoy!”** Fee and bottle limits are **not stated in fetched text**; historical “free every day” is not reconfirmed. Do not publish £0 from that sentence.
- **Cuisine evidence:** **“Purveyors of fine traditional punjabi cuisine since 1972”**; official page also references lamb chops. **Editorial:** off-dry Riesling for chilli/spice; low-tannin chilled Gamay for grilled lamb without excessive astringency; dry sparkling rosé for mixed rich/spiced plates.
- **Retailers:** [M9 Amathus City](#m9), western City approach; [M8 Passione Vino Shoreditch](#m8), northern approach and Italian expertise; [M6 Shrine Broadway Market](#m6), wider East London sourcing. None is asserted to be a Whitechapel doorstep shop.
- **Checked:** homepage, 2026-09-13. **Gap:** current fee, restrictions and official address extraction. Public general email unknown; no separate fee-specific contact lookup completed.

### 3. Cabotte
- **Repo ID:** `cabotte`. City/Bank; **48 Gresham Street, EC2V 7AY**. [Official/contact](http://www.cabotte.co.uk/contact-reservations).
- **Status: official-confirmed, Friday promotion.** **“Every Friday ... you and a guest can enjoy your first bottle corkage-free. Want to open a second bottle? It’s just £30 corkage”**. [Official post, 2025-05-30](https://www.cabotte.co.uk/blog/2025/5/30/enjoy-byo-fridays-in-the-heart-of-the-city).
- **Restrictions/gaps:** text describes you and a guest; larger parties, bottle sizes, lunch applicability, third bottles and other days not established. The post's later “Friday night” wording warrants checking lunch before recommending it. **Historical repo “free Mondays; £25/£50/£75” is contradicted/not reconfirmed.**
- **Cuisine:** official post says “exceptional French cuisine.” **Editorial:** white Burgundy for fish or creamy sauces; mature Pinot Noir for poultry/game preparations; mature Bordeaux for richer meat dishes, depending on that day's menu.
- **Public email:** `info@cabotte.co.uk`, contact page (search-visible; fetched contact page checked). **Retailers:** [M9](#m9) within City; [M8](#m8) Shoreditch alternative; [M10](#m10) Borough across the river. Wider options, not three adjoining shops.
- **Checked:** dated post and contact/reservations page, 2026-09-13. Ask about currency of this 2025 promotion before publication.

### 4. The Clove Club
- **Repo ID:** `cloveclub`. Shoreditch; **Shoreditch Town Hall, 380 Old Street, EC1V 9LT (H)**. [Official FAQ](https://www.thecloveclub.com/faq).
- **Status: official-confirmed.** **“one bottle of wine per two guests for a charge of £75 corkage per bottle, exclusive of service charge.”** Bottle format not specified. Do not omit the service-charge caveat.
- **Cuisine:** same FAQ: **“a seasonal tasting menu”** with produce from the British Isles. **Editorial:** complex traditional-method sparkling wine for varied starters; restrained Chardonnay for seafood/white-meat courses; fine-boned Pinot Noir for richer courses, selected after seeing the menu.
- **Public email:** `hello@thecloveclub.com` for sommelier advice; `reservations@thecloveclub.com` for reservations, both fetched FAQ.
- **Retailers:** [M8](#m8), same Shoreditch area; [M6](#m6), Broadway Market wider East London; [M9](#m9), City approach.
- **Checked:** FAQ readable and raw, 2026-09-13. **Gap:** address still historical in this ledger.

### 5. Luca
- **Repo ID:** `luca`. Clerkenwell; **88 St John Street, EC1M 4EH**. [Official](https://luca.restaurant/).
- **Status: official-confirmed.** Raw official footer states **“Our corkage policy is £50 per bottle, for a maximum of two bottles.”** No day limitation, format or service treatment stated there. Reader extraction alone missed the policy; the raw HTML is the proof.
- **Public email:** **`reservations@luca.restaurant`**, same fetched raw footer.
- **Cuisine evidence:** [private dining](https://luca.restaurant/private-dining) describes **“Michelin Star Italian cooking”**. **Editorial:** structured Verdicchio for Italian seafood/vegetable preparations; Sangiovese for tomato or meat-led preparations; mature Nebbiolo for richer meat courses if on the menu.
- **Retailers:** [M8b Passione Exmouth Market](#m8b), Clerkenwell Italian specialist; [M11](#m11), Bloomsbury fine-wine option; [M9](#m9), wider City alternative.
- **Checked:** homepage readable + raw; `/private-dining`; `/contact` failed 404, 2026-09-13. Historical fee reconfirmed through current fetched official HTML.

### 6. Trinity — downstairs restaurant
- **Repo ID:** `trinity`. Clapham Old Town; **4 The Polygon, SW4 0JG (H)**. [Official](https://trinityrestaurant.co.uk/).
- **Status: official-confirmed.** [2026 corkage PDF](https://trinityrestaurant.co.uk/wp-content/uploads/2026/01/Corkage-Policy-for-2026.pdf.pdf), downloaded and read: **“£20 Half Bottle 375ml £40 Still Wine 750ml £70 Still Wine Magnum 1500ml £50 Champagne 750ml £90 Champagne Magnum 1500ml”**; **“all corkage fees are waived on Sunday evenings.”**
- **Restrictions:** **one bottle per two guests**; no wines already on their list; inform restaurant when confirming; service charge added. **“We do not allow corkage Upstairs at Trinity.”** Do not extend downstairs policy upstairs. Historical £35 wine/£40 sparkling is superseded; “Champagne” should not silently become all sparkling categories.
- **Cuisine:** [menus](https://trinityrestaurant.co.uk/menus/) checked, but extraction mostly navigation: modern seasonal cuisine remains **H**, not a fresh full menu read. **Editorial provisional:** restrained Chardonnay for delicate fish/poultry; Pinot Noir for richer seasonal mains. These require menu confirmation.
- **Retailers:** [M12 D Vine Clapham](#m12), Clapham North; [M13 Bottle Apostle Abbeville](#m13), Clapham; [M14 Dulwich Vintners](#m14), a wider South London trip, not nearby.
- **Checked:** 2026 PDF and menus, 2026-09-13. Public email `Beverage@trinityrestaurant.co.uk` is published specifically for cellar sales, not represented as general booking contact. General contact page search yielded `dine@trinityrestaurant.co.uk`, S only.

### 7. Chez Bruce
- **Repo ID:** `chezbruce`. Wandsworth Common; **2 Bellevue Road, SW17 7EG (H; official contact S agrees)**. [Official wine](https://www.chezbruce.co.uk/wine/).
- **Status: official-confirmed.** **“one 75cl bottle per guest, with a four-bottle limit per table”**; **“£50 for dinner, and £25 for lunchtime services per 75cl bottle excluding the optional 12.5% service charge.”** Notify when booking if possible. No fetched Sunday-free provision. Historical £40 and magnum wording must not be retained.
- **Cuisine:** [food page](https://www.chezbruce.co.uk/food/): **“classical and regional French/ Mediterranean cuisine”**, including charcuterie and slow-cooked braises. **Editorial:** mature Bordeaux for braises; textured Chardonnay for French sauces; fresh Loire Cabernet Franc for charcuterie.
- **Retailers:** [M13](#m13) Abbeville and [M12](#m12) Clapham North are wider Clapham options; [M14](#m14) is a substantially wider Dulwich journey. No three genuinely adjacent verified shops found; Wine Tasting Shop Balham remains an unverified retrieval lead below.
- **Checked:** wine and food pages; contact page extraction failed, 2026-09-13. General email unknown; policy itself is fetched.

### 8. Noble Rot Lamb's Conduit
- **Repo ID:** new. Bloomsbury boundary exception; **51 Lamb's Conduit Street, WC1N 3NB**. [Official branch](https://noblerot.co.uk/restaurant/lambs-conduit).
- **Status: official-confirmed.** [Group FAQ](https://noblerot.co.uk/faq): **“Corkage is £35 per 750ml. Just let us know in advance.”** No fetched magnum rate or bottle cap. Same group FAQ covers Soho/Mayfair, which are not counted in this lane; tell other lane £25 is stale.
- **Public email:** `lambsconduit@noblerot.co.uk`, fetched branch and FAQ.
- **Cuisine:** [official food PDF](https://noblerot.co.uk/media/menus/nobleRot_LambsConduit_food.pdf), restaurant menu dated **2026-09-12**: French/European, e.g. “Braised Cornish Monkfish, Vin Jaune & Alsace Bacon” and roast game. **Editorial:** oxidative Jura white for the vin-jaune sauce; mature Pinot Noir for game; traditional-method sparkling for oysters/Comté starters. These are suggestions based on that dated menu, not guaranteed future dishes.
- **Retailers:** [M11](#m11), opposite-side same street and strongest fit; [M8b](#m8b), Exmouth Market; [M2](#m2), a wider Islington journey. No assertion that all three are nearby.
- **Checked:** branch, FAQ and four-page food PDF, 2026-09-13.

### 9. Trullo
- **Repo ID:** new. Highbury/Islington; **300–302 St Paul's Road, N1 2LH**. [Official](https://www.trullorestaurant.com/); [contact](https://www.trullorestaurant.com/contact/).
- **Status: third-party-only.** [Jamie Goode, 2021-10-01](https://wineanorak.com/2021/10/01/restaurants-trullo-islington-london/) fetched: **“corkage is £20”**. This is five-year-old lunch reporting, not a current price. No official general policy found in home/contact plus focused search.
- **Public email:** contact page publishes an obfuscated address; raw page's public Cloudflare encoding decodes to `enquiries@trullorestaurant.com` (not an inferred naming convention).
- **Cuisine:** official **“simple, seasonally focused, Italian inspired menu”**, fresh pasta and charcoal grill. **Editorial:** Sangiovese for ragù; dry Vermentino for grilled fish; Nebbiolo for meat-led dishes.
- **Retailers:** [M2](#m2), Upper Street/Highbury end; [M4 Yield N1](#m4), same St Paul's Road; [M1](#m1), wider Highbury Park. All strong specialist options in the north-Islington cluster.
- **Checked:** home/contact readable and raw, dated review raw, 2026-09-13. Current fee/limits require confirmation.

### 10. Westerns Laundry
- **Repo ID:** new. Highbury; **34 Drayton Park, N5 1PB**, fetched [contact](https://www.westernslaundry.com/map-contacts). [Official](https://www.westernslaundry.com/).
- **Status: inaccessible.** Homepage extraction incomplete; contact page readable, no policy there. Fee/restrictions unknown. This is not evidence BYO is unavailable.
- **Public email:** **`office@westernslaundry.com`**, fetched contact; bookings directed to phone/reservations link, not careers emails.
- **Cuisine:** seafood/European is a candidate lead; [OpenTable](https://www.opentable.com/r/westerns-laundry-london) search labels Modern European, but full retrieval aborted. Fetched official quote only **“daily changing menu”**. **Pairings withheld:** insufficient fetched food detail for useful food-specific suggestions.
- **Retailers:** [M1](#m1), Highbury Park; [M2](#m2), Highbury end of Upper Street; [M4](#m4), St Paul's Road.
- **Checked:** homepage failure, contact success, focused policy/contact search, OpenTable failed, 2026-09-13. Gap: menu, policy and fee.

### 11. Primeur
- **Repo ID:** new. Canonbury/Newington Green; **Barnes Motors, 116 Petherton Road, N5 2RT (S, OpenTable)**. [Official](https://www.primeurn5.co.uk/).
- **Status: inaccessible.** Home extraction incomplete. [Private-dining FAQ](https://www.primeurn5.co.uk/private-dining-terms-faqs) fetched; no corkage clause. Fee/restrictions unknown.
- **Public email:** **`PRIVATEDINING@PRIMEURN5.CO.UK`**, explicitly private-dining enquiries; ordinary reservations email unknown.
- **Cuisine:** sustainable seasonal cooking lead from [OpenTable](https://www.opentable.com/primeur), full retrieval aborted. Official FAQ only logistics, not menu proof. **Pairings withheld** pending usable cuisine/menu source.
- **Retailers:** [M3](#m3) Newington Green, [M4](#m4) St Paul's Road, [M1](#m1) Highbury Park; credible adjoining-area options.
- **Checked:** home failure, private-dining FAQ, focused search, OpenTable failure, 2026-09-13. Address not yet fetched-proof verified.

### 12. Perilla
- **Repo ID:** new. Newington Green; **1–3 Green Lanes, N16 9BS (S, OpenTable)**. [Official](https://www.perilladining.co.uk/).
- **Status: inaccessible.** Homepage JS-rendered; [contact](https://www.perilladining.co.uk/contact) fetched successfully. No fee/policy established.
- **Public email:** **`info@perilladining.co.uk`**, official heading **“INFO/BOOKINGS”**.
- **Cuisine:** Modern European is [OpenTable search evidence](https://www.opentable.co.uk/r/perilla-london), not fetched proof; page retrieval aborted. **Pairings withheld** until actual menu/cuisine source is accessible.
- **Retailers:** [M3](#m3), on the green; [M4](#m4), adjoining St Paul's Road; [M5 Shrine Stoke Newington](#m5), wider Stoke Newington trip.
- **Checked:** home, contact, focused search, failed OpenTable, 2026-09-13. Gap: food evidence, official address and policy.

### 13. BRAT Redchurch Street
- **Repo ID:** new. Shoreditch; **first floor, 4 Redchurch Street, E1 6JL**. [Official](https://bratrestaurant.co.uk/redchurch-st/).
- **Status: not-published in checked page.** Raw page recovered address and email omitted by readable extraction. No current policy established after focused search. Fee/limits unknown. Climpson's Arch not counted and not assumed to share any unpublished arrangement.
- **Public email:** **`bookings@bratrestaurant.com`**, fetched raw contact section.
- **Cuisine:** official HTML keywords include **“charcoal grill”**, **“seafood”**, **“basque”**; images identify turbot/hake. This supports a broad seafood/grill direction, not a current dish claim. **Editorial:** textured white Rioja for grilled fish; saline Albariño for seafood; restrained Garnacha for richer grilled preparations.
- **Retailers:** [M8](#m8) Shoreditch; [M6](#m6) Broadway Market; [M9](#m9) City approach.
- **Checked:** branch readable/raw and focused policy search, 2026-09-13. Gap: formal menu and corkage.

### 14. Brawn
- **Repo ID:** new. Columbia Road; **49 Columbia Road, E2 7RG**. [Official](https://www.brawn.co/).
- **Status: official-confirmed — PRIVATE HIRE ONLY evidence.** [Official event PDF, path dated 2024-11](https://www.brawn.co/wp-content/uploads/2024/11/A.C.T%5FBrawn%5FPrivate%5FHire%5FV6.pdf): **“we are happy for you to bring your own bottles; the corkage fee is £30 per bottle (75cl).”**
- **Scope:** semi-private back-room lunches Tuesday–Friday, 10–20 guests, 12–4; £2,000 food/beverage minimum and 12.5% service in this document. **Do not apply £30 to an ordinary dinner booking.** Document age warrants reconfirmation.
- **Public email:** `enquiries@brawn.co`, PDF and [contact](https://www.brawn.co/contact/).
- **Cuisine:** same PDF **“quality ingredient-led, seasonal cooking”** and natural-leaning wine list. **Editorial:** versatile Chenin Blanc for vegetable/white-meat courses; fresh Pinot Noir for richer seasonal plates, contingent on selected event menu.
- **Retailers:** [M6](#m6) Broadway Market; [M8](#m8) Shoreditch; [M7](#m7) Victoria Park, wider East London.
- **Checked:** home, six-page event PDF and contact, 2026-09-13. General-service fee unresolved.

### 15. Da Terra
- **Repo ID:** new. Bethnal Green; **8 Patriot Square, E2 9NF (official homepage S)**; FAQ confirms ground floor of Town Hall Hotel. [Correct official](https://www.daterra.co.uk/).
- **Status: official-confirmed.** [FAQ](https://www.daterra.co.uk/faq/): **“We charge corkage fee of £70 per bottle of 750ml and £40 per bottle of 375ml.”** No bottle cap/service treatment stated in fetched clause.
- **Public email:** `booking@daterra.co.uk`, fetched FAQ; `info@daterra.co.uk` also published there.
- **Cuisine:** homepage says chef's **“Brazillian and Italian origins”** intertwine in the menu. **Editorial:** textured dry Chenin for a multi-course menu; restrained Chardonnay for delicate/rich contrasts; fine Pinot Noir for meat courses. Final choice should follow actual menu.
- **Retailers:** [M7](#m7) Victoria Park and [M6](#m6) Broadway Market are East London options; [M8](#m8) is farther west in Shoreditch.
- **Checked:** correct homepage and FAQ, 2026-09-13. `da-terra.com` was rejected as an unrelated Brazilian garden business; not a restaurant source.

### 16. Restaurant St Barts
- **Repo ID:** new. Smithfield/City; **63 Bartholomew Close, EC1A 7BF (official contact S)**. [Official about](https://restaurant-stbarts.co.uk/about/).
- **Status: not-published in fetched about/FAQ.** [FAQ](https://restaurant-stbarts.co.uk/faqs/) checked; no corkage provision. Fee/limits unknown.
- **Public email:** `info@restaurant-stbarts.co.uk`, [official contact search result](https://restaurant-stbarts.co.uk/contact/) **S only**, not yet fetched email proof.
- **Cuisine:** **“a tasting menu that champions the very best small-scale farmers, growers, & conservationists”** across British Isles. **Editorial:** traditional-method sparkling for varied starters; textured Chardonnay for fish/white-meat courses; light Pinot Noir for richer courses, conditional on menu.
- **Retailers:** [M8b](#m8b) Clerkenwell; [M9](#m9) City; [M11](#m11) Bloomsbury. Not all immediate neighbours.
- **Checked:** about and FAQ plus focused search, 2026-09-13. Earlier wrongly formatted domain failed DNS and was discarded.

### 17. The Quality Chop House
- **Repo ID:** new. Farringdon; **88–94 Farringdon Road, EC1R 3EA**. [Official](https://thequalitychophouse.com/).
- **Status: not-published in fetched home/wine/contact sections.** Focused policy search found no explicit current clause. Fee/limits unknown.
- **Public email:** `info@thequalitychophouse.com` appears in official search results; fetched readable page obscures it. Treat as **S**, not independently decoded here.
- **Cuisine:** official **“contemporary ... ‘meaty’ past”**, British produce; wine section highlights Burgundy/Rhône. **Editorial:** Northern Rhône Syrah for chops; mature Cabernet-led red for beef; fresh Chenin for pâté/white-meat preparations if ordered.
- **Retailers:** [M8b](#m8b) Exmouth Market, [M11](#m11) Bloomsbury, [M2](#m2) wider Islington.
- **Checked:** full homepage with wine/menu links and focused search, 2026-09-13. Wrong initial `qualitychophouse.com` domain discarded; this source is `thequalitychophouse.com`.

### 18. Quality Wines
- **Repo ID:** new. Farringdon; **88 Farringdon Road, EC1R 3EA**. [Official](https://qualitywinesfarringdon.com/).
- **Status: not-published in fetched homepage.** Buying bottles from its own shelves for dining is not external BYO permission. Fee/limits unknown.
- **Public email:** **`info@qualitywinesfarringdon.com`**, fetched contact section.
- **Cuisine:** fetched sample sharing menus include focaccia, caponata, pasta and pot-roast poussin; broadly Mediterranean/European. **Editorial:** Sangiovese for ragù; Vermentino for vegetable/saline flavours; Pinot Noir for poultry. Sample dishes are not claimed current.
- **Retailers:** [M8b](#m8b) nearby Exmouth Market; [M11](#m11) Bloomsbury; [M2](#m2) wider Islington. Its own shelves remain an on-site alternative, not counted as external BYO sourcing.
- **Checked:** homepage, menu links and focused search, 2026-09-13. Linked current PDF menus were not read.

### 19. Sessions Arts Club
- **Repo ID:** new. Clerkenwell; **24 Clerkenwell Green, EC1R 0NA (official S)**. [Official](https://sessionsartsclub.com/).
- **Status: inaccessible/partial.** Home and [contact](https://sessionsartsclub.com/CONTACT) extraction omit address/contact/food content seen in search. No policy or fee established.
- **Public email:** `info@sessionsartsclub.com`, official contact **S only**. Fetched contact says **“We are unable to take reservations by email”**; use email only for enquiries, not an asserted reservation channel.
- **Cuisine:** insufficient fetched menu evidence. **Editorial pairings withheld** rather than attaching remembered dishes to a changing kitchen.
- **Retailers:** [M8b](#m8b), Clerkenwell; [M11](#m11), Bloomsbury; [M9](#m9), City, wider option.
- **Checked:** homepage/contact and focused search, 2026-09-13. Gap: menu, policy, fetched email/address proof.

### 20. Caravel
- **Repo ID:** new. Hoxton/Islington canal; **172 Shepherdess Walk, N1 7JL (official S)**. [Official lead](https://www.caravelrestaurant.com/contact/).
- **Status: inaccessible.** Contact and privacy pages returned 404 although indexed. No current policy/fee established. A Reddit £25 lead was deliberately not promoted to evidence.
- **Public email:** `contactus@caravelrestaurant.com`, [indexed official privacy/contact](https://www.caravelrestaurant.com/privacy-policy/) **S only**. Do not treat search indexing as proof the restaurant still operates unchanged.
- **Cuisine:** canal-boat bistro lead; usable official menu not retrieved. **Pairings withheld.**
- **Retailers:** [M8](#m8) Shoreditch; [M4](#m4) Islington; [M6](#m6) Broadway Market. All require a separate wider-neighbourhood stop.
- **Checked:** contact and privacy failed, focused search, 2026-09-13. High-priority operating-status and current-URL gap, not classified closed without evidence.

### 21. Jolene Newington Green
- **Repo ID:** new. Newington Green; **21 Newington Green, N16 9PU**. [Current official branch](https://www.jolenebakery.com/location/jolene-newington-green).
- **Status: not-published in fetched branch page.** Old `jolenen16.com` extraction failed; current branch page works. Fee/restrictions unknown.
- **Public email:** `office@jolenebakery.com`, official search results **S only**; no fetched email text in branch extraction.
- **Cuisine:** **“bakery and restaurant”**, **“daily changing menu for lunch and dinner.”** Exact cooking style unresolved. **Editorial provisional:** traditional-method sparkling with savoury bakery items; dry Chenin for broad seasonal lunch dishes. Dinner-specific pairings need the actual menu.
- **Retailers:** [M3](#m3) same green; [M4](#m4) adjoining St Paul's Road; [M5](#m5) wider Stoke Newington.
- **Checked:** old site failure, focused search, current named branch, 2026-09-13.

### 22. Morito Hackney Road
- **Repo ID:** new. Hackney Road; **195 Hackney Road, E2 8JL (official S)**. [Official branch lead](https://www.moritohackneyroad.co.uk/news/morito-hackney-road/).
- **Status: inaccessible.** [Group contact](https://www.morito.co.uk/contact-us) 404; [branch private-hire](http://moritohackneyroad.co.uk/private-hire) 403. Fee/policy unknown.
- **Public email:** `info@moritohackneyroad.co.uk`, official contact/private-hire **S only**. Different `info@moritohackney.co.uk` appears on an indexed catering page; do not conflate them.
- **Cuisine:** Moorish tapas/mezze is official group search description, not fetched page proof. **Editorial provisional:** dry fino-style sherry for salty tapas; dry rosé for spiced mezze. Requires verified menu before publishing pairing copy.
- **Retailers:** [M6](#m6) Broadway Market, [M8](#m8) Shoreditch, [M7](#m7) Victoria Park. Wider East London cluster.
- **Checked:** contact failure, one focused policy/email search and private-hire failure, 2026-09-13.

### 23. Manteca — Curtain Road
- **Repo ID:** new. Shoreditch; **49–51 Curtain Road, EC2A 3PT (official home/search)**. [Official](https://www.mantecarestaurant.co.uk/).
- **Status: not-published in checked homepage.** Raw HTML recovered full cuisine description, but no corkage provision established. [Contact](https://www.mantecarestaurant.co.uk/contact) readable extraction failed.
- **Public email:** `hello@mantecarestaurant.co.uk`, official contact **S only**. Fee/limits unknown.
- **Cuisine:** raw official **“hand rolled pasta, in-house salumeria, nose-to-tail butchery & fire-cooked cuts to share.”** **Editorial:** bright Sangiovese for pasta/meat sauces; sparkling dry Lambrusco for salumi; structured Nebbiolo for richer cuts.
- **Retailers:** [M8](#m8), same Shoreditch district; [M9](#m9), City; [M6](#m6), wider Broadway Market.
- **Checked:** home readable/raw, contact failure, focused search, 2026-09-13.

### 24. Planque
- **Repo ID:** new. Haggerston; **Arches 322–324 Acton Mews, E8 4EA (official contact S)**. [Official FAQ](https://planque.co.uk/faqs/).
- **Status: official-no for ordinary non-member guests.** **“Wines may not be brought in to be drank at Planque with the exception of our members who can also drink wines from within their Planque cellar.”** Membership exception is not general paid corkage; fee not given.
- **Public email:** `hello@planque.co.uk`, fetched FAQ.
- **Cuisine:** **“French leaning dishes meant for sharing.”** **Editorial:** white Burgundy for richer French sauces; Pinot Noir for poultry; Cabernet Franc for charcuterie, only after confirming actual dishes. These are on-list/member-context suggestions, not a recommendation to bring wine against policy.
- **Retailers:** [M6](#m6) Broadway Market, [M4](#m4) Islington, [M5](#m5) Stoke Newington. Take-home/member-cellar sourcing only; no ordinary BYO claim.
- **Checked:** FAQ and official contact search, 2026-09-13. Gap: full membership terms and fetched address.

### 25. Sune
- **Repo ID:** new. Broadway Market/Haggerston; **129A Pritchard's Road, E2 9AP**. [Official visit](https://www.sune.restaurant/visit).
- **Status: official-confirmed.** [Need to know](https://www.sune.restaurant/needtoknow): **“We charge £35 per bottle, £45 for sparkling and £65 per magnum.”** Special bottles welcome; bottle cap not stated. General discretionary service is 13.5%; specific fee treatment not separately explained.
- **Public email:** `ciao@sune.restaurant`, fetched visit/raw home.
- **Cuisine:** [sample-menu page](https://www.sune.restaurant/sample-menus) retrieved but menu itself not readable. **Food-based pairings withheld** until actual dishes/cuisine are extracted; a good policy is not sufficient menu evidence.
- **Retailers:** [M6](#m6), Broadway Market first; [M7](#m7), Victoria Park; [M8](#m8), wider Shoreditch.
- **Checked:** visit, need-to-know, home/raw and sample-menu page, 2026-09-13. Gap: food/menu proof.

### 26. Angelina — Dalston
- **Repo ID:** new. Dalston; **56 Dalston Lane, E8 3AH (official S)**. [Official branch](https://angelina.london/restaurant/).
- **Status: not-published in fetched restaurant page.** No policy found in focused search. Fee/limits unknown; Osteria Angelina Spitalfields not counted.
- **Public email:** `dalston@angelina.london`, official branch **S only**; text extractor omitted footer.
- **Cuisine:** **“We take our inspiration from Italy and Japan”**, changing seasonal menu. **Editorial:** dry Riesling for bright Japanese-influenced preparations; textured Soave for Italian/Japanese seafood; light Pinot Noir for umami-rich meat courses, conditional on menu.
- **Retailers:** [M6](#m6) Broadway Market, [M3](#m3) Newington Green, [M5](#m5) Stoke Newington. All wider adjoining districts rather than Dalston doorstep claims.
- **Checked:** branch and focused search, 2026-09-13. Gap: current fee, fetched address/email.

### 27. Elliot's Borough Market
- **Repo ID:** new. Borough; **12 Stoney Street, SE1 9AD**. [Official branch](https://www.elliots.london/reservations-borough).
- **Status: not-published in fetched reservations page.** In-house natural-wine store does not establish external BYO. Fee/limits unknown.
- **Public email:** `boroughmarket@elliots.london`, official branch search lead; branch page fetched, but full email extraction not independently quoted here.
- **Cuisine:** restaurant/bar/natural-wine-store is official title; full food menu not read. **Pairings withheld** pending [menu](https://www.elliots.london/menu-borough) extraction.
- **Retailers:** [M10](#m10), same market; [M9](#m9), across the river; [M11](#m11), wider Bloomsbury. Third genuinely local verified merchant remains a gap.
- **Checked:** branch/reservations, focused search returning menu link, 2026-09-13.

### 28. José Tapas Bar — Bermondsey Street
- **Repo ID:** new. Bermondsey; **104 Bermondsey Street, SE1 3UB (official S; street in fetched group text)**. [Official branch](https://josepizarro.com/venues/jose-tapas-bar-bermondsey/).
- **Status: not-published in fetched pages.** Old indexed group “midweek corkage” terms exclude José Tapas, but that clause was **not present in fetched current privacy/terms**, so neither general permission nor general refusal is established.
- **Public email:** `info@josepizarro.com`, official branch **S**; fetched text/contact extraction requires final confirmation.
- **Cuisine:** Spanish tapas; official describes a changing seasonal tapas menu. **Editorial:** fino sherry for salty tapas; Albariño for seafood; fresh Rioja/Garnacha for meat tapas.
- **Retailers:** [M10](#m10) Borough; [M9](#m9) City across river; [M11](#m11) farther Bloomsbury. Wider travel needed for third fully verified specialist.
- **Checked:** branch and [current privacy/terms](https://josepizarro.com/privacy-policy/), focused search, 2026-09-13. Do not transfer a Pizarro promotion here.

### 29. Pizarro — Bermondsey Street
- **Repo ID:** new. Bermondsey; **194 Bermondsey Street, SE1 3TQ**. [Official branch](https://josepizarro.com/venues/pizarro-restaurant-bermondsey/).
- **Status: not-published in fetched current pages.** Indexed old midweek promotion is not current fetched evidence; fee/day/quantity unknown.
- **Public email:** `reservations@pizarrorestaurant.com`, official S and publicly encoded contact link in fetched branch. Displayed email was Cloudflare-obscured, not independently decoded here.
- **Cuisine:** **“seasonal menu of tapas alongside more substantial dishes and larger group sharing plates”**, Spanish produce. **Editorial:** aged Rioja for pork/meat; dry sherry for tapas; Godello for richer seafood preparations.
- **Retailers:** [M10](#m10), Borough; [M9](#m9), across river; [M11](#m11), wider central trip. No false immediate-proximity claim.
- **Checked:** branch and current group privacy/terms, focused search, 2026-09-13.

### 30. Casse-Croûte
- **Repo ID:** new. Bermondsey; **109 Bermondsey Street, SE1 3XB**, official home. [Official](https://www.cassecroute.co.uk/).
- **Status: third-party-only.** [Fetched Bald Flavours article](https://baldflavours.substack.com/p/casse-croute-109-bermondsey-st-london), quoting an earlier Andy Hayler experience: **“£25 corkage fee ... only for French wine.”** Current fee/restriction not officially established; this is second-hand reporting, not restaurant consent.
- **Contact:** [official contact](https://www.cassecroute.co.uk/contact) says in search **“contact form below”**; fetch incomplete. **Contact form, no public email verified**. Reservations by phone/walk-in per official home.
- **Cuisine:** official **“Authentic bistro style French cuisine”**. **Editorial:** Loire Chenin for bistro fish; Pinot Noir for poultry; Bordeaux for braises, depending on daily menu. French styles chosen to respect the reported restriction without asserting it current.
- **Retailers:** [M10](#m10), Borough; [M9](#m9), City; [M11](#m11), wider Bloomsbury.
- **Checked:** official home, failed contact, focused search, third-party article raw, 2026-09-13.

### 31. Pique-Nique
- **Repo ID:** new. Bermondsey/Tanner Street; **Tanner Street, SE1 3LD (official S)**. [Official](https://pique-nique.co.uk/).
- **Status: inaccessible.** Homepage extraction JS-rendered. Focused search found wine-list PDF but no usable policy; fee/limits unknown.
- **Public email:** only `jobs@pique-nique.co.uk` appeared in official search, explicitly recruitment; **general contact unknown**, telephone 020 7403 9549 is S. Do not use a careers address as a booking address.
- **Cuisine:** official search title “French restaurant & rôtisserie,” not fetched proof. **Editorial provisional:** white Burgundy for roast chicken; mature Pinot Noir for roast poultry; Rhône red for richer roast meats. Menu confirmation needed.
- **Retailers:** [M10](#m10) Borough, [M9](#m9) City across river, [M11](#m11) wider central source.
- **Checked:** homepage failure and focused search, 2026-09-13. Linked 2024 wine PDF not fetched; explicit residual work, no current policy claim.

### 32. The Garrison
- **Repo ID:** new. Bermondsey; **99–101 Bermondsey Street, SE1 3XB**. [Official](https://www.thegarrison.co.uk/).
- **Status: not-published in fetched home.** Fee/limits unknown. Search surfaced an older wine list, not current permission.
- **Public email:** `garrison@youngs.co.uk`, official home/contact search **S**; current contact page displays a conflicting `info@thegarrison.co.uk` mailto in search, so address should be rechecked before outreach.
- **Cuisine:** official **“seasonal, British food”** with provenance focus. **Editorial:** dry Chenin for seasonal vegetables/white meat; Pinot Noir for roast poultry; Syrah for richer meat, conditional on menu.
- **Retailers:** [M10](#m10), [M9](#m9), [M11](#m11): Borough, City across river, then wider Bloomsbury; third immediate-neighbourhood merchant gap.
- **Checked:** home and focused search, 2026-09-13. Email conflict not silently resolved.

### 33. Legare
- **Repo ID:** new. Shad Thames/Tower Bridge; **Cardamom Building, 31G Shad Thames, SE1 2YR**. [Official](https://legarelondon.com/).
- **Status: not-published in fetched home.** Fee/restrictions unknown; private-dining search result provides no policy.
- **Public email:** **`info@legarelondon.com`**, fetched home.
- **Cuisine:** official title **“Neighbourhood Italian Restaurant”**; [about](https://legarelondon.com/about/) S specifies seasonal antipasti/pasta with British produce. **Editorial:** fresh Sangiovese for meat/tomato pasta; Verdicchio for seafood/vegetable antipasti; light Nebbiolo for richer preparations. Broad Italian suggestions, not current dish claims.
- **Retailers:** [M10](#m10) Borough, [M9](#m9) City across Tower/London Bridge area, [M11](#m11) wider Bloomsbury. No three immediate shops verified.
- **Checked:** homepage and focused policy search, 2026-09-13.

### 34. Trivet
- **Repo ID:** new. Bermondsey/London Bridge; **36 Snowsfields, SE1 3SU — postcode requires official verification; search OpenTable truncates it**. [Official about](https://trivetrestaurant.co.uk/about/).
- **Status: official-confirmed — MEMBERSHIP BENEFIT ONLY.** [Tasting Club](https://trivetrestaurant.co.uk/trivet-tasting-club/): **“Members enjoy free corkage during lunchtime at Trivet up to 4 bottles per table.”** £240 annual membership quoted on same page. General diner/dinner corkage unknown.
- **Public email:** **`info@trivetrestaurant.co.uk`**, fetched club page.
- **Cuisine:** official calls it an “informal, high-quality restaurant” using finest ingredients; specific menu style insufficiently evidenced. **Pairings withheld** until sourced menu, rather than projecting remembered signature dishes.
- **Retailers:** [M10](#m10), Borough; [M9](#m9), City across river; [M11](#m11), wider Bloomsbury. Retail purchases do not waive membership requirement.
- **Checked:** about and Tasting Club, focused search, 2026-09-13. **Gap:** ordinary-service policy, menu and full address proof.

### 35. OMA
- **Repo ID:** new. Borough Market; **2–4 Bedale Street, SE1 9AL, above AGORA**. [Official](https://www.oma.london/).
- **Status: not-published in fetched home/raw HTML.** Fee/restrictions unknown. Distinct from AGORA; no policy transfer.
- **Public email:** **`hello@oma.london`**, fetched raw footer.
- **Cuisine:** **“greek isles”** and **“bold flavours of the levant and further afield”**; 400+ bin wine list. **Editorial:** Assyrtiko for saline seafood/bright flavours; dry rosé for spiced vegetable plates; light Xinomavro for richer meat dishes, conditional on menu.
- **Retailers:** [M10](#m10), same Bedale Street; [M9](#m9), City; [M11](#m11), wider Bloomsbury. Third genuinely close verified shop remains a gap.
- **Checked:** home readable/raw and focused search, 2026-09-13.

### 36. Restaurant Story
- **Repo ID:** new. London Bridge/Tooley Street; **199 Tooley Street, SE1 2JX (official contact S)**. [Official](https://restaurantstory.co.uk/).
- **Status: official-confirmed.** [Useful information](https://restaurantstory.co.uk/useful-information/): **“£65 corkage fee for any 750ml bottle of wine, limited to one bottle per two guests.”** No service treatment stated in clause.
- **Public email:** `dine@restaurantstory.co.uk`, official home/contact S; home fetched.
- **Cuisine:** official **“story of British food through an ever-evolving tasting menu of seasonal dishes.”** **Editorial:** complex traditional-method sparkling for early courses; restrained Chardonnay for seafood/white meat; elegant Pinot Noir for richer courses, conditional on menu.
- **Retailers:** [M10](#m10) Borough; [M9](#m9) City; [M11](#m11) farther central sourcing.
- **Checked:** home and useful information, focused search, 2026-09-13. Full current menu/contact-page address extraction remains outstanding.

### 37. Artusi — Peckham
- **Repo ID:** new. Bellenden Road/Peckham; **161 Bellenden Road, SE15 4DH**. [Official](https://artusi.co.uk/).
- **Status: not-published in fetched home/info.** Fee/limits unknown. Do not confuse restaurant's Italian wine list with permission.
- **Public email:** **`info@artusi.co.uk`**, fetched home.
- **Cuisine:** official title Italian restaurant; indexed [info](https://artusi.co.uk/info) describes daily pasta/seasonal produce, but fetched path returned same home content. **Editorial:** Sangiovese for meat/tomato pasta; dry Verdicchio for vegetables/seafood; sparkling Lambrusco for salumi if served.
- **Retailers:** [M15 Hop Burns & Black](#m15), East Dulwich Road/Peckham edge; [M16 Gladwell's](#m16), Camberwell wider option; [M14](#m14), Dulwich Village wider specialist.
- **Checked:** home, info and focused search, 2026-09-13.

### 38. Levan
- **Repo ID:** new. Peckham Rye; **Units 3–4, 12–16 Blenheim Grove, SE15 4QL (official S)**. [Official about](https://www.levanlondon.co.uk/about/).
- **Status: not-published in about/booking page.** [Booking](https://www.levanlondon.co.uk/book-a-table/) checked; fee/limits unknown. Bar Levan next door is not merged with this restaurant.
- **Public email:** **`info@levanlondon.co.uk`**, booking page.
- **Cuisine:** **“contemporary European dishes”**; official about discusses fish, meat, vegetables, Sunday moules/steak frites. **Editorial:** saline Muscadet for mussels; fresh Cabernet Franc for steak; Jura Chardonnay for richer small plates. No bottle-stock claims.
- **Retailers:** [M15](#m15) Peckham/East Dulwich edge; [M16](#m16) Camberwell; [M14](#m14) Dulwich Village. Latter two wider travel.
- **Checked:** about/booking and focused search, 2026-09-13. Address extraction not independently fetched-proof verified.

### 39. Peckham Cellars
- **Repo ID:** new. Queens Road Peckham; **125 Queens Road, SE15 2ND (official S)**. [Official](https://peckhamcellars.co.uk/).
- **Status: not-published in home/private-hire.** Official sells wine to take away and drink in; this does not establish external BYO. Fee/limits unknown.
- **Public email:** **unknown from fetched official pages**. `hello@peckhamcellars.co.uk` appeared on LinkedIn search only and is not treated as verified restaurant contact. Website booking/WhatsApp route exists in indexed content; do not invent an email.
- **Cuisine:** **“seasonally inspired menu of snacks and small plates.”** **Editorial:** dry Chenin for varied small plates; fresh Gamay for lighter meat/vegetable dishes, conditional on actual menu. Specific country label not established.
- **Retailers:** [M15](#m15), Peckham/East Dulwich; [M16](#m16), Camberwell; [M14](#m14), Dulwich Village. All wider than Queens Road doorstep.
- **Checked:** home, [private hire](https://peckhamcellars.co.uk/private-hire/), focused search, 2026-09-13. Gap: email, policy and address extraction.

### 40. Little Cellars
- **Repo ID:** new. Camberwell; **75 Camberwell Church Street, SE5 8TU** (official short form “75 Church Street”). [Official](https://littlecellars.co.uk/).
- **Status: not-published in fetched home/private-hire.** Cellar Next Door's bottle shop is not external BYO permission or a restaurant corkage rate.
- **Public email:** **unknown** after home/private-hire and focused lookup; use site booking/contact route, not an invented address.
- **Cuisine:** official “neighbourhood bistro”; associated Cellar Next Door serves **“cheese and charcuterie plates and nibbles.”** **Editorial provisional:** fresh Gamay for charcuterie; dry Chenin for cheese. These are supported for the adjacent bar's food, **not a verified current main-restaurant menu**; main-restaurant pairings remain a gap.
- **Retailers:** [M16](#m16) same Camberwell Church Street; [M15](#m15) Peckham/East Dulwich; [M14](#m14) Dulwich Village. Own Cellar Next Door is an additional obvious option, but separate postal address not verified, so not counted in the three-address directory.
- **Checked:** home, [private hire](https://littlecellars.co.uk/private-hire/), focused search, 2026-09-13.

### 41. The Camberwell Arms
- **Repo ID:** new. Camberwell; **65 Camberwell Church Street, SE5 8TR (official contact S)**. [Official contact/about](https://thecamberwellarms.co.uk/contact/).
- **Status: not-published — current general policy unresolved.** Fetched [private-dining PDF](https://thecamberwellarms.co.uk/wp-content/uploads/2025/08/CA25-PDR-Terms-Conditions.pdf) explicitly applies **“17th Nov - 31st Dec 2025”**, published 18.08.2025. Its **“£25 per 750ml of still wine | £30 per 750ml of sparkling wine”** is **expired-period private-hire evidence**, not a current restaurant rate.
- **Public email:** **`enquiries@thecamberwellarms.co.uk`**, PDF.
- **Cuisine:** official seasonal cooking, house bread, pickles, smoked fish and ferments. **Editorial:** dry Riesling for pickles/smoked fish; Chenin for seasonal vegetables; Pinot Noir for richer meat plates if ordered.
- **Retailers:** [M16](#m16), same street; [M15](#m15), East Dulwich Road; [M14](#m14), Dulwich Village. Last two wider travel.
- **Checked:** contact/about and four-page PDF, focused search, 2026-09-13. Do not label this current official-confirmed merely because an official old PDF was found.

### 42. Flour & Grape
- **Repo ID:** new. Bermondsey; **214 Bermondsey Street, SE1 3TQ**. [Official](https://www.flourandgrape.com/).
- **Status: not-published in fetched home/raw.** Fee/restrictions unknown. Strong informal pasta destination rather than formal fine dining.
- **Public email:** **`contact@flourandgrape.com`**, fetched home.
- **Cuisine:** official raw metadata: **“Italian restaurant serving fresh handmade pasta”**. **Editorial:** Sangiovese for tomato/meat sauces; textured Verdicchio for richer white sauces; dry Lambrusco for salty/cheesy pasta accompaniments. Current dishes not inferred from old social image captions.
- **Retailers:** [M10](#m10) Borough, [M9](#m9) City, [M11](#m11) wider Bloomsbury. Third local-shop gap applies.
- **Checked:** home readable/raw, focused search, 2026-09-13.

### 43. Naughty Piglets
- **Repo ID:** new. Brixton; **28 Brixton Water Lane, SW2 1PE**. [Official](https://www.naughtypiglets.co.uk/); [contact/hours](https://www.naughtypiglets.co.uk/opening-hours).
- **Status: not-published in fetched home/hours.** Fee/restrictions unknown.
- **Public email:** **`naughtypiglets@gmail.com`**, fetched hours; this Gmail address is genuinely published, not inferred.
- **Cuisine:** official **“hosting guest chefs every 4 weeks”**, with different regional cuisines and wine selections. **Pairings withheld:** no fixed cuisine or current residency menu established; generic old French small-plates descriptions would be misleading.
- **Retailers:** [M12](#m12) Clapham North; [M13](#m13) Abbeville; [M14](#m14) Dulwich Village. All wider South London trips, not Brixton-local doorstep picks.
- **Checked:** home/hours, focused search, 2026-09-13. Gap: current residency menu and policy.

### 44. Sorella
- **Repo ID:** new. Clapham; **148 Clapham Manor Street, SW4 6BX — provisional lead, address not verified in fetched pages**. [Official about](https://www.sorellarestaurant.co.uk/about).
- **Status: not-published in checked about/events.** Fee/limits unknown.
- **Public email:** `reservations@sorellarestaurant.co.uk` appears on [official events](https://www.sorellarestaurant.co.uk/events) search and the page was fetched; historic event context, not independently verified as current booking mailbox.
- **Cuisine:** official **“neighbourhood Italian inspired restaurant”**. **Editorial:** Sangiovese for tomato/meat flavours; Soave for seafood/vegetable preparations; light Nebbiolo for richer pasta/meat, conditional on menu.
- **Retailers:** [M12](#m12) Clapham North; [M13](#m13) Abbeville; [M14](#m14) wider Dulwich Village. No three adjacent verified shops.
- **Checked:** about readable/raw, events, focused search, 2026-09-13. Address and current booking contact remain gaps.

### 45. Darby's
- **Repo ID:** new. Nine Elms; **3 Viaduct Gardens, SW11 7AY**. [Official](https://www.darbys-london.com/).
- **Status: official-confirmed, discretionary.** [Menus](https://www.darbys-london.com/darbysmenus), raw HTML: **“Still Wine - £35 - 75cl”**, **“Sparkling Wine - £45 - 75cl”**; **“all corkage arrangements including the quantity of bottles permitted are offered at the discretion of the management team.”** Advance agreement needed; no guaranteed bottle allowance.
- **Public email:** **`reservations@darbys-london.com`**, fetched raw home.
- **Cuisine:** [about](https://www.darbys-london.com/about): **“NYC inspired oyster bar, large open grill and bakery”**, British/Irish ingredients. **Editorial:** crisp Muscadet/Chablis for oysters; mature Cabernet blend for grilled beef; dry traditional-method sparkling for briny/rich contrasts.
- **Retailers:** [M12](#m12) Clapham North; [M13](#m13) Abbeville; [M10](#m10) Borough, farther east. None asserted as Nine Elms doorstep sourcing.
- **Checked:** home, about and menus readable/raw, focused search, 2026-09-13. Raw policy rescued a misleadingly empty reader extraction.

### 46. Smoke & Salt
- **Repo ID:** new. Tooting; **115 Tooting High Street, SW17 0SY (official PDF S)**. [Official FAQ](https://www.smokeandsalt.com/faq).
- **Status: not-published in fetched FAQ and drinks PDF.** [Drinks PDF](https://www.smokeandsalt.com/_files/ugd/ca551e_c8631608040242a6a6ae4aa27bf1320e.pdf) downloaded and read; no corkage clause. OpenTable BYO tag is only a lead, not a policy.
- **Public email:** **`manager@smokeandsalt.com`**, fetched FAQ for group bookings.
- **Cuisine:** FAQ describes **Craft and Culture tasting menus**; culinary techniques/dishes insufficiently read. **Pairings withheld** pending actual food menu, rather than assuming smoke/fermentation from the name alone.
- **Retailers:** [M13](#m13) Abbeville, [M12](#m12) Clapham North, [M14](#m14) Dulwich Village. All wider travel; Balham Wine Tasting Shop closer lead remained inaccessible.
- **Checked:** FAQ, focused search, two-page drinks PDF, 2026-09-13.

### 47. The Dysart Petersham
- **Repo ID:** new. Petersham/Richmond; **135 Petersham Road, TW10 7AA**, fetched raw official address. [Official](https://www.thedysartpetersham.co.uk/).
- **Status: not-published in fetched home/wine list.** [Wine list](https://www.thedysartpetersham.co.uk/wine-drink/drinks/wines/) checked; no usable current policy. Forum unanswered-enquiry anecdote discarded as not evidence of refusal.
- **Public email:** **`enquiries@thedysartpetersham.co.uk`**, fetched raw home.
- **Cuisine:** official site quotes highly seasonal cooking/classical technique and bold sauces; quote describes fish and duck examples, not guaranteed current menu. **Editorial:** textured Chardonnay for fish with sauce; Pinot Noir for duck; dry Riesling for sharp/verjus flavours, contingent on current preparation.
- **Retailers:** [M17 Good Wine Shop Richmond Hill](#m17) first; [M18 Kew](#m18), wider Richmond borough; [M19 Teddington](#m19), a separate cross-area journey.
- **Checked:** home readable/raw and wine list, focused search, 2026-09-13.

### 48. Petersham Nurseries Restaurant — Richmond
- **Repo ID:** new. Petersham/Richmond; **Church Lane, off Petersham Road, TW10 7AB — address lead not independently verified in this run**. [Official](https://petershamnurseries.com/).
- **Status: official-confirmed — permission entirely conditional.** [Terms](https://petershamnurseries.com/terms-and-conditions/): **“Petersham Nurseries Restaurant ... Corkage is at the manager's discretion.”** **No fee or bottle allowance published in fetched clause.** The nearby £30 is **cakeage**, not corkage.
- **Public email:** **`info.richmond@petershamnurseries.com`**, fetched terms, published for venue enquiries/complaints; not claimed a dedicated booking mailbox.
- **Cuisine:** current Richmond restaurant food page not obtained (`/richmond/` 404). **Pairings withheld** pending a fetched menu rather than assuming former Italian dishes remain.
- **Retailers:** [M17](#m17), Richmond Hill; [M18](#m18), Kew; [M19](#m19), Teddington, wider travel.
- **Checked:** terms readable/raw, failed location page, targeted search, 2026-09-13. Caveat: restaurant name/format and postal address need current location-page verification.

### 49. Chez Lindsay
- **Repo ID:** new. Richmond riverside/Hill Rise; **11 Hill Rise, TW10 6UQ — provisional address lead, not verified in fetched pages**. [Official contact lead](https://www.chez-lindsay.co.uk/contact-us.html).
- **Status: inaccessible.** Contact and [home](https://www.chez-lindsay.co.uk/home.html) extraction failed. No corkage/fee established.
- **Public email:** obscured behind JavaScript in official search; **contact form/unknown**, do not guess. Public phone search lead 020 8948 7473.
- **Cuisine:** Breton/French is a candidate lead but no usable fetched cuisine proof. **Pairings withheld** until menu is read.
- **Retailers:** [M17](#m17) Richmond Hill, [M18](#m18) Kew, [M20 Good Wine Shop St Margarets](#m20) across the river/wider area.
- **Checked:** contact/home failed plus one focused policy/email search, 2026-09-13. Operating status not inferred from failures.

### 50. The French Table
- **Repo ID:** new. Surbiton, London Borough of Kingston; **85 Maple Road, KT6 4AW**. [Official](https://www.thefrenchtable.co.uk/); [contact](https://www.thefrenchtable.co.uk/contact).
- **Status: official-confirmed.** [Wine page](https://www.thefrenchtable.co.uk/wine): **“maximum of two standard (75cl) bottles or up to one magnum per reservation regardless of numbers”**; **“£30 per standard bottle of still wine and £40 per standard bottle of sparkling, excluding the 12.5% service charge. For magnums, the corkage fee is £60.”** Mention when booking; sparkling-magnum distinction not separately given.
- **Public email:** **`enquiries@thefrenchtable.co.uk`**, fetched contact.
- **Cuisine:** official **“contemporary French cooking”**. **Editorial:** white Burgundy for sauce-led fish/poultry; mature Pinot Noir for duck/game if served; traditional-method sparkling for varied tasting starters.
- **Retailers:** [M19](#m19) Teddington first; [M17](#m17) Richmond Hill; [M18](#m18) Kew. **All require appreciable wider-area travel; these are not three nearby Surbiton shops.** Local Ex Cellar/Wined Up Here verification remains unresolved.
- **Checked:** home, wine and contact pages, 2026-09-13.

## Linked merchant directory
All entries below were checked 2026-09-13. A branch's existence/address does not verify stock, opening on the meal date or suitability of a specific vintage. Selection rationales are editorial. Addresses from successfully fetched official readable pages or raw HTML unless an explicit caveat is given. Reusing IDs is intentional.

<a id="m1"></a>**M1 — Highbury Vintners, Highbury.** 71 Highbury Park, London N5 1UA. [Official contact](https://highburyvintners.co.uk/pages/contact-us): “Visit our shop ... 71 Highbury Park”. Broad independent specialist; practical for Highbury restaurants. Official contact retrieved; no restaurant-to-shop distance asserted.

<a id="m2"></a>**M2 — The Sampler, Islington.** 266 Upper Street, London N1 2UQ. [Official contact](https://thesampler.co.uk/pages/contact). Specialist wine retailer with substantial range; strong Highbury/Upper Street option and wider Islington alternative for central restaurants.

<a id="m3"></a>**M3 — Yield N16, Newington Green.** Alliance House, 44/45 Newington Green, London N16 9PX. [Official locations](https://www.yieldlondon.com/). “top quality, low-intervention, natural wines”; same-green sourcing for Perilla/Jolene and adjoining Canonbury.

<a id="m4"></a>**M4 — Yield N1, Islington.** 97 St Paul's Road, London N1 2NA. [Official locations](https://www.yieldlondon.com/). Independent low-intervention specialist on Trullo's road; useful wider north-Islington option.

<a id="m5"></a>**M5 — Shrine to the Vine, Stoke Newington.** 163 Stoke Newington Church Street, London N16 0UL. [Official shops](https://shrinetothevine.co.uk/pages/london-wine-shops). Broad artisanal selection including classical French and wider European regions; wider trip north from Dalston/Newington Green, not automatically close.

<a id="m6"></a>**M6 — Shrine to the Vine, Broadway Market.** 27 Broadway Market, London E8 4PH. [Official shops](https://shrinetothevine.co.uk/pages/london-wine-shops): “second Shrine to the Vine wine shop”. Strong independent for London Fields, Broadway Market and wider Shoreditch. **This is not the closed Noble Fine Liquor under its old name.**

<a id="m7"></a>**M7 — Bottle Apostle, Victoria Park Village.** 95 Lauriston Road, Hackney, London E9 7HJ. [Official shops](https://www.bottleapostle.com/shops.html). Independent, over-1,000-item wine/beer/sake/spirits range across group; useful East London alternative, wider from Shoreditch.

<a id="m8"></a>**M8 — Passione Vino, Shoreditch.** 85 Leonard Street, London EC2A 4QS. [Official branches](https://passionevino.co.uk/wine-bars/); [official specialist/retail site](https://passionevino.co.uk/). Italian boutique wine specialist with bars and delivered retail selection. **Gap:** sources establish branch and wine retail business, but same-day physical bottle take-away terms at this bar were not separately verified; ask before detouring. Do not silently present it as guaranteed off-sales availability.

<a id="m8b"></a>**M8b — Passione Vino, Exmouth Market.** 58 Exmouth Market, London EC1R 4QR. [Official branches](https://passionevino.co.uk/wine-bars/). Strong Italian specialist fit for Luca/Farringdon. Same physical take-away verification caveat as M8; branch is verified, retail collection terms not.

<a id="m9"></a>**M9 — Amathus City.** 17–19 Leadenhall Market, London EC3V 1LR. [Official store](https://www.amathusdrinks.com/city-store). Broad fine-wine/spirits specialist; City choice and across-river alternative for Borough. **Officially closed Saturday/Sunday** in fetched page. Stock can require 1–2 working days' transfer; online inventory is not branch stock.

<a id="m10"></a>**M10 — Bedales of Borough.** 5 Bedale Street, Borough Market, London SE1 9AL. [Official](https://bedaleswines.com/), address confirmed in fetched raw HTML. Official says bottle collection available “on-site or take away”; small producers/family estates. Strong same-market source for Hawksmoor/OMA/Elliot's and wider Bermondsey.

<a id="m11"></a>**M11 — Shrine to the Vine, Lamb's Conduit Street.** 48 Lamb's Conduit Street, London WC1N 3LH. [Official shops](https://shrinetothevine.co.uk/pages/london-wine-shops). Excellent fine/artisanal wine selection and same street as Noble Rot; wider central purchase for City/Bermondsey, **not a nearby-shop claim**. Sunday closed in fetched page.

<a id="m12"></a>**M12 — D Vine Cellars, Clapham North.** 1 Voltaire Road, London SW4 6DQ. [Official contact](https://dvinecellars.com/pages/contact). Independent specialist/shop-bar; relevant for Clapham and wider Brixton/Nine Elms. **Closed Sunday and Monday** per fetched hours, important for Sunday corkage plans.

<a id="m13"></a>**M13 — Bottle Apostle, Clapham Abbeville Village.** 59 Abbeville Road, London SW4 9JW. [Official shops](https://www.bottleapostle.com/shops.html). Broad independent specialist, suitable for Clapham and a wider trip from Wandsworth/Tooting.

<a id="m14"></a>**M14 — Dulwich Vintners.** 85–87 Dulwich Village, London SE21 7BJ. [Official contact](https://www.dulwichvintners.co.uk/pages/contact-us). “Independent Wine Merchant”; broad South London specialist. Wider travel from Peckham/Camberwell and substantially wider from Clapham/Tooting. **Closed Mondays** per fetched hours.

<a id="m15"></a>**M15 — Hop Burns & Black, East Dulwich Road/Peckham.** 38 East Dulwich Road, London SE22 9AX. [Official](https://www.hopburnsblack.co.uk/), address checked in raw footer; natural wine alongside craft beer/hot sauce. A strong independent natural-wine option for Peckham; not claimed a classical rare-wine merchant.

<a id="m16"></a>**M16 — Gladwell's, Camberwell.** 2 Camberwell Church Street, London SE5 8QU. [Official visit](https://gladwells.co.uk/pages/visit-us); [official description](https://gladwells.co.uk/): includes “wine merchant” among its specialist departments. Closest-fit Camberwell option; a multi-department deli rather than a wine-only shop. Fine-wine depth not independently assessed.

<a id="m17"></a>**M17 — The Good Wine Shop, Richmond Hill.** 56 Friars Stile Road, Richmond TW10 6NQ. [Official shops](https://www.thegoodwineshop.co.uk/pages/shops). Specialist independent group, organic/biodynamic credentials; sensible Richmond/Petersham first choice.

<a id="m18"></a>**M18 — The Good Wine Shop, Kew.** 2 Royal Parade, Station Approach, Kew TW9 3QD. [Official shops](https://www.thegoodwineshop.co.uk/pages/shops). Same quality-led independent group; a separate Kew trip from Richmond/Petersham, much wider from Surbiton.

<a id="m19"></a>**M19 — The Good Wine Shop, Teddington.** 47 High Street, Teddington TW11 8HA. [Official shops](https://www.thegoodwineshop.co.uk/pages/shops). Good south-west sourcing option, still separate travel from Surbiton/Petersham. No walking-time claims.

<a id="m20"></a>**M20 — The Good Wine Shop, St Margarets.** 137 St Margarets Road, TW1 1RG. [Official shops](https://www.thegoodwineshop.co.uk/pages/shops). Strong independent group across the river from Richmond; not the same neighbourhood as Petersham.

### Merchant exclusions and incomplete local leads
- **Philglas & Swiggot: excluded.** [Fetched official closure](https://philglas-swiggot.com/): Marylebone and Battersea stores closed **16 March 2025**. Old Northcote Road/Richmond directory listings are not usable current merchant evidence.
- **Noble Fine Liquor: excluded under old name.** Trade reporting says closed; current official Shrine directory verifies the replacement at 27 Broadway Market.
- **Lea & Sandeman Barnes/Chiswick:** official indexed addresses 51 High Street SW13 9LN and 167 Chiswick High Road W4 2DR, but [shop-directory fetch](https://www.leaandsandeman.co.uk/content/shops.html) 403. Not counted as fetched-verified merchant recommendations.
- **The Wine Tasting Shop, Balham:** [official contact](https://thewinetastingshop.co.uk/contact-us/) indexed at 18 Hildreth Street SW12 9RQ; extraction incomplete. Promising more-local substitute for Chez Bruce/Tooting, not silently labelled verified.
- **Lechevalier:** [official lead](https://lechevalier.co.uk/) indexed at 85 Tower Bridge Road SE1 4TW; both domain forms failed fetch. Would improve Bermondsey practicality, but not counted as verified.
- **Dynamic Vines Bermondsey:** [official branch](https://www.dynamicvines.com/bermondsey) search gives Unit 5 Discovery Business Park, St James's Road SE16 4RA; fetched 403. Saturday public shop opening lead; not counted as verified.
- **Theatre of Wine:** indexed official store URL returned 404; no imagined Leytonstone/other branch carried forward.
- **Surbiton local specialist gap:** Ex Cellar and Wined Up Here surfaced but branch research not completed. The French Table's three merchant suggestions therefore explicitly require wider travel.

## Sources kept and dropped
**Kept:** primary FAQs, restaurant branch/contact pages, dated official PDFs and raw HTML, linked record-by-record above. Jamie Goode's dated Trullo review and the Casse-Croûte article are kept only as labelled third-party evidence.

**Dropped/not promoted:** Ourglass general BYO round-up and Reddit corkage list (not sufficient to verify current rates); restaurant aggregators where extraction failed; restaurant/menu snippets as policy proof; a US Luca FAQ with dollar fees (wrong restaurant); unrelated `da-terra.com`; the repurposed Leroy domain; expired Camberwell private-event pricing as current general corkage; stale/closed Philglas and Noble Fine Liquor merchant listings. Pophams pasta dinner, Lyle's, Nest and Lagom were considered as expansion leads but not made final candidates because closure/relaunch/current-scope uncertainty would add unnecessary false confidence. Clipstone was discarded as outside this lane, and all named lane exclusions are absent from the final 50.

## Review findings and residual work
1. **High — historical input `data.json`, `cabotte`, `chezbruce`, `trinity`:** stale price/scope descriptions conflict with fetched official evidence. Cabotte's dated Friday offer needs currency confirmation; Chez Bruce lunch/dinner and service treatment need explicit display; Trinity excludes Upstairs and requires bottle/list limits.
2. **High — this artifact, records 14/34/48:** special-scope evidence must not be published as general permission. Brawn is private-hire-only evidence; Trivet is paid-member lunch benefit; Petersham is entirely discretionary with no fee. Record 41's 2025-only private-event PDF is expired.
3. **High — this artifact, records 10–12/19–20/22/31/49:** retrieval gaps remain. No negative policy or closure conclusion can be drawn from them. All 50 slots are accounted for, **not all 50 records fully researched**.
4. **Medium — this artifact, contact/address fields:** several S/H/provisional fields remain, including menu/address gaps in some otherwise official-confirmed records. Email search results are explicitly not represented as fetched proof; obfuscated/unknown emails need a later manual contact-page review. No outreach was made.
5. **Medium — merchant directory M8/M8b and wider-area picks:** branch identity verified but physical take-away collection terms not established at Passione Vino. Bermondsey, Brixton/Tooting and Surbiton lack three independently verified close-by shops; wider recommendations are labelled, not padded with invented nearby branches.
6. **Medium — pairings:** several food-based pairing fields deliberately withheld/provisional because menu content was inaccessible. They should not be published until cuisine evidence is completed. No stock/vintage recommendations made.
7. **Low — technical extraction:** official readable extraction dropped accordion/footer policy at Luca and Darby's. Raw official HTML recovered both. Future checks should search raw source before treating a sparse page as policy absence.

### Suggested next work, not performed
Prioritise the 16 official-evidence records for human verification of scope/date and missing addresses; obtain menu evidence for Sune/Trivet/Petersham/Trinity; confirm Cabotte's current Friday offer. Then fill inaccessible restaurants, public general emails and more-local merchant alternatives in a separate bounded pass. No additional retries or outreach are implied as already done.

```acceptance-report
{
  "criteriaSatisfied": [
    {
      "id": "criterion-1",
      "status": "satisfied",
      "evidence": "Concrete sourced findings, severity-labelled review findings and residual risks written to /Users/danielbailey/.pi/agent/sessions/--Users-danielbailey-Documents-Code--/subagent-artifacts/outputs/eb6b3f11-b526-412a-9510-e7003bddd4af/corkage/north-east-south-city.md; 50 numbered candidates preserved. This attests the research artifact, not complete publication readiness."
    }
  ],
  "changedFiles": [
    "/Users/danielbailey/.pi/agent/sessions/--Users-danielbailey-Documents-Code--/subagent-artifacts/outputs/eb6b3f11-b526-412a-9510-e7003bddd4af/corkage/north-east-south-city.md"
  ],
  "testsAddedOrUpdated": [],
  "commandsRun": [
    {
      "command": "Read historical data.json; web_search workflow none; fetch_content readable/raw; read extracted official PDFs",
      "result": "passed",
      "summary": "Research tools executed; source-level retrieval failures retained explicitly. No shell, git, project edits, forms or restaurant communications."
    }
  ],
  "validationOutput": [
    "50 distinct named restaurant candidates; Hawksmoor counted only as Borough.",
    "Status count: 16 official-confirmed, 1 official-no, 2 third-party-only, 23 not-published, 8 inaccessible, 0 closed.",
    "Merchant references reuse 21 branch IDs; geographic and physical-retail caveats explicit.",
    "Supervisor supplied host-verified access date 2026-09-13 Europe/London."
  ],
  "residualRisks": [
    "Not all 50 records have complete fetched address, public email and cuisine/menu evidence.",
    "16 official-confirmed includes restricted/private/member/discretionary provisions and is not 16 unrestricted public BYO policies.",
    "Some pairings withheld or provisional; several merchant selections require wider travel and two Passione branches need take-away terms confirmed.",
    "Source webpages and promotions can change; no restaurant personally reconfirmed policy during this research."
  ],
  "noStagedFiles": true,
  "diffSummary": "Created research artifact only; no project/source or git actions.",
  "reviewFindings": [
    "high: historical data.json cabotte/chezbruce/trinity - official fees or conditions differ from historical records.",
    "high: north-east-south-city.md records 14/34/48 - restricted policy scopes must be preserved; record 41 expired-period PDF is not current general policy.",
    "medium: north-east-south-city.md merchant/contact/pairing sections - explicit retrieval and proximity gaps block publication-ready completeness."
  ],
  "manualNotes": "All 50 candidates retained, but broad user completeness requirements are only partially met. No git inspection was run because git actions were prohibited; noStagedFiles attests that this worker staged nothing, not the state of concurrent repository work."
}
```
