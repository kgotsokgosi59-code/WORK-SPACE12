#!/usr/bin/env python3
"""
build_site.py — scaffolding helper for the Jiks Academy site.

It writes plain, standalone HTML files into ./jiks-academy. Every page is a
separate file and can be edited directly afterwards; this script just keeps the
shared nav/footer identical across all of them. Delete it if you'd rather not
have it around.

Run:  python3 build_site.py
"""
import os

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "jiks-academy")
os.makedirs(os.path.join(OUT, "assets", "css"), exist_ok=True)
os.makedirs(os.path.join(OUT, "assets", "js"), exist_ok=True)
os.makedirs(os.path.join(OUT, "assets", "img", "crew"), exist_ok=True)

# Set this to the live domain before launch — Open Graph / manifest want absolute URLs.
SITE_URL = ""

EMAIL = "kgotsokgosi59@gmail.com"
PHONE = "+27 67 702 4063"
PHONE_HREF = "+27677024063"
PLACE = "Daveyton, East Rand, Gauteng"

NAV_ITEMS = [
    ("Home", "home.html"),
    ("About", "about.html"),
    ("Ventures", "ventures.html"),
    ("Crew", "crew.html"),
    ("Hector", "hector.html"),
    ("Services", "services.html"),
    ("Clients", "clients.html"),
    ("Contact", "contact.html"),
]

CLIENT_LOGOS = [
    ("agsa", "Auditor-General of South Africa", "Institutional", False),
    ("pepsico", "PepsiCo", "Corporate", False),
    ("nwpl", "North West Provincial Legislature", "Government", False),
    ("nwedu", "North West Provincial Education", "Government", False),
    ("tut", "Tshwane University of Technology", "Higher education", False),
    ("amcu", "AMCU", "Organised labour", False),
    ("birchwood", "Birchwood &amp; OR Tambo Conference Centre", "Venue partner", True),
    ("addprop", "AddProp", "Corporate", True),
]


def logo_row():
    """Row of real client logos on light (or dark) plates."""
    items = []
    for key, name, kind, dark in CLIENT_LOGOS:
        items.append('<span class="lplate%s"><img src="assets/img/clients/%s.png" alt="%s" loading="lazy"></span>'
                     % (" dark" if dark else "", key, name))
    return """<div class="wrap">
  <div class="logo-row">
    %s
  </div>
  <p style="text-align:center;margin-top:22px"><a class="btn sm" href="clients.html">Full client list &amp; pipeline <span class="arw">&rarr;</span></a></p>
</div>""" % "\n    ".join(items)


SILHOUETTE = ('<svg viewBox="0 0 100 120" aria-hidden="true"><path class="fill" d="M50 14a17 17 0 1 0 0 34 '
              '17 17 0 0 0 0-34Zm0 40c-19 0-34 12-36.5 29a3 3 0 0 0 3 3.4h67a3 3 0 0 0 3-3.4C84 66 69 54 50 54Z"/>'
              '</svg>')


# ----------------------------------------------------------------- partials
def nav(active):
    links = []
    for label, href in NAV_ITEMS:
        if label == active:
            links.append('<a href="%s" class="active" aria-current="page">%s</a>' % (href, label))
        else:
            links.append('<a href="%s">%s</a>' % (href, label))
    return """<header class="nav">
  <a class="brand" href="home.html">
    <span class="mark imgmark"><img src="assets/img/logo.png" alt="Jiks Academy — home"></span>
    <span class="brand-txt"><b>Jiks</b><span>Academy &mdash; estd 2025</span></span>
  </a>
  <nav class="nav-links" aria-label="Primary">
    %s
  </nav>
  <div class="nav-cta">
    <a class="btn" href="contact.html">Work with us <span class="arw">&rarr;</span></a>
  </div>
  <button class="burger" aria-label="Open menu" aria-expanded="false" aria-controls="mobile-menu"><i></i><i></i></button>
</header>

<nav class="mobile" id="mobile-menu" aria-label="Mobile" aria-hidden="true">
  <a href="home.html">Home</a>
  <a href="about.html">About</a>
  <a href="ventures.html">Ventures</a>
  <a href="crew.html">Crew</a>
  <a href="hector.html">Hector</a>
  <a href="services.html">Services</a>
  <a href="contact.html">Contact</a>
  <div class="m-sub">
    <a class="btn sm" href="east-rand-academy.html">East Rand Academy</a>
    <a class="btn sm" href="daveyton-stance-society.html">Daveyton Stance Society</a>
  </div>
</nav>
""" % ("\n    ".join(links))


FOOTER = """<footer>
  <div class="wrap">
    <div class="f-grid">
      <div>
        <img class="f-logo" src="assets/img/logo.png" alt="Jiks Academy">
        <p style="color:var(--bone-dim);max-width:36ch;font-size:15px">A creative house for the culture coming out of the East Rand. Home of East Rand Academy and Daveyton Stance Society.</p>
        <ul style="margin-top:18px">
          <li><a href="mailto:__EMAIL__">__EMAIL__</a></li>
          <li><a href="tel:__PHONE_HREF__">__PHONE__</a></li>
        </ul>
      </div>
      <div>
        <h2>Movements</h2>
        <ul>
          <li><a href="east-rand-academy.html">East Rand Academy</a></li>
          <li><a href="daveyton-stance-society.html">Daveyton Stance Society</a></li>
          <li><a href="ventures.html">All ventures</a></li>
        </ul>
      </div>
      <div>
        <h2>The crew</h2>
        <ul>
          <li><a href="shadrack-makamu.html">Shadrack Makamu</a></li>
          <li><a href="kgotso-matlakala.html">Kgotso Matlakala</a></li>
          <li><a href="skhumbuzo.html">Skhumbuzo</a></li>
        </ul>
      </div>
      <div>
        <h2>More</h2>
        <ul>
          <li><a href="about.html">About</a></li>
          <li><a href="services.html">Services</a></li>
          <li><a href="clients.html">Clients &amp; pipeline</a></li>
          <li><a href="hector.html">Hector &mdash; MC &amp; Speaker</a></li>
          <li><a href="contact.html">Contact</a></li>
        </ul>
      </div>
    </div>
    __ALL_PAGES__    <div class="f-big">Let's build<span>.</span></div>
    <div class="f-legal">
      <span>&copy; <span data-year>2026</span> Jiks Academy</span>
      <span>Daveyton &middot; East Rand &middot; Gauteng</span>
      <span>Ground up, not top down</span>
    </div>
  </div>
</footer>"""


# Set True to ship one combined stylesheet (main.css) instead of three.
SINGLE_CSS = False


def head_block(title, desc, ogimg, extra=""):
    """Everything from <!DOCTYPE> to </head>, shared by normal pages and the cover."""
    css = ('<link rel="stylesheet" href="assets/css/main.css">\n' if SINGLE_CSS else
           '<link rel="stylesheet" href="assets/css/base.css">\n'
           '<link rel="stylesheet" href="assets/css/components.css">\n'
           '<link rel="stylesheet" href="assets/css/pages.css">\n')
    return ('<!DOCTYPE html>\n<html lang="en">\n<head>\n'
            '<meta charset="utf-8">\n'
            '<meta name="viewport" content="width=device-width, initial-scale=1">\n'
            '<meta name="color-scheme" content="dark">\n'
            '<title>__T__</title>\n'
            '<meta name="description" content="__D__">\n'
            '<link rel="icon" type="image/png" href="assets/img/favicon.png">\n'
            '<link rel="apple-touch-icon" href="assets/img/apple-touch-icon.png">\n'
            '<link rel="manifest" href="site.webmanifest">\n'
            '<meta name="theme-color" content="#04060e">\n'
            '<meta property="og:type" content="website">\n'
            '<meta property="og:site_name" content="Jiks Academy">\n'
            '<meta property="og:title" content="__T__">\n'
            '<meta property="og:description" content="__D__">\n'
            '<meta property="og:image" content="__OG__">\n'
            '<meta name="twitter:card" content="summary_large_image">\n'
            '<meta name="twitter:title" content="__T__">\n'
            '<meta name="twitter:description" content="__D__">\n'
            '<meta name="twitter:image" content="__OG__">\n'
            '<link rel="preconnect" href="https://fonts.googleapis.com">\n'
            '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>\n'
            '<link href="https://fonts.googleapis.com/css2?family=Anton&family=Inter:wght@400;500;600&family=IBM+Plex+Mono:wght@400;500&display=swap" rel="stylesheet">\n'
            + css + extra +
            '</head>\n<body>\n'
            ).replace('__T__', title).replace('__D__', desc).replace('__OG__', ogimg)


def tidy(doc):
    """Keep purely decorative elements out of the accessibility tree."""
    for old, new in (
        ('<span class="arw">', '<span class="arw" aria-hidden="true">'),
        ('<span class="mono-mark">', '<span class="mono-mark" aria-hidden="true">'),
        ('<span class="idx">', '<span class="idx" aria-hidden="true">'),
        ('<span class="initials">', '<span class="initials" aria-hidden="true">'),
        ('<span class="n">', '<span class="n" aria-hidden="true">'),
        ('<div class="marquee track">', '<div class="marquee track" aria-hidden="true">'),
        ('<div class="scroll-cue">', '<div class="scroll-cue" aria-hidden="true">'),
        ('<div class="hazard">', '<div class="hazard" aria-hidden="true">'),
        ('<i>&rarr;</i>', '<i aria-hidden="true">&rarr;</i>'),
        ('<i>&larr;</i>', '<i aria-hidden="true">&larr;</i>'),
        ('<svg viewBox="0 0 100 120" aria-hidden="true">',
         '<svg viewBox="0 0 100 120" aria-hidden="true" focusable="false">'),
    ):
        doc = doc.replace(old, new)
    return doc


def page(title, desc, active, body, form=False, og="assets/img/hero.jpg"):
    js = '<script src="assets/js/form.js"></script>\n' if form else ''
    ogimg = (SITE_URL.rstrip("/") + "/" + og) if SITE_URL else og
    footer = (FOOTER.replace('__EMAIL__', EMAIL)
                    .replace('__PHONE_HREF__', PHONE_HREF)
                    .replace('__PHONE__', PHONE)
                    .replace('__ALL_PAGES__', footer_all_pages()))
    doc = (head_block(title, desc, ogimg)
           + '<a class="skip" href="#main">Skip to main content</a>\n\n'
           + nav(active) + '\n<main id="main" tabindex="-1">\n' + body + '\n</main>\n\n'
           + footer + '\n\n'
           '<script src="assets/js/nav.js"></script>\n'
           '<script src="assets/js/menu.js"></script>\n'
           '<script src="assets/js/reveal.js"></script>\n' + js +
           '</body>\n</html>\n')
    return tidy(doc)


