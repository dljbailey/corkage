# Research: Corkage Club — central and west London, 50-record investigation ledger

## Summary
This is a **research ledger, not a publishable list of 50 restaurants allowing corkage**. Ten restaurants have fetched official affirmative policies; three explicitly refuse corkage. Three candidates have closure evidence (of differing strength), and the remaining records need policy confirmation or further evidence.

**Access/check date for every restaurant and merchant below: 2026-09-13, Europe/London.** The supervising session verified its host clock at 19:41 BST. This is the date websites were checked, **not** the date a restaurant personally confirmed its policy. No restaurants or merchants were contacted, no forms submitted, and no project files or Git state changed.

## Scope and evidence rules
- Lane: West End/Westminster and west London. No Hawksmoor included. Existing IDs were read from `/Users/danielbailey/Documents/Code/corkage/data.json` as historical leads, not verification. All 12 requested existing records plus Maison François are retained.
- `official-confirmed`: affirmative policy actually retrieved from an official page or extracted PDF. `official-no`: explicit official refusal. `third-party-only`: affirmative third-party lead, explicitly distinguishing fetched text from search-only evidence. `not-published`: no policy located **within the identified accessible pages checked**, not a claim that no policy exists anywhere on the site. `inaccessible`: policy-bearing/branch information could not be adequately retrieved. `closed`: closure evidence described individually, not automatically official confirmation.
- Unknown fees mean **unknown**, never free. No mention does not mean permission. Private-event corkage and retailer-supplied wine are not automatically ordinary BYO permission.
- Unless a record identifies another source, cuisine, contact and address refer to its official URL. A dagger **†** means historical/search-only address evidence, **not fetched address proof**. Several pages suppress addresses/emails in readable extraction; public raw HTML was checked where useful.
- Short quotes below are exact passages from fetched content unless marked **search-only**. For records without a policy, the quote usually establishes cuisine or the public contact route; it is **not** a corkage quote.
- Merchant matches are editorial, ordered by specialist quality and sensible neighbourhood relation, **not an exhaustive top-three ranking**. No distances or walking times were calculated or claimed. Linked merchant IDs give the address and official branch evidence once.
- Pairings are **editorial wine-style suggestions**, not restaurant advice, current dishes guaranteed to be served, merchant stock, or permission to BYO. Where cuisine/menu evidence is insufficient, the gap is retained instead of inventing a menu.

## Counts
| Corkage status | Records | Count |
|---|---|---:|
| official-confirmed | 2, 3, 4, 6, 11, 13, 23, 24, 41, 45 | 10 |
| official-no | 26, 28, 36 | 3 |
| third-party-only | 10, 30, 43, 44, 50 | 5 |
| not-published, bounded to checked pages | 1, 8, 9, 12, 14–22, 25, 27, 29, 31, 33, 34, 37–40, 42, 48, 49 | 26 |
| inaccessible | 5, 32, 35 | 3 |
| closed / reported closed | 7, 46, 47 | 3 |
| **Total** | **1–50** | **50** |

**Important correction:** the not-published row contains 26 records; ranges are inclusive. Only ten affirmative policies are official-confirmed. This investigation does not deliver 50 active BYO venues. Research depth varies and is disclosed per record.

## Linked merchant directory

