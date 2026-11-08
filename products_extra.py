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
    <h1>Blowers, compressors and vacuum pumps on a levitated shaft</h1>
    <p class="lead">18.5–750 kW centrifugal blowers on magnetic bearings, 15–300 kW air-foil blowers, and air-foil compressors to 500 kPa. No gearbox, no oil, no mechanical contact — 85%+ efficiency where a Roots blower delivers under 65%.</p>
  </div>
</section>

<section>
  <div class="wrap grid-2" style="gap:56px;align-items:start">
    <div class="prose">
      <h2>Where the energy goes</h2>
      <p>Air duty is sized in cubic metres per minute and paid for in kilowatts, continuously. A Roots blower loses its efficiency to tip clearance and to a belt drive; a water-ring vacuum pump spends a third to a half of its shaft power churning sealing water.</p>
      <p>A levitated rotor removes both losses. The impeller is the only moving part, it runs at up to 40,000 rpm on a film of magnetic force or air, and nothing touches anything until the rotor lands at standstill.</p>
      <div class="table-wrap" style="margin:26px 0">
        <table>
          <thead><tr><th>&nbsp;</th><th>Roots vacuum pump</th><th>Ceramic-bearing turbo</th><th>Air-foil turbo</th></tr></thead>
          <tbody>
            <tr><td>Rotor speed</td><td>&lt; 2,000 rpm</td><td>≤ 20,000 rpm</td><td>≤ 40,000 rpm</td></tr>
            <tr><td>Bearing</td><td>Conventional ball</td><td>Ceramic ball</td><td>Hydrodynamic air film</td></tr>
            <tr><td>Bearing life</td><td>1–2 years</td><td>under 1 year</td><td>Semi-permanent</td></tr>
            <tr><td>Bearing power loss</td><td>2–5%</td><td>2–5%</td><td>&lt; 0.1%</td></tr>
            <tr><td>Drive</td><td>Belt</td><td>Direct</td><td>Direct</td></tr>
            <tr><td>Unit efficiency</td><td>&lt; 65%</td><td>&gt; 80%</td><td>&gt; 85%</td></tr>
            <tr><td>Noise</td><td>90–105 dB(A)</td><td>≤ 90 dB(A)</td><td>≤ 70 dB(A)</td></tr>
            <tr><td>Annual maintenance</td><td>Belts, oil, shaft seals</td><td>Bearing replacement</td><td>Filter mat</td></tr>
          </tbody>
        </table>
      </div>
      <div class="callout"><p><strong>No oil, no water, no gearbox.</strong> That removes the oil circuit, the oil cooler, the sealing-water supply and the belt drive from the equipment list — and from the maintenance schedule as well.</p></div>
    </div>
    <div>
      <div class="card">
        <h3>At a glance</h3>
        <ul class="checks">
          <li>Magnetic-bearing blowers: 18.5–750 kW, pressure rise 60–120 kPa, flow 16.4–640 m³/min</li>
          <li>Air-foil blowers: 15–300 kW, 40–120 kPa, 14–330 m³/min</li>
          <li>Air-foil compressors: 75–300 kW, 200–500 kPa, 18–107 m³/min</li>
          <li>Air-foil vacuum pumps for process duty, to −60 kPa</li>
          <li>Noise ≤ 70 dB(A) on the air-foil range</li>
          <li>Built-in surge protection, variable speed, remote monitoring</li>
        </ul>
      </div>
      <div class="card" style="margin-top:20px;background:#0c1a26;border-color:#0c1a26;color:#fff">
        <p class="tag" style="color:#ffb08a">Field reference</p>
        <h3 style="color:#fff">Fushun thermal power — return-air fan retrofit</h3>
        <p style="color:#c6d6df">A magnetic-bearing high-speed blower replaced the return-air fan on a circulating-fluidised-bed boiler. Belt drive and gearbox out, direct-drive rotor in — lower parasitic loss, no lubrication schedule, and stable pressure at part load.</p>
        <div class="kv" style="border-color:rgba(255,255,255,.14)"><span>Application</span><b>CFB return-air fan</b></div>
        <div class="kv" style="border-color:rgba(255,255,255,.14)"><span>Machine</span><b>Magnetic-bearing blower</b></div>
        <div class="kv" style="border:0"><span>Status</span><b style="color:#7ee2c4">In service</b></div>
      </div>
    </div>
  </div>
</section>

