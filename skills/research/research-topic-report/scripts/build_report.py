#!/usr/bin/env python3
"""Render a neutral BIL research-topic report as one self-contained HTML file.

Usage:
  python3 scripts/build_report.py --data templates/report-data.example.json --out report.html

The generated file embeds the stylesheet and the report data, makes no network
requests, and requires no JavaScript. Exit status 0 means the artifact was
written and passed the offline contract checks.
"""
from __future__ import annotations

import argparse
import datetime as _dt
import html
import json
import re
import sys
from pathlib import Path

SKILL_ROOT = Path(__file__).resolve().parents[1]
STYLESHEET = SKILL_ROOT / "templates" / "style.css"

FORBIDDEN_PATTERNS = (
    (re.compile(r"https?://"), "absolute URL"),
    (re.compile(r"<script\b(?![^>]*\bdata-bil-spy\b)", re.I), "unexpected script tag"),
    (re.compile(r"@import"), "CSS @import"),
    (re.compile(r"<link\b", re.I), "external stylesheet link"),
    (re.compile(r"\ssrc\s*=", re.I), "external resource reference"),
)

# The only JavaScript the report may carry: a small, self-contained active-section
# marker for the sticky nav. The document stays complete and readable without it.
SPY_SCRIPT = """<script data-bil-spy>
(function () {
  var sections = [].slice.call(document.querySelectorAll('section.section'));
  var links = {};
  [].slice.call(document.querySelectorAll('.section-nav a')).forEach(function (a) {
    links[(a.getAttribute('href') || '').slice(1)] = a;
  });
  function mark() {
    var y = window.scrollY + 96, current = null;
    sections.forEach(function (s) { if (s.offsetTop <= y) { current = s.id; } });
    if (!current && sections.length) { current = sections[0].id; }
    Object.keys(links).forEach(function (id) {
      if (id === current) { links[id].setAttribute('aria-current', 'true'); }
      else { links[id].removeAttribute('aria-current'); }
    });
  }
  window.addEventListener('scroll', mark, { passive: true });
  window.addEventListener('resize', mark, { passive: true });
  mark();
})();
</script>"""


AXIS_DIRECTIONS = {
    "scientific_risk": "higher is riskier",
    "execution_risk": "higher is riskier",
    "time_to_evidence": "lower is faster",
    "potential_impact": "higher is better",
}

AXIS_LABELS = {
    "scientific_risk": "Scientific risk",
    "execution_risk": "Execution risk",
    "time_to_evidence": "Time to evidence",
    "potential_impact": "Potential impact",
}

# Compact labels keep a chip from breaking mid-word at 390px; the full name is
# still rendered in the chip's tooltip and in the axis legend.
AXIS_SHORT = {
    "scientific_risk": "Sci. risk",
    "execution_risk": "Exec. risk",
    "time_to_evidence": "Time",
    "potential_impact": "Impact",
}

DETAIL_FIELDS = (
    ("Prediction", "prediction"),
    ("Falsifier", "falsifier"),
    ("Minimum evidence", "minimum_evidence"),
    ("Rival explanation", "rival"),
    ("Null or redundancy", "null"),
    ("Artifact or confounding", "artifact"),
)

SKEPTIC_GROUPS = (
    ("blocking", "Blocking defects"),
    ("high_impact", "High-impact improvements"),
    ("optional", "Optional notes"),
)

# PRISMA-like screening flow. Stage kinds: step advances, minus removes,
# hold is a visible end state that is neither an inclusion nor an exclusion.
FLOW_STAGE_KINDS = {"step", "minus", "hold"}

FLOW_REQUIRED_RULES = (
    "unique screened = excluded + promoted + uncertain",
    "full text assessed + not retrieved = sought for full text",
    "included + excluded at full text = full text assessed",
    "exclusion reasons sum to their stage total",
)

CLAIM_MAX_CHARS = 180
MONO_ATTR = ' class="mono"'


def esc(value) -> str:
    return html.escape("" if value is None else str(value), quote=True)


def as_list(value) -> list:
    if value is None:
        return []
    if isinstance(value, list):
        return value
    return [value]


def require(data, key, kind=None, where="report data"):
    if key not in data:
        raise ValueError(f"{where}: missing required field {key!r}")
    value = data[key]
    if kind is not None and not isinstance(value, kind):
        raise ValueError(f"{where}: field {key!r} must be {kind.__name__}")
    return value


def mono_attr(column) -> str:
    return MONO_ATTR if column.get("mono") else ""