def cover_page():
    """Full-bleed splash: the logo, then through to home.html."""
    body = """
<section class="cover" data-cover-to="home.html" data-cover-delay="5200">
  <div class="cover-bg tint"><img src="assets/img/hero.jpg" alt=""></div>
  <div class="cover-scrim"></div>
  <div class="cover-inner">
    <span class="cover-plate"><img src="assets/img/logo.png" alt="Jiks Academy" width="512" height="517"></span>
    <h1>Jiks Academy</h1>
    <p class="cover-tag">We back the builders</p>
    <a class="btn solid cover-enter" href="home.html">Enter the site <span class="arw">&rarr;</span></a>
    <div class="cover-bar" aria-hidden="true"><span data-progress></span></div>
    <p class="cover-note mono">Taking you through &mdash; or tap enter above</p>
    <p class="cover-meta">East Rand Academy &middot; Daveyton Stance Society &middot; Hector</p>
  </div>
</section>"""
    doc = (head_block("Jiks Academy — East Rand creative house",
                      "Jiks Academy — a creative house in Daveyton, East Rand. Home of East Rand Academy, "
                      "Daveyton Stance Society and Hector.",
                      (SITE_URL.rstrip("/") + "/assets/img/logo.png") if SITE_URL else "assets/img/logo.png",
                      extra='<link rel="stylesheet" href="assets/css/cover.css">\n')
           + '<main id="main" tabindex="-1">\n' + body + '\n</main>\n\n'
           '<script src="assets/js/cover.js"></script>\n'
           '</body>\n</html>\n')
    return tidy(doc)



def phead(bg, crumb, eyebrow, h1, h1_sub, chips):
    chip_html = "\n      ".join('<span class="chip">%s</span>' % c for c in chips)
    return """<section class="phead">
  <div class="phead-bg tint"><img src="%s" alt=""></div>
  <div class="phead-scrim"></div>
  <div class="wrap">
    <nav class="crumb" aria-label="Breadcrumb">%s</nav>
    <p class="eyebrow" style="margin-top:20px">%s</p>
    <h1>%s<br><span>%s</span></h1>
    <div class="sub">
      %s
    </div>
  </div>
</section>""" % (bg, crumb, eyebrow, h1, h1_sub, chip_html)


def cta(title, text, btn, href):
    return """<div class="cta-band">
  <h2>%s</h2>
  <p>%s</p>
  <a class="btn solid" href="%s">%s <span class="arw">&rarr;</span></a>
</div>""" % (title, text, href, btn)


# ----------------------------------------------------------------- crew data
CREW = [
    dict(
        slug="shadrack-makamu", name="Shadrack Makamu", sub="Head of Media",
        role="Head of Media &amp; Visuals", initials="SM",
        portrait="assets/img/crew/shadrack.jpg", kind="photo",
        bg="assets/img/academy.jpg",
        chips=["<b>Media &amp; Visuals</b>", "Film &middot; Photo &middot; Post", "Based in <b>Daveyton</b>"],
        meta=[("Based", PLACE), ("Discipline", "Film &middot; Photography &middot; Post-production"),
              ("Covers", "East Rand Academy &middot; Daveyton Stance Society")],
        bios=[
            "Shadrack Makamu runs the cameras, the edit suite and the look of everything Jiks Academy releases.",
            "If it's a shot of a build at golden hour, a live set cut to the beat or a portrait of an artist on the way up, it came through Shadrack. He decides how the East Rand looks on screen &mdash; and he holds that standard every time.",
        ],
        handles=[
            "Shooting and editing events, sessions and builds",
            "Photography for artist and vehicle features",
            "Post-production, colour and grading",
            "Keeping the visual identity consistent across both movements",
        ],
        quote="If it isn't shot properly,<br>it didn't happen. <span>Document everything.</span>",
    ),
    dict(
        slug="kgotso-matlakala", name="Kgotso Matlakala", sub="Events Lead",
        role="Events &amp; Operations Lead", initials="KM",
        portrait="assets/img/crew/kgotso.jpg", kind="photo",
        bg="assets/img/hero.jpg",
        chips=["<b>Events &amp; Operations</b>", "Logistics &middot; Production &middot; Safety", "Based in <b>Daveyton</b>"],
        meta=[("Based", PLACE), ("Discipline", "Logistics &middot; Production &middot; Safety"),
              ("Covers", "Stance meets &middot; Academy showcases &middot; Brand events")],
        bios=[
            "Kgotso Matlakala turns an empty lot into a venue by nightfall.",
            "He handles site, suppliers, security, run-of-show and every problem nobody else saw coming &mdash; the reason the doors open on time and the reason everybody gets home safely.",
            "From stance meets in Daveyton to academy showcase nights, Kgotso is the reason the plan survives contact with the day.",
        ],
        handles=[
            "Site, suppliers and supplier negotiation",
            "Run-of-show, stage management and timing",
            "Security, safety and crowd flow",
            "Load-in, load-out and everything that breaks in between",
        ],
        quote="Anyone can book a date.<br>Not everyone can <span>hold the floor</span> when it fills up.",
    ),
    dict(
        slug="skhumbuzo", name="Skhumbuzo", sub="Talent Liaison",
        role="Talent Liaison &amp; Community", initials="SK",
        portrait="assets/img/crew/skhumbuzo.jpg", kind="photo",
        bg="assets/img/stance.jpg",
        chips=["<b>Talent &amp; Community</b>", "Scouting &middot; Mentorship", "Based in <b>East Rand</b>"],
        meta=[("Based", PLACE), ("Discipline", "Scouting &middot; Mentorship &middot; Community"),
              ("Covers", "East Rand Academy roster &middot; Street scouting")],
        bios=[
            "Skhumbuzo is the link between the academy and the streets.",
            "He scouts new artists early, keeps the roster tight, and makes sure nobody from the East Rand gets left off a line-up they earned a place on.",
            "When a young artist needs someone to talk them through the unglamorous side of the industry, Skhumbuzo is the call.",
        ],
        handles=[
            "Scouting emerging artists and performers",
            "Mentorship and day-to-day artist support",
            "Line-ups, features and collaborations",
            "Community relationships across the East Rand",
        ],
        quote="Talent is everywhere.<br>Somebody has to go <span>find it</span> and stay with it.",
    ),
]

CREW_CARDS = {
    "shadrack-makamu": ('<img src="assets/img/crew/shadrack.jpg" alt="Shadrack Makamu">',
                        "Runs the cameras, the edit suite and the look of everything we release. If it's a build at golden hour or a live set cut to the beat, it came through Shadrack.",
                        ["Film", "Photo", "Post"]),
    "kgotso-matlakala": ('<img src="assets/img/crew/kgotso.jpg" alt="Kgotso Matlakala">',
                         "Turns a parking lot into a venue by nightfall. Handles site, suppliers, security, run-of-show and every problem nobody else saw coming.",
                         ["Logistics", "Production", "Safety"]),
    "skhumbuzo": ('<img src="assets/img/crew/skhumbuzo.jpg" alt="Skhumbuzo">',
                 "The link between the academy and the streets — scouts new artists, keeps the roster tight and makes sure nobody from the East Rand gets left off the line-up.",
                 ["Scouting", "Mentorship", "Community"]),
}


def crew_card(i, m):
    art, blurb, tags = CREW_CARDS[m["slug"]]
    tag_html = "".join('<span class="mini">%s</span>' % t for t in tags)
    return """<a class="member" href="%s.html">
        <span class="avatar">
          <span class="idx">%02d</span>
          %s
          <span class="initials">%s</span>
        </span>
        <h3>%s</h3>
        <span class="role">%s</span>
        <p>%s</p>
        <span class="tagsline">%s</span>
      </a>""" % (m["slug"], i, art, m["initials"], m["name"], m["role"], blurb, tag_html)


def crew_page(m, i):
    # Branch navigation: the first profile points back to the crew index, and so
    # does the last one. Between themselves they run in crew order.
    if i > 0:
        prev_slug, prev_name = CREW[i - 1]["slug"], CREW[i - 1]["name"]
    else:
        prev_slug, prev_name = "crew", "The Crew"
    if i + 1 < len(CREW):
        next_slug, next_name = CREW[i + 1]["slug"], CREW[i + 1]["name"]
    else:
        next_slug, next_name = "crew", "The Crew"

    if m["kind"] == "photo":
        art = """<figure class="portrait">
          <div class="ph tint"><img src="%s" alt="%s"><div class="scrim"></div></div>
          <figcaption class="badge"><b>%s</b><span>%s</span></figcaption>
        </figure>""" % (m["portrait"], m["name"], m["name"], m["sub"])
    else:
        art = """<figure class="portrait">
          <div class="silhouette">%s<span class="initials">%s</span></div>
          <figcaption class="badge" style="position:static;padding:16px 18px;border-top:1px solid var(--line)"><b>%s</b><span>%s</span></figcaption>
        </figure>""" % (SILHOUETTE, m["initials"], m["name"], m["sub"])

    meta_rows = "".join(
        '<div class="row"><span class="lbl">%s</span><span class="val">%s</span></div>' % (k, v)
        for k, v in m["meta"])

    bios = "".join("<p>%s</p>" % b for b in m["bios"])
    handles = "".join("<li><i>&rarr;</i> %s</li>" % h for h in m["handles"])

    body = phead(m["bg"],
                 '<a href="home.html">Home</a> &nbsp;/&nbsp; <a href="crew.html">Crew</a> &nbsp;/&nbsp; %s' % m["name"],
                 m["role"], m["name"], m["sub"], m["chips"])

    body += """
<section>
  <div class="wrap">
    <div class="profile rv">
      <div>
        %s
        <div class="p-meta">
          %s
        </div>
      </div>
      <div>
        <p class="eyebrow">The profile</p>
        <h2>%s</h2>
        <div class="prose" style="margin-top:22px">
          %s
        </div>
        <p class="eyebrow" style="margin-top:34px">What they handle</p>
        <ul class="checks" style="margin-top:14px">
          %s
        </ul>
      </div>
    </div>

    <div class="pull rv">%s</div>

    <div class="pager rv">
      <a href="%s.html"><span class="k">&larr; Previous</span><span class="n">%s</span></a>
      <a class="next" href="%s.html"><span class="k">Next &rarr;</span><span class="n">%s</span></a>
    </div>
  </div>
</section>

%s""" % (art, meta_rows, m["name"], bios, handles, m["quote"],
         prev_slug, prev_name, next_slug, next_name,
         cta("Work with us", "Projects, stages, campaigns or a build that needs covering &mdash; start the conversation.",
             "Get in touch", "contact.html"))

    return page("%s — Jiks Academy" % m["name"],
                "%s — %s at Jiks Academy, Daveyton, East Rand." % (m["name"], m["role"].replace("&amp;", "&")),
                "Crew", body)


