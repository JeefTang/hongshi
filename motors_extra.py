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

<section>
  <div class="wrap">
    <div class="sec-head">
      <p class="eyebrow">Bought on its own</p>
      <h2>A motor does not have to arrive with a pump</h2>
      <p class="lead">Most of the motors we ship to Malaysia and Indonesia go into palm oil mills as single replacement units: one motor in a crate, a test report with it, landing on a baseplate poured twenty years ago. We match the frame, not the catalogue number.</p>
    </div>
    <div class="grid-2" style="gap:40px;align-items:start">
      <div class="prose">
        <h3>Replacement is the largest motor market in ASEAN</h3>
        <p>A screw press stops on a Tuesday. The mill needs a 4-pole motor with the same foot holes, the same shaft height and the same shaft extension, running before the weekend. That is not a pump project and we do not treat it as one: it is a single unit, nameplate-matched, crated and shipped.</p>
        <ul class="checks">
          <li>One-off replacement units — no minimum quantity</li>
          <li>Frame, foot holes, flange and shaft matched to the motor coming out</li>
          <li>IE3 / IE4 / IE5 equivalent of an old IE1 / IE2 machine — same baseplate</li>
          <li>VFD-duty version where the drive stays and only the motor is replaced</li>
          <li>Ex d version where the area classification requires it</li>
          <li>Spare unit for the critical drive, ordered with the replacement</li>
        </ul>
      </div>
      <div class="prose">
        <h3>415 V, 380 V, 50 Hz</h3>
        <p>Malaysian mills are normally 415 V / 50 Hz; Indonesian mills are 380 V or 415 V / 50 Hz, with 60 Hz gensets on some isolated lines. All of these are standard builds for us — the motor is wound for the supply on site, not for a generic export voltage.</p>
        <h3>What we need to match it</h3>
        <ul>
          <li>A photo of the nameplate — kW, poles, voltage, frequency, frame, mounting</li>
          <li>Shaft extension and flange drawing, if the coupling or pulley is fixed</li>
          <li>Duty — continuous, or starts per hour</li>
          <li>Environment — ambient, humidity, dust, washdown</li>
          <li>Starting — direct-on-line, star-delta, soft starter or drive; cable length if driven</li>
        </ul>
        <p class="small">Send the photo and we reply with the equivalent model, a frame check against the baseplate, the price and the lead time. If the old frame is obsolete, we say what has to change before anything is ordered.</p>
      </div>
    </div>
    <div class="table-wrap" style="margin-top:38px">
      <table>
        <thead><tr><th>Palm oil mill drive</th><th>What usually decides the motor</th><th>What we match</th></tr></thead>
        <tbody>
          <tr><td><strong>Sterilizer / cage hauling</strong></td><td>Frequent starts, brake or geared drive, hot and wet surroundings</td><td>Frame and shaft, brake torque, IP55, VFD duty if the drive stays</td></tr>
          <tr><td><strong>Screw press</strong></td><td>High starting torque, continuous duty, heavy radial load</td><td>Foot or flange pattern, shaft extension, thermal margin</td></tr>
          <tr><td><strong>Thresher / bunch crusher</strong></td><td>High inertia at start, shock load in service</td><td>Frame, starting torque, IE3 or IE4 equivalent</td></tr>
          <tr><td><strong>Kernel plant</strong> — crusher, separator, winnower</td><td>Dust, continuous running, small frames</td><td>Frame 80–200, IP55, IE3 / IE4</td></tr>
          <tr><td><strong>EFB shredder / press</strong></td><td>Very high inertia, load swings, long acceleration</td><td>VFD duty with independent fan; thermal margin stated, not assumed</td></tr>
          <tr><td><strong>Boiler feed and process pumps</strong></td><td>Continuous duty, pressure controlled by speed</td><td>2- or 4-pole, VFD duty, motor alone or pump-and-motor</td></tr>
          <tr><td><strong>Sludge, desander and POME pumps</strong></td><td>Moisture, corrosive atmosphere, intermittent running</td><td>IP55 / IP65, moisture-resistant winding, frame match</td></tr>
        </tbody>
      </table>
    </div>
    <p class="small" style="margin-top:16px">The table is a checklist, not a selection: the rating is read off the nameplate and the driven machine, not off the equipment name. Where a mill replaces an IE1 or IE2 motor, the IE3 or IE4 equivalent is normally the same frame — the efficiency step costs nothing in civil works.</p>
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

    <div class="spec-grid" style="margin-top:34px">
      <article class="card" style="padding:0;overflow:hidden">
        <img src="assets/img/wn-motor-ye5.jpg" alt="YE5 series IE5 high-efficiency induction motor" loading="lazy" style="width:100%;aspect-ratio:4/3;object-fit:contain;background:#fff;display:block">
        <div style="padding:16px 18px 18px"><p class="tag" style="margin:0 0 6px">YE5 · IE5</p><p style="margin:0;font-size:14px">0.75–375 kW · frame 80–355</p></div>
      </article>
      <article class="card" style="padding:0;overflow:hidden">
        <img src="assets/img/wn-motor-ye4.jpg" alt="YE4 series IE4 high-efficiency induction motor" loading="lazy" style="width:100%;aspect-ratio:4/3;object-fit:contain;background:#fff;display:block">
        <div style="padding:16px 18px 18px"><p class="tag" style="margin:0 0 6px">YE4 · IE4</p><p style="margin:0;font-size:14px">0.37–375 kW · frame 63–355</p></div>
      </article>
      <article class="card" style="padding:0;overflow:hidden">
        <img src="assets/img/wn-motor-ye3.jpg" alt="YE3 series IE3 high-efficiency induction motor" loading="lazy" style="width:100%;aspect-ratio:4/3;object-fit:contain;background:#fff;display:block">
        <div style="padding:16px 18px 18px"><p class="tag" style="margin:0 0 6px">YE3 · IE3</p><p style="margin:0;font-size:14px">0.12–375 kW · frame 63–355</p></div>
      </article>
      <article class="card" style="padding:0;overflow:hidden">
        <img src="assets/img/wn-motor-ybx5.jpg" alt="YBX5 series explosion-proof IE5 induction motor" loading="lazy" style="width:100%;aspect-ratio:4/3;object-fit:contain;background:#fff;display:block">
        <div style="padding:16px 18px 18px"><p class="tag" style="margin:0 0 6px">YBX5 · Ex d · IE5</p><p style="margin:0;font-size:14px">0.18–375 kW · frame 80–355</p></div>
      </article>
      <article class="card" style="padding:0;overflow:hidden">
        <img src="assets/img/wn-motor-ykk.jpg" alt="YKK series high-voltage induction motor" loading="lazy" style="width:100%;aspect-ratio:4/3;object-fit:contain;background:#fff;display:block">
        <div style="padding:16px 18px 18px"><p class="tag" style="margin:0 0 6px">YKK · 6/10 kV</p><p style="margin:0;font-size:14px">160–2,500 kW · frame 355–630</p></div>
      </article>
    </div>

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
      <img src="assets/img/wn-motor-tycp.jpg" alt="TYCP series permanent-magnet synchronous motor" loading="lazy" style="width:100%;max-width:620px;display:block;margin:0 auto;border:1px solid #e2eaef;border-radius:14px;background:#fff">
      <figcaption class="small" style="text-align:center;margin-top:10px">TYCP / TYCP2 frame family — same 80–355 mounting envelope as the YE series induction motors.</figcaption>
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
      <h2>On its own, or as part of the pump package</h2>
      <p>A motor is a product line for us, not an accessory. It can ship as a single replacement unit against a nameplate — that is the usual order from a palm oil mill — or as part of a complete train: pump, motor, coupling and guard, baseplate, VFD or starter, instrumentation and control panel, assembled, aligned and tested before shipment.</p>
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

