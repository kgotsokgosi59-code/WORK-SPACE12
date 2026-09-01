#!/usr/bin/env python3
"""Accessibility audit: runs axe-core over every page of the Jiks Academy site.

  python3 audit_a11y.py            # audit http://localhost:8000
  python3 audit_a11y.py --json     # dump raw violations
"""
import sys, json
from playwright.sync_api import sync_playwright

BASE = "http://localhost:8000"
PAGES = ["index.html", "home.html", "about.html", "ventures.html", "east-rand-academy.html",
         "daveyton-stance-society.html", "crew.html", "hector.html", "services.html",
         "clients.html", "contact.html", "sitemap.html", "shadrack-makamu.html",
         "kgotso-matlakala.html", "skhumbuzo.html"]

AXE = "https://cdnjs.cloudflare.com/ajax/libs/axe-core/4.10.2/axe.min.js"

with sync_playwright() as pw:
    browser = pw.chromium.launch()
    page = browser.new_page(viewport={"width": 1440, "height": 900})
    total = 0
    all_violations = {}
    for name in PAGES:
        page.goto(f"{BASE}/{name}", wait_until="load")
        page.wait_for_timeout(350)
        try:
            page.add_script_tag(url=AXE)
        except Exception:
            print("  (axe CDN unavailable — offline)"); break
        res = page.evaluate("""async () => await axe.run(document, {
            runOnly: { type: 'tag', values: ['wcag2a','wcag2aa','wcag21a','wcag21aa','best-practice'] }
        })""")
        v = res.get("violations", [])
        total += len(v)
        all_violations[name] = v
        status = "OK  " if not v else "%d issues" % len(v)
        print("%-32s %s" % (name, status))
        for issue in v:
            print("     [%s] %s — %d element(s)"
                  % (issue["impact"], issue["help"], len(issue["nodes"])))
            for node in issue["nodes"][:3]:
                print("        %s" % node["html"][:110].replace("\n", " "))
    browser.close()

print("\nTOTAL VIOLATIONS:", total)
if "--json" in sys.argv:
    json.dump(all_violations, open("a11y-report.json", "w"), indent=2)
    print("raw report -> a11y-report.json")