<section class="alt">
  <div class="wrap">
    <div class="sec-head">
      <p class="eyebrow">Three families</p>
      <h2>Magnetic bearings where the power is, air foil where the speed is</h2>
      <p class="lead">Both are oil-free and both are direct drive. Magnetic bearings carry the large rotors and report rotor position continuously; air-foil bearings are the simpler, lower-cost architecture at moderate power.</p>
    </div>
    <div class="grid-3">
      <article class="card">
        <p class="tag">DHMCB · magnetic bearing</p>
        <h3>Centrifugal blower</h3>
        <p>Five-axis active magnetic bearings with digital control. Rotor displacement, vibration and temperature are measured and reported — the machine tells you its condition instead of failing without warning.</p>
        <ul class="checks">
          <li>18.5–750 kW</li>
          <li>Pressure rise 60–120 kPa</li>
          <li>16.4–640 m³/min</li>
        </ul>
      </article>
      <article class="card">
        <p class="tag">DHK · air foil bearing</p>
        <h3>Centrifugal blower</h3>
        <p>Compliant foil bearings riding on an air film generated by the rotor itself. No bearing controller, no electromagnets, no backup-bearing electronics.</p>
        <ul class="checks">
          <li>15–300 kW</li>
          <li>Pressure rise 40–120 kPa</li>
          <li>14–330 m³/min · ≤ 70 dB(A)</li>
        </ul>
      </article>
      <article class="card">
        <p class="tag">DKY · air foil bearing</p>
        <h3>Centrifugal compressor</h3>
        <p>Oil-free compressed air at process pressure, for plants that cannot accept oil carry-over in the air line.</p>
        <ul class="checks">
          <li>75–300 kW</li>
          <li>200–500 kPa</li>
          <li>18–107 m³/min</li>
        </ul>
      </article>
    </div>
  </div>
</section>

<section>
  <div class="wrap">
    <div class="sec-head">
      <p class="eyebrow">Selection table · magnetic bearing blowers</p>
      <h2>DHMCB 18–110</h2>
      <p class="lead">Flow in m³/min at 1 atm, 20 °C, 65% RH. Where a cell is blank the model is not offered at that pressure rise.</p>
    </div>
    <div class="table-wrap">
      <table>
        <thead><tr><th>Model</th><th>18</th><th>22</th><th>30</th><th>37</th><th>45</th><th>55</th><th>75</th><th>90</th><th>110</th></tr></thead>
        <tbody>
          <tr><td>Power (kW)</td><td>18.5</td><td>22</td><td>30</td><td>37</td><td>45</td><td>55</td><td>75</td><td>90</td><td>110</td></tr>
          <tr><td>60 kPa</td><td>16.4</td><td>20</td><td>27</td><td>34</td><td>42</td><td>52</td><td>69</td><td>82</td><td>105</td></tr>
          <tr><td>80 kPa</td><td>12.7</td><td>17</td><td>23</td><td>28</td><td>34</td><td>43</td><td>56</td><td>71</td><td>84</td></tr>
          <tr><td>100 kPa</td><td>—</td><td>—</td><td>—</td><td>22</td><td>26</td><td>35</td><td>48</td><td>57</td><td>73</td></tr>
          <tr><td>120 kPa</td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td><td>39</td><td>48</td><td>58</td></tr>
        </tbody>
      </table>
    </div>

    <div class="sec-head" style="margin-top:44px">
      <h2>DHMCB 150–750</h2>
    </div>
    <div class="table-wrap">
      <table>
        <thead><tr><th>Model</th><th>150</th><th>185</th><th>220</th><th>250</th><th>300</th><th>400</th><th>500</th><th>800</th><th>1000</th></tr></thead>
        <tbody>
          <tr><td>Power (kW)</td><td>150</td><td>185</td><td>220</td><td>250</td><td>300</td><td>400</td><td>500</td><td>600</td><td>750</td></tr>
          <tr><td>60 kPa</td><td>140</td><td>160</td><td>210</td><td>228</td><td>272</td><td>320</td><td>420</td><td>545</td><td>640</td></tr>
          <tr><td>80 kPa</td><td>109</td><td>135</td><td>164</td><td>175</td><td>216</td><td>270</td><td>325</td><td>430</td><td>540</td></tr>
          <tr><td>100 kPa</td><td>96</td><td>118</td><td>145</td><td>146</td><td>190</td><td>225</td><td>270</td><td>360</td><td>452</td></tr>
          <tr><td>120 kPa</td><td>78</td><td>95</td><td>117</td><td>123</td><td>156</td><td>200</td><td>240</td><td>318</td><td>400</td></tr>
        </tbody>
      </table>
    </div>
    <p class="small" style="margin-top:18px">Flow m³/min. Flange sizes from DN125 to DN600 depending on model and pressure rise; dimensions and mass are issued with the datasheet.</p>
  </div>
