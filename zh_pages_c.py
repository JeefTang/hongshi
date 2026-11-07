
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
    <h1>先把泵做好，再谈目录的工程团队</h1>
    <p class="lead">{CONFIG['brand_cn']}面向全球供应高压往复柱塞泵与浆料泵，出口业务由中国辽宁大连运营。</p>
  </div>
</section>

<section>
  <div class="wrap grid-2" style="gap:56px;align-items:start">
    <div class="prose">
      <h2>公司背景</h2>
      <p>公司 2018 年成立于上海浦东，属同济南汇科技园体系。产品研发依托四川省机械研究设计院（始建于 1957 年）——一家在机械、市政、石化与电力领域具备设计与 EPC 资质的国有科研院所。</p>
      <p>我们的工程中心专注两条技术路线：高速直驱与低速大扭矩驱动，这也是我们所有泵与风机产品背后的两种架构。</p>
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
        <div class="kv" style="color:var(--ink);border-color:var(--line)"><span class="muted">成立</span><b>2018 年 · 上海</b></div>
        <div class="kv" style="color:var(--ink);border-color:var(--line)"><span class="muted">产品范围</span><b>12–600 m³/h · 扬程 200–3,150 m · 至 70 MPa</b></div>
        <div class="kv" style="color:var(--ink);border-color:var(--line)"><span class="muted">泵效率</span><b>&gt;90%</b></div>
        <div class="kv" style="color:var(--ink);border-color:var(--line)"><span class="muted">大修周期</span><b>30,000 h+</b></div>
        <div class="kv" style="color:var(--ink);border:0"><span class="muted">市场</span><b>矿山 · 电力 · 油气</b></div>
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
        "关于大连宏实科技有限公司 — 往复泵工程 · 大连",
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
        zh_filterpress(), zh_tailings(), zh_water(), zh_calc(),
        zh_about(), zh_contact(), zh_references(), zh_404(),
    ]
    for p in pages:
        doc = (
            head(p["title"], p["desc"], p["slug"], p["extra_head"])
            + header(p["active"], en_href=p["slug"])
            + p["body"]
            + footer()
            + '\n<script src="../assets/js/calc.js" defer></script>\n</body>\n</html>'
        )
        with open(os.path.join(OUT_ZH, p["slug"]), "w", encoding="utf-8") as f:
            f.write(doc)
        print("wrote zh/" + p["slug"], len(doc))


if __name__ == "__main__":
    main()
