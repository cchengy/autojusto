import express, { type Express } from "express";
import cors from "cors";
import pinoHttp from "pino-http";
import router from "./routes";
import { logger } from "./lib/logger";
import { resolvePrototipoDir, resolveSiteDir } from "./lib/prototipo";

const app: Express = express();

app.use(
  pinoHttp({
    logger,
    serializers: {
      req(req) {
        return {
          id: req.id,
          method: req.method,
          url: req.url?.split("?")[0],
        };
      },
      res(res) {
        return {
          statusCode: res.statusCode,
        };
      },
    },
  }),
);
app.use(cors());
app.use(express.json());
app.use(express.urlencoded({ extended: true }));

app.use("/api", router);

// --- Site estático ---------------------------------------------------------
// A API responde em /api. O resto do domínio serve arquivos prontos:
//
//   /       landing (site/index.html)
//   /app    a jornada do cliente, começando em T00-onboarding.html
//   /telas  índice das 9 telas, ferramenta interna
//
// Se alguma das pastas não for encontrada, a API continua de pé sozinha: o
// health check em /api/healthz não depende de nada disso.

const prototipoDir = resolvePrototipoDir();
const siteDir = resolveSiteDir();

if (prototipoDir) {
  // "/app/" serve o shell: uma página só que carrega as telas em camadas e as
  // troca por fusão, em vez de recarregar a página a cada passo.
  //
  // O shell entra como índice do diretório, e não como rota própria, porque
  // precisa ser servido COM a barra final. Em "/app" sem barra, o src relativo
  // do iframe resolveria para "/T00-onboarding.html", fora deste mount.
  app.use(
    "/app",
    express.static(prototipoDir, { index: "shell.html", redirect: true }),
  );

  // O índice é um visualizador de desenvolvimento, separado do app. Precisa
  // redirecionar em vez de servir o arquivo daqui: em "/telas" os links
  // relativos das telas resolveriam para "/T01-chat.html", fora do mount.
  app.get("/telas", (_req, res) => {
    res.redirect(302, "/app/index.html");
  });

  logger.info({ prototipoDir }, "Protótipo servido em /app");
} else {
  logger.warn("Pasta prototipo/ não encontrada; /app e /telas indisponíveis");
}

if (siteDir) {
  app.use("/", express.static(siteDir));
  logger.info({ siteDir }, "Landing servida em /");
} else {
  logger.warn("Pasta site/ não encontrada; a landing fica indisponível");
}

export default app;
