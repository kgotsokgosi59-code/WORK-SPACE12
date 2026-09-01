"""Binary-searches each cover multiplier to the largest value that fills the
screen without overflowing, per viewport group, in all three engines."""
from playwright.sync_api import sync_playwright

GROUPS = {
    # var:        viewports (w, h)
    "--cov-p": [("phone 360x640",360,640),("phone 390x844",390,844),("phone 414x896",414,896),
                ("iPad 768x1024",768,1024),("iPad Air 820x1180",820,1180),("iPad Pro 1024x1366",1024,1366)],
    "--cov":   [("iPad land 1024x768",1024,768),("iPad land 1180x820",1180,820),
                ("iPad Pro land 1366x1024",1366,1024),("laptop 1280x800",1280,800),
                ("laptop 1366x768",1366,768),("laptop 1440x900",1440,900),("desktop 1920x1080",1920,1080)],
    "--cov-g": [("ph land 740x360",740,360),("ph land 844x390",844,390)],
}
JS = """() => {const g=s=>document.querySelector(s).getBoundingClientRect();
 const it=['.cover-plate','h1','.cover-tag','.cover-enter','.cover-bar','.cover-note','.cover-meta']
   .map(s=>{const e=document.querySelector(s);return e && getComputedStyle(e).display!=='none' ? g(s):null}).filter(Boolean);
 const top=Math.min(...it.map(b=>b.top)), bot=Math.max(...it.map(b=>b.bottom));
 return {fill:(bot-top)/innerHeight, over:document.documentElement.scrollHeight-innerHeight,
         hover:document.documentElement.scrollWidth-innerWidth,
         clip:Math.max(0,-top)+Math.max(0,bot-innerHeight)};}"""

def fits(pg, var, w, h, k):
    pg.set_viewport_size({"width": w, "height": h})
    pg.goto("http://localhost:8000/index.html", wait_until="load")
    pg.add_style_tag(content=".cover{%s:%s}" % (var, k))
    pg.wait_for_timeout(420)
    r = pg.evaluate(JS)
    return r["over"] <= 2 and r["hover"] <= 0 and r["clip"] <= 1, r

with sync_playwright() as pw:
    for var, vps in GROUPS.items():
        best = {}
        for eng in ("chromium", "firefox", "webkit"):
            b = getattr(pw, eng).launch(); pg = b.new_page()
            for name, w, h in vps:
                lo, hi = 0.5, 2.6
                for _ in range(7):                      # binary search
                    mid = round((lo + hi) / 2, 3)
                    ok, _ = fits(pg, var, w, h, mid)
                    if ok: lo = mid
                    else:  hi = mid
                best[name] = min(best.get(name, 9), lo)
            b.close()
        limit = min(best.values())
        print(f"{var}  max per viewport: " + ", ".join(f"{k}={v}" for k, v in best.items()))
        print(f"   -> safest {var} limit = {limit:.3f}   (recommend baking {max(1.0, limit-0.03):.2f})\n")