<section>
  <div class="wrap">
    <div class="sec-head">
      <p class="eyebrow">单独供货</p>
      <h2>电机不必跟着泵一起买</h2>
      <p class="lead">我们发往马来西亚、印尼的电机，多数是棕榈油厂的单台替换件：一台电机装箱发货、随附试验报告，落在二十年前浇的底座上。我们匹配的是机座和安装尺寸，不是产品目录上的型号。</p>
    </div>
    <div class="grid-2" style="gap:40px;align-items:start">
      <div class="prose">
        <h3>替换，是东盟最大的电机市场</h3>
        <p>周二一台螺旋压榨机停了。厂里需要的是一台同样底脚孔距、同样轴高、同样轴伸的 4 极电机，周末之前转起来。这不是一个泵类项目，我们也不按项目做：就是单台供货，按铭牌匹配，装箱发运。</p>
        <ul class="checks">
          <li>单台替换，无起订量</li>
          <li>机座、底脚孔、法兰与轴伸，按拆下来的那台匹配</li>
          <li>老 IE1 / IE2 电机可换 IE3 / IE4 / IE5 等效机型，原底座不动</li>
          <li>变频器保留、只换电机时，供变频专用机型</li>
          <li>区域划分要求时，供 Ex d 隔爆机型</li>
          <li>关键驱动可同时订一台备机</li>
        </ul>
      </div>
      <div class="prose">
        <h3>415 V、380 V、50 Hz</h3>
        <p>马来西亚棕榈油厂通常 415 V / 50 Hz；印尼多为 380 V 或 415 V / 50 Hz，部分孤网线路带 60 Hz 发电机组。这几种都是我们的标准供货电压——按现场电源绕线，不按通用出口电压凑。</p>
        <h3>匹配需要哪些信息</h3>
        <ul>
          <li>铭牌照片——功率、极数、电压、频率、机座号、安装方式</li>
          <li>联轴器或皮带轮已固定的，给轴伸与法兰尺寸图</li>
          <li>工作制——连续运行，还是每小时启动次数</li>
          <li>环境——环温、湿度、粉尘、是否冲洗</li>
          <li>启动方式——直接启动、星三角、软启或变频；变频时给电缆长度</li>
        </ul>
        <p class="small">把铭牌照片发来，我们回等效型号、与原底座的机座核对结果、价格和交期。老机座已停产的，先说清必须改什么，再谈下单。</p>
      </div>
    </div>
    <div class="table-wrap" style="margin-top:38px">
      <table>
        <thead><tr><th>棕榈油厂驱动</th><th>决定电机选型的因素</th><th>我们匹配的内容</th></tr></thead>
        <tbody>
          <tr><td><strong>杀菌罐 / 吊笼牵引</strong></td><td>频繁启停、带制动或减速机、湿热环境</td><td>机座与轴伸、制动转矩、IP55；变频保留时供变频专用</td></tr>
          <tr><td><strong>螺旋压榨机</strong></td><td>启动转矩大、连续运行、径向载荷重</td><td>底脚或法兰孔距、轴伸、热裕量</td></tr>
          <tr><td><strong>脱果机 / 果串破碎机</strong></td><td>启动惯量大、运行中有冲击负载</td><td>机座、启动转矩、IE3 或 IE4 等效</td></tr>
          <tr><td><strong>仁厂</strong>——破碎、分离、风选</td><td>粉尘、连续运行、机座偏小</td><td>80–200 机座、IP55、IE3 / IE4</td></tr>
          <tr><td><strong>EFB 撕碎机 / 压榨机</strong></td><td>惯量很大、负载波动、加速时间长</td><td>独立风机变频专用；热裕量写清楚，不靠默认</td></tr>
          <tr><td><strong>锅炉给水与工艺泵</strong></td><td>连续运行、靠调速控压</td><td>2 极或 4 极、变频专用；可只供电机，也可泵机成套</td></tr>
          <tr><td><strong>污泥泵、除砂泵、POME 泵</strong></td><td>潮湿、腐蚀性气氛、间歇运行</td><td>IP55 / IP65、防潮绕组、机座匹配</td></tr>
        </tbody>
      </table>
    </div>
    <p class="small" style="margin-top:16px">这张表是核对清单，不是选型结果：功率从铭牌和被驱动机械上读，不从设备名称上猜。老厂把 IE1 / IE2 换成 IE3 / IE4，机座通常不变——提一档能效，土建上一分钱不用花。</p>
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

    <div class="spec-grid" style="margin-top:34px">
      <article class="card" style="padding:0;overflow:hidden">
        <img src="assets/img/wn-motor-ye5.jpg" alt="YE5 系列 1 级能效（IE5）三相异步电动机" loading="lazy" style="width:100%;aspect-ratio:4/3;object-fit:contain;background:#fff;display:block">
        <div style="padding:16px 18px 18px"><p class="tag" style="margin:0 0 6px">YE5 · IE5</p><p style="margin:0;font-size:14px">0.75–375 kW · 机座 80–355</p></div>
      </article>
      <article class="card" style="padding:0;overflow:hidden">
        <img src="assets/img/wn-motor-ye4.jpg" alt="YE4 系列 2 级能效（IE4）三相异步电动机" loading="lazy" style="width:100%;aspect-ratio:4/3;object-fit:contain;background:#fff;display:block">
        <div style="padding:16px 18px 18px"><p class="tag" style="margin:0 0 6px">YE4 · IE4</p><p style="margin:0;font-size:14px">0.37–375 kW · 机座 63–355</p></div>
      </article>
      <article class="card" style="padding:0;overflow:hidden">
        <img src="assets/img/wn-motor-ye3.jpg" alt="YE3 系列 3 级能效（IE3）三相异步电动机" loading="lazy" style="width:100%;aspect-ratio:4/3;object-fit:contain;background:#fff;display:block">
        <div style="padding:16px 18px 18px"><p class="tag" style="margin:0 0 6px">YE3 · IE3</p><p style="margin:0;font-size:14px">0.12–375 kW · 机座 63–355</p></div>
      </article>
      <article class="card" style="padding:0;overflow:hidden">
        <img src="assets/img/wn-motor-ybx5.jpg" alt="YBX5 系列隔爆型 1 级能效异步电动机" loading="lazy" style="width:100%;aspect-ratio:4/3;object-fit:contain;background:#fff;display:block">
        <div style="padding:16px 18px 18px"><p class="tag" style="margin:0 0 6px">YBX5 · Ex d · IE5</p><p style="margin:0;font-size:14px">0.18–375 kW · 机座 80–355</p></div>
      </article>
      <article class="card" style="padding:0;overflow:hidden">
        <img src="assets/img/wn-motor-ykk.jpg" alt="YKK 系列高压三相异步电动机" loading="lazy" style="width:100%;aspect-ratio:4/3;object-fit:contain;background:#fff;display:block">
        <div style="padding:16px 18px 18px"><p class="tag" style="margin:0 0 6px">YKK · 6/10 kV</p><p style="margin:0;font-size:14px">160–2,500 kW · 机座 355–630</p></div>
      </article>
    </div>

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
      <img src="assets/img/wn-motor-tycp.jpg" alt="TYCP 系列永磁同步电动机" loading="lazy" style="width:100%;max-width:620px;display:block;margin:0 auto;border:1px solid #e2eaef;border-radius:14px;background:#fff">
      <figcaption class="small" style="text-align:center;margin-top:10px">TYCP / TYCP2 同一机座族——与 YE 系列异步电机同 80–355 安装尺寸。</figcaption>
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
      <h2>可以单供，也可以随泵组成套</h2>
      <p>电机在我们这里是一条产品线，不是泵的附件。可以按铭牌单供一台替换机——棕榈油厂的订单多是这种；也可以按整机机组报价：泵、电机、联轴器与护罩、底座、变频器或启动柜、仪表与控制柜——出厂前组装、对中、试车。</p>
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


