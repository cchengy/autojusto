# Auto Justo — Solução AI Native

## Visão Geral

A Auto Justo é uma plataforma mobile AI native que resolve o problema de confiança entre motoristas e oficinas mecânicas. A experiência central do cliente é uma conversa — não formulários, não navegação por abas. O cliente abre o app, fala o que precisa, e a Auto Justo conduz.

A IA não é uma funcionalidade dentro do app. A IA é a interface principal. Ela entende o contexto do cliente, interpreta linguagem leiga, cruza com dados técnicos e age — como o amigo que entende de carro que a maioria do público-alvo não tem.

**Problema que resolve:**
"Pessoas que não confiam nos serviços mecânicos porque não conseguem avaliar se o diagnóstico é verdadeiro, se o orçamento é justo ou se o serviço entregue foi de fato o necessário."

**Pilares da solução:**

- Transparência — orçamento estimado com peça e mão de obra detalhados
- Previsibilidade — diagnóstico prévio baseado na descrição de sintomas
- Referência — avaliações de clientes sobre mecânicos na plataforma
- Segurança — verificação do perfil do mecânico por CNPJ

---

## Princípio de Design: IA Conduz, Interface Apoia

A IA é a interface principal em tudo que envolve interpretar, recomendar e agir com base em contexto: diagnóstico, estimativa, recomendação de mecânico, análise de orçamento, acompanhamento pós-serviço, manutenção preventiva e emergência.

A interface tradicional (telas, botões, listas) entra onde o cliente precisa ver, comparar visualmente ou selecionar com precisão: perfil da oficina, calendário de agendamento, histórico do carro, contatos de emergência.

---

## Jornada do Cliente — Funcionalidades

### 1. Cadastro e configuração inicial

O cliente abre o app pela primeira vez e a Auto Justo pede para tirar uma foto do documento do carro (CRLV). A IA extrai placa, modelo, ano e Renavam via leitura do documento, e confirma com o cliente: "Seu carro é um Hyundai HB20 2018, correto?" O cliente só valida. Se não tiver o documento na mão, pode digitar a placa e a IA puxa o restante via API (Fipe, Denatran).

O histórico começa do zero e se constrói naturalmente conforme o cliente usa a plataforma.

**Por que IA aqui:** elimina formulário. O cadastro vira uma conversa de 30 segundos em vez de 2 minutos de campos. Reduz abandono no onboarding, que é onde a maioria dos apps perde usuário.

---

### 2. Descrição do problema — a conversa central

O cliente fala com a Auto Justo como falaria com um amigo que entende de carro. "Meu carro tá fazendo um barulho tipo tec-tec quando eu viro o volante pra direita." A IA faz perguntas de refinamento como um mecânico faria — "Acontece só em baixa velocidade? O barulho some quando você anda em linha reta?" — mas em linguagem leiga, nunca técnica.

O cliente pode enviar:

- **Texto** — descreve a situação com suas próprias palavras
- **Áudio** — grava a descrição ou o barulho do carro
- **Foto** — registra uma luz no painel, peça com vazamento, ou qualquer evidência visual

A IA processa tudo junto. Por trás, cruza a descrição conversacional com o modelo/ano/km do carro, a base técnica de manuais do veículo, o histórico de serviços na plataforma e os problemas mais comuns daquele modelo nessa quilometragem. A hipótese sai contextualizada e em linguagem que o cliente entende.

A base técnica de manuais não é exposta ao cliente — é insumo interno que a IA utiliza para cruzar informações e tornar o diagnóstico mais assertivo.

**Por que IA aqui:** este é o ponto onde a IA é mais insubstituível. Nenhuma lista de sintomas pré-definida captura a forma como pessoas leigas descrevem problemas de carro. "Tá fazendo um barulho de panela" não encaixa em nenhum dropdown. A IA interpreta linguagem natural, faz as perguntas certas para desambiguar, e traduz isso em hipótese técnica. Isso transforma o cliente de refém em alguém informado.

---

### 3. Orientação imediata (quando aplicável)

