from game.constants import (
    BIRD_START_X,
    BIRD_START_Y,
    GRAVITY,
    JUMP_STRENGTH
)


class Bird:

    def __init__(self):

        self.x = BIRD_START_X

        # float for smooth movement
        self.y = float(BIRD_START_Y)

        # current vertical speed
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
        
    def get_draw_y(self):

        return int(self.y)