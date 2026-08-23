# Prompt — Protótipo Auto Justo: Fluxo Diagnóstico Conversacional (v2)

## Contexto para a IA

Você vai criar um protótipo mobile de alta fidelidade de um aplicativo chamado **Auto Justo** — uma plataforma AI native conversacional que ajuda motoristas a diagnosticar problemas no carro, encontrar mecânicos de confiança e resolver situações de emergência.

A interface principal é um **chat conversacional** (estilo WhatsApp), onde a IA da Auto Justo conduz toda a jornada. O cliente envia mensagens (texto, áudio, foto) e a IA responde com orientações, diagnósticos e ações — tudo dentro da conversa.

---

## O que construir

Uma **tela única de chat** com uma conversa pré-montada que simula a jornada completa de um cliente com problema na bateria do carro. A conversa já aparece pronta na tela (como um histórico de chat), com scroll vertical para o usuário percorrer toda a interação.

A interação inclui **3 momentos de clique real** no protótipo (detalhados abaixo). O restante é conteúdo estático que demonstra o fluxo.

---

## Paleta e estilo visual

- **Fundo do chat:** `#F4F7FC` (off-white frio)
- **Bolhas do cliente (direita):** `#052577` (navy da marca) com texto branco
- **Bolhas da Auto Justo (esquerda):** `#FFFFFF` com texto `#2D3748`, borda sutil `#E2E8F0`
- **Ações, links e botão enviar:** `#0136AB` (azul da marca); hover/ativo `#084DB1`
- **Amarelo da marca (acento pontual):** `#F8C613`, texto `#6B4E00` sobre ele — chip de contexto, badge de destaque, faixa lateral de card
- **Cor de confirmação/sucesso:** `#10B981` (verde) — semântico, não é cor de marca
- **Alerta/cuidado:** `#E07A00` (laranja, para não brigar com o amarelo da marca)
- **Selo Respeitoso (badge):** `#EC4899` (pink)
- **Tipografia:** Inter ou system sans-serif, 14-15px corpo, 12px secundário
- **Wordmark "Auto Justo":** Canva Sans Bold Italic, sempre como SVG vetorizado (`assets/wordmark.svg`) — a fonte é proprietária da Canva e não pode ser embutida como webfont
- **Cantos das bolhas:** 16px, com canto inferior direito reto nas bolhas do cliente e inferior esquerdo reto nas da Auto Justo (padrão WhatsApp)
- **Header do chat:** fundo claro `#F4F7FC`, avatar = ícone do logo (`assets/logo-icon.png`, quadrado arredondado 32px), nome "Auto Justo", chip do carro em amarelo `#F8C613`
- **Largura:** 390px (mobile), centralizado na viewport

---

## Conversa completa — sequência de mensagens

Renderize todas as mensagens abaixo na ordem, como um histórico de chat. O protótipo abre com scroll posicionado no topo.

### Bloco 1 — Cliente relata o problema