# ----------------------------------------------------------------- pages
def home():
    cards = "\n      ".join(crew_card(i + 1, m) for i, m in enumerate(CREW))
    body = """
<section class="hero">
  <div class="hero-bg tint"><img src="assets/img/hero.jpg" alt="A modified stance car on a township street in Daveyton at golden hour"></div>
  <div class="hero-scrim"></div>
  <div class="hero-inner wrap">
    <p class="eyebrow">Re a go bona &mdash; we see you</p>
    <h1>We back<br>the <span class="stroke">builders</span></h1>
    <div class="hero-foot">
      <div>
        <p class="lede">Jiks Academy is a creative house built on the ground in Daveyton. We run two movements &mdash; <strong style="color:var(--bone)">East Rand Academy</strong> and <strong style="color:var(--bone)">Daveyton Stance Society</strong> &mdash; and we carry their stories through media, events, mentorship and brand storytelling.</p>
        <div class="hero-actions">
          <a class="btn solid" href="ventures.html">See the work <span class="arw">&rarr;</span></a>
          <a class="btn ghost-light" href="crew.html">Meet the crew <span class="arw">&rarr;</span></a>
        </div>
      </div>
      <div class="hero-meta">
        <span class="chip">Estd <b>2025</b></span>
        <span class="chip"><b>Daveyton</b> &middot; East Rand &middot; Gauteng</span>
        <span class="chip">Founder: <b>DJ ToxSA</b></span>
      </div>
    </div>
  </div>
  <div class="scroll-cue"><span></span>Scroll</div>
</section>

<div class="marquee track">
  <div class="mq">
    <span>Jiks Academy <i></i> East Rand Academy <i></i> Daveyton Stance Society <i></i> Media <i></i> Events <i></i> Mentorship <i></i> Stance Culture <i></i> Hector &mdash; MC &amp; Speaker <i></i></span>
    <span>Jiks Academy <i></i> East Rand Academy <i></i> Daveyton Stance Society <i></i> Media <i></i> Events <i></i> Mentorship <i></i> Stance Culture <i></i> Hector &mdash; MC &amp; Speaker <i></i></span>
  </div>
</div>

<section>
  <div class="wrap">
    <div class="sec-head rv">
      <div>
        <p class="eyebrow">Who we are</p>
        <h2>Ground up,<br>not top down</h2>
      </div>
      <div class="max">
        <p class="lede">We are not an agency that visits the East Rand for a campaign. We live here, we build here, and everything we put out has to make sense to the people on the corner first. <a href="about.html" style="color:var(--cyan)">More about us &rarr;</a></p>
      </div>
    </div>

    <div class="beliefs rv">
      <article class="belief">
        <span class="num">01 / Kasi first</span>
        <h3>We build from where we stand</h3>
        <p>Talent in the East Rand has never been the problem. Access has. Everything we make starts with the community it comes from.</p>
      </article>
      <article class="belief">
        <span class="num">02 / Culture is the client</span>
        <h3>We protect the sound</h3>
        <p>From amapiano studios to fitment and stance culture, we treat local culture as the brief, not the decoration.</p>
      </article>
      <article class="belief">
        <span class="num">03 / Earn permission</span>
        <h3>Attention is borrowed</h3>
        <p>The best marketing asks before it shouts. We lead with servanthood, humility and real relationships.</p>
      </article>
      <article class="belief">
        <span class="num">04 / Legacy over likes</span>
        <h3>Build people, not posts</h3>
        <p>Every project should leave something behind: a skill, a stage, a credit, a connection.</p>
      </article>
    </div>
  </div>
</section>

<div class="band">
  <div class="wrap">
    <div class="statement rv">
      <img src="assets/img/logo.png" alt="Jiks Academy" style="width:clamp(96px,12vw,150px);margin:0 auto 26px">
      <h2>We've been building in the background. <span>Now we turn it up.</span></h2>
      <p>Two movements. One crew. A media team, an event floor and a mentorship pipeline for the artists, drivers and makers of the East Rand.</p>
    </div>
  </div>
</div>

<section>
  <div class="wrap">
    <div class="sec-head rv">
      <div>
        <p class="eyebrow">Featured work</p>
        <h2>The<br>ventures</h2>
      </div>
      <div class="max">
        <p class="lede">Two properties, two audiences, one operating system. Both started by Innocent Tlhatlhedi (DJ ToxSA). <a href="ventures.html" style="color:var(--cyan)">All ventures &rarr;</a></p>
      </div>
    </div>

    <div class="ventures rv">
      <a class="venture" href="east-rand-academy.html">
        <div class="thumb tint">
          <span class="tag">Music &middot; Mentorship</span>
          <img src="assets/img/academy.jpg" alt="Young artists recording in a community studio">
          <div class="scrim"></div>
        </div>
        <div class="body">
          <h3>East Rand Academy</h3>
          <div class="meta">
            <span class="chip">Founded <b>14 April 2024</b></span>
            <span class="chip">Founder <b>DJ ToxSA</b></span>
          </div>
          <p>A creative movement built to uplift and support upcoming artists from the East Rand &mdash; a place for emerging musicians, creatives and performers to grow, collaborate and be seen.</p>
          <span class="go">View the movement <span class="arw">&rarr;</span></span>
        </div>
      </a>

      <a class="venture" href="daveyton-stance-society.html">
        <div class="thumb tint">
          <span class="tag">Automotive &middot; Events</span>
          <img src="assets/img/stance.jpg" alt="Modified stance cars lined up at night">
          <div class="scrim"></div>
        </div>
        <div class="body">
          <h3>Daveyton Stance Society</h3>
          <div class="meta">
            <span class="chip">Founded <b>2023</b></span>
            <span class="chip">Co-founder <b>DJ ToxSA</b></span>
          </div>
          <p>From a Facebook group sharing build pictures to a full media team, event curation house and recognised stance culture hub putting Daveyton on the map.</p>
          <span class="go">View the movement <span class="arw">&rarr;</span></span>
        </div>
      </a>
    </div>
  </div>
</section>

<section style="background:rgba(8,14,36,.55);border-block:1px solid var(--line)">
  <div class="wrap">
    <div class="sec-head rv">
      <div>
        <p class="eyebrow">The crew</p>
        <h2>People<br>behind it</h2>
      </div>
      <div class="max">
        <p class="lede">No faceless agency here. These are the people you'll find on site at 6am, editing at 2am and holding the line at the gate. <a href="crew.html" style="color:var(--cyan)">Full crew &rarr;</a></p>
      </div>
    </div>
    <div class="crew rv">
      %s
    </div>
  </div>
</section>

<section>
  <div class="wrap">
    <div class="hector-feat rv">
      <figure class="ph tint">
        <img src="assets/img/hector-portrait.jpg" alt="Hector, MC and motivational speaker" width="493" height="695">
        <div class="scrim"></div>
        <figcaption><b>Hector</b>MC &amp; Motivational Speaker</figcaption>
      </figure>
      <div>
        <p class="eyebrow">On the roster</p>
        <h2>The voice<br>on <span>your stage</span></h2>
        <p class="lede" style="margin:22px 0 26px">Hector is an MC and motivational speaker who carries rooms &mdash; corporate, institutional and cultural. He reads the room, he carries the message, he elevates the experience.</p>
        <ul class="checks">
          <li><i>&rarr;</i> Commanding, confident stage presence</li>
          <li><i>&rarr;</i> Sharp communication and impeccable delivery</li>
          <li><i>&rarr;</i> Natural audience connection through humour and insight</li>
          <li><i>&rarr;</i> Trusted brand and institutional representation</li>
          <li><i>&rarr;</i> Calm, professional leadership under pressure</li>
        </ul>
        <div class="hero-actions">
          <a class="btn solid" href="hector.html">Full profile <span class="arw">&rarr;</span></a>
          <a class="btn ghost-light" href="contact.html">Check availability <span class="arw">&rarr;</span></a>
        </div>
      </div>
    </div>
  </div>
</section>

<section style="background:rgba(8,14,36,.55);border-block:1px solid var(--line)">
  <div class="wrap">
    <div class="sec-head rv">
      <div>
        <p class="eyebrow">What we do</p>
        <h2>How we<br>show up</h2>
      </div>
      <div class="max">
        <p class="lede">Four disciplines, one crew. We can run a single piece of content or a full cultural campaign end to end. <a href="services.html" style="color:var(--cyan)">All services &rarr;</a></p>
      </div>
    </div>
    <div class="svc rv">
      <article class="svc-item"><span class="k">01</span><h3>Media &amp; Content</h3><p>Photography, video, reels and documentary coverage of builds, sessions and live events &mdash; shot on the ground, cut for the timeline.</p></article>
      <article class="svc-item"><span class="k">02</span><h3>Event Curation</h3><p>Concept, line-up, site, suppliers and run-of-show. From a stance meet in a lot to a full stage programme.</p></article>
      <article class="svc-item"><span class="k">03</span><h3>Talent &amp; Mentorship</h3><p>Finding emerging artists and builders early, then giving them the rooms, the rig and the guidance to hold a career.</p></article>
      <article class="svc-item"><span class="k">04</span><h3>Brand Storytelling</h3><p>Partnering with brands that want genuine access to East Rand culture &mdash; campaigns built with the community, not parachuted into it.</p></article>
    </div>
  </div>
</section>

%s

%s""" % (cards, logo_row(), cta("What are we building?", "A project, a stage, a campaign or a build you need covered &mdash; tell us what you're working on.", "Start a project", "contact.html"))
    return page("Jiks Academy — We Back The Builders",
                "Jiks Academy is a creative house in Daveyton, Gauteng. Home of East Rand Academy and Daveyton Stance Society — media, events, mentorship and brand storytelling from the East Rand.",
                "Home", body)


