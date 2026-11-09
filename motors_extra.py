#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Motor product line for the Hongshi site (added 2026-11-09).

Two families on one page:
  1. High-efficiency asynchronous motors — YE5 (IE5), YE4 (IE4), YE3 (IE3),
     YBX5 (Ex d, IE5) low voltage, plus YKK high voltage 6/10 kV.
  2. Permanent-magnet synchronous motors — TYCP / TYCP2.

The series listing follows the Wannan Electric (皖南电机) catalogue, which is the
mainstream Chinese type spectrum for these frame sizes, so model numbers and
mounting dimensions interchange with what most Chinese pump drawings already use.

Every number below is a supply-envelope range taken from the published series
data, not a model commitment; the exact model is fixed against the duty point at
quotation time (same policy as the pump pages).
"""

MOTORS_EN = """
{crumbs}
<section class="page-head">
  <div class="wrap">
    <p class="eyebrow">Motors · IE3 to IE5 · 0.12–2,500 kW</p>
    <h1>The motor is where the electricity is actually spent</h1>
    <p class="lead">High-efficiency asynchronous motors from 0.12 to 375 kW at 380 V and 160 to 2,500 kW at 6/10 kV, plus permanent-magnet synchronous motors to 450 kW. One efficiency step is 15–20% of the motor losses; two steps pay for themselves long before the pump does.</p>
  </div>
</section>

<section>
  <div class="wrap grid-2" style="gap:56px;align-items:start">
    <div class="prose">
      <h2>A pump is a motor with a wet end</h2>
      <p>On a 24/7 duty the motor runs more hours than anything else on the skid, and it runs them at whatever efficiency class it was bought at. A pump selected for 85% hydraulic efficiency is bolted to a motor that may be 89% efficient — the train number is the product, not the pump number alone.</p>
      <p>This is why we now quote the drive end with the pump end: motor, coupling, baseplate and, where the duty varies, the variable-frequency drive. One train, one set of drawings, one warranty.</p>
      <div class="callout">
        <p><strong>Every efficiency step removes about a fifth of the losses.</strong> IE3 → IE4 is roughly 15–20% of motor losses; IE4 → IE5 is another 20%. On continuous duty that is the cheapest kilowatt-hour you will ever buy — no civil works, no pipework, no shutdown beyond the swap.</p>
      </div>
      <h3>Frames and mounting stay the same</h3>
      <p>The low-voltage series below follow IEC 60034 dimensions: the same frame number means the same shaft height, foot holes and flange pattern as the motor you are replacing. A YE3 or YX3 unit comes out, a YE5 goes in on the same baseplate, with the same coupling alignment.</p>
    </div>
    <div>
      <div class="card">
        <h3>At a glance</h3>
        <ul class="checks">
          <li>Low voltage asynchronous: 0.12–375 kW, frame 63–355, 2–10 poles</li>
          <li>IE5 (GB 18613-2020 Grade 1) available from 0.75 kW</li>
          <li>High voltage YKK: 160–2,500 kW, 6/10 kV, frame 355–630</li>
          <li>Permanent-magnet synchronous: 0.55–450 kW, frame 80–355</li>
          <li>Explosion-proof YBX5: 0.18–375 kW, IE5, Ex d</li>
          <li>IP55 / F class as standard; IP54, IP65, H class on request</li>
        </ul>
      </div>
      <div class="card" style="margin-top:20px;background:#0c1a26;border-color:#0c1a26;color:#fff">
        <p class="tag" style="color:#ffb08a">Type spectrum</p>
        <h3 style="color:#fff">Series designations interchange</h3>
        <p style="color:#c6d6df">The listing follows the Wannan Electric (皖南电机) catalogue — the mainstream Chinese type spectrum for these frames. If your drawing or spare-parts list already says YE3-280M-4 or TYCP-315, you can read the equivalent straight off the tables below.</p>
        <div class="kv" style="border-color:rgba(255,255,255,.14)"><span>Mounting</span><b>IEC 60034 / DIN 42673</b></div>
        <div class="kv" style="border-color:rgba(255,255,255,.14)"><span>Efficiency standard</span><b>GB 18613-2020 / IEC 60034-30-1</b></div>
        <div class="kv" style="border:0"><span>PM standard</span><b>GB 30253-2013</b></div>
      </div>
    </div>
  </div>
