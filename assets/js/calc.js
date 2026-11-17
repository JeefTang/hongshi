/* Zero Carbon Assistant — pump sizing & energy calculator (client-side, no data leaves the browser)
   2026-11-17 口径统一（老唐定）：
   - 节电比较用「原泵系统效率（含电机）」 vs 「新泵：泵效率 ÷ 电机/传动效率」
   - 电机选型 = 选型点（流量 +10%、压差 +1 MPa）轴功率 × 1.10 → 向上取标准档
     与内网节能改造方案系统 engine.py、节能测算官网 同一套公式
*/
(function () {
  var G = 9.81;
  var MOTOR_STD = [0.75, 1.1, 1.5, 2.2, 3, 4, 5.5, 7.5, 11, 15, 18.5, 22, 30, 37,
                   45, 55, 75, 90, 110, 132, 160, 185, 200, 220, 250, 280, 315,
                   355, 400, 450, 500, 560, 630, 710, 800, 900, 1000, 1120, 1250];

  /* bilingual labels: page declares its language on <html lang="..."> */
  var ZH = (document.documentElement.lang || "").toLowerCase().indexOf("zh") === 0;
  var T = {
    years: ZH ? " 年" : " years",
    perYear: ZH ? "/年" : "/yr",
    co2: ZH ? " 吨 CO₂e/年" : " t CO₂e/yr",
    enterFlowHead: ZH ? "输入流量和扬程后显示结果。" : "Enter flow and head to see results.",
    effWarn: ZH ? "新泵效率必须高于原泵才会有节电。" : "New-pump efficiency must exceed the existing pump for a saving.",
    savingVs: function (e) { return ZH ? "节电基准：原泵系统效率（含电机）" + e + "%。" : "Saving is vs. an existing pump at " + e + "% system efficiency (motor included)."; },
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
  function checked(id, dflt) {
    var el = document.getElementById(id);
    return el ? !!el.checked : dflt;
  }

  /* 电机选型（与方案系统同一链条）：型号档位留余量（Q +10%、ΔP +1 MPa）→ 轴功率 × 1.10 → 标准档 */
  function pickMotor(Q, dP, etaPump, useMargin) {
    var q = useMargin ? Q * 1.10 : Q;
    var dp = useMargin ? dP + 1.0 : dP;
    var shaftSel = q * dp / 3.6 / etaPump;
    var raw = shaftSel * 1.10;
    var pick = null;
    for (var i = 0; i < MOTOR_STD.length; i++) {
      if (MOTOR_STD[i] >= raw) { pick = MOTOR_STD[i]; break; }
    }
    if (!pick) pick = Math.ceil(raw / 50) * 50;
    return { q: q, dp: dp, shaftSel: shaftSel, raw: raw, pick: pick, marginOn: !!useMargin };
  }

  /* ---------- Tab 1: energy & payback ---------- */
  function calcEnergy() {
    var Q = num("e_q");                    // m3/h
    var H = num("e_h");                    // m
    var rho = num("e_rho") || 1000;
    var effNew = (num("e_eff") || 90) / 100;
    var effOld = (num("e_eff_old") || 55) / 100;      // 原泵系统效率（含电机）
    var effMotor = (num("e_eff_motor") || 95) / 100;  // 新泵电机+传动
    var hours = num("e_hours") || 8000;
    var price = num("e_price") || 0.08;
    var capex = num("e_capex") || 0;
    var useMargin = checked("e_margin", true);

    // hydraulic power kW = rho*g*Q*H / 3.6e6  (Q in m3/h)
    var ph = (rho * G * Q * H) / 3600000;
    var pNewShaft = ph / effNew;
    var pNewGrid = pNewShaft / effMotor;      // 新泵电网取电（含电机/传动）
    var pOld = ph / effOld;                   // 原泵电网取电 = 实测输入功率

    var kwhNew = pNewGrid * hours;
    var kwhOld = pOld * hours;
    var costNew = kwhNew * price;
    var save = costOldMinus();
    function costOldMinus() { return kwhOld * price - kwhNew * price; }
    var payback = save > 0 ? capex / save : NaN;
    var co2 = (kwhOld - kwhNew) * 0.000581; // tCO2e, China grid factor ~0.581 kg/kWh
    var sel = Q && H ? pickMotor(Q, (rho * G * H) / 1e6, effNew, useMargin) : null;

    set("o_ph", fmt(ph, 1) + " kW");
    set("o_pnew", fmt(pNewShaft, 1) + " kW");
    set("o_pgrid", fmt(pNewGrid, 1) + " kW");
    set("o_pold", fmt(pOld, 1) + " kW");
    set("o_kwh", fmt(kwhNew, 0) + " kWh");
    set("o_cost", fmt(costNew, 0));
    set("o_save", fmt(save, 0));
    set("o_payback", isFinite(payback) ? fmt(payback, 1) + T.years : "—");
    set("o_co2", fmt(co2, 0) + T.co2);
    set("o_motor", sel ? (fmt(sel.pick, 0) + " kW") : "—");
    set("o_motor_note", sel
      ? (ZH
        ? "选型点 " + fmt(sel.q, 1) + " m³/h / " + fmt(sel.dp, 2) + " MPa（" + (sel.marginOn ? "含 +10% 流量、+1 MPa 余量" : "按运行点，未留余量") + "）→ 轴功率 " + fmt(sel.shaftSel, 1) + " kW × 1.10 = " + fmt(sel.raw, 1) + " kW"
        : "Selection point " + fmt(sel.q, 1) + " m³/h / " + fmt(sel.dp, 2) + " MPa (" + (sel.marginOn ? "+10% flow, +1 MPa margin" : "duty point, no margin") + ") → shaft " + fmt(sel.shaftSel, 1) + " kW × 1.10 = " + fmt(sel.raw, 1) + " kW")
      : "");

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
    set("o_scost", fmt(cost, 0) + T.perYear);

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
    ["e_q", "e_h", "e_rho", "e_eff", "e_eff_old", "e_eff_motor", "e_hours", "e_price", "e_capex", "e_margin"].forEach(function (id) {
      var el = document.getElementById(id);
      if (el) el.addEventListener("input", calcEnergy);
      if (el && el.type === "checkbox") el.addEventListener("change", calcEnergy);
    });
    ["s_q", "s_h", "s_c", "s_sg", "s_eff", "s_hours", "s_price"].forEach(function (id) {
      var el = document.getElementById(id);
      if (el) el.addEventListener("input", calcSlurry);
    });
    if (document.getElementById("e_q")) calcEnergy();
    if (document.getElementById("s_q")) calcSlurry();
  });
})();
