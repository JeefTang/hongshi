/* Zero Carbon Assistant — pump sizing & energy calculator (client-side, no data leaves the browser) */
(function () {
  var G = 9.81;

  /* bilingual labels: page declares its language on <html lang="..."> */
  var ZH = (document.documentElement.lang || "").toLowerCase().indexOf("zh") === 0;
  var T = {
    years: ZH ? " 年" : " years",
    perYear: ZH ? "/年" : "/yr",
    co2: ZH ? " 吨 CO₂e/年" : " t CO₂e/yr",
    enterFlowHead: ZH ? "输入流量和扬程后显示结果。" : "Enter flow and head to see results.",
    effWarn: ZH ? "新泵效率必须高于原泵才会有节电。" : "New-pump efficiency must exceed the existing pump for a saving.",
    savingVs: function (e) { return ZH ? "节电基准：原泵效率 " + e + "%。" : "Saving is vs. an existing pump at " + e + "% efficiency."; },
    enterFlow: ZH ? "输入流量后显示推荐机型。" : "Enter flow to see the model recommendation.",
    recV5: ZH ? "落在 V5 立式五柱塞浆料泵范围内（100–400 m³/h，扬程 ≤150 m）。" : "Fits the V5 vertical five-plunger slurry pump range (100–400 m³/h, ≤150 m head).",
    recHP: ZH ? "超出 V5 浆料泵范围 —— 请核对多柱塞高压系列（40–800 m³/h，4–50 MPa）。" : "Outside the V5 slurry envelope — check the multi-plunger high-pressure range (40–800 m³/h, 4–50 MPa).",
    recCustom: ZH ? "超出标准范围 —— 把工况点发给我们，我们做定制机型。" : "Outside standard ranges — send us the duty point and we will engineer a custom unit."
  };

  function num(id) {
    var v = parseFloat((document.getElementById(id) || {}).value);
    return isFinite(v) && v > 0 ? v : 0;
  }
  function fmt(x, d) {
    d = d === undefined ? 1 : d;
    if (!isFinite(x)) return "—";
    return x.toLocaleString("en-US", { minimumFractionDigits: d, maximumFractionDigits: d });
  }
  function set(id, text) {
    var el = document.getElementById(id);
    if (el) el.textContent = text;
  }

  /* ---------- Tab 1: energy & payback ---------- */
  function calcEnergy() {
    var Q = num("e_q");          // m3/h
    var H = num("e_h");          // m
    var rho = num("e_rho") || 1000;
    var effNew = (num("e_eff") || 90) / 100;
    var effOld = (num("e_eff_old") || 40) / 100;
    var hours = num("e_hours") || 8000;
    var price = num("e_price") || 0.08;
    var capex = num("e_capex") || 0;

    // hydraulic power kW = rho*g*Q*H / 3.6e6  (Q in m3/h)
    var ph = (rho * G * Q * H) / 3600000;
    var pNew = ph / effNew;
    var pOld = ph / effOld;

    var kwhNew = pNew * hours;
    var kwhOld = pOld * hours;
    var costNew = kwhNew * price;
    var costOld = kwhOld * price;
    var save = costOld - costNew;
    var payback = save > 0 ? capex / save : NaN;
    var co2 = (kwhOld - kwhNew) * 0.000581; // tCO2e, China grid factor ~0.581 kg/kWh

    set("o_ph", fmt(ph, 1) + " kW");
    set("o_pnew", fmt(pNew, 1) + " kW");
    set("o_pold", fmt(pOld, 1) + " kW");
    set("o_kwh", fmt(kwhNew, 0) + " kWh");
    set("o_cost", "$" + fmt(costNew, 0));
    set("o_save", "$" + fmt(save, 0));
    set("o_payback", isFinite(payback) ? fmt(payback, 1) + T.years : "—");
    set("o_co2", fmt(co2, 0) + T.co2);

    var hint = document.getElementById("e_hint");
    if (hint) {
      if (!Q || !H) hint.textContent = T.enterFlowHead;
      else if (save <= 0) hint.textContent = T.effWarn;
      else hint.textContent = T.savingVs(fmt(effOld * 100, 0));
    }
  }

  /* ---------- Tab 2: slurry check ---------- */
  function calcSlurry() {
    var Q = num("s_q");
    var H = num("s_h");
    var cw = (num("s_c")) / 100;          // solids concentration by weight
    var sg = num("s_sg") || 2.7;          // solids specific gravity
    var eff = (num("s_eff") || 83) / 100;
    var hours = num("s_hours") || 8000;
    var price = num("s_price") || 0.08;

    // mixture density from solids mass fraction (water SG = 1)
    var cwSafe = Math.min(Math.max(cw, 0), 0.85);
    var rhoMix = 1 / ((cwSafe / sg) + ((1 - cwSafe) / 1)) * 1000; // kg/m3
    var ph = (rhoMix * G * Q * H) / 3600000;
    var shaft = ph / eff;
    var kwh = shaft * hours;
    var cost = kwh * price;

    set("o_mix", fmt(rhoMix, 0) + " kg/m³");
    set("o_sg_mix", fmt(rhoMix / 1000, 2));
    set("o_sph", fmt(ph, 1) + " kW");
    set("o_sshaft", fmt(shaft, 1) + " kW");
    set("o_skwh", fmt(kwh, 0) + " kWh" + T.perYear);
    set("o_scost", "$" + fmt(cost, 0) + T.perYear);

    var rec = document.getElementById("s_rec");
    if (rec) {
      if (!Q) { rec.textContent = T.enterFlow; }
      else if (Q >= 100 && Q <= 400 && H <= 150) {
        rec.textContent = T.recV5;
      } else if (Q >= 40 && Q <= 800) {
        rec.textContent = T.recHP;
      } else {
        rec.textContent = T.recCustom;
      }
    }
  }

  /* ---------- tabs ---------- */
  function showTab(name) {
    document.querySelectorAll("[data-tab]").forEach(function (x) {
      x.classList.toggle("active", x.getAttribute("data-tab") === name);
    });
    document.querySelectorAll("[data-panel]").forEach(function (p) {
      p.style.display = p.getAttribute("data-panel") === name ? "" : "none";
    });
  }

  function initTabs() {
    var tabs = document.querySelectorAll("[data-tab]");
    if (!tabs.length) return;
    tabs.forEach(function (t) {
      t.addEventListener("click", function () {
        showTab(t.getAttribute("data-tab"));
      });
    });
    /* set the initial state: an explicitly active tab, else the first one.
       Needed on the mobile edition, where inline styles/classes are stripped. */
    var active = document.querySelector("[data-tab].active") || tabs[0];
    showTab(active.getAttribute("data-tab"));
  }

  document.addEventListener("DOMContentLoaded", function () {
    initTabs();
    ["e_q", "e_h", "e_rho", "e_eff", "e_eff_old", "e_hours", "e_price", "e_capex"].forEach(function (id) {
      var el = document.getElementById(id);
      if (el) el.addEventListener("input", calcEnergy);
    });
    ["s_q", "s_h", "s_c", "s_sg", "s_eff", "s_hours", "s_price"].forEach(function (id) {
      var el = document.getElementById(id);
      if (el) el.addEventListener("input", calcSlurry);
    });
    if (document.getElementById("e_q")) calcEnergy();
    if (document.getElementById("s_q")) calcSlurry();
  });
})();
