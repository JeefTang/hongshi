#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Chinese (zh-CN) edition of the Dalian Hongshi export website.
Generated into ./zh/ ; English pages are produced by build.py.
Run: python3 zh_pages.py   (zh_pages.py = a+b+c concatenated)
"""
import os, json
from datetime import date

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

NAV = [
    ("plunger-pumps.html", "柱塞泵"),
    ("slurry-pumps.html", "浆料泵"),
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
<link rel="icon" href="data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 34 34'><rect width='34' height='34' rx='9' fill='%230c1a26'/><path d='M17 6.5c3.6 2.4 6 6.2 6 10.2 0 3.3-2.7 6-6 6s-6-2.7-6-6c0-4 2.4-7.8 6-10.2Z' fill='%23e2570f'/></svg>">
{extra_head}
</head>
<body>"""


def header(active="", en_href="index.html"):
    items = ""
    for href, label in NAV:
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
