/* Auto Justo — helpers de microinteração compartilhados.
   Uso: <script src="aj.js"></script> depois do conteúdo. */
(function (global) {
  'use strict';

  var reduce = global.matchMedia &&
    global.matchMedia('(prefers-reduced-motion: reduce)').matches;

  function wait(ms) {
    return new Promise(function (r) { setTimeout(r, reduce ? 0 : ms); });
  }

  /* Texto da IA palavra por palavra. el recebe o texto de data-aj-type. */
  function typeText(el, text, speed) {
    text = text || el.getAttribute('data-aj-type') || el.textContent;
    speed = speed == null ? 42 : speed;
    var words = text.trim().split(/\s+/);
    el.textContent = '';
    if (reduce) { el.textContent = text; return Promise.resolve(); }
    var i = 0;
    return new Promise(function (done) {
      (function step() {
        if (i >= words.length) return done();
        el.textContent += (i ? ' ' : '') + words[i++];
        setTimeout(step, speed);
      })();
    });
  }

  /* Revela elementos .aj-enter em sequência, de baixo pra cima. */
  function reveal(nodes, stagger) {
    stagger = stagger == null ? 140 : stagger;
    var list = Array.prototype.slice.call(nodes);
    return list.reduce(function (chain, node, i) {
      return chain.then(function () {
        return wait(i ? stagger : 0).then(function () { node.classList.add('is-in'); });
      });
    }, Promise.resolve());
  }

  /* Checklist: itens marcam um por um. */
  function runChecklist(container, stagger) {
    return reveal(container.querySelectorAll('.aj-check'), stagger == null ? 520 : stagger);
  }

  /* Bottom sheet abre/fecha junto com o scrim irmão. */
  function openSheet(sheet) {
    var scrim = sheet.parentNode.querySelector('.aj-sheet-scrim');
    if (scrim) scrim.classList.add('is-open');
    sheet.classList.add('is-open');
    var seal = sheet.querySelector('.aj-seal');
    if (seal) setTimeout(function () { seal.classList.add('is-on'); }, 260);
  }
  function closeSheet(sheet) {
    var scrim = sheet.parentNode.querySelector('.aj-sheet-scrim');
    if (scrim) scrim.classList.remove('is-open');
    sheet.classList.remove('is-open');
  }

  /* Rola a conversa pro fim. */
  function scrollDown(scroller) {
    scroller.scrollTop = scroller.scrollHeight;
  }

  global.AJ = {
    reduce: reduce,
    wait: wait,
    typeText: typeText,
    reveal: reveal,
    runChecklist: runChecklist,
    openSheet: openSheet,
    closeSheet: closeSheet,
    scrollDown: scrollDown
  };
})(window);

/* ---------------------------------------------------------------
   Navegação do protótipo — injetada em toda tela que carrega aj.js.
   Zero markup necessário na tela: descobre onde está pelo filename.
   Também transforma os rodapés "Continua em T-0N …" em links.
   --------------------------------------------------------------- */
