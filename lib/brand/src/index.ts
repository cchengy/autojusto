/**
 * Auto Justo — paleta da marca em TypeScript.
 *
 * Espelha `tokens.css`. Use este módulo onde CSS não alcança: cores de gráfico,
 * estilo inline, geração de imagem. Para estilizar UI, prefira as variáveis CSS.
 *
 *   import { brand, semantic } from "@workspace/brand";
 *   import "@workspace/brand/tokens.css";
 */

/** Cores da marca, lidas do logo. Não invente acento fora desta lista. */
export const brand = {
  /** Azul-marinho — bolha do cliente, texto forte. */
  navy: "#052577",
  /** Navy pressionado. */
  navyDeep: "#03153F",
  /** Azul primário — botões, links, envio. */
  blue: "#0136AB",
  /** Azul vivo — hover, foco, estado ativo. */
  blueVivid: "#084DB1",
  /** Amarelo — acento pontual. Nunca fundo grande. */
  yellow: "#F8C613",
  /** Texto legível sobre amarelo claro. */
  yellowInk: "#6B4E00",
} as const;

/** Cores semânticas. Não são da marca e não servem como acento decorativo. */
export const semantic = {
  /** Só sucesso, check, confirmação. */
  success: "#10B981",
  /** Laranja, e não âmbar: âmbar competiria com o amarelo da marca. */
  warn: "#E07A00",
  danger: "#EF4444",
  /** Dedicada ao Selo Respeitoso. Sem outro uso. */
  respeito: "#EC4899",
} as const;

/** Neutros da interface. */
export const neutral = {
  bg: "#F4F7FC",
  surface: "#FFFFFF",
  tint: "#E9F0FC",
  border: "#E2E8F0",
  ink: "#2D3748",
  ink2: "#94A3B8",
} as const;

/**
 * Componentes HSL (`"H S% L%"`), no formato que tokens shadcn/Tailwind esperam
 * dentro de `hsl(...)`.
 */
export const brandHsl = {
  navy: "223 92% 24%",
  blue: "221 99% 34%",
  blueVivid: "215 91% 36%",
  yellow: "47 94% 52%",
  success: "160 84% 39%",
} as const;

/**
 * Ordem sugerida para séries de gráfico. Começa nos azuis da marca, usa o
 * amarelo como segunda série por ser o maior contraste disponível.
 */
export const chartSeries = [
  brand.blue,
  brand.yellow,
  brand.navy,
  brand.blueVivid,
  semantic.success,
] as const;

/**
 * Proporção da marca: o azul domina e o amarelo aparece em poucos pontos —
 * a mesma leitura do logo, onde o quadrado é azul e o sujeito é amarelo.
 */
export const brandRules = {
  wordmark:
    'O wordmark "Auto Justo" é Canva Sans Bold Italic, proprietária da Canva e sem licença de webfont. Use sempre assets/wordmark.svg; nunca recrie com fonte substituta.',
  yellowUsage:
    "Amarelo é acento pontual: chip de contexto, badge de destaque, faixa lateral de card. Nunca fundo de seção nem cor de botão primário.",
  greenUsage:
    "Verde é semântico, não é cor de marca. Só sucesso, check e confirmação.",
} as const;
