#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Build the mobile edition of the HONGSHI site.

Reads the already-generated desktop pages (EN at repo root, ZH under zh/),
linearises their content into a single-column, large-touch-target layout and
writes them to /m/ and /zh/m/.

Run after build.py and zh_pages.py:
    python3 build.py && python3 zh_pages.py && python3 m_build.py
"""
import os
import posixpath
import re
import sys

try:
    from lxml import html as LH
except ImportError:  # pragma: no cover
    sys.exit("lxml is required: pip3 install lxml --break-system-packages")

ROOT = os.path.dirname(os.path.abspath(__file__))
OUT_EN = os.path.join(ROOT, "m")
OUT_ZH = os.path.join(ROOT, "zh", "m")
DOMAIN = "https://jeeftang.github.io/hongshi"

SKIP = {"404.html", "index.bak.html"}
SKIP_TAGS = {"script", "style", "noscript", "header", "footer", "nav", "iframe"}
SKIP_CLASS_HINTS = ("chat", "hs-")

# current page language, set by build_page(); used by the spec-table renderer
CUR_LANG = "en"

LOGO = (
    '<svg viewBox="0 0 34 34" fill="none" aria-hidden="true">'
    '<rect width="34" height="34" rx="9" fill="#e2570f"/>'
    '<path d="M17 6.5c3.6 2.4 6 6.2 6 10.2 0 3.3-2.7 6-6 6s-6-2.7-6-6c0-4 2.4-7.8 6-10.2Z" fill="#fff"/>'
    '<path d="M17 22.7v4.8M11 14.5h12" stroke="#0c1a26" stroke-width="1.6" stroke-linecap="round" opacity=".85"/>'
    "</svg>"
)

# page slug -> (nav label EN, nav label ZH)
NAV_PRODUCTS = [
    ("plunger-pumps.html", "Multi-plunger pumps", "多柱塞泵"),
    ("slurry-pumps.html", "Slurry pumps", "浆料泵"),
    ("maglev-blowers.html", "Maglev blowers", "磁悬浮鼓风机"),
    ("mobile-pumps.html", "Mobile pump units", "移动泵站"),
    ("edge-ai.html", "Industrial AI box", "工业智能体"),
]


def classes(el):
    return (el.get("class") or "").split()


def txt(el):
    return re.sub(r"\s+", " ", (el.text_content() or "")).strip()


def is_dropped(el):
    if el.tag in SKIP_TAGS:
        return True
    cls = " ".join(classes(el))
    return any(h in cls for h in SKIP_CLASS_HINTS)


def esc(s):
    return (s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;"))


def render_table(el):
    el = LH.fromstring(LH.tostring(el))
    el.set("class", "")
    inner = re.sub(r'\s(class|style|width|height|align)="[^"]*"', "", LH.tostring(el, encoding="unicode"))
    inner = inner.replace("<table>", "<table>").replace("<tbody>", "").replace("</tbody>", "")
    return (
        '<div class="m-table-hint">← 左右滑动查看完整表格 / swipe to see all columns</div>'
        f'<div class="m-table">{inner}</div>'
    )


SPEC_LABELS = {
    "en": {
        "model": "Model",
        "flow": "Flow",
        "head": "Head",
        "pressure": "Pressure",
        "groups": [
            ("UDQ 12–200", "UDQ series · 12–200 m³/h · high head"),
            ("UDZ 280–600", "UDZ series · 280–600 m³/h · high flow"),
            ("UDQ 600H", "UDQ 600 · high flow at high head"),
        ],
    },
    "zh": {
        "model": "型号",
        "flow": "流量",
        "head": "扬程",
        "pressure": "压力",
        "groups": [
            ("UDQ 12–200", "UDQ 系列 · 12–200 m³/h · 高扬程"),
            ("UDZ 280–600", "UDZ 系列 · 280–600 m³/h · 大流量"),
            ("UDQ 600H", "UDQ 600 · 大流量 + 高扬程"),
        ],
    },
}


def render_specgrid(el):
    """Turn div.spec-grid (13 product cards) into grouped cards: photo + parameters."""
    lab = SPEC_LABELS["zh" if CUR_LANG == "zh" else "en"]
    rows = []
    for art in el.findall(".//article"):
        h = art.find(".//h3")
        if h is None:
            continue
        model = txt(h)
        im = art.find(".//img")
        img = im.get("src") if im is not None else ""
        vals = {}
        dl = art.find(".//dl")
        if dl is not None:
            # dt labels differ per language (Flow / 流量), so read the dd values
            # in document order: flow, head, pressure.
            dds = [txt(ch) for ch in dl if ch.tag == "dd" and txt(ch)]
            for key, value in zip(("flow", "head", "pressure"), dds):
                vals[key] = value
        duty = ""
        for p in art.findall(".//p"):
            if p.get("class") and "small" in p.get("class"):
                duty = txt(p)
                break
        rows.append((model, vals.get("flow", ""), vals.get("head", ""),
                     vals.get("pressure", ""), duty, img))

    if not rows:
        return ""

    def group_of(model):
        m = model.upper()
        if m.startswith("UDZ"):
            return 1
        if m.replace(" ", "") == "UDQ600":
            return 2
        return 0

    out = ['<div class="m-spec">']
    for gi, (_, glabel) in enumerate(lab["groups"]):
        sel = [r for r in rows if group_of(r[0]) == gi]
        if not sel:
            continue
        out.append(f'<p class="m-spec-grp">{esc(glabel)}</p>')
        for model, flow, head, press, duty, img in sel:
            out.append(
                '<article class="m-pc">'
                + (f'<img src="{img}" alt="{esc(model)}" loading="lazy">' if img else "")
                + '<div class="bd">'
                f'<h3>{esc(model)}</h3>'
                + (f'<p class="use">{esc(duty)}</p>' if duty else "")
                + '<ul class="kv">'
                f'<li><span>{lab["flow"]}</span><b>{esc(flow)}</b></li>'
                f'<li><span>{lab["head"]}</span><b>{esc(head)}</b></li>'
                f'<li><span>{lab["pressure"]}</span><b>{esc(press)}</b></li>'
                "</ul></div></article>"
            )
    out.append("</div>")
    return "".join(out)


def render_figure(el):
    out = []
    for img in el.iter("img"):
        src = img.get("src") or ""
        alt = img.get("alt") or ""
        if src:
            out.append(f'<img src="{src}" alt="{esc(alt)}" loading="lazy">')
    cap = el.find("figcaption")
    caption = txt(cap) if cap is not None else ""
    body = "".join(out)
    if not body:
        return ""
    return f'<figure class="m-fig">{body}{f"<figcaption>{esc(caption)}</figcaption>" if caption else ""}</figure>'


def render_card(el, heading_tag="h3"):
    parts = []
    tag = el.find('.//p[@class="tag"]')
    if tag is not None:
        parts.append(f'<p class="tag">{esc(txt(tag))}</p>')
    h = el.find(".//h3") if el.find(".//h3") is not None else el.find(".//h4")
    if h is not None:
        parts.append(f"<{heading_tag}>{esc(txt(h))}</{heading_tag}>")
    for child in el:
        if child is h or child is tag:
            continue
        if child.tag == "p":
            t = txt(child)
            if t:
                parts.append(f"<p>{esc(t)}</p>")
        elif child.tag in ("ul", "ol"):
            items = "".join(f"<li>{esc(txt(li))}</li>" for li in child.findall("li") if txt(li))
            if items:
                parts.append(f"<ul>{items}</ul>")
        elif child.tag == "a":
            href = child.get("href") or ""
            if href:
                parts.append(f'<a class="m-btn ghost" href="{href}">{esc(txt(child))}</a>')
        elif child.tag == "img":
            parts.append(f'<img src="{child.get("src")}" alt="{esc(child.get("alt") or "")}" loading="lazy">')
        elif child.tag == "div":
            parts.append(render_block(child))
    cls = "m-card checks" if el.find(".//ul") is not None and el.find(".//ul").get("class") == "checks" else "m-card"
    return f'<div class="{cls}">{"".join(parts)}</div>'


def render_block(el, seen=None):
    if seen is None:
        seen = set()
    if is_dropped(el):
        return ""
    cls = classes(el)
    tag = el.tag

    if tag in ("h1", "h2", "h3", "h4", "h5"):
        t = txt(el)
        if not t:
            return ""
        level = {"h1": "h1", "h2": "h2", "h3": "h3", "h4": "h3", "h5": "h3"}[tag]
        return f"<{level}>{esc(t)}</{level}>"

    if tag == "p":
        t = txt(el)
        if not t or t in seen:
            return ""
        seen.add(t)
        if "eyebrow" in cls:
            return f'<p class="eyebrow">{esc(t)}</p>'
        if "lead" in cls:
            return f'<p class="lead">{esc(t)}</p>'
        return f"<p>{esc(t)}</p>"

    if tag in ("ul", "ol"):
        items = []
        for li in el.findall("li"):
            t = txt(li)
            if t and t not in seen:
                seen.add(t)
                items.append(f"<li>{esc(t)}</li>")
        return f"<ul>{''.join(items)}</ul>" if items else ""

    if tag == "figure":
        return render_figure(el)

    if tag == "img":
        src = el.get("src") or ""
        return f'<img src="{src}" alt="{esc(el.get("alt") or "")}" loading="lazy">' if src else ""

    if tag == "table":
        return render_table(el)

    if tag == "article":
        # product cards use <article class="card">; the spec-grid has its own renderer
        if "spec" in cls:
            return ""
        if "card" in cls:
            return render_card(el)
        return "".join(render_block(c, seen) for c in el)

    if tag == "blockquote":
        t = txt(el)
        return f'<div class="callout"><p>{esc(t)}</p></div>' if t else ""

    if tag == "a":
        href = el.get("href") or ""
        t = txt(el)
        if not href or not t:
            return ""
        if "btn" in cls or "cta" in cls:
            return f'<a class="m-btn" href="{href}">{esc(t)}</a>'
        return f'<p><a href="{href}">{esc(t)}</a></p>'

    if tag in ("form", "input", "select", "textarea", "button", "label"):
        # keep interactive widgets intact, styles come from m.css
        inner = LH.tostring(el, encoding="unicode")
        inner = re.sub(r'\s(class|style)="[^"]*"', "", inner)
        return f'<div class="m-form">{inner}</div>'

    if tag == "div":
        # any container holding form controls must survive verbatim
        if (
            el.find(".//input") is not None
            or el.find(".//select") is not None
            or el.find(".//textarea") is not None
            or el.find(".//button") is not None
        ):
            inner = LH.tostring(el, encoding="unicode")
            inner = re.sub(r'\s(class|style)="[^"]*"', "", inner)
            return f'<div class="m-form">{inner}</div>'
        if "card" in cls:
            return render_card(el)
        if "spec-grid" in cls or "spec-grid" in (el.get("class") or ""):
            return render_specgrid(el)
        if "callout" in cls:
            out = "".join(render_block(c, seen) for c in el)
            return f'<div class="callout">{out}</div>'
        if any(c.startswith("grid") for c in cls) or "prose" in cls or "sec-head" in cls or "wrap" in cls:
            return "".join(render_block(c, seen) for c in el)
        # unknown wrapper: recurse if it has block children, else emit text
        if any(c.tag in ("p", "div", "ul", "ol", "h2", "h3", "figure", "table", "img", "a") for c in el):
            return "".join(render_block(c, seen) for c in el)
        t = txt(el)
        return f"<p>{esc(t)}</p>" if t and t not in seen else ""

    return ""


def section_heading(sec):
    for h in sec.iter("h2", "h1"):
        t = txt(h)
        if t:
            return t
    return ""


def build_page(path, depth, lang):
    """depth: path of source dir relative to site root ('' or 'zh')."""
    global CUR_LANG
    CUR_LANG = lang
    doc = LH.parse(path).getroot()
    body = doc.find("body")
    title_el = doc.find(".//title")
    title = txt(title_el) if title_el is not None else "DALIAN HONGSHI TECHNOLOGY"
    desc_el = doc.find('.//meta[@name="description"]')
    desc = desc_el.get("content", "") if desc_el is not None else ""

    sections = body.findall(".//section")
    chunks = []
    fold_after = 4
    for i, sec in enumerate(sections):
        sec_cls = classes(sec)
        wrap = sec.find('.//div[@class="wrap"]')
        holder = wrap if wrap is not None else sec
        inner = "".join(render_block(child, set()) for child in holder)
        if not inner.strip():
            continue

        if "page-head" in sec_cls or "hero" in sec_cls:
            chunks.append(f'<div class="mhero">{inner}</div>')
            continue

        tint = " tint" if "alt" in sec_cls else ""
        head = section_heading(sec)
        if i >= fold_after and head:
            # the heading already shows in <summary>; drop it from the body
            inner_folded = re.sub(
                r"<h2>" + re.escape(esc(head)) + r"</h2>", "", inner, count=1
            )
            chunks.append(
                f'<section class="m-sec{tint}"><details class="m-fold"><summary>{esc(head)}</summary>'
                f'<div class="fold-body">{inner_folded}</div></details></section>'
            )
        else:
            chunks.append(f'<section class="m-sec{tint}">{inner}</section>')

    content = "".join(chunks)
    return title, desc, content


def rewrite_paths(html_s, src_dir, out_dir):
    def sub(m):
        attr, val = m.group(1), m.group(2)
        if not val:
            return m.group(0)
        low = val.lower()
        if low.startswith(("http://", "https://", "//", "mailto:", "tel:", "data:", "javascript:", "#", "/")):
            return m.group(0)
        path, sep, frag = val.partition("#")
        if not path:
            return m.group(0)
        target = posixpath.normpath(posixpath.join(src_dir, path))
        new = posixpath.relpath(target, out_dir)
        return f'{attr}="{new}{"#" + frag if sep else ""}"'

    return re.sub(r'(href|src)="([^"]*)"', sub, html_s)


def page_shell(lang, slug, title, desc, content, src_dir, out_dir, canonical):
    ui = {
        "en": {
            "home": "Home",
            "products": "Products",
            "quote": "Get a quote",
            "desktop": "电脑版",
            "lang": "中文",
            "lang_href": posixpath.relpath(
                posixpath.join("zh", "m", slug), out_dir
            ),
            "desktop_href": posixpath.relpath(posixpath.join(src_dir, slug), out_dir) + "?view=desktop",
            "index": posixpath.relpath(posixpath.join("m", "index.html"), out_dir),
            "plunger": posixpath.relpath(posixpath.join("m", "plunger-pumps.html"), out_dir),
            "contact": posixpath.relpath(posixpath.join("m", "contact.html"), out_dir),
            "foot_note": "Mobile edition · 手机版",
        },
        "zh": {
            "home": "首页",
            "products": "产品",
            "quote": "获取报价",
            "desktop": "电脑版",
            "lang": "EN",
            "lang_href": posixpath.relpath(posixpath.join("m", slug), out_dir),
            "desktop_href": posixpath.relpath(posixpath.join(src_dir, slug), out_dir) + "?view=desktop",
            "index": "index.html",
            "plunger": "plunger-pumps.html",
            "contact": "contact.html",
            "foot_note": "手机版 · Mobile edition",
        },
    }[lang]

    prod_links = ""
    for href, en_label, zh_label in NAV_PRODUCTS:
        label = en_label if lang == "en" else zh_label
        rel = posixpath.relpath(posixpath.join(out_dir, href), out_dir)
        # product pages live in the same folder as this page
        prod_links += f'<a class="m-prod" href="{href}"><strong>{esc(label)}</strong></a>'

    PROD_TAG = {
        "plunger-pumps.html": ("12–600 m³/h · head to 3,150 m", "12–600 m³/h · 扬程至 3,150 m"),
        "slurry-pumps.html": ("Heavy duty · abrasive solids", "重载 · 高浓度磨蚀介质"),
        "maglev-blowers.html": ("30–400 kW · oil-free air", "30–400 kW · 无油气路"),
        "mobile-pumps.html": ("Trailer or skid · diesel / electric", "拖车或撬装 · 柴油/电动"),
        "edge-ai.html": ("On-machine edge agent", "装在现场设备上的边缘智能体"),
    }
    sheet_items = ""
    for href, en_label, zh_label in NAV_PRODUCTS:
        label = en_label if lang == "en" else zh_label
        tag = PROD_TAG[href][0 if lang == "en" else 1]
        cur = ' aria-current="page"' if href == slug else ""
        sheet_items += (
            f'<a class="m-sheet-item{ " is-cur" if href == slug else ""}" href="{href}"{cur}>'
            f'<span class="t"><strong>{esc(label)}</strong><small>{esc(tag)}</small></span>'
            '<span class="chev">›</span></a>'
        )
    sheet_title = "Products" if lang == "en" else "产品"
    sheet_all = "All products" if lang == "en" else "全部产品"
    sheet_close = "Close" if lang == "en" else "关闭"

    css = posixpath.relpath("assets/css/m.css", out_dir)
    vjs = posixpath.relpath("assets/js/version.js", out_dir)
    cjs = posixpath.relpath("assets/js/chat.js", out_dir)
    ccss = posixpath.relpath("assets/css/chat.css", out_dir)
    # the calculator is the only page with live client-side maths; the mobile
    # build strips <script> from the desktop page, so load the shared calc.js here
    calcjs = (
        f'\n<script src="{posixpath.relpath("assets/js/calc.js", out_dir)}" defer></script>'
        if slug == "calculator.html"
        else ""
    )

    return f"""<!doctype html>