</section>

<section class="alt">
  <div class="wrap">
    <div class="sec-head">
      <p class="eyebrow">Selection tables · air foil bearing</p>
      <h2>DHK blowers and DKY compressors</h2>
    </div>
    <div class="table-wrap">
      <table>
        <thead><tr><th>DHK blower</th><th>15</th><th>22</th><th>37</th><th>55</th><th>75</th><th>90</th><th>110</th><th>150</th><th>185</th><th>220</th><th>300</th></tr></thead>
        <tbody>
          <tr><td>Power (kW)</td><td>15</td><td>22</td><td>37</td><td>55</td><td>75</td><td>90</td><td>110</td><td>150</td><td>185</td><td>220</td><td>300</td></tr>
          <tr><td>40 kPa</td><td>16</td><td>31</td><td>48</td><td>74</td><td>100</td><td>120</td><td>147</td><td>201</td><td>220</td><td>260</td><td>330</td></tr>
          <tr><td>60 kPa</td><td>14</td><td>21</td><td>35</td><td>53</td><td>70</td><td>85</td><td>108</td><td>141</td><td>170</td><td>212</td><td>278</td></tr>
          <tr><td>80 kPa</td><td>—</td><td>17</td><td>28</td><td>42</td><td>56</td><td>70</td><td>88</td><td>110</td><td>138</td><td>165</td><td>220</td></tr>
          <tr><td>100 kPa</td><td>—</td><td>—</td><td>22</td><td>35</td><td>46</td><td>58</td><td>68</td><td>88</td><td>110</td><td>135</td><td>176</td></tr>
          <tr><td>120 kPa</td><td>—</td><td>—</td><td>19</td><td>29</td><td>37</td><td>48</td><td>58</td><td>78</td><td>96</td><td>114</td><td>145</td></tr>
        </tbody>
      </table>
    </div>
    <div class="table-wrap" style="margin-top:22px">
      <table>
        <thead><tr><th>DKY compressor</th><th>75</th><th>90</th><th>110</th><th>150</th><th>185</th><th>220</th><th>300</th></tr></thead>
        <tbody>
          <tr><td>Power (kW)</td><td>75</td><td>90</td><td>110</td><td>150</td><td>185</td><td>220</td><td>300</td></tr>
          <tr><td>200 kPa</td><td>25</td><td>32</td><td>42</td><td>54</td><td>66</td><td>78</td><td>107</td></tr>
          <tr><td>300 kPa</td><td>22</td><td>28</td><td>33</td><td>46</td><td>58</td><td>69</td><td>96</td></tr>
          <tr><td>400 kPa</td><td>19</td><td>26</td><td>29</td><td>41</td><td>50</td><td>60</td><td>84</td></tr>
          <tr><td>500 kPa</td><td>18</td><td>24</td><td>27</td><td>36</td><td>45</td><td>55</td><td>74</td></tr>
        </tbody>
      </table>
    </div>
    <p class="small" style="margin-top:18px">Air-foil centrifugal vacuum pumps are built on the same platform; the model is fixed against suction volume and working vacuum, so we quote them from the duty point rather than from a single table.</p>
  </div>
</section>

<section>
  <div class="wrap grid-2" style="gap:56px;align-items:start">
    <div class="prose">
      <h2>Monitoring is part of the machine</h2>
      <p>Every unit can be delivered with a remote monitoring platform: live status, pressure and flow trends, running hours, fault levels and maintenance reminders, presented on a web dashboard and a phone.</p>
      <ul>
        <li>Device list with online/offline state and location map</li>
        <li>Real-time curves against historical data</li>
        <li>Alarm log with fault level, not just a trip signal</li>
        <li>Maintenance schedule driven by actual running hours</li>
        <li>Role-based access for the plant, the service team and the distributor</li>
      </ul>
    </div>
    <div class="prose">
      <h2>Where they are used</h2>
      <ul>
        <li><strong>Wastewater aeration.</strong> Continuous duty, wide turndown, and the electricity bill is the largest line in the plant budget.</li>
        <li><strong>Power plant FGD oxidation air and CFB return air.</strong> Constant pressure, long runs, no tolerance for a gearbox failure.</li>
        <li><strong>Coal-mine gas drainage and ventilation.</strong> High suction volume at moderate vacuum, flow chasing methane concentration all shift.</li>
        <li><strong>Paper, chemical and pharmaceutical vacuum.</strong> Dry running where the process cannot take oil or water carry-over.</li>
        <li><strong>Cement, steel and glass.</strong> Process air and combustion air at stable pressure.</li>
      </ul>
      <p class="small">Certification for a specific market — CE, ATEX, EAC, or a mining approval such as MA — is quoted item by item against the target country and application. We do not describe a machine as certified for a market where that approval has not been issued for the delivered configuration.</p>
    </div>
  </div>
