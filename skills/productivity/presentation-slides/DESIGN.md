# Presentation design contract

The recovered `design-system/` package is canonical. Its tokens and rules use a white default canvas, blue brand/interaction color, and an editorial display plus precise grotesk sans relationship.

| Token | Value | Role |
|---|---|---|
| blue-900 | `#012169` | primary brand blue |
| blue-800 | `#003A70` | heritage blue, links, strong accents |
| blue-700 | `#00539B` | interactive blue |
| blue-100 | `#E8F1FA` | pale blue surface |
| blue-050 | `#F4F8FC` | subtle blue wash |
| white | `#FFFFFF` | default background |
| ink-950 | `#111318` | primary text |
| ink-700 | `#3F4650` | secondary text |
| ink-500 | `#68717D` | metadata and captions |
| gray-200 | `#D9DEE5` | borders and dividers |
| gray-100 | `#EDF0F4` | disabled/quiet surfaces |
| gray-050 | `#F7F8FA` | alternate neutral surface |

Semantic aliases are background=`white`, surface=`gray-050`, surface-accent=`blue-050`, text-primary=`ink-950`, text-secondary=`ink-700`, text-muted=`ink-500`, border=`gray-200`, primary=`blue-900`, primary-hover=`blue-800`, and focus=`blue-700`. White space dominates; no warm foundation palette, gradients, glass, or dashboard decoration.

Typography follows the recovered Hume AI reference logic: `Sharp Type`, `Georgia`, `Times New Roman`, serif for display; `PP Neue Montreal`, `Helvetica Neue`, `Arial`, sans-serif for body, labels, navigation, data, and UI; and `SFMono-Regular`, `Consolas`, monospace for data. Sharp Type and PP Neue Montreal are commercial typefaces: licensed files only may be stored under `design-system/assets/fonts/`, with fallbacks used until licensed.

Slides are fixed 1920×1080 stages scaled uniformly to fit. Slide headings use Inter semibold at 60px/1.02 with -0.03em tracking and span the content width; Source Serif 4 is reserved for the Title opening treatment. Body content is centered within the region between the heading and the bottom pager, not within the full 1080px canvas. The canonical Title opening follows the review-gallery composition: the approved full-stage Sunburst / spectral-edge asset remains behind everything; the combined lockup is 422px wide at right 44px/top 39px; the title begins at left 134px/top 378px, is capped at 672px, and uses regular Georgia at 80px/1.08; Presenter Name · Presentation Date metadata slots sit directly below. Title with Media keeps its title at left 120px/top 54px and metadata at left 120px/top 196px, with a 1180×660 media frame centred at x=370px/top=270px. Fit media with `object-fit: contain`, preserve a 32px radius, and omit any visible outline. The canonical specimen is “Ideas that move<br>the world.” Use concise, neutral specimens and preserve stable reading edges, generous margins, and restrained motion. Title and Title with Media opening layouts may use the approved `Sunburst / spectral-edge` decorative exception: a restrained lower-right optical glass/spectral edge, full-slide and edge-aligned behind content. It does not apply to content media or establish a general glass/gradient UI pattern. Regular remains undecorated. The combined `black_duke_bigideaslab.png` lockup is required across title and regular templates and previews. The three fixed layouts—Title, Title with Media, and Regular—are defined only by `slide-templates/template-manifest.json`; variation comes from the 13 component contracts.

The approved logo is `design-system/assets/logos/big-ideas-lab-logo.png`; it is bundled with the asset register and must not be redrawn, recolored, or given effects. New project assets require approval and provenance/licensing records.
