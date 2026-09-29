# Media Asset Register

This register covers every bundled identity asset. **Status means approved for the BIL design system; it is not a legal or trademark approval.** The package is intended for authorized BIG IDEAs Lab use. Institutional marks are excluded from the repository's MIT license, and current Duke brand and trademark requirements still apply.

| Asset ID | File | Category | Source / creator | Use boundary | Attribution required | Editable source | Status | Notes |
|---|---|---|---|---|---|---|---|---|
| logo-big-ideas-lab-primary | `assets/logos/big-ideas-lab-logo.png` | logos | BIG IDEAs Lab | BIL-internal institutional mark; outside MIT | No | Not available in this repository | approved | Incumbent lab logo; preserve proportions; do not recolor or recreate. |
| logo-bil-circle-black | `assets/logos/black_bil_circle.png` | logos | Existing BIL design library; original export provenance not recorded | BIL-internal institutional mark; outside MIT | No | Not available in this repository | approved | Black circular BIL variant for light backgrounds. |
| logo-bil-circle-white | `assets/logos/white_bil_circle.png` | logos | Existing BIL design library; original export provenance not recorded | BIL-internal institutional mark; outside MIT | No | Not available in this repository | approved | White circular BIL variant for dark backgrounds. |
| logo-bil-horizontal-black | `assets/logos/black_bil_horizontal.png` | logos | Existing BIL design library; original export provenance not recorded | BIL-internal institutional mark; outside MIT | No | Not available in this repository | approved | Black horizontal BIL variant for light backgrounds. |
| logo-bil-horizontal-black-alt | `assets/logos/black_bil_horizontal2.png` | logos | Existing BIL design library; original export provenance not recorded | BIL-internal institutional mark; outside MIT | No | Not available in this repository | approved | Alternate black horizontal BIL export; use only where the catalog specifies it. |
| logo-bil-horizontal-white | `assets/logos/white_bil_horizontal.png` | logos | Existing BIL design library; original export provenance not recorded | BIL-internal institutional mark; outside MIT | No | Not available in this repository | approved | White horizontal BIL variant for dark backgrounds. |
| logo-bil-two-line-white | `assets/logos/white_bil_two_line.png` | logos | Existing BIL design library; original export provenance not recorded | BIL-internal institutional mark; outside MIT | No | Not available in this repository | approved | White two-line BIL variant for dark backgrounds. |
| logo-duke-bme | `assets/logos/Duke_BiomedicalEngineering_Logo.png` | logos | Duke University / Duke Biomedical Engineering | Duke institutional mark; outside MIT; Duke requirements apply | No | Not available in this repository | approved | Use the official file unchanged; repository inclusion is not permission for third-party use. |
| logo-duke-big-ideas-black | `assets/logos/black_duke_bigideaslab.png` | logos | Existing Duke/BIL design library; original export provenance not recorded | Duke/BIL institutional mark; outside MIT; Duke requirements apply | No | Not available in this repository | approved | Canonical black co-branded opening-slide lockup for light backgrounds. |
| logo-duke-big-ideas-white | `assets/logos/white_duke_bigideaslab.png` | logos | Existing Duke/BIL design library; original export provenance not recorded | Duke/BIL institutional mark; outside MIT; Duke requirements apply | No | Not available in this repository | approved | White co-branded lockup for dark backgrounds. |
| logo-duke-bil-circle-white | `assets/logos/white_duke_bil_circle.png` | logos | Existing Duke/BIL design library; original export provenance not recorded | Duke/BIL institutional mark; outside MIT; Duke requirements apply | No | Not available in this repository | approved | White circular co-branded variant for dark backgrounds. |
| logo-duke-bil-horizontal-white | `assets/logos/white_duke_bil_horizontal.png` | logos | Existing Duke/BIL design library; original export provenance not recorded | Duke/BIL institutional mark; outside MIT; Duke requirements apply | No | Not available in this repository | approved | White horizontal co-branded variant for dark backgrounds. |
| logo-duke-bil-horizontal-white-alt | `assets/logos/white_duke_bil_horizontal2.png` | logos | Existing Duke/BIL design library; original export provenance not recorded | Duke/BIL institutional mark; outside MIT; Duke requirements apply | No | Not available in this repository | approved | Alternate white horizontal co-branded export; use only where the catalog specifies it. |
| bil-opening-sunburst-spectral-edge | `assets/decor/bil-opening-sunburst-spectral-edge.png` | decor | BIL opening layouts | Approved BIL design-system asset | No | Source selected from the BIL V4 media-generation attempts and normalized to a 1920 × 1080 RGB canvas | approved | Restrained lower-right optical glass/spectral edge for Title and Title with Media opening layouts only; never content media or a general glass/gradient UI pattern. Empty alt, aria-hidden, and pointer-events none. |

Allowed status values: `candidate`, `approved`, `deprecated`.

Do not place an asset in production use until its source and use-boundary fields are complete. Unknown original export provenance is disclosed rather than inferred; confirm it before distributing a mark outside the lab workflow.

## Agent invocation

Use the exact repository-relative path exposed in the catalog. The instruction copied from each asset card follows this contract:

> Use the exact approved file `design-system/assets/logos/<filename>` for authorized BIL work; preserve proportions, avoid recoloring or effects, and use it on the appropriate light or dark background.

The catalog is the source of truth for the approved filename and background pairing. Do not ask an agent to redraw a mark, approximate it with text, or choose a similarly named file. Use **Agent use → Copy agent instruction** on the asset card when handing the asset to an agent.
