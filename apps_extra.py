# -*- coding: utf-8 -*-
"""Additional application pages (boiler feed, high-head drainage / mountain
irrigation, seawater desalination booster, high-pressure descaling & cleaning).

Shared by build.py (English) and zh_pages.py (Chinese) so both editions stay
structurally identical. Content is written as small block lists and rendered by
render_body(); no fact here goes beyond the published product range.
"""

APPS = [
    {
        "slug": "boiler-feed.html",
        "en": {
            "title": "Boiler feed pumps — high-pressure multi-plunger units | DALIAN HONGSHI TECHNOLOGY",
            "desc": "High-pressure multi-plunger pumps for industrial and waste-heat boiler feed: 100–400 m3/h at 4–16 MPa, efficiency above 90%, replacement of multistage centrifugal feed pumps.",
            "crumb": "Boiler Feed Water",
            "eyebrow": "Application · power & process",
            "h1": "Boiler feed pumps for industrial and waste-heat boilers",
            "lead": "Steady flow, high pressure, and 8,000 hours a year. Feed duty is where a few points of efficiency turn into money.",
            "blocks": [
                ("h2", "The duty"),
                ("p", "A feed pump works against drum pressure plus feedwater line losses — typically 4–16 MPa for industrial boilers and waste-heat units — while the steam load moves above it. The pump itself runs almost continuously."),
                ("p", "That is why efficiency, not first cost, sets the operating bill: a unit that loses five points of efficiency costs more in a year than a large part of its purchase price."),
                ("h2", "Why positive displacement"),
                ("ul", [
                    "Volumetric efficiency stays above 90% as clearances open with age — the machine still delivers its rated flow years later.",
                    "Flow is set by speed, not by the system curve, so drum level control stays stable when load drops.",
                    "Low NPSH requirement, which matters with hot deaerated water.",
                    "VFD speed control for wide turn-down without recirculation losses.",
                ]),
                ("callout", "<strong>Reference:</strong> 120 t/h and 130/160 t/h boiler feed replacements in industrial plants, measured at 21% and 19% energy saving. A coke dry quenching waste-heat boiler feed replacement measured 26.7% saving with a 3.2-year payback."),
                ("h2", "Selection range"),
                ("p", "UDZ 100/16 and UDZ 160/16 cover most industrial boiler duties: 100–400 m³/h at 4–16 MPa. Where drum pressure or feed line length pushes beyond that, we extend the same family rather than change architecture."),
            ],
            "table": (
                ["Duty", "Typical value"],
                [
                    ["Flow per pump", "100–400 m³/h"],
                    ["Discharge pressure", "4–16 MPa"],
                    ["Feedwater temperature", "up to 120 °C"],
                    ["Efficiency", "&gt;90%"],
                    ["Wear parts", "5,000 h+"],
                    ["Range", "UDZ 100/16 – UDZ 160/16"],
                ],
            ),
            "needs": [
                "Boiler rating (t/h) and design pressure",
                "Feedwater temperature and deaerator height",
                "Annual operating hours",
                "Existing pump model and a measured power reading",
                "Supply voltage and frequency",
            ],
            "cta": ("Replacing a feed pump set?", "Send the boiler rating, feedwater temperature and one power reading — that is enough to size the replacement and estimate the saving.", "Send details"),
        },
        "zh": {
            "title": "锅炉给水泵 — 高压多柱塞给水泵｜大连宏实科技有限公司",
            "desc": "工业锅炉与余热锅炉给水用高压多柱塞泵：100–400 m³/h、4–16 MPa，效率 90% 以上，可替换多级离心给水泵。",
            "crumb": "锅炉给水",
            "eyebrow": "应用领域 · 电力与流程工业",
            "h1": "工业锅炉与余热锅炉给水泵",
            "lead": "流量稳定、压力高、一年运行 8000 小时。给水工况上，几个点的效率差就是真金白银。",
            "blocks": [
                ("h2", "工况特点"),
                ("p", "给水泵要克服汽包压力与给水管路阻力，工业锅炉与余热锅炉通常在 4–16 MPa，而蒸汽负荷在其上方波动；泵本身几乎是连续运行的。"),
                ("p", "所以决定运行成本的不是采购价，而是效率：效率低 5 个点的机组，一年多吃掉的电费就超过采购价的一大块。"),
                ("h2", "为什么选容积式"),
                ("ul", [
                    "容积效率随磨损间隙扩大仍能保持在 90% 以上，运行多年后铭牌流量照样给得出。",
                    "流量由转速决定，不随系统曲线漂移，低负荷时汽包水位控制更稳。",
                    "必需汽蚀余量（NPSHr）低，适合高温除氧水。",
                    "变频调速，宽范围调节且无再循环损失。",
                ]),
                ("callout", "<strong>业绩：</strong>工业锅炉 120 t/h 与 130/160 t/h 给水泵替换，实测节电 21% 与 19%；干熄焦余热锅炉给水泵替换实测节电 26.7%，回收期 3.2 年。"),
                ("h2", "选型范围"),
                ("p", "UDZ 100/16 与 UDZ 160/16 覆盖多数工业锅炉给水工况：100–400 m³/h、4–16 MPa。若汽包压力更高或给水管线更长，我们在同一系列内向上扩展，而不是换架构。"),
            ],
            "table": (
                ["工况参数", "典型值"],
                [
                    ["单泵流量", "100–400 m³/h"],
                    ["排出压力", "4–16 MPa"],
                    ["给水温度", "≤120 ℃"],
                    ["效率", "&gt;90%"],
                    ["易损件寿命", "5,000 h+"],
                    ["适用系列", "UDZ 100/16 – UDZ 160/16"],
                ],
            ),
            "needs": [
                "锅炉蒸发量（t/h）与设计压力",
                "给水温度与除氧器标高",
                "年运行小时数",
                "原泵型号与一次实测功率",
                "供电电压与频率",
            ],
            "cta": ("正在替换给水泵组？", "把锅炉蒸发量、给水温度和一次功率读数发给我们，就够做选型与节电估算。", "发送工况"),
        },
    },
    {
        "slug": "high-head-drainage.html",
        "en": {
            "title": "High-head drainage & mountain irrigation pumps | DALIAN HONGSHI TECHNOLOGY",
            "desc": "Multi-plunger pumps for high-lift water transfer: mountain irrigation, plateau supply and high-head drainage, 50–500 m3/h at 300–2,500 m head, single unit or series staged.",
            "crumb": "High-Head Drainage",
            "eyebrow": "Application · water transfer",
            "h1": "High-head drainage and mountain irrigation pumps",
            "lead": "Lifting water several hundred metres — mountain irrigation, plateau supply, high-lift drainage. The static head does the work; the pump has to do it efficiently.",
            "blocks": [
                ("h2", "The duty"),
                ("p", "Mountain irrigation and plateau water supply need lifts of 300–2,500 m, often over long pipelines, with reservoir levels that move through the season. Past a certain lift a single centrifugal stage cannot reach, and multistage units stack losses stage after stage."),
                ("p", "Because static head dominates, every point of pump efficiency is multiplied across the whole lift — and the pipeline has to be protected against surge when the pump stops."),
                ("h2", "How we specify it"),
                ("ul", [
                    "Series staging: two or more plunger pumps in series where the lift exceeds one unit's pressure rating.",
                    "Check valves and surge protection sized together with the pipeline, not added afterwards.",
                    "Efficiency held at part load, since irrigation demand varies through the season.",
                    "Hardened plungers and valve seats for water carrying sand or silt.",
                ]),
                ("h2", "Selection range"),
                ("p", "UDQ 60 through UDZ 600, single unit or series staged: 50–500 m³/h at 300–2,500 m of head, discharge up to 25 MPa. The number of stages is set by the lift, not by a catalogue page."),
            ],
            "table": (
                ["Duty", "Typical value"],
                [
                    ["Flow per pump", "50–500 m³/h"],
                    ["Total head", "300–2,500 m"],
                    ["Discharge pressure", "3–25 MPa"],
                    ["Configuration", "single unit or series staged"],
                    ["Solids", "low, some silt"],
                    ["Range", "UDQ 60 – UDZ 600"],
                ],
            ),
            "needs": [
                "Total lift and pipeline length / diameter",
                "Peak and average flow required",
                "Water source and solids content",
                "Seasonal operating hours",
                "Supply voltage and frequency",
            ],
            "cta": ("Planning a high-lift transfer?", "Send the lift, pipeline and flow — we will come back with the number of stages and the power draw.", "Send details"),
        },
        "zh": {
            "title": "高扬程排水与高山提灌泵｜大连宏实科技有限公司",
            "desc": "高扬程输水用多柱塞泵：高山提灌、高原供水与高扬程排水，50–500 m³/h、扬程 300–2500 m，可单机或串联分级。",
            "crumb": "高扬程排水（高山提灌）",
            "eyebrow": "应用领域 · 输水",
            "h1": "高扬程排水与高山提灌泵",
            "lead": "把水提升几百米——高山提灌、高原供水、高扬程排水。静扬程是硬指标，泵要做的是高效地完成它。",
            "blocks": [
                ("h2", "工况特点"),
                ("p", "高山提灌与高原供水需要 300–2500 m 的扬程，往往管线很长，且水库水位随季节变化。超过一定扬程，单级离心泵够不到；多级离心泵则一级一级把损失叠上去。"),
                ("p", "由于静扬程占主导，泵效率每高一个点，都会被整个扬程放大；同时管路必须做好停泵水锤防护。"),
                ("h2", "我们怎么选型"),
                ("ul", [
                    "串联分级：扬程超过单机压力等级时，两台或多台柱塞泵串联。",
                    "止回阀与水锤防护按管线参数一并设计，而不是事后补装。",
                    "部分负荷下仍保持效率，因为灌溉需求随季节变化。",
                    "含砂含泥水体配硬化柱塞与阀座。",
                ]),
                ("h2", "选型范围"),
                ("p", "UDQ 60 至 UDZ 600，单机或串联：50–500 m³/h、扬程 300–2500 m、排出压力至 25 MPa。级数由扬程决定，不由样本页决定。"),
            ],
            "table": (
                ["工况参数", "典型值"],
                [
                    ["单泵流量", "50–500 m³/h"],
                    ["总扬程", "300–2,500 m"],
                    ["排出压力", "3–25 MPa"],
                    ["配置", "单机或串联分级"],
                    ["含固", "低，少量泥沙"],
                    ["适用系列", "UDQ 60 – UDZ 600"],
                ],
            ),
            "needs": [
                "总扬程与管线长度／管径",
                "峰值流量与平均流量",
                "水源情况与含固量",
                "季节性运行小时数",
                "供电电压与频率",
            ],
            "cta": ("正在规划高扬程输水？", "把扬程、管线与流量发过来，我们给出级数配置与功率需求。", "发送工况"),
        },
    },
    {
        "slug": "seawater-desalination.html",
        "en": {
            "title": "Seawater desalination booster pumps — RO feed duty | DALIAN HONGSHI TECHNOLOGY",
            "desc": "High-pressure multi-plunger pumps for seawater RO feed and interstage boosting: 50–500 m3/h at 5–7 MPa, duplex and super duplex wetted parts, efficiency above 90%.",
            "crumb": "Seawater Desalination",
            "eyebrow": "Application · desalination",
            "h1": "Seawater desalination booster pumps",
            "lead": "RO feed and interstage booster duty at 5–7 MPa. Here the design driver is not efficiency alone — it is corrosion.",
            "blocks": [
                ("h2", "The duty"),
                ("p", "A seawater RO train needs a high-pressure feed pump at 5.0–7.0 MPa, held steady as membrane resistance rises with fouling and temperature moves through the year. Interstage boosters add 2–4 MPa between arrays."),
                ("p", "Seawater is the hard part. Chlorides attack anything that is not duplex, super duplex or a suitable high alloy — a pump that is efficient but corrodes is a maintenance contract, not an asset."),
                ("h2", "How we specify it"),
                ("ul", [
                    "Duplex / super duplex wetted parts (UNS S31803 / S32750) for seawater service.",
                    "Ceramic or coated plungers with flushed packing or mechanical seals.",
                    "Flow held constant as membrane resistance rises, trimmed by VFD.",
                    "Sized for net feed flow, so the energy recovery device works with the pump rather than against it.",
                ]),
                ("h2", "Selection range"),
                ("p", "UDZ 160/16 and UDZ 320/16 at reduced stroke cover 50–500 m³/h per train at 5–7 MPa. Brackish-water duties sit lower, at 2–4 MPa, and use the same family."),
            ],
            "table": (
                ["Duty", "Typical value"],
                [
                    ["Flow per train", "50–500 m³/h"],
                    ["Discharge pressure", "5.0–7.0 MPa (SWRO)"],
                    ["Interstage boost", "2–4 MPa"],
                    ["Wetted material", "duplex / super duplex"],
                    ["Efficiency", "&gt;90%"],
                    ["Range", "UDZ 160/16 – UDZ 320/16"],
                ],
            ),
            "needs": [
                "Permeate capacity and recovery ratio",
                "Feed salinity and temperature range",
                "Train arrangement (single pass / two pass)",
                "Energy recovery device type",
                "Materials specification and applicable standard",
            ],
            "cta": ("Sizing a desalination train?", "Send permeate capacity, recovery and feed salinity — we will size the feed and booster duties.", "Send details"),
        },
        "zh": {
            "title": "海水淡化增压泵 — 反渗透给水工况｜大连宏实科技有限公司",
            "desc": "海水反渗透给水与级间增压用高压多柱塞泵：50–500 m³/h、5–7 MPa，双相钢／超级双相钢过流部件，效率 90% 以上。",
            "crumb": "海水淡化增压",
            "eyebrow": "应用领域 · 海水淡化",
            "h1": "海水淡化增压泵",
            "lead": "反渗透给水与级间增压，压力 5–7 MPa。这里决定成败的不只是效率，还有腐蚀。",
            "blocks": [
                ("h2", "工况特点"),
                ("p", "海水反渗透装置需要 5.0–7.0 MPa 的高压给水泵，并且要在膜阻力随污堵上升、水温随季节变化时保持压力稳定；级间增压段再补 2–4 MPa。"),
                ("p", "难点在海水本身：氯离子会攻击除双相钢、超级双相钢或相应高合金之外的一切材料。效率高但会腐蚀的泵，不是资产，是一张长期维修单。"),
                ("h2", "我们怎么选型"),
                ("ul", [
                    "海水工况过流部件采用双相钢／超级双相钢（UNS S31803 / S32750）。",
                    "陶瓷或涂层柱塞，配冲洗填料或机械密封。",
                    "膜阻力上升时靠变频微调保持流量恒定。",
                    "按净给水量选型，使能量回收装置与泵协同而不是相互抵消。",
                ]),
                ("h2", "选型范围"),
                ("p", "UDZ 160/16 与 UDZ 320/16 降行程运行，覆盖单套装置 50–500 m³/h、5–7 MPa；苦咸水工况压力更低（2–4 MPa），仍用同一系列。"),
            ],
            "table": (
                ["工况参数", "典型值"],
                [
                    ["单套流量", "50–500 m³/h"],
                    ["排出压力", "5.0–7.0 MPa（海水 RO）"],
                    ["级间增压", "2–4 MPa"],
                    ["过流材质", "双相钢／超级双相钢"],
                    ["效率", "&gt;90%"],
                    ["适用系列", "UDZ 160/16 – UDZ 320/16"],
                ],
            ),
            "needs": [
                "产水量与回收率",
                "进水含盐量与温度范围",
                "装置流程（一段／两段）",
                "能量回收装置形式",
                "材质要求与执行标准",
            ],
            "cta": ("正在做海水淡化装置选型？", "把产水量、回收率与进水含盐量发过来，我们给出给水与增压段的配置。", "发送工况"),
        },
    },
    {
        "slug": "high-pressure-descaling.html",
        "en": {
            "title": "High-pressure descaling & cleaning pumps | DALIAN HONGSHI TECHNOLOGY",
            "desc": "Multi-plunger pumps for steel mill descaling headers and high-pressure cleaning: 20–200 m3/h at 10–40 MPa, to 70 MPa on request, flat pressure during the pass.",
            "crumb": "Descaling & Cleaning",
            "eyebrow": "Application · steel & cleaning",
            "h1": "High-pressure descaling and cleaning pumps",
            "lead": "20–30 MPa at the descaling header, or 10–40 MPa at the cleaning nozzle. Both punish anything that cannot hold pressure without leaking.",
            "blocks": [
                ("h2", "The duty"),
                ("p", "In hot rolling, the descaling header needs a pressure that stays flat through the pass and recovers at once when the valve opens. Industrial cleaning and water jetting need the same, with a flow that follows the number of nozzles in use."),
                ("p", "A centrifugal unit sheds pressure the moment flow jumps at valve opening. On a descaling header that shows up as incomplete scale removal and a patchy strip surface — a quality problem before it is an energy problem."),
                ("h2", "How we specify it"),
                ("ul", [
                    "Discharge pressure held within a few percent from no-flow to full nozzle flow.",
                    "Fast-acting unloader and accumulator sized with the header, not bolted on.",
                    "Hardened plungers and valve seats for water carrying mill scale.",
                    "Skid-mounted with filtration, relief valve and local controls.",
                ]),
                ("h2", "Selection range"),
                ("p", "UDZ 100/16 to UDZ 320/16 with high-pressure trim cover 20–200 m³/h at 10–40 MPa; special trims to 70 MPa on request. The skid is built around the duty cycle, because a descaling pump spends its life starting and stopping."),
            ],
            "table": (
                ["Duty", "Typical value"],
                [
                    ["Flow", "20–200 m³/h"],
                    ["Pressure", "10–40 MPa (to 70 MPa on request)"],
                    ["Response", "fast-acting unloader"],
                    ["Filtration", "100 µm or better"],
                    ["Efficiency", "&gt;90%"],
                    ["Range", "UDZ 100/16 – UDZ 320/16"],
                ],
            ),
            "needs": [
                "Header pressure and total nozzle flow",
                "Valve open / close cycle",
                "Water quality and available filtration",
                "Duty cycle, hours per day",
                "Existing pump and motor rating",
            ],
            "cta": ("Retrofitting a descaling or cleaning skid?", "Send header pressure, nozzle flow and the valve cycle — we will size the pump and the accumulator.", "Send details"),
        },
        "zh": {
            "title": "高压水除磷与清洗泵｜大连宏实科技有限公司",
            "desc": "钢厂除鳞集管与高压清洗用多柱塞泵：20–200 m³/h、10–40 MPa，特殊配置可至 70 MPa，过钢全程压力平稳。",
            "crumb": "高压水除磷、清洗",
            "eyebrow": "应用领域 · 冶金与清洗",
            "h1": "高压水除磷与清洗泵",
            "lead": "除鳞集管上 20–30 MPa，清洗喷嘴前 10–40 MPa。两者都容不下“压力保不住、还老漏”的设备。",
            "blocks": [
                ("h2", "工况特点"),
                ("p", "热轧除鳞要求集管压力在整道次内保持平稳，阀门一开立刻恢复；工业清洗与水射流同理，只是流量要随投入的喷嘴数量变化。"),
                ("p", "离心泵在阀门开启、流量突增的瞬间就掉压。在除鳞集管上，这表现为除鳞不净、板面花斑——先是质量问题，然后才是能耗问题。"),
                ("h2", "我们怎么选型"),
                ("ul", [
                    "从零流量到全喷嘴流量，排出压力波动控制在几个百分点内。",
                    "快开卸荷阀与蓄能器按集管参数配套设计，而不是事后加装。",
                    "含氧化铁皮水体配硬化柱塞与阀座。",
                    "撬装成套：过滤、安全阀与就地控制。",
                ]),
                ("h2", "选型范围"),
                ("p", "UDZ 100/16 至 UDZ 320/16 高压配置，覆盖 20–200 m³/h、10–40 MPa；特殊配置可至 70 MPa。撬块按工况循环设计——除鳞泵的一生就是不断启停。"),
            ],
            "table": (
                ["工况参数", "典型值"],
                [
                    ["流量", "20–200 m³/h"],
                    ["压力", "10–40 MPa（特殊配置至 70 MPa）"],
                    ["响应", "快开卸荷阀"],
                    ["过滤精度", "100 µm 或更细"],
                    ["效率", "&gt;90%"],
                    ["适用系列", "UDZ 100/16 – UDZ 320/16"],
                ],
            ),
            "needs": [
                "集管压力与喷嘴总流量",
                "阀门开闭周期",
                "水质与现有过滤条件",
                "每天运行小时数／占空比",
                "原泵与电机参数",
            ],
            "cta": ("正在改造除磷或清洗撬块？", "把集管压力、喷嘴流量与阀门周期发过来，我们给出泵与蓄能器配置。", "发送工况"),
        },
    },
]


