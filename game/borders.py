"""
borders.py

Draws the border around the game area.
"""

class Borders:

    def draw(self, renderer):

        width = renderer.width
        height = renderer.height

        renderer.draw_text(
            0,
            0,
            "+" + "-" * (width - 2) + "+"
        )

        renderer.draw_text(
            0,
            height - 1,
            "+" + "-" * (width - 2) + "+"
        )

        for y in range(1, height - 1):
            renderer.draw_text(0, y, "|")
            renderer.draw_text(width - 1, y, "|")