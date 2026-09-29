# Media Asset Register

| Asset ID | File | Category | Source / creator | License | Attribution required | Editable source | Status | Notes |
|---|---|---|---|---|---|---|---|---|
| logo-big-ideas-lab-primary | `assets/logos/big-ideas-lab-logo.png` | logos | BIG IDEAs Lab | Lab-owned identity asset | No | Not available in this repository | approved | Incumbent lab logo; black letterforms and orbit with a Duke-blue waveform on a white raster background. Preserve proportions; do not recolor or recreate. |
| bil-opening-sunburst-spectral-edge | `assets/decor/bil-opening-sunburst-spectral-edge.png` | decor | BIL opening layouts | Approved source: Sunburst / spectral-edge | No | Source selected from `.hermes/media/bil-v4/attempts/sunburst__spectral-edge__01/output.png`; normalized with 8 px white canvas above to 1920 × 1080 RGB | approved | Restrained lower-right optical glass/spectral edge for Title and Title with Media opening layouts only; never content media and never a general glass/gradient UI pattern. Empty alt, aria-hidden, and pointer-events none. |

Allowed status values: `candidate`, `approved`, `deprecated`.

Do not place an asset in production use until its source and license fields are complete.

## Agent invocation

Use the exact repository-relative path exposed in the catalog. The instruction copied from each asset card follows this contract:

> Use the exact approved file `design-system/assets/logos/<filename>`; preserve proportions, avoid recoloring or effects, and use it on the appropriate light or dark background.

The catalog is the source of truth for the approved filename and background pairing. Do not ask an agent to redraw a mark, approximate it with text, or choose a similarly named file. Use **Agent use → Copy agent instruction** on the asset card when handing the asset to an agent.
