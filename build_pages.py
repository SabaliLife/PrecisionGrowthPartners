# -*- coding: utf-8 -*-
"""Precision Growth Partners — SEO spoke-page generator.
Builds branded, fully-SEO'd service pages on the Tucson Badger Electric
hub-and-spoke pattern. Run from the PGP folder; writes .html files there.
"""
import os, re, html, json

ROOT = os.path.dirname(os.path.abspath(__file__))
SITE = "https://www.precisiongrowthpartnersaz.com"
EMAIL = "JoseOctavio@PrecisionGrowthPartnersAZ.com"
FORMSPREE = "https://formspree.io/f/mojbowww"
ORG_NAME = "Precision Growth Partners"
GEO = {"lat": "33.4484", "lon": "-112.0740", "region": "US-AZ", "place": "Phoenix, Arizona"}

# ---- Reuse the exact homepage stylesheet (brand tokens, fonts, nav, footer) ----
with open(os.path.join(ROOT, "index.html"), encoding="utf-8") as f:
    _idx = f.read()
_m = re.search(r"<style>.*?</style>", _idx, re.S)
BASE_STYLE = _m.group(0) if _m else "<style></style>"

# ---- Page-specific CSS appended after the base style ----
PAGE_CSS = """
<style>
  /* spoke-page components */
  .breadcrumb{max-width:1080px;margin:0 auto;padding:14px 28px 0;font-size:12.5px;color:var(--txt-dim)}
  .breadcrumb a{color:var(--accent)}
  .breadcrumb a:hover{text-decoration:underline}
  .sp-hero{background:radial-gradient(700px 400px at 80% -10%,#2a2320,transparent),var(--ink);
    color:#fff;padding:70px 0 64px;position:relative;overflow:hidden}
  .sp-hero h1{font-size:50px;max-width:780px;margin:12px 0 18px}
  .sp-hero p{font-size:17px;color:#c4c9d2;max-width:620px;margin-bottom:26px}
  .sp-meta{margin-top:22px;color:#8b929d;font-size:13px;letter-spacing:.5px}
  .statband{background:var(--ink-2);color:#fff;padding:0}
  .statband .wrap{display:grid;grid-template-columns:repeat(4,1fr);gap:1px;padding:0 28px}
  .stat{padding:30px 18px;text-align:center}
  .stat .n{font-family:'Barlow Condensed',sans-serif;font-size:34px;font-weight:700;color:var(--rose)}
  .stat .l{font-size:12.5px;color:#aeb4bd;letter-spacing:.5px;margin-top:4px}
  .feat-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(260px,1fr));gap:22px;margin-top:34px}
  .feat{background:var(--paper-2);border:1px solid var(--line);border-radius:12px;padding:26px}
  .feat h3{font-size:21px;margin-bottom:9px}
  .feat p{color:var(--txt-dim);font-size:14.5px}
  .feat .ix{font-family:'Barlow Condensed',sans-serif;color:var(--accent);font-weight:700;font-size:14px;letter-spacing:1px}
  .steps{display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:20px;margin-top:30px}
  .step{padding:22px;border-left:3px solid var(--rose);background:var(--paper-2)}
  .step .sn{font-family:'Barlow Condensed',sans-serif;font-size:26px;color:var(--rose);font-weight:700}
  .step h4{font-size:18px;margin:6px 0 6px}
  .step p{color:var(--txt-dim);font-size:14px}
  .checks{margin-top:24px;max-width:760px}
  .checks li{list-style:none;padding:10px 0 10px 30px;position:relative;border-bottom:1px solid var(--line);font-size:15px}
  .checks li:before{content:"\\2713";position:absolute;left:0;color:var(--rose);font-weight:700}
  .faq{max-width:820px;margin-top:18px}
  .faq details{border-bottom:1px solid var(--line);padding:16px 0}
  .faq summary{font-family:'Barlow Condensed',sans-serif;font-weight:700;font-size:19px;cursor:pointer;letter-spacing:.4px}
  .faq p{color:var(--txt-dim);font-size:14.5px;margin-top:10px}
  .related{background:var(--ink);color:#fff}
  .related .sec-title{color:#fff}
  .rel-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:16px;margin-top:26px}
  .rel-card{display:block;background:var(--ink-2);border:1px solid #2a2e36;border-radius:10px;padding:20px;color:#fff;transition:border-color .15s}
  .rel-card:hover{border-color:var(--accent)}
  .rel-card .rt{font-family:'Barlow Condensed',sans-serif;font-weight:700;font-size:18px}
  .rel-card .rd{color:#aeb4bd;font-size:13px;margin-top:6px}
  .cta-band{background:var(--grad-rose);color:#fff;text-align:center}
  .cta-band h2{font-size:34px;color:#fff;margin-bottom:10px}
  .cta-band p{max-width:560px;margin:0 auto 22px;font-size:16px}
  .cta-band .btn-lg{background:#14171b;color:#fff}
  .lead{max-width:620px;background:var(--paper-2);border:1px solid var(--line);border-radius:14px;padding:30px;margin-top:30px}
  .lead .fr{display:grid;grid-template-columns:1fr 1fr;gap:14px}
  .lead label{display:block;font-size:12.5px;color:var(--txt-dim);margin-bottom:5px;font-weight:600}
  .lead input,.lead select,.lead textarea{width:100%;padding:11px;border:1px solid var(--line);border-radius:8px;
    font-family:inherit;font-size:14px;background:#fff;margin-bottom:14px}
  .lead button{width:100%;background:var(--grad-teal);color:#fff;border:0;padding:14px;border-radius:9px;
    font-weight:700;font-size:15px;cursor:pointer;font-family:'Barlow Condensed',sans-serif;letter-spacing:.5px}
  .lead .note{font-size:12px;color:var(--txt-dim);margin-top:10px;text-align:center}
  .foot-cols{display:grid;grid-template-columns:repeat(auto-fit,minmax(150px,1fr));gap:26px;
    padding:14px 0 30px;border-top:1px solid #2a2e36;margin-top:24px}
  .foot-cols h5{font-family:'Barlow Condensed',sans-serif;font-size:14px;letter-spacing:1px;color:#fff;margin-bottom:12px;text-transform:uppercase}
  .foot-cols a{display:block;color:#aeb4bd;font-size:13px;padding:4px 0}
  .foot-cols a:hover{color:#fff}
  @media(max-width:760px){
    .sp-hero h1{font-size:34px}
    .statband .wrap{grid-template-columns:repeat(2,1fr)}
    .lead .fr{grid-template-columns:1fr}
  }
</style>
"""

NAV = """<nav>
  <div class="nav-in">
    <a href="index.html"><img class="logo-img" src="pgp-logo.png" alt="Precision Growth Partners"></a>
    <button type="button" class="hamburger" id="hamburger" onclick="document.getElementById('nav-links').classList.toggle('open')" aria-label="Menu">
      <span></span><span></span><span></span>
    </button>
    <div class="nav-links" id="nav-links">
      <a href="index.html#how-we-help">How We Help</a>
      <a href="index.html#what">What We Build</a>
      <a href="index.html#industries">Industries</a>
      <a href="index.html#projects">Projects</a>
      <a href="pricing.html">Partnership Structures</a>
      <a href="#quote" class="nav-cta">Book a Demo</a>
    </div>
  </div>
</nav>"""

def footer(active=None):
    def links(items):
        return "".join(f'<a href="{u}">{html.escape(t)}</a>' for t, u in items)
    solutions = [("Quoting & Sales", "quote-and-win-software.html"),
                 ("Inventory & Operations", "inventory-operations-software.html"),
                 ("Job Costing & Profit", "job-costing-software.html"),
                 ("Operating Playbook", "business-operations-playbook.html")]
    industries = [("Electrical Contractors", "electrical-contractor-software.html"),
                  ("Landscaping", "landscaping-business-software.html"),
                  ("Roofing", "roofing-business-software.html"),
                  ("Drywall", "drywall-contractor-software.html"),
                  ("Solar", "solar-installer-software.html"),
                  ("Barber & Salon", "barber-salon-software.html")]
    locations = [("Arizona", "small-business-software-arizona.html"),
                 ("Phoenix", "phoenix-small-business-help.html"),
                 ("Tucson", "tucson-small-business-help.html")]
    company = [("Start a Business", "start-a-contracting-business-arizona.html"),
               ("Startup Help", "small-business-startup-help-arizona.html"),
               ("Partnership Structures", "pricing.html"),
               ("Home", "index.html")]
    return f"""<footer>
  <div class="wrap">
    <div class="foot-row">
      <div class="foot-brand">
        <div class="foot-name">PRECISION GROWTH PARTNERS</div>
        <div class="foot-tag">Built honest. Built precise.</div>
      </div>
      <div class="foot-contact">
        <div class="foot-loc">Phoenix, Arizona &mdash; Serving Arizona and beyond</div>
        <div class="foot-email"><a href="mailto:{EMAIL}">{EMAIL}</a></div>
      </div>
    </div>
    <div class="foot-cols">
      <div><h5>Solutions</h5>{links(solutions)}</div>
      <div><h5>Industries</h5>{links(industries)}</div>
      <div><h5>Locations</h5>{links(locations)}</div>
      <div><h5>Company</h5>{links(company)}</div>
    </div>
    <div class="foot-base">
      <span>&copy; 2026 Precision Growth Partners &mdash; Phoenix, Arizona</span>
    </div>
  </div>
</footer>"""