</section>

<section class="tight">
  <div class="wrap">
    <div class="card">
      <p class="tag">OEM &amp; private label</p>
      <h3>Supplied under your brand, if that is what you need</h3>
      <p style="max-width:860px">Every machine on this page can be built to order under the nameplate of a distributor, integrator or project contractor: documentation, packing, paint scheme and label set to your specification. Certification, where a market requires it, is applied for against the brand and the market it will be sold in — we do not pass off one market's approval as another's.</p>
    </div>
  </div>
</section>

<section class="tight">
  <div class="wrap">
    <div class="band">
      <div>
        <h2>Replace the Roots blower, keep the pipework.</h2>
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
    <div class="card">
      <p class="tag">OEM &amp; private label</p>
      <h3>Supplied under your brand, if that is what you need</h3>
      <p style="max-width:860px">Every machine on this page can be built to order under the nameplate of a distributor, integrator or project contractor: documentation, packing, paint scheme and label set to your specification. Certification, where a market requires it, is applied for against the brand and the market it will be sold in — we do not pass off one market's approval as another's.</p>
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

<section class="tight">
  <div class="wrap">
    <figure style="margin:0">
      <img src="assets/img/edge-box-1.jpg" alt="Industrial AI agent appliance, desktop enclosure with DC input and dual Ethernet ports" style="width:100%;height:auto;border-radius:14px;display:block">
      <figcaption class="small" style="margin-top:12px">Reference unit: desktop enclosure, 12 V DC input, two Ethernet ports — one gigabit for the plant network, one 100 Mb for an instrument segment or an isolated cell.</figcaption>
    </figure>
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
        <h3 style="color:#fff">Reference hardware — Rockchip standard family</h3>
        <div class="kv" style="border-color:rgba(255,255,255,.14)"><span>Host</span><b>RK3588, 8-core</b></div>
        <div class="kv" style="border-color:rgba(255,255,255,.14)"><span>Accelerators</span><b>4 × RK1828</b></div>
        <div class="kv" style="border-color:rgba(255,255,255,.14)"><span>AI throughput</span><b>20 TOPS INT8 / 40 TOPS INT4 per card</b></div>
        <div class="kv" style="border-color:rgba(255,255,255,.14)"><span>Memory</span><b>15.6 GB visible, 4 × 5 GB stacked</b></div>
        <div class="kv" style="border-color:rgba(255,255,255,.14)"><span>Network</span><b>1 × GbE + 1 × 100M, optional 4G/5G</b></div>
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

<section>
  <div class="wrap grid-2" style="gap:56px;align-items:start">
    <div class="prose">
      <h2>Standard hardware, engineered deployment</h2>
      <p>The appliance is built on Rockchip's standard edge product family — an RK3588 host with RK1828 accelerator modules, the same silicon any integrator can buy. The hardware is not the product.</p>
      <p>What we deliver is everything above it: the model chosen and quantised for the duty, the OpenClaw agent runtime, the document index, the tool connections, the prompts and the guardrails that make it answer like a plant engineer instead of a chatbot — plus the people who pick up the phone when it does not.</p>
      <div class="callout"><p><strong>Same box, your brand.</strong> For distributors and system integrators we ship the appliance configured and tested, with your nameplate, your start screen and your support contact. You sell it into your market; we keep the runtime and the knowledge base current.</p></div>
    </div>
    <div class="prose">
      <h2>Where we are taking it</h2>
      <p>Our first export markets are the ASEAN countries and Southeast Asia, where a plant often has the machines and the meters but not the bandwidth, the budget or the data-protection clearance for a cloud AI service. An appliance that runs on 58 W, needs no internet and answers in the local language fits those sites.</p>
      <ul>
        <li>English and Chinese interfaces today; further languages on request</li>
        <li>Operates on a plant LAN with no external connection</li>
        <li>Supplied configured — commissioning is a network drop, not an integration project</li>
        <li>Distributor and OEM terms available for the region</li>
      </ul>
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
    <h1>悬在磁场与气膜上的鼓风机、压缩机与真空泵</h1>
    <p class="lead">18.5~750 kW 磁悬浮离心鼓风机、15~300 kW 空气悬浮鼓风机、200~500 kPa 空气悬浮压缩机。无齿轮箱、无润滑油、无机械接触——罗茨风机效率不到 65% 的地方，这里做到 85% 以上。</p>
  </div>