def about():
    body = phead("assets/img/crowd.jpg", '<a href="home.html">Home</a> &nbsp;/&nbsp; About',
                 "Who we are", "Ground up,", "not top down",
                 ["Estd <b>2025</b>", "Based in <b>Daveyton</b>", "Two movements &middot; one crew"])
    body += """
<section>
  <div class="wrap">
    <div class="cols rv">
      <div class="prose">
        <p><strong>Jiks Academy is a creative house built on the ground in Daveyton, on the East Rand.</strong></p>
        <p>We are not an agency that visits the East Rand for a campaign. We live here, we build here, and everything we put out has to make sense to the people on the corner first.</p>
        <p>Our work runs through two movements: <strong>East Rand Academy</strong>, founded on 14 April 2024 to uplift upcoming artists, and <strong>Daveyton Stance Society</strong>, founded in 2023 as an automotive and stance culture hub. Both were started by Innocent Tlhatlhedi &mdash; DJ ToxSA.</p>
        <p>We champion local languages because language is belonging. We lead with servanthood because the work is an act of stewardship. We serve with humility because the best marketing earns permission instead of demanding attention.</p>
      </div>
      <div>
        <figure class="tint" style="border:1px solid var(--line);position:relative">
          <img src="assets/img/hero.jpg" alt="Daveyton street scene at golden hour">
          <div class="scrim" style="background:linear-gradient(180deg,transparent 60%%,rgba(4,6,14,.7))"></div>
        </figure>
        <figcaption>Daveyton, East Rand</figcaption>
      </div>
    </div>

    <div class="pull rv">Our work is worship. Our clients are partners. <span>Our mission is impact.</span></div>

    <div class="sec-head rv" style="margin-bottom:28px">
      <div><p class="eyebrow">What we believe</p><h2>Four<br>commitments</h2></div>
      <div class="max"><p class="lede">These are the rules we actually run the house by.</p></div>
    </div>

    <div class="beliefs rv">
      <article class="belief">
        <span class="num">01 / Kasi first</span>
        <h3>We build from where we stand</h3>
        <p>Talent in the East Rand has never been the problem. Access has. Everything we make starts with the community it comes from and the people it is meant to open doors for.</p>
      </article>
      <article class="belief">
        <span class="num">02 / Culture is the client</span>
        <h3>We protect the sound</h3>
        <p>From amapiano studios to fitment and stance culture, we treat local culture as the brief, not the decoration. The work has to be true before it is clever.</p>
      </article>
      <article class="belief">
        <span class="num">03 / Earn permission</span>
        <h3>Attention is borrowed</h3>
        <p>The best marketing asks before it shouts. We lead with servanthood, humility and real relationships &mdash; with artists, builders, brands and the neighbourhoods that host us.</p>
      </article>
      <article class="belief">
        <span class="num">04 / Legacy over likes</span>
        <h3>Build people, not posts</h3>
        <p>Every project should leave something behind: a skill, a stage, a credit, a connection. If the next generation is not better off, we missed the point.</p>
      </article>
    </div>

    <div class="stats rv">
      <div class="stat"><b>2023</b><span>Daveyton Stance Society founded</span></div>
      <div class="stat"><b>14.04</b><span>East Rand Academy founded</span></div>
      <div class="stat"><b>02</b><span>Movements under one roof</span></div>
      <div class="stat"><b>100%%</b><span>Grown in the East Rand</span></div>
    </div>
  </div>
</section>

<section style="background:rgba(8,14,36,.55);border-block:1px solid var(--line)">
  <div class="wrap">
    <div class="sec-head rv">
      <div><p class="eyebrow">The road so far</p><h2>Marks on<br>the wall</h2></div>
      <div class="max"><p class="lede">From a Facebook group to a creative house with a media team, an event floor and a mentorship pipeline.</p></div>
    </div>
    <div class="timeline rv">
      <div class="tl">
        <span class="yr">2023</span>
        <div><h3>Daveyton Stance Society</h3><p>Innocent Tlhatlhedi (DJ ToxSA) and Thato Leroy Ngobeza start a Facebook group sharing pictures of stance cars and builds. It grows into a media team, an event curating team and a stance culture hub.</p></div>
      </div>
      <div class="tl">
        <span class="yr">2024</span>
        <div><h3>East Rand Academy</h3><p>On 14 April 2024, DJ ToxSA founds a creative movement to uplift and support upcoming artists from the East Rand &mdash; musicians, creatives and performers overlooked by the mainstream industry.</p></div>
      </div>
      <div class="tl">
        <span class="yr">2025</span>
        <div><h3>Jiks Academy</h3><p>Both movements come under one roof: one crew, one media pipeline, one events floor &mdash; and a brand to carry the culture coming out of the East Rand.</p></div>
      </div>
      <div class="tl">
        <span class="yr">Now</span>
        <div><h3>Building the legacy</h3><p>Music, events, mentorship and brand storytelling &mdash; with Hector on the roster carrying stages across the country.</p></div>
      </div>
    </div>
  </div>
</section>

%s""" % cta("Work with us", "Projects, stages, campaigns or a build that needs covering &mdash; start the conversation.", "Get in touch", "contact.html")
    return page("About — Jiks Academy",
                "Jiks Academy is a creative house in Daveyton, East Rand — home of East Rand Academy and Daveyton Stance Society.",
                "About", body)


def ventures():
    body = phead("assets/img/hero.jpg", '<a href="home.html">Home</a> &nbsp;/&nbsp; Ventures',
                 "Featured work", "The", "ventures",
                 ["<b>02</b> movements", "Founded <b>2023 &amp; 2024</b>", "Based in <b>Daveyton</b>"])
    body += """
<section>
  <div class="wrap">
    <div class="sec-head rv">
      <div><p class="eyebrow">What we run</p><h2>Two<br>properties</h2></div>
      <div class="max"><p class="lede">Two audiences, one operating system. Both were ere started by Innocent Tlhatlhedi (DJ ToxSA) &mdash; both exist to move people from the margins to the main stage.</p></div>
    </div>

    <div class="ventures rv">
      <a class="venture" href="east-rand-academy.html">
        <div class="thumb tint">
          <span class="tag">Music &middot; Mentorship</span>
          <img src="assets/img/academy.jpg" alt="Young artists recording in a community studio">
          <div class="scrim"></div>
        </div>
        <div class="body">
          <h3>East Rand Academy</h3>
          <div class="meta">
            <span class="chip">Founded <b>14 April 2024</b></span>
            <span class="chip">Founder <b>DJ ToxSA</b></span>
          </div>
          <p>A creative movement built to uplift and support upcoming artists from the East Rand &mdash; giving emerging musicians, creatives and performers a place to grow, collaborate and gain visibility.</p>
          <span class="go">View the movement <span class="arw">&rarr;</span></span>
        </div>
      </a>

      <a class="venture" href="daveyton-stance-society.html">
        <div class="thumb tint">
          <span class="tag">Automotive &middot; Events</span>
          <img src="assets/img/stance.jpg" alt="Modified stance cars lined up at night">
          <div class="scrim"></div>
        </div>
        <div class="body">
          <h3>Daveyton Stance Society</h3>
          <div class="meta">
            <span class="chip">Founded <b>2023</b></span>
            <span class="chip">Co-founders <b>DJ ToxSA &amp; Thato Leroy Ngobeza</b></span>
          </div>
          <p>From a Facebook group sharing build pictures to a full media team, event curating team and recognised stance culture hub putting Daveyton on the map.</p>
          <span class="go">View the movement <span class="arw">&rarr;</span></span>
        </div>
      </a>
    </div>
  </div>
</section>

%s""" % cta("Got a third one in you?", "If you're building something on the East Rand that deserves a stage, let's talk about it.", "Start a project", "contact.html")
    return page("Ventures — Jiks Academy",
                "The ventures of Jiks Academy: East Rand Academy and Daveyton Stance Society.",
                "Ventures", body)


def east_rand_academy():
    body = phead("assets/img/academy.jpg",
                 '<a href="home.html">Home</a> &nbsp;/&nbsp; <a href="ventures.html">Ventures</a> &nbsp;/&nbsp; Movement 01',
                 "Founded 14 April 2024", "East Rand", "Academy",
                 ["Founder: <b>Innocent Tlhatlhedi &mdash; DJ ToxSA</b>", "Based in <b>Daveyton</b>", "Music &middot; Creatives &middot; Performers"])
    body += """
<section>
  <div class="wrap">
    <div class="cols rv">
      <div class="prose">
        <p><strong>East Rand Academy is a creative movement founded by Innocent Tlhatlhed, popularly known as DJ ToxSA, on 14 April 2024.</strong></p>
        <p>The academy was established with one clear purpose: <strong>to uplift and support upcoming artists from the East Rand</strong>. Recognising the talent, passion and potential within communities across the East Rand, DJ ToxSA created East Rand Academy as a platform where emerging musicians, creatives and performers can grow, collaborate and gain visibility.</p>
        <p>Since its founding, the movement has focused on providing opportunities, resources and a sense of community for young artists who are often overlooked by the mainstream industry. East Rand Academy aims to nurture local talent and showcase the unique sound and culture coming out of the East Rand.</p>
      </div>
      <div>
        <figure class="tint" style="border:1px solid var(--line);position:relative">
          <img src="assets/img/academy.jpg" alt="Artists recording in a small studio">
        </figure>
        <figcaption>In session &mdash; East Rand</figcaption>
      </div>
    </div>

    <div class="pull rv">Through music, events and mentorship, East Rand Academy continues to build a legacy of <span>empowering the next generation</span> of artists.</div>

    <div class="sec-head rv" style="margin-bottom:28px">
      <div><p class="eyebrow">What we actually do</p><h2>Three<br>promises</h2></div>
      <div class="max"><p class="lede">Not a label, not a school &mdash; a working platform. Here is what an artist gets when they come through the academy.</p></div>
    </div>

    <div class="beliefs rv">
      <article class="belief">
        <span class="num">01 / Opportunity</span>
        <h3>A stage, not a waiting room</h3>
        <p>Performance slots, studio time, features and introductions. We put artists in front of real audiences instead of telling them to wait their turn.</p>
      </article>
      <article class="belief">
        <span class="num">02 / Resources</span>
        <h3>The gear and the know-how</h3>
        <p>Access to equipment, media and production support &mdash; plus the unglamorous knowledge about how the industry actually works.</p>
      </article>
      <article class="belief">
        <span class="num">03 / Community</span>
        <h3>You are not doing this alone</h3>
        <p>A room full of people making the same bet on themselves. Collaboration over competition, and a crew that shows up for each other.</p>
      </article>
    </div>
  </div>
</section>

<section style="background:rgba(8,14,36,.55);border-block:1px solid var(--line)">
  <div class="wrap">
    <div class="sec-head rv">
      <div><p class="eyebrow">The road so far</p><h2>Marks on<br>the wall</h2></div>
      <div class="max"><p class="lede">From an idea in Daveyton to a movement with a media team behind it.</p></div>
    </div>
    <div class="timeline rv">
      <div class="tl">
        <span class="yr">2024</span>
        <div><h3>14 April &mdash; the academy opens its doors</h3><p>DJ ToxSA founds East Rand Academy with a single mandate: uplift and support upcoming artists from the East Rand. The first sessions run out of borrowed rooms and borrowed gear.</p></div>
      </div>
      <div class="tl">
        <span class="yr">2024</span>
        <div><h3>First showcase</h3><p>A platform night for emerging musicians, creatives and performers from across the East Rand &mdash; the first time many of them play to a room of their own.</p></div>
      </div>
      <div class="tl">
        <span class="yr">2025</span>
        <div><h3>Media &amp; mentorship pipeline</h3><p>The crew behind Daveyton Stance Society steps in with cameras, edit suites and event muscle. Artists start leaving with content, not just memories.</p></div>
      </div>
      <div class="tl">
        <span class="yr">Now</span>
        <div><h3>Building the legacy</h3><p>Music, events and mentorship &mdash; a growing roster of East Rand artists, and a culture that is starting to get the attention it always deserved.</p></div>
      </div>
    </div>
  </div>
</section>

%s""" % cta("Artist? Pull up.", "If you're making music, performing or building something creative on the East Rand, there's a seat for you.", "Join the academy", "contact.html")
    return page("East Rand Academy — Jiks Academy",
                "East Rand Academy is a creative movement founded by DJ ToxSA on 14 April 2024 to uplift and support upcoming artists from the East Rand.",
                "Ventures", body)


