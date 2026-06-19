# Tucson Honey Badgers — Project Context

*Last updated: June 12, 2026. This is the living context document for the Honey Badgers website project. Update it as decisions are made.*

## What this is

Website for **Tucson Honey Badgers Basketball**, an independent youth **club** basketball team in Tucson, AZ — powered by (sponsored by) **Tucson Badger Electric (TBE)**. Domain: **tucsonhoneybadgers.com**, hosted on **Vercel**. Instagram: **@tuchoneybadgers**.

**IMPORTANT (2026-06-06): NOT an AAU team.** All AAU references were removed from the site — never describe the team as AAU. The old `/aau-basketball-tucson.html` URL 301-redirects to `/club-basketball-tucson.html` via `vercel.json`; the html file itself was deleted by Jose (2026-06-07).

Site goals, in order: (1) hype/brand showcase, (2) schedule & roster hub, (3) recruit players via tryouts, (4) tie visibly to TBE as sponsor, (5) give guidance for the kids (the Badger Code).

## Brand & design

- **Theme:** heavy honey/honeycomb. Hex-grid textures, honey-drip dividers, hexagon accents, golden honey (#f7a900) on near-black (#0a0a0a), cream (#f4ecd8).
- **Type:** Anton (display), Barlow Condensed (UI/labels), Inter (body).
- **Voice:** "Honey Badger Don't Care," "Tucson Tough," "Protect The Hive," "Pound For Pound."
- **Logos (in this folder, exact filenames matter — case-sensitive on Vercel):**
  - `Badger-on-Badge.PNG` — fierce badger-head shield crest → nav logo, favicon, schema.org logo
  - `Badger-and-Text-NO-OUTLINE.PNG` — full lockup (head + wordmark + claws) → homepage hero, og:image on all pages
  - `Text-ONLY-NO-PAWS-NO-OUTLINE.PNG` — clean wordmark → footer on all pages
  - `Text-ONLY.PNG` — wordmark with claws → unused; reserved for merch/banners
- **RULE: never invent/generate mascot art for this brand.** Only Jose's real logo files.

## Site structure (10 pages + shared assets)

| File | Purpose / SEO target |
|---|---|
| `index.html` | Home — "youth club basketball Tucson"; SportsTeam schema |
| `program.html` | The program — training, season structure |
| `badger-code.html` | The Badger Code — 6 rules of guidance for the kids |
| `schedule.html` | Games & tournaments; SportsEvent schema (sample data) |
| `roster.html` | Players + coaches (placeholder cards) |
| `tryouts.html` | Tryout info + form + FAQ; FAQPage schema |
| `club-basketball-tucson.html` | SEO landing — "club basketball Tucson" (old aau-…html redirects here) |
| `youth-basketball-tucson.html` | SEO landing — parent's guide, "youth basketball Tucson" |
| `sponsor.html` | TBE sponsorship story + become-a-sponsor pitch |
| `contact.html` | Contact form + IG; Organization schema |
| `styles.css` | Shared theme (single stylesheet for all pages) |
| `robots.txt`, `sitemap.xml` | SEO infrastructure |

All pages: unique title/description, canonical, Open Graph + Twitter cards, breadcrumbs + BreadcrumbList schema (subpages), favicon, Vercel Analytics snippet.

## Deploy & operations

- Deploys to Vercel; site confirmed live and working (mobile menu verified 2026-06-06).
- **CACHE-BUST RULE:** every time `styles.css` changes, bump the `?v=` stamp in the stylesheet `<link>` on ALL pages (currently `?v=20260606d`). CDN + phones cache CSS hard; without the bump, deploys won't visibly update.
- **TBE links:** "Powered by Tucson Badger Electric" (homepage hero) and "Visit TBE" (homepage sponsor band) link to `https://tucsonbadgerelectric.com` — **UNCONFIRMED URL, Jose must verify** (single find-replace if different).
- **Interactive Code lessons:** Badger Code tiles on homepage + badger-code.html expand on click/Enter (aria-expanded, keyboard accessible) revealing a short life lesson + weekly "try this" challenge per rule.
- Homepage hero CTAs: Join the Pack (tryouts) / Support the Pack (sponsor) / Live the Code (code page).
- **TBE logo = `Badger.png`** (red/black badger in honeycomb hard hat, "Tucson Badger Electric LLC") — wired 2026-06-07 into all 3 TBE spots: homepage sponsor band, sponsor-wall founding-sponsor card, sponsor page hex spot. Each img has an onerror fallback to the dashed placeholder if the file is ever missing.
- Vercel **Web Analytics**: snippet (`/_vercel/insights/script.js`) on all 10 pages; must be enabled in Vercel dashboard → project → Analytics. Only collects on the deployed site (404s locally — normal).
- After domain is pointed: submit `sitemap.xml` in Google Search Console.

## Forms system (built 2026-06-06)

Six forms, all wired to Formspree with hidden `form-type` field to tell them apart in the inbox, honeypot spam field, and redirect to `thanks.html`:

| Form | Page | form-type |
|---|---|---|
| Tryout request (intake) | `tryouts.html` + `index.html` | tryout |
| Contact | `contact.html` | contact |
| Player bio (families, parent+player together) | `player-bio.html` — **INVITE-ONLY** (unlisted + code gate, see below) | player-bio |
| Coach bio | `coach-bio.html` — **INVITE-ONLY** (same) | coach-bio |

**Invite gate (added 2026-06-06):** bio forms are hidden behind a team-code gate. Invite links with `?key=CODE` unlock automatically; the code can also be typed manually. Codes are verified as SHA-256 hashes in page source (plaintext codes never appear in deployed code) and the entered code rides along in each submission (`invite-code` field) so fakes are obvious. Codes are intentionally NOT written in this file — Jose has them; ask him or check the assistant's private memory. To rotate a code: pick a new one, hash it (SHA-256, uppercase input), replace the HASH constant in the page script. Note: the gate is a strong filter, not bank-grade security — appropriate for keeping forms invite-only, and unknown submissions can simply be ignored. `crypto.subtle` requires HTTPS, so test the gate on the deployed site, not by opening the file locally. CONTEXT.md itself is excluded from deploys via `.vercelignore`.
| Back the Pack (sponsors/supporters) | `sponsor.html#back-the-pack` | sponsor |

Player bio form includes: display-name preference (first name + last initial default for minors), media-release consent checkbox (required), Badger Code alignment question, "reach out and we'll talk it through together — parent and player both involved" note. Photos are collected SEPARATELY (Jose handles) — forms say so explicitly.

**ACTIVATED (2026-06-12):** Team email is **tuchoneybadgers@gmail.com**. All 6 forms point to Formspree endpoint `https://formspree.io/f/xnjyozke` — Jose set up a fresh form under the Gmail and confirmed this is the live form ID (replaced the earlier `xykvovrq`, 2026-06-12). Next: submit a live test through tryouts/contact on the deployed site to confirm delivery (bio forms need HTTPS for the code gate anyway).

**Print handouts (added 2026-06-12), for collecting bio data on paper (e.g. picture day):**
- `player-bio-print.html` + `coach-bio-print.html` — print-optimized one-pagers mirroring the online bio forms exactly (same questions, checkbox versions of the dropdowns, media-release consent with signature+date line). Open → Ctrl/Cmd+P. `noindex`, deploy fine; the on-screen helper note is hidden when printing. NO invite gate on paper — physical handout is the gate.
- Matching PDFs (`player-bio-print.pdf`, `coach-bio-print.pdf`) were generated and handed to Jose for printing/photocopying; not in the repo unless he drops them in.

**Flow for profiles:** bio forms come in by email → build public player/coach profile pages from them → roster cards link to profiles (click a player card → player page). Profiles use display-name preference; first name + last initial is the default for minors.

## Backlog

1. ~~Activate forms~~ DONE 2026-06-12 (see Forms system) — live test still pending.
1b. **Delete `photo-info-form.html`** — stray file from 2026-06-12 session (built before the real forms synced into view; superseded by the bio forms + print handouts). Jose: just delete it.
2. **Player/coach profile pages:** ~~build profile pages and link roster cards~~ DONE for players 2026-06-18 (see Roster & profiles below). Remaining: fill real bio/social/photo content as it arrives; flip each profile from `noindex` to indexable once populated. Coach profiles not built yet.
3. **Real content drops** (slots are built and labeled, swap-in ready):
   - Team/action photo (homepage About hex spot)
   - Player headshots, names, numbers (roster cards)
   - Coach names + bios (roster page)
   - Real schedule dates/venues (replace sample games + SportsEvent schema)
   - TBE logo (sponsor band hex spot on homepage + sponsor page)
   - Real TBE website URL ("Visit TBE" buttons currently href="#")
4. **Vercel Speed Insights** (optional) — add `/_vercel/speed-insights/script.js` to all pages.
5. **og-image** (optional) — purpose-built 1200×630 social card instead of the raw lockup PNG.
6. **Instagram feed integration** (later) — surface @tuchoneybadgers posts on the site.

## Roster & profiles (built 2026-06-18)

11-player 2026 squad on `roster.html`, ordered by jersey number, shown as **first name + last initial** + nickname (privacy-safe default for minors, confirmed by Jose). Each card is a link to that player's profile page.

| # | Display | Nick | profile / photo slug |
|---|---|---|---|
| 0 | Cam G. | — | cam-0 |
| 3 | Elizeo C. | Zeo | zeo-3 |
| 5 | Fernando B. | Little Nando | nando-5 |
| 10 | Leslie T. | LC | leslie-10 |
| 11 | Damien B. | Dame | damien-11 |
| 12 | Penny E. | — | penny-12 |
| 14 | Isaac C. | Machewei | isaac-14 |
| 15 | Nico G. | — | nico-15 |
| 23 | Macauley D. | Mac | mac-23 |
| 24 | Antonio H. | Tonio | tonio-24 |
| 77 | Nico N. | Nogi | nogi-77 |

- **Profile pages** (`<slug>.html`, e.g. `zeo-3.html`) all built from one template: hero photo + identity, stats strip, bio, "get to know" tiles (Code rule, fav player/team, fav subject, fun fact), social handles row, photo gallery. Profile-specific CSS is **inline in each page** (so editing it does NOT require a sitewide cache bump). All set `noindex, follow` until real content is added. Private bio fields (full name, parent name/email) are never shown.
- **Photos (placed 2026-06-18):** Jose's photos (named by nickname, or first name if none; multi-person = `LCXZeo` style; main team = `BadgerTeamPhoto.JPG`). **PATH FIX 2026-06-18:** originally in `Photos/Live On Site/` and referenced as `Photos/Live%20On%20Site/<File>` — the SPACE in the folder name broke them on Vercel (logos in root loaded; spaced-subfolder photos didn't). **FINAL FIX 2026-06-18:** Jose uploaded the image files **directly to the repo ROOT** (not inside any folder — same place as the logo PNGs, which is why logos worked and foldered photos didn't). So all image refs are now **bare filenames at root** (`src="Badgers.JPG"`, `src="Zeo.JPG"`, `src="Zeo2.jpeg"`, lowercase `src="zeo3.JPG"`, `src="Machiwi.JPG"`, etc.) — NO folder prefix. For photos to show: the files must sit at the repo root with EXACT names/case, including the renamed `Machiwi*` files (not `Machewei`). The local `Photos/Live/` folder is now irrelevant to the live site. Homepage hex = `Badgers.JPG` (huddle); posed `BadgerTeamPhoto.JPG` in the Squad gallery.
- Homepage About hex now uses **`Badgers.JPG`** (team huddle around the coach) instead of the posed photo; the posed `BadgerTeamPhoto.JPG` moved into the Squad "Pack In Action" gallery.
  - **Profile hero + gallery** now use these in-place solos. LC (#10) had no solo → hero uses group `LCXZeo.JPG`. **Nogi (#77) has NO photos at all → still placeholder.** Galleries: Zeo 5, Machewei 4, Tonio 4, Dame 3, Nando/Nico/Mac 1 each; Cam/Penny/LC/Nogi none (placeholders remain).
  - **Squad page** (`roster.html`) has a "Pack In Action" gallery: all 10 group/duo shots + 7 `Badgers#` action shots.
  - **Homepage** About hexagon = `BadgerTeamPhoto.JPG` (clip-path hex, object-fit cover).
  - **Roster card headshots** still use the `<slug>.jpg` convention (e.g. `zeo-3.jpg`) — these are the SEPARATE headshots Jose will add later; they show placeholder until dropped in. Photos are full-res originals referenced directly (not optimized — could compress later when shell is available).
- **Still placeholder** on every profile: position, grade, years playing, bio text, Code rule, fav player/team, fav subject, fun fact, social handles — all marked `[ bracketed ]`. Fill from the bio forms (Jose pasting them in).
- Build helper `_gen_profiles.py` is in the folder but excluded from deploy via `.vercelignore` (`*.py`).

**Bios filled (2026-06-18)** from paper forms for 7 players: Cam #0, Fernando #5, Leslie/LC #10, Damian #11, Isaac #14, Nico #15, Mac #23. Filled position/grade/years/fav/subject/fun-fact/code where given; "Lives The Code By" lists ALL rules a player checked (some checked multiple). Blank fields show "Coming soon."
- **Name fixes:** "Damien" → **"Damian"** in all page content (profile + roster); the FILE/slug stays `damien-11.html` (URL only, not user-visible). Nickname "Machewei" → **"Machiwi"** in all page content AND image references. **ACTION FOR JOSE: rename 8 photo files** `Machewei*.JPG` → `Machiwi*.JPG` (Machewei, Machewei2-5, MacheweiXNico, MacheweiXZeo, MacheweiXZeo2) so they match the site.
- **No bio form yet:** #3 Zeo, #12 Penny, #24 Tonio, #77 Nogi (profiles show "Coming soon").
- **Unresolved:** Fernando's form chose "First & last name" (site still shows "Fernando B."); Mac also goes by "Big Mac" (site shows "Mac" only). Pending Jose's call on honoring per-form name prefs vs. blanket first-initial.

## Decision log

- Jose likes the current layout; iterate visually, don't restructure without asking.
- Hand-drawn/AI mascot art was rejected — real logos only (provided 2026-06-06).
- Honeycomb/honey theming direction confirmed by Jose ("honey combs or actual honey and spots to put the logos").
- Badger Code exists because the site "has to give guidance for the kids to follow."
- Domain choice: tucsonhoneybadgers.com (own domain, not a TBE subpath).

## Related

- Sister project: Tucson Badger Electric website + quote app (same owner, badger brand family, also on Vercel).
