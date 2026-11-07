#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
New product-line pages for the Hongshi site (added 2026-11-08).

Three families:
  1. maglev-blowers.html  — magnetic / air-foil bearing high-speed turbo blowers
                            and turbo vacuum pumps
  2. mobile-pumps.html    — mobile / portable pump units (trailer, skid, container)
  3. edge-ai.html         — industrial AI agent appliance (OpenClaw on edge hardware)

Content is rendered by build.py (English) and zh_pages.py (Chinese).
Spec numbers are supply-envelope ranges, not model commitments; the exact model is
fixed per duty point at quotation time (same policy as the existing pump pages).
"""

# ------------------------------------------------------------------ EN: maglev

MAGLEV_EN = """
{crumbs}
<section class="page-head">
  <div class="wrap">
    <p class="eyebrow">High-speed turbo machinery · oil-free</p>
    <h1>Blowers and vacuum pumps on a levitated shaft</h1>
    <p class="lead">Direct-drive high-speed permanent-magnet rotors carried on magnetic or air-foil bearings. No gearbox, no oil, no mechanical contact — 70–80% isothermal efficiency where a water-ring or Roots machine delivers 30–65%.</p>
  </div>
</section>

<section>
  <div class="wrap grid-2" style="gap:56px;align-items:start">
    <div class="prose">
      <h2>Where the energy goes</h2>
      <p>Air and vacuum duty is sized in cubic metres per minute, but it is paid for in kilowatts, continuously. A water-ring vacuum pump spends a third to a half of its shaft power churning the sealing water. A Roots blower loses the rest to tip clearance that opens as the rotors wear.</p>
      <p>A levitated rotor removes both losses. The impeller is the only moving part, it turns on a film of magnetic force or air, and nothing touches anything until the rotor lands — which only happens at standstill.</p>
      <div class="table-wrap" style="margin:26px 0">
        <table>
          <thead><tr><th>Machine</th><th>Typical efficiency</th><th>Working fluid</th><th>Wear parts</th></tr></thead>
          <tbody>
            <tr><td>Water-ring vacuum pump</td><td>30–50%</td><td>Sealing water, continuous</td><td>Impeller, cone, shaft</td></tr>
            <tr><td>Roots blower / wet Roots vacuum pump</td><td>50–65%</td><td>Sealing water on wet types</td><td>Rotors, gears, seals</td></tr>
            <tr><td><strong>Turbo blower / turbo vacuum pump, levitated rotor</strong></td><td><strong>70–80%</strong></td><td>None — dry running</td><td>Air filter only</td></tr>
          </tbody>
        </table>
      </div>
      <p>On a 250 kW duty the difference between 55% and 75% is roughly 120 kW of shaft power — close to a million kilowatt-hours a year at 8,000 hours, before any maintenance saving is counted.</p>
      <div class="callout"><p><strong>No oil, no water, no gearbox.</strong> That removes the oil circuit, the oil cooler, the water supply and the gear-mesh noise from the equipment list — and removes them from the maintenance schedule as well.</p></div>
    </div>
    <div>
      <div class="card">
        <h3>At a glance</h3>
        <ul class="checks">
          <li>Flow 20–400 m³/min, pressure rise 40–100 kPa (blower)</li>
          <li>Suction to −58 kPa single stage, −75 kPa two stage (vacuum)</li>
          <li>Isothermal efficiency 70–80%, 20–35% saving against the machine replaced</li>
          <li>Variable speed 45–100%, surge protection and anti-surge recycle built in</li>
          <li>Remote monitoring over Modbus TCP / Ethernet as standard</li>
        </ul>
      </div>
      <div class="card" style="margin-top:20px;background:#0c1a26;border-color:#0c1a26;color:#fff">
        <p class="tag" style="color:#ffb08a">Duty benchmark</p>
        <h3 style="color:#fff">Coal-mine gas drainage</h3>
        <p style="color:#c6d6df">Replacing a wet Roots station at 60 kPa: a levitated turbo vacuum pump at 70% efficiency against Roots at 55% gives 21% lower shaft power at the same suction volume — 34 to 126 MWh saved per machine per year across the 200–750 m³/min range.</p>
        <div class="kv" style="border-color:rgba(255,255,255,.14)"><span>Suction volume</span><b>200–750 m³/min</b></div>
        <div class="kv" style="border-color:rgba(255,255,255,.14)"><span>Working vacuum</span><b>−60 kPa</b></div>
        <div class="kv" style="border:0"><span>Typical saving</span><b style="color:#7ee2c4">21% shaft power</b></div>
      </div>
    </div>
  </div>
</section>

<section class="alt">
  <div class="wrap">
    <div class="sec-head">
      <p class="eyebrow">Two bearing technologies</p>
      <h2>Magnetic where the duty is heavy, air foil where it is tight</h2>
      <p class="lead">Both are oil-free. The choice is made on power, duty cycle and how much control you want over rotor position.</p>
    </div>
    <div class="grid-2">
      <article class="card prod-card" style="padding:28px">
        <div class="card-body" style="padding:0">
          <p class="tag">MB series · active magnetic bearing</p>
          <h3>Magnetic-bearing blowers and vacuum pumps</h3>
          <p>Five-axis active magnetic bearings with digital position control. Rotor position, vibration and temperature are measured continuously and reported — the machine tells you its own condition instead of failing without warning.</p>
          <ul class="checks">
            <li>30–400 kW motor range, 20–400 m³/min</li>
            <li>Pressure rise 40–100 kPa; vacuum to −58 kPa (single) / −75 kPa (two stage)</li>
            <li>Rotor lands on backup bearings only at standstill</li>
            <li>Condition data available to the plant DCS</li>
          </ul>
        </div>
      </article>
      <article class="card prod-card" style="padding:28px">
        <div class="card-body" style="padding:0">
          <p class="tag">AB series · air foil bearing</p>
          <h3>Air-foil-bearing blowers</h3>
          <p>Compliant foil bearings that ride on an air film generated by the rotor itself. No controller, no electromagnets, no backup bearing electronics — the simplest oil-free architecture, and the cheapest to own at moderate power.</p>
          <ul class="checks">
            <li>30–250 kW motor range, 20–120 m³/min</li>
            <li>Pressure rise 40–80 kPa</li>
            <li>No bearing control cabinet; starts on the foil, not on a lift-off sequence</li>
            <li>Best fit for aeration and low-pressure process air</li>
          </ul>
        </div>
      </article>
    </div>
  </div>
</section>

<section>
  <div class="wrap">
    <div class="sec-head">
      <p class="eyebrow">Supply envelope</p>
      <h2>Standard ranges</h2>
      <p class="lead">These are the envelopes we quote from. The exact model, impeller trim and motor rating are fixed against your duty point — flow, pressure or vacuum, inlet temperature, altitude and gas composition.</p>
    </div>
    <div class="table-wrap">
      <table>
        <thead><tr><th>Family</th><th>Duty</th><th>Flow / suction volume</th><th>Pressure</th><th>Motor</th></tr></thead>
        <tbody>
          <tr><td>MB blower</td><td>Process air, aeration, conveying</td><td>30–400 m³/min</td><td>40–100 kPa rise</td><td>30–400 kW</td></tr>
          <tr><td>AB blower</td><td>Aeration, low-pressure air</td><td>20–120 m³/min</td><td>40–80 kPa rise</td><td>30–250 kW</td></tr>
          <tr><td>MB vacuum, single stage</td><td>Vacuum, filtration, gas drainage</td><td>100–750 m³/min</td><td>to −58 kPa</td><td>75–400 kW</td></tr>
          <tr><td>MB vacuum, two stage</td><td>High-vacuum process duty</td><td>100–750 m³/min</td><td>to −75 kPa</td><td>110–450 kW</td></tr>
        </tbody>
      </table>
    </div>
    <p class="small" style="margin-top:16px">Gas with entrained liquid or dust requires a separator and filtration package ahead of the machine — quoted with the unit, not assumed.</p>
  </div>
