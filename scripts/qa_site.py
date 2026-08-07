#!/usr/bin/env python3
"""Generic Playwright QA for a static website.

Usage:
  python qa_site.py --url http://localhost:8080

Checks: overflow at 1440/390/320, console errors, failed requests,
fonts, both themes, theme toggle, mobile menu, reduced motion.
"""

import argparse
import sys

from playwright.sync_api import sync_playwright


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--url", required=True)
    args = ap.parse_args()

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        results = []

        def record(name, ok, detail=""):
            results.append(ok)
            print(("PASS" if ok else "FAIL"), name, detail)

        page = browser.new_page(viewport={"width": 1440, "height": 900})
        errors, failed = [], []
        page.on("console", lambda m: errors.append(m.text) if m.type == "error" else None)
        page.on("pageerror", lambda e: errors.append(str(e)))
        page.on("requestfailed", lambda r: failed.append(r.url))
        page.goto(args.url, wait_until="networkidle")
        page.wait_for_timeout(700)

        record(
            "desktop overflow",
            page.evaluate("document.documentElement.scrollWidth <= document.documentElement.clientWidth"),
        )
        record(
            "fonts loaded",
            page.evaluate("document.fonts.check('16px \"Plus Jakarta Sans\"')"),
        )
        toggle = page.locator("#themeToggle")
        if toggle.count():
            toggle.click()
            page.wait_for_timeout(300)
            record(
                "theme toggle",
                page.evaluate("document.documentElement.dataset.theme === 'light'"),
            )
        record("no console errors", not errors, str(errors[:2]))
        record("no failed requests", not failed, str(failed[:2]))
        page.close()

        for w, h, label in [(390, 844, "mobile 390"), (320, 700, "mobile 320")]:
            page = browser.new_page(viewport={"width": w, "height": h})
            page.goto(args.url, wait_until="networkidle")
            page.wait_for_timeout(500)
            record(
                f"{label} overflow",
                page.evaluate("document.documentElement.scrollWidth <= document.documentElement.clientWidth"),
                f"w={page.evaluate('document.documentElement.scrollWidth')}",
            )
            if page.locator("#navToggle").count():
                page.locator("#navToggle").click()
                page.wait_for_timeout(400)
                record(
                    f"{label} menu opens",
                    page.evaluate("!document.querySelector('#navMenu').hidden"),
                )
            page.close()

        page = browser.new_page(viewport={"width": 1280, "height": 800})
        page.emulate_media(reduced_motion="reduce")
        page.goto(args.url, wait_until="networkidle")
        page.wait_for_timeout(300)
        record(
            "reduced motion content visible",
            page.locator(".reveal").first.evaluate(
                "el => getComputedStyle(el).opacity === '1'"
            ),
        )
        page.close()
        browser.close()

        print(f"\nSUMMARY: {sum(results)}/{len(results)} passed")
        sys.exit(0 if all(results) else 1)


if __name__ == "__main__":
    main()
