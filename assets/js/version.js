/* Version switcher — desktop <-> mobile edition (/m/ , /zh/m/)
   Rules
   1. ?view=mobile|desktop  → store preference in cookie, then act.
   2. Default = mobile edition: any desktop page with no explicit "desktop"
      preference (cookie/param) redirects to the /m/ twin of that page.
   3. Mobile pages never auto-redirect back (no loops); the "Desktop" link there
      passes ?view=desktop.
*/
(function () {
  var COOKIE = 'hs_view';
  var MAXAGE = 60 * 60 * 24 * 365;

  function getPref() {
    var m = document.cookie.match(/(?:^|;\s*)hs_view=(mobile|desktop)/);
    return m ? m[1] : null;
  }
  function setPref(v) {
    if (v !== 'mobile' && v !== 'desktop') return;
    document.cookie = COOKIE + '=' + v + ';path=/;max-age=' + MAXAGE + ';SameSite=Lax';
  }
  window.hsView = { get: getPref, set: setPref };

  var params = new URLSearchParams(location.search);
  var forced = params.get('view');
  if (forced) setPref(forced);

  var isMobilePage = /\/m\//.test(location.pathname) || /\/m$/.test(location.pathname);
  var pref = forced || getPref() || 'mobile';

  if (!isMobilePage && pref !== 'desktop') {
    var path = location.pathname;
    var target;
    if (/\/$/.test(path)) {
      target = path + 'm/';
    } else {
      target = path.replace(/\/([^\/]+)$/, '/m/$1');
    }
    if (target !== path) {
      var qs = location.search.replace(/[?&]view=[^&]*/g, '').replace(/^&/, '?');
      if (qs === '?' || qs === '') qs = '';
      location.replace(target + qs + location.hash);
    }
  }
})();
