/*  EDOS – Shared site-wide JavaScript
 *  Auto-detects features based on DOM elements present on the page.
 *  Pages only need <script src="/js/main.js" defer></script>
 */
(function(){
  'use strict';

  /* ---- NAV SCROLL STATE ---- */
  var nav=document.getElementById('mainNav');
  if(nav){
    window.addEventListener('scroll',function(){
      nav.classList[window.scrollY>48?'add':'remove']('scrolled');
    },{passive:true});
  }

  /* ---- HAMBURGER / OVERLAY MENU ---- */
  var burger=document.getElementById('navHamburger'),
      overlay=document.getElementById('navOverlay'),
      closeBtn=document.getElementById('navOverlayClose');
  if(burger&&overlay&&closeBtn){
    function openOv(){overlay.classList.add('open');burger.classList.add('open');document.body.style.overflow='hidden';}
    function closeOv(){overlay.classList.remove('open');burger.classList.remove('open');document.body.style.overflow='';}
    burger.addEventListener('click',function(){overlay.classList.contains('open')?closeOv():openOv();});
    closeBtn.addEventListener('click',closeOv);
    overlay.querySelectorAll('a').forEach(function(a){a.addEventListener('click',closeOv);});
  }

  /* ---- SMOOTH SCROLL FOR ANCHOR LINKS ---- */
  document.querySelectorAll('a[href^="#"]').forEach(function(a){
    a.addEventListener('click',function(e){
      var id=this.getAttribute('href');
      if(id==='#')return;
      var el=document.querySelector(id);
      if(el){e.preventDefault();el.scrollIntoView({behavior:'smooth'});}
    });
  });

  /* ---- REVEAL ANIMATIONS ---- */
  var revSel='.reveal,.reveal-scale,.reveal-left,.reveal-right';
  var revEls=document.querySelectorAll(revSel);
  if(revEls.length){
    /* stagger siblings */
    var parents=[];
    revEls.forEach(function(el){var p=el.parentElement;if(!parents.includes(p))parents.push(p);});
    parents.forEach(function(p){
      var kids=Array.from(p.querySelectorAll(':scope > '+revSel.replace(/,/g,', :scope > ')));
      kids.forEach(function(k,i){if(!k.style.transitionDelay)k.style.transitionDelay=(i*0.12)+'s';});
    });
    /* observe */
    if('IntersectionObserver' in window){
      var ro=new IntersectionObserver(function(entries){
        entries.forEach(function(e){if(e.isIntersecting){e.target.classList.add('visible');ro.unobserve(e.target);}});
      },{threshold:0.08,rootMargin:'0px 0px -40px 0px'});
      revEls.forEach(function(el){ro.observe(el);});
    }else{
      revEls.forEach(function(el){el.classList.add('visible');});
    }
  }

  /* ---- FIXED CTA (show/hide + dark mode) ---- */
  (function(){
    var fc=document.getElementById('fixedCta');
    if(!fc)return;
    /* auto-detect hero */
    var hero=document.querySelector('.cs-hero')||document.querySelector('.page-hero')||document.querySelector('.hero');
    var ctaFinal=document.querySelector('.cta-final');
    var past=false,inFinal=false;

    function updateVis(){fc.classList[past&&!inFinal?'add':'remove']('visible');}

    if('IntersectionObserver' in window){
      if(hero){
        var ho=new IntersectionObserver(function(es){
          es.forEach(function(e){if(e.target===hero){past=!e.isIntersecting;updateVis();}});
        },{threshold:0});
        ho.observe(hero);
      }else{past=true;}

      if(ctaFinal){
        var fo=new IntersectionObserver(function(es){
          inFinal=es[0].isIntersecting;updateVis();
        },{threshold:0.05});
        fo.observe(ctaFinal);
      }

      /* auto-detect dark sections */
      var darkSels=['.hero','.page-hero','.cs-hero','.cl-section','.pf-section','.numeri','.partnerflow','.cta-final'];
      var darks=document.querySelectorAll(darkSels.join(','));
      if(darks.length){
        var dc=0;
        var dobs=new IntersectionObserver(function(es){
          es.forEach(function(e){
            dc+=e.isIntersecting?1:-1;
            dc=Math.max(0,dc);
            fc.classList[dc>0?'add':'remove']('on-dark');
          });
        },{threshold:0,rootMargin:'0px -60px 0px 0px'});
        darks.forEach(function(s){dobs.observe(s);});
      }
    }
  })();

  /* ---- FOOTER ACCORDION (mobile) ---- */
  (function(){
    var cols=document.querySelectorAll('.footer-col');
    if(!cols.length)return;
    function initAccordion(){
      if(window.innerWidth>900){
        cols.forEach(function(c){c.classList.remove('open')});
        return;
      }
    }
    cols.forEach(function(col){
      var label=col.querySelector('.footer-col-label');
      if(!label)return;
      label.addEventListener('click',function(){
        if(window.innerWidth>900)return;
        var isOpen=col.classList.contains('open');
        cols.forEach(function(c){c.classList.remove('open')});
        if(!isOpen)col.classList.add('open');
      });
    });
    window.addEventListener('resize',initAccordion);
  })();

})();
