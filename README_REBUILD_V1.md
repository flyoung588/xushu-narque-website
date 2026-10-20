# 序束 / NARQUE Website v1.0 — Staging Build

**Status: review build only. The live GitHub Pages site remains unchanged.**

## Scope

- 7 Chinese + 7 English official pages
- Home hero and three-system layout: METRE / XREM / AIOS
- Research and international collaboration content from the approved editorial canon
- Responsive navigation, CSS/SVG scientific visuals, reduced-motion support
- Legacy page redirects for existing deep links
- Source of truth: `content-canon.json`
- The October 20 approved one-page company introduction is bundled verbatim (PDF and Markdown source).

## Local preview

```bash
python3 -m http.server 8000
# Open http://127.0.0.1:8000/
```

No build step or external runtime dependency is required for viewing the generated HTML. The bundled `build.py` may be used to regenerate the pages from `content-canon.json` using Python 3.10+.

## Quality gates

```bash
python3 qa_static.py
python3 qa_visual.py  # Requires Playwright and local Chromium
```

The current check-in requires: all 14 language pages, all 58 content blocks, no broken local links, no missing anchors, no client JavaScript errors, and zero horizontal overflow in desktop 1440px, mobile 390px, and narrow mobile 320px. `qa_visual.py` injects the local CSS/JS when running Chromium because the current hosted QA environment restricts `file://` and loopback HTTP navigation; this does not affect the website files themselves.

## Deployment discipline

1. Review all seven pages, especially METRE / XREM / AIOS and international collaboration.
2. Confirm the official contact mailbox and publication URLs before release.
3. Keep any staging branch separate from `main`; no auto-merge.
4. After human approval, merge the reviewed changes and verify the live GitHub Pages output with end-to-end link and language tests.

## Content and rights

The top-level company description follows the explicitly user-approved one-page introduction. Internal research status metadata is not rendered into public marketing sections. The public website does not claim journal peer review or grant awards. Specific book sales or DOI URLs are not fabricated.