def daveyton_stance():
    body = phead("assets/img/stance.jpg",
                 '<a href="home.html">Home</a> &nbsp;/&nbsp; <a href="ventures.html">Ventures</a> &nbsp;/&nbsp; Movement 02',
                 "Founded 2023", "Daveyton", "Stance Society",
                 ["Founders: <b>Innocent Tlhatlhedi (DJ ToxSA)</b> &amp; <b>Thato Leroy Ngobeza</b>",
                  "Based in <b>Daveyton</b>", "Automotive &middot; Media &middot; Events"])
    body += """
<section>
  <div class="wrap">
    <div class="cols rv">
      <div class="prose">
        <p><strong>Daveyton Stance Society is an automotive movement founded in 2023 by Innocent Tlhatlhedi (DJ ToxSA) and Thato Leroy Ngobeza.</strong></p>
        <p>The movement began as a Facebook group where both founders shared pictures of stance cars and builds. What started as a space to admire the beauty of modified cars and the automotive industry quickly grew into something much bigger.</p>
        <p>Over time, Daveyton Stance Society evolved from an online community into a full <strong>media team, event curating team, and a recognised stance culture hub in Daveyton</strong>. The society became a home for car enthusiasts who appreciate style, fitment, and the art of building unique vehicles.</p>
        <p>With growing momentum, Daveyton Stance Society has collaborated with major stance event curators and stance drivers across the <strong>East Rand</strong>, helping to put Daveyton on the map as a key centre for stance culture.</p>
      </div>
      <div>
        <figure class="tint" style="border:1px solid var(--line);position:relative">
          <img src="assets/img/stance.jpg" alt="Stance cars at a night meet">
        </figure>
        <figcaption>Night meet &mdash; Daveyton</figcaption>
      </div>
    </div>

    <div class="pull rv">The movement continues to celebrate creativity, community, and the passion for automotive expression &mdash; <span>uniting car lovers and inspiring the next generation of builders</span> in the East Rand and beyond.</div>

    <div class="sec-head rv" style="margin-bottom:28px">
      <div><p class="eyebrow">What the society is now</p><h2>Three<br>engines</h2></div>
      <div class="max"><p class="lede">A group chat that grew teeth. What runs behind the badge today.</p></div>
    </div>

    <div class="beliefs rv">
      <article class="belief">
        <span class="num">01 / Media team</span>
        <h3>Documenting the builds</h3>
        <p>Photography, video and coverage of cars, meets and the people behind the metal. If a build is worth doing, it's worth shooting properly.</p>
      </article>
      <article class="belief">
        <span class="num">02 / Event curating</span>
        <h3>Building the floor</h3>
        <p>Concept, curation and delivery of stance events &mdash; working with major curators and drivers across the East Rand to run days that people talk about for months.</p>
      </article>
      <article class="belief">
        <span class="num">03 / Culture hub</span>
        <h3>Home for the enthusiasts</h3>
        <p>A place for people who care about style, fitment and the art of building something that is unmistakably theirs.</p>
      </article>
    </div>
  </div>
</section>

<section style="background:rgba(8,14,36,.55);border-block:1px solid var(--line)">
  <div class="wrap">
    <div class="sec-head rv">
      <div><p class="eyebrow">From group chat to hub</p><h2>The<br>build-up</h2></div>
      <div class="max"><p class="lede">Nobody handed us a venue. Here is how it happened.</p></div>
    </div>
    <div class="timeline rv">
      <div class="tl">
        <span class="yr">2023</span>
        <div><h3>A Facebook group and a camera phone</h3><p>Innocent Tlhatlhedi (DJ ToxSA) and Thato Leroy Ngobeza start sharing pictures of stance cars and builds. The comment section does the rest.</p></div>
      </div>
      <div class="tl">
        <span class="yr">2023</span>
        <div><h3>From timeline to tar</h3><p>The online community starts meeting in person. First meets are small, loud and full of cars that took years to build.</p></div>
      </div>
      <div class="tl">
        <span class="yr">2024</span>
        <div><h3>Media and events, formally</h3><p>The society becomes a working media team and event curating team, collaborating with major stance curators and drivers across the East Rand.</p></div>
      </div>
      <div class="tl">
        <span class="yr">Now</span>
        <div><h3>Daveyton on the map</h3><p>A recognised stance culture hub, inspiring the next generation of builders in the East Rand and beyond.</p></div>
      </div>
    </div>
  </div>
</section>

%s""" % cta("Building something?", "Cars, content or a collaboration &mdash; if it's stance and it's on the East Rand, we want to see it.", "Get in touch", "contact.html")
    return page("Daveyton Stance Society — Jiks Academy",
                "Daveyton Stance Society is an automotive movement founded in 2023 by DJ ToxSA and Thato Leroy Ngobeza — a media team, event curating team and stance culture hub in Daveyton.",
                "Ventures", body)


def crew_index():
    cards = "\n      ".join(crew_card(i + 1, m) for i, m in enumerate(CREW))
    body = phead("assets/img/crowd.jpg", '<a href="home.html">Home</a> &nbsp;/&nbsp; Crew',
                 "The crew", "People", "behind it",
                 ["<b>03</b> people", "Based in <b>Daveyton</b>", "Media &middot; Events &middot; Talent"])
    body += """
<section>
  <div class="wrap">
    <div class="sec-head rv">
      <div><p class="eyebrow">No faceless agency</p><h2>The<br>people</h2></div>
      <div class="max"><p class="lede">These are the people you'll find on site at 6am, editing at 2am and holding the line at the gate. Every one of them has their own page.</p></div>
    </div>
    <div class="crew rv">
      %s
    </div>
  </div>
</section>

%s""" % (cards, cta("Want in?", "Photographers, videographers, stage managers, drivers &mdash; if you're building on the East Rand, come and find us.", "Get in touch", "contact.html"))
    return page("The Crew — Jiks Academy",
                "The crew behind Jiks Academy: Innocent Tlhatlhedi (DJ ToxSA), Shadrack Makamu, Kgotso Matlakala and Skhumbuzo.",
                "Crew", body)


def services():
    rows = [
        ("01", "Media &amp; Content", "assets/img/academy.jpg",
         "Photography, video, reels and documentary coverage of builds, sessions and live events &mdash; shot on the ground, cut for the timeline. We cover stance meets, studio sessions, showcases and brand activations, and we deliver assets that are ready to post the same week.",
         ["Event and build coverage", "Artist portraits and session films", "Reels, cuts and social deliverables", "Colour, grade and post-production"]),
        ("02", "Event Curation", "assets/img/crowd.jpg",
         "Concept, line-up, site, suppliers and run-of-show. From a stance meet in a lot to a full stage programme with a live audience &mdash; we plan it, staff it and hold it together on the day.",
         ["Concept and curation", "Site, suppliers and permits", "Run-of-show and stage management", "Security, safety and crowd flow"]),
        ("03", "Talent &amp; Mentorship", "assets/img/crowd.jpg",
         "Finding emerging artists and builders early, then giving them the rooms, the rig and the guidance to hold a career. Run through East Rand Academy, mentorship is hands-on and long-term.",
         ["Scouting and onboarding", "Mentorship and career guidance", "Studio and stage access", "Collaborations and features"]),
        ("04", "Brand Storytelling", "assets/img/stance.jpg",
         "Partnering with brands that want genuine access to East Rand culture &mdash; campaigns built with the community, not parachuted into it. Strategy, production and distribution in one crew.",
         ["Cultural strategy and insight", "Campaign concept and production", "Community and influencer access", "Measurement that means something"]),
    ]
    html_rows = []
    for i, (num, title, img, copy, bullets) in enumerate(rows):
        lis = "".join("<li><i>&rarr;</i> %s</li>" % b for b in bullets)
        flipped = " flipped" if i % 2 else ""
        html_rows.append("""<div class="svc-row%s rv">
      <div>
        <span class="num">%s</span>
        <h3>%s</h3>
        <p>%s</p>
        <ul class="checks" style="margin-top:22px">%s</ul>
      </div>
      <figure class="ph tint">
        <div class="ph-in"><img src="%s" alt="%s" loading="lazy"></div>
      </figure>
    </div>""" % (flipped, num, title, copy, lis, img, title))

    body = phead("assets/img/crowd.jpg", '<a href="home.html">Home</a> &nbsp;/&nbsp; Services',
                 "What we do", "How we", "show up",
                 ["<b>04</b> disciplines", "One crew", "Based in <b>Daveyton</b>"])
    body += """
<section>
  <div class="wrap">
    <div class="sec-head rv">
      <div><p class="eyebrow">Services</p><h2>End to end,<br>or one piece</h2></div>
      <div class="max"><p class="lede">We can run a single shoot or a full cultural campaign. Everything is delivered by the same crew that lives here.</p></div>
    </div>
    %s
  </div>
</section>

%s""" % ("\n    ".join(html_rows),
         cta("Let's scope it", "Tell us the dates, the room and the outcome you need. We'll come back with a plan.", "Start a project", "contact.html"))
    return page("Services — Jiks Academy",
                "Jiks Academy offers media and content, event curation, talent and mentorship, and brand storytelling from the East Rand.",
                "Services", body)