A orientação é contextual e sai dentro da mesma conversa. Se a IA identifica que pode ser algo verificável ("pode ser que o nível de água do radiador esteja baixo"), ela orienta com linguagem direta e pergunta o resultado: "Abre o capô e olha o reservatório de água — é um recipiente transparente com marcações de mínimo e máximo. O nível está abaixo do mínimo?"

Se o cliente responde "sim", a IA ajusta a hipótese e orienta o próximo passo. Se responde "não sei onde fica", a IA pode mostrar uma imagem de referência do reservatório naquele modelo específico. Nenhuma orientação envolve abrir ou mexer em componentes do carro.

Se a verificação não resolve ou o problema é mais complexo, a IA já direciona para a próxima etapa: buscar um mecânico. Em caso de risco, orienta a parar o carro e acionar ajuda.

**Por que IA aqui:** o passo a passo fixo assume que todo cliente tem o mesmo nível de conhecimento. A conversa adaptativa percebe quando o cliente entendeu e avança, ou quando está perdido e simplifica. Isso é particularmente importante para o público feminino da pesquisa, que relatou insegurança em interações técnicas.

---

### 4. Estimativa de custo automática

A estimativa é gerada automaticamente pela IA como parte natural da conversa de diagnóstico. Assim que a hipótese se forma, a IA consulta preços de peças (via API de fornecedores como Mercado Livre) e valores médios de mão de obra na região do cliente, e apresenta tudo junto:

"Para trocar a junta homocinética do seu HB20 2018, a peça custa entre R$ 120 e R$ 200, e a mão de obra na zona sul de SP fica entre R$ 150 e R$ 250. Total estimado: R$ 270 a R$ 450."

A estimativa fica salva e acompanha o cliente nas etapas seguintes como referência, inclusive na comparação de orçamentos.

**Por que IA aqui:** a IA conecta diagnóstico + modelo + região + preço em tempo real dentro da mesma conversa, sem o cliente precisar navegar para outra tela, pesquisar preço de peça em outro site ou fazer conta. Tudo acontece no fluxo natural.

---

### 5. Busca e recomendação de mecânico

A IA recomenda diretamente, sem o cliente precisar filtrar. "Para esse serviço no seu HB20, encontrei 3 oficinas bem avaliadas perto de você. A Oficina Silva tem 4.8 de avaliação, é especializada em suspensão e direção, tem selo de atendimento respeitoso, e fica a 1.2 km. Quer ver as outras duas?"

O cliente pode pedir ajustes conversacionalmente: "Tem alguma que atende no sábado?" e a IA refina a busca.

Os filtros tradicionais (mapa, lista ordenável) continuam existindo como alternativa para quem prefere navegar manualmente, mas o caminho padrão é a IA recomendar com base no contexto completo: problema + localização + histórico + preferências do cliente.

O perfil de cada mecânico é exibido em interface tradicional (tela, não conversa): nota geral, avaliações detalhadas (clareza do orçamento, qualidade das peças, qualidade do serviço, prazos, garantia, atendimento, preço, organização), comentários de outros clientes, selo de atendimento respeitoso, CNPJ verificado, especialidades, fotos da oficina e formas de contato. A IA leva o cliente até o perfil, mas o perfil em si é conteúdo para ler no próprio ritmo.

**Por que IA aqui:** filtrar é trabalho cognitivo. O cliente com carro com problema não quer avaliar 15 oficinas. Ele quer que alguém diga "vai nessa aqui, é boa para o seu caso". A IA faz a curadoria que antes só um amigo entendido faria.

---

### 6. Comparação de orçamentos com análise

O cliente seleciona até 3 oficinas (que habilitaram pré-orçamento). Cada oficina recebe a descrição do problema já estruturada pela IA. O prazo de resposta é de até 24h.

Os orçamentos chegam e a IA analisa para o cliente: "A Oficina Silva orçou R$ 380, a Oficina Park R$ 520 e a Oficina Central R$ 1.200. A Oficina Central está 215% acima da média regional para esse serviço — recomendo pedir justificativa antes de aceitar. Entre as outras duas, a diferença é a peça: a Silva usa paralela e a Park usa original. Para o seu carro com 7 anos, paralela de boa marca resolve bem."

