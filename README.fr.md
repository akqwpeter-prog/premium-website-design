# Premium Website Design

![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)
![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)
![Codex Skill](https://img.shields.io/badge/Codex-Skill-1a5dff.svg)

[English](README.md) · [中文版](README.zh-CN.md) · [日本語](README.ja.md) · [한국어](README.ko.md) · [Español](README.es.md)

Un skill Codex pour concevoir de bout en bout des sites personnels, portfolios et landing pages : direction artistique, tokens, typographie, interactions tactiles, art génératif, thèmes clair/sombre, QA et déploiement.

**Démo réalisée avec ce skill :** https://mengjin-site.pages.dev

## Galerie

Quatre directions de style rendues par le skill (tout est fictif) :

| Style | Dark | Light |
| --- | --- | --- |
| Editorial Magazine · The Ledger | ![dark](assets/demo/layouts/editorial-dark.webp) | ![light](assets/demo/layouts/editorial-light.webp) |
| Brutalist · BRUT// | ![dark](assets/demo/layouts/brutal-dark.webp) | ![light](assets/demo/layouts/brutal-light.webp) |
| Soft Structural · AERO | ![dark](assets/demo/layouts/soft-dark.webp) | ![light](assets/demo/layouts/soft-light.webp) |
| Cobalt Ink · Lumen | ![dark](assets/demo/dark.png) | ![light](assets/demo/light.png) |
| Forest · Moss | ![dark](assets/demo/styles/forest-dark.webp) | ![light](assets/demo/styles/forest-light.webp) |
| Mono Cherry · Noir | ![dark](assets/demo/styles/noir-dark.webp) | ![light](assets/demo/styles/noir-light.webp) |
| Terracotta Slate · Atelier Terra | ![dark](assets/demo/styles/terra-dark.webp) | ![light](assets/demo/styles/terra-light.webp) |

Mobile : ![mobile](assets/demo/mobile.png)

## Ce qu'il fait

1. **Lecture de design** - infère l'audience et le brief, règle variation / mouvement / densité
2. **Direction** - une esthétique assumée, sans templates génériques
3. **Tokens et structure** - système OKLCH dark-first avec thème clair
4. **Interactions** - entrée de caractères, spotlight, tilt 3D, boutons magnétiques, scroll, marquee, bascule de thème
5. **Art** - art génératif seedé (sans clé API) ou avatar IA avec règles de confidentialité
6. **Icônes** - recherche et téléchargement automatiques depuis Iconify / Simple Icons / iconfont avec vérification
7. **Vérification et déploiement** - checklist, QA Playwright, Cloudflare Pages

## Installation

Demandez à Codex d'installer le skill depuis ce dépôt, ou copiez-le dans votre dossier de skills :

```bash
cp -r premium-website-design ~/.codex/skills/
```

## Contenu

```text
SKILL.md                      Flux principal
references/preflight.md       Checklist de release
references/interactions.md    Recettes de mouvement
references/art-pipeline.md    Art génératif + avatar + confidentialité
references/icons.md           Icônes + vérification
assets/tokens.css             Tokens de design
scripts/qa_site.py            QA Playwright
```

## Licence

MIT
