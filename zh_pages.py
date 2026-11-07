#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Chinese (zh-CN) edition of the Dalian Hongshi export website.
Generated into ./zh/ ; English pages are produced by build.py.
Run: python3 zh_pages.py   (zh_pages.py = a+b+c concatenated)
"""
import os, json
from datetime import date
from apps_extra import APPS, render_body as render_app_body
from products_extra import PRODUCTS as NEW_PRODUCTS

CONFIG = {
    "brand": "DALIAN HONGSHI TECHNOLOGY",
    "brand_short": "HONGSHI",
    "brand_cn": "大连宏实科技有限公司",
    "brand_full": "Dalian Hongshi Technology Co., Ltd.",
    "tagline": "高压往复柱塞泵系统",
    "domain": "https://jeeftang.github.io/hongshi",
    "email": "18041136555@189.cn",
    "wechat_qr": "assets/img/wechat-qr.png",
    "address": "中国 · 辽宁 · 大连",
    "year": date.today().year,
}

OUT = os.path.dirname(os.path.abspath(__file__))
OUT_ZH = os.path.join(OUT, "zh")

PRODUCT_NAV = [
    ("plunger-pumps.html", "多柱塞高压泵"),
    ("slurry-pumps.html", "浆料泵"),
    ("maglev-blowers.html", "磁悬浮鼓风机与真空泵"),
    ("mobile-pumps.html", "移动式便携水泵"),
    ("edge-ai.html", "工业智能体盒子"),
]

NAV = [
    ("plunger-pumps.html", "产品", PRODUCT_NAV),
    ("applications.html", "应用领域"),
    ("calculator.html", "选型计算"),
    ("references.html", "业绩案例"),
    ("about.html", "关于我们"),
]

LOGO = """<svg width="34" height="34" viewBox="0 0 34 34" fill="none" aria-hidden="true">
<rect width="34" height="34" rx="9" fill="#0c1a26"/>
<path d="M17 6.5c3.6 2.4 6 6.2 6 10.2 0 3.3-2.7 6-6 6s-6-2.7-6-6c0-4 2.4-7.8 6-10.2Z" fill="#e2570f"/>
<path d="M17 22.7v4.8M11 14.5h12" stroke="#fff" stroke-width="1.6" stroke-linecap="round" opacity=".85"/>
</svg>"""


def head(title, desc, slug, extra_head=""):
    canonical = f"{CONFIG['domain']}/zh/{slug}"
    en_url = f"{CONFIG['domain']}/{slug}"
    return f"""<!doctype html>
<html lang="zh-CN">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="{canonical}">
<link rel="alternate" hreflang="zh-CN" href="{canonical}">
<link rel="alternate" hreflang="en" href="{en_url}">
<link rel="alternate" hreflang="x-default" href="{en_url}">
<meta property="og:type" content="website">
<meta property="og:site_name" content="{CONFIG['brand']}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="{canonical}">
<meta property="og:locale" content="zh_CN">
<meta name="twitter:card" content="summary_large_image">
<meta name="theme-color" content="#0c1a26">
<link rel="stylesheet" href="../assets/css/style.css">
<link rel="stylesheet" href="../assets/css/chat.css">
<link rel="icon" href="data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 34 34'><rect width='34' height='34' rx='9' fill='%230c1a26'/><path d='M17 6.5c3.6 2.4 6 6.2 6 10.2 0 3.3-2.7 6-6 6s-6-2.7-6-6c0-4 2.4-7.8 6-10.2Z' fill='%23e2570f'/></svg>">
{extra_head}
</head>
<body>"""


def header(active="", en_href="index.html"):
    items = ""
    for entry in NAV:
        href, label = entry[0], entry[1]
        sub = entry[2] if len(entry) > 2 else None
        if sub:
            on = " on" if any(s[0] == active for s in sub) else ""
            subitems = "".join(f'<li><a href="{h}">{l}</a></li>' for h, l in sub)
            items += f'<li class="has-sub{on}"><a href="{sub[0][0]}">{label}</a><ul class="sub">{subitems}</ul></li>'
        else:
            cls = ' class="on"' if href == active else ""
            items += f'<li><a href="{href}"{cls}>{label}</a></li>'
    return f"""<header class="site">
  <div class="wrap nav">
    <a class="brand" href="index.html">{LOGO}<span>{CONFIG['brand_short']}<small>工业泵</small></span></a>
    <ul>{items}</ul>
    <a class="lang-switch" href="{en_href}" hreflang="en" title="English version">EN</a>
    <a class="btn cta" href="contact.html">获取报价</a>
  </div>
</header>"""


def footer():
    return f"""<footer class="site">
  <div class="wrap">
    <div class="fgrid">
      <div>
        <a class="brand" href="index.html" style="color:#fff">{LOGO}<span style="color:#fff">{CONFIG['brand_short']}<small style="color:#8fa6b2">工业泵</small></span></a>
        <p style="margin-top:16px;max-width:320px">{CONFIG['brand_cn']}<br>面向矿山、电力、油气与流程工业的高压往复泵与浆料泵。</p>
      </div>
      <div>
        <h4>产品</h4>
        <ul>
          <li><a href="plunger-pumps.html">多柱塞高压泵</a></li>
          <li><a href="slurry-pumps.html">浆料泵</a></li>
          <li><a href="maglev-blowers.html">磁悬浮鼓风机与真空泵</a></li>
          <li><a href="mobile-pumps.html">移动式便携水泵</a></li>
          <li><a href="edge-ai.html">工业智能体盒子</a></li>
          <li><a href="calculator.html">选型计算器</a></li>
        </ul>
      </div>
      <div>
        <h4>应用</h4>
        <ul>
          <li><a href="mine-dewatering.html">矿井排水</a></li>
          <li><a href="filter-press-feed.html">压滤机入料</a></li>
          <li><a href="tailings-transport.html">尾矿输送</a></li>
          <li><a href="water-injection.html">油田注水</a></li>
          <li><a href="boiler-feed.html">锅炉给水</a></li>
          <li><a href="high-head-drainage.html">高扬程排水</a></li>
          <li><a href="high-pressure-descaling.html">高压水除磷清洗</a></li>
        </ul>
      </div>
      <div>
        <h4>联系</h4>
        <ul>
          <li><a href="mailto:{CONFIG['email']}">{CONFIG['email']}</a></li>
          <li>{CONFIG['address']}</li>
        </ul>
      </div>
    </div>
    <div class="copy">
      <span>© {CONFIG['year']} {CONFIG['brand_cn']} 版权所有</span>
      <span>中国设计制造 · 服务全球</span>
    </div>
  </div>
</footer>"""


def crumbs(items):
    lis = "".join(
        f'<li itemprop="itemListElement" itemscope itemtype="https://schema.org/ListItem">'
        f'<a itemprop="item" href="{u}"><span itemprop="name">{n}</span></a>'
        f'<meta itemprop="position" content="{i+1}"></li>'
        for i, (u, n) in enumerate(items)
    )
    return f'<nav class="crumbs" aria-label="面包屑"><div class="wrap"><ol style="list-style:none;display:flex;gap:8px;padding:0;margin:0" itemscope itemtype="https://schema.org/BreadcrumbList">{lis}</ol></div></nav>'


def page(slug, title, desc, body, active="", extra_head=""):
    return dict(slug=slug, title=title, desc=desc, body=body, active=active, extra_head=extra_head)


# ================================================================ 首页
INDEX_BODY = f"""
<section class="hero">
  <div class="wrap">
    <div class="badge"><i></i> 往复柱塞泵技术 · 12–600 m³/h · 扬程最高 3,150 m</div>
    <h1>高压泵，省的是电费，不是停机时间。</h1>
    <p class="lead">面向矿山、电厂、油田与流程工业的连续运行工况，提供多柱塞往复泵与浆料泵。效率 90% 以上，机械曲轴直驱，可直接替换多级离心泵。</p>
    <div class="hero-actions">
      <a class="btn" href="contact.html">提交工况参数</a>
      <a class="btn ghost" style="color:#fff;border-color:rgba(255,255,255,.35)" href="calculator.html">30 秒完成选型试算</a>
    </div>
    <div class="stats">
      <div class="stat"><b>90%+</b><span>泵效率，长期运行不衰减</span></div>
      <div class="stat"><b>12–600</b><span>m³/h 流量范围</span></div>
      <div class="stat"><b>4–50</b><span>MPa 排出压力</span></div>
      <div class="stat"><b>30,000 h</b><span>大修周期</span></div>
    </div>
  </div>
</section>

<section>
  <div class="wrap">
    <div class="sec-head">
      <p class="eyebrow">我们做什么</p>
      <h2>两大产品系列，一套工程方法</h2>
      <p class="lead">用机械直驱代替液压动力站：故障点更少、效率更高，外形尺寸可直接落进你现有的泵房。</p>
    </div>
    <div class="grid-2">
      <article class="card prod-card">
        <img class="prod-img" src="../assets/img/product-plunger.jpg" alt="安装在泵房内的多柱塞高压往复泵" loading="lazy">
        <div class="card-body">
          <p class="tag">UDZ 系列 · 3 / 5 / 7 柱塞</p>
          <h3>多柱塞高压泵</h3>
          <p>流量 12–600 m³/h，扬程 200–3,150 m（2.0–31.5 MPa），注水系列最高 70 MPa，效率均在 90% 以上。适用于锅炉给水、油田注水、高压除鳞与矿井排水。吸入口、排出口方位与被替换的多级离心泵一致——500 m³/h 的离心泵用一台 UDZ 600 替换，而不是两台并联。</p>
          <ul class="checks">
            <li>无液压站，机械曲轴驱动</li>
            <li>易损件 5,000 h 以上，大修 30,000 h 以上</li>
            <li>现场维修，不用返厂</li>
          </ul>
        </div>
        <a class="more" href="plunger-pumps.html">了解 UDZ 系列 →</a>
      </article>
      <article class="card prod-card">
        <img class="prod-img" src="../assets/img/product-slurry-1.jpg" alt="V5 立式五柱塞浆料泵" loading="lazy">
        <div class="card-body">
          <p class="tag">V5 · 立式五柱塞</p>
          <h3>耐磨工况用浆料泵</h3>
          <p>流量 100–400 m³/h，扬程最高 150 m，可输送重量浓度 30% 以上的固料。陶瓷柱塞与合金阀座承受住把离心浆料泵磨穿的磨损，效率超过 83%。</p>
          <ul class="checks">
            <li>效率 83%+，离心浆料泵仅 25–50%</li>
            <li>陶瓷柱塞 + 合金阀座</li>
            <li>易损件 4,000 h 以上，大修 30,000 h 以上</li>
          </ul>
        </div>
        <a class="more" href="slurry-pumps.html">了解 V5 浆料泵 →</a>
      </article>
    </div>
  </div>
