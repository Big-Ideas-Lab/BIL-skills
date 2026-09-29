# Research topic report — design contract

The report **reuses the BIL design tokens and typography** from the presentation system and defines its own **report layout rules**. It is a scrolling document, not a fixed-offset slide stage. Do not reflow slide geometry into the report, and do not introduce a second visual language.

Canonical token source: `design-system/tokens.json` in this skill directory, mirroring the BIG IDEAs Lab design foundations.

## Tokens

| Token | Value | Role |
|---|---|---|
| blue-900 | `#012169` | primary brand blue |
| blue-800 | `#003A70` | heritage blue, links, strong accents |
| blue-700 | `#00539B` | interactive blue, focus |
| blue-100 | `#E8F1FA` | pale blue surface |
| blue-050 | `#F4F8FC` | subtle blue wash |
| white | `#FFFFFF` | default background |
| ink-950 | `#111318` | primary text |
| ink-700 | `#3F4650` | secondary text |
| ink-500 | `#68717D` | metadata and captions |
| gray-200 | `#D9DEE5` | borders and dividers |
| gray-100 | `#EDF0F4` | quiet surfaces |
| gray-050 | `#F7F8FA` | alternate neutral surface |

Semantic aliases: background=`white`, surface=`gray-050`, surface-accent=`blue-050`, text-primary=`ink-950`, text-secondary=`ink-700`, text-muted=`ink-500`, border=`gray-200`, primary=`blue-900`, primary-hover=`blue-800`, focus=`blue-700`.

White space dominates. No gradients, glass, shadows-as-decoration, or dashboard chrome. Do not use color alone to communicate status — pair it with a label, position, or text.

## Typography

| Role | Stack | Use |
|---|---|---|
| Display | `Source Serif 4`, Georgia, `Times New Roman`, serif | report title and section headings |
| Interface | `Inter`, `Helvetica Neue`, Arial, sans-serif | body, labels, tables, UI |
| Data | `IBM Plex Mono`, `SFMono-Regular`, Consolas, monospace | identifiers, metric values, locators |

Both display and interface faces use system-available fallbacks; the report must not fetch webfonts. Body copy stays at 14 px or larger. Headings use weight 600 with tight tracking; the display face never sets table data.

## Report layout rules

- **Shell.** Single column. Max content width 1080 px, centred, chrome-free. Side padding 32 px desktop / 20 px mobile.
- **Rhythm.** 8 px base scale: 8 / 16 / 24 / 32 / 48 / 72.
- **Header.** Title, one-line topic statement, lane badge, build date, and a provenance line. No hero imagery.
- **Section heading.** Display face, 28 px desktop / 23 px mobile, with a 1 px bottom rule. Numbered sections matching `references/report-contract.md`.
- **Sticky section nav.** A compact horizontal list of the section numbers and short labels, sticky under the header, scrollable on narrow screens. It is navigation, not decoration.
- **Evidence table.** Full-width, `font-size: 13px`, `IBM Plex Mono` for identifiers and values, tabular numerals, sticky header row, horizontal scroll inside a bordered container on narrow screens. Never shrink columns below 96 px.
- **Hypothesis cards.** One card per hypothesis in a CSS grid: 2 equal columns ≥ 900 px, 1 column below. Cards are row-major and top-aligned; an odd count leaves one intentional empty cell in the last row rather than an uneven multi-column flow. Each card carries a short title, the one-line claim, four inline axis chips, a claim-state chip, and a collapsed details region for falsifier, minimum evidence, and alternative explanations.
- **Optional section lead.** A card-grid section may carry a `lead` array of prose paragraphs rendered above the grid — used for the chip legend. It does not replace the section body.
- **Axis chips.** Compact label (`Sci. risk`, `Exec. risk`, `Time`, `Impact`) plus ordinal value (`Low` / `Moderate` / `High`), never color alone. Chips are `flex: 0 0 auto` with `white-space: nowrap` so a value never breaks mid-word; the row wraps instead. The full axis name and direction live in the chip tooltip and in the legend line above the grid. Scientific risk and execution risk read higher-is-riskier; time to evidence reads shorter-is-better; potential impact reads higher-is-better.
- **Matrix view.** An accessible ordinal table pairing the four axes with rationale, and a small scatter only when truthful positions exist — no decorative quadrant claims.
- **Falsifier and minimum-evidence table.** Same treatment as the evidence table.
- **Callout for disagreements and unresolved questions.** 4 px left border in `blue-700`, `blue-050` surface. Never used for recommendations, because the report has none.
- **Skeptic section.** Findings grouped as blocking defects, high-impact improvements, and optional notes. Independence labels (`independent` / `same-context`) are rendered as text.
- **Footer.** Provenance, method summary, and the neutrality statement: no recommendation is offered; the portfolio is for group discussion.

## Interaction and accessibility

- Semantic landmarks (`header`, `nav`, `main`, `section`, `footer`) with heading levels in order.
- Collapsible details use native `<details>`/`<summary>` with visible labels and a 44 px minimum hit target.
- The page is fully readable with JavaScript disabled; collapse is native, not scripted.
- Focus ring uses `blue-700` at 2 px. Do not remove outlines.
- Tables carry `<caption>` and `scope` attributes. Axis chips expose their full text to assistive tech.
- Honor `prefers-reduced-motion`; motion is limited to a 120 ms opacity fade and is optional.

## Print

- Break inside sections is avoided; each section may start a new page.
- Collapsed `<details>` render expanded in print so no evidence is lost on paper.
- Print uses black text on white, drops the sticky nav, and keeps table borders at 1 px gray.

## Content limits

- Report length: aim for 900–1600 words of prose total, excluding tables.
- Section prose: max 120 words before a list, table, or card carries the detail instead.
- Evidence table: one row per source; no multi-source merged cells.
- Hypothesis cards: claim line max 180 characters.
- Cut any sentence that carries no evidence, trade-off, or open question.