def render_meta(data) -> str:
    rows = [
        ("Lane", data.get("lane", "routine")),
        ("Topic ID", data.get("topic_id", "")),
        ("Built", data.get("built", _dt.date.today().isoformat())),
    ]
    dl = "".join(f"<dt>{esc(k)}</dt><dd>{esc(v)}</dd>" for k, v in rows if v)
    badge = f'<span class="lane-badge">{esc(data.get("lane", "routine"))} lane</span>'
    return badge + f"<dl>{dl}</dl>"


def render_nav(sections) -> str:
    items = "".join(
        f'<li><a href="#{esc(s["id"])}">'
        f'<span class="nav-index">{i:02d}</span>{esc(s["title"])}</a></li>'
        for i, s in enumerate(sections, start=1)
    )
    return f'<nav class="section-nav" aria-label="Report sections"><ul>{items}</ul></nav>'


def render_list(items, ordered=False) -> str:
    items = as_list(items)
    if not items:
        return '<p class="empty">None recorded.</p>'
    tag = "ol" if ordered else "ul"
    rows = "".join(f"<li>{esc(i)}</li>" for i in items)
    return f"<{tag}>{rows}</{tag}>"


def render_table(spec) -> str:
    columns = require(spec, "columns", list, "table")
    rows = spec.get("rows", [])
    caption = spec.get("caption", "")
    head = "".join(
        f'<th scope="col"{mono_attr(c)}>{esc(c["label"])}</th>' for c in columns
    )
    body = []
    for row in rows:
        cells = "".join(
            f"<td{mono_attr(c)}>{esc(row.get(c['key'], ''))}</td>" for c in columns
        )
        body.append(f"<tr>{cells}</tr>")
    if not body:
        body.append(
            f'<tr><td colspan="{len(columns)}" class="empty">No records.</td></tr>'
        )
    caption_html = f"<caption>{esc(caption)}</caption>" if caption else ""
    return (
        '<div class="table-wrap"><table>'
        f"{caption_html}<thead><tr>{head}</tr></thead>"
        f"<tbody>{''.join(body)}</tbody></table></div>"
    )


def render_callout(spec) -> str:
    title = spec.get("title", "Note")
    return f'<div class="callout"><h3>{esc(title)}</h3>{render_list(spec.get("items"))}</div>'


def render_prose(blocks) -> str:
    out = []
    for block in as_list(blocks):
        if isinstance(block, str):
            out.append(f"<p>{esc(block)}</p>")
        elif isinstance(block, dict):
            if "list" in block:
                out.append(render_list(block["list"], ordered=bool(block.get("ordered"))))
            elif "table" in block:
                out.append(render_table(block["table"]))
            elif "callout" in block:
                out.append(render_callout(block["callout"]))
    if not out:
        return '<p class="empty">None recorded.</p>'
    return "".join(out)


def render_axis_chips(hyp) -> str:
    hyp_id = hyp.get("id", "?")
    axes = require(hyp, "axes", dict, f"hypothesis {hyp_id}")
    chips = []
    for key, label in AXIS_LABELS.items():
        if key not in axes:
            raise ValueError(f"hypothesis {hyp_id}: missing axis {key!r}")
        value = axes[key].get("value", "")
        rationale = axes[key].get("rationale", "")
        title = f"{label}: {value} ({AXIS_DIRECTIONS[key]}). {rationale}".strip()
        chips.append(
            f'<li class="chip" data-value="{esc(value)}" title="{esc(title)}">'
            f'<span class="chip-label">{esc(AXIS_SHORT[key])}</span>'
            f'<span class="chip-value">{esc(value)}</span></li>'
        )
    chips.append(
        '<li class="chip" data-kind="state">'
        '<span class="chip-label">Claim state</span>'
        f'<span class="chip-value">{esc(hyp.get("claim_state", "unknown"))}</span></li>'
    )
    return f'<ul class="chips">{"".join(chips)}</ul>'


