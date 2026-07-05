"""
borders.py

Draws the border around the game area.
"""

from game.constants import SCREEN_WIDTH, SCREEN_HEIGHT


class Borders:

    def __init__(self):

        self.width = SCREEN_WIDTH
        self.height = SCREEN_HEIGHT

    def draw(self, renderer):

        # Top
        renderer.draw_text(
            0,
            0,
            "+" + "-" * (self.width - 2) + "+"
        )

        # Bottom
        renderer.draw_text(
            0,
            self.height - 1,
            "+" + "-" * (self.width - 2) + "+"
        )

        # Left and Right
        for y in range(1, self.height - 1):

            renderer.draw_text(0, y, "|")

            renderer.draw_text(self.width - 1, y, "|")