---
name: BIG IDEAs Lab Visual Design System
version: 0.2.0
status: foundations-and-slides
reference: Hume AI typography
---

# BIG IDEAs Lab Visual Design System

This repository is a **design-system source and specimen catalog**, not a marketing website or content library. The current scope covers one canonical catalog page (`index.html`) with color, typography, assets, motion, 13 component families, three slide layouts, and restrained presentation motion. `tokens.css` and `tokens.json` remain the canonical token sources.

## Visual direction

- Modern, professional, institutional, and research-forward.
- White is the default canvas.
- Blue is the brand and interaction color.
- Typography takes its feel from Hume AI: editorial display headlines paired with a precise grotesk sans serif for utility and body text.
- No warm palette is implied or permitted by default.
- Duke is the institutional affiliation layer; the public lab identity is **BIG IDEAs Lab**.

## Color

### Core palette

| Token | Hex | Role |
|---|---:|---|
| `blue-900` | `#012169` | Primary brand blue; large fields and high-emphasis marks |
| `blue-800` | `#003A70` | Duke heritage blue; links and strong accents |
| `blue-700` | `#00539B` | Interactive blue |
| `blue-100` | `#E8F1FA` | Pale blue surface |
| `blue-050` | `#F4F8FC` | Subtle blue wash |
| `white` | `#FFFFFF` | Default background |
| `ink-950` | `#111318` | Primary text |
| `ink-700` | `#3F4650` | Secondary text |
| `ink-500` | `#68717D` | Metadata and captions |
| `gray-200` | `#D9DEE5` | Borders and dividers |
| `gray-100` | `#EDF0F4` | Disabled and quiet surfaces |
| `gray-050` | `#F7F8FA` | Alternate neutral surface |

### Semantic aliases

- `background`: `white`
- `surface`: `gray-050`
- `surface-accent`: `blue-050`
- `text-primary`: `ink-950`
- `text-secondary`: `ink-700`
- `text-muted`: `ink-500`
- `border`: `gray-200`
- `primary`: `blue-900`
- `primary-hover`: `blue-800`
- `focus`: `blue-700`

Use blue selectively; white space should dominate. Do not add warm cream, peach, tan, or coral foundation colors without an explicit future decision.

## Typography

### Type logic

BIG IDEAs Lab uses three self-hosted, free, open-source families:

1. **Source Serif 4** for the Title opening display treatment only.
2. **Inter** for slide headings, body text, labels, navigation, and interface copy. Slide headings inside the fixed stage use Inter semibold at 60px/1.02 with -0.03em tracking; serif headings are reserved for the Title opening layout.
3. **IBM Plex Mono** for measurements, tokens, code, and compact data.

### Font families

- `font-display`: `Source Serif 4`, serif
- `font-sans`: `Inter`, sans-serif
- `font-mono`: `IBM Plex Mono`, monospace

All three families are self-hosted under the SIL Open Font License. Do not introduce proprietary or subscription-only fonts into the system.

### Type roles

| Role | Family | Size / line-height | Weight | Tracking |
|---|---|---:|---:|---:|
| Display XL | Display | `clamp(3.5rem, 8vw, 8rem) / 0.92` | 400 | `-0.045em` |
| Display L | Display | `clamp(2.75rem, 6vw, 5.5rem) / 0.96` | 400 | `-0.035em` |
| Heading 1 | Sans | `3rem / 1.02` | 500 | `-0.035em` |
| Heading 2 | Sans | `2rem / 1.1` | 500 | `-0.025em` |
| Heading 3 | Sans | `1.375rem / 1.2` | 500 | `-0.015em` |
| Body L | Sans | `1.25rem / 1.55` | 400 | `-0.01em` |
| Body | Sans | `1rem / 1.55` | 400 | `-0.005em` |
| Small | Sans | `0.875rem / 1.45` | 400 | `0` |
| Label | Sans | `0.75rem / 1.2` | 500 | `0.08em` |
| Data | Mono | `0.875rem / 1.4` | 400 | `0` |

