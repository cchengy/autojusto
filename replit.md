# Auto Justo

App mobile AI native que resolve a desconfiança entre motoristas e oficinas mecânicas: o cliente descreve o problema em linguagem leiga, a IA levanta a hipótese, estima o custo com peça e mão de obra separadas, recomenda oficina verificada e acompanha até o pós-serviço.

## Run & Operate

- `pnpm --filter @workspace/api-server run dev` — run the API server (port 5000)
- `pnpm run typecheck` — full typecheck across all packages
- `pnpm run build` — typecheck + build all packages
- `pnpm --filter @workspace/api-spec run codegen` — regenerate API hooks and Zod schemas from the OpenAPI spec
- `pnpm --filter @workspace/db run push` — push DB schema changes (dev only)
- Required env: `DATABASE_URL` — Postgres connection string

## Stack

- pnpm workspaces, Node.js 24, TypeScript 5.9
- API: Express 5
- DB: PostgreSQL + Drizzle ORM
- Validation: Zod (`zod/v4`), `drizzle-zod`
- API codegen: Orval (from OpenAPI spec)
- Build: esbuild (CJS bundle)

## Where things live

- `docs/` — fonte da verdade do produto. `autojusto_solucao_ai_native.md` (funcionalidades e jornada), `compilacao_pitch.md` (problema, público, mercado), `autojusto_prompt0_atualizado.md` (direção visual).
- `prototipo/` — as 9 telas do app (T-00 a T-08) em HTML/CSS/JS puro, sem dependência externa. `tokens.css` tem a paleta e os componentes; `aj.js` tem as microinterações e a navegação entre telas. Abra qualquer `T0*.html` direto no navegador.
- Visualizadores de desktop — `index.html` (índice das telas), `autojusto-all-in-one.html` (as 9 telas num arquivo só) e `build-all-in-one.py` (gerador) — existem na sua cópia local mas estão no `.gitignore`. O repositório guarda só o app.
- Ainda não implementado em código de produção: `lib/` e `artifacts/` seguem o scaffold do workspace.

## Architecture decisions

- **Paleta vem do logo, não o contrário.** `docs/brand-logo.jpeg` é a fonte da verdade: `#052577` navy, `#0136AB` azul de ação, `#084DB1` hover, `#F8C613` amarelo. Estão em `prototipo/tokens.css` e, em HSL, em `artifacts/mockup-sandbox/src/index.css`. Mudou a marca, muda esses dois arquivos.
- **Azul domina, amarelo é acento pontual.** Mesma proporção do logo — quadrado azul, carro e polegar amarelos. Amarelo só em chip de contexto, badge e faixa de card; nunca fundo grande.
- **Verde `#10B981` é semântico, não é cor de marca.** Só sucesso, check e confirmação. Por isso o alerta virou laranja `#E07A00` em vez do âmbar `#F59E0B` original: âmbar brigava com o amarelo da marca.
- **O wordmark é SVG, não texto.** "Auto Justo" é Canva Sans Bold Italic — proprietária da Canva, sem licença de webfont e sem arquivo distribuível. A assinatura é um vetor traçado do logo (`prototipo/assets/wordmark.svg`), aplicado por image replacement: o texto continua no DOM pro leitor de tela.
- **O protótipo não tem dependência externa de propósito.** Nada de Google Fonts nem CDN — o all-in-one precisa abrir offline, por e-mail, sem servidor. Logo e wordmark entram como data URI no `tokens.css`, que é o único CSS que o build inlineia.

## Product

_Describe the high-level user-facing capabilities of this app once they exist._

## User preferences

_Populate as you build — explicit user instructions worth remembering across sessions._

## Gotchas

- Mexeu em qualquer tela `T0*.html`, no `tokens.css` ou no `aj.js`? Rode `python3 build-all-in-one.py` de dentro de `prototipo/`. O `autojusto-all-in-one.html` é gerado — editar ele à mão é jogar trabalho fora.
- Logo e wordmark ficam embutidos em base64 dentro do `tokens.css`, que o build inlineia uma vez por tela. Trocar por um asset maior multiplica por 9 no arquivo final (hoje 577 KB).
- Para o wordmark, use sempre `prototipo/assets/wordmark.svg`. Não recrie "Auto Justo" com fonte itálica qualquer — não bate com o logo. No `mockup-sandbox`, `.font-display` (Plus Jakarta Sans) serve para títulos, nunca para o wordmark.
- O protótipo usa Inter; o `mockup-sandbox` carrega o bundle de fontes do Replit. São dois sistemas separados de propósito — não tente unificar sem resolver o problema do offline.
- No `mockup-sandbox`, o Vite roda com `base: BASE_PATH` (`/__mockup`). Referência a asset de `public/` escrita como `/logo-icon.png` no JSX **não** recebe o prefixo e quebra: use `` `${import.meta.env.BASE_URL}logo-icon.png` ``. Por isso o favicon do `index.html` é data URI — não depende de base nem de publicDir.

## Pointers

- See the `pnpm-workspace` skill for workspace structure, TypeScript setup, and package details