</section>

<section class="alt">
  <div class="wrap">
    <div class="sec-head">
      <p class="eyebrow">Scope of supply</p>
      <h2>What arrives on the skid</h2>
    </div>
    <div class="grid-3">
      <article class="card">
        <div class="icon">◍</div>
        <h3>Core machine</h3>
        <p>High-speed PM rotor, titanium or aluminium impeller, magnetic or foil bearings, integrated high-frequency drive.</p>
      </article>
      <article class="card">
        <div class="icon">▤</div>
        <h3>Air path</h3>
        <p>Inlet filter and silencer, discharge silencer, check valve, flexible connectors, anti-surge recycle line where the duty needs it.</p>
      </article>
      <article class="card">
        <div class="icon">⌁</div>
        <h3>Control</h3>
        <p>Local HMI, VFD, surge and overspeed protection, Modbus TCP / Ethernet to the plant system, optional remote access.</p>
      </article>
      <article class="card">
        <div class="icon">▣</div>
        <h3>Mechanical</h3>
        <p>Common baseframe, spring isolators, anchor plan, lifting points, weatherproof canopy on outdoor units.</p>
      </article>
      <article class="card">
        <div class="icon">◷</div>
        <h3>Documentation</h3>
        <p>General arrangement, wiring diagram, I/O list, commissioning procedure, O&amp;M manual — English, with the quotation.</p>
      </article>
      <article class="card">
        <div class="icon">✦</div>
        <h3>Services</h3>
        <p>Selection and system design, commissioning support, remote diagnostics, spare parts and rotor exchange programme.</p>
      </article>
    </div>
  </div>
</section>

<section>
  <div class="wrap grid-2" style="gap:56px;align-items:start">
    <div class="prose">
      <h2>Where they are used</h2>
      <ul>
        <li><strong>Wastewater aeration.</strong> The classic application: continuous duty, wide flow turndown, and the electricity bill is the largest line in the plant budget.</li>
        <li><strong>Coal-mine gas drainage and ventilation.</strong> High suction volume at moderate vacuum, with the flow chasing methane concentration all shift long.</li>
        <li><strong>Paper, chemical and pharmaceutical vacuum.</strong> Dry running matters where the process cannot tolerate oil or sealing water carry-over.</li>
        <li><strong>Power plant FGD oxidation air, cement and steel process air.</strong> Constant pressure, long runs, no tolerance for a gearbox failure.</li>
        <li><strong>Semiconductor and electronics.</strong> Clean vacuum with no hydrocarbon backstreaming.</li>
      </ul>
      <h2>What we do not claim</h2>
      <p>Certification for a specific market — CE, ATEX, EAC, or a mining approval such as MA — is quoted item by item against the target country and application. We do not describe the machines as certified for a market where that approval has not been issued for the delivered configuration.</p>
    </div>
    <div>
      <div class="card">
        <h3>Send us the duty</h3>
        <p class="small" style="margin-bottom:14px">To select a machine we need five numbers and one description:</p>
        <ul class="checks">
          <li>Flow or suction volume (m³/min or Nm³/h)</li>
          <li>Pressure rise or working vacuum (kPa)</li>
          <li>Inlet temperature, altitude, relative humidity</li>
          <li>Gas composition — air, methane mix, solvent vapour, dust load</li>
          <li>Hours per year and ambient conditions on site</li>
        </ul>
        <p style="margin-top:16px"><a class="btn" href="contact.html">Request a selection</a></p>
      </div>
    </div>
  </div>
</section>

<section class="tight">
  <div class="wrap">
    <div class="band">
      <div>
        <h2>Replace the water ring, keep the pipework.</h2>
        <p>Send the nameplate of the machine you are running now. We answer with the equivalent levitated model, its power at your duty, and the annual kWh difference.</p>
      </div>
      <a class="btn light" href="contact.html">Ask for a comparison</a>
    </div>
  </div>
</section>
"""
# ------------------------------------------------------------------ EN: mobile pumps

MOBILE_EN = """
{crumbs}
<section class="page-head">
  <div class="wrap">
    <p class="eyebrow">Portable pump · axial-flux canned motor</p>
    <h1>A 2.7 kg pump that lifts water 62 metres</h1>
    <p class="lead">Axial-flux motor and impeller built into one sealed body: 8,000 L/h, 62 m of head, IP68, no shaft seal and no oil. Carried by hand, run from a 72 V battery pack, a vehicle supply or the mains, and adjusted from a phone.</p>
  </div>
</section>

<section>
  <div class="wrap grid-2" style="gap:56px;align-items:center">
    <div>
      <figure class="lead-photo">
        <img src="assets/img/portable-pump-hero.jpg" alt="Portable axial-flux pump unit in use outdoors" loading="eager">
        <figcaption>120 × 120 × 90 mm, 2.7 kg without cable — one hand, one hose.</figcaption>
      </figure>
    </div>
    <div class="prose">
      <h2>The seal is the part that fails</h2>
      <p>On a conventional pump the shaft passes through the casing, and a mechanical seal keeps the water out of the motor. That seal is the first thing to wear, the first thing to leak, and the reason a small pump cannot be left running unattended.</p>
      <p>This unit has no shaft. The rotor turns inside a thin can, the stator sits outside it, and the water never meets anything that can leak. No seal, no lubricant, no drip tray.</p>
      <div class="callout"><p><strong>Dry-run tolerant, corrosion resistant.</strong> Impeller and housing in high-strength PPS, bearings in silicon carbide. Handles coolants and mildly aggressive fluids without a coating that can flake.</p></div>
    </div>
  </div>
</section>

<section class="alt">
  <div class="wrap">
    <div class="sec-head">
      <p class="eyebrow">Specification</p>
      <h2>One model, one set of numbers</h2>
    </div>
    <div class="table-wrap">
      <table>
        <thead><tr><th>Parameter</th><th>Value</th><th>Parameter</th><th>Value</th></tr></thead>
        <tbody>
          <tr><td>Rated power</td><td>2 kW</td><td>Voltage</td><td>220 / 110 / 72 V</td></tr>
          <tr><td>Maximum flow</td><td>8,000 L/h (8 m³/h)</td><td>Maximum head</td><td>62 m (two units in series: 124 m)</td></tr>
          <tr><td>Rated speed</td><td>7,500 rpm</td><td>Protection</td><td>IP68 — submersible</td></tr>
          <tr><td>Dimensions</td><td>120 × 120 × 90 mm</td><td>Weight</td><td>2.7 kg without cable</td></tr>
          <tr><td>Noise at rated load</td><td>&lt; 65 dB</td><td>Medium temperature</td><td>−20 to +60 °C</td></tr>
          <tr><td>Ambient</td><td>−20 to +60 °C, RH &lt; 90%</td><td>Connections</td><td>RC 3/4 internal, RC 1" external</td></tr>
          <tr><td>Impeller / housing</td><td>High-strength PPS</td><td>Bearings</td><td>Silicon carbide</td></tr>
          <tr><td>Air tightness</td><td>1 MPa test, leakage &lt; 1 mL/min</td><td>Control</td><td>Variable speed, WiFi app</td></tr>
        </tbody>
      </table>
    </div>
    <p class="small" style="margin-top:16px">Performance is quoted at the rated voltage. Flow and head trade against each other along the published curve — send the duty point and we will confirm the operating position before you order.</p>
  </div>