def render_hypotheses(hypotheses) -> str:
    hypotheses = as_list(hypotheses)
    if not hypotheses:
        return '<p class="empty">No hypotheses recorded.</p>'
    cards = []
    for hyp in hypotheses:
        require(hyp, "id", str, "hypothesis")
        require(hyp, "title", str, "hypothesis")
        claim = require(hyp, "claim", str, "hypothesis")
        if len(claim) > CLAIM_MAX_CHARS:
            raise ValueError(
                f"hypothesis {hyp['id']}: claim exceeds the {CLAIM_MAX_CHARS}-character "
                "DESIGN.md limit"
            )
        details = "".join(
            f"<dt>{label}</dt><dd>{esc(hyp[key])}</dd>"
            for label, key in DETAIL_FIELDS
            if hyp.get(key)
        )
        details_html = (
            "<details><summary>Prediction, falsifier, and alternatives</summary>"
            f"<dl>{details}</dl></details>"
            if details
            else ""
        )
        cards.append(
            '<article class="hypothesis">'
            f'<p class="id">{esc(hyp["id"])} · {esc(hyp.get("class", "unclassified"))}</p>'
            f"<h3>{esc(hyp['title'])}</h3>"
            f'<p class="claim">{esc(claim)}</p>'
            f"{render_axis_chips(hyp)}{details_html}</article>"
        )
    return f'<div class="hypotheses">{"".join(cards)}</div>'


def render_skeptic(spec) -> str:
    parts = []
    for key, label in SKEPTIC_GROUPS:
        items = spec.get(key, [])
        body = render_list(items) if items else '<p class="empty">None recorded.</p>'
        parts.append(f'<div class="skeptic-group"><h3>{label}</h3>{body}</div>')
    independence = spec.get("independence", "unlabeled")
    dissent = spec.get("dissent", [])
    dissent_html = (
        f'<div class="callout"><h3>Preserved dissent</h3>{render_list(dissent)}</div>'
        if dissent
        else ""
    )
    return (
        f'<p><span class="independence">{esc(independence)}</span> '
        "Critic independence is labeled as recorded; a same-context pass is never "
        "presented as independent.</p>"
        f"{''.join(parts)}{dissent_html}"
    )


def render_flow(spec) -> str:
    """Render a PRISMA-like screening flow: stages, exclusion branches, the
    reconciled counts, and the screener attribution."""
    stages = require(spec, "stages", list, "flow")
    if not stages:
        raise ValueError("flow: at least one stage is required")
    rows = []
    for index, stage in enumerate(stages, start=1):
        label = esc(require(stage, "label", str, "flow stage"))
        kind = stage.get("kind", "step")
        if kind not in FLOW_STAGE_KINDS:
            raise ValueError(f"flow stage {index}: unknown kind {kind!r}")
        subitems = stage.get("routes") or stage.get("breakdown") or []
        sub_html = ""
        if subitems:
            items = "".join(
                f'<li><span>{esc(item["label"])}</span>'
                f'<span class="num">{esc(item.get("count", ""))}</span></li>'
                for item in subitems
            )
            sub_html = f'<ul class="flow-sub">{items}</ul>'
        box = (
            f'<div class="flow-box {esc(kind)}">'
            f'<span class="flow-order">{index:02d}</span>'
            f'<span class="flow-label">{label}</span>'
            f'<span class="flow-count num">{esc(stage.get("count", ""))}</span>'
            f"</div>{sub_html}"
        )
        branch = stage.get("branch")
        branch_html = ""
        if branch:
            reasons = branch.get("reasons") or []
            reason_html = ""
            if reasons:
                items = "".join(
                    f'<li><span>{esc(r["label"])}</span>'
                    f'<span class="num">{esc(r.get("count", ""))}</span></li>'
                    for r in reasons
                )
                reason_html = f'<ul class="flow-sub">{items}</ul>'
            branch_html = (
                '<aside class="flow-branch">'
                f'<p class="branch-label">{esc(branch.get("label", "Excluded"))}'
                f'<span class="num">{esc(branch.get("count", ""))}</span></p>'
                f"{reason_html}</aside>"
            )
        rows.append(f'<div class="flow-row">{box}{branch_html}</div>')

    rules = []
    for rule in spec.get("reconciliation") or []:
        # The state is derived from the numbers, never trusted from the flag
        # alone: a stale "ok": true must not render a PASS beside counts that
        # disagree.
        agrees = rule.get("lhs") == rule.get("rhs")
        state = "PASS" if (rule.get("ok") and agrees) else "FAIL"
        rules.append(
            f'<li class="rule {state.lower()}"><span class="state">{state}</span>'
            f'<span class="rule-text">{esc(rule.get("rule", ""))} '
            f'<span class="num">{esc(rule.get("lhs", ""))} = {esc(rule.get("rhs", ""))}</span>'
            f"</span></li>"
        )
    recon_html = (
        '<div class="flow-recon"><h3>Count reconciliation</h3>'
        f'<ul>{"".join(rules)}</ul></div>'
        if rules
        else ""
    )

    attribution = spec.get("attribution") or []
    attr_html = ""
    if attribution:
        pairs = "".join(
            f'<dt>{esc(a["label"])}</dt><dd>{esc(a.get("value", ""))}</dd>'
            for a in attribution
        )
        attr_html = f'<dl class="flow-attr">{pairs}</dl>'

    return f'<div class="flow">{"".join(rows)}</div>{recon_html}{attr_html}'