def _blocks_html(blocks):
    out = []
    for kind, val in blocks:
        if kind == "h2":
            out.append(f"      <h2>{val}</h2>")
        elif kind == "p":
            out.append(f"      <p>{val}</p>")
        elif kind == "ul":
            items = "".join(f"\n        <li>{i}</li>" for i in val)
            out.append(f"      <ul>{items}\n      </ul>")
        elif kind == "callout":
            out.append(f'      <div class="callout"><p>{val}</p></div>')
    return "\n".join(out)


def render_body(app, lang, crumbs_html, contact_href="contact.html"):
    d = app[lang]
    head_txt, rows = d["table"]
    thead = f'<thead><tr><th>{head_txt[0]}</th><th>{head_txt[1]}</th></tr></thead>'
    tbody = "".join(
        f'\n            <tr><td>{r[0]}</td><td class="num">{r[1]}</td></tr>' for r in rows
    )
    needs = "".join(f"\n          <li>{n}</li>" for n in d["needs"])
    ch2, cp, cbtn = d["cta"]
    return f"""
{crumbs_html}
<section class="page-head">
  <div class="wrap">
    <p class="eyebrow">{d['eyebrow']}</p>
    <h1>{d['h1']}</h1>
    <p class="lead">{d['lead']}</p>
  </div>
</section>

<section>
  <div class="wrap grid-2" style="gap:56px;align-items:start">
    <div class="prose">
{_blocks_html(d['blocks'])}
    </div>
    <div>
      <div class="table-wrap">
        <table>
          {thead}
          <tbody>{tbody}
          </tbody>
        </table>
      </div>
      <div class="card" style="margin-top:24px">
        <h3>{'What we need to quote' if lang == 'en' else '报价需要的信息'}</h3>
        <ul class="checks">{needs}
        </ul>
      </div>
    </div>
  </div>
</section>

<section class="tight"><div class="wrap"><div class="band"><div><h2>{ch2}</h2><p>{cp}</p></div><a class="btn light" href="{contact_href}">{cbtn}</a></div></div></section>
"""