</section>

<section>
  <div class="wrap grid-2" style="gap:56px;align-items:start">
    <div class="prose">
      <h2>电都耗在哪里</h2>
      <p>风量按立方米每分钟选型，电费却按千瓦连续支付。罗茨风机的效率丢在叶轮间隙和皮带上；水环真空泵三到五成轴功率耗在搅动密封水里。</p>
      <p>悬浮转子把这两项损失一起去掉：唯一运动件是叶轮，最高 40,000 rpm，浮在磁场或气膜上，直到停机落座之前没有任何零件互相接触。</p>
      <div class="table-wrap" style="margin:26px 0">
        <table>
          <thead><tr><th>&nbsp;</th><th>罗茨真空泵</th><th>陶瓷轴承离心</th><th>空气悬浮离心</th></tr></thead>
          <tbody>
            <tr><td>工作转速</td><td>&lt; 2,000 rpm</td><td>≤ 20,000 rpm</td><td>≤ 40,000 rpm</td></tr>
            <tr><td>轴承</td><td>普通滚珠轴承</td><td>陶瓷球轴承</td><td>动压空气轴承</td></tr>
            <tr><td>轴承寿命</td><td>1~2 年</td><td>不足 1 年</td><td>半永久</td></tr>
            <tr><td>轴承功耗</td><td>2~5%</td><td>2~5%</td><td>&lt; 0.1%</td></tr>
            <tr><td>传动形式</td><td>皮带</td><td>直连</td><td>直连</td></tr>
            <tr><td>整机效率</td><td>&lt; 65%</td><td>&gt; 80%</td><td>&gt; 85%</td></tr>
            <tr><td>噪声</td><td>90~105 dB(A)</td><td>≤ 90 dB(A)</td><td>≤ 70 dB(A)</td></tr>
            <tr><td>年度维护</td><td>皮带、润滑油、轴封</td><td>定期换轴承</td><td>过滤棉</td></tr>
          </tbody>
        </table>
      </div>
      <div class="callout"><p><strong>无油、无水、无齿轮箱。</strong>设备清单里少了油站、油冷却器、供水系统和皮带传动，维修计划里也一并少了。</p></div>
    </div>
    <div>
      <div class="card">
        <h3>关键指标</h3>
        <ul class="checks">
          <li>磁悬浮鼓风机：18.5~750 kW，压升 60~120 kPa，风量 16.4~640 m³/min</li>
          <li>空气悬浮鼓风机：15~300 kW，40~120 kPa，14~330 m³/min</li>
          <li>空气悬浮压缩机：75~300 kW，200~500 kPa，18~107 m³/min</li>
          <li>空气悬浮离心真空泵，适合工艺真空，真空度可至 −60 kPa</li>
          <li>空浮系列噪声 ≤ 70 dB(A)</li>
          <li>内置喘振保护、变频调速、远程监控</li>
        </ul>
      </div>
      <div class="card" style="margin-top:20px;background:#0c1a26;border-color:#0c1a26;color:#fff">
        <p class="tag" style="color:#ffb08a">现场案例</p>
        <h3 style="color:#fff">抚顺中机热电 · 返料风机改造</h3>
        <p style="color:#c6d6df">循环流化床锅炉返料风机改用磁悬浮高速鼓风机：去掉皮带与齿轮箱，改为直驱转子，寄生损耗降低、不再排润滑油计划，部分负荷下压力依然稳定。</p>
        <div class="kv" style="border-color:rgba(255,255,255,.14)"><span>应用</span><b>CFB 返料风机</b></div>
        <div class="kv" style="border-color:rgba(255,255,255,.14)"><span>机型</span><b>磁悬浮离心鼓风机</b></div>
        <div class="kv" style="border:0"><span>状态</span><b style="color:#7ee2c4">已投运</b></div>
      </div>
    </div>
  </div>
</section>