A IA não só mostra números — ela interpreta os números para o cliente, que não tem repertório técnico para fazer essa leitura sozinho.

Os orçamentos são estimativas. A plataforma deixa claro que o diagnóstico pode mudar após avaliação presencial do profissional.

**Por que IA aqui:** mostrar três orçamentos lado a lado sem explicação ainda deixa o cliente perdido ("o mais barato é pior? o mais caro é golpe? o que é peça paralela?"). A IA fecha o gap de conhecimento. Isso torna a confiança verificável, não só visível.

---

### 7. Compartilhamento inteligente

A IA gera um resumo estruturado para compartilhamento via WhatsApp — não um print de tela, mas uma mensagem clara:

"Diagnóstico: possível problema na junta homocinética. Estimativa Auto Justo: R$ 270–450. Orçamentos recebidos: Oficina Silva R$ 380 (peça paralela), Oficina Park R$ 520 (peça original). Link para ver detalhes no app."

O cliente manda para quem quiser com um toque. Essa funcionalidade respeita o comportamento real identificado na pesquisa: as pessoas delegam decisões sobre o carro a intermediários de confiança (pai, amigo, cônjuge). A Auto Justo facilita esse comportamento, mas agora com informação de qualidade.

**Por que IA aqui:** a IA transforma dados espalhados em uma mensagem coerente que qualquer pessoa consegue ler e opinar. O pai que recebe esse resumo no WhatsApp consegue ajudar de verdade, diferente de receber um print confuso de uma tela de app.

---

### 8. Escolha e agendamento

A IA pode sugerir horários disponíveis: "Quer agendar na Oficina Silva? Eles têm horário quinta às 14h e sexta às 9h." A seleção final é feita em interface tradicional — calendário visual ou toque no horário.

Se a oficina não habilitou agendamento pelo app, o cliente entra em contato por WhatsApp ou telefone exibidos no perfil. A plataforma registra a escolha para alimentar o histórico do carro.

**Por que interface tradicional no agendamento:** selecionar horário em calendário visual é mais eficiente que negociar por conversa. A IA conduz até esse ponto e entrega para a interface onde ela funciona melhor.

---

### 9. Pós-serviço: avaliação conversacional e registro automático

A Auto Justo puxa conversa de forma natural depois do prazo estimado do serviço: "Oi! Você levou o carro na Oficina Silva na terça. O barulho no volante parou?"

Se o cliente responde "sim, resolveu", a IA registra o serviço como concluído e pede a avaliação de forma leve: "De 1 a 5, como foi o atendimento? E o preço final ficou perto dos R$ 380 que orçaram?" Mais campo aberto opcional.

Se o cliente responde "não resolveu", a IA entra no fluxo de resolução: "O que continua acontecendo?" — e reinicia o diagnóstico com o contexto anterior, sem o cliente precisar repetir tudo.

O serviço realizado fica registrado automaticamente no histórico do carro, sem preenchimento manual. As avaliações feitas por mulheres alimentam o selo de atendimento respeitoso.

**Por que IA aqui:** formulário de avaliação pós-serviço tem taxa de resposta baixíssima. Conversa tem taxa muito maior. E a IA consegue perceber se o serviço não resolveu e agir, em vez de simplesmente registrar uma nota baixa.

---

### 10. Manutenção preventiva proativa

A Auto Justo avisa o cliente proativamente, como um lembrete inteligente: "Faz 8 meses que você trocou o óleo do HB20. Para o seu modelo, o manual recomenda a cada 10 mil km ou 12 meses. Considerando que você roda em cidade, vale fazer em breve. Estimativa: R$ 120–180. Quer que eu encontre uma oficina?"

A IA cruza tempo desde a última manutenção + quilometragem estimada + recomendações do manual + padrões de problema daquele modelo para decidir o que sugerir e quando.