</section>

<section class="alt">
  <div class="wrap">
    <div class="sec-head">
      <p class="eyebrow">Family 1</p>
      <h2>High-efficiency asynchronous motors</h2>
      <p class="lead">Squirrel-cage, totally enclosed fan cooled, cast-iron frame. The default drive for pumps, fans, compressors, conveyors and crushers — and the only family that can be dropped straight onto an existing baseplate without changing the drive.</p>
    </div>
    <div class="table-wrap">
      <table>
        <thead><tr><th>Series</th><th>Efficiency class</th><th>Power</th><th>Frame</th><th>Poles</th><th>Where it is used</th></tr></thead>
        <tbody>
          <tr><td><strong>YE5</strong></td><td>GB 18613-2020 Grade 1 (IE5)</td><td>0.75–375 kW</td><td>80–355</td><td>2, 4, 6, 8</td><td>Continuous duty where the kWh bill dominates — boiler feed, mine dewatering, aeration, pipeline transfer</td></tr>
          <tr><td><strong>YE4</strong></td><td>GB 18613-2020 Grade 2 (IE4)</td><td>0.37–375 kW</td><td>63–355</td><td>2, 4, 6, 8</td><td>The practical default when lead time or price rules out IE5</td></tr>
          <tr><td><strong>YE3</strong></td><td>GB 18613-2020 Grade 3 (IE3)</td><td>0.12–375 kW</td><td>63–355</td><td>2, 4, 6, 8, 10</td><td>General purpose and like-for-like replacement of the installed fleet</td></tr>
          <tr><td><strong>YBX5</strong></td><td>GB 18613-2020 Grade 1 (IE5), Ex d</td><td>0.18–375 kW</td><td>80–355</td><td>2, 4, 6, 8</td><td>Flammable-gas areas — gas boosting, refinery, paint and solvent plants</td></tr>
          <tr><td><strong>YKK</strong></td><td>High efficiency, 6/10 kV</td><td>160–2,500 kW</td><td>355–630</td><td>2–12</td><td>Large pump and fan drives where 380 V cable and switchgear stop making sense</td></tr>
        </tbody>
      </table>
    </div>
    <p class="small" style="margin-top:18px">Standard: 380 V / 50 Hz (other voltages and 60 Hz to order) · S1 duty · IP55 · F class · IC411 · B3 / B5 / B35 / V1 mounting. Derivatives available on the same platform: VFD-duty (YVF2 / YXVF), electromagnetic brake, multi-speed, low-vibration, marine, roller-table and stainless-steel shell.</p>

    <figure style="margin:34px 0 0">
      <img src="assets/img/motors-induction.svg" alt="Totally enclosed fan-cooled induction motor, frame 63 to 355" loading="lazy" style="width:100%;max-width:780px;display:block;margin:0 auto;border:1px solid #e2eaef;border-radius:14px;background:#fff">
    </figure>

    <div class="grid-2" style="margin-top:40px;gap:26px">
      <div class="card">
        <p class="tag">Efficiency, in plain numbers</p>
        <h3>What Grade 1 actually means</h3>
        <p>At 110 kW, 4-pole, the difference between IE3 and IE5 is about 1.1 percentage points of efficiency. That sounds small until it is multiplied by 8,000 hours a year: roughly 1.3 kW of continuous loss removed, about 10,400 kWh a year, about US$1,040 a year at US$0.10/kWh — per motor.</p>
        <p class="small">Indicative efficiencies; the exact value for a given model and voltage is taken from its type-test data and issued with the datasheet.</p>
      </div>
      <div class="card">
        <p class="tag">High voltage</p>
        <h3>YKK: when 380 V stops being sensible</h3>
        <p>Above roughly 300 kW the cable and switchgear for a 380 V motor become the expensive part of the installation. The YKK series runs at 6 kV or 10 kV, in a welded steel frame with a top-mounted air-to-air cooler and VPI insulation — 160–2,500 kW, 2 to 12 poles, IP44/IP54/IP55, F or H class, IMB3 or IMB35.</p>
        <ul class="checks">
          <li>Boiler feed and mine dewatering pump drives</li>
          <li>ID/FD and primary air fans</li>
          <li>Compressors, crushers, conveyors</li>
        </ul>
      </div>
    </div>
  </div>
