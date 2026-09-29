# BIG IDEAs Lab Visual Design System

A self-contained visual design-system catalog for BIG IDEAs Lab.

## Current scope

- Color palette: modern institutional blue, white, and cool neutrals
- Typography: Hume AI-inspired display/sans relationship
- Interface primitives: restrained controls, labels, fields, rules, and focus
- Media storage taxonomy
- One canonical catalog: `index.html`, ordered Color, Typography, Assets, Motion, Components, Slides
- Slides: three reusable 16:9 layouts — Title, Title with Media, and Regular
- Motion: fade/rise, line reveal, and staged-data presentation transitions

## Files

- `DESIGN.md` — normative design decisions and usage rules
- `tokens.css` — CSS custom properties
- `tokens.json` — machine-readable foundation tokens
- `index.html` — canonical catalog with the 12 implementation-backed components, button system remains available, and three-layout picker
- `components.html` and `slides.html` — accessible redirect/link fallbacks only
- `components-manifest.json` — slot, size, accessibility, and fragment contracts
- `assets/` — approved media storage by asset class

`tokens.css` and `tokens.json` remain canonical. The catalog demonstrates the system without adding new palette or type values, fabricating lab claims, or supplying unapproved media.
