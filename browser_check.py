#!/usr/bin/env python3
"""Cross-browser smoke test: Chromium, Firefox and WebKit.

Checks every page in each engine for console errors, broken images, collapsed
layout and missing key elements. Run the local server first.
"""
from playwright.sync_api import sync_playwright

BASE = "http://localhost:8000"
PAGES = ["index.html", "home.html", "about.html", "ventures.html", "east-rand-academy.html",
         "daveyton-stance-society.html", "crew.html", "hector.html", "services.html",
         "clients.html", "contact.html", "sitemap.html", "shadrack-makamu.html",
         "kgotso-matlakala.html", "skhumbuzo.html"]

PROBE = """() => {
  const q = s => document.querySelector(s);
  const vis = el => { if (!el) return false; const r = el.getBoundingClientRect();
                      const cs = getComputedStyle(el);
                      return r.width > 0 && r.height > 0 && cs.visibility !== 'hidden' && cs.display !== 'none'; };
  const imgs = [...document.images];
  return {
    title: document.title.slice(0, 40),
    nav:      vis(q('.nav')),
    brand:    vis(q('.brand img')),
    main:     vis(q('main')),
    h1:       (q('h1') || {}).textContent?.trim().slice(0, 34) || null,
    footer:   vis(q('footer')),
    email:    document.body.innerHTML.includes('kgotsokgosi59@gmail.com'),
    bodyBg:   getComputedStyle(document.body).backgroundColor,
    docH:     document.documentElement.scrollHeight,
    imgTotal: imgs.length,
    imgBroken: imgs.filter(i => i.complete && i.naturalWidth === 0).length,
    imgNoAlt: imgs.filter(i => i.getAttribute('alt') === null).length,
  };
}"""

with sync_playwright() as pw:
    for engine in ("chromium", "firefox", "webkit"):
        browser = getattr(pw, engine).launch()
        print("\n" + "=" * 74 + "\n%s\n" % engine.upper() + "=" * 74)
        problems = []
        for name in PAGES:
            page = browser.new_page(viewport={"width": 1366, "height": 900})
            errors = []
            page.on("console", lambda m: errors.append(m.text) if m.type == "error" else None)
            page.on("pageerror", lambda e: errors.append(str(e)))
            page.goto(f"{BASE}/{name}", wait_until="load")
            page.wait_for_timeout(500)
            r = page.evaluate(PROBE)
            h = r.pop("title")
            flags = []
            # index.html is the cover splash: no chrome, one screen tall, by design.
            splash = name == "index.html"
            if not r["nav"] and not splash:      flags.append("no nav")
            if not r["brand"] and not splash: flags.append("no logo")
            if not r["main"]:     flags.append("no main")
            if not r["footer"] and not splash: flags.append("no footer")
            if not r["h1"]:       flags.append("no h1")
            if not r["email"] and not splash: flags.append("email missing")
            if r["imgBroken"]:    flags.append("%d broken img" % r["imgBroken"])
            if r["imgNoAlt"]:     flags.append("%d img w/o alt" % r["imgNoAlt"])
            if r["docH"] < 1200 and not splash: flags.append("page looks collapsed (%dpx)" % r["docH"])
            if errors:            flags.append("console: " + errors[0][:60])
            print("  %-30s h=%-6d imgs=%-3d %s"
                  % (name, r["docH"], r["imgTotal"], "OK" if not flags else " | ".join(flags)))
            if flags:
                problems.append((name, flags))
            page.close()
        browser.close()
        print("  --> %s" % ("all pages OK" if not problems else "%d page(s) with issues" % len(problems)))