def contact():
    body = phead("assets/img/crowd.jpg", '<a href="home.html">Home</a> &nbsp;/&nbsp; Contact',
                 "Let's work", "What are", "we building?",
                 ["Reply within <b>24 hours</b>", "Based in <b>Daveyton</b>", "Nationwide travel"])
    body += """
<section>
  <div class="wrap">
    <div class="contact rv">
      <div>
        <p class="eyebrow">Contact</p>
        <h2>Start the<br><span>conversation</span></h2>
        <p class="lede" style="margin-top:22px;max-width:44ch">A project, a stage, a campaign or a build you need covered &mdash; tell us what you're working on and we'll come back to you within 24 hours.</p>
        <div class="deets">
          <div class="deet"><span class="lbl">Email</span><a class="val" href="mailto:%s">%s</a></div>
          <div class="deet"><span class="lbl">Phone</span><a class="val" href="tel:%s">%s</a></div>
          <div class="deet"><span class="lbl">Based in</span><span class="val">%s</span></div>
          <div class="deet"><span class="lbl">Bookings &mdash; Hector</span><a class="val" href="mailto:%s?subject=Hector%%20booking%%20enquiry">%s</a></div>
        </div>
        <div class="where">
          <h3>Where to find us</h3>
          <p style="color:var(--bone-dim)">%s. We travel nationwide for events, shoots and campaigns &mdash; and we know every venue, lot and hall on the East Rand.</p>
        </div>
      </div>
      <form id="contact-form" data-demo novalidate aria-describedby="form-note">
        <div class="field"><label for="n">Your name</label><input id="n" name="name" type="text" autocomplete="name" placeholder="Lerato Mokoena" required aria-required="true"></div>
        <div class="field"><label for="e">Email</label><input id="e" name="email" type="email" autocomplete="email" placeholder="you@company.co.za" required aria-required="true"></div>
        <div class="field"><label for="s">What do you need?</label>
          <select id="s" name="service">
            <option>Media &amp; content</option>
            <option>Event curation</option>
            <option>Talent &amp; mentorship</option>
            <option>Brand storytelling</option>
            <option>Book Hector as MC</option>
            <option>Something else</option>
          </select>
        </div>
        <div class="field"><label for="m">Tell us about it</label><textarea id="m" name="message" placeholder="Dates, location, budget range, what success looks like&hellip;"></textarea></div>
        <button class="btn solid" type="submit">Send it <span class="arw">&rarr;</span></button>
        <p class="form-note" id="form-note">Demo form &mdash; connect it to your email or Formspree to go live. See assets/js/form.js</p>
        <p class="form-ok" role="status" aria-live="polite">&#10003; Thanks &mdash; we'll come back to you within 24 hours.</p>
      </form>
    </div>
  </div>
</section>

%s
""" % (EMAIL, EMAIL, PHONE_HREF, PHONE, PLACE, EMAIL, EMAIL, PLACE, logo_row())
    return page("Contact — Jiks Academy",
                "Get in touch with Jiks Academy in Daveyton, East Rand — media, events, mentorship and brand storytelling.",
                "Contact", body, form=True)


def hector():
    client_cards = "\n      ".join(
        """<article class="client%s">
        <span class="plate"><img src="assets/img/clients/%s.png" alt="%s" loading="lazy"></span>
        <h3>%s</h3>
        <span class="k">%s</span>
      </article>""" % (" dark-plate" if dark else "", key, name, name, kind)
        for key, name, kind, dark in CLIENT_LOGOS
    )

    body = phead("assets/img/crowd.jpg", '<a href="home.html">Home</a> &nbsp;/&nbsp; Hector',
                 "MC &amp; Motivational Speaker", "Elevating events.", "Inspiring audiences.",
                 ["Corporate &middot; Institutional &middot; Cultural", "Bookings via <b>the office</b>", "Travels nationwide"])
    body += """
<section>
  <div class="wrap">
    <div class="hector-feat rv">
      <figure class="ph tint">
        <img src="assets/img/hector-portrait.jpg" alt="Hector, MC and motivational speaker" width="493" height="695">
        <div class="scrim"></div>
        <figcaption><b>Hector</b>MC &amp; Motivational Speaker</figcaption>
      </figure>
      <div>
        <p class="eyebrow">The profile</p>
        <h2>He reads<br>the <span>room</span></h2>
        <div class="prose" style="margin-top:22px">
          <p>Hector is an MC and motivational speaker who understands that a programme is only as good as the person holding it together. From corporate conferences and government gatherings to campus events and cultural stages, he carries the room with warmth, humour and command.</p>
          <p>He does not read a script at your audience. He listens to them, reads the energy in the room and moves with it &mdash; keeping dignitaries on schedule, speakers introduced properly and guests genuinely present.</p>
        </div>
      </div>
    </div>

    <div class="cols rv" style="margin-top:clamp(48px,6vw,90px)">
      <div>
        <p class="eyebrow">He ensures the following</p>
        <ul class="checks" style="margin-top:22px">
          <li><i>&rarr;</i> Your programme runs on time, every time</li>
          <li><i>&rarr;</i> Every speaker is introduced with accuracy and respect</li>
          <li><i>&rarr;</i> The tone of the room is set, held and lifted</li>
          <li><i>&rarr;</i> Your brand and institution are represented with dignity</li>
          <li><i>&rarr;</i> Transitions, announcements and moments land cleanly</li>
          <li><i>&rarr;</i> Nothing is left to chance on the day</li>
        </ul>
      </div>
      <div>
        <p class="eyebrow">Formats he hosts</p>
        <ul class="checks" style="margin-top:22px">
          <li><i>&rarr;</i> Conferences &amp; summits</li>
          <li><i>&rarr;</i> Awards &amp; gala dinners</li>
          <li><i>&rarr;</i> Government &amp; institutional programmes</li>
          <li><i>&rarr;</i> Campus &amp; youth events</li>
          <li><i>&rarr;</i> Brand activations &amp; launches</li>
          <li><i>&rarr;</i> Cultural &amp; community stages</li>
        </ul>
      </div>
    </div>
  </div>
</section>

<section style="background:rgba(8,14,36,.55);border-block:1px solid var(--line)">
  <div class="wrap">
    <div class="sec-head rv">
      <div><p class="eyebrow">Why clients choose Hector</p><h2>Five<br>reasons</h2></div>
      <div class="max"><p class="lede">The things clients say after the event, not before it.</p></div>
    </div>
    <div class="beliefs rv">
      <article class="belief"><span class="num">01</span><h3>Commanding stage presence</h3><p>A confident, grounded presence that settles a room the second he steps onto it.</p></article>
      <article class="belief"><span class="num">02</span><h3>Impeccable delivery</h3><p>Sharp communication, clean pronunciation and timing that never drags.</p></article>
      <article class="belief"><span class="num">03</span><h3>Real connection</h3><p>Natural audience connection through humour and insight &mdash; never forced, never filler.</p></article>
      <article class="belief"><span class="num">04</span><h3>Trusted representation</h3><p>Trusted brand and institutional representation, from boardrooms to stadium stages.</p></article>
      <article class="belief"><span class="num">05</span><h3>Calm under pressure</h3><p>Calm, professional leadership when the schedule slips and the tech misbehaves.</p></article>
    </div>
    <div class="pull rv" style="margin-inline:auto;text-align:center;border-left:0;padding-left:0">
      He reads the room.<br>He carries the <span>message</span>.<br>He elevates the experience.
    </div>
  </div>
</section>

<section>
  <div class="wrap">
    <div class="sec-head rv">
      <div><p class="eyebrow">Track record</p><h2>Rooms<br>he's held</h2></div>
      <div class="max"><p class="lede">Selected clients and stages Hector has hosted or represented.</p></div>
    </div>
    <div class="crew rv">
      %s
    </div>
  </div>
</section>

<section style="background:rgba(8,14,36,.55);border-block:1px solid var(--line)">
  <div class="wrap">
    <div class="cols rv">
      <div>
        <p class="eyebrow">Recent highlights</p>
        <h2 class="display" style="font-size:clamp(34px,5vw,72px);margin-top:16px">Recent<br>stages</h2>
        <p class="lede" style="margin-top:20px;max-width:40ch">A selection of recent engagements across universities, regulators, government departments and corporate clients.</p>
      </div>
      <div>
        <ul class="checks">
          <li><i>&rarr;</i> UNISA</li>
          <li><i>&rarr;</i> Tshwane University of Technology (TUT)</li>
          <li><i>&rarr;</i> South African Pharmaceutical Council</li>
          <li><i>&rarr;</i> Sefako Makgatho Health Sciences University</li>
          <li><i>&rarr;</i> AddProp</li>
          <li><i>&rarr;</i> North West Provincial Legislature</li>
          <li><i>&rarr;</i> Department of Forestry, Fisheries &amp; the Environment</li>
          <li><i>&rarr;</i> Gauteng Department of Education</li>
        </ul>
      </div>
    </div>
  </div>
</section>

<section>
  <div class="wrap">
    <div class="sec-head rv">
      <div><p class="eyebrow">The result</p><h2>What you<br>walk away with</h2></div>
    </div>
    <div class="beliefs rv">
      <article class="belief"><span class="num">01</span><h3>An event that feels intentional</h3><p>Every segment placed on purpose, with a thread your audience can follow from the first welcome to the last word.</p></article>
      <article class="belief"><span class="num">02</span><h3>A programme that feels alive</h3><p>Energy managed across the day &mdash; lifted when it dips, held when it matters, never allowed to flatline.</p></article>
      <article class="belief"><span class="num">03</span><h3>An audience that leaves engaged</h3><p>People who leave inspired, informed and aligned with the message you brought them in for.</p></article>
    </div>
  </div>
</section>

%s""" % (client_cards, cta("Book Hector.", "Tell us the date, the room and the audience. We'll come back with availability, a run-of-show and a quote.", "Check availability", "contact.html"))
    return page("Hector — MC &amp; Motivational Speaker | Jiks Academy",
                "Hector is an MC and motivational speaker. Elevating events. Inspiring audiences. Trusted by the Auditor-General of South Africa, PepsiCo, TUT, AMCU and more.",
                "Hector", body, og="assets/img/hector-portrait.jpg")


