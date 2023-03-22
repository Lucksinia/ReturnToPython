import pygame
from random import choice


class WFC:
    def __init__(self) -> None:
        pygame.init()
        self.display = pygame.display.set_mode((600, 600))
        self.clock = pygame.time.Clock()

    def run(self):
        while True:
            self.display.fill((0, 0, 0))
            for event in pygame.event.get():
                match event.type:
                    case pygame.QUIT:
                        quit()
                    case pygame.KEYDOWN:
                        if event.key == pygame.K_d:
                            hover = not hover
                        elif event.key == pygame.K_q:
                            quit()
            self.display.flip()


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
            self.options = [choice(self.options)]
            self.collapsed = True
        except:
            return