<html lang="{'en' if lang == 'en' else 'zh-CN'}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{esc(title)}</title>
<meta name="description" content="{esc(desc)}">
<link rel="canonical" href="{canonical}">
<meta name="theme-color" content="#0c1a26">
<meta name="format-detection" content="telephone=no">
<link rel="stylesheet" href="{ccss}">
<link rel="stylesheet" href="{css}">
<link rel="icon" href="data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 34 34'><rect width='34' height='34' rx='9' fill='%230c1a26'/><path d='M17 6.5c3.6 2.4 6 6.2 6 10.2 0 3.3-2.7 6-6 6s-6-2.7-6-6c0-4 2.4-7.8 6-10.2Z' fill='%23e2570f'/></svg>">
</head>
<body>
<div class="mhead">
  <a class="brand" href="{ui['index']}">{LOGO}<span>HONGSHI<small>{'工业泵 · Industrial Pumps' if lang == 'en' else '工业泵'}</small></span></a>
  <span class="sp"></span>
  <a class="link" href="{ui['lang_href']}">{ui['lang']}</a>
  <a class="link" href="{ui['desktop_href']}">{ui['desktop']}</a>
</div>
{content}
<div class="mfoot">
  <div class="fnav">
{prod_links.replace('class="m-prod"', 'class="fnavlink"')}
  </div>
  <p style="margin:0 0 8px">大连宏实科技有限公司 · DALIAN HONGSHI TECHNOLOGY</p>
  <p style="margin:0"><a href="mailto:18041136555@189.cn">18041136555@189.cn</a></p>
  <p style="margin:8px 0 0;color:#6f8794">© 2026 · {ui['foot_note']}</p>
