# Icon Sourcing & Verification

Workflow for getting UI and brand icons automatically, with a fail-closed check before shipping.

## Sources

### 1. Iconify API (recommended, no login)

Aggregates hundreds of open icon sets. Search first, then fetch the exact SVG:

```bash
# search
curl "https://api.iconify.design/search?query=email&limit=10"
# fetch (PREFIX from search result, e.g. mdi:email-outline)
curl -o email.svg "https://api.iconify.design/mdi/email-outline.svg"
```

Useful prefixes:

| Prefix | Set | Notes |
| --- | --- | --- |
| `mdi` | Material Design Icons | Apache 2.0 |
| `ph` | Phosphor | MIT |
| `tabler` | Tabler Icons | MIT |
| `bi` | Bootstrap Icons | MIT |
| `simple-icons` | Simple Icons | Official brand glyphs, MIT |
| `line-md` / `iconamoon` | animated / thin sets | check license per set |

Iconify responses are already clean: `viewBox`, `width="1em"`, `height="1em"`, `fill="currentColor"`.

### 2. Simple Icons (brands, official glyphs)

Use only for brand marks (GitHub, Xiaohongshu, WeChat, X, LinkedIn):

```bash
curl -o github.svg "https://cdn.jsdelivr.net/npm/simple-icons@latest/icons/github.svg"
curl -o xiaohongshu.svg "https://cdn.jsdelivr.net/npm/simple-icons@latest/icons/xiaohongshu.svg"
```

Do NOT pick a "same name" icon from a crowdsourced set when an official brand glyph exists.

### 3. Bootstrap Icons (fallback via jsdelivr)

```bash
curl -o sun.svg "https://cdn.jsdelivr.net/npm/bootstrap-icons@1.11.3/icons/sun.svg"
```

### 4. iconfont.cn (domestic alternative)

Works for Chinese-platform icons that overseas sets miss. The search page renders client-side:

1. Open `https://www.iconfont.cn/search/index?q=<keyword>` in a headless browser (Playwright).
2. Wait for the icon grid, then extract `svg.icon` elements with nearby item titles.
3. Prefer an item whose title exactly matches the keyword; for brands, prefer the official-looking glyph over a random same-name icon.
4. Clean the SVG: keep `viewBox` + `xmlns`, strip `class`/`style`/`p-id`/`fill`.

## Integration (cross-browser safe)

- **Inline the SVG into HTML** with `class="ic"`, `aria-hidden="true"`, `focusable="false"`. Do not rely on CSS `mask-image` with external SVG files: Safari support is inconsistent and the old CSS can be stuck in a long cache.
- Theme the icon with:

```css
.ic {
  display: inline-block;
  width: 1.05em;
  height: 1.05em;
  flex-shrink: 0;
  vertical-align: -0.15em;
  fill: currentColor;
}
```

- For toggle icons (sun/moon), add per-theme classes and show/hide via `[data-theme]` rules.
- Cache hygiene: never set `immutable` on CSS/JS; version their URLs (`style.css?v=3`) when content changes. Images/fonts can keep long cache.

## Verification checklist (fail-closed)

- [ ] HTTP 200 and `Content-Type: image/svg+xml` for every fetched SVG.
- [ ] SVG parses as XML and has a `viewBox`.
- [ ] No text, watermark, or embedded title confusion in decorative icons.
- [ ] Brand icons come from `simple-icons` (or the platform's official mark), not a random same-name glyph.
- [ ] In a real browser: icon has nonzero size, `fill` resolves to the theme color, and there are no failed requests.
- [ ] Theme toggle shows the correct icon in both dark and light.
- [ ] License recorded in the source comment or README (MIT/Apache for Iconify sets; MIT for Simple Icons and Bootstrap).
