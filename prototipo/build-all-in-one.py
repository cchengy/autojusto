#!/usr/bin/env python3
"""
Gera autojusto-all-in-one.html: um único arquivo autocontido com as 9 telas.

Cada tela vira um iframe com srcdoc próprio — isolamento total de IDs e de
escopo JS, que é o que permite juntar telas que usam os mesmos ids (#scroll,
#next, #replay) sem conflito.

Rode de dentro de prototipo/:   python3 build-all-in-one.py
"""

import base64
import pathlib

HERE = pathlib.Path(__file__).parent
OUT = HERE / "autojusto-all-in-one.html"

# marca o fechamento de <script> real durante o transporte dentro do arquivo único
CLOSE_TOKEN = "@@AJ_SCRIPT_CLOSE@@"

SCREENS = [
    ("T-00", "Cadastro",          "T00-onboarding.html",     "Foto do CRLV, IA extrai os dados, cliente só valida."),
    ("T-01", "Chat",              "T01-chat.html",           "A home. Onde 90% da experiência acontece."),
    ("T-02", "Diagnóstico",       "T02-diagnostico.html",    "Hipótese em linguagem leiga e custo estimado."),
    ("T-03", "Oficinas",          "T03-oficinas.html",       "A IA faz a curadoria em vez de o cliente filtrar."),
    ("T-04", "Perfil da oficina", "T04-perfil-oficina.html", "8 critérios, CNPJ verificado, comentários."),
    ("T-05", "Orçamentos",        "T05-orcamentos.html",     "A IA interpreta os números, não só mostra."),
    ("T-06", "Agendamento",       "T06-agendamento.html",    "A IA sugere, o calendário executa."),
    ("T-07", "Histórico",         "T07-historico.html",      "Avaliação por conversa e preventiva proativa."),
    ("T-08", "Emergência",        "T08-emergencia.html",     "Duas perguntas e um contato. Fricção mínima."),
]

# O host já desenha a moldura do device; dentro do iframe ela vira dobrada.
EMBED_CSS = """
<style>
  /* embed — quem desenha moldura, sombra e canto é o host */
  html, body { background: transparent; }
  .aj-device {
    margin: 0 auto;
    box-shadow: none;
    border-radius: 0;
    height: 100%;
  }
</style>
"""

# Dentro do iframe, qualquer navegação vira postMessage pro host.
SHIM = """
<script>
/* embed shim — o protótipo all-in-one não tem arquivos separados pra navegar */
(function () {
  'use strict';
  function fileOf(el) {
    if (!el) return null;
    var direct = el.getAttribute && el.getAttribute('data-aj-go');
    if (direct) return direct;
    var m = /Continua em\\s+(T-?\\d\\d)/i.exec(el.textContent || '');
    if (m) return 'T' + m[1].replace(/\\D/g, '') + '.html';
    var href = el.getAttribute && el.getAttribute('href');
    if (href && /\\.html$/.test(href)) return href;
    return null;
  }
  window.addEventListener('click', function (e) {
    var t = e.target.closest
      ? e.target.closest('[data-aj-go],[data-aj-linked],a[href$=".html"]')
      : null;
    var f = fileOf(t);
    if (!f) return;
    e.preventDefault();
    e.stopPropagation();
    parent.postMessage({ ajGo: f }, '*');
  }, true);
})();
</script>
"""


def inline(path: pathlib.Path, tokens_css: str, aj_js: str) -> str:
    html = path.read_text(encoding="utf-8")

    # o favicon do arquivo solto aponta para assets/; dentro do srcdoc nao resolve
    html = html.replace('<link rel="icon" type="image/png" href="assets/favicon.png">\n', "")

    link = '<link rel="stylesheet" href="tokens.css">'
    if link not in html:
        raise SystemExit(f"{path.name}: <link tokens.css> não encontrado")
    html = html.replace(link, "<style>\n" + tokens_css + "\n</style>\n" + EMBED_CSS)

    tag = '<script src="aj.js"></script>'
    if tag not in html:
        raise SystemExit(f"{path.name}: <script aj.js> não encontrado")
    # aj.js cita "</script>" dentro de um comentário; inline, isso fecharia a tag
    # antes da hora. Escapado assim continua válido como JS e inofensivo no parser.
    safe_js = aj_js.replace("</script", "<\\/script")
    html = html.replace(tag, "<script>\n" + safe_js + "\n</script>\n" + SHIM)

    return html


