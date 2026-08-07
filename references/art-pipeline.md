# Artwork Pipeline

## Algorithmic art (no API key)

Generate original abstract art with a p5.js flow-field sketch, export through a headless browser, and optimize:

1. Write a seeded p5.js sketch: thousands of particles follow layered Perlin noise; hue follows speed/noise; rare accent color marks turbulence.
2. Export canvas PNG via Playwright `toDataURL`, keep transparency.
3. Convert to WebP with alpha; crop to rendered aspect; size to 2x display width.
4. CSS: `mix-blend-mode: screen` on dark theme, `multiply` on light theme.
5. Keep seeds documented so every image is reproducible.

Same-seed guarantee: use `randomSeed(seed)` and `noiseSeed(seed)`.

## AI avatar (API key available)

Seedream (Volcano Ark) image-to-image flow:

1. Read the reference photo, base64 encode to a data URI.
2. POST `https://ark.cn-beijing.volces.com/api/v3/images/generations` with `model`, `prompt`, `image`, `size >= 1920x1920` for 5.0-lite, `response_format: b64_json`, `watermark: false`.
3. Prompt: keep likeness ("以参考照片为原型"), state style (e.g., 日本动漫电影级作画), palette (cobalt/navy), and "无文字、无水印、不要改变性别和年龄".
4. Fallback model chain: `doubao-seedream-5-0-pro-260628` -> `doubao-seedream-5-0-lite-260128` (alias `doubao-seedream-5-0-lite-260128`) -> 4.5 -> 4.0.
5. Common errors:
   - `SetLimitExceeded`: account hit Safe Experience Mode limit; ask user to adjust/close it or use another model.
   - `ModelNotOpen`: model not activated in Ark console; user must click 开通服务.
   - `InvalidParameter ... at least 3686400 pixels`: raise size to 2048x2048.
6. Post-process: crop to target aspect, resize, WebP, move the 2048px original out of the public repo.

## Privacy rules

- Never keep a real face photo in a public repo, even after replacement: git history retains deleted files.
- Move originals to a local private folder; recommend making the GitHub repo private if history already contains them.
- Recommend rotating any API key that has been shared in chat.
- Public site: year-only dates, no phone numbers, avatar instead of real photo.