### M1 — Berry Bros. & Rudd, London Wine Shop
- **63 Pall Mall, London SW1Y 5HZ.** [Official wine-shop page](https://www.bbr.com/our-shops/the-wine-shop), fetched and read.
- Exact evidence: “Our fine wine shop at 63 Pall Mall is the destination for fine wines in London.” Address also printed explicitly.
- Selection rationale: fine-wine expertise and a dedicated fine-wine room; particularly sensible for St James’s, Piccadilly and southern Mayfair.
- **Do not substitute No. 1 St James’s Street:** the official directory distinguishes that as the spirits shop. Wine-shop page lists Sunday and Monday closed; check hours before planning a Sunday BYO dinner.

### M2 — Hedonism Wines, Mayfair
- **3–7 Davies Street, London W1K 3DJ.** [Official home](https://hedonism.co.uk/), raw HTML fetched; [official about page](https://hedonism.co.uk/hedonism-wines), read.
- Exact address text: “3 / 7 Davies Street” and “London W1K 3DJ”. Use the official postcode rather than conflicting third-party W1K 3LD.
- Rationale: deep fine-wine selection, provenance emphasis and specialist advisers; strongest fit for Mayfair and a wider central-London alternative.

### M3 — Amathus, Soho
- **Hammer House, 113–117 Wardour Street, London W1F 0UN.** [Official Soho store](https://www.amathusdrinks.com/b2c/soho-store), raw HTML fetched.
- Exact evidence: “Address: Hammer House, 113-117 Wardour Street, W1F 0UN”.
- Rationale: specialist wine and spirits retailer in Soho itself; practical first option for Soho, Covent Garden and southern Fitzrovia. The page warns in-store and online prices may differ.

### M4 — Philglas & Swiggot, Marylebone
- **22 New Quebec Street, London W1H 7SB.** [Official Marylebone URL](https://philglas-swiggot.com/pages/marylebone), raw HTML fetched.
- Public structured data identifies “Marylebone - Philglas & Swiggot”, “22 New Quebec Street”, “W1H 7SB”.
- Rationale: independent specialist choice for Marylebone; also an eastward alternative for Notting Hill rather than pretending it is in the same neighbourhood.
- Evidence limitation: address was recovered from public structured data rather than readable shop prose; recheck current hours separately.

### M5 — Jeroboams, Knightsbridge
- **56 Walton Street, London SW3 1RB.** [Official branch page](https://jeroboamstrade.co.uk/about-us/shops/knightsbridge/), readable and raw HTML fetched.
- Exact address printed; branch description: “along the border between Chelsea and Knightsbridge”.
- Rationale: fine-wine cellar and specialist service on the Chelsea/Knightsbridge border; convenient neighbourhood relation for Chelsea and South Kensington.
- **Freshness caveat:** this official trade-site page still carries Covid-era copy. Address is page-verified, but current trading/hours merit rechecking on the newer consumer site.

### M6 — Jeroboams, Belgravia / Elizabeth Street
- **50–52 Elizabeth Street, London SW1W 9PB.** [Official branch page](https://jeroboamstrade.co.uk/about-us/shops/victoria/), raw HTML fetched.
- Exact evidence: “50-52 Elizabeth Street” / “SW1W 9PB”. Description places it in Belgravia’s commercial heart.
- Rationale: specialist fine-wine option for Victoria/Pimlico and eastern Chelsea. Same official trade-page freshness caveat as M5.

### M7 — Jeroboams, Kensington
- **254 Kensington High Street, London W8 6ND.** [Official branch page](https://jeroboamstrade.co.uk/about-us/shops/high-street-kensington/), readable and raw fetched.
- Exact evidence: “254 Kensington High Street” / “W8 6ND”; prose describes a “carefully curated range of wines and spirits”.
- Rationale: Kensington first choice; useful eastward alternative for Hammersmith/Chiswick and southward alternative for Notting Hill. Same trade-page freshness caveat.

### M8 — Jeroboams, Holland Park
- **96 Holland Park Avenue, London W11 3RB.** [Official branch page](https://jeroboamstrade.co.uk/about-us/shops/holland-park/), raw fetched.
- Exact address printed. Description says the shop “majors in fine food, with a small but focused range of wines and spirits”.
- Rationale: neighbourhood relation to Notting Hill and Kensington. Rank below deeper wine specialists if buying a particularly rare bottle; not misrepresented as the group’s largest wine range. Same trade-page freshness caveat.

### M9 — The Good Wine Shop, Chiswick
- **84 Chiswick High Road, London W4 1SY.** [Official Chiswick page](https://www.thegoodwineshop.co.uk/pages/chiswick), readable and raw fetched.
- Exact address printed in HTML and store structured data. **Do not use an older Devonshire Road address.**
- Rationale: dedicated independent shop and wine advisers in Chiswick; first choice for Chiswick restaurants and a westward alternative for Hammersmith.

### M10 — Vindinista, Acton
- **74 Churchfield Road, London W3 6DH.** [Official home/store page](https://vindinista.com/), raw fetched.
- Exact evidence: “Our store” / “74 Churchfield Road, W3 6DH”.
- Rationale: strong independent alternative north of Chiswick in Acton; geographic relation stated rather than a fabricated journey time.

### Provisional merchant leads — not promoted to verified matches
- **P1 Lea & Sandeman, Chelsea:** 170 Fulham Road, SW10 9PR. [Official branch URL](https://www.leaandsandeman.co.uk/content/chelsea.html). Official search result supplied address; fetch 403. **Inaccessible, not fetched proof.** Potentially a better local option than more distant matches for Medlar/Bandol.
- **P2 Lea & Sandeman, Kensington:** 106 Kensington Church Street, W8 4BH. [Official branch URL](https://www.leaandsandeman.co.uk/content/kensington.html). Official search result supplied address; fetch 403. **Inaccessible.** Potentially particularly useful for Clarke’s.
- **P3 Lea & Sandeman, Chiswick:** 167 Chiswick High Road, W4 2DR. [Official branch URL](https://www.leaandsandeman.co.uk/content/chiswick.html). Readable extraction returned only generic footer; raw retrieval produced a browser challenge. **Address search-only, not verified.**
- The [L&S shop directory](https://www.leaandsandeman.co.uk/content/shops.html) also returned 403. These are real official-source leads, not invented branches, but they are deliberately separated from the ten page-verified directory records.

## Detailed numbered restaurant ledger

### 1. Parsons — Covent Garden
- **Existing ID:** `parsons`. **Address:** 39 Endell Street, WC2H 9BA. **Official:** https://www.parsonslondon.co.uk/ . The repository’s `thebirdinhandlondon.com` is not the correct Parsons website.
- **Cuisine/evidence:** British-Isles-inspired seafood. “We offer a wide range of seafood, freshly landed fish, as well as more classic fish dishes inspired from the British Isles and beyond.” [Home](https://www.parsonslondon.co.uk/).
- **Status:** `not-published`. Fee/restrictions unknown; historical £25 is not verified. Checked official home/about/menu landing/contact sections in readable and raw HTML; initial guessed `parsons.london` failed DNS and was replaced by the search-discovered correct site.
- **Public email:** `reservations@parsonslondon.co.uk`, literal mailto in [official home](https://www.parsonslondon.co.uk/).
- **Merchants, ranked:** [M3](#m3--amathus-soho) nearby Soho specialist; [M2](#m2--hedonism-wines-mayfair) broader Mayfair fine-wine choice; [M1](#m1--berry-bros--rudd-london-wine-shop) St James’s cellar expertise.
- **Editorial styles:** Muscadet sur lie for saline shellfish; restrained white Burgundy for richer roasted fish; dry Riesling for freshness without heavy oak.
- **Gap:** individual food/wine PDF links were not fully inspected; seek current permission and limits before bringing wine.

### 2. Noble Rot Soho — Soho
- **ID:** `noblerotsoho`. **Address:** 2 Greek Street, W1D 4NB. [Official branch](https://noblerot.co.uk/restaurant/soho).
- **Status:** `official-confirmed`. **£35 per 750ml; notify in advance.** Exact: “Corkage is £35 per 750ml. Just let us know in advance.” [Official FAQ](https://noblerot.co.uk/faq). No separately published magnum price or bottle cap located; do not carry forward old £25/£50 figures.
- **Cuisine:** European/French-leaning wine-led cooking. FAQ explicitly discusses roast chicken with morels and vin jaune; that is food evidence, not a promise of availability on the visit date.
- **Contact:** `soho@noblerot.co.uk`, [FAQ](https://noblerot.co.uk/faq).
- **Checked:** branch page and full FAQ. **Merchants:** [M3](#m3--amathus-soho), Soho locality; [M2](#m2--hedonism-wines-mayfair), fine-wine depth; [M1](#m1--berry-bros--rudd-london-wine-shop), St James’s alternative.
- **Editorial styles:** Jura Savagnin for the nutty/mushroom flavour family identified in FAQ; white Burgundy for roast poultry; mature Pinot Noir for earthy savoury cooking.

### 3. Noble Rot Mayfair — Shepherd Market
- **ID:** `noblerotmayfair`. **Address:** 5 Trebeck Street, W1J 7LT. [Official branch](https://noblerot.co.uk/restaurant/mayfair).
- **Status:** `official-confirmed`. **£35/750ml, advance notice**, using the group-wide [FAQ](https://noblerot.co.uk/faq): “Corkage is £35 per 750ml. Just let us know in advance.” No inferred magnum charge.
- **Cuisine:** modern European is the historical lead; the retrieved branch text did not expose a menu description. **Branch-specific menu evidence remains a gap**; Soho dishes must not be transferred here.
- **Contact:** `mayfair@noblerot.co.uk`, [FAQ](https://noblerot.co.uk/faq). **Checked:** branch page and FAQ.
- **Merchants:** [M2](#m2--hedonism-wines-mayfair), same wider Mayfair area and cellar depth; [M1](#m1--berry-bros--rudd-london-wine-shop), neighbouring St James’s; [M3](#m3--amathus-soho), Soho alternative.
- **Pairing gap:** obtain the Mayfair menu before writing food-specific pairings. White Burgundy and mature Pinot Noir are provisional style ideas only, not menu-grounded recommendations.

### 4. Kitchen W8 — Kensington
- **ID:** `kitchenw8`. **Address:** 11–13 Abingdon Road, W8 6AH. [Contact](https://www.kitchenw8.com/contact/).
- **Status:** `official-confirmed`. **£30/bottle; one per two guests, maximum four/booking; no Saturday evening corkage. Free Sunday evening**, except special events, Valentine’s Day and NYE, with same caps. Discuss BYO/glassware when reserving.
- **Exact:** “We offer corkage at £30 per bottle, with a limit of one bottle per two people, up to a maximum of 4 bottles per booking.” [Wine](https://www.kitchenw8.com/wine/).
- **Cuisine:** ingredient-led contemporary cooking; [about/home](https://www.kitchenw8.com/) names seasonal wild food including venison, game birds and chanterelles. **Contact:** `info@kitchenw8.com` (official contact).
- **Checked:** about, wine, contact. **Merchants:** [M7](#m7--jeroboams-kensington), same Kensington area; [M8](#m8--jeroboams-holland-park), Holland Park; [M5](#m5--jeroboams-knightsbridge), South Kensington/Knightsbridge alternative.
- **Editorial styles:** mature Pinot Noir for game birds and mushrooms; northern Rhône Syrah for venison; structured Chardonnay for richer fish preparations.

### 5. The Ledbury — Notting Hill
- **ID:** `ledbury`. **Address:** 127 Ledbury Road, W11 2AQ, recovered from [official raw home](https://www.theledbury.com/).
- **Status:** `inaccessible`. Historical £75 not verified. Readable home and [food/wine](https://www.theledbury.com/food-wine) failed as JavaScript-rendered; search-discovered `/contact` returned 404. Raw home recovered address/email but not policy.
- **Contact:** `info@theledbury.com`, literal mailto on official raw home. **Exact contact passage:** “127 Ledbury Road” / “Notting Hill” / “London, W11 2AQ”.
- **Cuisine:** contemporary tasting-menu dining is a historical lead; no usable current branch menu fetched. Do not claim its present dishes from memory.
- **Merchants:** [M8](#m8--jeroboams-holland-park), neighbouring Holland Park; [M7](#m7--jeroboams-kensington), Kensington wine specialist; [M4](#m4--philglas--swiggot-marylebone), farther east in Marylebone.
- **Gap:** policy, current food evidence and menu-grounded style pairings remain unresolved. No BYO recommendation yet.

### 6. Medlar — Chelsea
- **ID:** `medlar`. **Address:** 438 King’s Road, SW10 0LJ†; official contact search result and historical record agree, contact page not fetched. [Official](https://www.medlarrestaurant.co.uk/).
- **Status:** `official-confirmed`. **£20/75cl lunch; £40/75cl evening; no bottle limit; email in advance.** Exact: “We have no limits on how many bottles you can bring but we do like to know in advance”. [Wine](https://www.medlarrestaurant.co.uk/wine).
- **Cuisine:** “The style is French based but takes inspiration from all over.” [Food](https://www.medlarrestaurant.co.uk/food). Seasonal British/European ingredients.
- **Email:** `info@medlarrestaurant.co.uk`, explicitly provided on wine page. **Checked:** home, wine and food.
- **Merchants:** [M5](#m5--jeroboams-knightsbridge), Chelsea/Knightsbridge border; [M6](#m6--jeroboams-belgravia--elizabeth-street), eastward Belgravia alternative; [M7](#m7--jeroboams-kensington), northward Kensington. P1 would be a stronger locality candidate once accessible.
- **Editorial styles:** white Burgundy for French sauces and fish; Pinot Noir for lighter meat preparations; mature Bordeaux for more substantial meat courses, conditional on the menu chosen.

### 7. Bandol — Chelsea / Hollywood Road
- **ID:** `bandol`. **Address:** 6 Hollywood Road; SW10 9HU†. Historical official URL https://www.barbandol.co.uk/ failed DNS.
- **Status:** `closed` **(third-party report, not official confirmation)**. [Fetched Restaurant Guru](https://restaurantguru.com/Bandol-London) states “The spot is permanently closed.” Do not publish historical £25 corkage as current.
- **Cuisine:** French/Provençal historical offering; fetched directory says “The varied menu based on French cuisine”.
- **Email:** unknown; no public current restaurant email established. **Checked:** historical domain and one focused closure/contact search; fetched closure directory.
- **Area-only merchant matches, not a visit plan:** [M5](#m5--jeroboams-knightsbridge), Chelsea border; [M7](#m7--jeroboams-kensington), northward; [M6](#m6--jeroboams-belgravia--elizabeth-street), eastward.
- **Editorial historical styles:** dry Provençal rosé for Mediterranean seafood; Rolle/Vermentino for aromatic coastal cooking. Not a current dining recommendation.
- **Gap:** reliable official closure evidence and closure date.

### 8. Quo Vadis — Soho restaurant, not members’ club-only booking
- **ID:** `quovadis`. **Address:** 26–29 Dean Street, W1D 3LL† (official search result; old repository said 28–29). [Official](https://www.quovadissoho.co.uk/).
- **Status:** `not-published`, bounded to readable home and [restaurant](https://www.quovadissoho.co.uk/restaurant/). Menu URL returned 403. Historical £30 wine/£50 Champagne not verified.
- **Cuisine/evidence:** “The restaurants serve seasonal, regional British fare”; restaurant page describes smoked eel, oysters, pies and fish. [Home](https://www.quovadissoho.co.uk/).
- **Public email lead:** `reception@quovadissoho.co.uk`, official restaurant-page **search-only** result; not exposed in fetched readable text. `info@quovadissoho.co.uk` also official search-only. Treat email proof as incomplete.
- **Merchants:** [M3](#m3--amathus-soho), Soho; [M2](#m2--hedonism-wines-mayfair), Mayfair; [M1](#m1--berry-bros--rudd-london-wine-shop), St James’s.
- **Editorial styles:** dry Riesling for smoked eel’s richness; white Burgundy for fish/sauce; mature claret for savoury pies.

### 9. Lorne — Victoria / Pimlico
- **ID:** `lorne`. **Address:** 76 Wilton Road, SW1V 1DE, [menu/contact footer](https://www.lornerestaurant.co.uk/menu). [Official](https://lornerestaurant.co.uk/).
- **Status:** `not-published`. Historical £40 not verified. Checked home and menu landing; one focused search found only a **July 2019** special, rejected as expired.
- **Cuisine/evidence:** “A creative British restaurant with its eyes on well-sourced food and an emphasis on wine.” [Home](https://lornerestaurant.co.uk/).
- **Email:** `bookings@lornerestaurant.co.uk`, literal mailto on home; `info@lornerestaurant.co.uk` on menu footer.
- **Merchants:** [M6](#m6--jeroboams-belgravia--elizabeth-street), neighbouring Belgravia; [M5](#m5--jeroboams-knightsbridge), Chelsea/Knightsbridge; [M1](#m1--berry-bros--rudd-london-wine-shop), northward St James’s.
- **Editorial styles:** restrained Chardonnay for seasonal fish; Pinot Noir for lighter meat; dry Chenin for vegetable-led courses. Broad cuisine-led options, not assertions of current dishes.

### 10. Les 110 de Taillevent London — Marylebone / Cavendish Square
- **ID:** `taillevent`. **Address:** 16 Cavendish Square, W1G 9DD. [Official contact](https://www.les-110-taillevent-london.com/contact/).
- **Status:** `third-party-only`. Star Wine List **search-only** says “Corkage can be available at £50.” [Source](https://starwinelist.com/wine-place/Les-110-de-taillevent); fetch 403, so no fetched policy proof. Historical one-bottle/per-table restriction is not verified.
- **Cuisine:** “both classic and modern French dishes” [official home](https://les-110-taillevent-london.com/).
- **Email:** `les110.london@taillevent.com`, fetched official contact. Avoid copying the sommelier link blindly: visible sommelier email and its mailto destination disagree.
- **Checked:** official home/contact; focused search and attempted Star Wine List fetch.
- **Merchants:** [M4](#m4--philglas--swiggot-marylebone), Marylebone; [M2](#m2--hedonism-wines-mayfair), southward Mayfair; [M3](#m3--amathus-soho), Soho.
- **Editorial styles:** white Burgundy for French sauces; mature Bordeaux for meat; Champagne for a restrained opening pairing. Confirm BYO rather than assuming its extensive wine list implies permission.

### 11. La Trompette — Chiswick
- **ID:** `latrompette`. **Address:** 3–7 Devonshire Road, W4 2EU† (official search result and historical record). [Official](https://www.latrompette.co.uk/).
- **Status:** `official-confirmed`. **£25/75cl lunch; £50/75cl dinner; maximum four 75cl bottles or two magnums/table; optional 12.5% service excluded; tell restaurant when booking.** [Wine](https://www.latrompette.co.uk/wine/): “We allow corkage up to a maximum of four 75cl bottles (or two magnums) per table.”
- A separate official [special-offers](https://www.latrompette.co.uk/special-offers/) **search result** advertises Sunday-evening free corkage, one/person, max four/table, no combination with offers. **Fetch incomplete: do not count that promotion as fetched confirmation.**
- **Cuisine:** French-based contemporary cuisine remains a historical lead; food menu not retrieved. **Contact:** not required to resolve affirmative regular policy; email not independently established.
- **Checked:** home (incomplete), wine (read), special-offers (incomplete).
- **Merchants:** [M9](#m9--the-good-wine-shop-chiswick), Chiswick; [M10](#m10--vindinista-acton), Acton to the north; [M7](#m7--jeroboams-kensington), farther east in Kensington. P3 requires verification.
- **Pairing gap:** menu-specific evidence outstanding. White Burgundy and Pinot Noir are provisional cuisine-led styles, not verified menu pairings.

### 12. Mountain — Soho
- **ID:** `mountain`. **Address:** 16–18 Beak Street, W1F 9RD† (historical address; website title establishes Beak Street/Soho). [Official](https://www.mountainbeakstreet.com/).
- **Status:** `not-published`. Historical £30 not verified. Checked home, fully extracted 40-page [wine list](https://mountainbeakstreet.com/menu/mountain-wine-list.pdf), two-page [food menu](https://mountainbeakstreet.com/menu/mountain-food-menu.pdf), dated 1.9.2026.
- **Cuisine/evidence:** British produce, Spanish/Welsh influences and fire cooking; menu says “Wild, native fish and shellfish, sustainably caught by day boats”, and lists grilled meats, wood-fired rice and seasonal vegetables.
- **Email:** `bookings@mountainbeakstreet.com`, fetched home.
- **Merchants:** [M3](#m3--amathus-soho), Soho; [M2](#m2--hedonism-wines-mayfair), Mayfair; [M1](#m1--berry-bros--rudd-london-wine-shop), St James’s.
- **Editorial styles:** saline Albariño for shellfish; mature Rioja for grilled meat; lighter Mencía for smoke and vegetables without excessive tannin. These are styles, not assertions of retailer stock.

### 13. Maison François — St James’s
- **ID:** new. **Address:** 34 Duke Street, St James’s, SW1Y 6DF. [Official](https://www.maisonfrancois.london/).
- **Status:** `official-confirmed`. **Free Sunday dinner corkage from 16:00.** Exact: “We offer free corkage on Sunday night dinner reservations from 16:00”. [Home/reservations](https://www.maisonfrancois.london/).
- No ordinary-day charge, cap or list-overlap rule located; do not extrapolate Sunday permission to other services. Frank’s bar is not a separate candidate.
- **Cuisine:** French brasserie / deli and bar à vin; page describes brasserie dining and oysters. Full main-menu PDF not read.
- **Contact:** affirmative policy obtained; homepage prints `office@maisonfrancois.london` specifically for recruitment, **not presented as reservation email**.
- **Checked:** home/reservations/location and linked menu labels (PDFs not fetched).
- **Merchants:** [M1](#m1--berry-bros--rudd-london-wine-shop), St James’s; [M2](#m2--hedonism-wines-mayfair), Mayfair; [M3](#m3--amathus-soho), Soho. Buy before Sunday if using M1.
- **Editorial styles:** Champagne for oysters; white Burgundy for brasserie richness; medium-bodied Bordeaux for meat preparations, subject to the chosen menu.

### 14. Andrew Edmunds — Soho
- **ID:** new. **Address:** 46 Lexington Street, W1F 0LP. [Official FAQ](https://www.andrewedmunds.com/faq).
- **Status:** `not-published`. Fee/restrictions unknown. Checked home, FAQ, contact (raw); focused policy/contact search did not establish BYO.
- **Cuisine:** exact FAQ: “We serve seasonal Modern European food — sometimes described as Franco-Mediterranean bistro cooking”. FAQ names sustainable fish and game in season.
- **Email:** `enquiries@andrewedmunds.com` / `reservations@andrewedmunds.com` from official [contact search result](https://www.andrewedmunds.com/contact); page fetched raw but mailto evidence not extracted, so **email citation still search-only**.
- **Merchants:** [M3](#m3--amathus-soho), Soho; [M2](#m2--hedonism-wines-mayfair), Mayfair; [M1](#m1--berry-bros--rudd-london-wine-shop), St James’s.
- **Editorial styles:** mature Pinot Noir for game; Chenin Blanc for fish/vegetables; mature claret for richer meats. Excellent wine list does not establish outside-wine permission.

### 15. The 10 Cases — Bistrot & Cave à Vin, Covent Garden
- **ID:** new; counted as one venue, not padded into two. **Address:** 16–18 Endell Street, WC2H 9BD. [Official](https://www.10cases.co.uk/).
- **Status:** `not-published`. Fee/restrictions unknown. Checked home and [contact](https://www.10cases.co.uk/contact), including raw HTML. No BYO permission established.
- **Cuisine:** modern Franco-European bistrot cooking [home](https://www.10cases.co.uk/); exact contact identity: “The 10 Cases Bistrot & Cave à Vin”.
- **Email:** none established. **Public contact form exists** on contact page (name/email/subject/message fields), plus 020 7836 6801. Newsletter is not the enquiry form; nothing submitted.
- **Merchants:** [M3](#m3--amathus-soho), neighbouring Soho; [M2](#m2--hedonism-wines-mayfair), broader fine wine; [M1](#m1--berry-bros--rudd-london-wine-shop), St James’s.
- **Editorial styles:** cru Beaujolais for versatile bistro fare; Loire Chenin for food-friendly acidity; Chardonnay for richer fish/sauces.
- **Gap:** distinguish buying bottles in its own Cave from bringing externally purchased wine; do not confuse the two.

### 16. Ducksoup — Soho
- **ID:** new. **Address:** 41 Dean Street, W1D 4PY. [Visit](https://www.ducksoupsoho.co.uk/visit).
- **Status:** `not-published` on accessible home/visit pages. Food URL failed extraction; fee/limits unknown.
- **Cuisine quote:** “Informed by a love of unfussy mediterranean cooking and honest made wines.” [Home](https://www.ducksoupsoho.co.uk/).
- **Email:** `restaurant@ducksoupsoho.co.uk`, [visit](https://www.ducksoupsoho.co.uk/visit), fetched.
- **Merchants:** [M3](#m3--amathus-soho), Soho; [M2](#m2--hedonism-wines-mayfair), Mayfair; [M4](#m4--philglas--swiggot-marylebone), wider independent option in Marylebone.
- **Editorial styles:** fresh Vermentino for Mediterranean vegetables/fish; light, low-tannin red such as Frappato for varied small plates; restrained skin-contact white for herbaceous/vegetable dishes if flavours suit.

### 17. The French House — upstairs restaurant, Soho
- **ID:** new. **Address:** 49 Dean Street, W1D 5BG†; official search establishes 49 Dean Street, postcode remains a lead. Correct [official](https://www.frenchhousesoho.com/), not initial failed `thefrenchhousesoho.com`.
- **Status:** `not-published`. Fee/limits unknown. Home/restaurant text fetched after one focused search.
- **Exact:** “The upstairs restaurant room is open for lunch…”; “the menu changes daily”. [Official](https://www.frenchhousesoho.com/).
- **Email:** `enquiries@frenchhousesoho.com`, literal fetched mailto. **Do not use older search-result Gmail address when this current official address is available.**
- **Cuisine gap:** British/French reputation is a lead, but fetched page does not identify cuisine or dishes.
- **Merchants:** [M3](#m3--amathus-soho), same neighbourhood; [M2](#m2--hedonism-wines-mayfair), Mayfair; [M1](#m1--berry-bros--rudd-london-wine-shop), St James’s.
- **Pairing gap:** current sample menu required before food-specific suggestions; no invented dishes.

### 18. Bocca di Lupo — Soho
- **ID:** new. **Address:** 12 Archer Street, W1D 7BB. [Official](https://www.boccadilupo.com/), home read/raw.
- **Status:** `not-published`. Fee/limits unknown; home and focused search checked. Wine-list PDF discovered, not read.
- **Cuisine quote:** “stripped-down, honest regional Italian cuisine”; cuisine covers Italy’s twenty regions. [Home](https://www.boccadilupo.com/).
- **Email:** `info@boccadilupo.com`, official literal mailto.
- **Merchants:** [M3](#m3--amathus-soho), Soho; [M1](#m1--berry-bros--rudd-london-wine-shop), neighbouring St James’s; [M2](#m2--hedonism-wines-mayfair), Mayfair fine-wine range.
- **Editorial styles:** Verdicchio for regional seafood/vegetable cooking; Sangiovese for savoury tomato/meat combinations; mature Nebbiolo for richer northern-Italian-style courses, conditional on menu selection.

### 19. Gauthier Soho — Soho
- **ID:** new. **Address:** 21 Romilly Street, W1D 5AF. [Official](https://www.gauthiersoho.co.uk/).
- **Status:** `not-published`. No current fee/limits established. Checked home, raw home, `home.php`, [contact](https://www.gauthiersoho.co.uk/contact.php), focused search.
- **Cuisine:** vegan fine dining; fetched official title “Vegan Restaurant & Private Dining Rooms, London - Gauthier Soho”.
- **Email:** `info@gauthiersoho.co.uk`, fetched contact. Quote: “Email: info@gauthiersoho.co.uk”.
- **Merchants:** [M3](#m3--amathus-soho), Soho; [M2](#m2--hedonism-wines-mayfair), Mayfair; [M1](#m1--berry-bros--rudd-london-wine-shop), St James’s.
- **Editorial styles:** dry Chenin for vegetable texture; low-tannin Pinot Noir for earthy plant flavours; Champagne for light savoury courses. Ask for vegan-suitable fining/production if important: grape style alone does not certify vegan wine.

### 20. Portland — Fitzrovia
- **ID:** new. **Address:** 113 Great Portland Street, W1W 6QQ. [Official](https://www.portlandrestaurant.co.uk/).
- **Status:** `not-published`. Full long homepage includes menus, wine, reservations/contact, no policy located. Linked PDFs not all inspected; fee unknown.
- **Cuisine quote:** “the finest produce we can find cooked with precision and a high level of technique.” Contemporary fine dining, with wine explicitly central.
- **Email:** public **email link exists but extraction obfuscates the address** (`[email protected]` / Cloudflare encoding); plain address not independently recovered. Contact route: official email link or 020 7436 3261, not an inferred email.
- **Merchants:** [M4](#m4--philglas--swiggot-marylebone), westward Marylebone; [M2](#m2--hedonism-wines-mayfair), fine wine in Mayfair; [M3](#m3--amathus-soho), southward Soho.
- **Editorial styles:** restrained Chardonnay for nuanced fish/sauce preparations; Pinot Noir for lighter meat; dry Chenin for vegetable-led options. Menu-specific matching remains to do.

### 21. Clipstone — Fitzrovia
- **ID:** new. **Address:** 5 Clipstone Street, W1W 6BB. [Official](https://www.clipstonerestaurant.co.uk/).
- **Status:** `not-published`. Home and `/menus` readable output returned mainly restaurant/contact description; no permission established. Fee/limits unknown.
- **Exact:** “We are an intimate neighbourhood restaurant on a bright corner of Fitzrovia, established in 2016.” [Home](https://www.clipstonerestaurant.co.uk/).
- **Email:** `info@clipstonerestaurant.co.uk`, literal fetched mailto.
- **Cuisine gap:** contemporary European is a candidate lead; menu extraction insufficient to verify. Do not infer identical cooking from Portland/64 Goodge ownership.
- **Merchants:** [M4](#m4--philglas--swiggot-marylebone), Marylebone; [M2](#m2--hedonism-wines-mayfair), Mayfair; [M3](#m3--amathus-soho), Soho.
- **Pairing gap:** obtain readable menu before two or three menu-grounded styles.

### 22. 64 Goodge Street — Fitzrovia
- **ID:** new. **Address:** 64 Goodge Street, W1T 4NF. [Official](https://www.64goodgestreet.co.uk/).
- **Status:** `not-published`. Full home including food/wine/private dining/contact read; linked wine/menu PDFs not individually read. Fee/limits unknown.
- **Cuisine quote:** “classical French food cooked with a modern sensibility”. The page explicitly describes French sauces and a Burgundy-focused cellar.
- **Email:** `info@64goodgestreet.co.uk`, fetched home contact.
- **Merchants:** [M3](#m3--amathus-soho), southward Soho; [M2](#m2--hedonism-wines-mayfair), cellar depth; [M4](#m4--philglas--swiggot-marylebone), westward independent.
- **Editorial styles:** white Burgundy for rich but delicate sauces; mature Pinot Noir for savoury French cooking; Champagne for a lighter first-course pairing.

### 23. Pied à Terre — Fitzrovia
- **ID:** new. **Address:** 34 Charlotte Street, W1T 2NH† (official search/location lead; fetched food page mentions Charlotte Street, full postcode proof outstanding). [Official](https://www.pied-a-terre.co.uk/).
- **Status:** `official-confirmed`. **£55/75cl wine; sparkling £80/bottle; two bottles/table; expectation to purchase from wine list; unavailable on special occasions such as Valentine’s Day.**
- **Exact:** “A £55 corkage fee per 75cl bottle applies, with corkage limited to two bottles per table and the expectation that a purchase is also made from our wine list.” [Food and drink](https://www.pied-a-terre.co.uk/food-and-drink). Same fetched section states £80 sparkling.
- **Cuisine:** “modern British cuisine enriched with classic French techniques”; omnivore and plant-based menus.
- **Checked:** home and food/drink, focused search. **Email lead:** `reservations@pied-a-terre.co.uk`, official contact search-only; affirmative policy does not depend on email.
- **Merchants:** [M3](#m3--amathus-soho), southward Soho; [M4](#m4--philglas--swiggot-marylebone), westward Marylebone; [M2](#m2--hedonism-wines-mayfair), fine-wine depth.
- **Editorial styles:** refined white Burgundy for French technique/sauces; mature Pinot Noir for meat; dry Chenin for plant-based courses.

### 24. Trishna — Marylebone
- **ID:** new. **Address:** 15–17 Blandford Street, W1U 3DG. [Official](https://www.trishnalondon.com/), raw footer verified.
- **Status:** `official-confirmed`. **£40/75cl; maximum two bottles/reservation; no corkage in private room.** [Official FAQ PDF](https://www.trishnalondon.com/wp-content/uploads/2025/05/May-2025-Trishna-FAQ.pdf), fetched, extracted and read.
- **Exact:** “Guests are welcome to bring their bottle of wine at £40 per 75cl bottle, we allow two bottles of wine per reservation except of reservations in our private room where we do not allow corkage.”
- **Cuisine:** coastal Indian [home](https://www.trishnalondon.com/). **Email:** `info@trishnalondon.com`, raw official mailto.
- **Checked:** home readable/raw and one-page FAQ. PDF filename May 2025 means source age should be retained, not rewritten as restaurant-confirmed September 2026.
- **Merchants:** [M4](#m4--philglas--swiggot-marylebone), Marylebone; [M2](#m2--hedonism-wines-mayfair), southward Mayfair; [M3](#m3--amathus-soho), Soho.
- **Editorial styles:** off-dry Riesling for spice heat; Chenin Blanc for coastal dishes and sauces; restrained Pinot Noir where a red is wanted, avoiding high alcohol/tannin.

### 25. Jikoni — Marylebone, not Café Jikoni
- **ID:** new. **Address:** 19–21 Blandford Street, W1U 3DJ, raw official footer. [Official](https://www.jikonilondon.com/).
- **Status:** `not-published`. Home/event text/raw checked; current corkage fee/restrictions unknown. Its wine week is not a BYO policy.
- **Cuisine quote:** “inspired by immigrant cuisine and the rich, shared flavours and cultures across parts of South Asia & the Far East, the Middle East, East Africa and Britain”.
- **Email:** `contact@jikonilondon.com`, public official organisation structured data, not an inferred pattern.
- **Merchants:** [M4](#m4--philglas--swiggot-marylebone), Marylebone; [M2](#m2--hedonism-wines-mayfair), Mayfair; [M3](#m3--amathus-soho), Soho.
- **Editorial styles:** aromatic off-dry Riesling for spice; textured Chenin for layered sauces; fresh low-tannin Gamay for varied cross-cultural plates.

### 26. Chishuru — Fitzrovia
- **ID:** new. **Address:** 3 Great Titchfield Street, W1W 8AX. [Official](https://www.chishuru.com/).
- **Status:** `official-no`. Exact public contact modal: **“We do not offer corkage, sorry”**. [Official contact page](https://www.chishuru.com/contact), raw HTML read.
- **Cuisine quote:** “A modern west African restaurant”; site describes Yoruba heat, Igbo spices and Hausa fire cooking.
- **Contact:** official contact menu exists; no need to infer obfuscated email to overturn an explicit refusal.
- **Checked:** home and contact. **Merchants for separate purchases only:** [M3](#m3--amathus-soho), neighbouring Soho; [M2](#m2--hedonism-wines-mayfair), Mayfair; [M4](#m4--philglas--swiggot-marylebone), Marylebone.
- **Editorial styles, not BYO:** off-dry Riesling for heat; light chilled Gamay for fire-cooked flavours; Chenin Blanc for texture. Ask the restaurant’s team for something in these styles from its own list.

### 27. Orrery by Pierre Minotti — Marylebone
- **ID:** new. **Address:** 55 Marylebone High Street, W1U 5RB. [Official](https://orrery-restaurant.co.uk/).
- **Status:** `not-published`. Home, raw contact footer and [restaurant page](https://orrery-restaurant.co.uk/by-pierre-minotti/) checked; no fee/limits established.
- **Cuisine quote:** “Chef Pierre Minotti unites classical French technique with the finest British seasonal produce.” Restaurant page.
- **Email:** `OrreryReservations@evolvcollection.com`, literal official mailto. Do not reuse older D&D email addresses.
- **Merchants:** [M4](#m4--philglas--swiggot-marylebone), same wider Marylebone area; [M2](#m2--hedonism-wines-mayfair), Mayfair; [M3](#m3--amathus-soho), Soho alternative.
- **Editorial styles:** white Burgundy for classical sauces; mature Pinot Noir for delicacy; mature claret for richer meat courses, conditional on menu selection.

### 28. Caractère — Notting Hill
- **ID:** new. **Address:** 209 Westbourne Park Road, W11 1EA, official raw footer. [Official](https://www.caractererestaurant.com/).
- **Status:** `official-no`. **“We currently do not allow you to bring your own wine. This may change further down the line.”** [Official FAQ](https://www.caractererestaurant.com/faqs), fetched/read.
- **Cuisine:** classically trained contemporary cooking; home says the experience represents “their classical training”. Full French/Italian menu evidence remains to be read rather than assumed from the chefs’ backgrounds.
- **Email:** `contact@caractererestaurant.com`, official [info/directions](https://www.caractererestaurant.com/info-directions) search result; page fetched, email passage not independently extracted.
- **Checked:** home raw/readable, failed old `/find-us`, then FAQ and current info/directions.
- **Merchants for separate purchases:** [M8](#m8--jeroboams-holland-park), Holland Park; [M7](#m7--jeroboams-kensington), Kensington; [M4](#m4--philglas--swiggot-marylebone), farther east.
- **Pairing gap:** no current menu-grounded recommendations claimed. Corkage explicitly unavailable.

### 29. Core by Clare Smyth — Notting Hill
- **ID:** new. **Address:** 92 Kensington Park Road, W11 2PN†, official reservations/about search results; fetched home prose does not expose address. [Official](https://www.corebyclaresmyth.com/).
- **Status:** `not-published`. Home and one focused search reviewed, no current fee/limits. Menu/reservations links discovered but not all fetched.
- **Cuisine quote:** “We craft exquisite dishes using the best British produce from dedicated farmers and food producers.” [Home](https://www.corebyclaresmyth.com/).
- **Email lead:** `info@claresmyth.com`, official [reservations](https://corebyclaresmyth.com/reservations/) **search-only**, not an inferred `@core...` address.
- **Merchants:** [M8](#m8--jeroboams-holland-park), Holland Park; [M7](#m7--jeroboams-kensington), Kensington; [M4](#m4--philglas--swiggot-marylebone), Marylebone alternative.
- **Editorial styles:** refined Chardonnay for produce-led fish courses; mature Pinot Noir for lighter meats; dry Chenin for vegetable-focused cooking. Broad cuisine-based suggestions only.

### 30. Dorian — Notting Hill
- **ID:** new. **Address:** 105–107 Talbot Road, W11 2AT, fetched [home](https://www.dorianrestaurant.com/).
- **Status:** `third-party-only`. Fetched [National Restaurant Awards](https://www.nationalrestaurantawards.co.uk/profile/dorian/) says: **“the corkage policy – introduced in 2024 – allows one bottle per table, at £100.”** Current official fee not confirmed. Additional purchase condition mentioned in search synthesis was not in fetched passage and is not treated as verified.
- **Cuisine:** contemporary bistro, steaks/protein-led mains described in the same review; official calls itself “a bistro for locals”.
- **Email:** `reservations@dorianrestaurant.com`, literal official raw mailto.
- **Checked:** official home/raw; NRA review. Linked wine PDF not read.
- **Merchants:** [M8](#m8--jeroboams-holland-park), Holland Park; [M7](#m7--jeroboams-kensington), Kensington; [M4](#m4--philglas--swiggot-marylebone), Marylebone.
- **Editorial styles:** mature Bordeaux for steak; northern Rhône Syrah for roasted/grilled protein; Champagne for lighter starters. Obtain direct current policy before purchase.

### 31. Elystan Street — Chelsea
- **ID:** new. **Address:** 43 Elystan Street, SW3 3NT, [official contact](https://www.elystanstreet.com/contact/) raw metadata and visible address.
- **Status:** `not-published` on fetched raw wine/contact pages. Home readable extraction initially failed; [menus](https://www.elystanstreet.com/menus/) fetched successfully but menu PDFs not read. No BYO fee established.
- **Email:** `info@elystanstreet.com`, explicit contact meta-description, not inferred from obfuscated link.
- **Cuisine:** contemporary European is a lead; retrieved menu landing confirms à la carte, tasting and Sunday lunch but not dishes. Quote: “À LA CARTE MENU”.
- **Merchants:** [M5](#m5--jeroboams-knightsbridge), Chelsea/Knightsbridge; [M6](#m6--jeroboams-belgravia--elizabeth-street), Belgravia; [M7](#m7--jeroboams-kensington), Kensington.
- **Pairing gap:** read one of the dated official menus before food-specific style suggestions. Website silence is not permission.

### 32. Claude Bosi at Bibendum — South Kensington / Chelsea
- **ID:** new. **Address:** Michelin House, 81 Fulham Road, SW3 6RD†, NRA search result. Historical official chef site: https://claudebosi.com/ . Branch site https://www.bibendum.co.uk/ failed retrieval.
- **Status:** `inaccessible` for branch policy. Chef site now retrieves wider group/Brooklands content and cannot establish a Bibendum policy. `/bibendum` returned 404. Fee/limits unknown.
- **Cuisine:** fetched [NRA review](https://www.nationalrestaurantawards.co.uk/profile/claude-bosi-at-bibendum/) describes “Bosi’s immaculate French cooking”.
- **Public email:** `enquiries@claudebosi.com` appears literally in fetched chef site for events; **group/event route, not verified branch reservations**. `enquiries@bibendum.co.uk` is a third-party NRA search-only branch lead.
- **Merchants:** [M5](#m5--jeroboams-knightsbridge), Walton Street/Chelsea border; [M6](#m6--jeroboams-belgravia--elizabeth-street), Belgravia; [M7](#m7--jeroboams-kensington), Kensington.
- **Editorial styles:** mature white Burgundy for complex French sauces; mature Pinot Noir for delicate savoury cooking; Champagne for rich seafood-based starters. Based on third-party cuisine, not current menu proof.
- **Gap:** current branch operation/contact and policy require verification; do not attribute Brooklands terms here.

### 33. The Five Fields — Chelsea
- **ID:** new. **Address:** 8–9 Blacklands Terrace, SW3 2SP, fetched raw [reservations](https://www.fivefieldsrestaurant.com/reservations).
- **Status:** `not-published`. Homepage/landing and reservations checked; wine/menu links discovered but PDFs not read. Fee/limits unknown.
- **Cuisine:** modern British, seasonal, own kitchen garden. Official [home](https://www.fivefieldsrestaurant.com/home) search result says “modern British restaurant”; raw organisation data describes “hyper-seasonal sustainable dining”.
- **Email:** `info@fivefieldsrestaurant.com`, literal official reservations mailto.
- **Merchants:** [M5](#m5--jeroboams-knightsbridge), Chelsea border; [M6](#m6--jeroboams-belgravia--elizabeth-street), neighbouring Belgravia; [M7](#m7--jeroboams-kensington), Kensington.
- **Editorial styles:** dry Chenin for garden-led dishes; white Burgundy for richer fish; elegant Pinot Noir for seasonal meat courses. Exact current menu not claimed.

### 34. Sabor — Heddon Street, Mayfair
- **ID:** new. **Address:** 35–37 Heddon Street, W1B 4BR, raw [official home](https://www.saborrestaurants.co.uk/).
- **Status:** `not-published`. Home/about/reservation/contact sections read/raw; no corkage passage. Fee/limits unknown. Different dining areas not assumed to share unstated rules.
- **Cuisine quote:** “from the tapas bars of Andalucía through to the asadors of Castile and the seafood restaurants of Galicia”. Spanish regional cooking.
- **Email:** `info@saborrestaurants.co.uk`, literal official mailto.
- **Merchants:** [M2](#m2--hedonism-wines-mayfair), Mayfair; [M3](#m3--amathus-soho), neighbouring Soho; [M1](#m1--berry-bros--rudd-london-wine-shop), St James’s.
- **Editorial styles:** fino/manzanilla for salty tapas; Albariño for Galician-style seafood; mature Rioja for roast meats.

### 35. Gymkhana — Mayfair only
- **ID:** new. **Address:** 42 Albemarle Street, W1S 4JH†, candidate lead not independently fetched. [Official](https://www.gymkhanalondon.com/).
- **Status:** `inaccessible`. Official fetch returned 429; raw alternative returned browser-verification checkpoint, not restaurant content. Fee/limits unknown. Search results now mention multiple locations, so location selection matters.
- **Cuisine:** official **search-only** home describes “classic Indian cuisine”, North Indian-led with South/West influences. [Source](https://gymkhanalondon.com/).
- **Email:** unknown; no public branch email established from accessible evidence. Contact route: official website, retrieval unresolved.
- **Merchants:** [M2](#m2--hedonism-wines-mayfair), Mayfair; [M1](#m1--berry-bros--rudd-london-wine-shop), St James’s; [M3](#m3--amathus-soho), Soho.
- **Provisional editorial styles:** off-dry Riesling for spice; medium-bodied Syrah for robust tandoor/roast flavour families. These are based on search-only cuisine, **not fetched menu verification**.

### 36. Benares — Mayfair
- **ID:** new. **Address:** 12a Berkeley Square, W1J 6BS†, address proof outstanding. [Official](https://www.benaresrestaurant.com/).
- **Status:** `official-no`. Exact: **“Currently we do not offer a corkage service”**, followed by explanation of its wine list/sommelier team. [Official FAQ](https://benaresrestaurant.com/f-a-qs/), raw fetched/read.
- **Cuisine:** contemporary Indian; fetched official homepage title “Michelin-starred Indian Restaurant in Mayfair”.
- **Email:** `reservations@benaresrestaurant.co.uk`, explicitly in official FAQ public structured data.
- **Checked:** home and FAQ. **Merchants for other purchases only:** [M2](#m2--hedonism-wines-mayfair), Berkeley Square/Mayfair relation; [M1](#m1--berry-bros--rudd-london-wine-shop), St James’s; [M3](#m3--amathus-soho), Soho.
- **Editorial styles, restaurant list only:** off-dry Riesling for spice; Chenin for sauces; restrained Syrah for richer meat preparations. Not a BYO candidate under published rules.

### 37. Jamavar London — Mayfair
- **ID:** new. **Address:** 8 Mount Street, W1K 3NF, raw official footer. [Official London page](https://jamavarrestaurants.com/indian-restaurant-mayfair/) now canonicalises to `/london/`.
- **Status:** `not-published`. Home/London food and events overview plus raw page checked. Fee/limits unknown. Private venue LSL Privée’s third-party “flexible beverage policies” not transferred to this dining room.
- **Cuisine quote:** “regional Indian cuisine”; official page describes India’s palatial traditions and seasonal British ingredients.
- **Email:** unknown from checked pages; no public restaurant email recovered. Official website contact/booking route only; a newsletter is not an enquiry email.
- **Merchants:** [M2](#m2--hedonism-wines-mayfair), nearby Mayfair specialist; [M1](#m1--berry-bros--rudd-london-wine-shop), St James’s; [M4](#m4--philglas--swiggot-marylebone), northward Marylebone.
- **Editorial styles:** off-dry Riesling for aromatic spice; dry Chenin for sauce texture; supple Grenache blend for robust meat courses without extreme tannin.

### 38. Veeraswamy — Regent Street / Mayfair
- **ID:** new. **Address:** Mezzanine Floor, Victory House, 99 Regent Street, W1B 4RS, raw [official home](https://www.veeraswamy.com/).
- **Status:** `not-published`. Home/raw/contact FAQ checked; no BYO fee or limits established. Search results about lease uncertainty are not proof of closure.
- **Cuisine:** Indian palace traditions, including Hyderabadi and Mughal influences. Quote: “Experience the cuisine of India’s royal palaces, with a modern touch”. [Home](https://www.veeraswamy.com/).
- **Email:** unknown; [official contact](https://www.veeraswamy.com/contact/) gives FAQs and booking route but readable extract no public email. Not inferred.
- **Merchants:** [M3](#m3--amathus-soho), neighbouring Soho; [M1](#m1--berry-bros--rudd-london-wine-shop), St James’s; [M2](#m2--hedonism-wines-mayfair), Mayfair.
- **Editorial styles:** aromatic Riesling for spice; mature Syrah for slow-cooked lamb flavours described on site; textural Chenin for rich sauces.

### 39. HIDE — Piccadilly, Mayfair
- **ID:** new. **Address:** 85 Piccadilly, W1J 7NB, raw [official home](https://hide.co.uk/).
- **Status:** `not-published`. Ordinary customer BYO policy unknown. Home/raw plus focused search checked. **Access to Hedonism’s wines is not proof that an outside customer bottle is accepted.**
- **Cuisine:** contemporary fine dining is a candidate lead; readable homepage exposes little food detail. Current menu not read.
- **Email:** `reservations@hide.co.uk` and `info@hide.co.uk`, literal official home.
- **Exact contact evidence:** “please contact reservations on 0203 146 8666 or” linked reservation email.
- **Merchants:** [M2](#m2--hedonism-wines-mayfair), wine expertise and actual ownership relationship but no inferred BYO right; [M1](#m1--berry-bros--rudd-london-wine-shop), nearby St James’s; [M3](#m3--amathus-soho), Soho.
- **Pairing gap:** current official menu needs reading before menu-grounded wine styles; no dishes invented from reputation.

### 40. Wiltons — St James’s
- **ID:** new. **Address:** 55 Jermyn Street, SW1Y 6LX. [Official](https://www.wiltons.co.uk/).
- **Status:** `not-published`. Home/menu overview/contact read; no policy located; detailed PDFs not inspected. Fee/limits unknown.
- **Cuisine quote:** “the finest seafood & game since 1742”. [Home](https://www.wiltons.co.uk/).
- **Email:** `reserve@wiltons.co.uk`, literal fetched mailto.
- **Merchants:** [M1](#m1--berry-bros--rudd-london-wine-shop), St James’s; [M2](#m2--hedonism-wines-mayfair), Mayfair; [M3](#m3--amathus-soho), Soho.
- **Editorial styles:** Champagne for shellfish; white Burgundy for richer seafood; mature Pinot Noir for game. Existing wine-friendly reputation alone does not establish BYO.

### 41. Fallow — St James’s
- **ID:** new. **Address:** 52 Haymarket, SW1Y 4RP†, candidate address awaiting fetched official proof. [Official](https://fallowrestaurant.com/).
- **Status:** `official-confirmed`. **£50/75cl still wine; £90/75cl sparkling; only bottles absent from restaurant list. Premium fine wines charged at 50% of average value at management discretion; management may refuse corkage.**
- **Exact:** “For premium fine wines, we will charge 50% of the average value of the wine at the discretion of the management.” [FAQ](https://fallowrestaurant.com/faq/). **Do not advertise £50 as an unconditional ceiling.**
- **Cuisine quote:** “modern British cuisine” and “conscious usage of British produce”, same FAQ.
- **Email:** `info@fallowrestaurant.com`, official FAQ for private-hire enquiries; confirm correct reservation route for BYO valuation.
- **Checked:** FAQ and our-story. **Merchants:** [M1](#m1--berry-bros--rudd-london-wine-shop), St James’s; [M3](#m3--amathus-soho), Soho; [M2](#m2--hedonism-wines-mayfair), Mayfair.
- **Editorial styles:** medium-bodied Syrah for bold savoury flavours; Chardonnay for richer fish; bright Gamay for varied sharing plates.

### 42. Cavita — Marylebone
- **ID:** new. **Address:** 60 Wigmore Street, W1U 2RZ, raw [official home](https://www.cavitarestaurant.com/).
- **Status:** `not-published`. Home/raw contact and cuisine text checked; fee/limits unknown. **Policy-specific follow-up still outstanding**; do not misrepresent as exhaustive site review.
- **Cuisine quote:** “heritage mexican cuisine”. Site describes preserving Mexican traditions with contemporary expression.
- **Email:** `contact@cavitarestaurant.com`, literal raw official mailto.
- **Merchants:** [M4](#m4--philglas--swiggot-marylebone), Marylebone; [M2](#m2--hedonism-wines-mayfair), southward Mayfair; [M3](#m3--amathus-soho), Soho.
- **Editorial styles:** dry rosé for versatile savoury/spiced food; off-dry Riesling when chilli heat dominates; fresh Grenache for more substantial dishes. No particular current dish claimed.

### 43. Clarke’s — Kensington
- **ID:** new. **Address:** 124 Kensington Church Street, W8 4BH. [Official restaurant page](https://www.sallyclarke.com/restaurant/).
- **Status:** `third-party-only`. OpenTable London **search-only** listing includes “Corkage Fee”, no amount or restrictions. [Correct London listing](https://www.opentable.co.uk/r/clarkes-restaurant-london). No fetched affirmative policy; do not confuse with Clarke’s in Lake Oswego, Oregon.
- **Cuisine:** seasonal produce-led restaurant is a lead; fetched official page mainly reservations/testimonials, not current menu.
- **Email:** `restaurant@sallyclarke.com`, literal fetched mailto. **Checked:** official restaurant page plus one focused search.
- **Merchants:** [M7](#m7--jeroboams-kensington), Kensington; [M8](#m8--jeroboams-holland-park), Holland Park; [M5](#m5--jeroboams-knightsbridge), South Kensington/Knightsbridge. P2 potentially much more local once verified.
- **Pairing gap:** read a current food menu before food-specific styles. Provisional white Burgundy/Pinot Noir are not sufficient publication evidence.

### 44. The River Cafe — Hammersmith, north bank
- **ID:** new. **Address:** Thames Wharf, Rainville Road, W6 9HA, raw [official home](https://rivercafe.co.uk/).
- **Status:** `third-party-only`, **historical only**. Vinous 2021 search result says “we negotiated corkage for this occasion”; Standard 2018 mentions £30. Neither establishes a current ordinary policy or price. [Vinous](https://billing.vinous.com/articles/vinous-table-the-river-cafe-london-uk-oct-2021); [Standard](https://www.standard.co.uk/going-out/restaurants/fay-maschlers-week-in-food-from-maison-bab-to-the-river-cafe-a3946151.html). Search-only, not fetched article proof.
- **Cuisine:** official fetched page title “Iconic Italian restaurant in London since 1987”.
- **Email:** `info@rivercafe.co.uk`, literal raw official general-restaurant contact.
- **Checked:** home readable/raw and focused search. **Merchants:** [M9](#m9--the-good-wine-shop-chiswick), westward Chiswick; [M7](#m7--jeroboams-kensington), eastward Kensington; [M10](#m10--vindinista-acton), north-west Acton alternative.
- **Editorial styles:** Vermentino for Italian seafood/vegetable cooking; Sangiovese for savoury meat/pasta combinations; mature Nebbiolo for richer courses. Menu-dependent.
- **Rejected bad lead:** Reddit “River Cafe, 1A Station Approach SW6” is the wrong location and must not contaminate this record.

### 45. The Harwood Arms — Fulham
- **ID:** new. **Address:** Walham Grove, SW6 1QP†, candidate address not exposed in fetched home. [Official](https://harwoodarms.com/).
- **Status:** `official-confirmed`. **£40/75cl bottle; one bottle/person. Free Friday lunch only, excluding December.**
- **Exact:** “We allow one 75cl bottle of wine per person and charge £40.00 per bottle.” Followed by “We offer free corkage on Friday lunch only, excluding December”. [Home](https://harwoodarms.com/).
- **Cuisine quote:** “the very best British produce with a focus on game and wild food”.
- **Email:** `info@harwoodarms.com`, literal fetched mailto. **Checked:** full home including food/wine/corkage/reservations.
- **Merchants:** [M7](#m7--jeroboams-kensington), northward Kensington; [M5](#m5--jeroboams-knightsbridge), eastward Chelsea border; [M6](#m6--jeroboams-belgravia--elizabeth-street), farther east Belgravia. These are regional alternatives, not claimed nearest shops; local L&S Fulham branch needs separate verification.
- **Editorial styles:** mature Pinot Noir for game birds; northern Rhône Syrah for venison; mature claret for beef and richer game preparations.

### 46. Le Vacherin — Chiswick, closure lead retained
- **ID:** new. **Address:** 76–77 South Parade, W4 5LF†, historical candidate address awaiting fetched proof. [Official](https://www.levacherin.com/).
- **Status:** `closed` **(press report; official site still accessible and potentially stale)**. Fetched [Caterer URL](https://www.thecaterer.com/news/le-vacherin-restaurant-in-london-closes-after-24-years-of-trading) title: “Le Vacherin restaurant in London closes after 24 years of trading”. Article body was not available in useful extraction. June 2026 date is search-only, not independently read.
- [Old official promotions](https://www.levacherin.com/promotions-old/) search result mentions free Wednesday and Sunday-evening corkage with meal/bottle restrictions. **Expired/closure-conflicted lead, not a live offer.**
- **Cuisine:** French is historical lead; retrieved home not fully assessed for current food evidence. **Email:** unknown; do not infer one from its domain.
- **Checked:** official home; press title; ChiswickW4 closure URL returned frame-wrapper text only (not article proof).
- **Area-only merchants:** [M9](#m9--the-good-wine-shop-chiswick), Chiswick; [M10](#m10--vindinista-acton), neighbouring Acton; [M7](#m7--jeroboams-kensington), eastward alternative.
- **Pairings:** not a current dining recommendation. Historical French-style options such as Chardonnay and Pinot Noir are provisional and not menu-verified.

### 47. The Silver Birch — Chiswick, closure lead retained
- **ID:** new. **Former address:** 142 Chiswick High Road, W4 1PU†, third-party search-only. [Official historical domain](https://www.silverbirchchiswick.co.uk/).
- **Status:** `closed` **(closure message on official historical domain; integrity/date caveat)**. Raw HTML exact: “After many wonderful years, we have made the very difficult decision to close our doors at The Silver Birch.”
- Domain now canonicalises to `silverbirch-memorial.com`; structured closure date is 2024-03-14 but this conflicts with later dining-review evidence. **Do not report that date as verified; domain ownership/current authenticity deserves checking.**
- Historical Andy Hayler £35 corkage (2025) search lead is not current. [Review lead](https://www.andyhayler.com/restaurant/silver-birch).
- **Cuisine/email:** current cuisine unavailable; historical modern British and `info@silverbirchchiswick.co.uk` are third-party search-only leads, not current contacts.
- **Checked:** official domain readable failed, raw closure message read; focused search.
- **Area-only merchants:** [M9](#m9--the-good-wine-shop-chiswick), Chiswick; [M10](#m10--vindinista-acton), Acton; [M7](#m7--jeroboams-kensington), eastward Kensington.
- **Pairing gap:** no current menu, so no food-specific current pairings. Retain record for exclusion review, not publication.

### 48. Dove — Notting Hill, not the former Orasay
- **ID:** new. **Address:** 31 Kensington Park Road, W11 2EU. [Official info](https://dove.london/info/).
- **Status:** `not-published`. Correct non-www official home/info fetched after www failed. Fee/limits unknown.
- **Cuisine quote:** “serving elevated comfort food with seasonal British ingredients”. [Info](https://dove.london/info/).
- **Email:** `restaurant@dove.london`, literal fetched mailto. Do not transfer Orasay’s historical policy to the replacement concept.
- **Merchants:** [M8](#m8--jeroboams-holland-park), Holland Park; [M7](#m7--jeroboams-kensington), Kensington; [M4](#m4--philglas--swiggot-marylebone), eastward independent alternative.
- **Editorial styles:** bright Gamay for comfort-food richness; textured Chardonnay for creamy/fish preparations; savoury Pinot Noir for lighter meat courses, subject to actual menu.

### 49. Langan’s Brasserie — Mayfair
- **ID:** new. **Address:** Stratton Street, W1J 8LB, raw [official home](https://www.langansbrasserie.com/).
- **Status:** `not-published`. Home raw/readable and [menus](https://www.langansbrasserie.com/menus/) landing fetched; detailed menu PDFs not inspected. **Focused corkage search outstanding.** Fee/limits unknown.
- **Cuisine quote:** “British elegance respecting French tradition”. Brasserie with Sunday tradition referenced on home.
- **Email:** `info@langansbrasserie.com`, literal official footer mailto.
- **Merchants:** [M2](#m2--hedonism-wines-mayfair), Mayfair; [M1](#m1--berry-bros--rudd-london-wine-shop), neighbouring St James’s; [M3](#m3--amathus-soho), Soho.
- **Editorial styles:** Champagne for a brasserie opening; white Burgundy for classic sauces; mature Bordeaux for robust meat courses. These are cuisine-led, not specific current dishes.

### 50. Wild Honey St James — Westminster / Pall Mall
- **ID:** new. **Address:** 8 Pall Mall, SW1Y 5NG, raw [official home](https://www.wildhoneystjames.co.uk/), now canonical to `wildhoneystjames.com`.
- **Status:** `third-party-only`. OpenTable **search-only** listing says “BYO Wine” and “Corkage Fee”; no charge/restrictions established. [Listing](https://www.opentable.com/r/wild-honey-saint-james-london). Tagvenue’s private-event terms are not transferred to normal restaurant bookings.
- **Cuisine:** official FAQ describes modern European with British and French influences; seasonal daily-changing menus.
- **Email:** `Dining.StJames@sofitel.com`, fetched FAQ and raw footer. Quote: “you may contact us by email at Dining.stjames@sofitel.com”.
- **Checked:** official home/FAQ/raw, focused third-party search. Avoid copying questionable award chronology from marketing FAQ; not needed to establish cuisine.
- **Merchants:** [M1](#m1--berry-bros--rudd-london-wine-shop), same Pall Mall/St James’s area; [M3](#m3--amathus-soho), Soho; [M2](#m2--hedonism-wines-mayfair), Mayfair fine wine.
- **Editorial styles:** white Burgundy for French-influenced sauces; Pinot Noir for seasonal meat; dry Chenin for vegetable-led courses. Confirm current corkage before purchase.

## Review findings and residual work

### High severity — publication blockers
1. **`data.json` historical corkage fields are stale/unverified.** Official current page text differs materially for Noble Rot, Kitchen W8, Medlar and La Trompette. No project edits made.
2. **This artifact is not 50 affirmative policies.** Three refusals and three closure records must not become “allows BYO” cards. Only ten official-confirmed records exist in this lane’s evidence.
3. **Closure integrity:** Bandol is third-party-closed; Le Vacherin official menus conflict with press closure; Silver Birch domain shows closure with inconsistent date/canonical domain. Current active status needs independent checking before any publication.
4. **Merchant freshness:** four Jeroboams trade pages carry Covid-era content. Addresses are fetched official evidence, but current store operation/hours were not verified separately. L&S addresses remain search-only/inaccessible and are not used as verified matches.

### Medium severity — incomplete research fields
- Several records lack fetched address/postcode proof (marked †); a few public emails remain search-only, obfuscated, or unknown. Notably 10 Cases has a verified contact form; Gymkhana, Jamavar and Veeraswamy need usable contact evidence.
- Current food/menu evidence is insufficient for fully grounded pairings at Noble Rot Mayfair, The Ledbury, La Trompette, French House, Clipstone, Caractère, Elystan Street, HIDE, Clarke’s and closure records. These gaps are not filled with imagined dishes.
- Full menu/wine PDFs remain unreviewed for many not-published records. Status is explicitly bounded to pages checked. Cavita and Langan’s still need their focused policy follow-up; other shallow records may warrant one targeted policy/menu search in a future pass, not repeated retries of failed URLs.
- Star Wine List Taillevent fetch was blocked; its £50 is search-only. Clarke’s/Wild Honey OpenTable feature tags and historical River Cafe reports are weak leads, not current policy proof.
- M4’s address is public structured-data evidence; M5–M8 need freshness checks. Merchant rank is editorial neighbourhood suitability, not a distance calculation or claim to the definitive best three.

### Next manageable batch
1. Verify the ten official affirmative entries’ missing street/contact fields and source age; read missing branch food menus, especially Noble Rot Mayfair and La Trompette.
2. Ask for policy confirmation through the published restaurant contacts only **after separate outbound approval**. Do not send anything from this research task.
3. Resolve closure evidence and replace rejected/closed candidates if the parent needs 50 active high-quality restaurants rather than 50 investigated records. No replacement invented here just to reach the count.
4. Recover fresh L&S/Jeroboams consumer branch pages, then improve local merchant matches for Chelsea, Fulham and Notting Hill.

## Sources kept / dropped
- **Kept:** official restaurant FAQs, wine pages, raw visible contact text and public structured data; Trishna’s extracted official FAQ PDF; Mountain’s fully read food and wine PDFs; official merchant branch sources. These directly support specific fields.
- **Kept with warnings:** NRA Dorian/Bibendum for third-party policy/cuisine; Restaurant Guru for Bandol closure; Caterer fetched closure title for Le Vacherin; search-only Star Wine List and OpenTable leads, clearly not promoted to fetched policy proof.
- **Dropped:** old Lorne July 2019 promotion; old Le Vacherin offers as live availability; River Cafe Station Approach Reddit mismatch; Clarke’s Oregon results; LSL Privée event corkage as Jamavar policy; HIDE/Hedonism integration as customer BYO permission; inferred email formats/data-broker email suggestions; failed retrieval as evidence of a negative policy.
- **Discarded discovery errors:** unrelated or out-of-lane URLs encountered during discovery (including a casino page on the former Greenhouse domain and mistaken restaurant-domain guesses) supplied no ledger evidence and are not candidates. No Hawksmoor records investigated or included.

## Acceptance report
```acceptance-report
{
  "criteriaSatisfied": [
    {
      "id": "criterion-1",
      "status": "satisfied",
      "evidence": "Concrete 50-record ledger, ten linked page-verified merchant records plus three inaccessible merchant leads, status counts, exact evidence passages, and severity-labelled findings are saved in the configured central-west.md artifact. Incomplete fields are individually labelled rather than asserted complete."
    }
  ],
  "changedFiles": [
    "/Users/danielbailey/.pi/agent/sessions/--Users-danielbailey-Documents-Code--/subagent-artifacts/outputs/eb6b3f11-b526-412a-9510-e7003bddd4af/corkage/central-west.md"
  ],
  "testsAddedOrUpdated": [],
  "commandsRun": [],
  "validationOutput": [
    "Read historical data.json without editing it; retained all 12 requested existing records and Maison Francois.",
    "50 numbered records accounted for: 10 official-confirmed, 3 official-no, 5 third-party-only, 26 not-published within checked pages, 3 inaccessible, 3 closed/reported closed.",
    "Web searches used workflow none; official pages/raw HTML/PDFs fetched; no external messages or form submissions.",
    "Host date 2026-09-13 supplied by supervisor after clock verification.",
    "No executable tests applicable to research-only artifact; no Git commands run."
  ],
  "residualRisks": [
    "This is not a publishable directory of 50 active BYO restaurants; only ten policies officially confirmed.",
    "Several address/email fields remain historical, search-only, or unknown; current menus and food-grounded pairings incomplete for specified records.",
    "Four Jeroboams official trade pages are stale in presentation; three Lea and Sandeman branches inaccessible.",
    "Bandol and Le Vacherin closures lack direct restaurant confirmation; Silver Birch closure-domain/date integrity needs checking.",
    "Search-only third-party corkage leads and expired offers must not be treated as current permission.",
    "No restaurant personally contacted; policies can change after access date."
  ],
  "noStagedFiles": true,
  "diffSummary": "Research artifact only; no project/source edits, staging, commits or Git actions. Existing staging state was not inspected.",
  "reviewFindings": [
    "high: data.json - historical fees differ from newly fetched official Noble Rot, Medlar, Kitchen W8 and La Trompette policies; file deliberately not changed.",
    "high: central-west.md records 7, 26, 28, 36, 46, 47 - refusal/closure records must not be published as affirmative BYO venues.",
    "medium: central-west.md merchant directory M5-M8/P1-P3 - official page freshness/access limitations remain.",
    "medium: central-west.md ledger - marked address, public-email and menu/pairing gaps prevent claiming full field-level completion."
  ],
  "manualNotes": "Acceptance attests concrete research findings and preserved records, not full fulfilment of every desired field. noStagedFiles means this research staged nothing; existing repository staging was not inspected under the no-Git rule."
}
```