Com o tempo, a IA aprende o padrão de uso do cliente (roda muito ou pouco, cidade ou estrada) e ajusta as sugestões. A sugestão vem acompanhada de estimativa de custo e atalho para mecânicos que o cliente já usou e avaliou bem, mecânicos próximos ou favoritos.

**Por que IA aqui:** manutenção preventiva só funciona se for proativa. Ninguém abre o app para checar "será que tá na hora de trocar a correia dentada". A IA que avisa no momento certo é o que diferencia a Auto Justo de uma tabela de revisão que ninguém consulta.

---

### 11. Emergência: carro parou

O cliente abre o app em pânico e digita ou fala "meu carro parou no meio da rua". A IA reconhece o contexto de emergência e muda o tom e a velocidade: poucas perguntas, respostas diretas. "Você está em segurança? O carro liga mas não anda, ou não liga de jeito nenhum?"

Dependendo da resposta, direciona para:

- **Mecânicos com filtro "atende emergência / 24h"** na região — já mostrando contato e avaliação
- **Base de contatos de guincho** — o suficiente para cobrir a região e evitar que o cliente tenha que buscar no Google em um momento de estresse. Contatos com avaliações de outros clientes quando disponíveis.

Sem menus, sem filtros, sem navegação. A conversa resolve.

O público-alvo deste projeto não possui seguro nem app de assistência. A base de guinchos existe para cobrir essa lacuna em situações de emergência.

**Por que IA aqui:** em emergência, qualquer fricção é inaceitável. O cliente não vai navegar abas e filtros com o carro parado na chuva. A IA reduz o caminho até a solução ao mínimo absoluto: duas perguntas e um contato.

---

## Onde a IA Não Entra

- **Perfil do mecânico e avaliações** — conteúdo estático que o cliente quer ler no próprio ritmo. Nota, comentários, selo, fotos, CNPJ verificado. Interface tradicional funciona melhor que conversa.
- **Calendário de agendamento** — seleção visual de horários é mais eficiente que negociação por texto.
- **Contato com guincho ou oficina por telefone/WhatsApp** — mostrar o botão de ligar ou WhatsApp é suficiente. O app não precisa intermediar essa ligação.
- **Histórico do carro** — tela de consulta para o cliente rever serviços anteriores, datas e valores. Informação para leitura, não para conversa.

---

## Selo de Atendimento Respeitoso a Mulheres

A pesquisa qualitativa revelou que 3 de 4 mulheres entrevistadas relatam sentir que são cobradas a mais por serem mulheres, e 2 abandonaram a posse de veículo por causa da experiência com oficinas.

O selo funciona assim: quanto mais mulheres avaliarem positivamente um mecânico na plataforma, mais evidência de que aquele estabelecimento trata clientes mulheres com respeito e justiça. O selo é visível no perfil do mecânico e nos resultados de busca (e mencionado pela IA nas recomendações), servindo como critério de escolha.

Esse recorte é um diferencial de posicionamento — nenhuma solução no mercado brasileiro trata explicitamente a vulnerabilidade de gênero no atendimento de oficinas.

---

## Resumo: O Que Muda de Tradicional para AI Native

| Aspecto | Tradicional | AI Native |
|---|---|---|
| Interface principal | Telas, menus, filtros | Conversa com IA |
| Cadastro | Formulário com campos | Foto do documento + validação por conversa |
| Diagnóstico | Lista de sintomas + resultado | Conversa adaptativa com perguntas de refinamento |
| Orientação imediata | Passo a passo estático | Conversa que se adapta às respostas do cliente |
| Busca de mecânico | Cliente filtra e escolhe | IA recomenda com base no contexto completo |
| Comparação de orçamentos | Números lado a lado | IA interpreta e explica as diferenças |
| Compartilhamento | Link ou print | Resumo estruturado gerado pela IA |
| Avaliação pós-serviço | Notificação com formulário | Conversa natural que detecta se o problema foi resolvido |
| Manutenção preventiva | Sugestão baseada em histórico | Lembrete proativo com aprendizado do padrão de uso |
| Emergência | Filtros e lista de contatos | Conversa direta com mínimo de fricção |
