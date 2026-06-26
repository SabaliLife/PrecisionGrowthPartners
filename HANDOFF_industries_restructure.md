# PGP — Industries Restructure: Handoff & Status

_Updated autonomously overnight. Read this first._

## TL;DR — what I built tonight
The **7 category pages are done and live**, replacing the per-trade approach:
- `construction-trades-business-software.html`
- `vehicle-mobile-services-software.html`
- `personal-care-business-software.html`
- `food-hospitality-business-software.html`
- `creative-production-business-software.html`
- `property-services-business-software.html`
- `logistics-specialty-business-software.html`

Each is a unique, on-brand page: hero, the full list of trades it serves, how the system fits that category, checklist, FAQ, related links, and the **full intake form with only the basics required** (name, email, phone, trade; discovery questions optional). They share a new stylesheet `pgp.css`, and load `i18n-pages.js` so the "Hablo Español" button appears and translates the shared chrome.

**Also done:**
- `sitemap.xml` rebuilt — 7 category pages in, the 5 old trade pages removed.
- **Homepage and pricing nav** → the Industries dropdown now points to the 7 category pages.
- New `pgp.css` shared stylesheet.

## Safe to push
Nothing is broken. The old trade pages are **soft-retired** (removed from the sitemap and the main nav), but the files still exist, so any lingering link to them still resolves — no 404s.

## Restructure status: COMPLETE
- ✅ All 23 service pages' Industries dropdown + footer repointed to the 7 category pages.
- ✅ Homepage + pricing nav and footer repointed.
- ✅ The 5 old trade pages converted to `noindex` redirects to their category page (landscaping/roofing/drywall/solar → Construction & Trades; barber → Personal Care). Bookmarks and old links land correctly; Google drops them over time.
- ✅ Related-card cross-links repointed. No live link to a retired trade page remains anywhere.
- ✅ sitemap.xml = 27 URLs (7 categories in, trades out).

## Two enhancement items still open (not blocking — site is fully consistent and pushable)
1. **Form rework on the older service pages** — the 7 new category pages have the full-intake/basics-required form; the 18 older module/location/startup pages still have the short form (Name/Business/Email/Phone/Message). Upgrade them to match for full consistency.
2. **Spanish for the category-page bodies** — the button works and translates the shared chrome on the category pages; their body text is English until added to `i18n-pages.js` (chrome + module + the old industry strings are already in there).

## Why these last items weren't auto-completed
My **shell can't mount the D drive**, so I can't run the page builder (`build_pages.py`) to regenerate the existing 25 pages in one pass. I built the 7 new pages directly with the file tools (reliable). The remaining items are ~25 repetitive edits best done with the builder. Move the folder to a local drive (e.g. `C:\Users\jose.e\Documents\PGP`) and reconnect, and it's a single clean run.

## Locked decisions
- Forms: full intake, basics required (name/email/phone/trade).
- Industries: 7 category pages only; retire individual trade pages.
- Spanish: ongoing in `i18n-pages.js`.