</section>

<section>
  <div class="wrap">
    <div class="sec-head">
      <p class="eyebrow">Family 2</p>
      <h2>Permanent-magnet synchronous motors</h2>
      <p class="lead">A rotor with permanent magnets instead of an induced cage. Higher efficiency and higher power density in the same frame — and a much wider efficient band at part load, which is exactly where a pump or fan actually runs.</p>
    </div>
    <div class="table-wrap">
      <table>
        <thead><tr><th>Series</th><th>Efficiency class</th><th>Power</th><th>Frame</th><th>Voltage</th><th>Cooling</th></tr></thead>
        <tbody>
          <tr><td><strong>TYCP</strong></td><td>GB 30253-2013 Grade 1</td><td>0.55–375 kW</td><td>80–355</td><td>380 V</td><td>IC411, IC416 at ≥55 kW / 3,000 rpm</td></tr>
          <tr><td><strong>TYCP2</strong></td><td>GB 30253-2013 Grade 1</td><td>0.55–450 kW</td><td>80–355</td><td>380 V</td><td>IC411</td></tr>
        </tbody>
      </table>
    </div>
    <figure style="margin:34px 0 0">
      <img src="assets/img/motors-pm.svg" alt="Permanent-magnet synchronous motor with matched variable-frequency drive" loading="lazy" style="width:100%;max-width:780px;display:block;margin:0 auto;border:1px solid #e2eaef;border-radius:14px;background:#fff">
    </figure>
    <div class="grid-2" style="margin-top:36px;gap:56px;align-items:start">
      <div class="prose">
        <h3>Why permanent magnet, and when not to</h3>
        <p>An induction rotor has to be magnetised by the stator — that magnetising current is a standing loss whether the shaft is loaded or not. A permanent-magnet rotor supplies its own field, so the efficiency curve stays flat from about 25% to 120% load. On a pump running at 60–80% of design flow for most of the year, that is where the saving is.</p>
        <p>The trade-off is honest: <strong>a PM motor must run from a drive.</strong> It cannot be started across the line. If the existing installation has no VFD, the drive has to be added, and that changes the payback — often still positive, but it has to be calculated, not assumed.</p>
      </div>
      <div class="prose">
        <h3>Drop-in replacement, dimensionally</h3>
        <p>TYCP series mounting dimensions match the YE2 / YX3 / YE3 / YE4 induction frames, so a PM motor goes onto the existing baseplate and coupling without re-machining. TYCP2 raises power density further — up to 450 kW in the same 80–355 frame range — so a smaller motor can carry a duty that previously needed the next frame up.</p>
        <ul>
          <li>0.55–375 kW in TYCP; 0.55–450 kW in TYCP2</li>
          <li>Efficiency GB 30253-2013 Grade 1, flat from 25% load</li>
          <li>Pump, fan, compressor, conveyor and machine-tool duty</li>
          <li>Supplied with a matched drive and, where asked, a complete panel</li>
        </ul>
      </div>
    </div>
  </div>
</section>

