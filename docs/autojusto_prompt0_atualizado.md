# Auto Justo — Prompt 0 Atualizado (com referência visual)

## Como usar

1. Abra a ferramenta de design com IA
2. Faça upload dos 3 arquivos .md do projeto + as 6 imagens de referência (ref_01 a ref_06)
3. Cole o prompt abaixo

---

## PROMPT 0 — Briefing Inicial (versão atualizada)

```
Estou criando um app mobile chamado Auto Justo. Anexei 3 arquivos que descrevem tudo sobre o projeto:

- autojusto_solucao_ai_native.md → a solução completa com todas as funcionalidades
- autojusto_user_flow_map.md → mapa de fluxos, inventário de telas (T-00 a T-08) e componentes inline do chat (C-01 a C-08)
- compilacao_pitch.md → contexto do problema, público-alvo e mercado

Também anexei 6 imagens de referência visual de um app que é o modelo de estilo que quero seguir. Analise todas elas com atenção.

---

SOBRE O APP:
- App mobile-first (375px de largura, proporção de iPhone)
- Conversational-first: a tela de chat (T-01) é a home e onde 90% da experiência acontece
- A IA é a interface principal — o cliente conversa, não navega por menus
- Público: homens e mulheres, 25-45 anos, sem conhecimento técnico de carros, em grandes cidades brasileiras
- Língua: português brasileiro

---

DIREÇÃO VISUAL — BASEADA NAS IMAGENS DE REFERÊNCIA:

O app de referência é um assistente conversacional de compras. Quero o MESMO estilo de interface para o Auto Justo, com os ajustes que descrevo abaixo.

PADRÕES QUE QUERO REPLICAR EXATAMENTE:

1. ESTRUTURA GERAL DO CHAT
   - A conversa é a tela inteira, sem abas laterais nem menus complexos
   - Header mínimo no topo: avatar + nome do assistente + contexto/modo à direita
   - Input na parte inferior: campo pill/arredondado com placeholder "Mensagem" + botão de envio circular
   - A tela respira — bastante espaço vazio entre os elementos

2. BOLHAS DE MENSAGEM
   - Mensagem do USUÁRIO: bolha escura (preta no original), texto branco, alinhada à direita, cantos bem arredondados, largura se adapta ao conteúdo
   - Mensagem da IA/SISTEMA: SEM bolha. O texto aparece direto no fundo da tela, alinhado à esquerda, como se fosse texto corrido. Isso dá um tom leve e conversacional, sem peso visual
   - Essa assimetria (bolha escura do usuário vs texto solto da IA) é a assinatura visual mais importante do app de referência

3. CHECKLIST DE PROGRESSO (microinteração)
   - Quando a IA está processando algo, aparece uma lista de etapas com checkmarks verdes (✓) que vão marcando uma a uma, como se estivessem sendo completadas em tempo real
   - Ex: ✓ Histórico de pedidos / ✓ 3 lojas verificadas / ✓ Frete para 04538-133
   - No Auto Justo, usar para: ✓ Analisando seu HB20 2018 / ✓ Base técnica consultada / ✓ Problemas comuns verificados / ✓ Estimativa calculada

4. CARDS INLINE (ofertas/opções)
   - Cards brancos com sombra mínima, cantos arredondados
   - Header em caps lock pequeno ("3 OFERTAS")
   - Cada item dentro do card tem: ícone/thumb + nome + info secundária (cinza) + preço à direita
   - Item selecionado: fundo levemente destacado (tom claro) + checkmark verde
   - Layout em lista vertical, NÃO em carrossel horizontal

5. CARD DE AÇÃO/RESUMO
   - Card branco separado com as informações finais + botão de ação grande
   - Ex do original: produto + cartão + endereço + total → botão "Revisar e pagar"
   - No Auto Justo: oficina + serviço + estimativa → botão "Agendar" ou "Pedir orçamento"
   - Botão de ação: arredondado, cor sólida (verde-escuro no original), texto branco, centralizado, largura total do card

6. BOTTOM SHEET (confirmação)
   - Para ações importantes, um painel sobe de baixo com fundo branco
   - Tem um "handle" sutil no topo (barrinha cinza centralizada)
   - Texto em caps: "CONFIRME VOCÊ MESMO" / "PAGAMENTO APROVADO"
   - Valor em destaque grande
   - Ícone de confirmação animado (círculo verde + check)
   - No Auto Justo, usar para: confirmação de agendamento, confirmação de envio de orçamento

7. MICROINTERAÇÕES QUE QUERO
   - Texto da IA aparecendo palavra por palavra (efeito de digitação)
   - Itens do checklist aparecendo um por um com animação fade-in + check
   - Cards surgindo de baixo pra cima com slide suave
   - Bottom sheet subindo com animação spring
   - Ícone de confirmação (check dentro do círculo) com animação de preenchimento

---

ADAPTAÇÃO DE COR PARA O AUTO JUSTO:

O app de referência usa fundo rosa/bege (#F0E8E4) e acentos em verde. Quero adaptar assim:

PALETA AUTO JUSTO — lida do logo da marca:
- Fundo principal: branco levemente azulado — #F4F7FC (off-white frio, não quente como o rosa do original)
- Bolha do usuário: azul-marinho da marca — #052577 (no lugar do preto do original)
- Texto da IA: cinza escuro — #2D3748 (texto solto no fundo, sem bolha)
- Acento primário (botões, send, links): azul da marca — #0136AB
- Hover / estado ativo: azul vivo — #084DB1
- Amarelo da marca — #F8C613, texto #6B4E00 sobre ele. Acento pontual: chip de contexto do carro, badge de destaque, faixa lateral de card. Nunca como cor de fundo grande.
- Confirmação/sucesso: verde — #10B981. Semântico, não é cor de marca: só checks, "Respondeu", confirmação de agendamento.
- Cards: branco puro #FFFFFF com sombra sutil (0 2px 8px rgba(0,0,0,0.06))
- Fundo sutil de item selecionado: #E9F0FC
- Header/badge de contexto: amarelo suave com borda — o "🚗 HB20 2018" no topo do chat
- Textos secundários: #94A3B8 (cinza-azulado)
- Alerta/cuidado: #E07A00 (laranja) — para orçamentos fora do padrão. Laranja e não âmbar, senão briga com o amarelo #F8C613 da marca.
- Selo respeitoso: #EC4899 (rosa) — cor dedicada ao selo de atendimento a mulheres

REGRA DA MARCA: azul domina (fundos, bolhas, ações) e o amarelo é o sujeito, aparecendo em poucos pontos. É a mesma proporção do logo — quadrado azul, carro e polegar amarelos.

TIPOGRAFIA:
- Mesma limpeza do app de referência
- Font principal: Inter ou SF Pro (sem serifa, moderna)
- Wordmark "Auto Justo": Canva Sans Bold Italic. A fonte é proprietária da Canva e não pode ser embutida como webfont — a assinatura entra sempre como SVG vetorizado (`prototipo/assets/wordmark.svg`), nunca como texto numa fonte substituta.
- Ícone do app: `prototipo/assets/logo-icon.png` — quadrado arredondado, usado como avatar da Auto Justo no header
- Tamanhos generosos — legibilidade como prioridade
- Headers de card em caps lock espaçado (tracking wide) como no original: "3 OFERTAS" → "3 OFICINAS"

---

REGRA DE OURO:
Se eu tirar uma screenshot do Auto Justo e colocar ao lado do app de referência, a linguagem visual precisa ser da mesma família. A diferença é só a paleta (azul-marinho no lugar de preto/rosa) e o conteúdo (mecânico no lugar de compras). A estrutura, o ritmo visual, o espaçamento, a tipografia e as microinterações devem ser praticamente idênticos.

---

Leia os 3 arquivos e as 6 imagens de referência com atenção. Vou pedir as telas uma por uma, sempre referenciando os IDs do flow map (T-00, T-01, C-01, etc). Confirme que entendeu o projeto e a direção visual antes de começarmos.
```

