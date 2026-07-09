import curses

from game.renderer import Renderer
from game.borders import Borders
from game.bird import Bird


def main(stdscr):

    renderer = Renderer(stdscr)

    borders = Borders()

    bird = Bird()

    renderer.clear()

    borders.draw(renderer)

    renderer.draw_sprite(
        bird.x,
        int(bird.y),
        bird.sprite
    )

    renderer.refresh()

    stdscr.getch()


if __name__ == "__main__":
    curses.wrapper(main)