</section>

<section>
  <div class="wrap">
    <div class="sec-head">
      <p class="eyebrow">新增产品线</p>
      <h2>无油风、移动水、厂内智能</h2>
      <p class="lead">在泵业务之外新增三条线：悬浮转子鼓风机与真空泵、成套移动泵组，以及跑在厂区网络里的工业智能体。</p>
    </div>
    <div class="grid-3">
      <article class="card">
        <div class="icon">◍</div>
        <p class="tag">磁悬浮 / 空浮</p>
        <h3>高速鼓风机与真空泵</h3>
        <p>风量 20–400 m³/min、压升 40–100 kPa，真空度可达 −75 kPa。无油、无齿轮箱，效率 70–80%，比被替换的水环泵或罗茨风机节电 20–35%。</p>
        <a class="more" href="maglev-blowers.html">查看型谱 →</a>
      </article>
      <article class="card">
        <div class="icon">◫</div>
        <p class="tag">移动机组</p>
        <h3>便携式与拖车式泵组</h3>
        <p>应急排水、防汛抢险与临时输送。柴油或电机驱动，快接管路，到现场当天就能开。</p>
        <a class="more" href="mobile-pumps.html">查看形式 →</a>
      </article>
      <article class="card">
        <div class="icon">⌁</div>
        <p class="tag">边缘智能</p>
        <h3>工业智能体盒子</h3>
        <p>27B 语言模型与 OpenClaw 智能体运行时跑在现场，四路并发、合计 40+ token/s，功耗约 58 W——不上云，数据不出厂。</p>
        <a class="more" href="edge-ai.html">查看配置 →</a>
      </article>
    </div>
  </div>
</section>

<section class="alt">
  <div class="wrap">
    <div class="sec-head">
      <p class="eyebrow">应用现场</p>
      <h2>专为"吃泵"的工况设计</h2>
    </div>
    <div class="grid-4">
      <article class="card">
        <div class="icon">⛏</div>
        <h3>矿井排水</h3>
        <p>从井下中央水仓到地面的多级提升，压力是离心泵守不住的那一关。</p>
        <a class="more" href="mine-dewatering.html">了解详情 →</a>
      </article>
      <article class="card">
        <div class="icon">▤</div>
        <h3>压滤机入料</h3>
        <p>整个进料周期压力稳定，滤饼成型更快、含水更低。</p>
        <a class="more" href="filter-press-feed.html">了解详情 →</a>
      </article>
      <article class="card">
        <div class="icon">≋</div>
        <h3>尾矿与煤泥</h3>
        <p>高浓度浆体输送，摆脱离心浆料泵"磨坏—更换"的循环。</p>
        <a class="more" href="tailings-transport.html">了解详情 →</a>
      </article>
      <article class="card">
        <div class="icon">◎</div>
        <h3>油田注水</h3>
        <p>120–500 m³/h、16–25 MPa，比功率低至 0.3 kWh/m³·MPa。</p>
        <a class="more" href="water-injection.html">了解详情 →</a>
      </article>
    </div>
  </div>
</section>

<section>
  <div class="wrap">
    <div class="grid-2" style="align-items:center;gap:56px">
      <div>
        <p class="eyebrow">用户为什么换泵</p>
        <h2>效率算得出来，检修排得出来</h2>
        <p>多级离心泵在磨蚀或高压工况下，一旦口环间隙被磨开，实际效率通常只有 45–65%。容积式柱塞泵能守住 90% 以上，因为它的容积效率不依赖精细间隙。</p>
        <ul class="checks">
          <li><strong>机械直驱。</strong>没有液压动力站，没有高速摩擦副，夏天不会油温过高。</li>
          <li><strong>原位替换。</strong>泵头方位与离心泵一致，改造是"换泵"，不是"重建泵房"。</li>
          <li><strong>磨损可预期。</strong>柱塞、阀座、密封是耗材，更换周期写得清清楚楚；曲轴、十字头、机架不是。</li>
          <li><strong>智能控制。</strong>每台机组可选配变频、状态监测、故障诊断与远程数据。</li>
        </ul>
      </div>
      <div class="card" style="background:#0c1a26;border-color:#0c1a26;color:#fff">
        <p class="tag" style="color:#ffb08a">现场案例</p>
        <h3 style="color:#fff">胜利油田 · 王岗注水站</h3>
        <p style="color:#c6d6df">七柱塞往复注水泵，2023 年 8 月投运并连续运行至今。实测比功率 0.3 kWh/m³·MPa，被替换的多级离心泵为 0.5–0.8。</p>
        <div class="kv" style="border-color:rgba(255,255,255,.14)"><span>配置</span><b>七柱塞 · 变频</b></div>
        <div class="kv" style="border-color:rgba(255,255,255,.14)"><span>工况</span><b>120–500 m³/h · 16–25 MPa</b></div>
        <div class="kv" style="border:0"><span>状态</span><b style="color:#7ee2c4">连续运行中</b></div>
      </div>
    </div>
  </div>
</section>

<section class="alt">
  <div class="wrap">
    <div class="sec-head">
      <p class="eyebrow">业绩</p>
      <h2>在役的设备，不是效果图</h2>
      <p class="lead">金矿、煤矿、油田注水站与余热锅炉房的往复泵安装现场。实测工况点、实测功率、有据可查的报告。</p>
    </div>
    <div class="gallery">
      <figure><img src="../assets/img/site-junde-1.jpg" alt="井下往复泵泵房" loading="lazy"><figcaption>煤矿排水——−50 / −250 / −500 m 三个泵房，6 台机组替换 24 台多级离心泵</figcaption></figure>
      <figure><img src="../assets/img/site-junde-3.jpg" alt="高压泵站管路" loading="lazy"><figcaption>高压排出管路，6.5 MPa 提升至 170 m 水平</figcaption></figure>
      <figure><img src="../assets/img/case-shengli.jpg" alt="胜利油田注水站" loading="lazy"><figcaption>胜利油田——官桥、王岗注水站，七柱塞机组</figcaption></figure>
      <figure><img src="../assets/img/product-slurry-2.jpg" alt="浆料泵细节" loading="lazy"><figcaption>V5 浆料泵——陶瓷柱塞与合金阀座，应对磨蚀工况</figcaption></figure>
    </div>
    <div class="kpi-row">
      <div class="kpi"><b>26.7%</b><span>干熄焦余热锅炉给水泵改造节电率</span></div>
      <div class="kpi"><b>22–37%</b><span>矿井排水改造节电率</span></div>
      <div class="kpi"><b>0.3</b><span>kWh/m³·MPa，油田注水比功率</span></div>
      <div class="kpi"><b>30,000 h</b><span>曲轴与机架大修周期</span></div>
    </div>
    <p style="margin-top:26px"><a class="btn ghost" href="references.html">查看业绩与检测报告 →</a></p>
  </div>
</section>

<section>
  <div class="wrap">
    <div class="sec-head">
      <p class="eyebrow">技术资料</p>
      <h2>买之前就能看的现场检测报告</h2>
      <p class="lead">来自在运装置的现场测试报告，流量、压力、功率与比能耗均为现场记录。完整 PDF 可在下方下载。</p>
    </div>
    <div class="report-grid">
      <div class="report-card"><div class="thumb"><img src="../assets/img/report-summary.png" alt="参考数据汇总表" loading="lazy"></div><div class="meta"><b>参考数据汇总</b><span class="muted">两个中段，改造前后实测</span><a href="../assets/docs/shandong-gold-reference-data.pdf">下载 PDF →</a></div></div>
      <div class="report-card"><div class="thumb"><img src="../assets/img/report-dongshan.png" alt="270 m 中段现场测试报告" loading="lazy"></div><div class="meta"><b>现场测试报告 — 270 m 中段</b><span class="muted">矿井排水 · 往复泵</span><a href="../assets/docs/test-report-dongshan.pdf">下载 PDF →</a></div></div>
      <div class="report-card"><div class="thumb"><img src="../assets/img/report-lingshan.png" alt="51 m 中段现场测试报告" loading="lazy"></div><div class="meta"><b>现场测试报告 — 51 m 中段</b><span class="muted">矿井排水 · 往复泵</span><a href="../assets/docs/test-report-lingshan.pdf">下载 PDF →</a></div></div>
    </div>
  </div>
</section>

<section class="tight">
  <div class="wrap">
    <div class="band">
      <div>
        <h2>给我们一个工况点，还你一个选型。</h2>
        <p>流量、扬程或压力、介质与温度——这些就够开始了。我们回复型号、性能曲线与预算价。</p>
      </div>
      <a class="btn light" href="contact.html">索取报价</a>
    </div>
  </div>
