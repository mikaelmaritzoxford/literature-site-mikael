from __future__ import annotations

from pathlib import Path

import plotly.graph_objects as go


FONT_SIZE = 14

# Matplotlib's Tableau 10 categorical colour cycle (tableau-colorblind10 is a
# separate palette). Keep this order stable so categories remain comparable.
TABLEAU_COLORS = (
    "#1f77b4",
    "#ff7f0e",
    "#2ca02c",
    "#d62728",
    "#9467bd",
    "#8c564b",
    "#e377c2",
    "#7f7f7f",
    "#bcbd22",
    "#17becf",
)

DRAW_MODEBAR_BUTTONS = (
    "drawline",
    "drawopenpath",
    "drawclosedpath",
    "drawcircle",
    "drawrect",
    "eraseshape",
)

PLOTLY_CONFIG = {
    "modeBarButtonsToAdd": list(DRAW_MODEBAR_BUTTONS),
}


def apply_standard_style(fig: go.Figure) -> go.Figure:
    """Apply the project's standard scientific Plotly presentation."""
    fig.update_layout(
        template="plotly_white",
        font=dict(size=FONT_SIZE),
        title_font=dict(size=FONT_SIZE),
        colorway=list(TABLEAU_COLORS),
        legend=dict(
            font=dict(size=FONT_SIZE),
            title_font=dict(size=FONT_SIZE),
        ),
        newshape=dict(line=dict(color=TABLEAU_COLORS[0])),
    )
    axis_style = dict(
        showline=True,
        mirror=True,
        linewidth=1,
        linecolor="black",
        ticks="outside",
        tickfont=dict(size=FONT_SIZE),
        title_font=dict(size=FONT_SIZE),
    )
    fig.update_xaxes(**axis_style)
    fig.update_yaxes(**axis_style)
    fig.update_annotations(font_size=FONT_SIZE)
    return fig


def write_figure_html(fig: go.Figure, out_html: Path | str) -> Path:
    """Apply the standard style and export a complete interactive HTML file."""
    output_path = Path(out_html)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    apply_standard_style(fig)
    fig.write_html(
        str(output_path),
        include_plotlyjs="cdn",
        full_html=True,
        config=PLOTLY_CONFIG,
    )
    return output_path