<section class="alt">
  <div class="wrap">
    <div class="sec-head">
      <p class="eyebrow">三个系列</p>
      <h2>大功率走磁悬浮，高转速走空气悬浮</h2>
      <p class="lead">两者都无油、都是直驱。磁悬浮承载大转子并实时反馈转子位置；空气悬浮在中等功率下结构最简、成本最低。</p>
    </div>
    <div class="grid-3">
      <article class="card">
        <p class="tag">DHMCB · 磁悬浮</p>
        <h3>离心鼓风机</h3>
        <p>五轴主动磁悬浮轴承 + 数字控制。转子位移、振动、温度全程测量并上报——机器自己报状态，而不是突然停给你看。</p>
        <ul class="checks">
          <li>18.5~750 kW</li>
          <li>压升 60~120 kPa</li>
          <li>16.4~640 m³/min</li>
        </ul>
      </article>
      <article class="card">
        <p class="tag">DHK · 空气悬浮</p>
        <h3>离心鼓风机</h3>
        <p>弹性箔片轴承靠转子自身带起的气膜承载，无轴承控制器、无电磁铁、无后备轴承电子件。</p>
        <ul class="checks">
          <li>15~300 kW</li>
          <li>压升 40~120 kPa</li>
          <li>14~330 m³/min · ≤ 70 dB(A)</li>
        </ul>
      </article>
      <article class="card">
        <p class="tag">DKY · 空气悬浮</p>
        <h3>离心压缩机</h3>
        <p>工艺压力的无油压缩空气，适合不允许油分进入气路的工厂。</p>
        <ul class="checks">
          <li>75~300 kW</li>
          <li>200~500 kPa</li>
          <li>18~107 m³/min</li>
        </ul>
      </article>
    </div>
  </div>
</section>

<section>
  <div class="wrap">
    <div class="sec-head">
      <p class="eyebrow">选型表 · 磁悬浮鼓风机</p>
      <h2>DHMCB 18~110</h2>
      <p class="lead">风量单位 m³/min，工况：1 atm、20 ℃、相对湿度 65%。空格表示该型号不提供此压升。</p>
    </div>
    <div class="table-wrap">
      <table>
        <thead><tr><th>型号</th><th>18</th><th>22</th><th>30</th><th>37</th><th>45</th><th>55</th><th>75</th><th>90</th><th>110</th></tr></thead>
        <tbody>
          <tr><td>功率 (kW)</td><td>18.5</td><td>22</td><td>30</td><td>37</td><td>45</td><td>55</td><td>75</td><td>90</td><td>110</td></tr>
          <tr><td>60 kPa</td><td>16.4</td><td>20</td><td>27</td><td>34</td><td>42</td><td>52</td><td>69</td><td>82</td><td>105</td></tr>
          <tr><td>80 kPa</td><td>12.7</td><td>17</td><td>23</td><td>28</td><td>34</td><td>43</td><td>56</td><td>71</td><td>84</td></tr>
          <tr><td>100 kPa</td><td>—</td><td>—</td><td>—</td><td>22</td><td>26</td><td>35</td><td>48</td><td>57</td><td>73</td></tr>
          <tr><td>120 kPa</td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td><td>39</td><td>48</td><td>58</td></tr>
        </tbody>
      </table>
    </div>

    <div class="sec-head" style="margin-top:44px">
      <h2>DHMCB 150~750</h2>
    </div>
    <div class="table-wrap">
      <table>
        <thead><tr><th>型号</th><th>150</th><th>185</th><th>220</th><th>250</th><th>300</th><th>400</th><th>500</th><th>800</th><th>1000</th></tr></thead>
        <tbody>
          <tr><td>功率 (kW)</td><td>150</td><td>185</td><td>220</td><td>250</td><td>300</td><td>400</td><td>500</td><td>600</td><td>750</td></tr>
          <tr><td>60 kPa</td><td>140</td><td>160</td><td>210</td><td>228</td><td>272</td><td>320</td><td>420</td><td>545</td><td>640</td></tr>
          <tr><td>80 kPa</td><td>109</td><td>135</td><td>164</td><td>175</td><td>216</td><td>270</td><td>325</td><td>430</td><td>540</td></tr>
          <tr><td>100 kPa</td><td>96</td><td>118</td><td>145</td><td>146</td><td>190</td><td>225</td><td>270</td><td>360</td><td>452</td></tr>
          <tr><td>120 kPa</td><td>78</td><td>95</td><td>117</td><td>123</td><td>156</td><td>200</td><td>240</td><td>318</td><td>400</td></tr>
        </tbody>
      </table>
    </div>
    <p class="small" style="margin-top:18px">风量 m³/min。出口口径按型号与压升在 DN125~DN600 之间选取；外形尺寸与重量随数据表提供。</p>
  </div>
</section>