</section>
"""


def zh_index():
    return page(
        "index.html",
        "高压柱塞泵与浆料泵｜大连宏实科技有限公司",
        "多柱塞往复泵 12–600 m³/h、扬程至 3,150 m、注水系列至 70 MPa；浆料泵 100–400 m³/h、效率 83% 以上。可直接替换多级离心泵。",
        INDEX_BODY,
    )


# ================================================================ 柱塞泵
def spec(img, name, flow, head, press, note, alt):
    return f"""      <article class="spec">
        <img src="../assets/img/udq/{img}" alt="{alt}" loading="lazy">
        <div class="body">
          <h3>{name}</h3>
          <dl><dt>流量</dt><dd>{flow}</dd><dt>扬程</dt><dd>{head}</dd><dt>压力</dt><dd>{press}</dd></dl>
          <p class="small" style="margin:8px 0 0">{note}</p>
        </div>
      </article>"""


SPECS = "\n".join([
    spec("udq-12.jpg", "UDQ 12", "12 m³/h", "200–630 m", "2.0–6.3 MPa", "小型锅炉给水、高山供水", "UDQ 12 多柱塞往复泵"),
    spec("udq-20.jpg", "UDQ 20", "20 m³/h", "300–1,250 m", "3.0–12.5 MPa", "锅炉给水、除鳞", "UDQ 20 多柱塞往复泵"),
    spec("udq-30.jpg", "UDQ 30", "30 m³/h", "300–1,250 m", "3.0–12.5 MPa", "锅炉给水、流程输送", "UDQ 30 多柱塞往复泵"),
    spec("udq-46.jpg", "UDQ 46", "46 m³/h", "300–800 m", "3.0–8.0 MPa", "锅炉给水、供水", "UDQ 46 多柱塞往复泵"),
    spec("udq-60.jpg", "UDQ 60", "60 m³/h", "300–3,150 m", "3.0–31.5 MPa", "系列内扬程最高", "UDQ 60 多柱塞往复泵"),
    spec("udq-85.jpg", "UDQ 85", "85 m³/h", "300–2,000 m", "3.0–20.0 MPa", "锅炉给水、矿井排水", "UDQ 85 多柱塞往复泵"),
    spec("udq-120.jpg", "UDQ 120", "120 m³/h", "300–1,600 m", "3.0–16.0 MPa", "锅炉给水、矿井排水", "UDQ 120 多柱塞往复泵"),
    spec("udq-155.jpg", "UDQ 155", "155 m³/h", "300–1,600 m", "3.0–16.0 MPa", "矿井排水、供水", "UDQ 155 多柱塞往复泵"),
    spec("udq-200.jpg", "UDQ 200", "200 m³/h", "300–1,000 m", "3.0–10.0 MPa", "矿井排水", "UDQ 200 多柱塞往复泵"),
    spec("udz-280.jpg", "UDZ 280", "280 m³/h", "300–800 m", "3.0–8.0 MPa", "矿井排水、灰渣输送", "UDZ 280 多柱塞往复泵"),
    spec("udz-450.jpg", "UDZ 450", "450 m³/h", "300–1,000 m", "3.0–10.0 MPa", "大型矿井排水", "UDZ 450 多柱塞往复泵"),
    spec("udz-600.jpg", "UDZ 600", "600 m³/h", "300–630 m", "3.0–6.3 MPa", "最大单机——替换 500 m³/h 离心泵", "UDZ 600 多柱塞往复泵"),
    spec("udq-600h.jpg", "UDQ 600", "600 m³/h", "700–1,000 m", "7.0–10.0 MPa", "600 m³/h 高扬程，功率至 2,240 kW", "UDQ 600 多柱塞往复泵"),
])

PLUNGER_BODY = f"""
{crumbs([("index.html", "首页"), ("plunger-pumps.html", "柱塞泵")])}
<section class="page-head">
  <div class="wrap">
    <p class="eyebrow">UDZ 系列 · 多柱塞往复泵</p>
    <h1>多柱塞泵：12–600 m³/h，扬程最高 3,150 m</h1>
    <p class="lead">三柱塞、五柱塞、七柱塞机型，机械曲轴驱动。效率稳定在 90% 以上，易损件 5,000 小时起，外形尺寸可直接替代多级离心泵，泵站无需重新配管。</p>
  </div>
</section>

<section>
  <div class="wrap grid-2" style="gap:56px;align-items:start">
    <div class="prose">
      <h2>为什么选往复泵，而不是离心泵</h2>
      <p>压力超过 10 MPa 后，多级离心泵是在跟自己的物理规律较劲：每加一级就多一份间隙损失，口环一磨开效率就往下掉。柱塞泵每冲程排出固定容积，容积效率在柱塞整个寿命周期内都保持高位——连续运行通常高于 90%。</p>
      <p>直接后果就是电耗。400 m³/h、20 MPa 的工况，62% 与 90% 效率之间差着约 1,100 kW 轴功率，按年运行 8,000 小时算约合 880 万 kWh。</p>
      <div class="callout"><p><strong>改造不动土建。</strong>泵头的吸入口、排出口方位与多级离心泵一致，替换只是管路对接，而不是重建泵房。</p></div>
      <h2>机械驱动，不是液压驱动</h2>
      <p>国内工业现场多数柱塞泵走液压路线：油站给油缸加压，油缸推动柱塞。这套架构多出液压站、散热、油过滤和另一类故障模式。我们的机组用曲轴、连杆、十字头——油田泵的经典架构，因为那里讲的就是可用率。</p>
      <ul>
        <li>无液压动力站，无油冷却器，无伺服阀</li>
        <li>寄生负载更低，电机输出更多落到介质上</li>
        <li>故障是机械的、看得见的，不会藏在液压回路里</li>
      </ul>
    </div>
    <div>
      <figure class="lead-photo">
        <img src="../assets/img/product-plunger.jpg" alt="机械曲轴驱动的多柱塞往复泵" loading="eager">
        <figcaption>UDZ / UDQ 多柱塞泵——曲轴驱动，不带液压动力站。</figcaption>
      </figure>
      <div class="card" style="margin-top:20px">
        <h3>关键指标</h3>
        <ul class="checks">
          <li>三柱塞、五柱塞、七柱塞机型</li>
          <li>容积效率 ≥97%，总效率 ≥90%</li>
          <li>易损件 5,000 h 起，大修 30,000 h</li>
          <li>吸入排出方位与原离心泵一致，可直接替换</li>
        </ul>
      </div>
    </div>
  </div>
</section>

<section class="alt">
  <div class="wrap">
    <div class="sec-head">
      <p class="eyebrow">随机智能</p>
      <h2>跑在设备上的流体机械工业智能体</h2>
      <p class="lead">每台泵都可以配一套边缘智能体：一台装在设备侧的工业计算机，看着这台泵、把看到的东西讲清楚，并把工况点按在效率真正最高的位置上。</p>
    </div>
    <div class="grid-3">
      <div class="card"><p class="tag">状态</p><h3>看得懂的健康度</h3><p>振动、压力、功率折算成一个健康度指数，配一句人话结论：哪个指标在漂、漂得多快、在停机之前该做什么。</p></div>
      <div class="card"><p class="tag">能效</p><h3>省下来的电不再悄悄跑掉</h3><p>智能体按调试基线跟踪比功率。当磨损、结垢或工况变化把节电量吃掉时，它会说出来——而不是让节能量无声消失。</p></div>
      <div class="card"><p class="tag">自主</p><h3>离线，就在现场</h3><p>推理在 RK3576 级边缘模块上本地完成：不用云账号、数据不出厂区，井下或偏远泵房没有网络也能跑。</p></div>
    </div>
    <div class="grid-2" style="margin-top:28px;gap:40px;align-items:start">
      <div class="prose">
        <h3>为什么它该长在泵上，而不是长在报表里</h3>
        <p>多数监测系统止步于一条趋势线，判断"这条线是磨损、汽蚀、阀门关了还是工况变了"仍要靠人。智能体带着泵的机理模型和调试数据，能把症状归到原因，并说成班组能执行的话。</p>
        <p>因为用的是机理模型而不是黑箱，工况点一变它照样有效——这正是纯回归模型失效的场景。</p>
      </div>
      <div class="prose">
        <h3>它不做什么</h3>
        <p>不发出跳闸或启泵指令。保护归现场安全系统和人，智能体只做提醒、记录和升级上报。这条边界是刻意的——也正因如此，它才能进得了正在生产的厂区。</p>
        <h3>怎么供货</h3>
        <p>边缘模块与传感器可随泵一起报价、可对既有泵站改造加装，也可按多台设备打包。该系统目前在我们自有设备上试点运行，客户项目按项目单独报价。</p>
      </div>
    </div>
  </div>
</section>

<section>
  <div class="wrap">
    <div class="sec-head">
      <p class="eyebrow">型谱</p>
      <h2>13 个规格，覆盖 12–600 m³/h</h2>
      <p class="lead">流量由柱塞直径与转速决定，扬程由级数与压力等级决定。先按最接近的规格初选，再用计算器核对。</p>
    </div>
    <div class="spec-grid">
{SPECS}
    </div>
      <p class="small" style="margin-top:12px">转速 180–310 rpm，容积效率 ≥97%，总效率 ≥90%。扬程（m）÷100 即为对应的压力（MPa）。注水系列 UDZ 30/50/100/160/320 …/16 覆盖 7–320 m³/h、16–70 MPa——该系列样本请另行索取。</p>
      <div class="card" style="margin-top:24px">
        <h3>机械参数</h3>
        <ul class="checks">
          <li>易损件（柱塞、阀座、密封）：5,000 h 以上</li>
          <li>大修周期：30,000 h 以上</li>
          <li>现场维修——不返厂</li>
          <li>可选变频、状态监测与远程 I/O</li>
        </ul>
      </div>
  </div>
</section>

<section class="alt">
  <div class="wrap">
    <div class="sec-head"><h2>UDZ 系列的典型用途</h2></div>
    <div class="grid-3">
      <article class="card"><h3>锅炉给水</h3><p>替代工业锅炉与电站锅炉的多级离心给水泵，全负荷段压力稳定。</p><a class="more" href="contact.html">聊聊工况 →</a></article>
      <article class="card"><h3>油田注水</h3><p>120–500 m³/h、16–25 MPa；比功率低至 0.3 kWh/m³·MPa，不需要单独的润滑站。</p><a class="more" href="water-injection.html">油田注水 →</a></article>
      <article class="card"><h3>矿井排水</h3><p>从井下中央水仓多级提升，这个压力段能把离心泵寿命压到几个月。</p><a class="more" href="mine-dewatering.html">矿井排水 →</a></article>
      <article class="card"><h3>高压除鳞</h3><p>钢铁与铝材轧线除鳞，20–40 MPa，整个道次压力不掉。</p><a class="more" href="contact.html">除鳞工况 →</a></article>
      <article class="card"><h3>管输增压</h3><p>长距离浆体与清水输送，瓶颈在压力而不在流量时的选择。</p><a class="more" href="tailings-transport.html">尾矿输送 →</a></article>
      <article class="card"><h3>流程高压</h3><p>化工、石化与电力流程中需要重载往复泵的场合。</p><a class="more" href="contact.html">流程工况 →</a></article>
    </div>
  </div>
</section>