**Cliente (bolha direita):**
> 📷 [Imagem: foto de um painel de carro com a luz de bateria acesa — use um placeholder retangular cinza escuro (#2D3748) com ícone de bateria em vermelho (#EF4444) no centro e texto pequeno "Luz da bateria acesa" abaixo]

**Cliente (bolha direita):**
> "Essa luz acendeu no painel do meu carro e ele não tá ligando. O que eu faço?"

**Timestamp:** "Hoje, 14:32"

---

### Bloco 2 — Auto Justo orienta (verificação imediata)

**Auto Justo (bolha esquerda):**
> "Oi! Vi a foto — essa é a luz da **bateria**. Vamos verificar algumas coisas antes de qualquer decisão."
>
> "Tenta o seguinte:"
>
> "1️⃣ Gira a chave na posição de ignição (sem forçar a partida). As luzes do painel acendem normalmente ou estão fracas?"
>
> "2️⃣ Quando você tenta ligar, faz algum barulho? (tipo um clique, ou fica totalmente mudo?)"

---

### Bloco 3 — Cliente responde

**Cliente (bolha direita):**
> "As luzes do painel ficam bem fracas e quando tento ligar só faz um clique e nada acontece"

---

### Bloco 4 — Auto Justo dá orientação prática

**Auto Justo (bolha esquerda):**
> "Entendi. Com luzes fracas e clique único, o mais provável é que a **bateria esteja descarregada ou no fim da vida útil**."
>
> "Uma coisa que pode funcionar agora:"
>
> "🔋 Se você tiver cabos de chupeta e alguém por perto com outro carro, pode tentar dar uma partida auxiliar (chupeta). Conecta o cabo vermelho no positivo (+) das duas baterias, o preto no negativo (−) do carro bom e em um ponto metálico do seu carro. Liga o outro carro, espera 2 minutos e tenta ligar o seu."
>
> "Consegue tentar isso?"

---

### Bloco 5 — Cliente diz que não funcionou

**Cliente (bolha direita):**
> "Tentei a chupeta mas não funcionou, o carro deu uma engasgada mas não ligou. Qual o próximo passo?"

---

### Bloco 6 — Auto Justo apresenta diagnóstico prévio COM estimativa de custo

**Auto Justo (bolha esquerda):**
> "Se a chupeta não resolveu, os possíveis problemas e custos estimados são:"

**[Componente: Card de diagnóstico prévio + estimativa]** — card branco com borda esquerda `#F8C613` (faixa de acento da marca), dentro da área de mensagem da Auto Justo:

```
┌──────────────────────────────────────┐
│  🔍 Diagnóstico prévio + estimativa  │
│                                      │
│  ● Bateria sem condições de carga    │
│    (mais provável)                   │
│    Peça: R$ 250–450                  │
│    Mão de obra: R$ 50–80             │
│    💰 Total estimado: R$ 300–530     │
│                                      │
│  ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─  │
│                                      │
│  ● Alternador com defeito            │
│    Peça: R$ 350–700                  │
│    Mão de obra: R$ 150–250           │
│    💰 Total estimado: R$ 500–950     │
│                                      │
│  ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─  │
│                                      │
│  ● Motor de arranque com problema    │
│    Peça: R$ 300–600                  │
│    Mão de obra: R$ 120–200           │
│    💰 Total estimado: R$ 420–800     │
│                                      │
│  📋 Baseado no seu Hyundai           │
│     HB20 2018 · 62.000 km           │
│     Preços da região de São Paulo    │
└──────────────────────────────────────┘
```

Cada hipótese mostra: nome do problema, valor da peça, valor da mão de obra e total estimado. Os valores de "Total estimado" devem ter destaque visual (bold em `#052577`).

**Auto Justo (bolha esquerda, logo abaixo do card):**
> "O mais comum para o seu modelo nessa quilometragem é a bateria mesmo — e é o mais barato de resolver. Mas um mecânico precisa testar para confirmar."

---

### Bloco 7 — Auto Justo oferece próximos passos

**Auto Justo (bolha esquerda):**
> "O que você gostaria de fazer agora?"

**[Componente: Botões de ação inline]** — dois botões empilhados, largura total da bolha, estilo outline com borda `#052577`, cantos arredondados 12px:

```
┌──────────────────────────────────┐
│  📍 Localizar mecânico com       │
│     Selo Auto Justo              │
└──────────────────────────────────┘
┌──────────────────────────────────┐
│  📋 Solicitar orçamento          │
│     detalhado a um mecânico      │
│     parceiro                     │
└──────────────────────────────────┘
```

**INTERAÇÃO REAL #1:** O botão "Localizar mecânico com Selo Auto Justo" é clicável. Ao clicar, a conversa avança e exibe os blocos 8 e 9 abaixo (que estavam ocultos). O botão clicado muda para estado preenchido (`background: #052577`, texto branco) para indicar a seleção. O outro botão fica com opacidade reduzida (0.4).

---

### Bloco 8 — Cliente seleciona (aparece após clique)

**Cliente (bolha direita):**
> "Localizar mecânico com Selo Auto Justo"

---

### Bloco 9 — Auto Justo traz mecânicos (aparece após clique)

**Auto Justo (bolha esquerda):**
> "Encontrei 3 mecânicos com Selo Auto Justo perto de você:"

**[Componente: Lista de 3 cards de mecânico]** — cards empilhados, brancos, com sombra sutil, dentro da área de mensagens:

**Card 1:**
```
┌──────────────────────────────────┐
│  🔧 Auto Elétrica Silva          │
│  ⭐ 4.8 (127 avaliações)         │
│  📍 1.2 km · Rua Augusta, 432    │
│  🏷️ Bateria · Parte elétrica     │
│  🩷 Selo de Atendimento          │
│     Respeitoso                   │
│                                  │
│  [ Ver detalhes ]                │
└──────────────────────────────────┘
```

**Card 2:**
```
┌──────────────────────────────────┐
│  🔧 Oficina Park Centro          │
│  ⭐ 4.6 (89 avaliações)          │
│  📍 2.1 km · Av. Paulista, 1578  │
│  🏷️ Elétrica · Mecânica geral    │
│  🩷 Selo de Atendimento          │
│     Respeitoso                   │
│                                  │
│  [ Ver detalhes ]                │
└──────────────────────────────────┘
```

**Card 3:**
```
┌──────────────────────────────────┐
│  🔧 MasterCar Bela Vista         │
│  ⭐ 4.5 (64 avaliações)          │
│  📍 3.4 km · Rua da Consolação,  │
│     891                          │
│  🏷️ Bateria · Alternador ·       │
│     Arranque                     │
│  🩷 Selo de Atendimento          │
│     Respeitoso                   │
│                                  │
│  [ Ver detalhes ]                │
└──────────────────────────────────┘
```

**INTERAÇÃO REAL #2:** Cada botão "Ver detalhes" é clicável. Ao clicar, o card **expande in-place** (ou abre um bottom sheet) mostrando informações adicionais:

**Conteúdo expandido (exemplo para Auto Elétrica Silva):**
```
┌──────────────────────────────────┐
│  🔧 Auto Elétrica Silva          │
│  ⭐ 4.8 (127 avaliações)         │
│  📍 Rua Augusta, 432 — Consolação│
│  🕐 Seg–Sex 8h–18h · Sáb 8h–13h │
│                                  │
│  Especialidades:                 │
│  Bateria · Alternador · Parte    │
│  elétrica · Injeção eletrônica   │
│                                  │
│  🩷 Selo de Atendimento          │
│     Respeitoso                   │
│     93% de aprovação feminina    │
│                                  │
│  📋 CNPJ verificado ✓            │
│                                  │
│  ┌────────────────────────────┐  │
│  │  ✅ Selecionar este         │  │
│  │     mecânico                │  │
│  └────────────────────────────┘  │
└──────────────────────────────────┘
```

Cada card tem seu próprio conteúdo expandido com dados específicos. Renderize os 3:

- **Oficina Park Centro:** ⭐ 4.6, Av. Paulista 1578 — Bela Vista, Seg–Sex 8h–19h · Sáb 8h–14h, Especialidades: Elétrica · Mecânica geral · Suspensão, Selo Respeitoso 87% aprovação feminina, CNPJ verificado ✓
- **MasterCar Bela Vista:** ⭐ 4.5, Rua da Consolação 891 — Consolação, Seg–Sex 7h30–18h, Especialidades: Bateria · Alternador · Arranque · Motor, Selo Respeitoso 81% aprovação feminina, CNPJ verificado ✓

**INTERAÇÃO REAL #3:** O botão "Selecionar este mecânico" (em qualquer card) é clicável. Ao clicar, exibe os blocos 10 e 11. O nome do mecânico selecionado aparece na mensagem do cliente no bloco 10.

---

### Bloco 10 — Cliente confirma (aparece após seleção do mecânico)

**Cliente (bolha direita):**
> "Quero esse — [nome do mecânico selecionado]"

(O texto muda dinamicamente conforme o mecânico escolhido.)

---

### Bloco 11 — Auto Justo conecta com o mecânico

**Auto Justo (bolha esquerda):**
> "Ótima escolha! A [nome do mecânico] tem excelente avaliação em serviços de bateria e parte elétrica."
>
> "Aqui está o contato direto:"

**[Componente: Card de contato]** — card com fundo `#10B981` suave (10% opacity), borda `#10B981`:

Os dados de contato mudam conforme o mecânico selecionado:

- **Auto Elétrica Silva:** WhatsApp (11) 98765-4321, Telefone (11) 3456-7890
- **Oficina Park Centro:** WhatsApp (11) 97654-3210, Telefone (11) 3567-8901
- **MasterCar Bela Vista:** WhatsApp (11) 96543-2109, Telefone (11) 3678-9012

```
┌──────────────────────────────────┐
│  🔧 [Nome do mecânico]           │
│  📍 [Endereço]                   │
│                                  │
│  ┌────────────────────────────┐  │
│  │  💬 Abrir WhatsApp          │  │
│  │     [número WhatsApp]       │  │
│  └────────────────────────────┘  │
│                                  │
│  ┌────────────────────────────┐  │
│  │  📞 Ligar                   │  │
│  │     [número telefone]       │  │
│  └────────────────────────────┘  │
└──────────────────────────────────┘
```

**Auto Justo (bolha esquerda, mensagem final):**
> "Dica: mostra pro mecânico o diagnóstico prévio que fizemos aqui — assim ele já sabe o que testar primeiro. 👆"
>
> "Depois que resolver, me conta como foi pra eu manter seu histórico atualizado! 🚗"

---

## Regras de implementação

1. **Mobile-first:** viewport 390px, centralizado. Simule o frame de um celular (bordas arredondadas, barra de status no topo).

2. **Scroll:** a conversa inteira tem scroll vertical. Comece com scroll no topo.

3. **Interações progressivas:** os blocos 8-9 ficam ocultos até o clique no botão "Localizar mecânico". Os blocos 10-11 ficam ocultos até o clique em "Selecionar este mecânico". Use animação suave de entrada (fade in + slide up, 300ms). Quando novos blocos aparecem, faça auto-scroll suave até eles.

4. **Conteúdo dinâmico:** os blocos 10 e 11 devem refletir o mecânico que o usuário efetivamente selecionou (nome, endereço, telefones). Não hardcode para um mecânico específico.

5. **Imagem do painel:** placeholder estilizado — retângulo com cantos arredondados, fundo cinza escuro (#2D3748), ícone de bateria em vermelho (#EF4444) no centro, texto pequeno "Luz da bateria acesa" abaixo.

6. **Selo Respeitoso:** sempre renderizar o badge em `#EC4899` (pink) com ícone de coração.

7. **Timestamps:** mostrar timestamps discretos entre blocos de mensagens (cinza claro, centralizado, fonte 11px).

8. **Input bar:** barra de input fixa no bottom com placeholder "Digite sua mensagem...", ícones de câmera, microfone e botão enviar — **não funcional** (é protótipo visual).

9. **Header:** fixo no topo, fundo claro `#F4F7FC`, com seta de voltar, avatar Auto Justo (ícone do logo, quadrado arredondado 32px), nome "Auto Justo", chip do carro em amarelo `#F8C613`.

---

## Stack sugerida

- **React** (JSX) com Tailwind ou CSS inline
- Componente único `<AutoJustoChat />`
- Estado com `useState` para controlar revelação progressiva dos blocos
- Sem dependências externas além de React

---

## O que NÃO fazer

- Não criar múltiplas telas ou navegação entre páginas
- Não implementar input funcional — é um protótipo de demonstração
- Não usar cores fora da paleta definida
- Não colocar a IA explicando o que é a Auto Justo — ela age como se já conhecesse o cliente e o carro dele
- Não separar diagnóstico e estimativa em etapas diferentes — vêm juntos no mesmo card