SECTION_RENDERERS = {
    "prose": render_prose,
    "hypotheses": render_hypotheses,
    "skeptic": render_skeptic,
    "flow": render_flow,
}


def section_body(section) -> str:
    """Render a section's own section-type body, plus an optional prose lead."""
    kind = section.get("kind", "prose")
    renderer = SECTION_RENDERERS.get(kind)
    if renderer is None:
        raise ValueError(f"section {section.get('id', '?')}: unknown kind {kind!r}")
    parts = []
    if kind != "prose" and section.get("lead"):
        parts.append(render_prose(section["lead"]))
    parts.append(renderer(section.get("body", [])))
    return "".join(parts)


def render_sections(data):
    sections = require(data, "sections", list)
    if not sections:
        raise ValueError("report data: at least one section is required")
    nav = render_nav(sections)
    rendered = []
    for index, section in enumerate(sections, start=1):
        body = section_body(section)
        rendered.append(
            f'<section class="section" id="{esc(section["id"])}">'
            f'<h2><span class="nav-index">{index:02d}</span> {esc(section["title"])}</h2>'
            f"{body}</section>"
        )
    return nav, "".join(rendered)


def build(data) -> str:
    css = STYLESHEET.read_text(encoding="utf-8")
    title = require(data, "title", str)
    statement = require(data, "topic_statement", str)
    nav, sections = render_sections(data)
    footer = data.get("footer", {})
    method = footer.get("method", "Method not recorded.")
    provenance = footer.get("provenance", "Provenance not recorded.")
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(title)}</title>
<style>
{css}
</style>
</head>
<body>
<header class="masthead">
<h1>{esc(title)}</h1>
<p class="topic-statement">{esc(statement)}</p>
<div class="meta-row">{render_meta(data)}</div>
</header>
{nav}
<main>
{sections}
</main>
<footer class="report-footer">
<p class="neutrality">Neutral hypothesis portfolio. No option, hypothesis, or direction is recommended; the portfolio and its trade-offs are presented for group discussion.</p>
<p>{esc(method)}</p>
<p>{esc(provenance)}</p>
</footer>
{SPY_SCRIPT}
</body>
</html>
"""


def check_offline(document) -> list:
    findings = []
    for pattern, label in FORBIDDEN_PATTERNS:
        for match in pattern.finditer(document):
            findings.append(f"{label}: {match.group(0)[:60]}")
    return findings


def flow_warnings(data) -> list:
    """A failed reconciliation rule must never ship silently.

    A review may disclose a non-reconciling count, so the render still
    succeeds — but every disagreement is surfaced on stderr rather than
    left for a reader to notice.
    """
    findings = []
    for section in data.get("sections", []):
        if section.get("kind") != "flow":
            continue
        body = section.get("body") or {}
        for rule in body.get("reconciliation") or []:
            if not rule.get("ok") or rule.get("lhs") != rule.get("rhs"):
                findings.append(
                    f"{section.get('id', '?')}: unreconciled — "
                    f"{rule.get('rule', '')} ({rule.get('lhs')} vs {rule.get('rhs')})"
                )
    return findings


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description="Render a neutral BIL research-topic report.")
    parser.add_argument("--data", required=True)
    parser.add_argument("--out", required=True)
    args = parser.parse_args(argv)

    data = json.loads(Path(args.data).read_text(encoding="utf-8"))
    try:
        document = build(data)
    except ValueError as exc:
        print(f"data error — {exc}", file=sys.stderr)
        return 2

    findings = check_offline(document)
    if findings:
        for finding in findings:
            print(f"offline contract violation — {finding}", file=sys.stderr)
        return 1

    out = Path(args.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(document, encoding="utf-8")

    # The report must advise nothing. "recommend" may only appear inside the
    # neutrality disclaimer itself.
    lines = [
        line
        for line in document.splitlines()
        if "recommend" in line.lower() and "neutrality" not in line
    ]
    for line in lines:
        print(f"neutrality warning — {line.strip()[:120]}", file=sys.stderr)

    for warning in flow_warnings(data):
        print(f"flow reconciliation warning — {warning}", file=sys.stderr)

    lines_written = document.count("\n") + 1
    print(f"wrote {out} ({out.stat().st_size} bytes, {lines_written} lines) — offline contract clean")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
