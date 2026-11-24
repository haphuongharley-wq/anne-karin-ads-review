"""Build index.html from the ads markdown in the Anne Karin repo."""
import re, markdown, pathlib
SRC = pathlib.Path.home() / "anne-karin-kunsten-a-overbevise/ads/ads-leder-rewrite-nov-2026.md"
md = SRC.read_text()
imgs = {"S1": "s1-tid.png", "S2": "s2-strategi.png", "S3": "s3-grunder.png"}
for k, f in imgs.items():
    md = re.sub(rf"(### 🖼️ {k} · ANNONSE[^\n]*\n)",
                rf'\1\n<a href="images/{f}" target="_blank"><img class="ad" src="images/{f}" alt="Annonsebilde {k}"></a>\n\n', md)
body = markdown.markdown(md, extensions=["tables"])
perf = (SRC.parent / "ads-performance-2026.md").read_text()
perf_html = markdown.markdown(perf, extensions=["tables"]).replace("<h2>Ads performance", '<h2 id="performance">Ads performance', 1)
body = f'<div class="perf">{perf_html}</div>' + body
nav = "".join(f'<a href="#{i}">{t}</a>' for i, t in [("performance","Performance"),("s1","S1 Teams og tid"),("s2","S2 Strategi"),("s3","S3 Gründer"),("maalretting","Målretting")])
body = body.replace("<h2>S1 –", '<h2 id="s1">S1 –').replace("<h2>S2 –", '<h2 id="s2">S2 –').replace("<h2>S3 –", '<h2 id="s3">S3 –').replace("<h2>Målretting", '<h2 id="maalretting">Målretting')
page = f"""<!DOCTYPE html><html lang="no"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>Annonser – lederversjon</title>
<style>
:root{{--bg:#F8F6F1;--ink:#0F1A2B;--muted:#4A5568;--teal:#3F8F93;--red:#9B1B2A;--card:#FFFFFF;color-scheme:light}}
*{{box-sizing:border-box}}
body{{margin:0;overflow-wrap:anywhere;background:var(--bg);color:var(--ink);font:17px/1.6 -apple-system,'Helvetica Neue',Arial,sans-serif}}
header{{background:var(--ink);color:#fff;padding:40px 16px 28px}}
.wrap{{max-width:760px;margin:0 auto}}
header h1{{font-family:Georgia,serif;font-size:34px;margin:0 0 8px}}
header p{{margin:0;color:#C9D3E0}}
nav{{display:flex;flex-wrap:wrap;gap:8px;margin-top:18px}}
nav a{{color:#fff;text-decoration:none;border:1px solid rgba(255,255,255,.35);border-radius:999px;padding:6px 14px;font-size:14px}}
main{{padding:24px 16px 64px}}
h1,h2,h3{{font-family:Georgia,serif;line-height:1.25}}
main h1{{display:none}}
h2{{font-size:28px;margin-top:56px;padding-top:12px;border-top:3px solid var(--teal)}}
h3{{font-size:20px;margin-top:32px}}
blockquote{{margin:0;padding:12px 18px;background:var(--card);border-left:4px solid var(--teal);border-radius:6px}}
img.ad{{width:100%;max-width:560px;display:block;border-radius:10px;box-shadow:0 6px 24px rgba(15,26,43,.15);margin:8px 0 16px}}
table{{border-collapse:collapse;width:100%;font-size:15px;display:block;overflow-x:auto}}
td,th{{border:1px solid #D9D4C8;padding:8px 10px;text-align:left;vertical-align:top}}

.perf table{{white-space:nowrap;font-size:14px;width:max-content;max-width:100%;margin:12px 0 20px}}
.perf table:first-of-type{{max-width:calc(100vw - 32px);position:relative;left:50%;transform:translateX(-50%)}}
.perf td:first-child{{font-weight:600}}
code{{background:#ECE7DC;padding:1px 5px;border-radius:4px;font-size:14px;word-break:break-all}}
hr{{display:none}}
</style></head><body>
<header><div class="wrap"><h1>Annonser – lederversjon</h1>
<p>Anne Karin Nordskag · Gjennomslagskraft. Tekster, annonsebilder og målretting for neste runde, til godkjenning.</p>
<nav>{nav}</nav></div></header>
<main><div class="wrap">{body}</div></main></body></html>"""
pathlib.Path(__file__).with_name("index.html").write_text(page)
print("ok")