---

## O QUE MUDA NOS PROMPTS SEGUINTES

Com o Prompt 0 acima definindo a direção visual, os prompts 1 a 15 do guia anterior continuam válidos. A única mudança é que agora você pode adicionar lembretes curtos como:

**No Prompt 2 (Chat principal), acrescente no final:**
```
Lembre-se: bolha do usuário em azul-marinho (#052577), texto da IA sem bolha (solto no fundo), input pill com placeholder "Mensagem". Seguir o estilo das imagens de referência.
```

**No Prompt 3 (Diagnóstico), acrescente:**
```
Quando a IA estiver processando o diagnóstico, mostre o checklist de progresso animado:
✓ Analisando seu HB20 2018
✓ Base técnica consultada  
✓ Problemas comuns verificados
✓ Estimativa calculada
Cada item aparece um por um, como nas imagens de referência.
```

**No Prompt 4 (Cards de mecânico), acrescente:**
```
Use o mesmo estilo dos cards de ofertas da referência: header em caps "3 OFICINAS RECOMENDADAS", lista vertical com nome + info + nota à direita, item recomendado com fundo azul-claro sutil + check azul-marinho.
```

**No Prompt 6 (Orçamentos), acrescente:**
```
Use o padrão de cards do app de referência: header "3 ORÇAMENTOS", lista vertical com oficina + info + preço. Badge de alerta laranja (#E07A00) no orçamento fora do padrão. Abaixo, card de ação com resumo + botão "Escolher oficina" (azul da marca #0136AB, largura total).
```

**No Prompt 8 (Agendamento - confirmação), acrescente:**
```
Ao confirmar o agendamento, use bottom sheet subindo de baixo como na referência:
- Handle sutil no topo
- "AGENDAMENTO CONFIRMADO" em caps
- Oficina + data + horário em destaque
- Ícone de check animado (círculo verde-azulado + check branco)
- Texto: "Vou te avisar depois pra saber como foi"
```

---

## IMAGENS DE REFERÊNCIA — O QUE CADA UMA MOSTRA

Ao fazer upload das 6 imagens na ferramenta de design, use esta descrição:

| Arquivo | O que mostra | Padrão a replicar |
|---|---|---|
| ref_01 | Tela inicial — chat vazio, input com texto, header mínimo | Estrutura base do chat, fundo, header, input |
| ref_02 | Checklist de progresso — IA processando com checks verdes | Microinteração de progresso/loading |
| ref_03 | Cards de ofertas — lista de 3 opções com preço | Estilo dos cards inline (C-01, C-02) |
| ref_04 | Card de ação — resumo de pagamento com botão CTA | Estilo do card de resumo/ação |
| ref_05 | Bottom sheet — confirmação com biometria | Padrão de bottom sheet para confirmações |
| ref_06 | Confirmação aprovada — check verde + recibo | Tela de sucesso com animação de check |