# ======================================================================
# Variable-frequency duty motors (added 2026-11-09, per Lao Tang)
# Separate product entry under the motor category: YVF2 / YXVF / YBBP.
# Ranges are supply-envelope, confirmed per model at quotation.
# ======================================================================

VFD_EN = """
{crumbs}
<section class="page-head">
  <div class="wrap">
    <p class="eyebrow">VFD-duty motors · 0.55–315 kW · YVF2 / YXVF</p>
    <h1>A motor on a drive is not a standard motor</h1>
    <p class="lead">A variable-frequency drive changes more than the speed. It changes how the motor is cooled at low speed, what the winding insulation has to survive, where the current goes in the bearings, and which part of the torque curve you are allowed to use. The YVF2 / YXVF series is built for that duty from the frame up.</p>
  </div>
</section>

<section>
  <div class="wrap grid-2" style="gap:56px;align-items:start">
    <div class="prose">
      <h2>Four things a general-purpose motor gets wrong on a drive</h2>
      <p>Bolting a VFD onto a standard YE3 works — for a fan running at 80–100% speed. It stops working when the duty spends real hours at low speed, in a hot plant, on a long cable, or at constant torque. The failure is rarely immediate; it shows up as a winding that smells hot after eighteen months.</p>
      <div class="table-wrap">
        <table>
          <thead><tr><th>What the drive does</th><th>What it breaks on a standard motor</th><th>What the VFD motor does instead</th></tr></thead>
          <tbody>
            <tr><td>Runs below base speed</td><td>The shaft-mounted fan moves almost no air at 30% speed, so the winding cooks at exactly the moment the load is highest</td><td>Independent constant-speed cooling fan (IC416) — full airflow at any rotor speed</td></tr>
            <tr><td>Switches at 4–16 kHz</td><td>PWM pulses arrive as a steep wavefront; on a long cable the reflected wave can nearly double the peak voltage at the terminals</td><td>Inverter-grade magnet wire and reinforced turn/phase insulation, rated for the pulse stress</td></tr>
            <tr><td>Creates common-mode voltage</td><td>Shaft voltage discharges through the bearings and erodes the raceway</td><td>Insulated bearing on the non-drive end and a shaft grounding path on the larger frames</td></tr>
            <tr><td>Holds constant torque at low speed</td><td>Self-ventilation and the standard thermal margin run out; the motor cannot hold the load</td><td>Thermal design and fan sized for continuous constant-torque duty across the stated range</td></tr>
          </tbody>
        </table>
      </div>
      <p class="small" style="margin-top:16px">This is why the two products are not interchangeable on paper even when the nameplate kW matches. The frame may be the same; the cooling, insulation system and bearing arrangement are not.</p>
    </div>
    <div>
      <div class="card">
        <h3>At a glance</h3>
        <ul class="checks">
          <li>YVF2 general VFD duty: 0.55–315 kW, frame 80–355</li>
          <li>YXVF high-efficiency VFD duty: 0.75–375 kW, frame 80–355</li>
          <li>2, 4, 6 and 8 poles; 380 V as standard</li>
          <li>Independent cooling fan, IC416, full airflow down to minimum speed</li>
          <li>Insulation class F standard, H on request; IP55</li>
          <li>Constant torque below base speed, constant power above</li>
          <li>Explosion-proof VFD duty (YBBP, Ex d) quoted per area classification</li>
        </ul>
      </div>
      <div class="card" style="margin-top:20px;background:#0c1a26;border-color:#0c1a26;color:#fff">
        <p class="tag" style="color:#ffb08a">Where they go</p>
        <h3 style="color:#fff">Pumps, fans, conveyors, mixers</h3>
        <p style="color:#c6d6df">Any duty where the flow or the process sets the speed instead of the mains: boiler feed on sliding pressure, mine dewatering on varying inflow, aeration on dissolved-oxygen control, slurry transfer on density, cooling-tower fans on wet-bulb.</p>
        <div class="kv" style="border-color:rgba(255,255,255,.14)"><span>Typical base frequency</span><b>50 Hz</b></div>
        <div class="kv" style="border-color:rgba(255,255,255,.14)"><span>Typical speed range</span><b>5–100 Hz</b></div>
        <div class="kv" style="border:0"><span>Duty</span><b>S1, continuous</b></div>
      </div>
    </div>
  </div>
</section>

<section class="alt">
  <div class="wrap">
    <div class="sec-head">
      <p class="eyebrow">Type spectrum</p>
      <h2>VFD-duty series</h2>
      <p class="lead">Same IEC frames as the YE series, so the motor still lands on the existing baseplate — but the cooling and insulation system are specified for drive supply, not for the mains.</p>
    </div>
    <div class="table-wrap">
      <table>
        <thead><tr><th>Series</th><th>Duty</th><th>Power</th><th>Frame</th><th>Poles</th><th>Cooling</th><th>Typical use</th></tr></thead>
        <tbody>
          <tr><td><strong>YVF2</strong></td><td>General VFD duty, constant torque below base speed</td><td>0.55–315 kW</td><td>80–355</td><td>2, 4, 6, 8</td><td>IC416 independent fan</td><td>Pumps, fans, conveyors, mixers on a drive</td></tr>
          <tr><td><strong>YXVF</strong></td><td>High-efficiency VFD duty</td><td>0.75–375 kW</td><td>80–355</td><td>2, 4, 6, 8</td><td>IC416 independent fan</td><td>Continuous duties where the kWh bill dominates</td></tr>
          <tr><td><strong>YBBP</strong></td><td>Flameproof VFD duty, Ex d</td><td>Quoted per area classification</td><td>Per Ex schedule</td><td>2, 4, 6, 8</td><td>IC416 independent fan</td><td>Flammable-gas areas: gas boosting, refinery, solvent plants</td></tr>
        </tbody>
      </table>
    </div>
    <p class="small" style="margin-top:18px">Above about 300 kW the cable and switchgear for 380 V become the expensive part of the installation; a high-voltage YKK machine (160–2,500 kW, 6/10 kV) can be supplied for drive duty with the drive and the winding insulation co-specified. Ranges above are supply envelopes, not model commitments — the exact model is fixed against the duty point at quotation.</p>
  </div>
</section>

<section>
  <div class="wrap">
    <div class="sec-head">
      <p class="eyebrow">Duty envelope · indicative</p>
      <h2>Torque, speed and the limits in between</h2>
      <p class="lead">A drive-duty motor is normally sold as constant torque below base speed and constant power above it. What that means for a pump is simple: below base speed you can hold any head the pump can make at that speed; above it you get more flow but the torque falls away.</p>
    </div>
    <div class="table-wrap">
      <table>
        <thead><tr><th>Region</th><th>Range (typical)</th><th>What is available</th><th>What to watch</th></tr></thead>
        <tbody>
          <tr><td>Constant torque</td><td>5–50 Hz</td><td>Rated torque continuously, with full cooling from the independent fan</td><td>Minimum continuous speed is set by the driven machine, not only by the motor — check pump lubrication and bearing film</td></tr>
          <tr><td>Constant power</td><td>50–100 Hz</td><td>Rated power, torque falls in inverse proportion to speed</td><td>Above base speed the mechanical limits of the driven machine matter more than the motor</td></tr>
          <tr><td>Below minimum</td><td>&lt; 5 Hz</td><td>Short-term only, or not at all</td><td>Low-speed continuous duty needs a different thermal arrangement; ask before assuming</td></tr>
          <tr><td>Skip bands</td><td>Case by case</td><td>—</td><td>The drive is programmed to jump critical speeds of the train; we need the shaft and baseplate data</td></tr>
        </tbody>
      </table>
    </div>
    <p class="small" style="margin-top:18px">A pump or fan load is quadratic: at 80% speed the shaft power is about half, at 50% speed about one eighth. That is the whole economic case for the drive — the motor only has to survive the trip down there.</p>
  </div>
</section>

<section class="alt">
  <div class="wrap grid-2" style="gap:56px;align-items:start">
    <div class="prose">
      <h2>When a standard motor plus a drive is enough</h2>
      <p>We would rather sell the cheaper answer when it is the right one. A general-purpose YE3 or YE4 on a drive is a sensible choice when all of the following hold:</p>
      <ul>
        <li>The duty stays above roughly 70% of rated speed for most running hours</li>
        <li>The load is quadratic (centrifugal pump or fan), not constant torque</li>
        <li>Starts and stops are infrequent, and the ambient is normal</li>
        <li>The motor-to-drive cable is short and the drive output is filtered if it is not</li>
      </ul>
      <p>Specify VFD duty when any of these is true:</p>
      <ul>
        <li>Continuous operation below about 50% speed</li>
        <li>Constant-torque load — positive-displacement pumps, conveyors, mixers, crushers</li>
        <li>High ambient, high altitude, or a hot enclosure</li>
        <li>Frequent starts, high switching frequency, or a long cable run to the motor</li>
      </ul>
    </div>
    <div class="prose">
      <h2>What we need to quote one</h2>
      <ul>
        <li><strong>Duty point</strong> — kW at the shaft at rated speed, and the driven machine's curve</li>
        <li><strong>Speed range</strong> — minimum and maximum operating speed, and how long is spent at each</li>
        <li><strong>Load type</strong> — quadratic or constant torque; starting torque if it is heavy</li>
        <li><strong>Supply</strong> — voltage, frequency, phases; 380 V or 6/10 kV</li>
        <li><strong>Drive</strong> — make and model, or let us select it with the motor</li>
        <li><strong>Installation</strong> — cable length from drive to motor, ambient, altitude, indoor/outdoor, IP requirement</li>
        <li><strong>Area classification</strong> — safe area, or the Ex zone and gas group</li>
        <li><strong>Extras</strong> — encoder, winding and bearing RTDs, space heaters, brake, terminal box position</li>
      </ul>
      <p class="small">Send the existing nameplate and the drive model and we will come back with the equivalent YVF2 / YXVF frame, the cooling arrangement, the minimum continuous speed and the torque available at your lowest operating point.</p>
    </div>
  </div>
</section>

<section>
  <div class="wrap">
    <div class="sec-head">
      <p class="eyebrow">As a package</p>
      <h2>Motor, drive, panel and pump as one train</h2>
      <p class="lead">The failure modes on a VFD-driven train are interface failures: the drive's overload setting against the motor's thermal time constant, the cable against the winding insulation, the minimum speed against the pump's bearing film. Buying them from one place puts that interface on one drawing. The motor can also ship on its own, with or without a drive — a replacement on a palm oil mill's EFB line or screw press is the usual case.</p>
    </div>
    <div class="spec-grid">
      <article class="card"><p class="tag">01 · Drive selection</p><h3>Sized to the duty, not the nameplate</h3><p>Heavy-duty overload margin, switching frequency, and the actual cable length are part of the selection — not left to whoever supplies the drive.</p></article>
      <article class="card"><p class="tag">02 · Cable and filter</p><h3>Long runs get a filter</h3><p>Above the drive manufacturer's cable limit we add a dv/dt or sine filter, or specify a reinforced winding. The motor is ordered to match the decision.</p></article>
      <article class="card"><p class="tag">03 · Panel</p><h3>One enclosure, one set of drawings</h3><p>Drive, breaker, line reactor, cooling and terminals assembled and tested as a panel, not shipped as loose components.</p></article>
      <article class="card"><p class="tag">04 · Commissioning</p><h3>Aligned and run before shipment</h3><p>Pump, motor, coupling and baseplate aligned; the train run at minimum, base and maximum speed before it leaves.</p></article>
    </div>
  </div>
</section>

<section class="tight">
  <div class="wrap">
    <div class="card">
      <p class="tag">Compliance</p>
      <h3>Efficiency, and what we will not claim</h3>
      <p style="max-width:900px">The IE classes in GB 18613-2020 are written for line-start machines. For a motor running from a drive, the meaningful figure is the type-test efficiency at the speed and load where it actually runs, and we state the standard and the test point it was measured against. We do not label a VFD-duty motor with an IE class borrowed from its line-start equivalent. Market certifications — CE, EAC, UL/CSA or a hazardous-area approval — are quoted item by item against the motor, the drive, the voltage and the country of installation.</p>
    </div>
  </div>
</section>

<section class="tight">
  <div class="wrap">
    <div class="band">
      <div>
        <h2>Tell us the speed range, not just the kW.</h2>
        <p>Minimum speed, maximum speed, load type and cable length decide whether the answer is a standard motor on a drive or a VFD-duty machine. We will tell you which, and why.</p>
      </div>
      <a class="btn light" href="contact.html">Ask for a VFD motor selection</a>
    </div>
  </div>
</section>
"""

