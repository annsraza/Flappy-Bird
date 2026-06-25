from game.bird import Bird


class GameLoop:

    def __init__(self):

        self.bird = Bird()

        self.running = True
    def draw(self, screen):

        screen.draw_border()

        screen.draw_bird(self.bird)