<section>
  <div class="wrap prose">
    <h2>常见问题</h2>
    <h3>能直接替换我们现有的多级离心泵吗？</h3>
    <p>多数情况可以。泵头的吸入口、排出口方位一致，底座与管路只需小幅改动即可对接。确认前我们会要一份管路草图和你现在的工况点。</p>
    <h3>需要做哪些维护？</h3>
    <p>柱塞、阀座、密封属耗材，周期从 5,000 小时起。曲轴、十字头与机架按 30,000 小时大修设计。易损件更换全部在现场完成。</p>
    <h3>电机和变频器你们供吗？</h3>
    <p>供。可以只供泵、泵加电机，或整撬供货（含变频、仪表与控制）。</p>
    <h3>执行什么标准？</h3>
    <p>UDZ 系列按中国往复式容积泵国家标准制造。材质证明、试验报告以及项目所需的第三方检验在订货阶段约定——每个市场什么有证、什么没有，我们都会写清楚。</p>
  </div>
</section>
"""


def zh_plunger():
    return page(
        "plunger-pumps.html",
        "多柱塞往复泵 12–600 m³/h，扬程至 3,150 m｜大连宏实科技有限公司",
        "三柱塞、五柱塞、七柱塞往复泵：12–600 m³/h，扬程 200–3,150 m，注水系列至 70 MPa，效率 90% 以上。可直接替换多级离心泵。",
        PLUNGER_BODY,
        active="plunger-pumps.html",
    )

# ================================================================ 浆料泵
SLURRY_BODY = f"""
{crumbs([("index.html", "首页"), ("slurry-pumps.html", "浆料泵")])}
<section class="page-head">
  <div class="wrap">
    <p class="eyebrow">V5 系列 · 立式五柱塞</p>
    <h1>磨蚀工况下仍能守住 83% 效率的浆料泵</h1>
    <p class="lead">100–400 m³/h，扬程最高 150 m，固料重量浓度 30% 以上。机械式五柱塞结构，配陶瓷柱塞与合金阀座——用来替换几周就磨穿的离心浆料泵，以及白白浪费三分之一电能的液压陶瓷柱塞泵。</p>
  </div>
</section>

<section class="tight" style="padding-top:0">
  <div class="wrap">
    <figure class="lead-photo">
      <img src="../assets/img/v5-slurry-pump.jpg" alt="V5 倒立式五柱塞浆料泵" loading="eager">
      <figcaption>V5 倒立式五柱塞浆料泵——陶瓷柱塞、合金阀座、机械曲轴驱动，不带液压站。</figcaption>
    </figure>
  </div>
</section>

<section>
  <div class="wrap">
    <div class="sec-head">
      <p class="eyebrow">问题在哪</p>
      <h2>浆体输送，是泵经济性最容易算错的地方</h2>
      <p class="lead">在选矿厂，浆体输送是公认的薄弱环节：离心浆料泵被磨蚀，电费跟着效率曲线一路下滑。</p>
    </div>
    <div class="grid-3">
      <div class="card"><p class="tag">磨损</p><h3>15 天到 6 个月</h3><p>磨蚀性浆体下的叶轮与泵壳寿命，取决于颗粒粒径与流速。每次返修都是一次停产。</p></div>
      <div class="card"><p class="tag">效率</p><h3>25–50%</h3><p>离心浆料泵在间隙被磨开后的实际运行效率。剩下的能量都变成了热和噪声。</p></div>
      <div class="card"><p class="tag">电耗</p><h3>每年 4–5 万美元</h3><p>一台中型浆料泵按工业电价折算的年电费——其中大部分损失在低效率上。</p></div>
    </div>
  </div>
</section>

<section class="alt">
  <div class="wrap">
    <div class="sec-head">
      <p class="eyebrow">V5 的答案</p>
      <h2>为磨蚀而设计的容积式结构</h2>
    </div>
    <div class="grid-2" style="gap:56px;align-items:start">
      <div class="prose">
        <p>V5 不把磨蚀性颗粒甩到高速旋转的叶轮上，而是用五个立式柱塞缓慢推送。流速低，磨损就只取决于直接接触的过流零件材质，而不是整条水力通道。</p>
        <ul>
          <li><strong>陶瓷柱塞</strong>，耐磨性远超涂层钢。</li>
          <li><strong>合金阀座</strong>，浆体通过时仍能保持高容积效率。</li>
          <li><strong>机械驱动</strong>——没有液压站，没有高速摩擦副。</li>
          <li><strong>立式布置</strong>，占地小，吸入口始终灌满。</li>
        </ul>
        <div class="callout"><p><strong>结果：</strong>效率高于 83%——比离心浆料泵高出 33 个百分点以上，同工况电耗约为一半。</p></div>
      </div>
      <div>
        <div class="table-wrap">
          <table>
            <thead><tr><th>参数</th><th>V5 五柱塞</th></tr></thead>
            <tbody>
              <tr><td>流量</td><td class="num">100–400 m³/h</td></tr>
              <tr><td>扬程</td><td class="num">最高 150 m</td></tr>
              <tr><td>排出压力</td><td class="num">最高 1.5 MPa</td></tr>
              <tr><td>固料浓度</td><td class="num">重量浓度 ≥30%</td></tr>
              <tr><td>效率</td><td class="num">&gt;83%</td></tr>
              <tr><td>易损件寿命</td><td class="num">4,000 h+</td></tr>
              <tr><td>大修周期</td><td class="num">30,000 h+</td></tr>
              <tr><td>驱动方式</td><td>机械曲轴，无液压站</td></tr>
            </tbody>
          </table>
        </div>
        <p class="small" style="margin-top:12px">以上为参考工况区间；最终选型取决于粒径分布、密度与 pH。</p>
      </div>
    </div>
  </div>
</section>

<section>
  <div class="wrap">
    <div class="sec-head"><p class="eyebrow">对比</p><h2>三种技术，同一个工况</h2></div>
    <div class="table-wrap">
      <table>
        <thead><tr><th>&nbsp;</th><th>离心浆料泵</th><th>液压陶瓷柱塞泵</th><th>V5 机械柱塞泵</th></tr></thead>
        <tbody>
          <tr><td><strong>效率</strong></td><td class="num">25–50%</td><td class="num">65–70%</td><td class="num"><strong>&gt;83%</strong></td></tr>
          <tr><td><strong>磨损寿命</strong></td><td>15 天 – 6 个月</td><td>中等</td><td>易损件 4,000 h+</td></tr>
          <tr><td><strong>液压站</strong></td><td>无</td><td>有——油、冷却、过滤</td><td>无</td></tr>
          <tr><td><strong>维护</strong></td><td>频繁返修</td><td>回路复杂</td><td>现场更换易损件</td></tr>
          <tr><td><strong>高浓度（&gt;30%）</strong></td><td>差</td><td>好</td><td>好</td></tr>
        </tbody>
      </table>
    </div>
  </div>
</section>

<section class="alt">
  <div class="wrap">
    <div class="sec-head"><h2>典型安装场合</h2></div>
    <div class="grid-3">
      <article class="card"><h3>压滤机入料</h3><p>进料与保压阶段压力稳定，周期更短，滤饼更干。</p><a class="more" href="filter-press-feed.html">压滤机入料 →</a></article>
      <article class="card"><h3>尾矿与煤泥</h3><p>高浓度输送，低流速，磨损可预期。</p><a class="more" href="tailings-transport.html">尾矿输送 →</a></article>
      <article class="card"><h3>重介与精矿</h3><p>精矿与重介输送，离心叶轮在这里往往很快就报废。</p><a class="more" href="contact.html">聊聊工况 →</a></article>
    </div>
  </div>
</section>

<section>
  <div class="wrap prose">
    <h2>常见问题</h2>
    <h3>能过多大的颗粒？</h3>
    <p>V5 针对磨机排矿、压滤机入料与尾矿的常见粒径设计。询价时请附粒径分布——阀座与阀球选型取决于它。</p>
    <h3>1.5 MPa 对我们的管路够吗？</h3>
    <p>100–400 m³/h、扬程 150 m 以内的浆体工况够用。需要更高压力时，可选 UDZ 多柱塞系列，最高 70 MPa。</p>
    <h3>一次返修要多久？</h3>
    <p>易损件现场更换，以小时计，不是以天计。30,000 小时的大修是计划检修，不是抢修。</p>
  </div>
</section>
"""


def zh_slurry():
    return page(
        "slurry-pumps.html",
        "浆料泵 100–400 m³/h，效率 83% 以上｜大连宏实科技有限公司",
        "V5 立式五柱塞浆料泵：100–400 m³/h，扬程 150 m，固料浓度 30% 以上，陶瓷柱塞与合金阀座，效率 83% 以上。",
        SLURRY_BODY,
        active="slurry-pumps.html",
    )


# ================================================================ 应用总览
APPS_BODY = f"""
{crumbs([("index.html", "首页"), ("applications.html", "应用领域")])}
<section class="page-head">
  <div class="wrap">
    <p class="eyebrow">应用领域</p>
    <h1>七类工况，泵选错，运行成本就注定偏高</h1>
    <p class="lead">矿井排水、锅炉给水、浆料输送与高压清洗有一个共同点：这些工况都在"惩罚"离心泵。下面是我们配什么、为什么这么配。</p>
  </div>
</section>

<section>
  <div class="wrap grid-2">
    <article class="card prod-card">
      <div><p class="tag">UDZ 100/16 · UDZ 160/16</p><h3>矿井排水</h3>
      <p>从井下中央水仓多级提升到地面。高扬程、含固磨蚀水，而且不接受泵停。</p></div>
      <a class="more" href="mine-dewatering.html">矿井排水 →</a>
    </article>
    <article class="card prod-card">
      <div><p class="tag">V5</p><h3>压滤机入料</h3>
      <p>进料阶段要稳压，压榨阶段要升压，离心泵两头都做不好。</p></div>
      <a class="more" href="filter-press-feed.html">压滤机入料 →</a>
    </article>
    <article class="card prod-card">
      <div><p class="tag">V5</p><h3>尾矿与煤泥</h3>
      <p>高浓度、低流速。整笔经济账的核心就是磨损寿命。</p></div>
      <a class="more" href="tailings-transport.html">尾矿输送 →</a>
    </article>
    <article class="card prod-card">
      <div><p class="tag">UDZ 320/16</p><h3>油田注水</h3>
      <p>120–500 m³/h、16–25 MPa。真正决定成本的是比功率，而这正是多级离心泵丢掉的东西。</p></div>
      <a class="more" href="water-injection.html">油田注水 →</a>
    </article>
    <article class="card prod-card">
      <div><p class="tag">UDZ 100/16 · UDZ 160/16</p><h3>锅炉给水</h3>
      <p>工业锅炉与余热锅炉的稳定高压给水，4–16 MPa，全年大部分时间连续运行。</p></div>
      <a class="more" href="boiler-feed.html">锅炉给水 →</a>
    </article>
    <article class="card prod-card">
      <div><p class="tag">UDQ 60 – UDZ 600</p><h3>高扬程排水（高山提灌）</h3>
      <p>长管线提升 300–2500 m，可单机运行，也可串联分级。</p></div>
      <a class="more" href="high-head-drainage.html">高扬程排水 →</a>
    </article>
    <article class="card prod-card">
      <div><p class="tag">UDZ 100/16 – UDZ 320/16</p><h3>高压水除磷、清洗</h3>
      <p>集管或喷嘴前 10–40 MPa，过钢全程压力平稳。</p></div>
      <a class="more" href="high-pressure-descaling.html">高压水除磷清洗 →</a>
    </article>
  </div>
