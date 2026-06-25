import curses

from game.game_loop import GameLoop
from game.screen import Screen


def main(stdscr):

    screen = Screen(stdscr)

    game = GameLoop()


curses.wrapper(main)