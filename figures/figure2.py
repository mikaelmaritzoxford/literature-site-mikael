\
from __future__ import annotations

from pathlib import Path

import pandas as pd
import plotly.graph_objects as go

if __package__:
    from .plotly_style import write_figure_html
else:
    from plotly_style import write_figure_html


FIGURE_TITLE = "Figure 2. Temperature vs fabrication method"


def _num(series: pd.Series) -> pd.Series:
    return pd.to_numeric(series, errors="coerce")


def generate_figure(workbook_path: Path, out_html: Path) -> Path:
    df = pd.read_excel(workbook_path, sheet_name="Reported Data")

    required = ["Fabrication technique", "Deposition temp (C)", "Post-deposition temp (C)"]
    for col in required:
        if col not in df.columns:
            raise KeyError(f"Missing required column: {col}")

    work = df.copy()
    work["Deposition temp (C)"] = _num(work["Deposition temp (C)"])
    work["Post-deposition temp (C)"] = _num(work["Post-deposition temp (C)"])

    records = []
    for _, row in work.iterrows():
        technique = row.get("Fabrication technique", "")
        paper = row.get("Paper ID", "")
        sample = row.get("Sample / condition", "")
        atmosphere = row.get("Atmosphere", "")
        gas_mix = row.get("Gas mix", "")
        dep = row.get("Deposition temp (C)")
        post = row.get("Post-deposition temp (C)")
        if pd.notna(dep):
            records.append(
                {
                    "fabrication": technique,
                    "temperature": float(dep),
                    "stage": "Deposition",
                    "paper": paper,
                    "sample": sample,
                    "atmosphere": atmosphere,
                    "gas_mix": gas_mix,
                }
            )
        if pd.notna(post):
            records.append(
                {
                    "fabrication": technique,
                    "temperature": float(post),
                    "stage": "Post-deposition",
                    "paper": paper,
                    "sample": sample,
                    "atmosphere": atmosphere,
                    "gas_mix": gas_mix,
                }
            )

    out_html.parent.mkdir(parents=True, exist_ok=True)

    if not records:
        fig = go.Figure()
        fig.add_annotation(
            text="No deposition or post-deposition temperatures were found.",
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
            xaxis_title="Fabrication technique",
            yaxis_title="Temperature (°C)",
            height=600,
        )
        return write_figure_html(fig, out_html)

    points = pd.DataFrame.from_records(records)
    stage_order = ["Deposition", "Post-deposition"]
    symbol_map = {"Deposition": "circle", "Post-deposition": "diamond"}

    fig = go.Figure()
    for stage in stage_order:
        subset = points[points["stage"] == stage]
        if subset.empty:
            continue
        fig.add_trace(
            go.Scatter(
                x=subset["fabrication"],
                y=subset["temperature"],
                mode="markers",
                name=stage,
                marker=dict(size=12, symbol=symbol_map.get(stage, "circle"), line=dict(width=1, color="black")),
                customdata=subset[["paper", "sample", "atmosphere", "gas_mix"]].values,
                hovertemplate=(
                    "Fabrication: %{x}<br>"
                    "Temperature: %{y:.0f} °C<br>"
                    "Paper: %{customdata[0]}<br>"
                    "Sample: %{customdata[1]}<br>"
                    "Atmosphere: %{customdata[2]}<br>"
                    "Gas mix: %{customdata[3]}<extra></extra>"
                ),
            )
        )

    fig.update_layout(
        template="plotly_white",
        title=FIGURE_TITLE,
        xaxis_title="Fabrication technique",
        yaxis_title="Temperature (°C)",
        height=650,
        margin=dict(l=60, r=40, t=70, b=60),
        legend_title_text="Processing stage",
    )

    return write_figure_html(fig, out_html)


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Generate Figure 2.")
    parser.add_argument("workbook", type=Path)
    parser.add_argument("out_html", type=Path)
    args = parser.parse_args()
    path = generate_figure(args.workbook, args.out_html)
    print(path)
