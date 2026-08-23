import { existsSync } from "node:fs";
import path from "node:path";

/** Arquivo que prova que achamos a pasta certa, e não uma homônima. */
const SENTINELA = "T01-chat.html";

/**
 * Resolve a pasta `prototipo/` na raiz do repositório.
 *
 * O cwd muda conforme o ambiente: em produção o Replit roda
 * `node artifacts/api-server/dist/index.mjs` a partir da raiz do repo, e em
 * desenvolvimento o `pnpm --filter` roda de dentro do pacote. Em vez de fixar
 * um caminho relativo que só funciona num dos dois, subimos a árvore a partir
 * do cwd até achar a pasta.
 *
 * Retorna `null` se não encontrar — nesse caso a API segue servindo normalmente
 * e só o site estático fica indisponível.
 */
export function resolvePrototipoDir(
  from: string = process.cwd(),
): string | null {
  let dir = path.resolve(from);

  for (;;) {
    const candidato = path.join(dir, "prototipo");

    if (existsSync(path.join(candidato, SENTINELA))) {
      return candidato;
    }

    const pai = path.dirname(dir);

    if (pai === dir) {
      return null;
    }

    dir = pai;
  }
}

/** Idem, para a pasta `site/` com a landing. */
export function resolveSiteDir(from: string = process.cwd()): string | null {
  let dir = path.resolve(from);

  for (;;) {
    const candidato = path.join(dir, "site");

    if (existsSync(path.join(candidato, "index.html"))) {
      return candidato;
    }

    const pai = path.dirname(dir);

    if (pai === dir) {
      return null;
    }

    dir = pai;
  }
}