<section class="alt">
  <div class="wrap">
    <div class="sec-head">
      <p class="eyebrow">Selection guide · indicative</p>
      <h2>Frame and power, 4-pole</h2>
      <p class="lead">A starting point for reading a nameplate or sketching a layout. The definitive table is per series and per voltage; we issue it with the quotation.</p>
    </div>
    <div class="table-wrap">
      <table>
        <thead><tr><th>Frame</th><th>80</th><th>90</th><th>100</th><th>112</th><th>132</th><th>160</th><th>180</th><th>200</th><th>225</th><th>250</th><th>280</th><th>315</th><th>355</th></tr></thead>
        <tbody>
          <tr><td>kW at 4-pole</td><td>0.55–0.75</td><td>1.1–1.5</td><td>2.2–3.0</td><td>4.0</td><td>5.5–7.5</td><td>11–15</td><td>18.5–22</td><td>30</td><td>37–45</td><td>55</td><td>75–90</td><td>110–132</td><td>160–375</td></tr>
          <tr><td>IE5 availability</td><td>●</td><td>●</td><td>●</td><td>●</td><td>●</td><td>●</td><td>●</td><td>●</td><td>●</td><td>●</td><td>●</td><td>●</td><td>●</td></tr>
        </tbody>
      </table>
    </div>
    <p class="small" style="margin-top:18px">2-, 6-, 8- and 10-pole machines cover the same frames at different speeds and powers; explosion-proof and high-voltage frames follow their own tables. Where a duty falls between frames, the choice is made on starting torque, thermal margin and the driven machine's inertia — not on price alone.</p>
  </div>
</section>

<section>
  <div class="wrap grid-2" style="gap:56px;align-items:start">
    <div class="prose">
      <h2>What we need to quote a motor</h2>
      <ul>
        <li><strong>Duty power and speed</strong> — kW at the shaft, rpm, or the driven machine's curve</li>
        <li><strong>Supply</strong> — voltage, frequency, phases; 380 V or 6/10 kV</li>
        <li><strong>Starting</strong> — direct-on-line, star-delta, soft starter or VFD; starts per hour</li>
        <li><strong>Environment</strong> — ambient temperature, altitude, indoor/outdoor, humidity, dust</li>
        <li><strong>Area classification</strong> — safe area, or the Ex zone and gas group</li>
        <li><strong>Mounting</strong> — B3, B5, B35, V1; foot or flange dimensions if it must match an existing baseplate</li>
        <li><strong>Extras</strong> — encoder, winding and bearing RTDs, space heaters, terminal box position, paint colour</li>
      </ul>
      <p class="small">Send the nameplate photo of the motor you are replacing and we will come back with the equivalent model, its efficiency class and the annual kWh difference at your running hours.</p>
    </div>
    <div class="prose">
      <h2>Supplied as part of the pump package</h2>
      <p>Every plunger pump, slurry pump and mobile unit on this site can now be quoted as a complete train: pump, motor, coupling and guard, baseplate, VFD or starter, instrumentation and control panel — assembled, aligned and tested before shipment.</p>
      <ul>
        <li><strong>One interface.</strong> One supplier for the shaft alignment, the coupling selection and the starting method.</li>
        <li><strong>One guarantee.</strong> The train is warranted as a train, not as three parts from three vendors.</li>
        <li><strong>Spares in one list.</strong> Bearings, seals, windings and drives on a single recommended-spares schedule.</li>
      </ul>
      <p>For a replacement motor on an existing pump, we work from the nameplate and the driven curve, and confirm the frame will land on the existing baseplate before anything is ordered.</p>
    </div>
  </div>
</section>