</section>

<section>
  <div class="wrap">
    <div class="sec-head">
      <p class="eyebrow">Why it is built this way</p>
      <h2>Fewer parts, fewer failures</h2>
    </div>
    <div class="grid-3">
      <article class="card"><div class="icon">◍</div><h3>No shaft, no seal</h3><p>The rotor is the only moving part and it is fully enclosed. Nothing to repack, nothing to drip, no seal to replace on a schedule.</p></article>
      <article class="card"><div class="icon">⌁</div><h3>Axial-flux motor</h3><p>A flat motor of high power density built into the pump body — that is why a 2 kW machine fits in the palm of your hand.</p></article>
      <article class="card"><div class="icon">▤</div><h3>Sealed for immersion</h3><p>IP68 rated, so it can be dropped into a tank as a submersible, or bolted into a line as a booster, with the same unit.</p></article>
      <article class="card"><div class="icon">◷</div><h3>Variable speed</h3><p>Integrated controller with stepless adjustment. Turn the flow down instead of throttling a valve and wasting the difference.</p></article>
      <article class="card"><div class="icon">✦</div><h3>Phone control</h3><p>WiFi app for start/stop, speed and irrigation schedules — useful where the pump is somewhere you would rather not walk to.</p></article>
      <article class="card"><div class="icon">◎</div><h3>Quiet</h3><p>Under 65 dB at rated load, with no gear mesh and no cooling fan screaming at 7,500 rpm.</p></article>
    </div>
  </div>
</section>

<section class="alt">
  <div class="wrap">
    <div class="sec-head">
      <p class="eyebrow">Applications</p>
      <h2>Where a hand-carried pump earns its place</h2>
      <p class="lead">Six duties this unit was built for — and the reason it is kept charged and ready rather than stored in a shed.</p>
    </div>
    <div class="grid-3">
      <article class="card"><h3>Vehicle and outdoor</h3><p>Runs from a portable power station in the truck or camper. Water transfer, washing down, drawing from a stream or tank.</p></article>
      <article class="card"><h3>Irrigation</h3><p>Factories, gardens, estates, farms, schools, hospitals, nurseries, livestock. Scheduled watering from the app, with flushing duties in between.</p></article>
      <article class="card"><h3>Food and beverage</h3><p>Clean fluids — milk, soy, drinks — where a leaking seal would be a contamination event rather than a maintenance ticket.</p></article>
      <article class="card"><h3>Pressure boosting</h3><p>Wells, hillside villas, guesthouses, upper floors and hot-water circulation. One unit gives 62 m; two in series give 124 m.</p></article>
      <article class="card"><h3>Marine</h3><p>Deck and hold washing, bilge transfer, auxiliary fire duty on small and medium vessels.</p></article>
      <article class="card"><h3>Emergency response</h3><p>Narrow lanes and rural sites a fire appliance cannot reach, and post-flood flushing of silt and contamination.</p></article>
    </div>
  </div>
</section>

<section>
  <div class="wrap grid-2" style="gap:56px;align-items:start">
    <div class="prose">
      <h2>One unit, four ways to install</h2>
      <ul>
        <li><strong>Submersible.</strong> Dropped into a tank, sump or well — IP68 and small enough to pass a manhole.</li>
        <li><strong>In-line.</strong> Bolted into pipework as a transfer or circulation pump.</li>
        <li><strong>Booster.</strong> Added to an existing supply to lift pressure at the top of a building.</li>
        <li><strong>Portable set.</strong> Carried with a battery pack and a hose reel as a standalone unit.</li>
      </ul>
      <p>The same body works in all four because there is no seal to orient and no oil to keep level. Vertical or horizontal, it does not care.</p>
    </div>
    <div>
      <figure class="lead-photo">
        <img src="assets/img/portable-pump-1.jpg" alt="Portable pump unit close-up" loading="lazy">
      </figure>
      <div class="card" style="margin-top:20px">
        <h3>Supply scope</h3>
        <ul class="checks">
          <li>Pump unit with integrated controller</li>
          <li>Mains adapter, or 72 V DC lead for battery operation</li>
          <li>Hose tails to RC 3/4 and RC 1"</li>
          <li>WiFi app setup and operating manual</li>
          <li>Spare parts: impeller, bearing set, controller</li>
        </ul>
      </div>
    </div>
  </div>
</section>

<section class="tight">
  <div class="wrap">
    <div class="band">
      <div>
        <h2>Tell us the lift and the volume.</h2>
        <p>Height from water level to outlet, litres per hour you need, and what power is available. We will confirm whether one unit does it or two in series.</p>
      </div>
      <a class="btn light" href="contact.html">Request a configuration</a>
    </div>
  </div>
</section>
"""


# ------------------------------------------------------------------ EN: edge AI

EDGE_EN = """
{crumbs}
<section class="page-head">
  <div class="wrap">
    <p class="eyebrow">Edge intelligence · nothing leaves the plant</p>
    <h1>An industrial AI agent that runs on site</h1>
    <p class="lead">A self-contained appliance running a 27-billion-parameter language model and the OpenClaw agent runtime locally. Four concurrent sessions, 40+ tokens per second in total, about 58 W average — no cloud account, no data leaving the network.</p>
  </div>
</section>

<section>
  <div class="wrap">
    <div class="kpi-row" style="margin-top:0">
      <div class="kpi"><b>27B</b><span>Language model resident on the appliance</span></div>
      <div class="kpi"><b>4</b><span>Concurrent agent sessions</span></div>
      <div class="kpi"><b>40+</b><span>Tokens per second, aggregate</span></div>
      <div class="kpi"><b>58 W</b><span>Average system power, measured</span></div>
    </div>
  </div>
</section>