</div>
<div class="m-sheet" id="mSheet" hidden>
  <button type="button" class="m-sheet-bd" data-close aria-label="{sheet_close}"></button>
  <div class="m-sheet-panel" role="dialog" aria-modal="true" aria-label="{sheet_title}">
    <div class="m-sheet-hd"><strong>{sheet_title}</strong>
      <button type="button" class="m-sheet-x" data-close aria-label="{sheet_close}">✕</button>
    </div>
    <div class="m-sheet-list">
{sheet_items}
    </div>
    <a class="m-sheet-all" href="{ui['plunger']}">{sheet_all} ›</a>
  </div>
</div>
<div class="mbar">
  <a href="{ui['index']}"><span class="ic">⌂</span>{ui['home']}</a>
  <button type="button" class="mbar-prod" id="mProdBtn" aria-expanded="false" aria-controls="mSheet"><span class="ic">▤</span>{ui['products']}</button>
  <a class="cta" href="{ui['contact']}"><span class="ic">✉</span>{ui['quote']}</a>
</div>
<script src="{vjs}" defer></script>
<script src="{cjs}" defer></script>{calcjs}
<script>
(function(){{
  var b=document.getElementById('mProdBtn'),s=document.getElementById('mSheet');
  if(!b||!s)return;
  function open(){{s.hidden=false;document.body.classList.add('m-lock');b.setAttribute('aria-expanded','true');}}
  function close(){{s.hidden=true;document.body.classList.remove('m-lock');b.setAttribute('aria-expanded','false');}}
  b.addEventListener('click',function(){{s.hidden?open():close();}});
  s.addEventListener('click',function(e){{if(e.target.closest('[data-close]'))close();}});
  s.addEventListener('click',function(e){{var a=e.target.closest('a');if(a)close();}});
  document.addEventListener('keydown',function(e){{if(e.key==='Escape')close();}});
}}());
</script>
</body>
</html>"""


def tune_calculator(content):
    """Restore the few class names the generic mobile converter strips.

    The converter keeps form containers verbatim but removes class/style, so the
    calculator loses .calc-tabs / .calc-out that m.css styles.
    """
    content = re.sub(
        r'<div class="m-form"><div>(\s*<button data-tab=)',
        r'<div class="m-form"><div class="calc-tabs">\1',
        content,
    )
    content = re.sub(
        r'<div>(\s*<h3>(?:Results|计算结果)</h3>)',
        r'<div class="calc-out">\1',
        content,
    )
    return content


def build_dir(src_dir, out_dir, lang, depth_label):
    os.makedirs(out_dir, exist_ok=True)
    src_abs = os.path.join(ROOT, src_dir) if src_dir else ROOT
    count = 0
    for name in sorted(os.listdir(src_abs)):
        if not name.endswith(".html") or name in SKIP:
            continue
        path = os.path.join(src_abs, name)
        try:
            title, desc, content = build_page(path, src_dir, lang)
        except Exception as exc:  # noqa: BLE001
            print(f"  ! {name}: {exc}")
            continue
        if not content.strip():
            print(f"  ! {name}: empty content, skipped")
            continue
        canonical = f"{DOMAIN}/{posixpath.join(out_dir.replace(ROOT, '').lstrip('/'), name)}"
        content = rewrite_paths(content, src_dir, out_dir)
        if name == "calculator.html":
            content = tune_calculator(content)
        html_out = page_shell(lang, name, title, desc, content, src_dir, out_dir, canonical)
        with open(os.path.join(out_dir, name), "w", encoding="utf-8") as f:
            f.write(html_out)
        count += 1
        print(f"  wrote {depth_label}/{name}  {len(html_out)//1024} KB")
    return count


def main():
    print("building mobile edition →")
    n1 = build_dir("", OUT_EN, "en", "m")
    n2 = build_dir("zh", OUT_ZH, "zh", "zh/m")
    print(f"done: {n1} EN + {n2} ZH mobile pages")


if __name__ == "__main__":
    main()
