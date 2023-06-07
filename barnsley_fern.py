"""
Barnsley Fern Implementation

Based on The Coding Train / Daniel Shiffman implementation in p5.js:
https://youtu.be/JFugGF1URNo

"""

import pygame as pg
from random import random
from functools import cache


class App:
    def __init__(self, resolution: tuple) -> None:
        # base configs
        pg.init()
        self.screen = pg.display.set_mode(resolution)
        self.clock = pg.Clock()

        # position
        self.x = 0
        self.y = 0

    def calculate_points(self):
        choiser = random()
        if choiser < 0.01:
            self.x = 0.00
            self.y = 0.16 * self.y
        elif choiser < 0.86:
            self.x = 0.85 * self.x + 0.04 * self.y
            self.y = -0.04 * self.x + 0.85 * self.y + 1.60
        elif choiser < 0.93:
            self.x = 0.20 * self.x - 0.26 * self.y
            self.y = 0.23 * self.x + 0.22 * self.y + 1.60
        else:
            self.x = -0.15 * self.x + 0.28 * self.y
            self.y = 0.26 * self.x + 0.24 * self.y + 0.44

    def check_events(self) -> None:
        for e in pg.event.get():
            if e.type == pg.QUIT:
                pg.quit()
                quit()

    def update(self) -> None:
        pg.display.flip()
        pg.display.set_caption(f"Barnsley Fern")

    def draw(self) -> None:
        # numbers are arbitrary, but derived from
        x = self.x * 60
        y = self.y * 37 - 272
        pg.draw.circle(self.screen, "white", (x + 300, y + 300), 1)

    def run(self) -> None:
        while True:
            self.check_events()
            self.update()
            self.draw()
            self.calculate_points()


if __name__ == "__main__":
    app = App((600, 600))  # resolution  brougtht from Wiki examples
    app.run()