<section class="alt">
  <div class="wrap grid-2" style="gap:56px;align-items:start">
    <div class="prose">
      <h2>Why on site instead of in a cloud</h2>
      <p>Plant data — P&amp;ID sets, maintenance logs, meter readings, operator notes, photographs of a failed bearing — is exactly the data that a security review will not let out of the building. An agent that needs the internet to answer a question about a pump is an agent that will not be deployed.</p>
      <p>This appliance answers locally. The model, the documents, the conversation history and the tool results all stay inside the plant network. There is no per-token bill and no dependency on a vendor staying in business or keeping an API online.</p>
      <div class="callout"><p><strong>Measured, not estimated.</strong> The performance figures on this page were recorded on our reference unit: 4-way concurrent generation at 8K context per session, 10.4–10.9 tokens/s per stream, NPU utilisation reaching 99%, hottest point 52 °C, about 1.5 GB of the 15.6 GB memory in use.</p></div>
      <h2>What the agent actually does</h2>
      <ul>
        <li><strong>Answers from your documents.</strong> Manuals, commissioning reports, contracts, test sheets — indexed locally, answered with the source cited.</li>
        <li><strong>Reads what is on site.</strong> Photographs and scanned nameplates are read by on-board NPU OCR, so a picture of a pump nameplate becomes structured data.</li>
        <li><strong>Runs scheduled work.</strong> Daily energy summaries, shift handover notes, meter comparisons, overdue-maintenance lists — generated and pushed to the people who need them.</li>
        <li><strong>Talks to the systems you already have.</strong> Modbus, MQTT and HTTP interfaces for meters, PLCs and monitoring platforms.</li>
        <li><strong>Connects to your messaging.</strong> WeChat, Feishu, Telegram or email — the same agent, reachable from a phone on the plant network.</li>
      </ul>
    </div>
    <div>
      <div class="card" style="background:#0c1a26;border-color:#0c1a26;color:#fff">
        <p class="tag" style="color:#ffb08a">Configuration</p>
        <h3 style="color:#fff">Reference hardware</h3>
        <div class="kv" style="border-color:rgba(255,255,255,.14)"><span>Host</span><b>RK3588, 8-core</b></div>
        <div class="kv" style="border-color:rgba(255,255,255,.14)"><span>Accelerators</span><b>4 × RK1828</b></div>
        <div class="kv" style="border-color:rgba(255,255,255,.14)"><span>AI throughput</span><b>20 TOPS INT8 / 40 TOPS INT4 per card</b></div>
        <div class="kv" style="border-color:rgba(255,255,255,.14)"><span>Memory</span><b>15.6 GB visible, 4 × 5 GB stacked</b></div>
        <div class="kv" style="border-color:rgba(255,255,255,.14)"><span>Network</span><b>2 × GbE, optional 4G/5G</b></div>
        <div class="kv" style="border-color:rgba(255,255,255,.14)"><span>Power</span><b>12–36 V DC, ~58 W average</b></div>
        <div class="kv" style="border:0"><span>Enclosure</span><b>Desktop or DIN-rail, fanless option</b></div>
      </div>
      <div class="card" style="margin-top:20px">
        <h3>Software layer</h3>
        <ul class="checks">
          <li>OpenClaw agent runtime, running offline</li>
          <li>Local model serving, 27B quantised to W4A16</li>
          <li>Local document index with citations</li>
          <li>NPU OCR for photographs and scans</li>
          <li>Scheduled tasks, audit log, role-based access</li>
        </ul>
      </div>
    </div>
  </div>
</section>

<section>
  <div class="wrap">
    <div class="sec-head">
      <p class="eyebrow">Measured performance</p>
      <h2>Reference unit, four sessions at once</h2>
      <p class="lead">27B model, W4A16 quantisation, 8K context per session, four sessions generating simultaneously.</p>
    </div>
    <div class="table-wrap">
      <table>
        <thead><tr><th>Metric</th><th>Measured</th><th>Note</th></tr></thead>
        <tbody>
          <tr><td>Time to first token</td><td>0.9–2.6 s</td><td>Per session, four running in parallel</td></tr>
          <tr><td>Decode speed per session</td><td>10.4–10.9 tokens/s</td><td>Stable across the run</td></tr>
          <tr><td>Aggregate throughput</td><td>40+ tokens/s</td><td>Four sessions combined</td></tr>
          <tr><td>NPU utilisation</td><td>83 → 99%</td><td>Saturates as all four streams fill</td></tr>
          <tr><td>Memory in use</td><td>1.2–1.6 GB of 15.6 GB</td><td>Leaves headroom for a larger context</td></tr>
          <tr><td>Temperature</td><td>32–52 °C</td><td>Host 32–41 °C, accelerators 38–52 °C</td></tr>
          <tr><td>Long-context mode</td><td>32K per session, 2 sessions</td><td>About 6.5 GB per card at 32K</td></tr>
        </tbody>
      </table>
    </div>
    <p class="small" style="margin-top:16px">A single session runs faster than 10 tokens/s; the figure above is the per-stream rate with four sessions sharing the hardware. Context length trades against concurrency — the appliance is configured for whichever your workload needs.</p>
  </div>
</section>

<section class="alt">
  <div class="wrap">
    <div class="sec-head">
      <p class="eyebrow">Industrial use</p>
      <h2>Where an on-site agent earns its place</h2>
    </div>
    <div class="grid-3">
      <article class="card">
        <div class="icon">◍</div>
        <h3>Equipment condition</h3>
        <p>Vibration and acoustic data ingested locally, trend summaries and anomaly notes written in plain language for the maintenance team.</p>
      </article>
      <article class="card">
        <div class="icon">▤</div>
        <h3>Energy accounting</h3>
        <p>Meter data collected, specific energy calculated per unit of output, and the weekly saving report drafted before the meeting.</p>
      </article>
      <article class="card">
        <div class="icon">≋</div>
        <h3>Gas and ventilation</h3>
        <p>Drainage and ventilation readings summarised against limits, with exceptions flagged instead of buried in a spreadsheet.</p>
      </article>
      <article class="card">
        <div class="icon">⌁</div>
        <h3>Maintenance knowledge</h3>
        <p>Manuals, drawings and past work orders searchable in natural language — including photographs of nameplates and damage.</p>
      </article>
      <article class="card">
        <div class="icon">◷</div>
        <h3>Shift reporting</h3>
        <p>Handover notes, production summaries and incident drafts generated from the data the plant already records.</p>
      </article>
      <article class="card">
        <div class="icon">✦</div>
        <h3>Field engineering</h3>
        <p>Selection checks, pump sizing and quotation drafts produced on site, without a connection back to head office.</p>
      </article>
    </div>
  </div>
</section>

<section>
  <div class="wrap grid-2" style="gap:56px;align-items:start">
    <div class="prose">
      <h2>Deployment</h2>
      <p>The appliance is delivered configured, with the model loaded and the agent runtime installed. Commissioning is a network drop and an account setup, not a software project.</p>
      <ul>
        <li>Runs fully offline; internet is optional, for updates and remote support only</li>
        <li>Local accounts and role-based access, with an audit log of every agent action</li>
        <li>Document ingestion done on site — files are not uploaded anywhere</li>
        <li>Optional site-to-site VPN for vendor support, enabled by the plant when needed</li>
        <li>Model and knowledge base can be updated from a USB device, no network required</li>
      </ul>
    </div>
    <div class="prose">
      <h2>What it is not</h2>
      <p>It is not a replacement for a plant historian, a DCS or a safety system. It reads, summarises and drafts; it does not close a control loop, and it is not connected to protection logic.</p>
      <p>It is also not an unlimited model. A 27B model on edge silicon is a capable assistant for engineering and reporting work — it is not a frontier model, and we do not present it as one. The value is that it runs here, on your data, at a fixed cost, with no network dependency.</p>
    </div>
  </div>
</section>

<section class="tight">
  <div class="wrap">
    <div class="band">
      <div>
        <h2>Bring a laptop to the plant, leave with a working agent.</h2>
        <p>Tell us the documents you want it to read and the questions you want answered. We will demonstrate it on your own files, offline.</p>
      </div>
      <a class="btn light" href="contact.html">Arrange a demonstration</a>
    </div>
  </div>
</section>
"""
# ------------------------------------------------------------------ ZH: 磁悬浮/空浮

MAGLEV_ZH = """
{crumbs}
<section class="page-head">
  <div class="wrap">
    <p class="eyebrow">高速透平机械 · 无油</p>
    <h1>悬在磁场与气膜上的鼓风机与真空泵</h1>
    <p class="lead">高速永磁电机直驱，磁悬浮或空气悬浮轴承承载，无齿轮箱、无润滑油、无机械接触。等温效率 70~80%，同样工况下水环泵/罗茨风机只有 30~65%。</p>
  </div>
</section>

