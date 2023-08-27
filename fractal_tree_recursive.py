"""
Recursive fractal tree implementation
"""

import pygame as pg
from math import pi, sin, cos


class App:
    def __init__(self, resolution: tuple) -> None:
        # base configs
        pg.init()
        self.height, self.width = resolution
        self.screen = pg.display.set_mode(resolution)
        self.clock = pg.Clock()
        # Getting input reading
        self.x, self.y = pg.mouse.get_pos()
        # variables
        self.theta = pi / 6
        self.factor = 0.67

    def check_events(self) -> None:
        for e in pg.event.get():
            if e.type == pg.QUIT:
                pg.quit()
                quit()

    def update(self) -> None:
        pg.display.flip()
        pg.display.set_caption(f"Recursive Tree")

    def recursive_branch(self, x, y, length, angle):
        if length <= 1:
            return
        x2 = x - length * cos(angle)
        y2 = y - length * sin(angle)
        pg.draw.line(self.screen, "antiquewhite", (x, y), (x2, y2))
        self.clock.tick()
        self.recursive_branch(x2, y2, length * self.factor, angle + self.theta)
        self.recursive_branch(x2, y2, length * self.factor, angle - self.theta)

    def draw(self) -> None:
        # centering the treee, because of pygame-ce coordinates grid
        self.recursive_branch(x=self.width / 2, y=self.height, length=160, angle=pi / 2)

    def run(self) -> None:
        while True:
            # self.clock.tick()
            self.check_events()
            self.update()
            self.draw()


if __name__ == "__main__":
    app = App((600, 600))  # resolution  brougtht from Wiki examples of Barnsley fern.
    app.run()
