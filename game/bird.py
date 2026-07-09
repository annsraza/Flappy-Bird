"""
bird.py

Represents the player-controlled bird.
"""

from game.constants import (
    BIRD_START_X,
    BIRD_START_Y,
)


class Bird:

    def __init__(self):

        self.x = BIRD_START_X

        # Stored as float for smooth movement later
        self.y = float(BIRD_START_Y)

        # Vertical speed
        self.velocity = 0.0

        self.sprite = [
            "  (@>",
            " {||",
            '--""--'
        ]