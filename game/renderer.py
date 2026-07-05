"""
renderer.py

Purpose:
    Draw text and sprites on the terminal.

This file NEVER knows about:
    - Bird
    - Pipes
    - Score

It only knows HOW to draw.
"""

from game.terminal import run


class Renderer:

    def __init__(self, screen):
        self.screen = screen