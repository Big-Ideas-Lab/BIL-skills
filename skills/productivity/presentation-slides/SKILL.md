---
name: presentation-slides
description: Build and reuse an HTML-first design system and fixed-stage slide template library for presentations.
disable-model-invocation: false
argument-hint: "What presentation HTML slide or format should we create?"
---

# Presentation slides

The recovered BIG IDEAs Lab system in `design-system/` is canonical. `slide-templates/` is a separate sibling containing the reusable HTML template, machine-readable manifest, and approved Reddit CGM deck as provenance.

Use the single canonical `design-system/index.html` catalog as the reference surface. `slide-templates/template-manifest.json` is the generation contract: exactly three fixed layouts, Title, Title with Media, and Regular. The source wearable project is not a runtime dependency; HTML only is the target.

## Workflow

1. Read `DESIGN.md`, the recovered `design-system/` package, and `slide-templates/template-manifest.json`.
2. Reuse the recovered semantic tokens and the manifest-defined layout contract.
3. Create fixed `1920px × 1080px` `.slide-stage` elements. Scale the stage uniformly to the viewport; never reflow slide content responsively.
4. Keep content generic and placeholder-first. Consuming labs provide approved data, citations, figures, and any newly approved project assets.
5. Use opacity/visibility/pointer-events for deck navigation, preserve reading order, provide labels and keyboard navigation, and honor reduced-motion preferences.
6. Run `python3 scripts/validate.py` and `python3 -m unittest discover -s tests -v` before delivery.

The final medium is HTML. Do not create PowerPoint/PPTX files or use PowerPoint-specific libraries unless a user separately requests an export; PowerPoint is intentionally not the target medium for this skill.

## Design contract

- Use a 16:9 widescreen canvas.
- Preserve the recovered light academic visual language: white-space dominance, deep navy hierarchy, blue emphasis, restrained borders, and generous whitespace. Do not introduce teal, orange, gradients, glass, or generic dashboards.
- Treat the system as a communication aid, not a dashboard.
- Keep one dominant idea per slide and use direct titles.
- Prefer inspectable HTML/CSS primitives over pasted screenshots.
- The approved BIG IDEAs Lab logo is bundled at `design-system/assets/logos/big-ideas-lab-logo.png` with its asset register. New project assets require approval and appropriate provenance/licensing.
- Do not use color alone to communicate status. Pair color with labels, position, or text.
- Keep normal body copy at 14 pt or larger and preserve reading order.
- Keep Title with Media at the shared title band of left 120px/top 54px and a centred 1180×660 media frame at x=370px/top=270px with `object-fit: contain` and no visible outline.
- Use Inter semibold (60px/1.02, -0.03em tracking) for every content slide heading and let it span the content width; reserve Source Serif 4 for the Title opening treatment.
- Place the lab lockup once, on the opening slide, with its top edge level with the title cap line; content slides omit it.
- Center a content slide's body within the usable region between the heading and the bottom pager, not within the full 1080px canvas.

## Source of truth

- `design-system/index.html`: the canonical catalog; the other two HTML files are redirect fallbacks.
- `design-system/tokens.css`, `tokens.json`, and `DESIGN.md`: canonical recovered sources.
- `slide-templates/bil-lab-presentation-template.html`: reusable fixed-stage template.
- `slide-templates/template-manifest.json`: machine-readable slide contract.
- `slide-templates/reference-decks/`: approved provenance deck, not a generic template.
- `DESIGN.md`: layout rules and component guidance.

## Catalog contract

The catalog has one page with 13 manifest-backed components, a button system, and three layouts. It uses the shared `design-system/bil-components.css` layer; implementation details remain collapsed and subtle.

## Verify

From this skill directory:

```bash
python3 scripts/validate.py
python3 -m unittest discover -s tests -v
```

## Extending the library

1. Add or revise semantic tokens first.
2. Add reusable component classes when a pattern appears in more than one slide.
3. Add or revise manifest slots only when a reusable layout contract changes.
4. Validate structure and inspect both HTML pages at 16:9 before sharing.

## Asset and licensing boundary

This is a BIG IDEAs Lab–internal skill pack. It bundles catalogued design-system variants of BIL and Duke/BIL marks for authorized lab workflows; use only the exact files recorded in `design-system/assets/ASSET_REGISTER.md`, without redrawing or alteration. Repository inclusion is not trademark approval and does not place institutional marks under the MIT license. Follow current Duke brand and trademark requirements for every use. New figures, citations, photographs, scientific data, and project-specific assets still require appropriate provenance and permission.