<section class="alt">
  <div class="wrap">
    <div class="sec-head">
      <p class="eyebrow">选型表 · 空气悬浮</p>
      <h2>DHK 鼓风机与 DKY 压缩机</h2>
    </div>
    <div class="table-wrap">
      <table>
        <thead><tr><th>DHK 鼓风机</th><th>15</th><th>22</th><th>37</th><th>55</th><th>75</th><th>90</th><th>110</th><th>150</th><th>185</th><th>220</th><th>300</th></tr></thead>
        <tbody>
          <tr><td>功率 (kW)</td><td>15</td><td>22</td><td>37</td><td>55</td><td>75</td><td>90</td><td>110</td><td>150</td><td>185</td><td>220</td><td>300</td></tr>
          <tr><td>40 kPa</td><td>16</td><td>31</td><td>48</td><td>74</td><td>100</td><td>120</td><td>147</td><td>201</td><td>220</td><td>260</td><td>330</td></tr>
          <tr><td>60 kPa</td><td>14</td><td>21</td><td>35</td><td>53</td><td>70</td><td>85</td><td>108</td><td>141</td><td>170</td><td>212</td><td>278</td></tr>
          <tr><td>80 kPa</td><td>—</td><td>17</td><td>28</td><td>42</td><td>56</td><td>70</td><td>88</td><td>110</td><td>138</td><td>165</td><td>220</td></tr>
          <tr><td>100 kPa</td><td>—</td><td>—</td><td>22</td><td>35</td><td>46</td><td>58</td><td>68</td><td>88</td><td>110</td><td>135</td><td>176</td></tr>
          <tr><td>120 kPa</td><td>—</td><td>—</td><td>19</td><td>29</td><td>37</td><td>48</td><td>58</td><td>78</td><td>96</td><td>114</td><td>145</td></tr>
        </tbody>
      </table>
    </div>
    <div class="table-wrap" style="margin-top:22px">
      <table>
        <thead><tr><th>DKY 压缩机</th><th>75</th><th>90</th><th>110</th><th>150</th><th>185</th><th>220</th><th>300</th></tr></thead>
        <tbody>
          <tr><td>功率 (kW)</td><td>75</td><td>90</td><td>110</td><td>150</td><td>185</td><td>220</td><td>300</td></tr>
          <tr><td>200 kPa</td><td>25</td><td>32</td><td>42</td><td>54</td><td>66</td><td>78</td><td>107</td></tr>
          <tr><td>300 kPa</td><td>22</td><td>28</td><td>33</td><td>46</td><td>58</td><td>69</td><td>96</td></tr>
          <tr><td>400 kPa</td><td>19</td><td>26</td><td>29</td><td>41</td><td>50</td><td>60</td><td>84</td></tr>
          <tr><td>500 kPa</td><td>18</td><td>24</td><td>27</td><td>36</td><td>45</td><td>55</td><td>74</td></tr>
        </tbody>
      </table>
    </div>
    <p class="small" style="margin-top:18px">空气悬浮离心真空泵与上述平台同源，按抽气量与工作真空度选型，因此不单列型谱表，按工况点报价选型。</p>
  </div>
</section>

<section>
  <div class="wrap grid-2" style="gap:56px;align-items:start">
    <div class="prose">
      <h2>监控是标配的一部分</h2>
      <p>整机可配远程物联网监控平台：运行状态、压力与流量趋势、运行小时、故障等级与维保提醒，网页与手机同步查看。</p>
      <ul>
        <li>设备清单，含在线/离线状态与地域分布</li>
        <li>实时曲线与历史数据对照</li>
        <li>告警记录带故障等级，不只是一个跳机信号</li>
        <li>按实际运行小时驱动的维保计划</li>
        <li>厂方、服务团队与经销商分角色权限</li>
      </ul>
    </div>
    <div class="prose">
      <h2>用在哪里</h2>
      <ul>
        <li><strong>污水处理曝气。</strong>连续工况、流量调节范围宽，电费是厂里最大一笔支出。</li>
        <li><strong>电厂脱硫氧化风、CFB 返料风。</strong>定压长周期运行，容不得齿轮箱出事。</li>
        <li><strong>煤矿瓦斯抽采与通风。</strong>中等负压下大抽气量，风量整天跟着甲烷浓度跑。</li>
        <li><strong>造纸、化工、制药真空。</strong>工艺不能容忍油或水带出的场合，干运行就是刚需。</li>
        <li><strong>水泥、钢铁、玻璃。</strong>工艺风与助燃风，压力要稳。</li>
      </ul>
      <p class="small">目标市场认证——CE、ATEX、EAC，或矿用产品安全标志（MA）——按目标国家与具体应用逐项报价。对交付配置尚未取得批准的认证，我们不会写成"已通过"。</p>
    </div>
  </div>
</section>

<section class="tight">
  <div class="wrap">
    <div class="card">
      <p class="tag">OEM / 贴牌</p>
      <h3>可以按你的品牌交付</h3>
      <p style="max-width:860px">本页机型均可按经销商、集成商或工程承包商的要求贴牌生产：随机文件、包装、涂装与铭牌按你的规格制作。目标市场要求认证的，认证按实际销售品牌与销售国别申请——不会把某一市场的证当成另一市场的证。</p>
    </div>
  </div>