def clients():
    stages = [
        ("01", "Brief",
         "We start with the outcome, not the deliverable. What is the room supposed to feel like, and what should be different afterwards?",
         ["The real problem, not the requested format", "Audience, date, budget, non-negotiables"]),
        ("02", "Concept",
         "A route, references pulled from the culture itself, and a plan that will survive contact with the day.",
         ["Treatment, references and run-of-show", "Who we need in the room and on the crew"]),
        ("03", "Pre-production",
         "Site, suppliers, permits, call sheets, gear and people. This is where events are won or lost.",
         ["Bookings, permits and site plan", "Crew, kit and contingency"]),
        ("04", "Production",
         "We shoot it, build it or run the floor &mdash; and we cover it live while it's happening.",
         ["Cameras, stage and floor management", "Live selects for socials the same day"]),
        ("05", "Delivery &amp; aftercare",
         "Edits, masters and handover. Then a straight conversation about what worked and what runs next.",
         ["Final cuts, selects and archives", "Debrief, numbers, what we build next"]),
    ]
    stage_cards = []
    for num, title, blurb, bullets in stages:
        lis = "".join("<li>%s</li>" % b for b in bullets)
        stage_cards.append("""<article class="stage">
        <span class="n">%s</span>
        <h3>%s</h3>
        <p>%s</p>
        <ul class="tiny">%s</ul>
      </article>""" % (num, title, blurb, lis))

    hector_clients = [
        dict(ini="AGSA", name="Auditor-General of South Africa", kind="Institutional", logo="agsa"),
        dict(ini="PEP", name="PepsiCo", kind="Corporate", logo="pepsico"),
        dict(ini="NWPL", name="North West Provincial Legislature", kind="Government", logo="nwpl"),
        dict(ini="NWPE", name="North West Provincial Education", kind="Government", logo="nwedu"),
        dict(ini="TUT", name="Tshwane University of Technology", kind="Higher education", logo="tut"),
        dict(ini="AMCU", name="AMCU", kind="Organised labour", logo="amcu"),
        dict(ini="BIR", name="Birchwood &amp; OR Tambo Conference Centre", kind="Venue partner",
             logo="birchwood", dark=True),
        dict(ini="ADD", name="AddProp", kind="Corporate", logo="addprop", dark=True),
    ]
    era_clients = [
        dict(ini="DJ", name="Innocent Tlhatlhedi &mdash; DJ ToxSA", kind="Founder &amp; artist",
             logo="innocent",
             desc="Founder of both movements, represented by the academy."),
        dict(ini="RA", name="Roster artists", kind="Talent", ph=True,
             desc="Musicians, producers and performers developing through the academy."),
        dict(ini="SR", name="Studios &amp; session rooms", kind="Production", ph=True,
             desc="Rooms we record, rehearse and build in across the East Rand."),
        dict(ini="VS", name="Venues &amp; stages", kind="East Rand", ph=True,
             desc="Halls, lots and rooms that host the showcases."),
        dict(ini="MP", name="Media partners", kind="Coverage", ph=True,
             desc="Pages, blogs and channels that carry the artists' work."),
        dict(ini="MT", name="Mentors &amp; facilitators", kind="Development", ph=True,
             desc="People who give time, gear and guidance to the roster."),
        dict(ini="BR", name="Brands &amp; sponsors", kind="Partnership", ph=True,
             desc="Partners funding stages, gear and releases."),
    ]
    dss_clients = [
        dict(ini="SC", name="Stance event curators", kind="East Rand", ph=True,
             desc="Curators we've built meets and shows with across the East Rand."),
        dict(ini="SD", name="Stance drivers &amp; builders", kind="Community", ph=True,
             desc="The drivers and builders whose cars carry the culture."),
        dict(ini="FP", name="Fitment &amp; parts partners", kind="Trade", ph=True,
             desc="Workshops, fitment centres and parts suppliers."),
        dict(ini="VL", name="Venues &amp; lots", kind="Sites", ph=True,
             desc="Sites that host the meets, shows and shoot days."),
        dict(ini="MC", name="Media &amp; coverage partners", kind="Coverage", ph=True,
             desc="Pages and channels that run the coverage."),
        dict(ini="DW", name="Detailers &amp; wrap shops", kind="Trade", ph=True,
             desc="Shops finishing the builds we shoot."),
    ]

    def tiles(rows):
        out = []
        for r in rows:
            if r.get("logo"):
                art = ('<span class="plate"><img src="assets/img/clients/%s.png" alt="%s" loading="lazy"></span>'
                       % (r["logo"], r["name"]))
            else:
                art = '<span class="mono-mark">%s</span>' % r["ini"]
            cls = "client"
            if r.get("dark"):
                cls += " dark-plate"
            if r.get("ph"):
                cls += " placeholder"
            note = '<span class="ph-flag">Placeholder</span>' if r.get("ph") else ""
            body = '<p>%s</p>%s' % (r["desc"], note) if r.get("desc") else note
            out.append("""<article class="%s">
        %s
        <h3>%s</h3>
        <span class="k">%s</span>
        %s
      </article>""" % (cls, art, r["name"], r["kind"], body))
        return "\n      ".join(out)

    body = phead("assets/img/crowd.jpg", '<a href="home.html">Home</a> &nbsp;/&nbsp; Clients',
                 "Clients &amp; pipeline", "The work", "&amp; who it's for",
                 ["<b>03</b> properties", "One crew", "Based in <b>Daveyton</b>"])
    body += """
<section>
  <div class="wrap">
    <div class="sec-head rv">
      <div>
        <p class="eyebrow">The creative pipeline</p>
        <h2>How the<br>work moves</h2>
      </div>
      <div class="max">
        <p class="lede">Same five stages whether it's a stance meet, an artist showcase or a conference stage. Nothing starts at &ldquo;make us a video&rdquo; and nothing ends at &ldquo;here are the files&rdquo;.</p>
      </div>
    </div>
    <div class="pipeline rv">
      %s
    </div>
    <p class="mono" style="margin-top:22px">Every project passes through all five &mdash; we just scale the crew, not the process.</p>
  </div>
</section>

<section style="background:rgba(8,14,36,.55);border-block:1px solid var(--line)">
  <div class="wrap">
    <div class="sec-head rv">
      <div><p class="eyebrow">Client list</p><h2>Hector</h2></div>
      <div class="max"><p class="lede">MC &amp; motivational speaker. Rooms and institutions Hector has hosted or represented.</p></div>
    </div>
    <div class="clients rv">
      %s
    </div>
    <div class="stage-list rv">
      <p class="eyebrow">Also on stage for</p>
      <ul class="checks" style="margin-top:16px">
        <li><i>&rarr;</i> UNISA</li>
        <li><i>&rarr;</i> Tshwane University of Technology (TUT)</li>
        <li><i>&rarr;</i> South African Pharmaceutical Council</li>
        <li><i>&rarr;</i> Sefako Makgatho Health Sciences University</li>
        <li><i>&rarr;</i> AddProp</li>
        <li><i>&rarr;</i> North West Provincial Legislature</li>
        <li><i>&rarr;</i> Department of Forestry, Fisheries &amp; the Environment</li>
        <li><i>&rarr;</i> Gauteng Department of Education</li>
      </ul>
    </div>
  </div>
</section>

<section>
  <div class="wrap">
    <div class="sec-head rv">
      <div><p class="eyebrow">Client list</p><h2>East Rand<br>Academy</h2></div>
      <div class="max"><p class="lede">The artists, rooms and partners the academy works with. The rest are categories until you send the real list.</p></div>
    </div>
    <div class="clients rv">
      %s
    </div>
  </div>
</section>

<section style="background:rgba(8,14,36,.55);border-block:1px solid var(--line)">
  <div class="wrap">
    <div class="sec-head rv">
      <div><p class="eyebrow">Client list</p><h2>Daveyton<br>Stance Society</h2></div>
      <div class="max"><p class="lede">Curators, builders, trade partners and sites across the East Rand. Names to follow &mdash; these tiles are categories until you send the real list.</p></div>
    </div>
    <div class="clients rv">
      %s
    </div>
  </div>
</section>

<section>
  <div class="wrap">
    <div class="cols rv">
      <div>
        <p class="eyebrow">Adding real names</p>
        <h2 class="display" style="font-size:clamp(30px,4vw,54px);margin-top:16px">Send us<br>the list</h2>
        <p class="lede" style="margin-top:20px;max-width:44ch">The placeholder tiles above are categories, not invented clients. Send the names and logos for East Rand Academy and Daveyton Stance Society and they go straight in &mdash; same tiles, real marks.</p>
        <div class="hero-actions">
          <a class="btn solid" href="contact.html">Send the list <span class="arw">&rarr;</span></a>
          <a class="btn ghost-light" href="services.html">See the services <span class="arw">&rarr;</span></a>
        </div>
      </div>
      <div>
        <figure class="tint" style="border:1px solid var(--line);position:relative">
          <img src="assets/img/crowd.jpg" alt="A live crowd at night">
        </figure>
        <figcaption>On the floor &mdash; East Rand</figcaption>
      </div>
    </div>
  </div>
</section>

%s""" % ("\n      ".join(stage_cards), tiles(hector_clients), tiles(era_clients), tiles(dss_clients),
         cta("Want to be on this list?", "Projects, stages, campaigns or a build that needs covering &mdash; start the conversation.",
             "Get in touch", "contact.html"))
    return page("Clients &amp; Pipeline — Jiks Academy",
                "The Jiks Academy creative pipeline and client list — Hector, East Rand Academy and Daveyton Stance Society.",
                "Clients", body)