def head(p):
    """Build the full <head> for a page from its content dict."""
    url = f"{SITE}/{p['slug']}"
    desc = html.escape(p["desc"], quote=True)
    title = html.escape(p["title"], quote=True)
    img = f"{SITE}/pgp-logo.png"
    # ---- JSON-LD @graph: Organization (shared) + Service + Breadcrumb + FAQ ----
    org = {
        "@type": ["Organization", "ProfessionalService"],
        "@id": f"{SITE}/#org",
        "name": ORG_NAME,
        "url": SITE + "/",
        "email": EMAIL,
        "logo": img,
        "image": img,
        "slogan": "Built honest. Built precise.",
        "description": ("Precision Growth Partners builds complete digital operating systems for small "
                        "contractors, service businesses, and startups — quoting, inventory, scheduling, "
                        "job costing, and the playbook to run it."),
        "areaServed": [{"@type": "State", "name": "Arizona"},
                       {"@type": "City", "name": "Phoenix"},
                       {"@type": "City", "name": "Tucson"}],
        "address": {"@type": "PostalAddress", "addressRegion": "AZ",
                    "addressLocality": "Phoenix", "addressCountry": "US"},
        "geo": {"@type": "GeoCoordinates", "latitude": GEO["lat"], "longitude": GEO["lon"]},
    }
    service = {
        "@type": "Service",
        "@id": url + "#service",
        "name": p["title"].split(" | ")[0],
        "serviceType": p.get("svc_type", "Business operations software & consulting"),
        "description": p["desc"],
        "provider": {"@id": f"{SITE}/#org"},
        "areaServed": {"@type": "State", "name": "Arizona"},
        "url": url,
    }
    crumbs = {
        "@type": "BreadcrumbList",
        "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "Home", "item": SITE + "/"},
            {"@type": "ListItem", "position": 2, "name": p["crumb"], "item": url},
        ],
    }
    graph = [org, service, crumbs]
    if p.get("faq"):
        graph.append({
            "@type": "FAQPage",
            "@id": url + "#faq",
            "mainEntity": [{"@type": "Question", "name": q,
                            "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in p["faq"]],
        })
    ld = json.dumps({"@context": "https://schema.org", "@graph": graph}, ensure_ascii=False, indent=1)
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="{url}">
<meta name="robots" content="index, follow">
<meta name="author" content="{ORG_NAME}">
<meta name="geo.region" content="{GEO['region']}">
<meta name="geo.placename" content="{GEO['place']}">
<meta name="geo.position" content="{GEO['lat']};{GEO['lon']}">
<meta name="ICBM" content="{GEO['lat']}, {GEO['lon']}">
<meta property="og:type" content="website">
<meta property="og:site_name" content="{ORG_NAME}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{img}">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{title}">
<meta name="twitter:description" content="{desc}">
<meta name="twitter:image" content="{img}">
<link rel="icon" type="image/png" href="pgp-logo.png">
<link href="https://fonts.googleapis.com/css2?family=Barlow+Condensed:wght@500;600;700&family=Inter:wght@400;500;600&display=swap" rel="stylesheet">
{BASE_STYLE}
{PAGE_CSS}
<script type="application/ld+json">
{ld}
</script>
</head>
<body>"""


def render(p):
    feats = "".join(
        f'<div class="feat"><div class="ix">{html.escape(ix)}</div><h3>{html.escape(t)}</h3><p>{html.escape(d)}</p></div>'
        for ix, t, d in p["features"])
    steps = "".join(
        f'<div class="step"><div class="sn">{i+1:02d}</div><h4>{html.escape(t)}</h4><p>{html.escape(d)}</p></div>'
        for i, (t, d) in enumerate(p["steps"]))
    checks = "".join(f"<li>{html.escape(c)}</li>" for c in p["checks"])
    faq = "".join(
        f'<details><summary>{html.escape(q)}</summary><p>{html.escape(a)}</p></details>'
        for q, a in p.get("faq", []))
    rels = "".join(
        f'<a class="rel-card" href="{u}"><div class="rt">{html.escape(t)}</div><div class="rd">{html.escape(d)}</div></a>'
        for t, d, u in p["related"])
    stats = "".join(
        f'<div class="stat"><div class="n">{html.escape(n)}</div><div class="l">{html.escape(l)}</div></div>'
        for n, l in p["stats"])
    faq_block = f"""<section><div class="wrap"><div class="sec-kicker">Questions</div>
      <h2 class="sec-title">{html.escape(p['faq_title'])}</h2>
      <div class="faq">{faq}</div></div></section>""" if faq else ""
    return f"""{head(p)}
{NAV}
<div class="breadcrumb"><a href="index.html">Home</a> &nbsp;/&nbsp; {html.escape(p['crumb'])}</div>
<header class="sp-hero">
  <div class="wrap">
    <div class="kicker">{html.escape(p['kicker'])}</div>
    <h1>{p['h1']}</h1>
    <p>{html.escape(p['sub'])}</p>
    <div class="hero-btns">
      <a href="#quote" class="btn-lg">Book a Working Demo</a>
      <a href="#how" class="btn-out">See How It Works</a>
    </div>
    <div class="sp-meta">{html.escape(p['meta_line'])}</div>
  </div>
</header>
<section class="statband"><div class="wrap">{stats}</div></section>
<section>
  <div class="wrap">
    <div class="sec-kicker">{html.escape(p['s1_kicker'])}</div>
    <h2 class="sec-title">{html.escape(p['s1_title'])}</h2>
    <p class="sec-intro">{html.escape(p['s1_intro'])}</p>
    <div class="feat-grid">{feats}</div>
  </div>
</section>
<section id="how" style="background:var(--paper-2)">
  <div class="wrap">
    <div class="sec-kicker">How It Works</div>
    <h2 class="sec-title">{html.escape(p['steps_title'])}</h2>
    <div class="steps">{steps}</div>
  </div>
</section>
<section>
  <div class="wrap">
    <div class="sec-kicker">{html.escape(p['checks_kicker'])}</div>
    <h2 class="sec-title">{html.escape(p['checks_title'])}</h2>
    <ul class="checks">{checks}</ul>
  </div>
</section>
{faq_block}
<section class="related">
  <div class="wrap">
    <div class="sec-kicker">Explore More</div>
    <h2 class="sec-title">Related solutions</h2>
    <div class="rel-grid">{rels}</div>
  </div>
</section>
<section class="cta-band" id="quote">
  <div class="wrap">
    <h2>{html.escape(p['cta_title'])}</h2>
    <p>{html.escape(p['cta_sub'])}</p>
    <form class="lead" action="{FORMSPREE}" method="POST">
      <input type="hidden" name="_subject" value="New inquiry — {html.escape(p['crumb'])} — Precision Growth Partners">
      <input type="hidden" name="Source Page" value="{html.escape(p['crumb'])}">
      <div class="fr">
        <div><label>Name</label><input name="Name" type="text" required></div>
        <div><label>Business</label><input name="Business" type="text"></div>
      </div>
      <div class="fr">
        <div><label>Email</label><input name="Email" type="email" required></div>
        <div><label>Phone</label><input name="Phone" type="tel"></div>
      </div>
      <label>What do you want to fix or build?</label>
      <textarea name="Message" rows="3"></textarea>
      <button type="submit">Book a Working Demo &rarr;</button>
      <div class="note">We respond within one business day. No spam, ever.</div>
    </form>
  </div>
</section>
{footer()}
</body>
</html>"""


# Cross-link helpers
R = {
 "quote": ("Quoting & Sales Software", "Win more work with fast, professional quotes that protect your margin.", "quote-and-win-software.html"),
 "inv":   ("Inventory & Operations", "Materials, scheduling, and purchasing planned off your real job pipeline.", "inventory-operations-software.html"),
 "cost":  ("Job Costing & Profit", "See what every job actually made — and tighten the next quote.", "job-costing-software.html"),
 "play":  ("The Operating Playbook", "Run by the numbers: hiring, pricing, cash, and growth milestones.", "business-operations-playbook.html"),
 "elec":  ("Electrical Contractors", "The system behind our first live build, Tucson Badger Electric.", "electrical-contractor-software.html"),
 "land":  ("Landscaping", "Quote, route, and cost recurring and project landscaping work.", "landscaping-business-software.html"),
 "roof":  ("Roofing", "Material-heavy, multi-stage roofing jobs, run start to finish.", "roofing-business-software.html"),
 "dry":   ("Drywall", "Bid by the board, track production, and stop guessing on materials.", "drywall-contractor-software.html"),
 "solar": ("Solar", "Design-to-PTO workflow with permits, inventory, and milestones.", "solar-installer-software.html"),
 "barber":("Barber & Salon", "Appointments, supplies, and per-chair numbers in one place.", "barber-salon-software.html"),
 "az":    ("Arizona Small Business Systems", "Operating systems built for Arizona operators.", "small-business-software-arizona.html"),
 "phx":   ("Phoenix Small Business Help", "Hands-on systems and guidance for Phoenix-area owners.", "phoenix-small-business-help.html"),
 "tuc":   ("Tucson Small Business Help", "Local systems support across the Tucson metro.", "tucson-small-business-help.html"),
 "start": ("Start a Contracting Business", "Stand up your business on real systems from day one.", "start-a-contracting-business-arizona.html"),
 "startup":("Small Business Startup Help", "From idea to first invoice with the right foundation.", "small-business-startup-help-arizona.html"),
}

PAGES = [
# ============================== MODULE / OFFERING ==============================
{
 "slug":"quote-and-win-software", "crumb":"Quoting & Sales Software",
 "title":"Quoting & Sales Software for Contractors | Precision Growth Partners",
 "desc":"Build fast, professional, margin-protected quotes and track every deal. Quoting and sales software for small contractors and service businesses in Arizona.",
 "svc_type":"Quoting & sales operations software",
 "kicker":"Quote & Win", "h1":'Quote fast. Win clean. <span class="accent">Protect your margin.</span>',
 "sub":"A quoting and sales workspace built for small operators: itemized quotes off real material and labor costs, a quote log that tells you what you win and lose, and the numbers to never underbid a job again.",
 "meta_line":"Module 01 of the PGP operating system · Phoenix, Arizona",
 "stats":[("<2 min","To a sent quote"),("100%","Itemized to cost"),("0","Margin guesswork"),("1","Source of truth")],
 "s1_kicker":"What it does","s1_title":"Bidding that defends your profit",
 "s1_intro":"Most small operators quote from memory or a shoebox of old invoices. This replaces that with a system that prices off your actual materials, labor hours, and target margin.",
 "features":[("01","Itemized quote builder","Pull services and materials with real unit costs and labor standards. Every line ties to a number you can defend to the customer and to yourself."),
             ("02","Margin targets, enforced","Set the markup and target margin once. The quote shows you the moment a job slips below where it needs to be."),
             ("03","Quote log & win/loss","Every quote is logged with status. See your real close rate and a lost-reason breakdown — price, timing, or fit — so you fix what's actually costing you deals.")],
 "steps_title":"From request to signed quote",
 "steps":[("Capture the request","Customer details, scope, and industry captured in one intake — nothing lost on a text thread."),
          ("Build off real costs","Add services and materials priced from your standards, not a guess. Labor and markup applied automatically."),
          ("Send it professionally","A clean, branded PDF goes out the same day — the number you give is the number that holds."),
          ("Track to a decision","Won, pending, or lost with a reason. The log turns every bid into data you can act on.")],
 "checks_kicker":"Included","checks_title":"What comes with the quoting module",
 "checks":["Itemized quote builder priced from your real materials and labor",
           "Branded, professional quote PDFs sent same-day",
           "Quote log with win/loss tracking and lost-reason analysis",
           "Margin and markup targets applied automatically on every line",
           "Flows straight into inventory, scheduling, and job costing — no re-entry",
           "Bilingual (English / Spanish) on request"],
 "faq_title":"Quoting software questions",
 "faq":[("Is this just a quote template?","No. It's a connected quoting system: quotes are priced from your real material and labor costs, logged with win/loss outcomes, and they feed your purchasing, scheduling, and job-costing automatically. A template can't tell you your close rate or protect your margin."),
        ("Do I need to be technical to use it?","No. It's built for owners and crews who have never used software like this. We deploy it for you, load your services and materials, and walk you through it. The whole point of Precision Growth Partners is that you get the system without having to build it."),
        ("Will it work for my trade?","The quoting engine is industry-agnostic — it runs on whatever services and materials we load for your trade. We have live and demo-ready builds for electrical, landscaping, roofing, drywall, solar, and barber/salon, and we build new trades to fit.")],
 "related":[R["inv"],R["cost"],R["play"],R["elec"]],
 "cta_title":"See your quotes, running.","cta_sub":"Book a working demo and we'll quote a real job from your trade — live, with your numbers."
},
{
 "slug":"inventory-operations-software", "crumb":"Inventory & Operations",
 "title":"Inventory, Materials & Operations Software | Precision Growth Partners",
 "desc":"Plan materials, purchasing, and scheduling off your real job pipeline. Inventory and operations software for small contractors and service businesses in Arizona.",
 "svc_type":"Inventory, materials & operations planning software",
 "kicker":"Sales, Inventory & Operations Planning", "h1":'Buy what the jobs <span class="accent">actually need.</span>',
 "sub":"Stop over-ordering and stop running short. This module nets your material demand against on-hand stock — prioritized by your real schedule — so you know exactly what to buy, for which job, and by when.",
 "meta_line":"Module 02 of the PGP operating system · Phoenix, Arizona",
 "stats":[("Net","Demand minus on-hand"),("By date","Sorted by needed-by"),("1-click","RFQ export"),("0","Double-buying")],
 "s1_kicker":"What it does","s1_title":"Purchasing planned, not panicked",
 "s1_intro":"The engine allocates your on-hand stock to won jobs first by earliest scheduled date, then to pending quotes — producing an accurate net-to-buy per part with the date you actually need it.",
 "features":[("01","Schedule-driven netting","Material requirements are calculated against won jobs by earliest start date, then pending quotes. You see net-to-buy per part and per job — never gross guesses."),
             ("02","Reorder alerts","On-hand levels and job demand surface what's about to run short before it stalls a crew on site."),
             ("03","Supplier-ready RFQs","Export a clean request-for-quote with net quantities and needed-by dates straight to suppliers — one click from the purchasing view or any quote.")],
 "steps_title":"From pipeline to purchase order",
 "steps":[("Jobs drive demand","Won jobs and pending quotes generate the material demand automatically — no separate list to maintain."),
          ("Net against stock","On-hand inventory is allocated to the earliest jobs first, leaving an accurate net-to-buy per part."),
          ("See what to buy","A 'to purchase' table lists part, quantity, unit, est. cost, and needed-by date — sorted so nothing is late."),
          ("Send the RFQ","Export supplier-facing RFQs with net quantities and blank pricing for the supplier to fill.")],
 "checks_kicker":"Included","checks_title":"What comes with the operations module",
 "checks":["Material requirements netting (net = demand − on-hand), prioritized by schedule",
           "Per-job and per-quote material breakdowns",
           "Reorder alerts before a crew runs short",
           "One-click supplier RFQ export (PDF) with needed-by dates",
           "Production board and scheduling tied to the same data",
           "Designed to extend into full procurement (POs, receiving) when you're ready"],
 "faq_title":"Inventory & operations questions",
 "faq":[("How is this different from a spreadsheet?","A spreadsheet can hold a parts list. It can't allocate your stock to the right jobs by date, tell you the true net you still need to buy, or generate a supplier RFQ. This does — and it updates automatically as jobs are won and scheduled."),
        ("What's an RFQ and why does it matter?","A request-for-quote is what you send suppliers to price your materials. The system builds it for you with the exact net quantities and the date you need them, so you get accurate supplier pricing without rebuilding the list by hand."),
        ("Can it grow into full purchasing?","Yes. The same engine is built to add suppliers, purchase orders, and receiving so netting becomes demand − on-hand − on-order. You start with planning and scale into procurement on the same monthly partnership — no new platform.")],
 "related":[R["quote"],R["cost"],R["roof"],R["solar"]],
 "cta_title":"Stop guessing on materials.","cta_sub":"Book a demo and we'll net a real job's materials live — and show you the RFQ it produces."
},
{
 "slug":"job-costing-software", "crumb":"Job Costing & Profit",
 "title":"Job Costing & Profit Tracking Software | Precision Growth Partners",
 "desc":"Know what every job actually made. Job costing and profit-tracking software for small contractors and service businesses in Arizona — quote vs. actual, by job.",
 "svc_type":"Job costing & profitability software",
 "kicker":"Cost & Learn", "h1":'Know what every job <span class="accent">actually made.</span>',
 "sub":"Quoted versus actual, job by job. This module closes the loop on every project — material variance, labor variance, real margin — so the next quote is tighter and the guesswork ends.",
 "meta_line":"Module 03 of the PGP operating system · Phoenix, Arizona",
 "stats":[("Quote","vs. Actual"),("Per job","Margin clarity"),("Variance","Material & labor"),("Tighter","Next quote")],
 "s1_kicker":"What it does","s1_title":"The number that runs the business",
 "s1_intro":"DJ Quik said it: if it don't make dollars, it don't make sense. This module makes the dollars visible — what you quoted, what you spent, and what you kept on every single job.",
 "features":[("01","Quote vs. actual","Every job compares what you bid to what it cost. No more finding out at tax time that a 'good' job lost money."),
             ("02","Variance you can act on","Material and labor variance break down where the money went, so you know whether to fix the quote, the crew, or the supplier."),
             ("03","Standards that improve","Real outcomes feed back into your labor and material standards — so each quarter your quotes get sharper and your margins hold.")],
 "steps_title":"Closing the loop on a job",
 "steps":[("Quote sets the baseline","The original itemized quote becomes the budget you measure against."),
          ("Actuals roll in","Materials used and labor hours land against the job as the work happens."),
          ("Variance surfaces","The system shows over/under on materials and labor and the real margin you earned."),
          ("Standards tighten","Patterns across jobs update your standards so the next bid is built on truth, not hope.")],
 "checks_kicker":"Included","checks_title":"What comes with the job-costing module",
 "checks":["Quoted-vs-actual comparison on every job",
           "Material and labor variance analysis",
           "Real per-job and period margin reporting",
           "Lost-reason and win/loss context from the quote log",
           "Feedback loop into your pricing and labor standards",
           "One connected system — costing data comes from your quotes and inventory, not re-entry"],
 "faq_title":"Job costing questions",
 "faq":[("I already use accounting software. Why this?","Accounting tells you whether the business made money overall and keeps the IRS happy. Job costing tells you which jobs, which crews, and which estimates made or lost money — the operational view accounting doesn't give you. They complement each other; we stop short of replacing your books."),
        ("Do I have to enter a lot of data?","No. The costing pulls from the quote and inventory you already built in the system, plus the labor hours your crew logs. The whole design avoids double entry — that's the point of one connected platform."),
        ("How does this make my quotes better?","Variance shows you exactly where your estimates miss — a material you always underbuy, a task that always runs long. Those patterns update your standards so the next quote is built on what really happens on your jobs.")],
 "related":[R["quote"],R["inv"],R["play"],R["dry"]],
 "cta_title":"Run by the numbers.","cta_sub":"Book a demo and we'll walk a job from quote to closed margin with real figures."
},
{
 "slug":"business-operations-playbook", "crumb":"Operating Playbook",
 "title":"Small Business Operating Playbook & Systems | Precision Growth Partners",
 "desc":"More than software — a partner. The operating playbook for small business owners: hiring, pricing, cash reserves, and growth milestones, run by the numbers in Arizona.",
 "svc_type":"Business operations consulting & systems",
 "kicker":"Refine & Repeat", "h1":'More than software. <span class="accent">A real partner.</span>',
 "sub":"The system gives you the data; the playbook tells you what to do with it. Departmentalization, hiring, pricing and margin targets, capital expenditure, cash reserves, and the growth milestones that turn a job into a business.",
 "meta_line":"The guidance layer of the PGP partnership · Phoenix, Arizona",
 "stats":[("6","Owner goal areas"),("Monthly","Working partnership"),("Quarterly","Course correction"),("100%","Your business")],
 "s1_kicker":"What it covers","s1_title":"Built for owners, run by the numbers",
 "s1_intro":"Software alone doesn't grow a business — decisions do. The playbook is the recurring guidance that turns your operating data into the moves that matter.",
 "features":[("01","Hiring & departmentalization","Know when the numbers justify the next hire, and how to split the work so the business doesn't live entirely in your head."),
             ("02","Pricing, margin & cash","Set pricing and margin targets that hold, plan capital expenditure, and build the cash reserves that let you sleep."),
             ("03","Growth milestones","The next door — second crew, second truck, second location — and the last door: a clean sale, or a business worth handing to someone you love.")],
 "steps_title":"How the partnership runs",
 "steps":[("Stand up the system","We deploy your operating platform and load it with your real services, materials, and standards."),
          ("Run by the numbers","Quotes, costs, and cash become visible — the dashboard replaces the gut feel."),
          ("Quarterly course-correction","We review what the numbers say and adjust pricing, hiring, and purchasing with you."),
          ("Refine & repeat","Each cycle tightens the standards and opens the next growth door — the partnership only works when it works for you.")],
 "checks_kicker":"The promise","checks_title":"What the partnership includes",
 "checks":["A complete operating system, deployed and run for you — not a login and good luck",
           "All modules included in the base price; hide what you don't need yet and grow into it",
           "Guidance on hiring, departmentalization, pricing, capex, cash reserves, and growth",
           "Flexible structures — pay up front, monthly, revenue share, peso or dollar, or hybrid",
           "Bilingual support in English and Spanish",
           "You keep what fits and drop what doesn't — past the cap, your growth is 100% yours"],
 "faq_title":"Partnership questions",
 "faq":[("Is this consulting or software?","Both, and that's the point. You get the operating system and a partner who helps you use it to make decisions. Greed has flooded the market with tools that bill you and disappear; Precision Growth Partners has faith in people and stays in the work with you."),
        ("What does it cost?","It's built to fit your cash flow — an initial payment, a monthly retainer, and a revenue share with a cap, or a hybrid you choose. You keep what fits and drop what doesn't. See Partnership Structures for the full model."),
        ("Who is this for?","Small operators and startups who are tired of running the business out of a shoebox — existing contractors who want to run by the numbers, and new owners who want the right foundation from day one.")],
 "related":[R["cost"],R["quote"],R["az"],R["startup"]],
 "cta_title":"It's time to bake our own bread.","cta_sub":"Book a working demo and let's talk about what your business could become with the right system behind it."
},
# ============================== INDUSTRY ==============================
{
 "slug":"electrical-contractor-software", "crumb":"Electrical Contractors",
 "title":"Electrical Contractor Software in Arizona | Precision Growth Partners",
 "desc":"Quoting, materials, permits, and job costing for electrical contractors. The operating system behind Tucson Badger Electric — built for Arizona electricians.",
 "svc_type":"Electrical contractor operations software",
 "kicker":"Industry · Electrical (Residential & Commercial)", "h1":'The system behind a <span class="accent">working electrician.</span>',
 "sub":"From quote to permit to inspection to paid — the operating system we built with our first live client, Tucson Badger Electric. Itemized bids, material netting, milestone payments, and the margin on every job.",
 "meta_line":"Live build: Tucson Badger Electric · Phoenix & Tucson, Arizona",
 "stats":[("Live","Real deployment"),("30/40/30","Milestone payments"),("Permit","To inspection, tracked"),("Per job","Real margin")],
 "s1_kicker":"Built with a real electrician","s1_title":"Quote → Permit → Install → Inspection → Paid",
 "s1_intro":"Electrical work is permit-heavy, material-heavy, and milestone-paid. The system maps the whole lifecycle so nothing falls through — and you always know where every job and every dollar stands.",
 "features":[("01","Itemized electrical bids","Price panel upgrades, EV chargers, rewires, and new construction off real materials and labor — defendable to the customer, profitable to you."),
             ("02","Materials netted to the schedule","Wire, panels, breakers, and devices netted against on-hand stock by job date, with supplier RFQs one click away."),
             ("03","Milestone payments & job costing","30/40/30 milestone billing tied to rough-in and final, with quoted-vs-actual margin on every job.")],
 "steps_title":"How an electrical job runs in the system",
 "steps":[("Quote the job","Itemized bid from your electrical service and material standards, sent same-day as a clean PDF."),
          ("Pull permits & order","Permit tracked, materials netted and ordered via RFQ so the truck is stocked before the crew rolls."),
          ("Install & track","Job moves across stages — scheduled, rough-in, trim-out — with labor logged against the bid."),
          ("Inspect, invoice, learn","Final inspection, milestone invoice, and a closed-out margin that sharpens the next quote.")],
 "checks_kicker":"For electricians","checks_title":"What electrical contractors get",
 "checks":["Itemized quoting for panel upgrades, EV chargers, remodels, additions, and new builds",
           "Material netting for wire, panels, breakers, and devices with supplier RFQs",
           "Permit and inspection stages tracked across the job lifecycle",
           "30/40/30 milestone billing on new construction and large jobs",
           "Quoted-vs-actual job costing and win/loss analysis",
           "Bilingual (English / Spanish) — built for Arizona crews"],
 "faq_title":"Electrical contractor software questions",
 "faq":[("Is this really running in a real business?","Yes. Tucson Badger Electric is our first live client and the real-world deployment of this system. The electrical build started from our industry-standard template and was customized with their actual services, pricing, and workflow."),
        ("Does it handle permits and inspections?","The job lifecycle includes the stages an electrical job actually moves through — quoted, permitted, scheduled, installed, inspected, invoiced, paid — so you always know where a job stands and nothing stalls between steps."),
        ("Commercial or residential?","Both. The residential build is live today; commercial electrical runs on the same engine with its own services, materials, and stages. We tailor the build to how you actually work.")],
 "related":[R["quote"],R["inv"],R["solar"],R["tuc"]],
 "cta_title":"See an electrical job, running.","cta_sub":"Book a demo and we'll run a real electrical job from quote to closed margin in the live system."
},
{
 "slug":"landscaping-business-software", "crumb":"Landscaping",
 "title":"Landscaping Business Software in Arizona | Precision Growth Partners",
 "desc":"Quoting, scheduling, materials, and job costing for landscaping companies. Run recurring and project landscaping work by the numbers in Arizona.",
 "svc_type":"Landscaping business operations software",
 "kicker":"Industry · Landscaping", "h1":'Landscaping that runs <span class="accent">by the route and the numbers.</span>',
 "sub":"Recurring maintenance and big installs in one system: itemized quotes, materials and equipment planned to the job, scheduling that fits your crews, and the real margin on every property and project.",
 "meta_line":"Demo-ready industry build · Phoenix, Arizona",
 "stats":[("Recurring","+ project work"),("Per property","Margin clarity"),("Materials","Planned to job"),("Crews","Scheduled right")],
 "s1_kicker":"For landscapers","s1_title":"Maintenance routes and installs, one system",
 "s1_intro":"Landscaping is two businesses in one — recurring service and project installs. The system handles both, so neither the weekly route nor the big paver job runs on memory.",
 "features":[("01","Quote both kinds of work","Recurring maintenance agreements and itemized install bids — hardscape, irrigation, planting — priced off real materials and labor."),
             ("02","Materials & equipment to the job","Plants, stone, soil, and irrigation parts planned against the schedule so trucks leave loaded right."),
             ("03","Per-property profit","See which accounts and which installs actually make money, and which routes are quietly losing it.")],
 "steps_title":"How a landscaping job runs",
 "steps":[("Quote the work","Itemized install bid or recurring agreement, priced from your standards and sent same-day."),
          ("Plan materials & crews","Materials netted to the job, crews scheduled to fit the route and the install calendar."),
          ("Do the work","Jobs move across stages with labor and materials logged against the bid."),
          ("Close & learn","Real margin per property and per install feeds tighter pricing next season.")],
 "checks_kicker":"For landscapers","checks_title":"What landscaping companies get",
 "checks":["Itemized quoting for hardscape, irrigation, planting, and maintenance",
           "Recurring service agreements alongside project bids",
           "Materials and equipment planned to the schedule with supplier RFQs",
           "Crew scheduling and a production board for installs",
           "Per-property and per-install job costing",
           "Bilingual (English / Spanish) for your crews"],
 "faq_title":"Landscaping software questions",
 "faq":[("Does it handle recurring maintenance and one-off installs?","Yes — that's the point. Recurring maintenance agreements and large itemized installs live in the same system, so you run the weekly route and the big paver project without two different shoeboxes."),
        ("Can it plan plants, stone, and irrigation materials?","Yes. Materials are netted against your job schedule, so you order what the upcoming installs actually need and send suppliers a clean RFQ instead of guessing at the yard."),
        ("Is the landscaping build ready to see?","Landscaping is one of our demo-ready industry builds. We can show you a working version today and then customize it with your real services, pricing, and materials as a client build.")],
 "related":[R["quote"],R["inv"],R["cost"],R["phx"]],
 "cta_title":"See your landscaping business, running.","cta_sub":"Book a demo and we'll quote and cost a real landscaping job in the live system."
},
{
 "slug":"roofing-business-software", "crumb":"Roofing",
 "title":"Roofing Business Software in Arizona | Precision Growth Partners",
 "desc":"Quoting, materials, production, and job costing for roofing contractors. Run material-heavy, multi-stage roofing jobs by the numbers in Arizona.",
 "svc_type":"Roofing contractor operations software",
 "kicker":"Industry · Roofing", "h1":'Roofing jobs, run <span class="accent">start to finish.</span>',
 "sub":"Material-heavy and multi-stage by nature — roofing needs a system. Itemized bids by square, materials netted to the job, a production board that keeps crews moving, and the real margin after every tear-off.",
 "meta_line":"Demo-ready industry build · Phoenix, Arizona",
 "stats":[("By square","Itemized bids"),("Materials","Netted to job"),("Multi-stage","Production board"),("Per job","Real margin")],
 "s1_kicker":"For roofers","s1_title":"Heavy on materials, heavy on stages",
 "s1_intro":"A roofing job lives or dies on accurate material takeoffs and crews that stay scheduled. The system handles both so a busy season doesn't turn into a guessing game.",
 "features":[("01","Bid by the square","Itemized quotes for tear-off, underlayment, shingles or tile, flashing, and disposal — priced off real costs and waste factors."),
             ("02","Materials netted to the job","Shingles, underlayment, and flashing planned against the schedule with supplier RFQs, so a crew never sits idle waiting on a delivery."),
             ("03","Production board & costing","Multi-stage jobs tracked across the board, with quoted-vs-actual margin after disposal and labor.")],
 "steps_title":"How a roofing job runs",
 "steps":[("Quote by square","Itemized bid built from your roofing standards and waste factors, sent same-day."),
          ("Net the materials","Shingles, underlayment, and flashing netted to the job date with a supplier RFQ ready to send."),
          ("Run the crews","Jobs move across the production board — scheduled, tear-off, dry-in, finish — with labor logged."),
          ("Close the margin","Real cost after disposal and labor shows the true margin and sharpens the next bid.")],
 "checks_kicker":"For roofers","checks_title":"What roofing contractors get",
 "checks":["Itemized bidding by square with waste factors built in",
           "Material netting for shingles, tile, underlayment, and flashing",
           "Supplier RFQ export with needed-by dates",
           "Multi-stage production board for tear-off through finish",
           "Quoted-vs-actual job costing including disposal and labor",
           "Bilingual (English / Spanish) for your crews"],
 "faq_title":"Roofing software questions",
 "faq":[("Can it handle accurate material takeoffs?","Yes. Bids are itemized by square with your waste factors, and the materials flow into netting so you order shingles, underlayment, and flashing against the real schedule — with a supplier RFQ ready to send."),
        ("Does it keep multiple crews scheduled?","A production board tracks every job across its stages — tear-off, dry-in, finish — so you can see where every crew and every job stands during a busy season."),
        ("Is the roofing build ready?","Roofing is a demo-ready industry build. We can show a working version now and customize it into a client build with your real services, pricing, and material standards.")],
 "related":[R["inv"],R["quote"],R["cost"],R["dry"]],
 "cta_title":"See a roofing job, running.","cta_sub":"Book a demo and we'll bid and cost a real roof in the live system."
},
{
 "slug":"drywall-contractor-software", "crumb":"Drywall",
 "title":"Drywall Contractor Software in Arizona | Precision Growth Partners",
 "desc":"Quoting, materials, production, and job costing for drywall contractors. Bid by the board, track production, and run drywall jobs by the numbers in Arizona.",
 "svc_type":"Drywall contractor operations software",
 "kicker":"Industry · Drywall", "h1":'Bid by the board. <span class="accent">Keep the margin.</span>',
 "sub":"Hang, tape, and finish — drywall runs on volume and tight margins. The system bids off board count and labor standards, plans materials to the job, and shows you the real profit on every project.",
 "meta_line":"Demo-ready industry build · Phoenix, Arizona",
 "stats":[("By board","Itemized bids"),("Materials","Planned to job"),("Stages","Hang → finish"),("Per job","Real margin")],
 "s1_kicker":"For drywall crews","s1_title":"Volume work needs tight numbers",
 "s1_intro":"Drywall margins are thin enough that a loose estimate eats the profit. The system bids off real board and labor standards and tracks the job so the thin margin actually survives to the bank.",
 "features":[("01","Bid by board and finish level","Itemized quotes by board count, finish level, and labor — priced off standards, not a gut number."),
             ("02","Materials to the job","Board, mud, tape, and fasteners planned against the schedule with supplier RFQs."),
             ("03","Production stages & costing","Hang, tape, and finish tracked across stages, with quoted-vs-actual margin on every job.")],
 "steps_title":"How a drywall job runs",
 "steps":[("Quote by the board","Itemized bid from board count, finish level, and labor standards, sent same-day."),
          ("Plan materials","Board, mud, and tape netted to the schedule with a supplier RFQ ready."),
          ("Run the stages","Hang → tape → finish tracked on the board with labor logged against the bid."),
          ("Close the margin","Real cost vs. quote shows whether the thin margin held — and tightens the next bid.")],
 "checks_kicker":"For drywall crews","checks_title":"What drywall contractors get",
 "checks":["Itemized bidding by board count and finish level",
           "Material planning for board, mud, tape, and fasteners",
           "Supplier RFQ export with needed-by dates",
           "Hang/tape/finish production stages on a board",
           "Quoted-vs-actual job costing on thin-margin work",
           "Bilingual (English / Spanish) for your crews"],
 "faq_title":"Drywall software questions",
 "faq":[("Why a system for drywall specifically?","Drywall margins are thin and the work is high-volume, so a loose estimate quietly eats the profit. Bidding off real board and labor standards and tracking actual cost is exactly how you keep the margin you quoted."),
        ("Is the drywall build a fast one to deploy?","Drywall is one of our lighter-materials, simpler-stage builds, which makes it quick to stand up. It's also the template we often start from for adjacent trades."),
        ("Can it scale into purchasing?","Yes — material planning extends into full purchasing with suppliers and POs on the same partnership when you're ready.")],
 "related":[R["quote"],R["inv"],R["roof"],R["cost"]],
 "cta_title":"See a drywall job, running.","cta_sub":"Book a demo and we'll bid and cost a real drywall job in the live system."
},
{
 "slug":"solar-installer-software", "crumb":"Solar",
 "title":"Solar Installer Software in Arizona | Precision Growth Partners",
 "desc":"Quoting, materials, permits, and job costing for solar installers. Run design-to-PTO solar jobs with milestones and inventory by the numbers in Arizona.",
 "svc_type":"Solar installer operations software",
 "kicker":"Industry · Solar", "h1":'Solar jobs from <span class="accent">design to PTO.</span>',
 "sub":"Permit-heavy, equipment-heavy, milestone-paid — solar is built for a system. Itemized proposals, panels and inverters netted to the job, permit and interconnection stages tracked, and the real margin on every install.",
 "meta_line":"Demo-ready industry build · Phoenix, Arizona",
 "stats":[("Design","to PTO"),("Equipment","Netted to job"),("Permit","& interconnection"),("Per job","Real margin")],
 "s1_kicker":"For solar installers","s1_title":"A long lifecycle that can't drop a step",
 "s1_intro":"A solar job spans design, permit, install, inspection, and permission-to-operate — weeks of steps where a dropped ball costs money. The system tracks the whole arc so nothing stalls.",
 "features":[("01","Itemized proposals","Price systems by panels, inverters, racking, and labor — defendable to the customer and profitable to you."),
             ("02","Equipment netted to the job","Panels, inverters, and racking planned against the schedule with supplier RFQs, so high-value gear arrives on time."),
             ("03","Permit-to-PTO tracking & costing","Design, permit, install, inspection, and PTO tracked as stages, with quoted-vs-actual margin per install.")],
 "steps_title":"How a solar job runs",
 "steps":[("Propose the system","Itemized proposal by panels, inverters, and labor, sent same-day."),
          ("Permit & order","Permit tracked, equipment netted and ordered via RFQ so the install isn't waiting on gear."),
          ("Install & inspect","Job moves across stages — scheduled, installed, inspected — with labor logged against the bid."),
          ("PTO & close","Permission-to-operate reached, milestone invoiced, and real margin closed out.")],
 "checks_kicker":"For solar installers","checks_title":"What solar installers get",
 "checks":["Itemized proposals by panels, inverters, racking, and labor",
           "Equipment netting for high-value gear with supplier RFQs",
           "Design → permit → install → inspection → PTO stages tracked",
           "Milestone billing on large installs",
           "Quoted-vs-actual job costing per install",
           "Bilingual (English / Spanish) for your crews"],
 "faq_title":"Solar software questions",
 "faq":[("Does it track the full permit-to-PTO lifecycle?","Yes. A solar job's stages — design, permit, install, inspection, permission-to-operate — are tracked so you always know where each project stands across a multi-week timeline and nothing falls through."),
        ("Can it manage high-value equipment?","Equipment like panels and inverters is netted against your job schedule with supplier RFQs, so expensive gear is ordered to arrive when the install needs it — not too early, not too late."),
        ("Is the solar build ready to see?","Solar is a demo-ready industry build. We show a working version and then customize it with your real equipment, pricing, and workflow as a client build.")],
 "related":[R["inv"],R["quote"],R["elec"],R["cost"]],
 "cta_title":"See a solar job, running.","cta_sub":"Book a demo and we'll run a real solar install from proposal to closed margin."
},
{
 "slug":"barber-salon-software", "crumb":"Barber & Salon",
 "title":"Barber & Salon Software in Arizona | Precision Growth Partners",
 "desc":"Appointments, supplies, and per-chair profitability for barbershops and salons. Run your shop by the numbers in Arizona with Precision Growth Partners.",
 "svc_type":"Barber & salon operations software",
 "kicker":"Industry · Barber & Beauty", "h1":'Run the chair <span class="accent">like a business.</span>',
 "sub":"Appointments, services, supplies, and the numbers behind every chair. Built for barbershops and salons that want to stop running on a calendar app and a cash drawer and start running on a system.",
 "meta_line":"Demo-ready industry build · Phoenix, Arizona",
 "stats":[("Per chair","Profit clarity"),("Supplies","Tracked to use"),("Services","Priced right"),("Booked","& costed")],
 "s1_kicker":"For shops & salons","s1_title":"Appointment-driven, supply-aware, profit-clear",
 "s1_intro":"A shop doesn't need a roofing production board — it needs clean booking, supply tracking, and a clear view of what each chair and each service actually earns. The system fits the work.",
 "features":[("01","Services priced right","Every service priced with the supply cost and chair time behind it, so your menu reflects real margin, not habit."),
             ("02","Supplies tracked to use","Color, product, and consumables tracked against services so you reorder on time and know your true cost per client."),
             ("03","Per-chair numbers","See what each chair, stylist, and service line earns — the view a calendar app will never give you.")],
 "steps_title":"How the shop runs in the system",
 "steps":[("Set the menu","Services priced with real supply cost and chair time behind each line."),
          ("Book the work","Appointments captured cleanly so the day runs on a system, not sticky notes."),
          ("Track supplies","Product and consumables tracked against services with reorder alerts."),
          ("See the numbers","Per-chair and per-service profit shows where the shop actually makes money.")],
 "checks_kicker":"For shops & salons","checks_title":"What barbershops and salons get",
 "checks":["Service menu priced off real supply cost and chair time",
           "Appointment capture and a clean daily view",
           "Supply and consumable tracking with reorder alerts",
           "Per-chair, per-stylist, and per-service profitability",
           "The same costing and reporting discipline as our trade builds",
           "Bilingual (English / Spanish)"],
 "faq_title":"Barber & salon software questions",
 "faq":[("Isn't a booking app enough?","A booking app fills the calendar but can't tell you what each chair earns, what a service really costs in supplies, or when to reorder color. The system adds the business view on top of booking, so you run the shop by the numbers."),
        ("Do I need the heavy modules?","No. All modules are included, but you hide what you don't need — a shop runs lean on services, supplies, and per-chair numbers, and can grow into more later on the same partnership."),
        ("Is the barber/salon build ready?","Barber & Beauty is a demo-ready industry build. We show a working version and customize it to your menu, pricing, and supplies as a client build.")],
 "related":[R["quote"],R["cost"],R["play"],R["startup"]],
 "cta_title":"See your shop, running.","cta_sub":"Book a demo and we'll set up a real service menu and show the per-chair numbers."
},
# ============================== LOCATION ==============================
{
 "slug":"small-business-software-arizona", "crumb":"Arizona",
 "title":"Small Business Software & Systems in Arizona | Precision Growth Partners",
 "desc":"Complete operating systems for Arizona small businesses and contractors — quoting, inventory, scheduling, job costing, and guidance. Built honest. Built precise.",
 "svc_type":"Small business operations software & consulting",
 "kicker":"Serving Arizona", "h1":'Systems for Arizona&rsquo;s <span class="accent">small operators.</span>',
 "sub":"From Phoenix to Tucson and the communities between, we build complete digital operations for small contractors and service businesses — and stay in the work as a partner, not a vendor who bills you and disappears.",
 "meta_line":"Phoenix-based · Serving Arizona and beyond",
 "stats":[("Arizona","Born & based"),("Bilingual","EN / ES"),("End-to-end","Quote to cash"),("Partner","Not a vendor")],
 "s1_kicker":"Why Arizona operators","s1_title":"Software that fits, at a cost that compares",
 "s1_intro":"Arizona's small operators have been sold software that doesn't fit and consultants who don't stay. We build the system, deploy it, and run alongside you — bilingual, honest, and tied to your real numbers.",
 "features":[("01","Built for how you work","Quoting, materials, scheduling, and job costing tailored to your trade — not a generic tool you bend your business around."),
             ("02","Bilingual by default","English and Spanish across the app, quotes, and support — built for Arizona's crews and customers."),
             ("03","A partner who stays","Monthly partnership with guidance on pricing, hiring, and growth. The relationship only works when it works for you.")],
 "steps_title":"How we work with Arizona businesses",
 "steps":[("Talk it through","A working demo with your real numbers — no slideware, no pressure."),
          ("Stand up your system","We deploy and load it with your services, materials, and standards."),
          ("Run by the numbers","Quotes, costs, and cash become visible across your whole operation."),
          ("Grow on the same partnership","Add modules and open growth doors as the business is ready.")],
 "checks_kicker":"Across the state","checks_title":"Where we serve",
 "checks":["Phoenix metro — Scottsdale, Mesa, Tempe, Chandler, Gilbert, Glendale",
           "Tucson metro — Marana, Oro Valley, Sahuarita, Vail",
           "Remote deployment and support statewide and beyond",
           "Bilingual (English / Spanish) service",
           "Trades, service businesses, and startups",
           "Flexible partnership structures to fit your cash flow"],
 "faq_title":"Arizona small business questions",
 "faq":[("Do you only work in Phoenix?","We're Phoenix-based but serve all of Arizona — the Tucson metro, the surrounding communities, and beyond. Deployment and support are remote-friendly, with in-person where it makes sense."),
        ("What kinds of businesses do you work with?","Small contractors and service businesses — electrical, landscaping, roofing, drywall, solar, barber and salon, and more — plus new owners standing up a business from scratch."),
        ("Do you offer service in Spanish?","Yes. The system, quotes, and support are bilingual in English and Spanish, in natural Mexican Spanish — built for Arizona's operators and their customers.")],
 "related":[R["phx"],R["tuc"],R["play"],R["startup"]],
 "cta_title":"Built honest. Built precise.","cta_sub":"Book a working demo and see your Arizona business running on a real system."
},
{
 "slug":"phoenix-small-business-help", "crumb":"Phoenix",
 "title":"Phoenix Small Business Help & Systems | Precision Growth Partners",
 "desc":"Phoenix small business help — operating systems and hands-on guidance for contractors and service businesses across the Valley. Quoting, costing, and growth.",
 "svc_type":"Small business operations software & consulting",
 "kicker":"Serving the Valley", "h1":'Phoenix small business, <span class="accent">run by the numbers.</span>',
 "sub":"Hands-on help for Valley operators who are done running the business out of a shoebox. We build your quoting, materials, and job-costing system, then partner with you on the decisions that grow it.",
 "meta_line":"Phoenix, Arizona · Serving the Valley and beyond",
 "stats":[("Phoenix","Based here"),("Valley-wide","On-site & remote"),("End-to-end","Quote to cash"),("Bilingual","EN / ES")],
 "s1_kicker":"For Valley operators","s1_title":"Local help, real systems",
 "s1_intro":"The Valley is full of hard-working operators who never had software that fit. We bring the system and the guidance, deployed and run for you, tied to your real numbers.",
 "features":[("01","Your system, deployed","Quoting, inventory, scheduling, and job costing stood up for your trade — not a login and a tutorial."),
             ("02","Hands-on guidance","Pricing, hiring, cash reserves, and growth milestones, reviewed with you each quarter."),
             ("03","Here in the Valley","Phoenix-based and close — Scottsdale, Mesa, Tempe, Chandler, Gilbert, Glendale and the rest of the metro.")],
 "steps_title":"How we help Phoenix businesses",
 "steps":[("Working demo","See your real numbers in the system before you commit to anything."),
          ("Deploy & load","We stand up the system with your services, materials, and standards."),
          ("Run by the numbers","Your whole operation becomes visible — quotes, costs, cash."),
          ("Grow together","Add modules and open growth doors on the same monthly partnership.")],
 "checks_kicker":"Across the Valley","checks_title":"Phoenix-area communities we serve",
 "checks":["Phoenix, Scottsdale, Tempe, Mesa, Chandler, Gilbert, Glendale, Peoria, Surprise",
           "On-site where it helps, remote where it's faster",
           "Bilingual (English / Spanish) service",
           "Contractors, service businesses, and startups",
           "All modules included; hide what you don't need yet",
           "Flexible partnership structures to fit your cash flow"],
 "faq_title":"Phoenix small business questions",
 "faq":[("What does 'small business help' actually mean here?","It means we build and run your operating system — quoting, materials, job costing — and act as a partner on the decisions that grow the business: pricing, hiring, cash, and growth. Software plus guidance, not one or the other."),
        ("Do you meet in person in Phoenix?","Yes, where it helps. We're Phoenix-based, so on-site work across the Valley is straightforward; a lot of deployment and support is also remote to keep things fast and affordable."),
        ("How much does it cost?","It's built to fit your cash flow — an initial payment, a monthly retainer, and a revenue share with a cap, or a hybrid. See Partnership Structures for the full model.")],
 "related":[R["az"],R["tuc"],R["play"],R["startup"]],
 "cta_title":"Let's grow your Phoenix business.","cta_sub":"Book a working demo and see your Valley business running on a real system."
},
{
 "slug":"tucson-small-business-help", "crumb":"Tucson",
 "title":"Tucson Small Business Help & Systems | Precision Growth Partners",
 "desc":"Tucson small business help — operating systems and hands-on guidance for contractors and service businesses across the Tucson metro. Home of our first live client.",
 "svc_type":"Small business operations software & consulting",
 "kicker":"Serving the Tucson Metro", "h1":'Tucson small business, <span class="accent">running on a system.</span>',
 "sub":"Tucson is home to our first live client, Tucson Badger Electric. We bring the same complete operating system and hands-on partnership to contractors and service businesses across the metro.",
 "meta_line":"Serving Tucson, Marana, Oro Valley, Sahuarita & Vail",
 "stats":[("Tucson","First live client"),("Metro-wide","On-site & remote"),("End-to-end","Quote to cash"),("Bilingual","EN / ES")],
 "s1_kicker":"For Tucson operators","s1_title":"Proven local, built to fit",
 "s1_intro":"Our first real deployment runs in Tucson. That means the system isn't a concept here — it's working in a local business, and we bring the same build-and-partner approach to your trade.",
 "features":[("01","A proven local build","Tucson Badger Electric runs on this system today. We start from a working build and customize it to how you operate."),
             ("02","Your system, run for you","Quoting, materials, scheduling, and job costing deployed and supported — not handed over cold."),
             ("03","Across the metro","Tucson, Marana, Oro Valley, Sahuarita, Green Valley, and Vail — local and close.")],
 "steps_title":"How we help Tucson businesses",
 "steps":[("Working demo","See a real Tucson build and your own numbers in the system."),
          ("Deploy & load","We stand up your system with your services, materials, and standards."),
          ("Run by the numbers","Your whole operation becomes visible — quotes, costs, cash."),
          ("Grow together","Add modules and open growth doors on the same monthly partnership.")],
 "checks_kicker":"Across the metro","checks_title":"Tucson-area communities we serve",
 "checks":["Tucson, Marana, Oro Valley, Sahuarita, Green Valley, Vail, Catalina Foothills",
           "Home of our first live client, Tucson Badger Electric",
           "On-site where it helps, remote where it's faster",
           "Bilingual (English / Spanish) service",
           "Contractors, service businesses, and startups",
           "Flexible partnership structures to fit your cash flow"],
 "faq_title":"Tucson small business questions",
 "faq":[("Do you really have a live client in Tucson?","Yes. Tucson Badger Electric is our first live client and the real-world deployment of the system. It started from our electrical template and was customized with their actual services, pricing, and workflow."),
        ("Will you build for my trade in Tucson?","Yes. We have demo-ready builds for several trades and customize them to your business. If your trade isn't built yet, you could be the first local case study for it."),
        ("Is service available in Spanish?","Yes. The system, quotes, and support are bilingual in English and Spanish, built for the Tucson metro's operators and customers.")],
 "related":[R["elec"],R["az"],R["phx"],R["start"]],
 "cta_title":"Let's grow your Tucson business.","cta_sub":"Book a working demo and see your Tucson business running on the same system as our first live client."
},
# ============================== STARTUP ==============================
{
 "slug":"start-a-contracting-business-arizona", "crumb":"Start a Contracting Business",
 "title":"How to Start a Contracting Business in Arizona | Precision Growth Partners",
 "desc":"Starting a contracting business in Arizona? Stand up your quoting, materials, and job-costing systems from day one — with a partner who runs the numbers with you.",
 "svc_type":"New business systems & startup consulting",
 "kicker":"Startup · Contractors & Trades", "h1":'Start your trade on <span class="accent">real systems.</span>',
 "sub":"Most new contractors start with a truck, a phone, and a shoebox of receipts. Start with a system instead — quoting that protects your margin from job one, materials planned to the work, and a partner who runs the numbers with you.",
 "meta_line":"For new Arizona contractors & service businesses",
 "stats":[("Day one","On a system"),("Margin","Protected early"),("Bilingual","EN / ES"),("Partner","From the start")],
 "s1_kicker":"For new owners","s1_title":"The foundation most owners build too late",
 "s1_intro":"The operators who struggle aren't the ones without talent — they're the ones who never built systems and found out at tax time what the jobs really made. Start with the foundation, not the shoebox.",
 "features":[("01","Quote like a pro from job one","Itemized, professional quotes priced off real costs and a target margin — so you don't underbid your way out of business in year one."),
             ("02","Know your numbers early","Job costing from the start means you learn what actually makes money before bad habits set in."),
             ("03","A partner, not just a tool","Guidance on pricing, that first hire, cash reserves, and the growth milestones ahead — the help most new owners never get.")],
 "steps_title":"From idea to first invoice",
 "steps":[("Talk it through","We learn your trade and your goals, and show you the system with realistic numbers."),
          ("Stand up the foundation","Quoting, materials, and costing deployed with industry-standard defaults for your trade."),
          ("Win your first jobs","Professional quotes out the door, materials planned, margin protected from the start."),
          ("Grow on purpose","Run by the numbers and open the next door — second crew, second truck — when the figures say so.")],
 "checks_kicker":"For new contractors","checks_title":"What you get starting out",
 "checks":["Professional, margin-protected quoting from your very first bid",
           "Materials and purchasing planned to your real jobs",
           "Job costing so you learn what makes money early",
           "Guidance on pricing, hiring, cash reserves, and growth",
           "Bilingual (English / Spanish)",
           "Flexible structures built to fit a new business's cash flow"],
 "faq_title":"Starting a contracting business in Arizona",
 "faq":[("I'm brand new — is this overkill?","It's the opposite. Starting on a system is far cheaper than learning the hard way that your jobs lost money. You start lean — quoting and costing — and grow into the rest. The foundation is what keeps a new business alive."),
        ("Do you help with licensing and the legal setup?","Our focus is the operating system and the business numbers — quoting, materials, costing, pricing, and growth. We point you in the right direction on licensing (in Arizona, the ROC for contractors) but we're not a law firm; we make sure the business runs profitably once you're set up."),
        ("Can I afford this as a startup?","Partnership structures are built to fit cash flow — including monthly and revenue-share options — so a new business isn't priced out of the foundation it needs. See Partnership Structures.")],
 "related":[R["startup"],R["quote"],R["cost"],R["az"]],
 "cta_title":"Start with the foundation.","cta_sub":"Book a working demo and let's stand up your new contracting business on real systems."
},
{
 "slug":"small-business-startup-help-arizona", "crumb":"Startup Help",
 "title":"Small Business Startup Help in Arizona | Precision Growth Partners",
 "desc":"Small business startup help in Arizona — from idea to first invoice. Build the right systems and run by the numbers with a partner who has faith in people.",
 "svc_type":"New business systems & startup consulting",
 "kicker":"Startup · Any Small Business", "h1":'From idea to <span class="accent">first invoice.</span>',
 "sub":"Greed has flooded the market with tools that bill you and partners who disappear. We have faith in people — the ones who took the harder road. If you're starting something, we help you start it right and run it by the numbers.",
 "meta_line":"For new Arizona owners · Bilingual EN / ES",
 "stats":[("Idea","to invoice"),("Right","Foundation"),("Bilingual","EN / ES"),("Faith","In people")],
 "s1_kicker":"For new owners","s1_title":"Start it right, run it real",
 "s1_intro":"A new business doesn't need every module on day one — it needs the right foundation and a partner who tells the truth about the numbers. We meet you where you are and grow with you.",
 "features":[("01","The right starting set","Quoting and costing first — the two things that decide whether a new business survives — with the rest ready when you grow into it."),
             ("02","Run by the numbers early","Learn what makes money from the first jobs, so you build good habits instead of expensive ones."),
             ("03","A partner with faith in people","Honest guidance for the owner who's betting on themselves — pricing, that first hire, cash, and the road ahead.")],
 "steps_title":"How we help you start",
 "steps":[("Talk it through","No pressure — we learn your idea and your goals and show you what running it on a system looks like."),
          ("Build the foundation","The starting set, deployed and loaded for your kind of business."),
          ("Reach first invoice","Professional quotes out, costs tracked, margin clear from the very first job."),
          ("Grow on the same partnership","Add modules and open growth doors as the business is ready.")],
 "checks_kicker":"For new owners","checks_title":"What startup help includes",
 "checks":["A right-sized starting system — quoting and costing first",
           "Job costing so you learn what makes money early",
           "Guidance on pricing, first hire, cash reserves, and growth",
           "All modules included; grow into them on the monthly partnership",
           "Bilingual (English / Spanish), in natural Mexican Spanish",
           "Flexible structures built to fit a startup's cash flow"],
 "faq_title":"Startup help questions",
 "faq":[("What kinds of startups do you help?","Small operators across trades and service businesses — and owners who don't fit a neat category yet. If you're starting something and want to run it on real systems instead of a shoebox, that's exactly who this is for."),
        ("Do I need to know what software I want?","No. That's our job. You bring the business and the goals; we bring the system, deploy it, and guide you on using the numbers to grow. You don't have to be technical."),
        ("Why should I trust a partner this early?","Because the partnership only works when it works for you — you keep what fits and drop what doesn't. We'd rather grow with an owner who's betting on themselves than bill a stranger and vanish. That's the whole idea behind Precision Growth Partners.")],
 "related":[R["start"],R["play"],R["quote"],R["az"]],
 "cta_title":"It's time to bake our own bread.","cta_sub":"Book a working demo and let's start your business on the right foundation."
},
]

if __name__ == "__main__":
    written = []
    for p in PAGES:
        out = os.path.join(ROOT, p["slug"] + ".html")
        with open(out, "w", encoding="utf-8") as f:
            f.write(render(p))
        written.append(p["slug"] + ".html")
    # sitemap.xml
    urls = ["", "pricing.html"] + [s for s in written]
    sm = ['<?xml version="1.0" encoding="UTF-8"?>',
          '<urlset xmlns="http://www.sitemap.org/schemas/sitemap/0.9">'.replace("sitemap.org","sitemaps.org")]
    from datetime import date
    today = date.today().isoformat()
    for u in urls:
        loc = SITE + "/" + u
        pr = "1.0" if u == "" else ("0.8" if u == "pricing.html" else "0.7")
        sm.append(f"  <url><loc>{loc}</loc><lastmod>{today}</lastmod><changefreq>monthly</changefreq><priority>{pr}</priority></url>")
    sm.append("</urlset>")
    with open(os.path.join(ROOT, "sitemap.xml"), "w", encoding="utf-8") as f:
        f.write("\n".join(sm))
    # robots.txt
    with open(os.path.join(ROOT, "robots.txt"), "w", encoding="utf-8") as f:
        f.write(f"User-agent: *\nAllow: /\n\nSitemap: {SITE}/sitemap.xml\n")
    print("WROTE", len(written), "pages + sitemap.xml + robots.txt")
    for w in written:
        print(" -", w)