Labels may use uppercase. Body copy should not. Avoid bold-heavy pages; hierarchy should come mainly from scale, family, spacing, and color.

## Radius

Rounded edges are a **system value, not a per-deck choice**. Decks consume these
tokens rather than declaring their own radius, which is what previously let card
corners drift to square.

| Token | Value | Role |
|---|---:|---|
| `--radius-card` | `16px` | Cards and grouped content surfaces — the working default on every presentation |
| `--radius-media` | `32px` | Image and media crops |
| `--radius-pill` | `999px` | Page turners and other fully rounded controls |

Button-like controls stay nearly square (`--button-radius`, `3px`). The canonical
card is `.bil-card`, with `.bil-card--accent` for the navy top rule,
`.bil-card--raised` for elevation, and `.bil-card--wash` for a pale blue surface.

## Media storage

All durable media belongs under `assets/`, organized by function:

- `logos/` — approved lab and institutional marks, with source and export variants
- `photography/` — original or licensed photographs
- `illustrations/` — editable illustrations and exports
- `icons/` — icon source sets and approved exports
- `figures/` — reusable scientific figures and figure templates
- `video/` — motion assets and poster frames
- `audio/` — audio assets and transcripts
- `fonts/` — self-hosted open-source font files and OFL records

All image and media specimens use rounded 32px crops with no visible outline; captions remain outside the clipped image region. Every media directory contains a `.gitkeep` until approved assets are added. Use descriptive lowercase kebab-case filenames. Store editable sources beside exports when practical. Do not add stock media without source, license, and attribution records.

The incumbent approved mark is `assets/logos/big-ideas-lab-logo.png`. Show it without redrawing, recoloring, or applying visual effects. Empty media categories must remain restrained storage specimens; do not fabricate previews.

## Slides

Slide templates use a 16:9 frame and the canonical color and typography tokens. The core set is:

- **Title** — opening label, title, institution context line, and logo. Its fixed-stage opening composition follows the review gallery: 422px lockup at right 44px/top 39px; title at left 134px/top 378px with a 672px cap and regular Source Serif 4 at 80px/1.08; metadata slots Presenter Name · Presentation Date · Duke University directly below. Use the specimen “Ideas that move<br>the world.” for catalog and starter previews while preserving the context slot.
- **Title with Media** — title at left 120px/top 54px, metadata at left 120px/top 196px, and a 1180×660 media frame centred at x=370px/top=270px. Media uses `object-fit: contain`, a 32px radius, and no visible outline. Keep the title and lockup in one shared top band. The title uses Inter semibold, not the display serif.
- **Section Divider** — numbered transition with a short section title.
- **Content / Research** — question or finding, supporting copy, and evidence or method note.
- **Data / Results** — primary measure and a clearly labeled comparison area.

Specimens describe structure only. Use concise labels and neutral placeholders; do not invent research findings, performance claims, citations, or other laboratory content. Preserve generous margins, align content to a stable reading edge, and reserve blue for identity and emphasis. Approved opening exception: `Sunburst / spectral-edge` may appear as a restrained lower-right optical glass/spectral edge on Title and Title with Media opening layouts only. It is decorative, not content media, and does not permit a general glass/gradient UI pattern. Regular stays undecorated.

## Presentation motion

Motion supports sequence and comprehension. Approved patterns are fade with a slight rise, left-to-right line reveal, and short staged entrances for related data marks.

- Keep individual transitions under roughly 700 ms.
- Use short offsets between related elements; avoid continuous or decorative motion.
- Provide a replay control when motion is demonstrated in a specimen.
- Honor `prefers-reduced-motion` by minimizing duration and removing staggered delays.
- Do not use gradients, color cycling, spring effects, or exaggerated travel.

## Current boundary

There are intentionally no marketing pages, product layouts, dashboards, finished presentations, laboratory claims, or fabricated media in this version. Slide specimens are reusable structures, not presentation content. New visual values must be introduced through the canonical token files before use in the catalog.
