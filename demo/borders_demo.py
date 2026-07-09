import curses

from game.renderer import Renderer
from game.borders import Borders


def main(stdscr):

    renderer = Renderer(stdscr)

    borders = Borders()

    renderer.clear()

    borders.draw(renderer)

    renderer.refresh()

    stdscr.getch()


if __name__ == "__main__":
    curses.wrapper(main)