<section>
  <div class="wrap grid-2" style="gap:56px;align-items:start">
    <div class="prose">
      <h2>电都耗在哪里</h2>
      <p>风量和真空度按立方米每分钟选型，电费却按千瓦连续支付。水环真空泵三到五成轴功率耗在搅动密封水上；罗茨风机则把功率丢在随磨损不断变大的叶轮间隙里。</p>
      <p>悬浮转子把这两项损失一起去掉：唯一运动件是叶轮，它浮在磁场或气膜上，直到停机落座之前，没有任何零件互相接触。</p>
      <div class="table-wrap" style="margin:26px 0">
        <table>
          <thead><tr><th>机型</th><th>典型效率</th><th>工作液</th><th>易损件</th></tr></thead>
          <tbody>
            <tr><td>水环真空泵</td><td>30~50%</td><td>需连续供水</td><td>叶轮、分配器、轴</td></tr>
            <tr><td>罗茨风机 / 湿式罗茨真空泵</td><td>50~65%</td><td>湿式需喷水</td><td>转子、齿轮、密封</td></tr>
            <tr><td><strong>悬浮转子透平鼓风机 / 真空泵</strong></td><td><strong>70~80%</strong></td><td>无（干运行）</td><td>仅进气过滤器</td></tr>
          </tbody>
        </table>
      </div>
      <p>250 kW 的工况，效率从 55% 提到 75%，轴功率就差约 120 kW——按年运行 8000 小时算，接近一百万度电，还没算省下来的维修费。</p>
      <div class="callout"><p><strong>无油、无水、无齿轮箱。</strong>设备清单里少了油站、油冷却器、供水系统和齿轮啮合噪声，维修计划里也一并少了。</p></div>
    </div>
    <div>
      <div class="card">
        <h3>关键指标</h3>
        <ul class="checks">
          <li>风量 20~400 m³/min，压升 40~100 kPa（鼓风机）</li>
          <li>真空：单级 −58 kPa，双级 −75 kPa</li>
          <li>等温效率 70~80%，较被替换机型节电 20~35%</li>
          <li>变频调速 45~100%，内置喘振保护与防喘回流</li>
          <li>标配 Modbus TCP / 以太网远程监控</li>
        </ul>
      </div>
      <div class="card" style="margin-top:20px;background:#0c1a26;border-color:#0c1a26;color:#fff">
        <p class="tag" style="color:#ffb08a">工况对标</p>
        <h3 style="color:#fff">煤矿瓦斯抽采</h3>
        <p style="color:#c6d6df">替代 60 kPa 湿式罗茨抽采站：磁悬浮透平真空泵按 70%、罗茨按 55% 计，同等抽气量下轴功率低 21%；200~750 m³/min 档位，单台年节电 34~126 万 kWh。</p>
        <div class="kv" style="border-color:rgba(255,255,255,.14)"><span>抽气量</span><b>200~750 m³/min</b></div>
        <div class="kv" style="border-color:rgba(255,255,255,.14)"><span>工作负压</span><b>−60 kPa</b></div>
        <div class="kv" style="border:0"><span>典型节电</span><b style="color:#7ee2c4">轴功率 21%</b></div>
      </div>
    </div>
  </div>
</section>

<section class="alt">
  <div class="wrap">
    <div class="sec-head">
      <p class="eyebrow">两条轴承路线</p>
      <h2>大功率走磁悬浮，紧凑场合走空气悬浮</h2>
      <p class="lead">两者都无油。分界看功率、连续运行要求，以及你对转子位置控制的要求有多细。</p>
    </div>
    <div class="grid-2">
      <article class="card prod-card" style="padding:28px">
        <div class="card-body" style="padding:0">
          <p class="tag">MB 系列 · 主动磁悬浮</p>
          <h3>磁悬浮鼓风机 / 真空泵</h3>
          <p>五轴主动磁悬浮轴承 + 数字位置控制。转子位移、振动、温度全程在线测量并上报——机器自己报状态，而不是突然停给你看。</p>
          <ul class="checks">
            <li>电机 30~400 kW，风量 20~400 m³/min</li>
            <li>压升 40~100 kPa；真空单级 −58 kPa / 双级 −75 kPa</li>
            <li>仅在停机时落座保护轴承</li>
            <li>状态数据可接入厂区 DCS</li>
          </ul>
        </div>
      </article>
      <article class="card prod-card" style="padding:28px">
        <div class="card-body" style="padding:0">
          <p class="tag">AB 系列 · 空气悬浮</p>
          <h3>空浮鼓风机</h3>
          <p>弹性箔片轴承靠转子自身带起的气膜承载，无控制器、无电磁铁、无后备轴承电子件——结构最简的无油方案，中等功率下全生命周期成本最低。</p>
          <ul class="checks">
            <li>电机 30~250 kW，风量 20~120 m³/min</li>
            <li>压升 40~80 kPa</li>
            <li>无轴承控制柜，箔片上直接起浮</li>
            <li>适合曝气与低压工艺风</li>
          </ul>
        </div>
      </article>
    </div>
  </div>
</section>

<section>
  <div class="wrap">
    <div class="sec-head">
      <p class="eyebrow">供货范围</p>
      <h2>标准型谱</h2>
      <p class="lead">下表是我们报价的覆盖范围，具体型号、叶轮切割与电机功率按你的工况点确定——风量、压升或真空度、进气温度、海拔、气体成分。</p>
    </div>
    <div class="table-wrap">
      <table>
        <thead><tr><th>系列</th><th>用途</th><th>风量 / 抽气量</th><th>压力</th><th>电机</th></tr></thead>
        <tbody>
          <tr><td>MB 鼓风机</td><td>工艺风、曝气、输送</td><td>30~400 m³/min</td><td>压升 40~100 kPa</td><td>30~400 kW</td></tr>
          <tr><td>AB 鼓风机</td><td>曝气、低压风</td><td>20~120 m³/min</td><td>压升 40~80 kPa</td><td>30~250 kW</td></tr>
          <tr><td>MB 真空泵（单级）</td><td>真空、过滤、瓦斯抽采</td><td>100~750 m³/min</td><td>至 −58 kPa</td><td>75~400 kW</td></tr>
          <tr><td>MB 真空泵（双级）</td><td>高真空工艺</td><td>100~750 m³/min</td><td>至 −75 kPa</td><td>110~450 kW</td></tr>
        </tbody>
      </table>
    </div>
    <p class="small" style="margin-top:16px">含液滴或粉尘的气体需在机前配置分离器与过滤装置，随主机一并报价，不默认"现场应该有"。</p>
  </div>
</section>

<section class="alt">
  <div class="wrap">
    <div class="sec-head">
      <p class="eyebrow">供货内容</p>
      <h2>到货即一套系统</h2>
    </div>
    <div class="grid-3">
      <article class="card"><div class="icon">◍</div><h3>主机</h3><p>高速永磁转子、钛合金或铝合金叶轮、磁悬浮或箔片轴承、一体化高频驱动器。</p></article>
      <article class="card"><div class="icon">▤</div><h3>气路</h3><p>进气过滤器与消声器、排气消声器、止回阀、柔性接头，工况需要时配防喘回流管路。</p></article>
      <article class="card"><div class="icon">⌁</div><h3>控制</h3><p>本地触摸屏、变频器、喘振与超速保护、Modbus TCP / 以太网接口，可选远程访问。</p></article>
      <article class="card"><div class="icon">▣</div><h3>机械</h3><p>公共底座、弹簧减振器、地脚图、吊点，室外机型配防雨罩。</p></article>
      <article class="card"><div class="icon">◷</div><h3>文件</h3><p>总图、电气原理图、I/O 清单、调试大纲、运行维护手册，随报价提供。</p></article>
      <article class="card"><div class="icon">✦</div><h3>服务</h3><p>选型与系统设计、调试支持、远程诊断、备件与转子返修计划。</p></article>
    </div>
  </div>
