# Offline HTML contract

The rendered report is a **single self-contained `.html` file** that works from a local filesystem with no network access and no JavaScript. Lab members open it on a laptop, project it in a meeting, and print it.

## Hard requirements

| Requirement | Why |
|---|---|
| Stylesheet embedded in `<style>` | no external CSS request, no broken styling offline |
| At most one inline `<script data-bil-spy>`, with no `src` | the document must be complete and readable with scripting disabled; the only script is the optional active-section marker |
| No absolute `http(s)://` URLs | no fonts, images, analytics, or trackers fetched |
| No `<link>` elements | no external stylesheets or preloads |
| No `src=` attributes | no images or media fetched at open time |
| No `@import` | no nested stylesheet fetch |
| Native `<details>`/`<summary>` for collapse | no script needed for interaction |
| Webfont stacks fall back to system fonts | `Source Serif 4`, `Inter`, and `IBM Plex Mono` are preferred, not required |

`scripts/build_report.py` enforces all of the above and exits non-zero if a violation appears in the render. Run it before delivering any report.

## Progressive enhancement only

The scroll-spy that marks the current section in the sticky nav is the single permitted script. It adds `aria-current="true"` to one navigation link. Everything else — the section list, the tables, the cards, the collapsed details — is native HTML and CSS:

- the nav is a plain list of in-page links, so it navigates with scripting disabled;
- card details use native `<details>`/`<summary>`;
- no content is inserted, fetched, or computed by script;
- removing the script leaves a complete, readable document.

Do not introduce scripts that fetch data, mutate content, or depend on a network. A report that needs JavaScript to show its evidence is not within this contract.

## Data separation

Keep the report **data** separate from the **render**:

- the data file (JSON) is the durable record — it is what gets updated when evidence changes;
- the rendered HTML is a build product, regenerated rather than hand-edited.

Never hand-edit a rendered report. Edit the data and rebuild, so the artifact stays reproducible from its inputs.

## Accessibility

- Semantic landmarks: `header`, `nav`, `main`, `section`, `footer`.
- One `<h1>`; section headings in order.
- Tables carry `<caption>` and column `scope`.
- Axis and state chips expose their full text, not color alone.
- Interactive targets meet 44 px minimum height.
- Text contrast uses `ink-950` on `white` and `blue-800` on `white`; never light blue text on white.
- `prefers-reduced-motion` disables transitions.

## Print

- All `<details>` render expanded in print, so no evidence is lost on paper.
- Sections avoid breaking across pages.
- Sticky navigation is dropped.
- Borders stay a hairline gray; the palette becomes black on white.

## Sizing

- Single column, max 1080 px, centred.
- Hypothesis cards: two columns at 900 px and above, one below.
- Tables scroll horizontally inside their own container rather than pushing the page wide.

## When an image is genuinely required

Prefer none. If a report must include a figure, embed it as a `data:` URI so the file stays self-contained, and record the figure's provenance in the report footer. A figure with no provenance is not acceptable in a decision-grade artifact.
