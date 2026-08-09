\
from __future__ import annotations

from pathlib import Path
import math

import pandas as pd
import plotly.graph_objects as go

if __package__:
    from .plotly_style import write_figure_html
else:
    from plotly_style import write_figure_html


FIGURE_TITLE = "Figure 1. Mobility vs dopant concentration"


def _num(series: pd.Series) -> pd.Series:
    return pd.to_numeric(series, errors="coerce")


def generate_figure(workbook_path: Path, out_html: Path) -> Path:
    df = pd.read_excel(workbook_path, sheet_name="Reported Data")

    required = ["Dopant (at.%)", "Mobility (cm^2/Vs)"]
    for col in required:
        if col not in df.columns:
            raise KeyError(f"Missing required column: {col}")

    work = df.copy()
    work["Dopant (at.%)"] = _num(work["Dopant (at.%)"])
    work["Mobility (cm^2/Vs)"] = _num(work["Mobility (cm^2/Vs)"])
    work["Resistivity (ohm·cm)"] = _num(work.get("Resistivity (ohm·cm)"))
    work = work.dropna(subset=["Dopant (at.%)", "Mobility (cm^2/Vs)"])

    out_html.parent.mkdir(parents=True, exist_ok=True)

    if work.empty:
        fig = go.Figure()
        fig.add_annotation(
            text="No rows currently contain both dopant concentration and mobility.",
            xref="paper",
            yref="paper",
            x=0.5,
            y=0.5,
            showarrow=False,
            font=dict(size=16),
        )
        fig.update_layout(
            template="plotly_white",
            title=FIGURE_TITLE,
            xaxis_title="Dopant concentration (at.%)",
            yaxis_title="Mobility (cm²/Vs)",
            height=600,
        )
        return write_figure_html(fig, out_html)

    work = work.sort_values("Dopant (at.%)")

    # Color by resistivity (log scale) when available.
    color_vals = []
    for v in work["Resistivity (ohm·cm)"].tolist():
        if pd.notna(v) and v > 0:
            color_vals.append(math.log10(float(v)))
        else:
            color_vals.append(None)

    hover = []
    for _, row in work.iterrows():
        hover.append(
            {
                "paper": row.get("Paper ID", ""),
                "sample": row.get("Sample / condition", ""),
                "technique": row.get("Fabrication technique", ""),
                "resistivity": row.get("Resistivity (ohm·cm)", ""),
                "sheet": row.get("Sheet resistance (ohm/sq)", ""),
                "confidence": row.get("Confidence", ""),
            }
        )

    fig = go.Figure()
    trace_kwargs = dict(
        x=work["Dopant (at.%)"],
        y=work["Mobility (cm^2/Vs)"],
        mode="markers",
        marker=dict(
            size=12,
            line=dict(width=1, color="black"),
        ),
        customdata=hover,
        hovertemplate=(
            "Paper: %{customdata.paper}<br>"
            "Sample: %{customdata.sample}<br>"
            "Technique: %{customdata.technique}<br>"
            "Dopant: %{x:.2f} at.%<br>"
            "Mobility: %{y:.2f} cm²/Vs<br>"
            "Resistivity: %{customdata.resistivity}<br>"
            "Sheet resistance: %{customdata.sheet}<br>"
            "Confidence: %{customdata.confidence}<extra></extra>"
        ),
        name="Reported data",
    )

    if any(v is not None for v in color_vals):
        trace_kwargs["marker"]["color"] = color_vals
        trace_kwargs["marker"]["colorscale"] = "Viridis"
        trace_kwargs["marker"]["showscale"] = True
        trace_kwargs["marker"]["colorbar"] = dict(title="log10 resistivity\n(Ω·cm)")
    fig.add_trace(go.Scatter(**trace_kwargs))

    if len(work) > 1:
        fig.add_trace(
            go.Scatter(
                x=work["Dopant (at.%)"],
                y=work["Mobility (cm^2/Vs)"],
                mode="lines",
                line=dict(width=1),
                hoverinfo="skip",
                showlegend=False,
            )
        )

    fig.update_layout(
        template="plotly_white",
        title=FIGURE_TITLE,
        xaxis_title="Dopant concentration (at.%)",
        yaxis_title="Mobility (cm²/Vs)",
        height=650,
        margin=dict(l=60, r=40, t=70, b=60),
    )

    return write_figure_html(fig, out_html)


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Generate Figure 1.")
    parser.add_argument("workbook", type=Path)
    parser.add_argument("out_html", type=Path)
    args = parser.parse_args()
    path = generate_figure(args.workbook, args.out_html)
    print(path)