</section>

<section>
  <div class="wrap grid-2" style="gap:56px;align-items:start">
    <div class="prose">
      <h2>用在哪里</h2>
      <ul>
        <li><strong>污水处理曝气。</strong>典型连续工况、流量调节范围宽，电费是厂里最大一笔支出。</li>
        <li><strong>煤矿瓦斯抽采与通风。</strong>中等负压下大抽气量，风量整天跟着甲烷浓度跑。</li>
        <li><strong>造纸、化工、制药真空。</strong>工艺不能容忍油或密封水带出的场合，干运行就是刚需。</li>
        <li><strong>电厂脱硫氧化风、水泥与钢铁工艺风。</strong>定压长周期运行，容不得齿轮箱出事。</li>
        <li><strong>半导体与电子。</strong>洁净真空，无碳氢返流。</li>
      </ul>
      <h2>我们不承诺什么</h2>
      <p>目标市场认证——CE、ATEX、EAC，或矿用产品安全标志（MA）——按目标国家与具体应用逐项报价。对交付配置尚未取得批准的认证，我们不会在页面上写成"已通过"。</p>
    </div>
    <div>
      <div class="card">
        <h3>发工况给我们</h3>
        <p class="small" style="margin-bottom:14px">选型需要五个数字和一段描述：</p>
        <ul class="checks">
          <li>风量或抽气量（m³/min 或 Nm³/h）</li>
          <li>压升或工作真空度（kPa）</li>
          <li>进气温度、海拔、相对湿度</li>
          <li>气体成分——空气、瓦斯混合、溶剂蒸气、含尘量</li>
          <li>年运行小时与现场环境</li>
        </ul>
        <p style="margin-top:16px"><a class="btn" href="contact.html">提交选型需求</a></p>
      </div>
    </div>
  </div>
</section>

<section class="tight">
  <div class="wrap">
    <div class="band">
      <div>
        <h2>换掉水环泵，管路不用动。</h2>
        <p>把现用机组的铭牌发给我们。回你对应悬浮机型、该工况下的功率，以及一年省多少度电。</p>
      </div>
      <a class="btn light" href="contact.html">索取对比测算</a>
    </div>
  </div>
</section>
"""


# ------------------------------------------------------------------ ZH: 移动式便携水泵

MOBILE_ZH = """
{crumbs}
<section class="page-head">
  <div class="wrap">
    <p class="eyebrow">便携泵 · 轴向磁通屏蔽电机</p>
    <h1>2.7 公斤，把水送上去 62 米</h1>
    <p class="lead">轴向磁通电机与叶轮做在一个密封体内：8000 L/h、扬程 62 米、IP68，无轴、无轴封、无油。单手可提，可接 72 V 电池包、车载电源或市电，手机调参。</p>
  </div>
</section>

<section>
  <div class="wrap grid-2" style="gap:56px;align-items:center">
    <div>
      <figure class="lead-photo">
        <img src="assets/img/portable-pump-hero.jpg" alt="户外使用中的便携式轴向磁通泵" loading="eager">
        <figcaption>120 × 120 × 90 mm，不含电缆 2.7 kg——一只手，一根管。</figcaption>
      </figure>
    </div>
    <div class="prose">
      <h2>最容易坏的，是那道轴封</h2>
      <p>常规泵的轴要穿过泵壳，靠机械密封把水挡在电机外面。这道密封最先磨损、最先渗漏，也是小型泵不敢长期无人值守运行的根源。</p>
      <p>这台泵没有轴。转子在一层薄薄的屏蔽套里转，定子在套外，水碰不到任何会漏的东西——没有轴封、没有润滑油、没有接漏盘。</p>
      <div class="callout"><p><strong>耐干转、耐腐蚀。</strong>叶轮与外壳为高强度 PPS，轴承为碳化硅。可输送冷却液与一般腐蚀性介质，不靠涂层，不存在涂层脱落的风险。</p></div>
    </div>
  </div>
</section>

<section class="alt">
  <div class="wrap">
    <div class="sec-head">
      <p class="eyebrow">参数</p>
      <h2>一个型号，一组数字</h2>
    </div>
    <div class="table-wrap">
      <table>
        <thead><tr><th>参数</th><th>数值</th><th>参数</th><th>数值</th></tr></thead>
        <tbody>
          <tr><td>额定功率</td><td>2 kW</td><td>额定电压</td><td>220 / 110 / 72 V</td></tr>
          <tr><td>最大流量</td><td>8000 L/h（8 m³/h）</td><td>最高扬程</td><td>62 m（两级串联 124 m）</td></tr>
          <tr><td>额定转速</td><td>7500 rpm</td><td>防护等级</td><td>IP68，可潜水</td></tr>
          <tr><td>外形尺寸</td><td>120 × 120 × 90 mm</td><td>重量</td><td>2.7 kg（不含电缆）</td></tr>
          <tr><td>额定负载噪声</td><td>&lt; 65 dB</td><td>介质温度</td><td>−20 ~ +60 ℃</td></tr>
          <tr><td>环境条件</td><td>−20 ~ +60 ℃，湿度 &lt;90%</td><td>接口</td><td>内螺纹 RC 3/4、外螺纹 RC 1"</td></tr>
          <tr><td>叶轮 / 外壳</td><td>高强度 PPS</td><td>轴承</td><td>碳化硅</td></tr>
          <tr><td>气密性</td><td>1 MPa 测试，泄漏 &lt;1 mL/min</td><td>控制</td><td>变频无级调速，手机 APP（WiFi）</td></tr>
        </tbody>
      </table>
    </div>
    <p class="small" style="margin-top:16px">性能按额定电压给出；流量与扬程沿曲线此消彼长，请把工况点发给我们，确认实际工作位置后再下单。</p>
  </div>
</section>

<section>
  <div class="wrap">
    <div class="sec-head">
      <p class="eyebrow">为什么这样做</p>
      <h2>零件少，故障就少</h2>
    </div>
    <div class="grid-3">
      <article class="card"><div class="icon">◍</div><h3>无轴、无轴封</h3><p>转子是唯一运动件，且完全封闭。不用盘根、不会滴漏，也没有需要定期更换的密封。</p></article>
      <article class="card"><div class="icon">⌁</div><h3>轴向磁通电机</h3><p>扁平结构、功率密度高，直接做进泵体——这就是 2 kW 机组能握在手里的原因。</p></article>
      <article class="card"><div class="icon">▤</div><h3>可潜水</h3><p>IP68，同一台机器既可作为潜水泵丢进水池，也可串进管路作增压泵。</p></article>
      <article class="card"><div class="icon">◷</div><h3>变频调速</h3><p>集成变频控制器，无级调速。需要小流量时降转速，而不是关小阀门白白节流。</p></article>
      <article class="card"><div class="icon">✦</div><h3>手机控制</h3><p>WiFi APP 控制启停、转速与浇灌计划——泵装在你不愿意跑一趟的地方时最有用。</p></article>
      <article class="card"><div class="icon">◎</div><h3>安静</h3><p>额定负载噪声低于 65 dB，没有齿轮啮合声，也没有在 7500 rpm 上尖叫的风扇。</p></article>
    </div>
  </div>
</section>

