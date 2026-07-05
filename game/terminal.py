"""
terminal.py

Responsible for:
- Starting curses
- Stopping curses
- Running demos safely
"""

import curses


def run(callback):
    """
    Runs a function inside a curses session.

    Parameters
    ----------
    callback : function
        Function that receives stdscr.
    """

    curses.wrapper(callback)