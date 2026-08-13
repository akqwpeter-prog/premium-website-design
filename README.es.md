# Premium Website Design

![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)
![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)
![Codex Skill](https://img.shields.io/badge/Codex-Skill-1a5dff.svg)

[English](README.md) · [中文版](README.zh-CN.md) · [日本語](README.ja.md) · [한국어](README.ko.md) · [Français](README.fr.md)

Un skill de Codex para diseñar sitios personales, portafolios y páginas de aterrizaje de extremo a extremo: dirección, tokens, tipografía, interacciones táctiles, arte generativo, temas claro/oscuro, QA y despliegue.

**Demo real hecha con este skill:** https://mengjin-site.pages.dev

## Galería

Cuatro direcciones de estilo generadas por el skill (todo contenido ficticio):

| Style | Dark | Light |
| --- | --- | --- |
| Editorial Magazine · The Ledger | ![dark](assets/demo/layouts/editorial-dark.webp) | ![light](assets/demo/layouts/editorial-light.webp) |
| Brutalist · BRUT// | ![dark](assets/demo/layouts/brutal-dark.webp) | ![light](assets/demo/layouts/brutal-light.webp) |
| Soft Structural · AERO | ![dark](assets/demo/layouts/soft-dark.webp) | ![light](assets/demo/layouts/soft-light.webp) |
| Cobalt Ink · Lumen | ![dark](assets/demo/dark.png) | ![light](assets/demo/light.png) |
| Forest · Moss | ![dark](assets/demo/styles/forest-dark.webp) | ![light](assets/demo/styles/forest-light.webp) |
| Mono Cherry · Noir | ![dark](assets/demo/styles/noir-dark.webp) | ![light](assets/demo/styles/noir-light.webp) |
| Terracotta Slate · Atelier Terra | ![dark](assets/demo/styles/terra-dark.webp) | ![light](assets/demo/styles/terra-light.webp) |

Móvil: ![mobile](assets/demo/mobile.png)

## Qué hace

1. **Lectura de diseño** - infiere audiencia y brief, ajusta variación / movimiento / densidad
2. **Dirección** - una estética clara, sin plantillas genéricas
3. **Tokens y esqueleto** - sistema OKLCH dark-first con tema claro
4. **Interacciones** - entrada de personajes, spotlight, tilt 3D, botones magnéticos, scroll, marquee, cambio de tema
5. **Arte** - generación gratuita sin marca de agua (SiliconFlow Kolors) + revisión visual gratuita (GLM-4V-Flash), arte generativo sin API, o pipeline de avatar IA con privacidad
6. **Iconos** - búsqueda y descarga automática desde Iconify / Simple Icons / iconfont con verificación
7. **Verificación y despliegue** - checklist, QA con Playwright, Cloudflare Pages

## Instalación

Pide a Codex que instale el skill desde este repositorio, o cópialo a tu directorio de skills:

```bash
cp -r premium-website-design ~/.codex/skills/
```

## Contenido

```text
SKILL.md                      Flujo principal
references/preflight.md       Checklist de lanzamiento
references/interactions.md    Recetas de movimiento
references/art-pipeline.md    Arte generativo + avatar + privacidad
references/icons.md           Iconos + verificación
assets/tokens.css             Tokens de diseño
scripts/qa_site.py            QA con Playwright
```

## Licencia

MIT