<section class="alt">
  <div class="wrap">
    <div class="sec-head">
      <p class="eyebrow">应用场景</p>
      <h2>一只手提得动的泵，用在哪</h2>
      <p class="lead">六个为它设计的用途——也是它应当保持满电待用、而不是锁在库房里的理由。</p>
    </div>
    <div class="grid-3">
      <article class="card"><h3>户外与车载</h3><p>配移动电源使用，卡车、房车、自驾取水与冲洗；也能从溪流、水罐直接抽取。</p></article>
      <article class="card"><h3>浇灌</h3><p>工厂、花园、小区、农场、学校、医院、苗圃、养殖场；APP 可设自动浇灌，兼顾冲洗。</p></article>
      <article class="card"><h3>食品行业</h3><p>牛奶、豆浆、饮料等洁净流体——这里漏一次是污染事件，不是一张维修单。</p></article>
      <article class="card"><h3>增压</h3><p>井水、山区别墅、民宿、高楼供水与热水循环。单泵 62 m，两级串联 124 m。</p></article>
      <article class="card"><h3>船用</h3><p>中小型船舶取水、甲板与船舱冲洗，兼作辅助消防。</p></article>
      <article class="card"><h3>应急</h3><p>消防车进不去的乡村窄巷第一时间处置；水灾后快速清除冲洗淤泥与污染。</p></article>
    </div>
  </div>
</section>

<section>
  <div class="wrap grid-2" style="gap:56px;align-items:start">
    <div class="prose">
      <h2>一台机器，四种装法</h2>
      <ul>
        <li><strong>潜水泵。</strong>放进水池、水仓或井里——IP68，体积小到能过人孔。</li>
        <li><strong>管道泵。</strong>串进管路，做输送或循环。</li>
        <li><strong>增压泵。</strong>接在既有供水上，把楼顶压力补起来。</li>
        <li><strong>便携机组。</strong>配电池包与软管卷盘，随车随人走。</li>
      </ul>
      <p>四种装法共用同一个机体：没有需要定方位的轴封，也没有要保持油位的油室，立着装卧着装都一样。</p>
    </div>
    <div>
      <figure class="lead-photo">
        <img src="assets/img/portable-pump-1.jpg" alt="便携泵产品细节" loading="lazy">
      </figure>
      <div class="card" style="margin-top:20px">
        <h3>供货内容</h3>
        <ul class="checks">
          <li>泵体（含集成控制器）</li>
          <li>市电适配器，或 72 V 直流电池线</li>
          <li>RC 3/4 与 RC 1" 配套接头</li>
          <li>WiFi APP 使用说明与操作手册</li>
          <li>备件：叶轮、轴承组、控制器</li>
        </ul>
      </div>
    </div>
  </div>
</section>

<section class="tight">
  <div class="wrap">
    <div class="band">
      <div>
        <h2>告诉我扬程和水量。</h2>
        <p>水面到出水口的高度、每小时要多少升、现场有什么电源。我们回复一台够不够，还是两台串联。</p>
      </div>
      <a class="btn light" href="contact.html">索取配置方案</a>
    </div>
  </div>
</section>
"""


# ------------------------------------------------------------------ ZH: 工业智能体

EDGE_ZH = """
{crumbs}
<section class="page-head">
  <div class="wrap">
    <p class="eyebrow">边缘智能 · 数据不出厂</p>
    <h1>装在厂里的工业智能体</h1>
    <p class="lead">一台独立设备，本地运行 270 亿参数语言模型和内嵌 OpenClaw 智能体运行时。四路会话并发、合计 40+ token/s、平均功耗约 58 W——不需要云账号，数据不离开厂内网络。</p>
  </div>
</section>

<section>
  <div class="wrap">
    <div class="kpi-row" style="margin-top:0">
      <div class="kpi"><b>27B</b><span>常驻本机的语言模型</span></div>
      <div class="kpi"><b>4 路</b><span>可同时服务的智能体会话</span></div>
      <div class="kpi"><b>40+</b><span>token/s（四路合计）</span></div>
      <div class="kpi"><b>58 W</b><span>整机平均功耗（实测）</span></div>
    </div>
  </div>
</section>

<section class="alt">
  <div class="wrap grid-2" style="gap:56px;align-items:start">
    <div class="prose">
      <h2>为什么放在现场，而不是放到云上</h2>
      <p>厂里的数据——P&amp;ID 图、检修记录、电表读数、运行日志、拍下的损坏轴承照片——恰恰是安全评审不肯放出门的那批数据。一个必须联网才能回答"这台泵什么型号"的助手，最终不会被部署。</p>
      <p>这台设备在本地回答。模型、文档、对话记录、工具调用结果，全部留在厂内网络里。没有按 token 计费，也不依赖某家厂商是否还在经营、接口是否还开着。</p>
      <div class="callout"><p><strong>实测，不是估算。</strong>本页数据取自我们的参考机：四路并发生成、每路 8K 上下文，单路 10.4~10.9 token/s，NPU 占用爬到 99%，最高温度 52 ℃，内存 15.6 GB 中仅用约 1.5 GB。</p></div>
      <h2>它具体干什么</h2>
      <ul>
        <li><strong>基于你的文档回答。</strong>手册、调试报告、合同、试验记录在本机建索引，回答时给出出处。</li>
        <li><strong>看得懂现场的资料。</strong>照片与扫描件由机载 NPU 做 OCR——拍一张泵铭牌，就变成结构化数据。</li>
        <li><strong>按计划自动干活。</strong>每日能耗摘要、交接班记录、电量对比、超期保养清单，生成后推给需要的人。</li>
        <li><strong>接得上现有系统。</strong>提供 Modbus、MQTT、HTTP 接口，对接电表、PLC 与监测平台。</li>
        <li><strong>走你们在用的消息通道。</strong>微信、飞书、Telegram 或邮件——同一个智能体，厂内网络里用手机就能问。</li>
      </ul>
    </div>
    <div>
      <div class="card" style="background:#0c1a26;border-color:#0c1a26;color:#fff">
        <p class="tag" style="color:#ffb08a">配置</p>
        <h3 style="color:#fff">参考硬件</h3>
        <div class="kv" style="border-color:rgba(255,255,255,.14)"><span>主机</span><b>RK3588 八核</b></div>
        <div class="kv" style="border-color:rgba(255,255,255,.14)"><span>加速卡</span><b>4 × RK1828</b></div>
        <div class="kv" style="border-color:rgba(255,255,255,.14)"><span>算力</span><b>单卡 20 TOPS INT8 / 40 TOPS INT4</b></div>
        <div class="kv" style="border-color:rgba(255,255,255,.14)"><span>内存</span><b>可见 15.6 GB（4×5 GB 堆叠）</b></div>
        <div class="kv" style="border-color:rgba(255,255,255,.14)"><span>网络</span><b>2 × 千兆，可选 4G/5G</b></div>
        <div class="kv" style="border-color:rgba(255,255,255,.14)"><span>供电</span><b>12~36 V DC，均值约 58 W</b></div>
        <div class="kv" style="border:0"><span>结构</span><b>台式或导轨安装，可选无风扇</b></div>
      </div>
      <div class="card" style="margin-top:20px">
        <h3>软件层</h3>
        <ul class="checks">
          <li>OpenClaw 智能体运行时，离线运行</li>
          <li>本地模型服务，27B 按 W4A16 量化</li>
          <li>本地文档索引，回答带出处</li>
          <li>NPU OCR，处理照片与扫描件</li>
          <li>定时任务、审计日志、分角色权限</li>
        </ul>
      </div>
    </div>
  </div>