def main() -> None:
    tokens_css = (HERE / "tokens.css").read_text(encoding="utf-8")
    aj_js = (HERE / "aj.js").read_text(encoding="utf-8")
    # logo embutido no shell: o all-in-one precisa rodar como arquivo solto
    logo_b64 = base64.b64encode(
        (HERE / "assets" / "logo-icon-128.png").read_bytes()
    ).decode("ascii")

    blocks = []
    for i, (sid, name, filename, desc) in enumerate(SCREENS):
        src = HERE / filename
        if not src.exists():
            raise SystemExit(f"faltando: {filename}")
        doc = inline(src, tokens_css, aj_js)
        # </script> real quebraria o <script type="text/plain"> que carrega isso.
        # Sentinela própria, e não "<\\/script": o aj.js JÁ usa essa forma escapada
        # de propósito, e um unescape global no host desfaria essa proteção.
        doc = doc.replace("</script", CLOSE_TOKEN)
        blocks.append(
            f'<script type="text/plain" class="aj-src" '
            f'data-id="{sid}" data-file="{filename}" data-name="{name}" '
            f'data-desc="{desc}">\n{doc}\n</script>'
        )

    wordmark_b64 = base64.b64encode(
        (HERE / "assets" / "wordmark.svg").read_bytes()
    ).decode("ascii")
    host = HOST.replace("@@LOGO_B64@@", logo_b64)
    host = host.replace("@@WORDMARK_B64@@", wordmark_b64)
    OUT.write_text(host.replace("<!--SOURCES-->", "\n".join(blocks)), encoding="utf-8")
    kb = OUT.stat().st_size / 1024
    print(f"ok → {OUT.name} ({kb:.0f} KB, {len(SCREENS)} telas)")


