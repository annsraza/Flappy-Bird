"""
bird.py

Represents the player-controlled bird.
"""

from game.constants import (
    BIRD_START_X,
    GRAVITY,
    JUMP_STRENGTH,
)


class Bird:

    def __init__(self, renderer):

        self.x = BIRD_START_X

        self.y = renderer.height / 2

        self.velocity = 0.0

        self.sprite = [
            "  (@>",
            " {||",
            '--""--'
        ]
    def apply_gravity(self):
        self.velocity += GRAVITY
        self.y += self.velocity
    def jump(self):
        self.velocity = JUMP_STRENGTH