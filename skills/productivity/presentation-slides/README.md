# BIG IDEAs Lab Presentation HTML Slide System

An HTML-first design-system workspace and fixed-stage slide template library for research and presentations. It generates HTML slides, not PowerPoint files.

## Quick start

```bash
npx skills@latest add Big-Ideas-Lab/BIL-skills
```

Choose `presentation-slides`. From this directory, run `python3 -m http.server 8000`, then open `http://localhost:8000/design-system/index.html` or `http://localhost:8000/slide-templates/bil-lab-presentation-template.html`. Start from the manifest; the source wearable project is not a runtime dependency.

The catalog has one canonical page, `design-system/index.html`, ordered Color, Typography, Assets, Motion, Components, and Slides.

## File map

- `design-system/`: complete recovered canonical package, including tokens, assets, catalog PNGs, and validator
- `design-system/index.html`: canonical catalog with 13 components, button system, and three layouts
- `design-system/components.html` and `design-system/slides.html`: accessible link fallbacks
- `design-system/components-manifest.json`: component contracts
- `slide-templates/starters/`: clean Title, Title with Media, and Regular starter HTML
- `slide-templates/bil-lab-presentation-template.html`: reusable fixed 1920×1080 template
- `slide-templates/template-manifest.json`: generation contract
- `DESIGN.md`: visual and accessibility system
- `scripts/validate.py`: dependency-free validator
- `tests/test_structure.py`: structural tests

## Manifest layouts

Exactly three layouts: Title, Title with Media, and Regular. Apply layout exposes the complete contract for copying and a starter HTML download. Title with Media uses a title at left 120px/top 54px and a centred 1180×660 media frame at x=370px/top=270px with `object-fit: contain`. Slide headings use Inter semibold at 60px/1.02 with -0.03em tracking; Source Serif 4 is reserved for the Title opening treatment. Place the lab lockup once, on the opening slide, with its top edge level with the title cap line. Center a slide's body between the heading and the bottom pager rather than within the full canvas.

## Customize

Use the manifest and template contract. Keep content generic in the library; new project text, figures, citations, and assets require approval.

## Build

Slides use fixed 1920×1080 HTML stages that scale uniformly to the viewport. The design system is dependency-free.

## Licensing and asset notes

Code and documentation are released under the MIT License. The approved BIG IDEAs Lab logo is bundled with its asset register. Commercial display/sans fonts are referenced with fallbacks and are not bundled; new project assets require approval and licensing.