</section>

<section class="alt">
  <div class="wrap">
    <div class="sec-head"><h2>典型工况区间</h2><p class="lead">可先按此初选，再用计算器核对，或直接把工况点发给我们。</p></div>
    <div class="table-wrap">
      <table>
        <thead><tr><th>应用</th><th>流量（m³/h）</th><th>扬程 / 压力</th><th>固料</th><th>推荐机型</th></tr></thead>
        <tbody>
          <tr><td>矿井排水</td><td class="num">12–600</td><td class="num">200–3,150 m</td><td>含固磨蚀水</td><td>UDQ 60–UDZ 600</td></tr>
          <tr><td>压滤机入料</td><td class="num">100–400</td><td class="num">≤150 m</td><td>30%+</td><td>V5</td></tr>
          <tr><td>尾矿输送</td><td class="num">100–400</td><td class="num">≤150 m</td><td>30–60%</td><td>V5</td></tr>
          <tr><td>油田注水</td><td class="num">7–320</td><td class="num">16–70 MPa</td><td>清水</td><td>UDZ …/16 系列</td></tr>
          <tr><td>锅炉给水</td><td class="num">100–400</td><td class="num">4–16 MPa</td><td>清水、高温</td><td>UDZ 100/16 – 160/16</td></tr>
          <tr><td>高扬程排水／高山提灌</td><td class="num">50–500</td><td class="num">300–2,500 m</td><td>低，少量泥沙</td><td>UDQ 60 – UDZ 600</td></tr>
          <tr><td>高压水除磷、清洗</td><td class="num">20–200</td><td class="num">10–40 MPa</td><td>氧化铁皮／细颗粒</td><td>UDZ 100/16 – 320/16</td></tr>
        </tbody>
      </table>
    </div>
  </div>
</section>

<section class="tight"><div class="wrap"><div class="band"><div><h2>不确定该选哪个系列？</h2><p>把流量、扬程和介质描述发过来，我们告诉你适用哪个区间——如果两个都不合适，也会直说。</p></div><a class="btn light" href="contact.html">咨询工程师</a></div></div></section>
"""


def zh_apps():
    return page(
        "applications.html",
        "泵应用：矿井排水 · 锅炉给水 · 高扬程提灌 · 除磷清洗｜大连宏实科技有限公司",
        "高压柱塞泵与浆料泵在矿井排水、锅炉给水、高扬程排水（高山提灌）与高压水除磷清洗中的应用选型指南。",
        APPS_BODY,
        active="applications.html",
    )


# ================================================================ 矿井排水
MINE_BODY = f"""
{crumbs([("index.html", "首页"), ("applications.html", "应用领域"), ("mine-dewatering.html", "矿井排水")])}
<section class="page-head">
  <div class="wrap">
    <p class="eyebrow">应用 · 矿山</p>
    <h1>高扬程、含固磨蚀水的矿井排水泵</h1>
    <p class="lead">从井下中央水仓到地面，往往还要分多级。水里有细颗粒，扬程又高，泵一停，矿就停。</p>
  </div>
</section>

<section>
  <div class="wrap grid-2" style="gap:56px;align-items:start">
    <div class="prose">
      <h2>离心排水泵的问题出在哪</h2>
      <p>多级离心泵在清水、设计点上效率不错。可井下两样都不占：水里带细颗粒，把口环间隙磨开；扬程又随水仓水位变化，一天里大半时间偏离高效区。</p>
      <p>结果就是新泵 65%、运行一段时间掉到 45–50%，叶轮和口环几个月换一次。三个泵房一起算，检修量是叠加的。</p>
      <h2>我们怎么配</h2>
      <ul>
        <li><strong>容积式多柱塞泵</strong>：扬程变化时效率不塌——输出由转速决定，不看管路特性曲线。</li>
        <li><strong>陶瓷或硬化柱塞</strong>：扛得住会磨蚀离心叶轮的细颗粒。</li>
        <li><strong>泵房之间并联或串联</strong>：每台机组按自己那级的提升高度选型。</li>
        <li><strong>按水位调速</strong>：让泵去贴合来水量，而不是频繁启停。</li>
      </ul>
      <div class="callout"><p><strong>参考业绩：</strong>国内某煤矿 −50 m、−250 m、−500 m 三个泵房，6 台多柱塞机组替换 24 台多级离心泵，三个泵站实测节电 22–37%。</p></div>
      <h2>选型区间</h2>
      <p>典型排水工况落在 UDQ 60 到 UDZ 600 之间：60–600 m³/h，扬程 300–3,150 m。若提升高度低、流量大且含固，则用 V5 浆料泵处理含固污水。</p>
    </div>
    <div>
      <div class="table-wrap">
        <table>
          <thead><tr><th>参数</th><th>典型值</th></tr></thead>
          <tbody>
            <tr><td>单泵流量</td><td class="num">100–400 m³/h</td></tr>
            <tr><td>排出压力</td><td class="num">4–25 MPa</td></tr>
            <tr><td>单级提升高度</td><td class="num">150–500 m</td></tr>
            <tr><td>固料</td><td>煤粉 / 岩粉细颗粒</td></tr>
            <tr><td>效率</td><td class="num">&gt;90%</td></tr>
            <tr><td>易损件</td><td class="num">5,000 h+</td></tr>
          </tbody>
        </table>
      </div>
      <div class="card" style="margin-top:24px">
        <h3>报价需要的信息</h3>
        <ul class="checks">
          <li>每个泵房的流量与总来水量</li>
          <li>垂直提升高度、管路长度与管径</li>
          <li>含固量与颗粒粒径</li>
          <li>供电电压与频率</li>
          <li>若为改造：原泵型号与实测功率</li>
        </ul>
      </div>
    </div>
  </div>
</section>

<section class="tight"><div class="wrap"><div class="band"><div><h2>要改造现有排水站？</h2><p>把原泵型号和一次实测功率发过来——足够我们做替换选型并估算节电量。</p></div><a class="btn light" href="contact.html">提交资料</a></div></div></section>
"""


def zh_mine():
    return page(
        "mine-dewatering.html",
        "矿井排水泵 — 高扬程 · 含固磨蚀水｜大连宏实科技有限公司",
        "井下多柱塞排水泵：100–400 m³/h、4–25 MPa，效率 90% 以上，易损件现场更换，泵房之间可并联或串联。",
        MINE_BODY,
        active="applications.html",
    )


# ================================================================ 压滤机入料
FP_BODY = f"""
{crumbs([("index.html", "首页"), ("applications.html", "应用领域"), ("filter-press-feed.html", "压滤机入料")])}
<section class="page-head">
  <div class="wrap">
    <p class="eyebrow">应用 · 选矿</p>
    <h1>整个周期都能稳住压力的压滤机入料泵</h1>
    <p class="lead">压滤机先要低阻力下的大流量，再要滤饼成型后的恒定压力。离心泵给的恰恰相反，容积式浆料泵给的才是压滤机真正需要的。</p>
  </div>
</section>

<section>
  <div class="wrap grid-2" style="gap:56px;align-items:start">
    <div class="prose">
      <h2>一个周期里发生了什么</h2>
      <p>进料：滤室空着，阻力低、流量大。压榨：滤饼形成、阻力上升，泵必须在极小流量下保住压力，而且不能把自己憋坏。</p>
      <p>离心泵活在自己的曲线上——阻力一升，流量掉，压力跟着掉。操作工只能靠节流或者干脆接受更长的周期。柱塞泵每冲程排固定容积，压力由安全阀设定，周期自然就短。</p>
      <h2>实际收益</h2>
      <ul>
        <li><strong>周期更短</strong>：压力能撑到进料结束。</li>
        <li><strong>滤饼更干</strong>：终压稳定，后续运输与烘干成本都降。</li>
        <li><strong>吸入口不汽蚀</strong>：立式五柱塞结构，进口始终灌满。</li>
        <li><strong>磨损可预期</strong>：陶瓷柱塞与合金阀座，4,000 h 以上。</li>
      </ul>
      <div class="callout"><p><strong>选型提示：</strong>入料泵通常按进料速率选，而不是按平均流量选。请告诉我们滤室容积、目标周期和浆体密度。</p></div>
    </div>
    <div>
      <div class="table-wrap">
        <table>
          <thead><tr><th>参数</th><th>典型值</th></tr></thead>
          <tbody>
            <tr><td>流量</td><td class="num">100–400 m³/h</td></tr>
            <tr><td>压力</td><td class="num">0.8–1.5 MPa</td></tr>
            <tr><td>固料</td><td class="num">重量浓度 30–60%</td></tr>
            <tr><td>效率</td><td class="num">&gt;83%</td></tr>
            <tr><td>机型</td><td>V5 立式五柱塞</td></tr>
          </tbody>
        </table>
      </div>
      <div class="card" style="margin-top:24px">
        <h3>与离心入料泵相比</h3>
        <ul class="checks">
          <li>压力撑到进料结束，而不是只有开头</li>
          <li>同工况装机功率约为一半</li>
          <li>不会被磨蚀性滤饼磨掉叶轮</li>
        </ul>
      </div>
    </div>
  </div>
</section>