(function (global) {
  'use strict';

  var SCREENS = [
    { file: 'T00-onboarding.html',    id: 'T-00', name: 'Cadastro' },
    { file: 'T01-chat.html',          id: 'T-01', name: 'Chat' },
    { file: 'T02-diagnostico.html',   id: 'T-02', name: 'Diagnóstico' },
    { file: 'T03-oficinas.html',      id: 'T-03', name: 'Oficinas' },
    { file: 'T04-perfil-oficina.html',id: 'T-04', name: 'Perfil da oficina' },
    { file: 'T05-orcamentos.html',    id: 'T-05', name: 'Orçamentos' },
    { file: 'T06-agendamento.html',   id: 'T-06', name: 'Agendamento' },
    { file: 'T07-historico.html',     id: 'T-07', name: 'Histórico' },
    { file: 'T08-emergencia.html',    id: 'T-08', name: 'Emergência' }
  ];

  function currentIndex() {
    var f = global.location.pathname.split('/').pop();
    for (var i = 0; i < SCREENS.length; i++) {
      if (SCREENS[i].file === f) return i;
    }
    return -1;
  }

  /* Resolve "T-03" ou "T03" para o arquivo correspondente. */
  function fileForId(raw) {
    var n = String(raw).replace(/\D/g, '');
    for (var i = 0; i < SCREENS.length; i++) {
      if (SCREENS[i].id.replace(/\D/g, '') === n) return SCREENS[i].file;
    }
    return null;
  }

  var CSS = [
    '.ajnav{position:fixed;left:50%;bottom:16px;transform:translateX(-50%);z-index:9999;',
    'display:flex;align-items:center;gap:4px;padding:6px;border-radius:999px;',
    'background:rgba(255,255,255,.92);backdrop-filter:blur(10px);',
    'box-shadow:0 6px 24px rgba(15,23,42,.22);font-family:var(--aj-font);}',
    '.ajnav a,.ajnav span{display:inline-flex;align-items:center;gap:6px;',
    'text-decoration:none;font-size:12px;font-weight:600;color:#052577;',
    'padding:8px 14px;border-radius:999px;white-space:nowrap;}',
    '.ajnav a:hover{background:#E9F0FC;}',
    '.ajnav .ajnav-now{color:#94A3B8;font-weight:600;letter-spacing:.08em;text-transform:uppercase;font-size:11px;}',
    '.ajnav .ajnav-off{color:#CBD5E1;pointer-events:none;}',
    '.ajnav .ajnav-home{background:#052577;color:#fff;}',
    '.ajnav .ajnav-home:hover{background:#03153F;}',
    '.ajnav-sel{appearance:none;border:0;background:transparent;font-family:inherit;',
    'font-size:12px;font-weight:600;color:#052577;padding:8px 10px;border-radius:999px;cursor:pointer;}',
    'body{padding-bottom:88px;}',
    '@media (max-width:520px){.ajnav .ajnav-lbl{display:none;}}'
  ].join('');

  /* A barra é ferramenta de desenvolvimento, não parte do app. Só aparece
     quando a URL pede: o índice em index.html liga as telas com "?nav=1".
     Abrir a tela direto (/app/...) entrega o app sem cromo em volta. */
  var NAV_FLAG = '?nav=1';

  function navRequested() {
    return /[?&]nav=/.test(global.location.search);
  }

  function withNav(file) {
    return file + NAV_FLAG;
  }

  function build() {
    if (!navRequested()) return;

    var i = currentIndex();
    if (i < 0 || document.querySelector('.ajnav')) return;

    var style = document.createElement('style');
    style.textContent = CSS;
    document.head.appendChild(style);

    var prev = SCREENS[i - 1];
    var next = SCREENS[i + 1];
    var nav = document.createElement('nav');
    nav.className = 'ajnav';
    nav.setAttribute('aria-label', 'Navegação do protótipo');

    nav.innerHTML =
      '<a class="ajnav-home" href="index.html">◱ <span class="ajnav-lbl">Todas as telas</span></a>' +
      (prev
        ? '<a href="' + withNav(prev.file) + '">← <span class="ajnav-lbl">' + prev.id + ' ' + prev.name + '</span></a>'
        : '<span class="ajnav-off">←</span>') +
      '<span class="ajnav-now">' + SCREENS[i].id + '</span>' +
      (next
        ? '<a href="' + withNav(next.file) + '"><span class="ajnav-lbl">' + next.id + ' ' + next.name + '</span> →</a>'
        : '<span class="ajnav-off">→</span>');

    /* Seletor pra pular direto pra qualquer tela. */
    var sel = document.createElement('select');
    sel.className = 'ajnav-sel';
    sel.setAttribute('aria-label', 'Pular para tela');
    SCREENS.forEach(function (s, k) {
      var o = document.createElement('option');
      o.value = withNav(s.file);
      o.textContent = s.id + ' · ' + s.name;
      if (k === i) o.selected = true;
      sel.appendChild(o);
    });
    sel.addEventListener('change', function () { global.location.href = sel.value; });
    nav.appendChild(sel);

    document.body.appendChild(nav);
  }

  /* Rodapés "Continua em T-0N …" viram links de verdade. */
  function linkFooters() {
    var nodes = document.querySelectorAll('body *');
    Array.prototype.forEach.call(nodes, function (el) {
      if (el.children.length > 1 || el.dataset.ajLinked) return;
      var m = /Continua em\s+(T-?\d\d)/i.exec(el.textContent || '');
      if (!m) return;
      var file = fileForId(m[1]);
      if (!file) return;
      el.dataset.ajLinked = '1';
      el.setAttribute('role', 'link');
      el.setAttribute('tabindex', '0');
      /* Uma aparência só para todas as telas, no lugar dos seis estilos
         próprios que cada uma tinha. A seta some do texto: agora ela é
         desenhada pelo CSS. */
      /* Descarta o estilo próprio da tela: ele vive no <style> dela, que carrega
         depois do tokens.css e venceria o desempate de especificidade. */
      Array.prototype.slice.call(el.classList).forEach(function (c) {
        if (/^t\d+-next$/.test(c)) el.classList.remove(c);
      });
      el.classList.add('aj-next');
      el.textContent = (el.textContent || '').replace(/\s*[→>]\s*$/, '');
      el.addEventListener('click', function () { global.location.href = file; });
      el.addEventListener('keydown', function (e) {
        if (e.key === 'Enter' || e.key === ' ') { e.preventDefault(); global.location.href = file; }
      });
    });
  }

  /* Qualquer elemento com data-aj-go="arquivo.html" navega ao clicar. */
  function wireGo() {
    document.addEventListener('click', function (e) {
      var t = e.target.closest ? e.target.closest('[data-aj-go]') : null;
      if (!t) return;
      global.location.href = t.getAttribute('data-aj-go');
    });
  }

  /* O passo seguinte fica sempre por último na rolagem. Antes ele aparecia em
     posição variável conforme a tela, e era fácil não achar. Só move quando
     ainda não está no fim, senão a própria movimentação realimentaria o
     observador de mutações. */
  function fixarNoFim() {
    var todos = document.querySelectorAll('.aj-next');
    Array.prototype.forEach.call(todos, function (el) {
      var pai = el.parentNode;
      if (pai && pai.lastElementChild !== el) pai.appendChild(el);
    });
  }

  function init() {
    build();
    wireGo();
    linkFooters();
    fixarNoFim();
    /* telas revelam rodapé depois da animação — reobserva. */
    var mo = new MutationObserver(function () {
      linkFooters();
      fixarNoFim();
    });
    mo.observe(document.body, { childList: true, subtree: true, attributes: true, attributeFilter: ['hidden', 'class'] });
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }

  global.AJ.SCREENS = SCREENS;
})(window);