<section class="tight">
  <div class="wrap">
    <div class="card">
      <p class="tag">Compliance</p>
      <h3>Efficiency labels, and what we will not claim</h3>
      <p style="max-width:900px">Efficiency classes are stated against the Chinese mandatory standards GB 18613-2020 (asynchronous) and GB 30253-2013 (permanent-magnet synchronous), with the IEC 60034-30-1 equivalent given for reference. Certificates for a specific market — CE, EAC, UL/CSA or a hazardous-area approval — are quoted item by item against the motor, the voltage and the country it will be installed in. We do not describe a motor as certified for a market where that approval has not been issued for the delivered configuration.</p>
    </div>
  </div>
</section>

<section class="tight">
  <div class="wrap">
    <div class="band">
      <div>
        <h2>Send the nameplate you are running now.</h2>
        <p>Frame, power, speed and efficiency class are all we need to start. We answer with the equivalent high-efficiency model, the frame check, and the annual kWh difference at your running hours.</p>
      </div>
      <a class="btn light" href="contact.html">Ask for a motor comparison</a>
    </div>
  </div>
</section>
"""

MOTORS_ZH = """
{crumbs}
<section class="page-head">
  <div class="wrap">
    <p class="eyebrow">电机 · IE3–IE5 · 0.12–2,500 kW</p>
    <h1>电耗在电机上，不在泵壳上</h1>
    <p class="lead">低压 0.12–375 kW 高能效异步电动机、6/10 kV 高压 160–2,500 kW 异步电动机，以及 0.55–450 kW 永磁同步电动机。每提一档能效，电机损耗就去掉 15%~20%——两档的差价，往往在泵回本之前就赚回来了。</p>
  </div>
</section>

<section>
  <div class="wrap grid-2" style="gap:56px;align-items:start">
    <div class="prose">
      <h2>泵是带水力端的电机</h2>
      <p>连续运行的工况里，电机比撬上任何部件转得都久，而且它以出厂时的能效等级一直转下去。一台水力效率 85% 的泵，配的可能是效率 89% 的电机——客户买到的是机组效率，不是单看泵的效率。</p>
      <p>所以我们把驱动端和泵端一起报：泵、电机、联轴器与护罩、底座，工况有变化时再加变频器。一套图纸、一家负责、一个质保。</p>
      <div class="callout">
        <p><strong>每提一档能效，损耗去掉约五分之一。</strong>IE3→IE4 约减 15%~20% 电机损耗，IE4→IE5 再减约 20%。连续工况下这是最便宜的一度电：不用土建、不用改管路，停机时间就是换机那几小时。</p>
      </div>
      <h3>机座与安装尺寸不变</h3>
      <p>下列低压系列符合 IEC 60034 尺寸：同一机座号＝同一轴中心高、同一底脚孔距、同一法兰止口。YE3 或 YX3 拆下来，YE5 装上去，底座不动、联轴器重新对中即可。</p>
    </div>
    <div>
      <div class="card">
        <h3>一眼看全</h3>
        <ul class="checks">
          <li>低压异步：0.12–375 kW，机座 63–355，2–10 极</li>
          <li>IE5（GB 18613-2020 1 级）自 0.75 kW 起可供</li>
          <li>高压 YKK：160–2,500 kW，6/10 kV，机座 355–630</li>
          <li>永磁同步：0.55–450 kW，机座 80–355</li>
          <li>隔爆 YBX5：0.18–375 kW，IE5，Ex d</li>
          <li>标配 IP55 / F 级；IP54、IP65、H 级可定制</li>
        </ul>
      </div>
      <div class="card" style="margin-top:20px;background:#0c1a26;border-color:#0c1a26;color:#fff">
        <p class="tag" style="color:#ffb08a">型谱</p>
        <h3 style="color:#fff">型号可以对着查</h3>
        <p style="color:#c6d6df">本页型谱按皖南电机（Wannan Electric）样本编排——这是国内这几个机座号的主流型谱。您图纸或备件清单上写的是 YE3-280M-4 还是 TYCP-315，都能直接在下表找到对应规格。</p>
        <div class="kv" style="border-color:rgba(255,255,255,.14)"><span>安装尺寸</span><b>IEC 60034 / DIN 42673</b></div>
        <div class="kv" style="border-color:rgba(255,255,255,.14)"><span>能效标准</span><b>GB 18613-2020 / IEC 60034-30-1</b></div>
        <div class="kv" style="border:0"><span>永磁标准</span><b>GB 30253-2013</b></div>
      </div>
    </div>
  </div>