<section class="tight"><div class="wrap"><div class="band"><div><h2>告诉我们压滤机规格</h2><p>滤室容积、目标周期、浆体密度——我们据此选入料泵，并给出预期周期。</p></div><a class="btn light" href="contact.html">索取选型</a></div></div></section>
"""


def zh_filterpress():
    return page(
        "filter-press-feed.html",
        "压滤机入料泵 — 全程稳压 · 效率 83% 以上｜大连宏实科技有限公司",
        "V5 五柱塞压滤机入料泵：100–400 m³/h、0.8–1.5 MPa，固料 30–60%，效率 83% 以上，周期更短、滤饼更干。",
        FP_BODY,
        active="applications.html",
    )

# ================================================================ 尾矿输送
TAIL_BODY = f"""
{crumbs([("index.html", "首页"), ("applications.html", "应用领域"), ("tailings-transport.html", "尾矿输送")])}
<section class="page-head">
  <div class="wrap">
    <p class="eyebrow">应用 · 矿山与煤炭</p>
    <h1>尾矿与煤泥泵：经济性就写在磨损寿命上</h1>
    <p class="lead">高浓度、细颗粒、连续运行。尾矿泵的成本不在采购价，而在返修、停机和电费。</p>
  </div>
</section>

<section>
  <div class="wrap grid-2" style="gap:56px;align-items:start">
    <div class="prose">
      <h2>离心泵在这里为什么撑不住</h2>
      <p>离心浆料泵靠把浆体加速到叶轮外缘线速度来工作。固料超过 30% 时，这个速度正是磨掉叶轮、蜗壳与护套的元凶。15 天到 6 个月的使用寿命属正常，每次返修都占用生产时间。</p>
      <h2>V5 的做法有什么不同</h2>
      <p>五柱塞结构以低流速、离散容积的方式推送浆体。磨损集中在柱塞表面、阀座与密封上——全部是耗材，更换周期写得明明白白。</p>
      <ul>
        <li>陶瓷柱塞，应对磨蚀性固料</li>
        <li>合金阀座，保持容积效率</li>
        <li>易损件 4,000 h 以上，大修 30,000 h 以上</li>
        <li>机械驱动——没有液压油路要维护</li>
      </ul>
      <div class="callout"><p><strong>效率：</strong>高于 83%，而被磨开的离心浆料泵只有 25–50%。250 m³/h、扬程 120 m 的工况下，这个差距就是"电费可以接受"与"电费无法接受"的差别。</p></div>
    </div>
    <div>
      <div class="table-wrap">
        <table>
          <thead><tr><th>参数</th><th>V5</th></tr></thead>
          <tbody>
            <tr><td>流量</td><td class="num">100–400 m³/h</td></tr>
            <tr><td>扬程</td><td class="num">≤150 m</td></tr>
            <tr><td>固料浓度</td><td class="num">重量浓度 30–60%</td></tr>
            <tr><td>效率</td><td class="num">&gt;83%</td></tr>
            <tr><td>易损件</td><td class="num">4,000 h+</td></tr>
            <tr><td>大修</td><td class="num">30,000 h+</td></tr>
          </tbody>
        </table>
      </div>
      <div class="card" style="margin-top:24px">
        <h3>询价请一并提供</h3>
        <ul class="checks">
          <li>固料浓度与真密度</li>
          <li>颗粒粒径分布（d50、d90）</li>
          <li>流量、管路长度与高差</li>
          <li>pH 与温度</li>
        </ul>
      </div>
    </div>
  </div>
</section>

<section class="tight"><div class="wrap"><div class="band"><div><h2>先把电耗差算出来</h2><p>我们的计算器可以按你自己的工况点和电价，对比柱塞泵与离心泵的年电费。</p></div><a class="btn light" href="calculator.html">打开计算器</a></div></div></section>
"""


def zh_tailings():
    return page(
        "tailings-transport.html",
        "尾矿与煤泥泵 — 固料 30–60% · 效率 83% 以上｜大连宏实科技有限公司",
        "V5 五柱塞尾矿与煤泥输送泵：100–400 m³/h，固料 30–60%，效率 83% 以上，易损件 4,000 h，现场维护。",
        TAIL_BODY,
        active="applications.html",
    )


# ================================================================ 油田注水
WI_BODY = f"""
{crumbs([("index.html", "首页"), ("applications.html", "应用领域"), ("water-injection.html", "油田注水")])}
<section class="page-head">
  <div class="wrap">
    <p class="eyebrow">应用 · 油气</p>
    <h1>比功率 0.3 kWh/m³·MPa 的油田注水泵</h1>
    <p class="lead">多级离心注水泵通常在 0.5–0.8 kWh/m³·MPa。我们的七柱塞机组是 0.3——而且不需要单独的润滑站。</p>
  </div>
</section>

<section>
  <div class="wrap grid-2" style="gap:56px;align-items:start">
    <div class="prose">
      <h2>决定项目成败的那个数字</h2>
      <p>注水站一开就是好几年。0.2–0.5 kWh/m³·MPa 的差距不是四舍五入的误差：300 m³/h、20 MPa 的站，一年就是约 2,900–7,300 MWh。</p>
      <p>多级离心泵还得返厂大修，意味着要么备一套机组，要么接受停产。柱塞泵就地检修。</p>
      <h2>典型配置</h2>
      <ul>
        <li><strong>UDZ 600 七柱塞</strong>，最高 600 m³/h、扬程 300–630 m——一台替换 500 m³/h 多级离心泵</li>
        <li><strong>变频或定速</strong>，取决于油藏压力策略</li>
        <li><strong>智能控制</strong>：自动调节、状态监测、故障诊断、远程遥测</li>
        <li><strong>撬装供货</strong>：含吸入缓冲、安全阀与仪表</li>
      </ul>
      <div class="callout"><p><strong>现场业绩：</strong>胜利油田王岗注水站——七柱塞机组 2023 年 8 月投运，连续运行至今，比功率 0.3 kWh/m³·MPa。</p></div>
    </div>
    <div>
      <div class="table-wrap">
        <table>
          <thead><tr><th>参数</th><th>典型值</th></tr></thead>
          <tbody>
            <tr><td>流量</td><td class="num">120–500 m³/h</td></tr>
            <tr><td>排出压力</td><td class="num">16–25 MPa</td></tr>
            <tr><td>比功率</td><td class="num">0.3 kWh/m³·MPa</td></tr>
            <tr><td>效率</td><td class="num">&gt;90%</td></tr>
            <tr><td>润滑站</td><td>不需要</td></tr>
            <tr><td>大修</td><td class="num">30,000 h+，就地</td></tr>
          </tbody>
        </table>
      </div>
    </div>
  </div>
</section>