</section>

<section class="tight">
  <div class="wrap">
    <div class="band">
      <div>
        <h2>换掉罗茨风机，管路不用动。</h2>
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
    <div class="card">
      <p class="tag">OEM / 贴牌</p>
      <h3>可以按你的品牌交付</h3>
      <p style="max-width:860px">本页机型均可按经销商、集成商或工程承包商的要求贴牌生产：随机文件、包装、涂装与铭牌按你的规格制作。目标市场要求认证的，认证按实际销售品牌与销售国别申请——不会把某一市场的证当成另一市场的证。</p>
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

<section class="tight">
  <div class="wrap">
    <figure style="margin:0">
      <img src="assets/img/edge-box-1.jpg" alt="工业智能体整机，桌面式机箱，直流输入，双以太网口" style="width:100%;height:auto;border-radius:14px;display:block">
      <figcaption class="small" style="margin-top:12px">参考样机：桌面式机箱、12 V 直流输入、双以太网口——千兆口接厂内网络，百兆口接仪表段或隔离单元。</figcaption>
    </figure>
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
        <h3 style="color:#fff">参考硬件 · 瑞芯微标准系列</h3>
        <div class="kv" style="border-color:rgba(255,255,255,.14)"><span>主机</span><b>RK3588 八核</b></div>
        <div class="kv" style="border-color:rgba(255,255,255,.14)"><span>加速卡</span><b>4 × RK1828</b></div>
        <div class="kv" style="border-color:rgba(255,255,255,.14)"><span>算力</span><b>单卡 20 TOPS INT8 / 40 TOPS INT4</b></div>
        <div class="kv" style="border-color:rgba(255,255,255,.14)"><span>内存</span><b>可见 15.6 GB（4×5 GB 堆叠）</b></div>
        <div class="kv" style="border-color:rgba(255,255,255,.14)"><span>网络</span><b>1 × 千兆 + 1 × 百兆，可选 4G/5G</b></div>
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

<section>
  <div class="wrap grid-2" style="gap:56px;align-items:start">
    <div class="prose">
      <h2>标准硬件，工程化交付</h2>
      <p>整机基于瑞芯微标准边缘产品系列——RK3588 主机加 RK1828 加速模块，这些芯片任何集成商都买得到。硬件本身不是产品。</p>
      <p>我们交付的是硬件之上的全部：按工况选型并量化的模型、OpenClaw 智能体运行时、文档索引、工具对接、提示词与护栏——让它像一个现场工程师那样回答，而不是一个聊天机器人；外加出问题时接电话的人。</p>
      <div class="callout"><p><strong>同一个盒子，你的品牌。</strong>面向经销商与系统集成商，我们按配置完成并测试后出货，铭牌、开机画面与售后联系方式用你的。你在你的市场卖，我们保持运行时与知识库更新。</p></div>
    </div>
    <div class="prose">
      <h2>我们先去哪里</h2>
      <p>首批出口市场是东盟及东南亚国家——那里的工厂往往设备齐全、电表也齐，但缺带宽、缺预算，也过不了云端 AI 服务的数据合规。一台 58 W、不联网、能说当地语言的机器，正好落在这种现场。</p>
      <ul>
        <li>目前提供中英文界面，其他语种按需定制</li>
        <li>在厂区局域网内运行，不需外网连接</li>
        <li>交付即配置完成——上线是接网线，不是做集成项目</li>
        <li>区域内可谈经销与贴牌条件</li>
      </ul>
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
            "title": "Maglev & Air-Foil Blowers, Compressors and Vacuum Pumps | DALIAN HONGSHI TECHNOLOGY",
            "desc": "Oil-free levitated-rotor machines: 18.5-750 kW magnetic-bearing blowers, 15-300 kW air-foil blowers and compressors to 500 kPa, vacuum pumps to -60 kPa. 85%+ efficiency, 70 dB(A).",
            "crumb": "Maglev Blowers",
            "body": MAGLEV_EN,
        },
        "zh": {
            "title": "磁悬浮 / 空气悬浮鼓风机、压缩机与真空泵 | 大连宏实科技",
            "desc": "无油悬浮转子机械：18.5~750 kW 磁悬浮鼓风机、15~300 kW 空气悬浮鼓风机与 200~500 kPa 压缩机、真空泵至 −60 kPa。效率 85% 以上，噪声低至 70 dB(A)。",
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
