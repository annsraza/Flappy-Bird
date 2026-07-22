"""
bird.py

Represents the player-controlled bird.
"""

from game.constants import (
    BIRD_START_X,
    GRAVITY,
    JUMP_STRENGTH,
    MAX_FALL_SPEED
)


class Bird:

    def __init__(self, screen_height):

        self.x = BIRD_START_X

        self.y = float(screen_height / 2)

        self.velocity = 0.0

        self.sprite = [
            "  (@>",
            " {||",
            '--""--'
        ]

    def apply_gravity(self):

        self.velocity += GRAVITY

        if self.velocity > MAX_FALL_SPEED:
            self.velocity = MAX_FALL_SPEED

        self.y += self.velocity

    def jump(self):

        self.velocity = JUMP_STRENGTH