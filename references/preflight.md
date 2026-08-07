# Preflight Checklist

Fail-closed gate. Every box must be true before shipping.

## Surface
- [ ] Zero em-dash and en-dash in visible text (use hyphen or restructure).
- [ ] One primary accent; optional signal color only for semantic status.
- [ ] One corner-radius system across the page.
- [ ] No pure black / pure white; use off-black and off-white.
- [ ] Both light and dark themes defined and tested.
- [ ] No section flips to inverted mode mid-page.

## Type
- [ ] No Inter as default; no banned serifs (Fraunces, Instrument Serif) unless brand-justified.
- [ ] Chinese text has positive tracking; italic descenders get 1.1+ line-height.
- [ ] Headline hierarchy via weight and scale, not raw size alone.
- [ ] Hero headline fits 2 lines; hero subtext short; CTA visible without scroll.

## Layout
- [ ] No three equal feature cards.
- [ ] No centered-hero-over-mesh default (allowed only for manifesto briefs).
- [ ] No two sections share the same layout family consecutively (work rows vs timeline rail must differ).
- [ ] Bento cells have 2-3 with real visual variation; N items -> N cells.
- [ ] Mobile collapse: single column, no horizontal overflow at 320px.
- [ ] `min-h-[100dvh]` where full viewport is needed; never `h-screen`.

## Content
- [ ] No generic names, fake-perfect numbers, startup-slop brand names, or filler verbs.
- [ ] No decorative scroll cues, version labels, section numbering eyebrows, or locale strips.
- [ ] No pills/labels overlaid on images.
- [ ] No duplicate CTA intent.
- [ ] Privacy scan: no phone numbers, month-precision dates, or private files in the public dir.

## Motion
- [ ] Every animation justified; at least one entrance, one scroll-linked, one feedback effect.
- [ ] Only `transform` and `opacity` animated.
- [ ] No `window.addEventListener("scroll")`.
- [ ] Pointer effects gated on `(pointer: fine)`.
- [ ] Reduced-motion mode collapses everything to static.

## Accessibility
- [ ] CTA text contrast >= 4.5:1 (3:1 large); body >= 4.5:1.
- [ ] Focus-visible outlines everywhere.
- [ ] Keyboard nav works; mobile menu closes on Escape and link click.
- [ ] Alt text present on meaningful images; decorative images empty alt.

## Performance
- [ ] Fonts self-hosted and preloaded; decorative images lazy + low priority.
- [ ] Images sized to render size x2, WebP, quality balanced.
- [ ] No failed requests in console.
- [ ] Cache headers for immutable assets.