</section>

<section class="alt">
  <div class="wrap">
    <div class="sec-head">
      <p class="eyebrow">第一类</p>
      <h2>高能效异步电动机</h2>
      <p class="lead">鼠笼转子、全封闭风扇冷却、铸铁机座。泵、风机、压缩机、输送机、破碎机的默认驱动——也是唯一能直接落在原底座上、不动传动方式的品类。</p>
    </div>
    <div class="table-wrap">
      <table>
        <thead><tr><th>系列</th><th>能效等级</th><th>功率</th><th>机座号</th><th>极数</th><th>典型用途</th></tr></thead>
        <tbody>
          <tr><td><strong>YE5</strong></td><td>GB 18613-2020 1 级（IE5）</td><td>0.75–375 kW</td><td>80–355</td><td>2、4、6、8</td><td>电费占比高的连续工况——锅炉给水、矿井排水、曝气、外输</td></tr>
          <tr><td><strong>YE4</strong></td><td>GB 18613-2020 2 级（IE4）</td><td>0.37–375 kW</td><td>63–355</td><td>2、4、6、8</td><td>交期或预算不取 IE5 时的实用默认档</td></tr>
          <tr><td><strong>YE3</strong></td><td>GB 18613-2020 3 级（IE3）</td><td>0.12–375 kW</td><td>63–355</td><td>2、4、6、8、10</td><td>通用场合；在役机队的同规格替换</td></tr>
          <tr><td><strong>YBX5</strong></td><td>GB 18613-2020 1 级（IE5），Ex d</td><td>0.18–375 kW</td><td>80–355</td><td>2、4、6、8</td><td>可燃气体环境——瓦斯增压、炼化、喷涂与溶剂车间</td></tr>
          <tr><td><strong>YKK</strong></td><td>高效率，6/10 kV</td><td>160–2,500 kW</td><td>355–630</td><td>2–12</td><td>380 V 的电缆与开关柜不再划算的大功率泵、风机驱动</td></tr>
        </tbody>
      </table>
    </div>
    <p class="small" style="margin-top:18px">标准：380 V / 50 Hz（其他电压、60 Hz 可定制）· S1 工作制 · IP55 · F 级 · IC411 · B3 / B5 / B35 / V1 安装。同平台派生：变频调速（YVF2 / YXVF）、电磁制动、变极多速、低振动低噪声、船用、辊道、不锈钢机壳。</p>

    <figure style="margin:34px 0 0">
      <img src="assets/img/motors-induction.svg" alt="全封闭风扇冷却异步电动机，机座号 63–355" loading="lazy" style="width:100%;max-width:780px;display:block;margin:0 auto;border:1px solid #e2eaef;border-radius:14px;background:#fff">
    </figure>

    <div class="grid-2" style="margin-top:40px;gap:26px">
      <div class="card">
        <p class="tag">算一遍就明白</p>
        <h3>1 级能效到底值多少</h3>
        <p>110 kW、4 极，IE3 与 IE5 的效率差约 1.1 个百分点。听着不多，乘上每年 8,000 小时：约 1.3 kW 的损耗被永久去掉，一年约 10,400 kWh，按 0.10 美元/kWh 是每年约 1,040 美元——一台电机。</p>
        <p class="small">效率值为示意口径；具体型号与电压的实测效率以型式试验数据为准，随数据表出具。</p>
      </div>
      <div class="card">
        <p class="tag">高压</p>
        <h3>YKK：380 V 不再划算的时候</h3>
        <p>大约 300 kW 以上，380 V 电机的电缆与开关柜反而成了安装里最贵的一块。YKK 系列用 6 kV 或 10 kV，全钢板焊接机座、顶部空空冷却器、VPI 真空压力浸漆——160–2,500 kW，2–12 极，IP44/IP54/IP55，F/H 级，IMB3 / IMB35。</p>
        <ul class="checks">
          <li>锅炉给水泵、矿井排水泵驱动</li>
          <li>引风机、送风机、一次风机</li>
          <li>压缩机、破碎机、输送机</li>
        </ul>
      </div>
    </div>
  </div>
