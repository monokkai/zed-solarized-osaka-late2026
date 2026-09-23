#!/usr/bin/env python3
"""Generate the Zed theme family from a single palette."""

import json
import os

PALETTE = {
    "base04": "#001419",
    "base05": "#00070B",
    "base03": "#002c38",
    "base02": "#063540",
    "base01": "#7b99a2",
    "base00": "#85a1ac",
    "base0": "#b6c5c6",
    "base1": "#c2cdcd",
    "base2": "#f4eeda",
    "base3": "#fff8e7",
    "blue": "#5aaefa",
    "cyan": "#34c5b9",
    "green": "#a2bb00",
    "orange": "#fb724a",
    "yellow": "#dba500",
    "red": "#ff6c6a",
    "magenta": "#fe67a8",
    "violet": "#9498ea",
    "gutter": "#664c00",
    "bracket": "#e0e2ea",
}

P = PALETTE


def hexa(color: str, alpha: float = 1.0) -> str:
    a = max(0, min(255, round(alpha * 255)))
    return f"{color}{a:02x}"


def syn(color: str, style=None, weight=None) -> dict:
    return {"color": hexa(color), "font_style": style, "font_weight": weight}


def build_style(blurred: bool) -> dict:
    surface_a = 0.69 if blurred else 1.0
    panel_a = 0.0 if blurred else 1.0
    editor_a = 0.0 if blurred else 1.0
    window_a = 0.50 if blurred else 1.0
    elem_a = 0.0 if blurred else 1.0

    bg = P["base05"] if blurred else P["base04"]
    line = P["base03"]
    sel = P["base02"]
    fg = P["base0"]
    dim = P["base01"]

    ui_text = "#c3c7c9"
    ui_text_muted = "#8b9295"

    style = {
        "background.appearance": "blurred" if blurred else "opaque",
        "background": hexa(bg, window_a),
        "border": hexa(P["base01"], 0.14 if blurred else 1.0),
        "border.variant": hexa(P["base01"], 0.09 if blurred else 0.6),
        "border.focused": hexa(P["blue"], 0.6),
        "border.selected": hexa(P["blue"], 0.8),
        "border.transparent": hexa(bg, 0.0),
        "border.disabled": hexa(sel, 0.4),
        "elevated_surface.background": hexa(bg, 1.0 if not blurred else 0.96),
        "surface.background": hexa(bg, window_a),
        "drop_target.background": hexa(P["blue"], 0.2),

        "text": hexa(ui_text),
        "text.muted": hexa(ui_text_muted),
        "text.placeholder": hexa(dim, 0.7),
        "text.disabled": hexa(dim, 0.5),
        "text.accent": hexa(P["orange"]),
        "link_text.hover": hexa(P["blue"]),

        "icon": hexa(ui_text),
        "icon.muted": hexa(ui_text_muted),
        "icon.disabled": hexa(dim, 0.5),
        "icon.placeholder": hexa(dim, 0.7),
        "icon.accent": hexa(P["orange"]),

        "element.background": hexa(line, elem_a),
        "element.hover": hexa(sel, 0.5 if blurred else 0.8),
        "element.active": hexa(sel, 0.0 if blurred else 1.0),
        "element.selected": hexa(sel, 0.3 if blurred else 1.0),
        "element.disabled": hexa(line, 0.5),
        "ghost_element.background": hexa(bg, 0.38 if blurred else 0.0),
        "ghost_element.hover": hexa(line, 0.56 if blurred else 0.5),
        "ghost_element.active": hexa(sel, 0.8),
        "ghost_element.selected": hexa(sel),
        "ghost_element.disabled": hexa(line, 0.4),

        "panel.background": hexa(bg, panel_a),
        "panel.focused_border": hexa(P["base01"], 0.14 if blurred else 0.6),
        "pane.focused_border": hexa(P["base01"], 0.14 if blurred else 0.6),
        "status_bar.background": hexa(bg, window_a),
        "title_bar.background": hexa(bg, window_a),
        "title_bar.inactive_background": hexa(bg, window_a * 0.95),
        "toolbar.background": hexa(bg, panel_a),
        "tab_bar.background": hexa(bg, panel_a),
        "tab.active_background": hexa(line, surface_a),
        "tab.inactive_background": hexa(bg, panel_a),

        "scrollbar.track.background": hexa(bg, 0.0),
        "scrollbar.track.border": hexa(sel, 0.0),
        "scrollbar.thumb.background": hexa(P["base01"], 0.3),
        "scrollbar.thumb.hover_background": hexa(P["base01"], 0.5),
        "scrollbar.thumb.border": hexa(sel, 0.0),

        "editor.background": hexa(bg, editor_a),
        "editor.foreground": hexa(fg),
        "editor.gutter.background": hexa(bg, editor_a),
        "editor.line_number": hexa(P["gutter"]),
        "editor.active_line_number": hexa(P["orange"]),
        "editor.hover_line_number": hexa(P["orange"], 0.8),
        "editor.active_line.background": hexa(line, 0.0 if blurred else 0.6),
        "editor.highlighted_line.background": hexa(line, 0.07 if blurred else 0.8),
        "editor.subheader.background": hexa(line, 0.0 if blurred else 1.0),
        "editor.invisible": hexa(sel),
        "editor.wrap_guide": hexa(sel, 0.5),
        "editor.active_wrap_guide": hexa(sel),
        "editor.document_highlight.read_background": hexa(P["blue"], 0.15),
        "editor.document_highlight.write_background": hexa(P["orange"], 0.15),

        "search.match_background": hexa(P["yellow"], 0.25),
        "search.active_match_background": hexa(P["yellow"], 0.45),

        "error": hexa(P["red"]),
        "error.background": hexa(P["red"], 0.12),
        "error.border": hexa(P["red"], 0.4),
        "warning": hexa(P["yellow"]),
        "warning.background": hexa(P["yellow"], 0.12),
        "warning.border": hexa(P["yellow"], 0.4),
        "info": hexa(P["blue"]),
        "info.background": hexa(P["blue"], 0.12),
        "info.border": hexa(P["blue"], 0.4),
        "hint": hexa(P["cyan"]),
        "hint.background": hexa(P["cyan"], 0.12),
        "hint.border": hexa(P["cyan"], 0.4),
        "success": hexa(P["green"]),
        "success.background": hexa(P["green"], 0.12),
        "success.border": hexa(P["green"], 0.4),
        "predictive": hexa(dim, 0.7),
        "predictive.background": hexa(dim, 0.1),
        "predictive.border": hexa(dim, 0.3),
        "conflict": hexa(P["magenta"]),
        "conflict.background": hexa(P["magenta"], 0.12),
        "conflict.border": hexa(P["magenta"], 0.4),
        "unreachable": hexa(dim),
        "unreachable.background": hexa(dim, 0.1),
        "unreachable.border": hexa(dim, 0.3),

        "created": hexa(P["green"]),
        "created.background": hexa(P["green"], 0.12),
        "created.border": hexa(P["green"], 0.4),
        "modified": hexa(P["yellow"]),
        "modified.background": hexa(P["yellow"], 0.12),
        "modified.border": hexa(P["yellow"], 0.4),
        "deleted": hexa(P["red"]),
        "deleted.background": hexa(P["red"], 0.12),
        "deleted.border": hexa(P["red"], 0.4),
        "renamed": hexa(P["blue"]),
        "renamed.background": hexa(P["blue"], 0.12),
        "renamed.border": hexa(P["blue"], 0.4),
        "hidden": hexa(dim),
        "hidden.background": hexa(dim, 0.1),
        "hidden.border": hexa(dim, 0.3),
        "ignored": hexa(dim, 0.7),
        "ignored.background": hexa(dim, 0.1),
        "ignored.border": hexa(dim, 0.3),
        "version_control.added": hexa(P["green"]),
        "version_control.modified": hexa(P["yellow"]),
        "version_control.deleted": hexa(P["red"]),
        "version_control.word_added": hexa(P["green"], 0.2),
        "version_control.word_deleted": hexa(P["red"], 0.2),
        "version_control.conflict_marker.ours": hexa(P["green"], 0.2),
        "version_control.conflict_marker.theirs": hexa(P["blue"], 0.2),

        "pane_group.border": hexa(P["base01"], 0.14 if blurred else 1.0),
        "editor.indent_guide": hexa(sel, 0.6),
        "editor.indent_guide_active": hexa(P["base01"], 0.8),
        "editor.debugger_active_line.background": hexa(P["orange"], 0.07),
        "editor.document_highlight.bracket_background": hexa(P["blue"], 0.09),
        "panel.indent_guide": hexa(sel, 0.6),
        "panel.indent_guide_active": hexa(P["base01"], 0.8),
        "panel.indent_guide_hover": hexa(P["blue"]),
        "panel.overlay_background": hexa(bg, 0.0 if blurred else 1.0),
        "minimap.thumb.background": hexa(P["base01"], 0.2),
        "minimap.thumb.hover_background": hexa(P["base01"], 0.4),
        "minimap.thumb.active_background": hexa(P["base01"], 0.6),
        "debugger.accent": hexa(P["red"]),
        "version_control.conflict": hexa(P["magenta"]),
        "version_control.ignored": hexa(dim),
        "version_control.renamed": hexa(P["blue"]),
        "terminal.ansi.background": hexa(bg, 0.0 if blurred else 1.0),
        "vim.mode.text": hexa(bg),
        "vim.normal.background": hexa(P["blue"]),
        "vim.normal.foreground": hexa(bg),
        "vim.insert.background": hexa(P["green"]),
        "vim.insert.foreground": hexa(bg),
        "vim.replace.background": hexa(P["red"]),
        "vim.replace.foreground": hexa(bg),
        "vim.visual.background": hexa(P["violet"]),
        "vim.visual.foreground": hexa(bg),
        "vim.visual_line.background": hexa(P["violet"]),
        "vim.visual_line.foreground": hexa(bg),
        "vim.visual_block.background": hexa(P["magenta"]),
        "vim.visual_block.foreground": hexa(bg),
        "vim.helix_normal.background": hexa(P["blue"]),
        "vim.helix_normal.foreground": hexa(bg),
        "vim.helix_select.background": hexa(P["violet"]),
        "vim.helix_select.foreground": hexa(bg),
        "terminal.background": hexa(bg, panel_a),
        "terminal.foreground": hexa(fg),
        "terminal.bright_foreground": hexa(P["base1"]),
        "terminal.dim_foreground": hexa(dim),
        "terminal.ansi.black": hexa(P["base03"]),
        "terminal.ansi.red": hexa(P["red"]),
        "terminal.ansi.green": hexa(P["green"]),
        "terminal.ansi.yellow": hexa(P["yellow"]),
        "terminal.ansi.blue": hexa(P["blue"]),
        "terminal.ansi.magenta": hexa(P["magenta"]),
        "terminal.ansi.cyan": hexa(P["cyan"]),
        "terminal.ansi.white": hexa(fg),
        "terminal.ansi.bright_black": hexa(dim),
        "terminal.ansi.bright_red": hexa(P["red"]),
        "terminal.ansi.bright_green": hexa(P["green"]),
        "terminal.ansi.bright_yellow": hexa(P["yellow"]),
        "terminal.ansi.bright_blue": hexa(P["blue"]),
        "terminal.ansi.bright_magenta": hexa(P["magenta"]),
        "terminal.ansi.bright_cyan": hexa(P["cyan"]),
        "terminal.ansi.bright_white": hexa(P["base1"]),
        "terminal.ansi.dim_black": hexa(P["base02"]),
        "terminal.ansi.dim_red": hexa(P["red"], 0.6),
        "terminal.ansi.dim_green": hexa(P["green"], 0.6),
        "terminal.ansi.dim_yellow": hexa(P["yellow"], 0.6),
        "terminal.ansi.dim_blue": hexa(P["blue"], 0.6),
        "terminal.ansi.dim_magenta": hexa(P["magenta"], 0.6),
        "terminal.ansi.dim_cyan": hexa(P["cyan"], 0.6),
        "terminal.ansi.dim_white": hexa(dim),
    }

    style["players"] = [
        {"cursor": hexa(c), "background": hexa(c), "selection": hexa(c, 0.24)}
        for c in [P["blue"], P["orange"], P["green"], P["magenta"],
                  P["cyan"], P["yellow"], P["violet"], P["red"]]
    ]

    style["syntax"] = {
        "comment": syn(dim, "italic"),
        "comment.doc": syn(dim, "italic"),

        "string": syn(P["cyan"]),
        "string.escape": syn(P["orange"]),
        "string.regex": syn(P["orange"]),
        "string.special": syn(P["orange"]),
        "string.special.symbol": syn(P["cyan"]),
        "text.literal": syn(P["cyan"]),

        "number": syn(P["cyan"]),
        "boolean": syn(P["cyan"]),
        "constant": syn(P["cyan"]),
        "variant": syn(P["magenta"]),

        "keyword": syn(P["green"]),
        "operator": syn(P["green"]),
        "tag": syn(P["green"]),

        "function": syn(P["blue"]),
        "property": syn(P["blue"]),
        "attribute": syn(P["blue"]),
        "selector": syn(P["blue"]),
        "selector.pseudo": syn(P["blue"]),
        "label": syn(P["blue"]),

        "type": syn(P["yellow"]),
        "enum": syn(P["yellow"]),
        "constructor": syn(P["red"]),

        "variable": syn(P["red"]),
        "variable.parameter": syn(P["orange"]),
        "variable.special": syn(P["violet"], "italic"),
        "namespace": syn(P["violet"]),

        "punctuation": syn(P["red"]),
        "punctuation.bracket": syn(P["red"]),
        "punctuation.delimiter": syn(P["red"]),
        "punctuation.special": syn(P["orange"]),
        "punctuation.list_marker": syn(P["red"]),
        "punctuation.markup": syn(P["red"]),

        "embedded": syn(fg),
        "emphasis": syn(P["orange"], "italic"),
        "emphasis.strong": syn(P["orange"], None, 700),
        "title": syn(P["green"], None, 700),
        "link_text": syn(P["blue"], "italic"),
        "link_uri": syn(P["cyan"]),

        "preproc": syn(P["violet"]),
        "primary": syn(fg),
        "hint": syn(P["cyan"]),
        "predictive": syn(dim, "italic"),
        "diff.plus": syn(P["green"]),
        "diff.minus": syn(P["red"]),
    }

    return style


def main() -> None:
    here = os.path.dirname(os.path.abspath(__file__))
    out = os.path.join(here, "themes", "solarized-osaka-late2026.json")
    os.makedirs(os.path.dirname(out), exist_ok=True)

    family = {
        "$schema": "https://zed.dev/schema/themes/v0.2.0.json",
        "name": "Solarized Osaka Late 2026",
        "author": "monokkai",
        "themes": [
            {
                "name": "Solarized Osaka Late 2026",
                "appearance": "dark",
                "style": build_style(blurred=False),
            },
            {
                "name": "Solarized Osaka Late 2026 (Blurred)",
                "appearance": "dark",
                "style": build_style(blurred=True),
            },
        ],
    }

    with open(out, "w", encoding="utf-8") as f:
        json.dump(family, f, indent=2)
        f.write("\n")
    print(f"wrote {out}")
    for t in family["themes"]:
        print(f"  {t['name']}: {len(t['style'])} style keys, "
              f"{len(t['style']['syntax'])} syntax entries")


if __name__ == "__main__":
    main()
