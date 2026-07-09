class Renderer:

    

    def __init__(self, screen):
        self.screen = screen

        self.height, self.width = self.screen.getmaxyx()
    def clear(self):
        self.screen.clear()

    def refresh(self):
        self.screen.refresh()

    def draw_text(self, x, y, text):
        self.screen.addstr(y, x, text)

    def draw_sprite(self, x, y, sprite):
        for row, line in enumerate(sprite):
            self.draw_text(x, y + row, line)