</section>

<section>
  <div class="wrap">
    <div class="sec-head">
      <p class="eyebrow">第二类</p>
      <h2>永磁同步电动机</h2>
      <p class="lead">转子自带永磁体，不靠定子励磁。同机座号下效率更高、功率密度更大，而且部分负载段的高效区宽得多——泵和风机恰恰常年跑在部分负载。</p>
    </div>
    <div class="table-wrap">
      <table>
        <thead><tr><th>系列</th><th>能效等级</th><th>功率</th><th>机座号</th><th>电压</th><th>冷却方式</th></tr></thead>
        <tbody>
          <tr><td><strong>TYCP</strong></td><td>GB 30253-2013 1 级</td><td>0.55–375 kW</td><td>80–355</td><td>380 V</td><td>IC411；≥55 kW / 3,000 rpm 为 IC416</td></tr>
          <tr><td><strong>TYCP2</strong></td><td>GB 30253-2013 1 级</td><td>0.55–450 kW</td><td>80–355</td><td>380 V</td><td>IC411</td></tr>
        </tbody>
      </table>
    </div>
    <figure style="margin:34px 0 0">
      <img src="assets/img/motors-pm.svg" alt="永磁同步电动机与配套变频器" loading="lazy" style="width:100%;max-width:780px;display:block;margin:0 auto;border:1px solid #e2eaef;border-radius:14px;background:#fff">
    </figure>
    <div class="grid-2" style="margin-top:36px;gap:56px;align-items:start">
      <div class="prose">
        <h3>什么时候用永磁，什么时候别用</h3>
        <p>异步电机的转子要靠定子励磁，这股励磁电流不管轴上有没有负载都在耗。永磁转子自带磁场，所以效率曲线在 25%~120% 负载区间几乎是平的。泵常年跑在设计流量的 60%~80%，省下来的就在这一段。</p>
        <p>代价要说清楚：<strong>永磁电机必须配变频器运行，不能直接合闸启动。</strong>现场原本没有变频器，就得加驱动，回收期要重算——多数情况仍然划算，但必须算，不能默认。</p>
      </div>
      <div class="prose">
        <h3>尺寸可原位替换</h3>
        <p>TYCP 系列安装尺寸与 YE2 / YX3 / YE3 / YE4 异步电机一致，永磁机可以直接落在原底座、原联轴器上，不用重新加工。TYCP2 把功率密度再抬一档——80–355 机座做到 450 kW，原来要大一档机座的工况，现在可用小一档的电机。</p>
        <ul>
          <li>TYCP 0.55–375 kW；TYCP2 0.55–450 kW</li>
          <li>效率 GB 30253-2013 1 级，25% 负载起即保持平坦</li>
          <li>泵、风机、压缩机、输送机、机床主轴工况</li>
          <li>可配套供应变频器，需要时供整柜</li>
        </ul>
      </div>
    </div>
  </div>
</section>

