/* HONGSHI · on-site consultation widget
   Layer 1: offline knowledge base (built from the site's own published figures)
   Layer 2: optional LLM endpoint (assets/data/chat-config.json -> endpoint)
   Layer 3: escalate to the sales inbox when the question is out of scope */
(function () {
  "use strict";
  var ZH = (document.documentElement.lang || "en").toLowerCase().indexOf("zh") === 0;
  var T = ZH ? {
    btn: "在线咨询",
    title: "宏实技术咨询",
    sub: "工程师在线 · 通常 1 个工作日内回复",
    ph: "输入工况或问题，例如：120 m³/h，16 MPa，含固 5%…",
    note: "自动应答仅供参考，正式选型以工程师确认为准",
    greet: "你好，我是大连宏实的技术咨询助手。\n可以帮你：查系列参数、判断该用柱塞泵还是浆料泵、估算节能、索取样本与试验报告。\n直接描述工况最快：流量、扬程或压力、介质、温度、年运行小时。",
    chips: ["选型：流量 + 压力", "柱塞泵 vs 离心泵", "浆料泵（含固 ≥30%）", "联系工程师"],
    human: "转工程师",
    escTitle: "留下邮箱，工程师 1 个工作日内回复",
    escName: "姓名（选填）",
    escMail: "邮箱（必填）",
    escBtn: "发送并等待回复",
    escOk: "已收到，工程师会尽快回复到你的邮箱。",
    escFail: "发送失败，请直接发邮件到 ",
    escAlt: "或直接发邮件：",
    typing: "正在输入",
    errNet: "网络不可用，已切换为本地知识库回答。",
    copied: "对话已复制"
  } : {
    btn: "Ask an engineer",
    title: "HONGSHI technical chat",
    sub: "Engineers online · replies within one working day",
    ph: "Describe the duty: flow m³/h, head m or pressure MPa, fluid…",
    note: "Automated answers are indicative — final selection is confirmed by an engineer",
    greet: "Hello — I answer technical questions for Dalian Hongshi.\nI can look up series data, tell you whether a plunger or slurry pump fits, estimate the energy difference, or send datasheets and test reports.\nFastest way: give me flow, head or pressure, fluid, temperature and annual hours.",
    chips: ["Sizing: flow + pressure", "Plunger vs centrifugal", "Slurry, solids ≥30%", "Talk to an engineer"],
    human: "Talk to an engineer",
    escTitle: "Leave your email — an engineer replies within one working day",
    escName: "Name (optional)",
    escMail: "Email (required)",
    escBtn: "Send and wait for a reply",
    escOk: "Received. An engineer will reply to your email shortly.",
    escFail: "Send failed — please email ",
    escAlt: "Or email directly: ",
    typing: "typing",
    errNet: "Network unavailable — answered from the local knowledge base.",
    copied: "Transcript copied"
  };

  var EMAIL = "18041136555@189.cn";

  /* ---------------------------------------------------------------- knowledge base
     Every figure below is taken from this website. Do not add unverified numbers. */
  var KB = [
    { id: "range", k: ["range", "capacity", "flow range", "how much flow", "max flow", "参数范围", "流量范围", "最大流量", "多大流量", "规格范围", "范围"],
      en: "Multi-plunger pumps: 12–600 m³/h, head up to 3,150 m, discharge pressure up to about 70 MPa.\nSlurry pumps (V5): 100–400 m³/h, head up to 150 m (1.5 MPa), solids 30%+ by weight.\nTell me your flow and pressure and I will point to the right series.",
      zh: "多柱塞泵：12–600 m³/h，扬程最高 3,150 m，排出压力最高约 70 MPa。\n浆料泵 V5：100–400 m³/h，扬程 ≤150 m（1.5 MPa），含固 ≥30%（重量）。\n告诉我流量和压力，我直接说该看哪个系列。" },

    { id: "series_udq", k: ["udq", "three plunger", "five plunger", "seven plunger", "三柱塞", "五柱塞", "七柱塞", "柱塞泵型号", "型号"],
      en: "UDQ series (mechanical crank, 3 / 5 / 7 plungers):\nUDQ 12 → 12 m³/h, 200–630 m, 2.0–6.3 MPa\nUDQ 20 / 30 → 300–1,250 m, 3.0–12.5 MPa\nUDQ 46 → 300–800 m\nUDQ 60 → 300–3,150 m (highest head)\nUDQ 85 → 300–2,000 m\nUDQ 120 / 155 / 200 and UDZ 280 / 450 / 600, UDQ 600H for the larger flows.\nWhich duty are you sizing?",
      zh: "UDQ 系列（机械曲轴，3／5／7 柱塞）：\nUDQ 12 → 12 m³/h，200–630 m，2.0–6.3 MPa\nUDQ 20／30 → 300–1,250 m，3.0–12.5 MPa\nUDQ 46 → 300–800 m\nUDQ 60 → 300–3,150 m（最高扬程）\nUDQ 85 → 300–2,000 m\n更大流量：UDQ 120／155／200、UDZ 280／450／600、UDQ 600H。\n你的工况是多大流量、多少压力？" },

    { id: "series_udz16", k: ["udz", "16 mpa", "25 mpa", "water injection series", "注水", "16兆帕", "油田注水"],
      en: "UDZ …/16 family — the water-injection range: 7–320 m³/h at 16–70 MPa, volumetric efficiency ≥97%, overall efficiency 88–90%+.\nOn Shengli oilfield injection duty the measured specific power is around 0.3 kWh/m³·MPa where the centrifugal units drew 0.5–0.8.",
      zh: "UDZ …/16 系列＝注水专用型谱：7–320 m³/h，16–70 MPa，容积效率 ≥97%，总效率 88–90% 以上。\n胜利油田注水实测单耗约 0.3 kWh/m³·MPa，原离心泵为 0.5–0.8。" },

    { id: "series_v5", k: ["v5", "slurry", "浆料", "渣浆", "尾矿", "含固", "solid", "abrasive", "磨蚀"],
      en: "V5 series — vertical five-plunger slurry pump: 100–400 m³/h, head up to 150 m, solids ≥30% by weight, efficiency >83% (a centrifugal slurry pump runs 25–50% once worn).\nCeramic plungers, alloy valve seats, mechanical crank drive — no hydraulic power pack. Wear parts 4,000 h+, overhaul 30,000 h+.\nSolids size distribution, density and pH decide the final trim — send those and we will confirm.",
      zh: "V5 系列＝立式五柱塞浆料泵：100–400 m³/h，扬程 ≤150 m，含固 ≥30%（重量），效率 >83%（离心渣浆泵磨损后通常只有 25–50%）。\n陶瓷柱塞＋合金阀座，机械曲轴直驱，无液压站；过流件 4,000 h 以上，大修周期 30,000 h 以上。\n最终配型要看粒径分布、密度和 pH——把这些给我，我来确认。" },

    { id: "why_plunger", k: ["why", "compare", "centrifugal", "difference", "better than", "为什么", "对比", "离心泵", "区别", "优势"],
      en: "Above roughly 10 MPa a multistage centrifugal pump fights its own physics: every stage adds clearance loss and efficiency falls as wear rings open.\nA plunger pump displaces a fixed volume per stroke, so volumetric efficiency stays high (typically >90%) for the life of the plunger.\nExample from the site: 400 m³/h at 20 MPa, 62% vs 90% efficiency ≈ 1,100 kW shaft power, about 8.8 million kWh a year at 8,000 h.",
      zh: "超过约 10 MPa 后，多级离心泵是在跟自己的物理规律较劲：每一级都增加间隙损失，磨损环一开效率就掉。\n柱塞泵每行程排量固定，容积效率在整个寿命期内都保持高位（通常 >90%）。\n站上例子：400 m³/h、20 MPa，效率 62% 对 90%，轴功率差约 1,100 kW，按 8,000 h 算一年约 880 万 kWh。" },

    { id: "efficiency", k: ["efficiency", "efficient", "90%", "83%", "效率", "多高"],
      en: "Plunger pumps: stable efficiency above 90% in continuous service; UDZ …/16 shows volumetric efficiency ≥97% and overall 88–90%+.\nV5 slurry: >83%, against 25–50% for a worn centrifugal slurry pump.\nEfficiency is measured, not catalogue-claimed — the site's test reports show measured flow, pressure and input power.",
      zh: "柱塞泵：连续运行效率稳定在 90% 以上；UDZ …/16 容积效率 ≥97%，总效率 88–90% 以上。\nV5 浆料泵：>83%，而磨损后的离心渣浆泵只有 25–50%。\n数据是实测的——站上试验报告里有实测流量、压力和输入功率。" },

    { id: "wear", k: ["wear", "spare parts", "life", "maintenance", "overhaul", "备件", "寿命", "维护", "检修", "大修", "易损件"],
      en: "Plunger pumps: wear parts from 5,000 h, overhaul interval 30,000 h+.\nV5 slurry: wear parts 4,000 h+, overhaul 30,000 h+.\nMaintenance is on site — plungers, seals and valve seats are accessible without returning the machine to a factory. Spare kits are quoted with the pump.",
      zh: "柱塞泵：易损件寿命 5,000 h 起，大修周期 30,000 h 以上。\nV5 浆料泵：过流件 4,000 h 以上，大修 30,000 h 以上。\n维护在现场做——柱塞、密封、阀座可拆换，不必整机返厂。备件包随机报价。" },

    { id: "drive", k: ["hydraulic", "crank", "drive", "液压", "驱动", "曲轴", "机械"],
      en: "Our machines use a crankshaft, connecting rod and crosshead — the architecture used in oilfield pumps. No hydraulic power pack, no oil cooler, no servo valve.\nThat removes a parasitic load and a whole family of failure modes: faults are mechanical and visible instead of hidden in a hydraulic circuit.",
      zh: "我们用曲轴＋连杆＋十字头，这是油田泵的架构。没有液压站、没有油冷却器、没有伺服阀。\n少一份寄生损耗，也少一整类故障源：故障是机械的、看得见的，而不是藏在液压回路里。" },

    { id: "retrofit", k: ["retrofit", "replace", "existing pump", "civil", "piping", "改造", "替换", "原有", "土建", "管路", "安装"],
      en: "Pump heads are arranged with the same suction and discharge orientation as the multistage centrifugal unit, so a replacement is a piping tie-in rather than a pump-house rebuild.\nFor a replacement quote we need: existing model, measured flow and pressure, and a power reading — that is enough to size it and estimate the saving.",
      zh: "泵头进出口方位与原多级离心泵一致，替换是管路对接，不是泵房重建。\n替换报价只需要：原泵型号、实测流量与压力、一个功率读数——足够配型并估算节电量。" },

    { id: "application", k: ["application", "where", "use for", "应用", "用在哪", "工况", "场景", "能用"],
      en: "Four duties where the choice decides operating cost:\n• Mine dewatering — 12–600 m³/h, 200–3,150 m; UDQ 60 – UDZ 600\n• Filter press feed — 100–400 m³/h, ≤150 m, 30%+ solids; V5\n• Tailings / coal slime — 100–400 m³/h, 30–60% solids; V5\n• Oilfield water injection — 7–320 m³/h, 16–70 MPa; UDZ …/16\nBoiler feed, descaling and process high pressure are covered by the UDQ range.",
      zh: "决定运行成本的四个典型工况：\n• 矿山排水：12–600 m³/h，200–3,150 m；UDQ 60 – UDZ 600\n• 压滤机喂料：100–400 m³/h，≤150 m，含固 30%+；V5\n• 尾矿／煤泥：100–400 m³/h，含固 30–60%；V5\n• 油田注水：7–320 m³/h，16–70 MPa；UDZ …/16\n锅炉给水、除鳞、流程高压由 UDQ 系列覆盖。" },

    { id: "boiler", k: ["boiler", "feed water", "锅炉", "给水", "电厂", "power plant"],
      en: "Boiler feed is the UDQ range: e.g. UDQ 46 (46 m³/h, 3.0–8.0 MPa) for small industrial boilers, UDQ 60 up to 31.5 MPa.\nReference: 120 / 130 / 160 t/h industrial boiler feed conversions — multistage centrifugal replaced by three- and five-plunger units, 19–21% saving at identical steam output.\nA coke dry quenching waste-heat boiler feed replacement measured 26.7% saving, ~128,500 kWh a year at 8,000 h, 3.2-year payback.",
      zh: "锅炉给水走 UDQ 系列：如 UDQ 46（46 m³/h，3.0–8.0 MPa）适合小型工业锅炉，UDQ 60 最高 31.5 MPa。\n业绩：120／130／160 t/h 工业锅炉给水改造，多级离心泵换三柱塞／五柱塞，同产汽量下节电 19–21%。\n干熄焦余热锅炉给水泵改造实测节电 26.7%，按 8,000 h 年节电约 12.85 万 kWh，回收期 3.2 年。" },

    { id: "price", k: ["price", "cost", "how much", "quote", "quotation", "budget", "价格", "报价", "多少钱", "费用", "预算", "单价"],
      en: "We do not publish equipment prices — a quote is built per duty point, because impeller/plunger trim, materials, motor and certification all change with the application.\nSend flow, head or pressure, fluid (with solids and pH), temperature and annual hours, and you get a model, a curve and a budgetary price. Reviewed within one working day.\nWant me to take those details now?",
      zh: "我们不公开设备价格——报价按具体工况出，因为柱塞/叶轮配型、材质、电机、认证都会随应用变化。\n把流量、扬程或压力、介质（含固与 pH）、温度、年运行小时发来，我们回：型号＋曲线＋预算价。1 个工作日内答复。\n要现在把这些参数给我吗？" },

    { id: "terms", k: ["fob", "cif", "incoterm", "shipping", "packing", "trade terms", "贸易", "交货", "运输", "包装", "条款", "出口"],
      en: "Trade terms: FOB Dalian or FOB Shanghai, or CIF.\nEvery export order ships with English datasheets, GA drawings, performance curves, packing list and test reports.\nLead time depends on trim and motor; it is confirmed with the quotation.",
      zh: "贸易条款：FOB 大连／FOB 上海，或 CIF。\n每单出口随附：英文数据表、总图、性能曲线、装箱单、试验报告。\n交期取决于配型与电机，随报价一并确认。" },

    { id: "lead", k: ["lead time", "delivery time", "when can", "how long", "production time", "交期", "多久", "什么时候", "货期"],
      en: "Lead time is confirmed with the quotation — it depends on the hydraulic trim, motor and any third-party certification.\nStandard builds are quoted in weeks, not months; the exact window is stated in the offer.",
      zh: "交期随报价确认，取决于水力配型、电机和是否需要第三方认证。\n常规机型按周计，不是按月；具体周期在报价单里写明。" },

    { id: "cert", k: ["certificate", "certification", "ce", "iso", "atex", "explosion", "认证", "证书", "防爆", "iso9001"],
      en: "Units are built to Chinese reciprocating-pump standards. Certification for a specific target market (CE, ATEX and similar) is quoted item by item — we do not claim certificates we do not hold.\nTell me the destination market and I will confirm what can be supplied with the order.",
      zh: "整机按中国往复泵标准制造。针对目标市场的认证（CE、ATEX 等）按项目单独报价——没有的证书我们不会声称有。\n告诉我目的市场，我确认这单能随货提供哪些文件。" },

    { id: "docs", k: ["datasheet", "catalogue", "catalog", "curve", "drawing", "brochure", "pdf", "样本", "数据表", "曲线", "图纸", "资料", "手册"],
      en: "Available: series datasheets, performance curves, GA drawings, and the site test reports published on the References page (270 m and 51 m level dewatering, April 2024).\nLeave an email and I will send the set that matches your duty — specify pump type or application.",
      zh: "可提供：系列数据表、性能曲线、总图，以及业绩页公开的现场试验报告（270 m／51 m 中段排水，2024 年 4 月）。\n留个邮箱，我按你的工况发对应资料——说明泵型或应用即可。" },

    { id: "service", k: ["service", "after sales", "commissioning", "spare", "support", "售后", "服务", "调试", "备件供应"],
      en: "Serviced worldwide: commissioning support, on-site maintenance and spare kits are part of the offer.\nBecause the drive is mechanical, most maintenance is carried out on site instead of a factory return — that is the point of the architecture.",
      zh: "全球服务：调试支持、现场维护、备件包都在供货范围内。\n机械驱动的好处是大部分维护可在现场完成，不必整机返厂——这正是这套架构的意义。" },

    { id: "calc", k: ["calculator", "calculate", "sizing tool", "计算器", "选型计算", "算一下", "试算"],
      en: "The sizing calculator takes flow and pressure (or head) and returns shaft power and the likely series, with an energy comparison against a centrifugal unit.\nOpen Calculator in the top menu. If you would rather I run it, send flow, pressure, fluid and annual hours.",
      zh: "选型计算器输入流量和压力（或扬程），输出轴功率、建议系列，并给出与离心泵的能耗对比。\n顶部菜单「选型计算」即可。想让我算也行——给流量、压力、介质和年运行小时。" },

    { id: "agent", k: ["agent", "distributor", "dealer", "reseller", "代理", "经销", "合作"],
      en: "We work with regional partners on a project basis. Send your company profile, territory and the applications you cover, and the export desk will follow up with terms.",
      zh: "我们按项目与区域伙伴合作。发来公司简介、覆盖区域和主要应用，出口部会跟你谈具体条款。" },

    { id: "visit", k: ["visit", "factory", "sample", "tour", "参观", "工厂", "样品", "考察"],
      en: "Factory visits and witnessed tests can be arranged with the order schedule. Tell me the dates and which pump family you want to see, and I will coordinate.",
      zh: "可以安排工厂参观和见证试验，跟订单排产走。告诉我时间和想看哪个系列，我来协调。" },

    { id: "warranty", k: ["warranty", "guarantee", "质保", "保修", "保证期"],
      en: "Warranty terms are stated in the quotation for the specific build, together with the wear-part schedule. I do not want to quote a period here that the offer might contradict — the engineer will confirm it with the price.",
      zh: "质保条款随具体配置写在报价单里，同时给易损件更换周期。这里不先给一个可能与报价单不一致的数字——工程师会连同价格一起确认。" },

    { id: "contact", k: ["contact", "email", "phone", "whatsapp", "wechat", "call", "联系", "电话", "微信", "邮箱", "怎么联系"],
      en: "Email: " + EMAIL + "\nWeChat: the QR code on the Contact page (mostly for China-based contacts).\nNo WhatsApp line in this market — email reaches the export desk directly and is the fastest route for overseas enquiries.\nLocation: Dalian, Liaoning, China.",
      zh: "邮箱：" + EMAIL + "\n微信：联系页有二维码（主要面向国内联系人）。\n海外不用 WhatsApp——邮件直达出口部，是海外询盘最快的通道。\n地址：中国 · 辽宁 · 大连。" },

    { id: "who", k: ["who are you", "company", "about", "hongshi", "manufacturer", "factory or trader", "你们是谁", "公司", "介绍", "厂家", "贸易商"],
      en: "Dalian Hongshi Technology Co., Ltd. — high-pressure reciprocating pump and slurry pump systems for mining, power, oil & gas and process industries.\nWe supply complete machines and retrofit packages, with measured references in coal mine dewatering, oilfield injection, boiler feed and slurry transfer.",
      zh: "大连宏实科技有限公司——面向矿山、电力、油气与流程工业的高压往复泵与浆料泵系统。\n提供整机与改造方案，在煤矿排水、油田注水、锅炉给水、浆料输送都有实测业绩。" },

    { id: "solid", k: ["solids", "particle", "ph", "viscosity", "temperature", "含固率", "粒径", "酸碱", "ph值", "粘度", "温度", "介质"],
      en: "Fluid data decides the trim: solids concentration and size distribution, density, pH, temperature and whether the flow is continuous.\nV5 handles 30%+ solids by weight up to 150 m head; above that, or with large particles, we check erosion and valve selection before quoting.",
      zh: "介质决定配型：含固率与粒径分布、密度、pH、温度、是否连续运行。\nV5 可处理含固 ≥30%（重量）、扬程 ≤150 m；超出或粒径偏大时，要先核磨损与阀组选型再报价。" },

    { id: "energy", k: ["energy saving", "save", "kwh", "payback", "roi", "节电", "省电", "节能", "回收期", "投资回报"],
      en: "Energy is where the payback comes from. Published references: 19–21% on industrial boiler feed, 26.7% on a CDQ waste-heat boiler feed (3.2-year payback), and injection specific power down to 0.3 kWh/m³·MPa from 0.5–0.8.\nGive me flow, pressure, annual hours and your tariff and I will give you a first-pass saving.",
      zh: "回报主要来自电费。已公开业绩：工业锅炉给水节电 19–21%，干熄焦余热锅炉给水 26.7%（回收期 3.2 年），注水单耗从 0.5–0.8 降到 0.3 kWh/m³·MPa。\n给我流量、压力、年运行小时和电价，我先给你一版节电估算。" },

    { id: "lang", k: ["language", "english", "chinese", "语言", "英文", "中文"],
      en: "English and Chinese both work here. Drawings, datasheets and test reports are issued in English for export orders.",
      zh: "中英文都可以。出口订单的图纸、数据表、试验报告出英文版。" }
  ];

  /* ---------------------------------------------------------------- helpers */
  function norm(s) {
    return (s || "").toLowerCase().replace(/[，。？、；：！（）]/g, " ").replace(/\s+/g, " ").trim();
  }
  function match(text) {
    var q = norm(text), best = null, bestScore = 0;
    for (var i = 0; i < KB.length; i++) {
      var s = 0, k = KB[i].k;
      for (var j = 0; j < k.length; j++) {
        var kw = k[j].toLowerCase();
        if (q.indexOf(kw) !== -1) s += kw.length > 4 ? 2 : 1;
      }
      if (s > bestScore) { bestScore = s; best = KB[i]; }
    }
    return bestScore >= 1 ? best : null;
  }
  var HUMAN_RE = /human|engineer|sales|person|call me|contact me|工程师|人工|销售|联系我|转人工|真人/i;

  /* ---------------------------------------------------------------- DOM */
  var root = document.createElement("div");
  root.id = "hs-chat-root";
  document.body.appendChild(root);

  var btn = document.createElement("button");
  btn.className = "hs-chat-btn";
  btn.type = "button";
  btn.setAttribute("aria-label", T.btn);
  btn.innerHTML = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 11.5a8.4 8.4 0 0 1-9 8.4 9.6 9.6 0 0 1-3.4-.6L3 21l1.7-4.6A8.4 8.4 0 0 1 12 3.1a8.4 8.4 0 0 1 9 8.4Z"/></svg><span class="hs-btn-label">' + T.btn + '</span>';

  var panel = document.createElement("section");
  panel.className = "hs-chat-panel";
  panel.setAttribute("role", "dialog");
  panel.setAttribute("aria-label", T.title);
  panel.innerHTML =
    '<div class="hs-chat-head"><div><div class="hs-title">' + T.title + '</div><div class="hs-sub">' + T.sub + '</div></div><button class="hs-close" type="button" aria-label="Close">&times;</button></div>' +
    '<div class="hs-chat-body" id="hs-body"></div>' +
    '<div class="hs-chat-foot"><div class="hs-inputrow"><textarea id="hs-ta" rows="1" placeholder="' + T.ph + '"></textarea>' +
    '<button class="hs-send" id="hs-send" type="button" aria-label="Send"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M22 2 11 13"/><path d="M22 2 15 22l-4-9-9-4Z"/></svg></button></div>' +
    '<div class="hs-note">' + T.note + '</div></div>';

  root.appendChild(btn);
  root.appendChild(panel);

  var body = panel.querySelector("#hs-body");
  var ta = panel.querySelector("#hs-ta");
  var send = panel.querySelector("#hs-send");
  var history = [];
  var opened = false;

  function scroll() { body.scrollTop = body.scrollHeight; }

  function plain(s) {
    return String(s).replace(/\*\*(.+?)\*\*/g, "$1").replace(/^#{1,6}\s*/gm, "").replace(/`/g, "");
  }
  function add(who, text) {
    var row = document.createElement("div");
    row.className = "hs-msg " + who;
    var b = document.createElement("div");
    b.className = "hs-bubble";
    b.textContent = who === "bot" ? plain(text) : text;
    row.appendChild(b);
    body.appendChild(row);
    if (who !== "sys") history.push({ role: who === "me" ? "user" : "assistant", content: text });
    scroll();
    return row;
  }

  function chips(list) {
    var wrap = document.createElement("div");
    wrap.className = "hs-chips";
    list.forEach(function (label) {
      var c = document.createElement("button");
      c.className = "hs-chip";
      c.type = "button";
      c.textContent = label;
      c.addEventListener("click", function () {
        wrap.remove();
        ask(label);
      });
      wrap.appendChild(c);
    });
    body.appendChild(wrap);
    scroll();
  }

  function typing(on) {
    var el = document.getElementById("hs-typing");
    if (on) {
      if (el) return;
      var row = document.createElement("div");
      row.className = "hs-msg bot";
      row.id = "hs-typing";
      row.innerHTML = '<div class="hs-bubble"><span class="hs-typing"><i></i><i></i><i></i></span></div>';
      body.appendChild(row);
      scroll();
    } else if (el) { el.remove(); }
  }

  function escalate(prefix) {
    var box = document.createElement("div");
    box.className = "hs-escalate";
    box.innerHTML = '<p>' + T.escTitle + '</p>' +
      '<input id="hs-name" placeholder="' + T.escName + '" autocomplete="name">' +
      '<input id="hs-mail" type="email" placeholder="' + T.escMail + '" autocomplete="email">' +
      '<button type="button">' + T.escBtn + '</button>' +
      '<div class="hs-alt">' + T.escAlt + '<a href="mailto:' + EMAIL + '">' + EMAIL + '</a></div>';
    body.appendChild(box);
    scroll();
    var nameEl = box.querySelector("#hs-name");
    var mailEl = box.querySelector("#hs-mail");
    box.querySelector("button").addEventListener("click", function () {
      var mail = (mailEl.value || "").trim();
      if (!/^[^@\s]+@[^@\s]+\.[^@\s]+$/.test(mail)) { mailEl.focus(); return; }
      var payload = {
        _subject: "Website enquiry" + (prefix ? " — " + prefix : ""),
        _template: "table",
        name: (nameEl.value || "").trim() || "(not given)",
        email: mail,
        page: location.href,
        language: ZH ? "zh" : "en",
        question: prefix || "",
        transcript: history.map(function (h) { return (h.role === "user" ? "> " : "") + h.content; }).join("\n\n").slice(0, 6000)
      };
      this.disabled = true;
      var self = this;
      fetch("https://formsubmit.co/ajax/" + EMAIL, {
        method: "POST",
        headers: { "Content-Type": "application/json", Accept: "application/json" },
        body: JSON.stringify(payload)
      }).then(function (r) { return r.json(); }).then(function (j) {
        box.remove();
        add("bot", T.escOk);
      }).catch(function () {
        self.disabled = false;
        add("bot", T.escFail + EMAIL);
      });
    });
  }

  function answerFor(text) {
    if (HUMAN_RE.test(text)) { add("bot", ZH ? "好的，请留下邮箱，工程师直接回复你。" : "Sure — leave an email and an engineer will reply directly."); escalate(text); return true; }
    var hit = match(text);
    if (hit) { add("bot", ZH ? hit.zh : hit.en); return true; }
    return false;
  }

  var endpoint = null;
  var BASE = location.pathname.indexOf("/zh/") !== -1 ? "../" : "";
  function loadConfig() {
    fetch(BASE + "assets/data/chat-config.json", { cache: "no-store" })
      .then(function (r) { return r.ok ? r.json() : null; })
      .then(function (c) { if (c && c.endpoint) endpoint = c.endpoint; })
      .catch(function () {});
  }

  function ask(text) {
    text = (text || "").trim();
    if (!text) return;
    add("me", text);
    if (answerFor(text)) return;
    if (endpoint) {
      typing(true);
      fetch(endpoint.replace(/\/$/, "") + "/chat", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ message: text, lang: ZH ? "zh" : "en", history: history.slice(-8) })
      }).then(function (r) { return r.ok ? r.json() : Promise.reject(); })
        .then(function (j) {
          typing(false);
          if (j && j.reply) {
            add("bot", j.reply);
            if (j.escalate) escalate(text);
          } else { throw new Error("empty"); }
        })
        .catch(function () {
          typing(false);
          add("bot", T.errNet);
          add("bot", ZH ? "这条我先转给工程师。" : "I will pass this one to an engineer.");
          escalate(text);
        });
      return;
    }
    add("bot", ZH
      ? "这个问题我这边拿不准，转给工程师更靠谱。留个邮箱，1 个工作日内回复；急的话直接发邮件。"
      : "That one is outside what I can answer reliably — better to pass it to an engineer. Leave an email and you will get a reply within one working day.");
    escalate(text);
  }

  function openPanel() {
    panel.classList.add("open");
    btn.style.display = "none";
    if (!opened) {
      opened = true;
      add("bot", T.greet);
      chips(T.chips);
      loadConfig();
    }
    ta.focus();
  }
  function closePanel() {
    panel.classList.remove("open");
    btn.style.display = "";
  }

  btn.addEventListener("click", openPanel);
  panel.querySelector(".hs-close").addEventListener("click", closePanel);

  send.addEventListener("click", function () {
    var v = ta.value;
    ta.value = "";
    ta.style.height = "";
    ask(v);
  });
  ta.addEventListener("keydown", function (e) {
    if (e.key === "Enter" && !e.shiftKey) { e.preventDefault(); send.click(); }
  });
  ta.addEventListener("input", function () {
    ta.style.height = "auto";
    ta.style.height = Math.min(ta.scrollHeight, 96) + "px";
  });

  document.addEventListener("keydown", function (e) {
    if (e.key === "Escape" && panel.classList.contains("open")) closePanel();
  });
})();