</section>

<section>
  <div class="wrap">
    <div class="sec-head">
      <p class="eyebrow">实测性能</p>
      <h2>参考机 · 四路同时会话</h2>
      <p class="lead">27B 模型，W4A16 量化，每路 8K 上下文，四路同时生成。</p>
    </div>
    <div class="table-wrap">
      <table>
        <thead><tr><th>指标</th><th>实测</th><th>说明</th></tr></thead>
        <tbody>
          <tr><td>首字延迟</td><td>0.9~2.6 s</td><td>四路并行时各路数值</td></tr>
          <tr><td>单路解码速度</td><td>10.4~10.9 token/s</td><td>全程稳定</td></tr>
          <tr><td>合计吞吐</td><td>40+ token/s</td><td>四路合计</td></tr>
          <tr><td>NPU 占用</td><td>83 → 99%</td><td>四路都跑起来后打满</td></tr>
          <tr><td>内存占用</td><td>1.2~1.6 GB / 15.6 GB</td><td>为更长上下文留有余量</td></tr>
          <tr><td>温度</td><td>32~52 ℃</td><td>主机 32~41 ℃，加速卡 38~52 ℃</td></tr>
          <tr><td>长上下文模式</td><td>32K/路，2 路并行</td><td>32K 时单卡约 6.5 GB</td></tr>
        </tbody>
      </table>
    </div>
    <p class="small" style="margin-top:16px">单路独占时速度高于 10 token/s；上表是四路共享硬件时的单路速率。上下文长度与并发数此消彼长，按你的业务形态配置。</p>
  </div>
</section>

<section class="alt">
  <div class="wrap">
    <div class="sec-head">
      <p class="eyebrow">工业场景</p>
      <h2>装在厂里能顶什么用</h2>
    </div>
    <div class="grid-3">
      <article class="card"><div class="icon">◍</div><h3>设备状态</h3><p>振动与声学数据本地采集，趋势摘要和异常说明用人话写给检修班组，不用他们读频谱图。</p></article>
      <article class="card"><div class="icon">▤</div><h3>能耗核算</h3><p>电表数据汇总，按产出计算单耗，周报在开会前就写好。</p></article>
      <article class="card"><div class="icon">≋</div><h3>瓦斯与通风</h3><p>抽采与通风数据对照限值汇总，异常被标出来，而不是埋在表格里。</p></article>
      <article class="card"><div class="icon">⌁</div><h3>检修知识</h3><p>手册、图纸、历史工单用自然语言可查——包括铭牌照片和损坏部位照片。</p></article>
      <article class="card"><div class="icon">◷</div><h3>班次报告</h3><p>交接班记录、生产小结、事件初稿，用厂里已有的数据生成。</p></article>
      <article class="card"><div class="icon">✦</div><h3>现场工程</h3><p>选型核算、泵参数计算、报价草稿在现场就能出，不需要连回总部。</p></article>
    </div>
  </div>
</section>

<section>
  <div class="wrap grid-2" style="gap:56px;align-items:start">
    <div class="prose">
      <h2>部署</h2>
      <p>交付时已完成配置：模型装好、智能体运行时装好。上线只是接一根网线、建一个账号，不是一个软件项目。</p>
      <ul>
        <li>完全离线运行；联网仅用于升级与远程支持，可选</li>
        <li>本地账号与分角色权限，智能体的每一步操作留审计日志</li>
        <li>文档在现场导入建索引，不上传任何地方</li>
        <li>可选站点 VPN，由厂方按需开启用于厂商支持</li>
        <li>模型与知识库可用 U 盘升级，不需要网络</li>
      </ul>
    </div>
    <div class="prose">
      <h2>它不是什么</h2>
      <p>它不替代厂级历史站、DCS 或安全系统。它读、总结、起草；不闭合控制回路，也不接保护逻辑。</p>
      <p>它也不是无限能力的模型。边缘芯片上的 27B 是工程与报告场景里称职的助手，不是顶尖模型，我们不会把它说成顶尖模型。它的价值在于：跑在这里、用你的数据、成本固定、不依赖网络。</p>
    </div>
  </div>
</section>

<section class="tight">
  <div class="wrap">
    <div class="band">
      <div>
        <h2>带台笔记本进厂，带着能用的智能体出来。</h2>
        <p>告诉我你要它读哪些文件、回答哪些问题。我们就在你的文件上、断网演示。</p>
      </div>
      <a class="btn light" href="contact.html">预约演示</a>
    </div>
  </div>
</section>
"""


# ------------------------------------------------------------------ registry

PRODUCTS = [
    {
        "slug": "maglev-blowers.html",
        "en": {
            "title": "Maglev & Air-Foil Bearing Blowers and Vacuum Pumps | DALIAN HONGSHI TECHNOLOGY",
            "desc": "Oil-free high-speed turbo blowers 20-400 m3/min at 40-100 kPa and turbo vacuum pumps to -75 kPa. Magnetic or air-foil bearings, direct-drive PM motor, 70-80% efficiency, 20-35% less power than water-ring or Roots machines.",
            "crumb": "Maglev Blowers",
            "body": MAGLEV_EN,
        },
        "zh": {
            "title": "磁悬浮 / 空浮高压鼓风机与真空泵 | 大连宏实科技",
            "desc": "无油高速透平鼓风机，风量 20~400 m³/min、压升 40~100 kPa；透平真空泵真空度可达 −75 kPa。磁悬浮或空气悬浮轴承、永磁电机直驱，效率 70~80%，较水环泵与罗茨风机节电 20~35%。",
            "crumb": "磁悬浮鼓风机",
            "body": MAGLEV_ZH,
        },
    },
    {
        "slug": "mobile-pumps.html",
        "en": {
            "title": "Portable Axial-Flux Pump — 2 kW, 62 m Head, 2.7 kg | DALIAN HONGSHI TECHNOLOGY",
            "desc": "Hand-carried axial-flux pump: 8,000 L/h, 62 m head (124 m in series), IP68, no shaft seal, no oil. Runs on 220/110/72 V, variable speed, WiFi app control.",
            "crumb": "Portable Pump",
            "body": MOBILE_EN,
        },
        "zh": {
            "title": "便携式轴向磁通水泵｜2 kW · 扬程 62 m · 2.7 kg | 大连宏实科技",
            "desc": "手提式轴向磁通屏蔽泵：8000 L/h、扬程 62 m（两级串联 124 m），IP68 可潜水，无轴封无油，220/110/72 V 供电，变频调速、手机 APP 控制。",
            "crumb": "便携式水泵",
            "body": MOBILE_ZH,
        },
    },
    {
        "slug": "edge-ai.html",
        "en": {
            "title": "Industrial AI Agent Appliance — Edge Inference Box | DALIAN HONGSHI TECHNOLOGY",
            "desc": "Edge appliance running a 27B language model and the OpenClaw agent runtime locally: four concurrent sessions, 40+ tokens/s aggregate, about 58 W. No cloud, no data leaving the plant.",
            "crumb": "Industrial AI Box",
            "body": EDGE_EN,
        },
        "zh": {
            "title": "工业智能体 · 边缘计算盒子（内嵌 OpenClaw）| 大连宏实科技",
            "desc": "本机运行 27B 语言模型与 OpenClaw 智能体运行时：四路并发、合计 40+ token/s、平均功耗约 58 W，数据不出厂，无需云账号。",
            "crumb": "工业智能体",
            "body": EDGE_ZH,
        },
    },
]
