import time
import curses

from game.constants import FPS
from game.renderer import Renderer
from game.borders import Borders
from game.bird import Bird


def main(stdscr):

    renderer = Renderer(stdscr)

    borders = Borders()

    # Bird starts in the vertical center of the terminal
    bird = Bird(renderer.height)
    stdscr.nodelay(True)
    stdscr.timeout(0)

    running = True

    while running:

        key = stdscr.getch()

        if key == ord(' '):
            bird.jump()

        bird.apply_gravity()

        if bird.y < 1:

            bird.y = 1

            bird.velocity = 0

        renderer.clear()

        borders.draw(renderer)

        renderer.draw_sprite(
            bird.x,
            int(bird.y),
            bird.sprite
        )

        renderer.refresh()

        if bird.y >= renderer.height - len(bird.sprite) - 1:

            bird.y = renderer.height - len(bird.sprite) - 1

            bird.velocity = 0

        time.sleep(1 / FPS)


if __name__ == "__main__":
    curses.wrapper(main)