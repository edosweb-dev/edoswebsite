/*  EDOS – Cookie Consent Banner
 *  GDPR-compliant, no dependencies, vanilla JS.
 *  Categories: necessary (always on), analytics, marketing.
 *
 *  API:
 *    window.edosCookies.get()          → {necessary:true, analytics:bool, marketing:bool}
 *    window.edosCookies.showPrefs()    → open preferences panel
 *    window.edosCookies.on(cat, fn)    → callback when category is accepted
 *
 *  Emits custom event 'cookie-consent-update' on document whenever prefs change.
 */
(function(){
  'use strict';

  var COOKIE_NAME = 'edos_cookie_consent';
  var COOKIE_DAYS = 365;
  var CATEGORIES  = ['necessary','analytics','marketing'];

  /* ---------- helpers ---------- */
  function setCookie(name, val, days){
    var d = new Date();
    d.setTime(d.getTime() + days * 864e5);
    document.cookie = name + '=' + encodeURIComponent(val) +
      ';expires=' + d.toUTCString() + ';path=/;SameSite=Lax';
  }
  function getCookie(name){
    var m = document.cookie.match('(^|;)\\s*' + name + '=([^;]*)');
    return m ? decodeURIComponent(m[2]) : null;
  }

  function getPrefs(){
    var raw = getCookie(COOKIE_NAME);
    if(!raw) return null;
    try { return JSON.parse(raw); } catch(e){ return null; }
  }
  function savePrefs(prefs){
    prefs.necessary = true; // always on
    setCookie(COOKIE_NAME, JSON.stringify(prefs), COOKIE_DAYS);
    document.dispatchEvent(new CustomEvent('cookie-consent-update', {detail: prefs}));
    fireCallbacks(prefs);
  }

  /* ---------- callbacks ---------- */
  var listeners = {};
  function onCat(cat, fn){
    if(!listeners[cat]) listeners[cat] = [];
    listeners[cat].push(fn);
    // fire immediately if already accepted
    var p = getPrefs();
    if(p && p[cat]) fn();
  }
  function fireCallbacks(prefs){
    CATEGORIES.forEach(function(c){
      if(prefs[c] && listeners[c]){
        listeners[c].forEach(function(fn){ fn(); });
        listeners[c] = []; // fire once
      }
    });
  }

  /* ---------- DOM ---------- */
  function createBanner(){
    // Blocking overlay — dims the page until user interacts with the banner
    var wall = document.createElement('div');
    wall.id = 'cookieWall';
    wall.className = 'cw';
    document.body.appendChild(wall);

    // Banner
    var banner = document.createElement('div');
    banner.id = 'cookieBanner';
    banner.className = 'cb';
    banner.innerHTML =
      '<div class="cb-inner">' +
        '<div class="cb-logo"><img src="/logo-white.png" alt="Edos" loading="lazy"></div>' +
        '<div class="cb-text">' +
          '<p class="cb-desc">Per fornire le migliori esperienze, utilizziamo tecnologie come i cookie per memorizzare e/o accedere alle informazioni del dispositivo. Il consenso a queste tecnologie ci permetter\u00e0 di elaborare dati come il comportamento di navigazione o ID unici su questo sito. Non acconsentire o ritirare il consenso pu\u00f2 influire negativamente su alcune caratteristiche e funzioni. ' +
            '<a href="/cookie-policy">Cookie Policy</a></p>' +
        '</div>' +
        '<div class="cb-actions">' +
          '<button class="cb-btn cb-btn-accept" id="cbAcceptAll">Accetta tutti</button>' +
          '<button class="cb-btn cb-btn-prefs" id="cbShowPrefs">Personalizza</button>' +
          '<button class="cb-btn cb-btn-reject" id="cbRejectAll">Rifiuta non necessari</button>' +
        '</div>' +
      '</div>';

    // Preferences panel
    var panel = document.createElement('div');
    panel.id = 'cookiePrefs';
    panel.className = 'cp';
    panel.innerHTML =
      '<div class="cp-overlay" id="cpOverlay"></div>' +
      '<div class="cp-panel">' +
        '<div class="cp-header">' +
          '<span class="cp-title">Preferenze cookie</span>' +
          '<button class="cp-close" id="cpClose" aria-label="Chiudi">' +
            '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="18" y1="6" x2="6" y2="18"/><line x1="6" y1="6" x2="18" y2="18"/></svg>' +
          '</button>' +
        '</div>' +
        '<div class="cp-body">' +
          '<div class="cp-cat">' +
            '<div class="cp-cat-head">' +
              '<div class="cp-cat-info"><span class="cp-cat-name">Cookie necessari</span><span class="cp-cat-badge">Sempre attivi</span></div>' +
            '</div>' +
            '<p class="cp-cat-desc">Indispensabili per il funzionamento del sito. Includono cookie di sessione, preferenze di navigazione e caricamento dei font (Google Fonts).</p>' +
          '</div>' +
          '<div class="cp-cat">' +
            '<div class="cp-cat-head">' +
              '<div class="cp-cat-info"><span class="cp-cat-name">Cookie analitici</span></div>' +
              '<label class="cp-toggle" for="cpAnalytics"><input type="checkbox" id="cpAnalytics" aria-label="Cookie analitici"><span class="cp-toggle-slider"></span></label>' +
            '</div>' +
            '<p class="cp-cat-desc">Raccolgono informazioni aggregate su come i visitatori utilizzano il sito, per migliorare l\u2019esperienza di navigazione e le prestazioni.</p>' +
          '</div>' +
          '<div class="cp-cat">' +
            '<div class="cp-cat-head">' +
              '<div class="cp-cat-info"><span class="cp-cat-name">Cookie di marketing</span></div>' +
              '<label class="cp-toggle" for="cpMarketing"><input type="checkbox" id="cpMarketing" aria-label="Cookie di marketing"><span class="cp-toggle-slider"></span></label>' +
            '</div>' +
            '<p class="cp-cat-desc">Utilizzati per mostrare annunci pertinenti e misurare l\u2019efficacia delle campagne pubblicitarie su piattaforme esterne.</p>' +
          '</div>' +
        '</div>' +
        '<div class="cp-footer">' +
          '<button class="cb-btn cb-btn-accept" id="cpSaveAll">Accetta tutti</button>' +
          '<button class="cb-btn cb-btn-prefs" id="cpSave">Salva preferenze</button>' +
        '</div>' +
      '</div>';

    document.body.appendChild(banner);
    document.body.appendChild(panel);
  }

  function showBanner(){
    var b = document.getElementById('cookieBanner');
    var w = document.getElementById('cookieWall');
    if(b) b.classList.add('cb-visible');
    if(w) w.classList.add('cw-visible');
  }
  function hideBanner(){
    var b = document.getElementById('cookieBanner');
    var w = document.getElementById('cookieWall');
    if(b) b.classList.remove('cb-visible');
    if(w) w.classList.remove('cw-visible');
  }
  function showPrefs(){
    var p = document.getElementById('cookiePrefs');
    if(!p) return;
    // Load current prefs into checkboxes
    var prefs = getPrefs() || {necessary:true, analytics:false, marketing:false};
    var a = document.getElementById('cpAnalytics');
    var m = document.getElementById('cpMarketing');
    if(a) a.checked = !!prefs.analytics;
    if(m) m.checked = !!prefs.marketing;
    p.classList.add('cp-visible');
    document.body.style.overflow = 'hidden';
  }
  function hidePrefs(){
    var p = document.getElementById('cookiePrefs');
    if(p) p.classList.remove('cp-visible');
    document.body.style.overflow = '';
  }

  function acceptAll(){
    savePrefs({necessary:true, analytics:true, marketing:true});
    hideBanner();
    hidePrefs();
  }
  function rejectAll(){
    savePrefs({necessary:true, analytics:false, marketing:false});
    hideBanner();
    hidePrefs();
  }
  function saveCustom(){
    var a = document.getElementById('cpAnalytics');
    var m = document.getElementById('cpMarketing');
    savePrefs({
      necessary: true,
      analytics: a ? a.checked : false,
      marketing: m ? m.checked : false
    });
    hideBanner();
    hidePrefs();
  }

  /* ---------- init ---------- */
  function init(){
    createBanner();

    // Bind events
    document.getElementById('cbAcceptAll').addEventListener('click', acceptAll);
    document.getElementById('cbShowPrefs').addEventListener('click', showPrefs);
    document.getElementById('cbRejectAll').addEventListener('click', rejectAll);
    document.getElementById('cpClose').addEventListener('click', hidePrefs);
    document.getElementById('cpOverlay').addEventListener('click', hidePrefs);
    document.getElementById('cpSaveAll').addEventListener('click', acceptAll);
    document.getElementById('cpSave').addEventListener('click', saveCustom);

    // "Gestisci cookie" links anywhere on the page
    document.querySelectorAll('[data-cookie-prefs]').forEach(function(el){
      el.addEventListener('click', function(e){
        e.preventDefault();
        showPrefs();
      });
    });

    // Show banner if no consent yet
    var prefs = getPrefs();
    if(!prefs){
      // Small delay for page render
      setTimeout(showBanner, 600);
    } else {
      fireCallbacks(prefs);
    }
  }

  if(document.readyState === 'loading'){
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }

  /* ---------- public API ---------- */
  window.edosCookies = {
    get: function(){ return getPrefs() || {necessary:true, analytics:false, marketing:false}; },
    showPrefs: showPrefs,
    on: onCat
  };

})();