<section class="alt">
  <div class="wrap">
    <div class="sec-head">
      <p class="eyebrow">选型对照 · 示意</p>
      <h2>4 极电机：机座号与功率</h2>
      <p class="lead">用于读铭牌、画布置图的起点。最终以各系列、各电压的正式型谱为准，随报价提供。</p>
    </div>
    <div class="table-wrap">
      <table>
        <thead><tr><th>机座号</th><th>80</th><th>90</th><th>100</th><th>112</th><th>132</th><th>160</th><th>180</th><th>200</th><th>225</th><th>250</th><th>280</th><th>315</th><th>355</th></tr></thead>
        <tbody>
          <tr><td>4 极功率 kW</td><td>0.55–0.75</td><td>1.1–1.5</td><td>2.2–3.0</td><td>4.0</td><td>5.5–7.5</td><td>11–15</td><td>18.5–22</td><td>30</td><td>37–45</td><td>55</td><td>75–90</td><td>110–132</td><td>160–375</td></tr>
        </tbody>
      </table>
    </div>
    <p class="small" style="margin-top:18px">2、6、8、10 极在同一机座号下对应不同转速与功率；隔爆与高压机型另有各自型谱。工况卡在两档机座之间时，按启动转矩、热裕量和被驱动机械的转动惯量选，不单看价格。</p>
  </div>
</section>

<section>
  <div class="wrap grid-2" style="gap:56px;align-items:start">
    <div class="prose">
      <h2>报价需要哪些参数</h2>
      <ul>
        <li><strong>轴功率与转速</strong>——kW（轴端）、rpm，或被驱动机械的性能曲线</li>
        <li><strong>电源</strong>——电压、频率、相数；380 V 还是 6/10 kV</li>
        <li><strong>启动方式</strong>——直接启动、星三角、软启或变频；每小时启动次数</li>
        <li><strong>环境</strong>——环境温度、海拔、室内/室外、湿度、粉尘</li>
        <li><strong>区域划分</strong>——安全区，或防爆区域与气体组别</li>
        <li><strong>安装</strong>——B3、B5、B35、V1；需与原底座匹配时给出底脚/法兰尺寸</li>
        <li><strong>附加</strong>——编码器、绕组与轴承测温、防凝露加热器、接线盒方位、漆色</li>
      </ul>
      <p class="small">把在役电机的铭牌拍照发来，我们回等效型号、能效等级，以及按您的年运行小时算出的年节电量。</p>
    </div>
    <div class="prose">
      <h2>随泵组成套供货</h2>
      <p>本站的柱塞泵、浆料泵、移动泵站，现在都可以按整机机组报价：泵、电机、联轴器与护罩、底座、变频器或启动柜、仪表与控制柜——出厂前组装、对中、试车。</p>
      <ul>
        <li><strong>一个接口。</strong>对中、联轴器选型、启动方式，由一家负责。</li>
        <li><strong>一个质保。</strong>按机组整体质保，不是三家供应商各保一段。</li>
        <li><strong>一张备件单。</strong>轴承、密封、绕组、驱动，合并成一份推荐备件清单。</li>
      </ul>
      <p>给在役泵换电机时，我们从铭牌和被驱动曲线反推，下单前先确认机座能落在原底座上。</p>
    </div>
  </div>
</section>

<section class="tight">
  <div class="wrap">
    <div class="card">
      <p class="tag">合规口径</p>
      <h3>能效标识，以及我们不会说的话</h3>
      <p style="max-width:900px">能效等级按中国强制性标准标注：异步电机 GB 18613-2020，永磁同步电机 GB 30253-2013，并附 IEC 60034-30-1 对应等级供参考。面向特定市场的认证——CE、EAC、UL/CSA 或防爆认证——逐项按电机、电压与安装国别报价。交付配置尚未取得该市场认证的，我们不会写成"已认证"。</p>
    </div>
  </div>
</section>

<section class="tight">
  <div class="wrap">
    <div class="band">
      <div>
        <h2>把在役电机的铭牌发来。</h2>
        <p>机座号、功率、转速、能效等级，有这四项就能起步。我们回等效高效型号、机座核对结果，以及按年运行小时算出的节电量。</p>
      </div>
      <a class="btn light" href="contact.html">索取电机替换对比</a>
    </div>
  </div>
</section>
"""