VFD_ZH = """
{crumbs}
<section class="page-head">
  <div class="wrap">
    <p class="eyebrow">变频调速电机 · 0.55–315 kW · YVF2 / YXVF</p>
    <h1>带变频器的电机，不是普通电机</h1>
    <p class="lead">变频器改变的不只是转速。低速时怎么散热、绕组绝缘要承受什么、电流从轴承里走哪条路、转矩曲线的哪一段能用——这四件事全都变了。YVF2 / YXVF 系列是按变频工况从机座开始设计的。</p>
  </div>
</section>

<section>
  <div class="wrap grid-2" style="gap:56px;align-items:start">
    <div class="prose">
      <h2>普通电机上变频，四处会出问题</h2>
      <p>把变频器接到普通 YE3 上，能用——前提是风机水泵常年跑在 80–100% 转速。一旦工况真的要在低速停留几个小时、车间温度高、电缆拉得长，或者负载是恒转矩，问题就来了。而且很少当场坏：通常是一年半以后，绕组发出一股焦味。</p>
      <div class="table-wrap">
        <table>
          <thead><tr><th>变频器做的事</th><th>普通电机坏在哪</th><th>变频电机怎么解决</th></tr></thead>
          <tbody>
            <tr><td>低于基频运行</td><td>同轴风扇在 30% 转速下几乎不送风，负载最重的时候恰恰散热最差</td><td>独立恒速风机（IC416）——任何转速下风量不变</td></tr>
            <tr><td>4–16 kHz 开关</td><td>PWM 脉冲以陡波前到达；电缆一长，反射波会把端子峰值电压抬到接近两倍</td><td>变频专用漆包线 + 加强匝间/相间绝缘，按脉冲应力选型</td></tr>
            <tr><td>产生共模电压</td><td>轴电压经轴承放电，电蚀滚道</td><td>非驱动端绝缘轴承，较大机座加轴接地</td></tr>
            <tr><td>低速恒转矩</td><td>自扇冷和标准热裕量都不够，带不动负荷</td><td>热设计与风机按连续恒转矩工况选，覆盖标称调速范围</td></tr>
          </tbody>
        </table>
      </div>
      <p class="small" style="margin-top:16px">所以两者不能只看铭牌 kW 互换：机座可能一样，冷却方式、绝缘系统和轴承结构不一样。</p>
    </div>
    <div>
      <div class="card">
        <h3>一眼看全</h3>
        <ul class="checks">
          <li>YVF2 通用变频：0.55–315 kW，机座 80–355</li>
          <li>YXVF 高效变频：0.75–375 kW，机座 80–355</li>
          <li>2、4、6、8 极；标准 380 V</li>
          <li>独立风机 IC416，最低转速下仍满风量</li>
          <li>绝缘 F 级（可定制 H 级）；防护 IP55</li>
          <li>基频以下恒转矩，基频以上恒功率</li>
          <li>隔爆变频（YBBP，Ex d）按防爆区域逐项报价</li>
        </ul>
      </div>
      <div class="card" style="margin-top:20px;background:#0c1a26;border-color:#0c1a26;color:#fff">
        <p class="tag" style="color:#ffb08a">用在哪</p>
        <h3 style="color:#fff">泵、风机、输送机、搅拌机</h3>
        <p style="color:#c6d6df">所有"流量或工艺决定转速、而不是电网决定转速"的工况：滑压运行的锅炉给水、来水量变化的矿井排水、按溶解氧控制的曝气、按浓度调转速的浆料输送、按湿球温度调转速的冷却塔风机。</p>
        <div class="kv" style="border-color:rgba(255,255,255,.14)"><span>典型基频</span><b>50 Hz</b></div>
        <div class="kv" style="border-color:rgba(255,255,255,.14)"><span>典型调速范围</span><b>5–100 Hz</b></div>
        <div class="kv" style="border:0"><span>工作制</span><b>S1 连续</b></div>
      </div>
    </div>
  </div>
</section>

<section class="alt">
  <div class="wrap">
    <div class="sec-head">
      <p class="eyebrow">型谱</p>
      <h2>变频调速系列</h2>
      <p class="lead">与 YE 系列同一套 IEC 机座，仍然落在原底座上——但冷却和绝缘是按变频供电选的，不是按电网直供选的。</p>
    </div>
    <div class="table-wrap">
      <table>
        <thead><tr><th>系列</th><th>用途</th><th>功率</th><th>机座</th><th>极数</th><th>冷却</th><th>典型场合</th></tr></thead>
        <tbody>
          <tr><td><strong>YVF2</strong></td><td>通用变频，基频以下恒转矩</td><td>0.55–315 kW</td><td>80–355</td><td>2、4、6、8</td><td>IC416 独立风机</td><td>泵、风机、输送机、搅拌机变频拖动</td></tr>
          <tr><td><strong>YXVF</strong></td><td>高效变频</td><td>0.75–375 kW</td><td>80–355</td><td>2、4、6、8</td><td>IC416 独立风机</td><td>电费占比高的连续工况</td></tr>
          <tr><td><strong>YBBP</strong></td><td>隔爆变频，Ex d</td><td>按防爆区域报价</td><td>按防爆型谱</td><td>2、4、6、8</td><td>IC416 独立风机</td><td>易燃易爆气体场所：增压、炼化、溶剂车间</td></tr>
        </tbody>
      </table>
    </div>
    <p class="small" style="margin-top:18px">约 300 kW 以上，380 V 的电缆与开关柜会成为安装成本的大头；高压 YKK（160–2,500 kW，6/10 kV）可按变频工况供货，绕组绝缘与变频器一并指定。以上功率为供货区间，不是型号承诺——具体型号按工况点在报价时锁定。</p>
  </div>
</section>

<section>
  <div class="wrap">
    <div class="sec-head">
      <p class="eyebrow">工况包络 · 参考</p>
      <h2>转矩、转速，以及两者之间的边界</h2>
      <p class="lead">变频电机通常按"基频以下恒转矩、基频以上恒功率"供货。对泵来说意思很简单：基频以下，泵在该转速下能打的扬程都能打；基频以上，流量更大，但转矩按转速反比下降。</p>
    </div>
    <div class="table-wrap">
      <table>
        <thead><tr><th>区间</th><th>范围（典型）</th><th>能用什么</th><th>要注意什么</th></tr></thead>
        <tbody>
          <tr><td>恒转矩</td><td>5–50 Hz</td><td>连续输出额定转矩，独立风机保证满风量</td><td>最低连续转速由被驱动机械决定，不只由电机决定——要核泵的润滑与轴承油膜</td></tr>
          <tr><td>恒功率</td><td>50–100 Hz</td><td>额定功率，转矩随转速反比下降</td><td>基频以上，被驱动机械的机械极限比电机更关键</td></tr>
          <tr><td>低于下限</td><td>&lt; 5 Hz</td><td>仅短时，或不建议</td><td>低速连续运行要另做热设计，别默认能用</td></tr>
          <tr><td>跳频段</td><td>逐案</td><td>—</td><td>变频器会设定跳过机组临界转速；需要轴系与底座数据</td></tr>
        </tbody>
      </table>
    </div>
    <p class="small" style="margin-top:18px">泵与风机是平方转矩负载：80% 转速时轴功率约一半，50% 转速时约八分之一。这就是变频的全部经济性来源——电机只要保证能在这个区间里长期活下来。</p>
  </div>
</section>

<section class="alt">
  <div class="wrap grid-2" style="gap:56px;align-items:start">
    <div class="prose">
      <h2>什么时候普通电机加变频就够</h2>
      <p>该用便宜方案的时候，我们宁可卖便宜的。以下条件全部满足时，普通 YE3 / YE4 配变频器是合理选择：</p>
      <ul>
        <li>大部分运行时间在额定转速 70% 以上</li>
        <li>负载是平方转矩（离心泵、风机），不是恒转矩</li>
        <li>启停不频繁，环境温度正常</li>
        <li>电机到变频器的电缆不长，长了就加输出滤波</li>
      </ul>
      <p>出现以下任一情况，就应选变频专用电机：</p>
      <ul>
        <li>长期在约 50% 转速以下连续运行</li>
        <li>恒转矩负载——容积泵、输送机、搅拌机、破碎机</li>
        <li>高环温、高海拔，或装在闷热的柜体/罩壳里</li>
        <li>频繁启停、高开关频率，或电机电缆很长</li>
      </ul>
    </div>
    <div class="prose">
      <h2>报价需要哪些参数</h2>
      <ul>
        <li><strong>工况点</strong>——额定转速下的轴功率 kW，以及被驱动机械的性能曲线</li>
        <li><strong>调速范围</strong>——最低/最高运行转速，以及各转速停留多久</li>
        <li><strong>负载类型</strong>——平方转矩还是恒转矩；重载启动要给启动转矩</li>
        <li><strong>电源</strong>——电压、频率、相数；380 V 还是 6/10 kV</li>
        <li><strong>变频器</strong>——品牌型号，或由我们与电机一起选</li>
        <li><strong>安装</strong>——变频器到电机电缆长度、环温、海拔、室内/室外、防护等级要求</li>
        <li><strong>区域划分</strong>——安全区，或防爆区域与气体组别</li>
        <li><strong>附加</strong>——编码器、绕组与轴承测温、防凝露加热器、制动器、接线盒方位</li>
      </ul>
      <p class="small">把在役电机铭牌和变频器型号发来，我们回等效的 YVF2 / YXVF 机座、冷却方式、最低连续转速，以及在你最低运行点上还能输出多少转矩。</p>
    </div>
  </div>
</section>

<section>
  <div class="wrap">
    <div class="sec-head">
      <p class="eyebrow">成套</p>
      <h2>电机、变频器、控制柜、泵——按一套机组供货</h2>
      <p class="lead">变频机组的故障，多数出在接口上：变频器的过载设定对不上电机的热时间常数、电缆对不上绕组绝缘、最低转速对不上泵的轴承油膜。从一家买，这些接口就在同一张图纸上。电机也可以单台供货，带不带变频器都行——棕榈油厂 EFB 线、螺旋压榨机换电机，多是这种情况。</p>
    </div>
    <div class="spec-grid">
      <article class="card"><p class="tag">01 · 变频器选型</p><h3>按工况选，不按铭牌选</h3><p>重载过载裕量、开关频率、实际电缆长度都算进选型，不留给"谁供变频器谁定"。</p></article>
      <article class="card"><p class="tag">02 · 电缆与滤波</p><h3>长线加滤波</h3><p>超过变频器厂家允许的电缆长度，就加 dv/dt 或正弦波滤波器，或者改订加强绝缘绕组——电机按这个决定下单。</p></article>
      <article class="card"><p class="tag">03 · 控制柜</p><h3>一个柜，一套图纸</h3><p>变频器、断路器、进线电抗器、散热与端子，组装成柜并通电测试后出厂，不是散件发货。</p></article>
      <article class="card"><p class="tag">04 · 出厂试车</p><h3>对中、试运行后再发运</h3><p>泵、电机、联轴器、底座对中；最低、基频、最高三个转速点在厂内跑过再出厂。</p></article>
    </div>
  </div>
</section>

<section class="tight">
  <div class="wrap">
    <div class="card">
      <p class="tag">合规口径</p>
      <h3>能效标识，以及我们不会说的话</h3>
      <p style="max-width:900px">GB 18613-2020 的 IE 等级是写给电网直供（line-start）电机的。变频运行的电机，真正有意义的数字是"在实际运行的那个转速和负载点上的型式试验效率"，我们会同时说明它按哪个标准、在哪个测试点测得。我们不会把直供机型的 IE 等级直接贴到变频电机上。面向特定市场的认证——CE、EAC、UL/CSA 或防爆认证——按电机、变频器、电压与安装国别逐项报价。</p>
    </div>
  </div>
</section>

<section class="tight">
  <div class="wrap">
    <div class="band">
      <div>
        <h2>请告诉我们调速范围，而不只是 kW。</h2>
        <p>最低转速、最高转速、负载类型、电缆长度，这四项决定答案是"普通电机配变频"还是"变频专用电机"。我们会告诉你选哪个，以及为什么。</p>
      </div>
      <a class="btn light" href="contact.html">索取变频电机选型</a>
    </div>
  </div>
</section>
"""