def sitemap():
    """Every file on the site, in reading order, plus how the navigation fits together."""
    # reading order: cover, main chain, with the crew branch slotted in after Crew
    order = [("index.html", "Cover")]
    for f, l in SITE_ORDER:
        order.append((f, l))
        if f == "crew.html":
            order.extend(CREW_BRANCH)
    rows = []
    for i, (f, l) in enumerate(order, 1):
        rows.append('<li><a href="%s"><span class="sm-n">%02d</span><span class="sm-t">%s</span>'
                    '<span class="sm-d">%s</span><code>%s</code></a></li>'
                    % (f, i, l, FILE_NOTES[f], f))
    page_list = "\n      ".join(rows)

    def files_list(items, folder):
        out = []
        for name, note in items:
            out.append('<li><a href="%s/%s"><span class="sm-t">%s</span><span class="sm-d">%s</span>'
                       '<code>%s</code></a></li>' % (folder, name, name, note, name))
        return "\n      ".join(out)

    body = phead("assets/img/crowd.jpg", '<a href="home.html">Home</a> &nbsp;/&nbsp; Site map',
                 "Every file, in order", "Site", "map",
                 ["15 HTML files", "3 stylesheets", "5 scripts"])

    body += """
<section class="band">
  <div class="wrap">
    <p class="eyebrow">Reading order</p>
    <h2 class="rv">Every page, one after the other</h2>
    <p class="lede rv">This is the order the site is meant to be read in. The three crew
      profiles are a branch that hangs off <a href="crew.html">The Crew</a>, which is why
      they sit inside the list rather than at the end of it.</p>
    <ol class="sm-list rv">
      %s
    </ol>
  </div>
</section>

<section class="band alt">
  <div class="wrap">
    <div class="cols">
      <div class="prose rv">
        <h3>How you move around</h3>
        <p><b>Header.</b> The same eight links on every page, with the page you are on
          marked for screen readers.</p>
        <p><b>Breadcrumbs.</b> Under every page head, back to Home and one level up.</p>
        <p><b>Previous / next.</b> A band at the bottom of every page that walks the
          reading order and wraps at both ends.</p>
        <p><b>Branch.</b> On <a href="crew.html">The Crew</a> that band also offers the
          three profiles; from there you step Shadrack &rarr; Kgotso &rarr; Skhumbuzo and
          back to the crew index.</p>
        <p><b>Footer.</b> Every page ends with the full list, numbered, in the same order
          as this page.</p>
      </div>
      <div class="prose rv">
        <h3>How the files are kept</h3>
        <p>Each page is a standalone <code>.html</code> file &mdash; no framework, no build
          step. The three stylesheets split by job, and each script does one thing.</p>
        <p>Nothing is bundled. Change a colour in <code>base.css</code> and the whole site
          follows; the pages only describe themselves.</p>
      </div>
    </div>
  </div>
</section>

<section class="band">
  <div class="wrap">
    <p class="eyebrow">Folders</p>
    <h2 class="rv">Where everything lives</h2>
    <pre class="tree rv"><code>jiks-academy/
<b>index.html</b>                    cover / splash
<b>home.html</b>                     the home page
about.html  ventures.html  crew.html  hector.html
services.html  clients.html  contact.html  sitemap.html
east-rand-academy.html  daveyton-stance-society.html
shadrack-makamu.html  kgotso-matlakala.html  skhumbuzo.html
site.webmanifest
assets/
  css/    <b>base.css</b>  <b>components.css</b>  <b>pages.css</b>
  js/     <b>nav.js</b>  <b>menu.js</b>  <b>cover.js</b>  <b>reveal.js</b>  <b>form.js</b>
  img/    logo, hero, photos, crew/, clients/</code></pre>
  </div>
</section>

<section class="band alt">
  <div class="wrap">
    <p class="eyebrow">Stylesheets</p>
    <h2 class="rv">Three files, one job each</h2>
    <ol class="sm-list rv">
      %s
    </ol>
  </div>
</section>

<section class="band">
  <div class="wrap">
    <p class="eyebrow">Scripts</p>
    <h2 class="rv">Five files, no bundler</h2>
    <ol class="sm-list rv">
      %s
    </ol>
  </div>
</section>

""" % (page_list, files_list(CSS_FILES, "assets/css"), files_list(JS_FILES, "assets/js"))

    body += cta("Jump back in", "The site map is here for orientation &mdash; the work is on the other pages.",
                "Back to the home page", "home.html")
    return page("Site map &mdash; Jiks Academy",
                "Every page, stylesheet and script on the Jiks Academy site, in reading order.",
                "Site map", body)


# ----------------------------------------------------------------- write
SITE_ORDER = [
    ("home.html", "Home"),
    ("about.html", "About"),
    ("ventures.html", "Ventures"),
    ("east-rand-academy.html", "East Rand Academy"),
    ("daveyton-stance-society.html", "Daveyton Stance Society"),
    ("crew.html", "The Crew"),
    ("hector.html", "Hector"),
    ("services.html", "Services"),
    ("clients.html", "Clients &amp; Pipeline"),
    ("contact.html", "Contact"),
    ("sitemap.html", "Site map"),
]

# The crew profiles form a branch off crew.html rather than sitting in the main chain:
# crew -> Shadrack -> Kgotso -> Skhumbuzo -> back to crew.
CREW_BRANCH = [
    ("shadrack-makamu.html", "Shadrack Makamu"),
    ("kgotso-matlakala.html", "Kgotso Matlakala"),
    ("skhumbuzo.html", "Skhumbuzo"),
]

# One line per page, used by the site map and the footer index.
FILE_NOTES = {
    "index.html": "Cover &mdash; the logo splash that opens the site, then through to Home.",
    "home.html": "Home &mdash; hero, beliefs, the two ventures, crew, Hector, services and a closing call to action.",
    "about.html": "About &mdash; who we are, four commitments, the stats and the founding timeline.",
    "ventures.html": "Ventures &mdash; the index of the two movements we run.",
    "east-rand-academy.html": "Movement 01 &mdash; East Rand Academy. Full bio, promises and timeline.",
    "daveyton-stance-society.html": "Movement 02 &mdash; Daveyton Stance Society. Full bio, engines and timeline.",
    "crew.html": "The Crew &mdash; all three people, each linking to their own profile.",
    "shadrack-makamu.html": "Profile &mdash; Shadrack Makamu, Head of Media &amp; Visuals.",
    "kgotso-matlakala.html": "Profile &mdash; Kgotso Matlakala, Events &amp; Operations Lead.",
    "skhumbuzo.html": "Profile &mdash; Skhumbuzo, Talent Liaison &amp; Community.",
    "hector.html": "Hector &mdash; MC and motivational speaker. Full profile, stages and booking.",
    "services.html": "Services &mdash; the four disciplines we sell, in detail.",
    "clients.html": "Clients &amp; Pipeline &mdash; the five-stage creative pipeline plus the client list.",
    "contact.html": "Contact &mdash; details, where to find us and the enquiry form.",
    "sitemap.html": "Site map &mdash; this page. Every file on the site, in reading order.",
}

CSS_FILES = [
    ("base.css", "Colour tokens, reset, typography and layout primitives. The theme lives here."),
    ("components.css", "Nav, buttons, cards, marquee, stats, forms and footer."),
    ("pages.css", "Page-specific blocks: cover, hero, page heads, profiles, pager, site map and services."),
]

JS_FILES = [
    ("nav.js", "Sticky navigation state on scroll."),
    ("menu.js", "Mobile menu: burger state, focus handling and Escape to close."),
    ("cover.js", "Cover page auto-advance and progress bar."),
    ("reveal.js", "Scroll reveals and the footer year."),
    ("form.js", "Contact form success message."),
]


def footer_all_pages():
    """Compact ordered index of every file, in the footer of every page."""
    main = [("index.html", "Cover")] + SITE_ORDER
    row = lambda items: "\n      ".join('<li><a href="%s">%s</a></li>' % (f, l) for f, l in items)
    return """    <nav class="f-all" aria-label="All pages">
      <h2>All pages, in order</h2>
      <ol class="f-all-row">
      %s
      </ol>
      <ol class="f-all-row">
      %s
      </ol>
    </nav>
""" % (row(main), row(CREW_BRANCH))


def page_pager(name):
    """Previous / next navigation.

    Main pages follow SITE_ORDER and wrap at both ends. Crew profiles are
    skipped here: they already carry an in-page pager that forms the branch
    crew -> Shadrack -> Kgotso -> Skhumbuzo -> back to crew.
    """
    if name in [f for f, _ in CREW_BRANCH]:
        return ""  # crew profiles carry their own pager in the page body
    chain = SITE_ORDER
    files = [f for f, _ in chain]
    if name not in files:
        return ""
    i = files.index(name)
    prev_f, prev_l = chain[(i - 1) % len(chain)]
    next_f, next_l = chain[(i + 1) % len(chain)]
    branch = ""
    if name == "crew.html":
        links = "\n      ".join('<a href="%s">%s</a>' % (f, l) for f, l in CREW_BRANCH)
        branch = """<div class="pager-branch rv">
      <span class="k">Branch &mdash; crew profiles</span>
      <span class="bl">
      %s
      </span>
    </div>""" % links
    return """<section class="pager-band" aria-label="Page navigation">
  <div class="wrap">
    <div class="pager rv">
      <a href="%s"><span class="k">&larr; Previous page</span><span class="n">%s</span></a>
      <a class="next" href="%s"><span class="k">Next page &rarr;</span><span class="n">%s</span></a>
    </div>
%s
  </div>
</section>""" % (prev_f, prev_l, next_f, next_l, branch)


PAGES = {
    "index.html": cover_page(),
    "home.html": home(),
    "about.html": about(),
    "ventures.html": ventures(),
    "east-rand-academy.html": east_rand_academy(),
    "daveyton-stance-society.html": daveyton_stance(),
    "crew.html": crew_index(),
    "hector.html": hector(),
    "services.html": services(),
    "clients.html": clients(),
    "contact.html": contact(),
    "sitemap.html": sitemap(),
}
for i, m in enumerate(CREW):
    PAGES["%s.html" % m["slug"]] = crew_page(m, i)

for name, html in PAGES.items():
    pager = page_pager(name)
    if pager:
        html = html.replace("\n</main>", "\n" + pager + "\n</main>")
    with open(os.path.join(OUT, name), "w", encoding="utf-8") as f:
        f.write(html)
    print("  wrote %-32s %5d bytes" % (name, len(html)))

# Optional: one joined stylesheet instead of three. Off by default, so the site
# ships the separate files; switch SINGLE_CSS to True above to emit (and link) main.css.
if SINGLE_CSS:
    css_dir = os.path.join(OUT, "assets", "css")
    parts = []
    for part in ("base.css", "components.css", "pages.css"):
        parts.append("/* ==== %s ==== */\n" % part
                     + open(os.path.join(css_dir, part), encoding="utf-8").read().rstrip())
    joined = ("/* main.css — generated by build_site.py: base + components + pages joined.\n"
              "   Do not edit by hand; change the source files and re-run the build. */\n\n"
              + "\n\n".join(parts) + "\n")
    open(os.path.join(css_dir, "main.css"), "w", encoding="utf-8").write(joined)
    print("  wrote %-32s %5d bytes" % ("assets/css/main.css", len(joined)))
else:
    stale = os.path.join(OUT, "assets", "css", "main.css")
    if os.path.exists(stale):
        os.remove(stale)
        print("  removed %-30s (three separate stylesheets ship instead)" % "assets/css/main.css")

print("\n%d pages written to %s" % (len(PAGES), OUT))
