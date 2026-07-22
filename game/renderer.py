"""
renderer.py

Responsible for drawing everything on the terminal.
"""

import curses


class Renderer:

    def __init__(self, screen):
        self.screen = screen

        # Get terminal size
        self.height, self.width = self.screen.getmaxyx()

        # Prevent drawing on the last row/column
        self.height -= 1
        self.width -= 1

    def clear(self):
        self.screen.clear()

    def refresh(self):
        self.screen.refresh()

    def draw_text(self, x, y, text):
        try:
            self.screen.addstr(y, x, text)
        except curses.error:
            # Ignore attempts to draw outside the screen
            pass

    def draw_sprite(self, x, y, sprite):
        for row, line in enumerate(sprite):
            self.draw_text(x, y + row, line)