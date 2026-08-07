# Premium Website Design

[English](README.md) · [中文版](README.zh-CN.md) · [日本語](README.ja.md) · [한국어](README.ko.md) · [Français](README.fr.md)

Un skill de Codex para diseñar sitios personales, portafolios y páginas de aterrizaje de extremo a extremo: dirección, tokens, tipografía, interacciones táctiles, arte generativo, temas claro/oscuro, QA y despliegue.

**Demo real hecha con este skill:** https://mengjin-site.pages.dev

## Qué hace

1. **Lectura de diseño** - infiere audiencia y brief, ajusta variación / movimiento / densidad
2. **Dirección** - una estética clara, sin plantillas genéricas
3. **Tokens y esqueleto** - sistema OKLCH dark-first con tema claro
4. **Interacciones** - entrada de personajes, spotlight, tilt 3D, botones magnéticos, scroll, marquee, cambio de tema
5. **Arte** - arte generativo con semilla (sin API key) o avatar IA con privacidad
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
