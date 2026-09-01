"""Measures how well the cover fills each screen, and whether anything overflows."""
from playwright.sync_api import sync_playwright
VP = [("phone 320x568",320,568),("phone 360x640",360,640),("phone 390x844",390,844),
      ("phone 414x896",414,896),("phone 430x932",430,932),("ph land 667x375",667,375),
      ("ph land 740x360",740,360),("ph land 844x390",844,390),("ph land 932x430",932,430),
      ("iPad 768x1024",768,1024),("iPad Air 820x1180",820,1180),("iPad Pro 1024x1366",1024,1366),
      ("iPad land 1024x768",1024,768),("iPad land 1180x820",1180,820),("iPad Pro land 1366x1024",1366,1024),
      ("laptop 1280x800",1280,800),("laptop 1366x768",1366,768),("laptop 1440x900",1440,900),
      ("laptop 1536x864",1536,864),("desktop 1920x1080",1920,1080),("desktop 2560x1440",2560,1440)]
JS = """() => {
  const g=s=>{const e=document.querySelector(s);return e?e.getBoundingClientRect():null};
  const items=['.cover-plate','h1','.cover-tag','.cover-enter','.cover-bar','.cover-note','.cover-meta']
      .map(s=>g(s)).filter(Boolean);
  const top=Math.min(...items.map(b=>b.top)), bot=Math.max(...items.map(b=>b.bottom));
  const h1=document.querySelector('h1');
  return {h1: parseFloat(getComputedStyle(h1).fontSize),
          lines: Math.round(g('h1').height / (parseFloat(getComputedStyle(h1).fontSize)*0.86)),
          plate: Math.round(g('.cover-plate').width),
          fill: Math.round((bot-top)/innerHeight*100),
          vover: document.documentElement.scrollHeight - innerHeight,
          hoverflow: document.documentElement.scrollWidth - innerWidth,
          clip: Math.round(Math.max(0,-top) + Math.max(0, bot-innerHeight))};
}"""
with sync_playwright() as pw:
    br = pw.chromium.launch(); pg = br.new_page()
    print(f"{'viewport':22} {'h1px':>5} {'ln':>3} {'plate':>5} {'fill%':>6} {'vOver':>6} {'hOver':>6} {'clip':>5}")
    bad = 0
    for name, w, h in VP:
        pg.set_viewport_size({"width": w, "height": h})
        pg.goto("http://localhost:8000/index.html", wait_until="load")
        pg.wait_for_timeout(650)
        r = pg.evaluate(JS)
        prob = r['vover'] > 2 or r['hoverflow'] > 0 or r['clip'] > 1
        bad += prob
        print(f"{name:22} {r['h1']:5.0f} {r['lines']:3d} {r['plate']:5d} {r['fill']:6d} "
              f"{r['vover']:6d} {r['hoverflow']:6d} {r['clip']:5d}"
              + ("   <-- OVERFLOW" if prob else ("   <-- underfilled" if r['fill'] < 68 else "")))
    print("\nproblem viewports:", bad)
    br.close()
