# Interaction Recipes

All effects honor `prefers-reduced-motion: reduce` (collapse to static) and pointer-fine gating.

## 1. Hero character entrance

JS splits the title into spans; CSS rises each char with stagger:

```css
.hero__name { overflow: clip; }
.hero__name .char {
  display: inline-block;
  transform: translateY(115%) rotate(6deg);
  animation: char-rise 720ms cubic-bezier(0.16,1,0.3,1) forwards;
  animation-delay: calc(140ms + var(--i,0) * 55ms);
}
@keyframes char-rise { to { transform: none; } }
```

```js
const h = document.querySelector(".hero__name");
const text = h.textContent.trim();
h.setAttribute("aria-label", text);
h.textContent = "";
[...text].forEach((ch, i) => {
  const s = document.createElement("span");
  s.className = "char";
  s.style.setProperty("--i", i);
  s.textContent = ch === " " ? "\u00A0" : ch;
  h.appendChild(s);
});
```

## 2. Card cursor spotlight

```css
.cell { isolation: isolate; position: relative; }
.cell::before {
  content: ""; position: absolute; inset: 0; z-index: -1; border-radius: inherit;
  background: radial-gradient(260px circle at var(--mx,50%) var(--my,50%), var(--tint-accent-strong), transparent 72%);
  opacity: 0; transition: opacity 420ms;
}
.cell:hover::before { opacity: 1; }
```

```js
cell.addEventListener("pointermove", e => {
  if (raf) return;
  raf = requestAnimationFrame(() => {
    const r = cell.getBoundingClientRect();
    cell.style.setProperty("--mx", `${e.clientX - r.left}px`);
    cell.style.setProperty("--my", `${e.clientY - r.top}px`);
    raf = null;
  });
});
cell.addEventListener("pointerleave", () => {
  cell.style.removeProperty("--mx");
  cell.style.removeProperty("--my");
});
```

## 3. Portrait 3D tilt

Apply on `(pointer: fine)` only; reset inline transform on leave:

```js
const rx = ((e.clientY - r.top) / r.height - 0.5) * -8;
const ry = ((e.clientX - r.left) / r.width - 0.5) * 8;
el.style.transform = `perspective(900px) rotateX(${rx}deg) rotateY(${ry}deg) translateY(-4px)`;
```

## 4. Magnetic button

Keep offsets small (<= 6px) so the button never escapes the cursor. Clear inline transform on leave; `:active` edge shadow still provides press feedback.

## 5. Scroll-linked timeline rail

```css
.timeline { position: relative; }
.timeline::after {
  content: ""; position: absolute; top: 0; bottom: 0; width: 1px;
  background: linear-gradient(180deg, var(--color-accent), var(--color-accent-deep));
  transform-origin: top; transform: scaleY(0);
  animation: rail-grow linear;
  animation-timeline: view();
  animation-range: entry 12% cover 42%;
}
@keyframes rail-grow { to { transform: scaleY(1); } }
@supports not (animation-timeline: view()) { .timeline::after { transform: scaleY(1); } }
```

## 6. Skills marquee

Duplicate the group, translate track by -50%:

```css
.marquee { overflow: hidden; }
.marquee__track { display: flex; width: max-content; animation: marquee-slide 36s linear infinite; }
@keyframes marquee-slide { to { transform: translateX(-50%); } }
```

One marquee per page max.

## 7. Aurora backdrop

Fixed `pointer-events: none`, z-index -1, three blurred blobs (transform-only keyframes). Reduce opacity in dark mode via tokens. Disable under reduced motion.

## 8. Theme toggle (dark / light)

```css
:root[data-theme="light"] { /* override tokens */ }
```

```js
function applyTheme(t) {
  document.documentElement.dataset.theme = t;
  localStorage.setItem("mengjin-theme", t);
}
```

Set `data-theme` in a tiny head script before CSS loads to avoid flash. Default dark.

## Reduced motion

```css
@media (prefers-reduced-motion: reduce) {
  *, *::before, *::after { animation-duration: 0.01ms !important; transition-duration: 0.01ms !important; }
  .reveal, .hero__name .char { opacity: 1; transform: none; }
  .marquee, .aurora { display: none; }
}
```