<section class="tight"><div class="wrap"><div class="band"><div><h2>正在评估注水系统升级？</h2><p>把站场流量、注水压力和当前比功率发过来，我们算一算年电耗差。</p></div><a class="btn light" href="contact.html">联系我们</a></div></div></section>
"""


def zh_water():
    return page(
        "water-injection.html",
        "油田注水泵 — 比功率 0.3 kWh/m³·MPa｜大连宏实科技有限公司",
        "七柱塞油田注水泵：120–500 m³/h、16–25 MPa，比功率 0.3 kWh/m³·MPa，无需润滑站，就地大修。",
        WI_BODY,
        active="applications.html",
    )


# ================================================================ 选型计算器
CALC_CSS = """<style>
.tabs{display:flex;gap:8px;margin-bottom:22px;flex-wrap:wrap}
.tabs button{border:1px solid #ccd8df;background:#fff;padding:10px 16px;border-radius:9px;font:inherit;font-weight:700;font-size:14px;cursor:pointer;color:#16303f}
.tabs button.active{background:#0c1a26;color:#fff;border-color:#0c1a26}
.formula{background:#fff;border:1px solid #dde5ea;border-radius:12px;padding:18px 22px;font-family:ui-monospace,SFMono-Regular,Menlo,monospace;font-size:14px;color:#16303f;overflow-x:auto}
</style>"""

CALC_BODY = f"""
{crumbs([("index.html", "首页"), ("calculator.html", "选型计算")])}
<section class="page-head">
  <div class="wrap">
    <p class="eyebrow">工程工具</p>
    <h1>选型与节电计算器</h1>
    <p class="lead">每个项目我们都会算的两笔账：一个工况点要多少轴功率，以及离心泵换成柱塞泵后差多少。全部在浏览器里算，数据不外传。</p>
  </div>
</section>

<section>
  <div class="wrap">
    <div class="tabs">
      <button data-tab="energy" class="active">节电与回收期</button>
      <button data-tab="slurry">浆体工况校核</button>
    </div>

    <div data-panel="energy">
      <div class="calc">
        <div class="calc-form">
          <div class="field"><label for="e_q">流量 Q（m³/h）</label><input id="e_q" type="number" value="250" min="1" step="1"><div class="hint">工况点体积流量</div></div>
          <div class="field"><label for="e_h">总扬程 H（m）</label><input id="e_h" type="number" value="800" min="1" step="10"><div class="hint">排出压头减吸入压头，含管路损失</div></div>
          <div class="field"><label for="e_rho">介质密度（kg/m³）</label><input id="e_rho" type="number" value="1000" min="500" step="10"></div>
          <div class="field"><label for="e_eff">新泵效率（%）</label><input id="e_eff" type="number" value="90" min="30" max="98" step="1"><div class="hint">90% 为 UDZ 系列的公开效率值</div></div>
          <div class="field"><label for="e_eff_old">原泵效率（%）</label><input id="e_eff_old" type="number" value="55" min="10" max="95" step="1"><div class="hint">填实测值或铭牌值；磨损的多级泵常在 45–65%</div></div>
          <div class="field"><label for="e_hours">年运行小时</label><input id="e_hours" type="number" value="8000" min="100" step="100"></div>
          <div class="field"><label for="e_price">电价（美元/kWh）</label><input id="e_price" type="number" value="0.08" min="0.01" step="0.01"></div>
          <div class="field"><label for="e_capex">新泵投资（美元）</label><input id="e_capex" type="number" value="150000" min="0" step="1000"><div class="hint">可选——仅用于静态回收期</div></div>
        </div>
        <div class="calc-out">
          <h3>计算结果</h3>
          <div class="kv"><span>水力功率</span><b id="o_ph">—</b></div>
          <div class="kv"><span>新泵轴功率</span><b id="o_pnew">—</b></div>
          <div class="kv"><span>原泵轴功率</span><b id="o_pold">—</b></div>
          <div class="kv"><span>新泵年耗电</span><b id="o_kwh">—</b></div>
          <div class="kv"><span>新泵年电费</span><b id="o_cost">—</b></div>
          <div class="kv hl"><span>年节省</span><b id="o_save">—</b></div>
          <div class="kv hl"><span>静态回收期</span><b id="o_payback">—</b></div>
          <div class="kv"><span>年减排 CO₂</span><b id="o_co2">—</b></div>
          <p class="note" id="e_hint"></p>
        </div>
      </div>
      <div class="formula" style="margin-top:22px">
        P<sub>hyd</sub> = ρ · g · Q · H / 3.6×10⁶  [kW，Q 单位 m³/h] &nbsp;·&nbsp; P<sub>shaft</sub> = P<sub>hyd</sub> / η &nbsp;·&nbsp; CO₂ 系数 0.581 kg/kWh
      </div>
    </div>

    <div data-panel="slurry" style="display:none">
      <div class="calc">
        <div class="calc-form">
          <div class="field"><label for="s_q">浆体流量 Q（m³/h）</label><input id="s_q" type="number" value="250" min="1" step="1"></div>
          <div class="field"><label for="s_h">扬程 H（m）</label><input id="s_h" type="number" value="120" min="1" step="5"></div>
          <div class="field"><label for="s_c">固料浓度（重量 %）</label><input id="s_c" type="number" value="35" min="0" max="80" step="1"><div class="hint">按质量分数计的矿浆浓度</div></div>
          <div class="field"><label for="s_sg">固料真密度（g/cm³）</label><input id="s_sg" type="number" value="2.7" min="1.1" max="8" step="0.1"><div class="hint">常见岩矿 / 煤矸石尾矿取 2.7</div></div>
          <div class="field"><label for="s_eff">泵效率（%）</label><input id="s_eff" type="number" value="83" min="30" max="98" step="1"></div>
          <div class="field"><label for="s_hours">年运行小时</label><input id="s_hours" type="number" value="8000" min="100" step="100"></div>
          <div class="field"><label for="s_price">电价（美元/kWh）</label><input id="s_price" type="number" value="0.08" min="0.01" step="0.01"></div>
        </div>
        <div class="calc-out">
          <h3>计算结果</h3>
          <div class="kv"><span>混合密度</span><b id="o_mix">—</b></div>
          <div class="kv"><span>混合比重</span><b id="o_sg_mix">—</b></div>
          <div class="kv"><span>水力功率</span><b id="o_sph">—</b></div>
          <div class="kv hl"><span>轴功率</span><b id="o_sshaft">—</b></div>
          <div class="kv"><span>年耗电</span><b id="o_skwh">—</b></div>
          <div class="kv"><span>年电费</span><b id="o_scost">—</b></div>
          <p class="note" id="s_rec"></p>
        </div>
      </div>
      <div class="formula" style="margin-top:22px">
        ρ<sub>mix</sub> = 1 / (c/ρ<sub>s</sub> + (1−c)/ρ<sub>w</sub>) &nbsp;·&nbsp; c = 固料质量分数 &nbsp;·&nbsp; P<sub>shaft</sub> = ρ<sub>mix</sub>·g·Q·H / (3.6×10⁶ · η)
      </div>
    </div>
  </div>
</section>

<section class="alt">
  <div class="wrap prose">
    <h2>结果怎么读</h2>
    <p>这是初筛数据，不是正式选型。计算按清水功率与你输入的效率进行，未计 NPSH、黏度修正与电机裕量。正式选型会再加 10–15% 电机裕量，并校核吸入条件。</p>
    <h3>最容易让人意外的部分</h3>
    <p>磨损离心泵的轴功率常是新泵的 1.6–2 倍——不是电机选大了，而是效率已经掉离设计点。你能提供的最有用的一项数据，是实测输入功率。</p>
    <h3>回收期的口径</h3>
    <p>这里只算静态回收期，未计维护费节省（磨蚀工况通常为节电额的 30–50%）、停产损失与旧机残值——所以真实回收期一般比显示值更短。</p>
  </div>
</section>
"""


def zh_calc():
    return page(
        "calculator.html",
        "选型与节电计算器｜大连宏实科技有限公司",
        "免费泵计算器：水力与轴功率、年电费、相对离心泵的节电量、静态回收期，以及含混合密度的浆体工况校核。",
        CALC_BODY,
        active="calculator.html",
        extra_head=CALC_CSS,
    )


# ================================================================ 关于我们
ABOUT_BODY = f"""
{crumbs([("index.html", "首页"), ("about.html", "关于我们")])}
<section class="page-head">
  <div class="wrap">
    <p class="eyebrow">关于我们</p>
    <h1>二十余年工业工程积累，专注流体机械</h1>
    <p class="lead">{CONFIG['brand_cn']}成立于 1999 年，位于辽宁省大连市。2020 年起设立流体机械事业部，从事流体机械设备的成套制造与国际贸易。</p>
  </div>
</section>

<section>
  <div class="wrap grid-2" style="gap:56px;align-items:start">
    <div class="prose">
      <h2>公司背景</h2>
      <p>大连宏实科技有限公司成立于 1999 年 11 月 26 日，位于辽宁省大连市。公司起家从事工业自动化产品与系统集成，二十几年以来积累了丰富的工业企业工程经验，广泛服务于机械制造、造船、汽车、电子、矿业、石油化工、烟草等领域。</p>
      <p>2020 年，随着业务发展，公司成立流体机械事业部，主要从事流体机械设备的成套制造与国际贸易。我们流体机械设备的工厂位于大连旅顺与安徽宣城。</p>
      <p>事业部专注两条技术路线：高速直驱与低速大扭矩驱动，这也是我们所有泵产品背后的两种架构。</p>
      <h2>已交付的项目</h2>
      <ul>
        <li><strong>锅炉给水</strong>——120 t/h 与 130/160 t/h 机组替换工业锅炉多级离心给水泵，节电 21% 与 19%。</li>
        <li><strong>矿井排水</strong>——−50、−250、−500 m 三个泵房，6 台机组替换 24 台离心泵，节电 22–37%。</li>
        <li><strong>干熄焦余热锅炉</strong>——给水泵替换，节电 26.7%，回收期 3.2 年。</li>
        <li><strong>油田注水</strong>——胜利油田七柱塞注水站，比功率 0.3 kWh/m³·MPa。</li>
      </ul>
      <h2>我们怎么做项目</h2>
      <p>多数项目都从一个实测工况点开始，而不是一份技术规格书。我们要流量、压力、运行小时和一次功率读数，然后给出机型和一个数字。如果算不出节电，我们会直说——自己赚不回投资的泵，不算项目。</p>
    </div>
    <div>
      <div class="card">
        <h3>一览</h3>
        <div class="kv" style="color:var(--ink);border-color:var(--line)"><span class="muted">成立</span><b>1999 年 11 月 · 辽宁大连</b></div>
        <div class="kv" style="color:var(--ink);border-color:var(--line)"><span class="muted">工厂</span><b>大连旅顺 · 安徽宣城</b></div>
        <div class="kv" style="color:var(--ink);border-color:var(--line)"><span class="muted">产品范围</span><b>12–600 m³/h · 扬程 200–3,150 m · 至 70 MPa</b></div>
        <div class="kv" style="color:var(--ink);border-color:var(--line)"><span class="muted">泵效率</span><b>&gt;90%</b></div>
        <div class="kv" style="color:var(--ink);border-color:var(--line)"><span class="muted">大修周期</span><b>30,000 h+</b></div>
        <div class="kv" style="color:var(--ink);border:0"><span class="muted">市场</span><b>矿山 · 电力 · 油气 · 流程工业</b></div>
      </div>
      <div class="card" style="margin-top:20px">
        <h3>工程支持</h3>
        <ul class="checks">
          <li>工况点选型与性能曲线复核</li>
          <li>结合现有管路的改造布置</li>
          <li>调试与操作培训</li>
          <li>按磨损周期配置的备件方案</li>
        </ul>
      </div>
    </div>
  </div>
</section>

<section class="alt">
  <div class="wrap">
    <div class="sec-head">
      <p class="eyebrow">现场</p>
      <h2>我们的设备在哪里运行</h2>
    </div>
    <div class="gallery">
      <figure><img src="../assets/img/site-junde-2.jpg" alt="泵站安装现场" loading="lazy"><figcaption>矿井排水站——往复泵泵房</figcaption></figure>
      <figure><img src="../assets/img/site-junde-4.jpg" alt="高压泵撬" loading="lazy"><figcaption>高压提升泵站，排出压力 6.5 MPa</figcaption></figure>
      <figure><img src="../assets/img/site-junde-3.jpg" alt="高压泵站管路" loading="lazy"><figcaption>高压排出管路与仪表</figcaption></figure>
    </div>
  </div>
</section>

<section class="tight"><div class="wrap"><div class="band"><div><h2>正在做出口项目？</h2><p>可报 FOB 大连 / FOB 上海或 CIF，随货提供英文样本、性能曲线与装箱单。</p></div><a class="btn light" href="contact.html">联系销售</a></div></div></section>
"""


def zh_about():
    return page(
        "about.html",
        "关于大连宏实科技有限公司 — 工业工程与流体机械 · 大连",
        "多柱塞往复泵与浆料泵制造企业，研发依托四川省机械研究设计院；已交付锅炉给水、矿井排水与油田注水项目。",
        ABOUT_BODY,
        active="about.html",
    )


# ================================================================ 联系我们
CONTACT_BODY = f"""
{crumbs([("index.html", "首页"), ("contact.html", "联系我们")])}
<section class="page-head">
  <div class="wrap">
    <p class="eyebrow">联系我们</p>
    <h1>发来工况点，给你选型</h1>
    <p class="lead">流量、扬程或压力、介质、温度与年运行小时。如果是替换现有泵，再加上型号和一次实测功率——这些就够我们做选型并估算节电量。</p>
  </div>
</section>

<section>
  <div class="wrap grid-2" style="gap:56px;align-items:start">
    <div>
      <form class="enquiry" action="https://formsubmit.co/18041136555@189.cn" method="POST">
        <div><label class="small" for="name">姓名</label><input id="name" name="name" required></div>
        <div><label class="small" for="company">公司</label><input id="company" name="company"></div>
        <div><label class="small" for="email">邮箱</label><input id="email" name="email" type="email" required></div>
        <div><label class="small" for="country">国家 / 地区</label><input id="country" name="country"></div>
        <div class="full"><label class="small" for="duty">工况参数</label><textarea id="duty" name="duty" placeholder="流量 m³/h · 扬程 m 或压力 MPa · 介质 · 固料浓度 % · 温度 · 年运行小时 · 现有泵型号"></textarea></div>
        <div class="full"><button class="btn" type="submit">提交询价</button></div>
      </form>
      <p class="small" style="margin-top:14px">首次使用表单会有一道确认步骤（防垃圾提交）。也可以直接写信到 <a href="mailto:{CONFIG['email']}">{CONFIG['email']}</a>。</p>
    </div>
    <div>
      <div class="card">
        <h3>联系方式</h3>
        <div class="kv" style="color:var(--ink);border-color:var(--line)"><span class="muted">邮箱</span><b><a href="mailto:{CONFIG['email']}">{CONFIG['email']}</a></b></div>
        <div class="kv" style="color:var(--ink);border:0"><span class="muted">地址</span><b>{CONFIG['address']}</b></div>
      </div>
      <div class="card" style="margin-top:20px;text-align:center">
        <h3 style="text-align:left">微信</h3>
        <img src="../{CONFIG['wechat_qr']}" alt="微信二维码 — 零碳小助手" style="width:180px;height:180px;border-radius:8px;display:block;margin:0 auto 10px">
        <p class="small" style="margin:0">扫码加微信<br>
        本市场不使用 WhatsApp，电话与询价请走邮箱。</p>
      </div>
      <div class="card" style="margin-top:20px">
        <h3>接下来会发生什么</h3>
        <ul class="checks">
          <li>我们会在一个工作日内复核工况点</li>
          <li>你会收到型号、性能曲线与预算价</li>
          <li>若需要现场踏勘或实测数据，我们会先把要求讲清</li>
        </ul>
      </div>
      <div class="card" style="margin-top:20px">
        <h3>贸易条款</h3>
        <p class="small" style="margin:0">FOB 大连 / FOB 上海或 CIF。每个出口订单随货提供英文样本、总装图、性能曲线、装箱单与试验报告。</p>
      </div>
    </div>
  </div>
</section>
"""


def zh_contact():
    return page(
        "contact.html",
        "联系我们 — 索取泵报价｜大连宏实科技有限公司",
        "提交工况点，获取选型与预算价。高压柱塞泵与浆料泵，FOB 大连 / FOB 上海或 CIF，英文技术文件齐备。",
        CONTACT_BODY,
        active="contact.html",
    )


# ================================================================ 业绩案例
REF_BODY = f"""
{crumbs([("index.html", "首页"), ("references.html", "业绩案例")])}
<section class="page-head">
  <div class="wrap">
    <p class="eyebrow">业绩与检测报告</p>
    <h1>来自在运装置的实测数据</h1>
    <p class="lead">下面每一个数字都来自现场测试：流量、压力、输入功率与比能耗均在机组上实测，不是抄自样本曲线。</p>
  </div>
</section>

<section>
  <div class="wrap">
    <div class="sec-head">
      <p class="eyebrow">项目</p>
      <h2>部分业绩</h2>
    </div>
    <div class="case-row">
      <article class="case">
        <img src="../assets/img/site-junde-1.jpg" alt="井下泵房" loading="lazy">
        <div class="body">
          <div class="tags"><span>煤矿</span><span>排水</span></div>
          <h3>三个泵房，−50 / −250 / −500 m</h3>
          <p class="small">6 台往复机组替换 24 台多级离心泵：台数更少、比能耗更低，检修在现场完成而不必返厂。</p>
        </div>
      </article>
      <article class="case">
        <img src="../assets/img/case-shengli.jpg" alt="胜利油田注水站" loading="lazy">
        <div class="body">
          <div class="tags"><span>油田</span><span>注水</span></div>
          <h3>胜利油田 — 官桥与王岗注水站</h3>
          <p class="small">七柱塞注水泵自 2023 年连续运行。实测比功率低至 0.3 kWh/m³·MPa，被替换的离心机组为 0.5–0.8。</p>
        </div>
      </article>
      <article class="case">
        <img src="../assets/img/report-summary.png" alt="参考数据表" loading="lazy" style="object-position:top">
        <div class="body">
          <div class="tags"><span>金矿</span><span>两个中段</span></div>
          <h3>金矿排水 — 270 m 与 51 m 中段</h3>
          <p class="small">2024 年 4 月的现场测试报告，两个中段的往复泵工况点与功率由业主方工程师记录。</p>
          <p><a class="more" href="../assets/docs/shandong-gold-reference-data.pdf">参考数据（PDF） →</a></p>
        </div>
      </article>
      <article class="case">
        <img src="../assets/img/product-plunger.jpg" alt="锅炉给水泵安装" loading="lazy">
        <div class="body">
          <div class="tags"><span>电力</span><span>锅炉给水</span></div>
          <h3>干熄焦余热锅炉</h3>
          <p class="small">CDQ 余热锅炉给水泵替换：节电 26.7%，按年运行 8,000 小时计年节电约 128.5 万 kWh，回收期 3.2 年。</p>
        </div>
      </article>
      <article class="case">
        <img src="../assets/img/product-slurry-2.jpg" alt="浆料泵" loading="lazy">
        <div class="body">
          <div class="tags"><span>有色</span><span>浆体</span></div>
          <h3>有色金属矿 — 浆体输送</h3>
          <p class="small">固料重量浓度 30% 以上的磨蚀性浆体，离心浆料泵返修后几个月内效率就掉下来。</p>
        </div>
      </article>
      <article class="case">
        <img src="../assets/img/site-junde-3.jpg" alt="高压管路" loading="lazy">
        <div class="body">
          <div class="tags"><span>工业</span><span>高压</span></div>
          <h3>工业锅炉给水 — 120 / 130 / 160 t/h</h3>
          <p class="small">多级离心给水泵改为三柱塞与五柱塞机组，同等蒸发量下节电 19–21%。</p>
        </div>
      </article>
    </div>
  </div>
</section>

<section class="alt">
  <div class="wrap">
    <div class="sec-head">
      <p class="eyebrow">技术资料</p>
      <h2>现场检测报告</h2>
      <p class="lead">在运装置的扫描报告。每份含泵型号、实测流量与压力、电输入以及由此得出的比能耗。</p>
    </div>
    <div class="report-grid">
      <div class="report-card"><div class="thumb"><img src="../assets/img/report-dongshan.png" alt="270 m 中段测试报告" loading="lazy"></div><div class="meta"><b>现场测试报告 — 270 m 中段</b><span class="muted">矿井排水 · 2024 年 4 月</span><a href="../assets/docs/test-report-dongshan.pdf">下载 PDF →</a></div></div>
      <div class="report-card"><div class="thumb"><img src="../assets/img/report-lingshan.png" alt="51 m 中段测试报告" loading="lazy"></div><div class="meta"><b>现场测试报告 — 51 m 中段</b><span class="muted">矿井排水 · 2024 年 4 月</span><a href="../assets/docs/test-report-lingshan.pdf">下载 PDF →</a></div></div>
      <div class="report-card"><div class="thumb"><img src="../assets/img/report-summary.png" alt="参考数据汇总" loading="lazy"></div><div class="meta"><b>参考数据汇总</b><span class="muted">两个中段，改造前后</span><a href="../assets/docs/shandong-gold-reference-data.pdf">下载 PDF →</a></div></div>
    </div>
    <p class="small" style="margin-top:22px">具体订单的合格证、材质报告与出厂试验记录随报价文件一并提供。机组按中国往复泵标准制造；目标市场所需的认证按项单独报价。</p>
  </div>
</section>

<section class="tight">
  <div class="wrap">
    <div class="band">
      <div>
        <h2>需要完整业绩清单？</h2>
        <p>告诉我们应用场合，我们把最接近的同类装置连同实测数据一起发给你。</p>
      </div>
      <a class="btn light" href="contact.html">索取业绩资料</a>
    </div>
  </div>
</section>
"""


def zh_references():
    return page(
        "references.html",
        "业绩与现场检测报告｜大连宏实科技有限公司",
        "矿井排水、油田注水、锅炉给水与浆体输送的已投运业绩，附可下载的现场检测报告，含实测流量、压力与功率。",
        REF_BODY,
        active="references.html",
    )



# ================================================================ 新增应用领域页
def zh_extra_apps():
    out = []
    for app in APPS:
        d = app["zh"]
        body = render_app_body(
            app,
            "zh",
            crumbs([("index.html", "首页"), ("applications.html", "应用领域"), (app["slug"], d["crumb"])]),
        )
        out.append(page(app["slug"], d["title"], d["desc"], body, active="applications.html"))
    return out


def zh_new_products():
    out = []
    for p in NEW_PRODUCTS:
        d = p["zh"]
        body = d["body"].replace(
            "{crumbs}",
            crumbs([("index.html", "首页"), (p["slug"], d["crumb"])]),
        ).replace('src="assets/', 'src="../assets/').replace('href="assets/', 'href="../assets/')
        out.append(page(p["slug"], d["title"], d["desc"], body, active=p["slug"]))
    return out


# ================================================================ 404
NOTFOUND_BODY = """<section class="page-head"><div class="wrap"><h1>页面不存在</h1><p class="lead">这个页面找不到了。可以回到产品页，或者直接把工况点发给我们。</p><p style="margin-top:24px"><a class="btn" href="index.html">返回首页</a></p></div></section>"""


def zh_404():
    return page(
        "404.html",
        "页面不存在｜大连宏实科技有限公司",
        "页面不存在。",
        NOTFOUND_BODY,
    )


# ================================================================ build
def main():
    os.makedirs(OUT_ZH, exist_ok=True)
    pages = [
        zh_index(), zh_plunger(), zh_slurry(), zh_apps(), zh_mine(),
        zh_filterpress(), zh_tailings(), zh_water(), *zh_extra_apps(), zh_calc(),
        zh_about(), zh_contact(), zh_references(), *zh_new_products(), zh_404(),
    ]
    for p in pages:
        doc = (
            head(p["title"], p["desc"], p["slug"], p["extra_head"])
            + header(p["active"], en_href="../" + p["slug"])
            + p["body"]
            + footer()
            + '\n<script src="../assets/js/calc.js" defer></script>\n<script src="../assets/js/chat.js" defer></script>\n</body>\n</html>'
        )
        with open(os.path.join(OUT_ZH, p["slug"]), "w", encoding="utf-8") as f:
            f.write(doc)
        print("wrote zh/" + p["slug"], len(doc))


if __name__ == "__main__":
    main()
