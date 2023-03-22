import pygame


class WFC:
    def __init__(self) -> None:
        pygame.init()
        self.display = pygame.display.set_mode((600, 600))
        self.clock = pygame.time.Clock()

    def run(self):
        self.display.fill((0, 0, 0))


class Cell:
    def __init__(self, x, y, size, options) -> None:
        self.x = x
        self.y = y
        self.size = size
        self.options = options

    def draw(self, window):
        if len(self.options) == 1:
            return self.options[0].draw(window, self.y * self.size, self.x * self.size)

    def entropy(self):
        return len(self.options)

    def update(self):
        self.collapsed = bool(self.entropy() == True)

    def observe(self):
        try:
            self.options = [random.choise(self.options)]
            self.collapsed = True
        except:
            return
