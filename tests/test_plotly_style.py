import unittest

import plotly.graph_objects as go

from figures.plotly_style import (
    DRAW_MODEBAR_BUTTONS,
    FONT_SIZE,
    PLOTLY_CONFIG,
    TABLEAU_COLORS,
    apply_standard_style,
)


class PlotlyStyleTest(unittest.TestCase):
    def test_applies_font_tableau_cycle_and_boxed_axes(self):
        fig = apply_standard_style(go.Figure())

        self.assertEqual(fig.layout.font.size, FONT_SIZE)
        self.assertEqual(fig.layout.title.font.size, FONT_SIZE)
        self.assertEqual(tuple(fig.layout.colorway), TABLEAU_COLORS)
        for axis in (fig.layout.xaxis, fig.layout.yaxis):
            self.assertTrue(axis.showline)
            self.assertTrue(axis.mirror)
            self.assertEqual(axis.linecolor, "black")
            self.assertEqual(axis.tickfont.size, FONT_SIZE)
            self.assertEqual(axis.title.font.size, FONT_SIZE)

    def test_adds_all_shape_drawing_buttons(self):
        self.assertEqual(
            tuple(PLOTLY_CONFIG["modeBarButtonsToAdd"]),
            DRAW_MODEBAR_BUTTONS,
        )


if __name__ == "__main__":
    unittest.main()