HOST = r"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Auto Justo — Protótipo completo</title>
<link rel="icon" type="image/png" href="data:image/png;base64,@@LOGO_B64@@">
<style>
  :root {
    --ink:      #03153F;
    --ink-2:    #5A6B7D;
    --accent:   #0136AB;
    --navy:     #052577;
    --yellow:   #F8C613;
    --brand-logo: url("data:image/png;base64,@@LOGO_B64@@");
    --surface:  #FFFFFF;
    --field:    #C6D2DE;
    --line:     rgba(15,31,48,.12);
    --font: "Inter", -apple-system, BlinkMacSystemFont, "SF Pro Text", system-ui, sans-serif;
  }
  * { box-sizing: border-box; }
  html, body {
    margin: 0; padding: 0;
    background: var(--field);
    font-family: var(--font);
    color: var(--ink);
    -webkit-font-smoothing: antialiased;
  }

  /* ---------- barra superior ---------- */
  .bar {
    position: sticky; top: 0; z-index: 40;
    display: flex; align-items: center; gap: 16px;
    padding: 14px 20px;
    background: rgba(255,255,255,.86);
    backdrop-filter: blur(14px);
    border-bottom: 1px solid var(--line);
    flex-wrap: wrap;
  }
  .brand { display: flex; align-items: center; gap: 10px; margin-right: 4px; }
  .brand__mark {
    width: 30px; height: 30px; border-radius: 8px;
    background: var(--brand-logo) center / cover no-repeat;
    font-size: 0; color: transparent;
  }
  .brand__name {
    width: 101px; height: 16px;
    background: url("data:image/svg+xml;base64,@@WORDMARK_B64@@") left center / contain no-repeat;
    text-indent: -9999px; overflow: hidden; white-space: nowrap;
  }
  .brand__sub { font-size: 11px; color: var(--ink-2); font-weight: 600; letter-spacing: .06em; text-transform: uppercase; }

  .seg {
    display: flex; gap: 2px; padding: 3px;
    background: rgba(15,31,48,.06);
    border-radius: 999px;
  }
  .seg button {
    border: 0; background: transparent;
    font-family: inherit; font-size: 12px; font-weight: 600;
    color: var(--ink-2);
    padding: 7px 14px; border-radius: 999px; cursor: pointer;
    transition: background 180ms ease, color 180ms ease;
  }
  .seg button.is-on { background: var(--surface); color: var(--accent); box-shadow: 0 1px 3px rgba(15,31,48,.14); }

  .tabs { display: flex; gap: 2px; overflow-x: auto; flex: 1 1 320px; scrollbar-width: none; }
  .tabs::-webkit-scrollbar { display: none; }
  .tab {
    flex: 0 0 auto;
    border: 0; background: transparent;
    font-family: inherit; font-size: 12px; font-weight: 600;
    color: var(--ink-2);
    padding: 8px 12px; border-radius: 8px; cursor: pointer;
    white-space: nowrap;
    transition: background 160ms ease, color 160ms ease;
  }
  .tab:hover { background: rgba(15,31,48,.06); color: var(--ink); }
  .tab.is-on { background: var(--accent); color: #fff; }
  .tab small { opacity: .62; font-weight: 600; margin-right: 5px; }
  .tab.is-on small { opacity: .72; }

  /* ---------- palco ---------- */
  .stage { padding: 28px 20px 64px; }

  /* modo uma tela */
  .solo { display: flex; flex-direction: column; align-items: center; gap: 18px; }
  .solo__head { text-align: center; max-width: 46ch; }
  .solo__id {
    font-size: 11px; font-weight: 700; letter-spacing: .16em;
    text-transform: uppercase; color: var(--accent);
  }
  .solo__name { font-size: 22px; font-weight: 700; margin: 4px 0 6px; letter-spacing: -.01em; }
  .solo__desc { font-size: 13px; line-height: 1.55; color: var(--ink-2); margin: 0; }

  .device-wrap {
    width: 375px; height: 812px;
    border-radius: 40px;
    overflow: hidden;
    box-shadow: 0 24px 64px rgba(15,23,42,.28);
    background: #F4F7FC;
    flex: 0 0 auto;
  }
  .device-wrap iframe { width: 375px; height: 812px; border: 0; display: block; }

  .steps { display: flex; align-items: center; gap: 8px; }
  .steps button {
    border: 1px solid var(--line);
    background: var(--surface);
    font-family: inherit; font-size: 13px; font-weight: 600;
    color: var(--accent);
    padding: 10px 18px; border-radius: 999px; cursor: pointer;
    transition: background 160ms ease, opacity 160ms ease;
  }
  .steps button:hover { background: #E9F0FC; }
  .steps button:disabled { opacity: .34; cursor: default; }
  .steps__count { font-size: 12px; font-weight: 600; color: var(--ink-2); min-width: 52px; text-align: center; }

  /* modo todas */
  .grid {
    display: grid;
    gap: 28px 20px;
    grid-template-columns: repeat(auto-fill, minmax(240px, 1fr));
    max-width: 1400px; margin: 0 auto;
  }
  .cell { display: flex; flex-direction: column; gap: 10px; }
  .cell__frame {
    width: 100%;
    aspect-ratio: 375 / 812;
    border-radius: 26px;
    overflow: hidden;
    box-shadow: 0 10px 30px rgba(15,23,42,.20);
    background: #F4F7FC;
    position: relative;
    cursor: pointer;
  }
  .cell__frame iframe {
    width: 375px; height: 812px; border: 0;
    transform-origin: top left;
    position: absolute; top: 0; left: 0;
    pointer-events: none;
  }
  .cell__open {
    position: absolute; inset: 0;
    background: rgba(5,37,119,0);
    display: grid; place-items: center;
    transition: background 180ms ease;
  }
  .cell__open span {
    opacity: 0;
    background: rgba(255,255,255,.95);
    color: var(--accent);
    font-size: 12px; font-weight: 700;
    padding: 8px 16px; border-radius: 999px;
    transition: opacity 180ms ease;
  }
  .cell__frame:hover .cell__open { background: rgba(5,37,119,.22); }
  .cell__frame:hover .cell__open span { opacity: 1; }
  .cell__cap { display: flex; align-items: baseline; gap: 8px; }
  .cell__id { font-size: 11px; font-weight: 700; letter-spacing: .12em; color: var(--accent); }
  .cell__name { font-size: 14px; font-weight: 600; }

  .hint {
    max-width: 1400px; margin: 40px auto 0;
    padding-top: 18px; border-top: 1px solid var(--line);
    font-size: 12px; line-height: 1.7; color: var(--ink-2);
  }
  .hint kbd {
    background: var(--surface); border: 1px solid var(--line);
    border-bottom-width: 2px;
    border-radius: 5px; padding: 1px 6px;
    font-family: inherit; font-size: 11px; font-weight: 600; color: var(--ink);
  }

  [hidden] { display: none !important; }

  @media (max-width: 460px) {
    .device-wrap { width: 100%; max-width: 375px; }
  }
</style>
</head>
<body>

<div class="bar">
  <div class="brand">
    <div class="brand__mark">AJ</div>
    <div>
      <div class="brand__name">Auto Justo</div>
      <div class="brand__sub">protótipo · 9 telas</div>
    </div>
  </div>

  <div class="seg" role="tablist" aria-label="Modo de visualização">
    <button id="modeSolo" class="is-on" type="button">Uma tela</button>
    <button id="modeGrid" type="button">Todas</button>
  </div>

  <div class="tabs" id="tabs"></div>
</div>

<main class="stage">

  <section class="solo" id="solo">
    <div class="solo__head">
      <div class="solo__id" id="soloId"></div>
      <h1 class="solo__name" id="soloName"></h1>
      <p class="solo__desc" id="soloDesc"></p>
    </div>

    <div class="device-wrap"><iframe id="soloFrame" title="Tela do protótipo"></iframe></div>

    <div class="steps">
      <button id="prev" type="button">← anterior</button>
      <span class="steps__count" id="count"></span>
      <button id="next" type="button">próxima →</button>
    </div>
  </section>

  <section class="grid" id="grid" hidden></section>

  <p class="hint">
    <strong>Navegação:</strong> os botões dentro das telas levam pra tela seguinte de verdade — clique em
    “Ver oficinas perto de mim”, “Pedir orçamento”, “Escolher esta oficina”. Use <kbd>←</kbd> <kbd>→</kbd>
    pra trocar de tela e <kbd>G</kbd> pra alternar entre uma e todas.<br>
    <strong>Arquivo único:</strong> tudo embutido aqui — CSS, JS e as 9 telas. Funciona sem servidor, sem
    internet e sem dependência externa. Cada tela roda isolada em seu próprio iframe.
  </p>

</main>

<!--SOURCES-->

<script>
(function () {
  'use strict';

  var raw = Array.prototype.map.call(
    document.querySelectorAll('script.aj-src'),
    function (s) {
      return {
        id:   s.dataset.id,
        file: s.dataset.file,
        name: s.dataset.name,
        desc: s.dataset.desc,
        /* nunca escrever '</scr'+'ipt' inteiro aqui: fecharia esta própria tag */
        html: s.textContent.split('@@AJ_SCRIPT_CLOSE@@').join('<' + '/script')
      };
    }
  );

  var tabsEl  = document.getElementById('tabs');
  var solo    = document.getElementById('solo');
  var grid    = document.getElementById('grid');
  var frame   = document.getElementById('soloFrame');
  var soloId  = document.getElementById('soloId');
  var soloNm  = document.getElementById('soloName');
  var soloDs  = document.getElementById('soloDesc');
  var prevBtn = document.getElementById('prev');
  var nextBtn = document.getElementById('next');
  var countEl = document.getElementById('count');
  var bSolo   = document.getElementById('modeSolo');
  var bGrid   = document.getElementById('modeGrid');

  var cur = 0;
  var mode = 'solo';
  var gridBuilt = false;

  function indexOfFile(file) {
    for (var i = 0; i < raw.length; i++) if (raw[i].file === file) return i;
    return -1;
  }

  /* ---------- tabs ---------- */
  raw.forEach(function (s, i) {
    var b = document.createElement('button');
    b.className = 'tab';
    b.type = 'button';
    b.innerHTML = '<small>' + s.id + '</small>' + s.name;
    b.addEventListener('click', function () { show(i); });
    tabsEl.appendChild(b);
  });
  var tabBtns = Array.prototype.slice.call(tabsEl.children);

  /* ---------- modo uma tela ---------- */
  function show(i) {
    cur = Math.max(0, Math.min(raw.length - 1, i));
    var s = raw[cur];

    if (mode !== 'solo') setMode('solo');

    frame.srcdoc = s.html;
    frame.title = s.id + ' ' + s.name;
    soloId.textContent = s.id;
    soloNm.textContent = s.name;
    soloDs.textContent = s.desc;
    countEl.textContent = (cur + 1) + ' / ' + raw.length;
    prevBtn.disabled = cur === 0;
    nextBtn.disabled = cur === raw.length - 1;

    tabBtns.forEach(function (b, k) { b.classList.toggle('is-on', k === cur); });
    tabBtns[cur].scrollIntoView({ block: 'nearest', inline: 'nearest' });
  }

  prevBtn.addEventListener('click', function () { show(cur - 1); });
  nextBtn.addEventListener('click', function () { show(cur + 1); });

  /* ---------- modo todas ---------- */
  function buildGrid() {
    if (gridBuilt) return;
    gridBuilt = true;

    raw.forEach(function (s, i) {
      var cell = document.createElement('div');
      cell.className = 'cell';

      var box = document.createElement('div');
      box.className = 'cell__frame';
      box.addEventListener('click', function () { show(i); });

      var f = document.createElement('iframe');
      f.title = s.id + ' ' + s.name;
      f.setAttribute('scrolling', 'no');
      f.srcdoc = s.html;
      box.appendChild(f);

      var ov = document.createElement('div');
      ov.className = 'cell__open';
      ov.innerHTML = '<span>abrir ' + s.id + '</span>';
      box.appendChild(ov);

      var cap = document.createElement('div');
      cap.className = 'cell__cap';
      cap.innerHTML = '<span class="cell__id">' + s.id + '</span>' +
                      '<span class="cell__name">' + s.name + '</span>';

      cell.appendChild(box);
      cell.appendChild(cap);
      grid.appendChild(cell);
    });

    scaleGrid();
  }

  /* o iframe tem 375px fixos; a célula é fluida — escala pra caber */
  function scaleGrid() {
    Array.prototype.forEach.call(grid.querySelectorAll('.cell__frame'), function (box) {
      var f = box.querySelector('iframe');
      if (f) f.style.transform = 'scale(' + (box.clientWidth / 375) + ')';
    });
  }
  window.addEventListener('resize', function () { if (mode === 'grid') scaleGrid(); });

  function setMode(m) {
    mode = m;
    var isGrid = m === 'grid';
    bGrid.classList.toggle('is-on', isGrid);
    bSolo.classList.toggle('is-on', !isGrid);
    grid.hidden = !isGrid;
    solo.hidden = isGrid;
    if (isGrid) { buildGrid(); scaleGrid(); }
  }

  bSolo.addEventListener('click', function () { setMode('solo'); });
  bGrid.addEventListener('click', function () { setMode('grid'); });

  /* ---------- navegação vinda de dentro das telas ---------- */
  window.addEventListener('message', function (e) {
    var go = e.data && e.data.ajGo;
    if (!go) return;
    var i = indexOfFile(go);
    if (i >= 0) show(i);
  });

  /* ---------- teclado ---------- */
  document.addEventListener('keydown', function (e) {
    if (e.target && /^(INPUT|TEXTAREA)$/.test(e.target.tagName)) return;
    if (e.key === 'ArrowRight') { show(cur + 1); }
    else if (e.key === 'ArrowLeft') { show(cur - 1); }
    else if (e.key === 'g' || e.key === 'G') { setMode(mode === 'grid' ? 'solo' : 'grid'); }
  });

  show(0);
})();
</script>

</body>
</html>
"""


if __name__ == "__main__":
    main()
