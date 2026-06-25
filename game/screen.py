import curses


class Screen:

    def __init__(self, stdscr):

        self.stdscr = stdscr

    def clear(self):

        self.stdscr.clear()

    def refresh(self):

        self.stdscr.refresh()

    def draw_border(self):

        height, width = self.stdscr.getmaxyx()

        for x in range(width):
            self.stdscr.addch(height - 1, x, "-")

    def draw_bird(self, bird):

        y = bird.get_draw_y()

        for row, line in enumerate(bird.sprite):

            self.stdscr.addstr(
                y + row,
                bird.x,
                line
            )