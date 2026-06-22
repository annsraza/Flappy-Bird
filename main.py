import keyboard
import os
import time
import os
import time

# ======================
# SETTINGS
# ======================

WIDTH = 60
HEIGHT = 20

bird_x = 10
bird_y = 8

pipe_x = 45
gap_start = 6
gap_size = 5

gravity_speed = 1

# ======================
# BIRD
# ======================

bird = [
    "  (@>",
    " {||",
    '--""--'
]

# ======================
# FUNCTIONS
# ======================

def create_screen():
    return [[" " for _ in range(WIDTH)] for _ in range(HEIGHT)]


def draw_border(screen):

    for r in range(HEIGHT):
        screen[r][0] = "|"
        screen[r][WIDTH - 1] = "|"

    for c in range(WIDTH):
        screen[HEIGHT - 1][c] = "-"


def draw_bird(screen, x, y):

    for row in range(len(bird)):
        for col in range(len(bird[row])):

            if (
                0 <= y + row < HEIGHT
                and 0 <= x + col < WIDTH
            ):
                screen[y + row][x + col] = bird[row][col]


def draw_pipe(screen, x, gap_start, gap_size):

    pipe_width = 14

    for row in range(HEIGHT - 1):

        # skip gap area
        if gap_start <= row < gap_start + gap_size:
            continue

        # cap
        if row == gap_start - 1:
            for w in range(pipe_width):
                if 0 <= x + w < WIDTH:
                    screen[row][x + w] = "▓"

        # lower cap
        elif row == gap_start + gap_size:
            for w in range(pipe_width):
                if 0 <= x + w < WIDTH:
                    screen[row][x + w] = "▓"

        # body
        else:

            if 0 <= x < WIDTH:
                screen[row][x] = "█"

            for w in range(1, pipe_width - 1):
                if 0 <= x + w < WIDTH:
                    screen[row][x + w] = "░"

            if 0 <= x + pipe_width - 1 < WIDTH:
                screen[row][x + pipe_width - 1] = "█"


def print_screen(screen):

    for row in screen:
        print("".join(row))


# ======================
# GAME LOOP
# ======================

while True:

    screen = create_screen()

    draw_border(screen)

    draw_bird(screen, bird_x, int(bird_y))

    draw_pipe(
        screen,
        pipe_x,
        gap_start,
        gap_size
    )

    os.system("cls")

    print_screen(screen)

    # gravity
    bird_y += gravity_speed

    # move pipe
    pipe_x -= 1

    time.sleep(0.15)