from random import choice, randrange
import pygame as pg
import pygame.ftfont as pgftf
from string import hexdigits

HEIGHT, WIDTH = 800, 800
FONTSIZE = 24
LASTALPHA = 170


class Character:
    def __init__(self, x, y, speed) -> None:
        self.x = x
        self.y = y
        self.font = pgftf.Font("assets/impacted.ttf", FONTSIZE)
        objects = [char for char in hexdigits]
        self.text = [
            self.font.render(char, True, color=(40, randrange(130, 256), 40))
            for char in objects
        ]
        self.bottomchar = [
            self.font.render(char, True, color="#90ee90") for char in objects
        ]
        self.pick = choice(self.text)
        self.waittime = randrange(5, 25)
        self.speed = randrange(2, 6)

    def draw(self, surface, color):
        time = pg.time.get_ticks()
        if not time % self.waittime:
            self.pick = choice(self.text if color == "green" else self.bottomchar)
        self.y = self.y + self.speed if self.y < HEIGHT else -FONTSIZE
        surface.blit(self.pick, (self.x, self.y))


class CharColumn(Character):
    # TODO: un-tangle this spagetti
    def __init__(self, x, y, speed=None) -> None:
        super().__init__(x, y, speed)
        self.capasity = randrange(8, 24)
        self.chars = [
            Character(x, i, self.speed)
            for i in range(y, y - FONTSIZE * self.capasity, -FONTSIZE)
        ]

    def draw(self, surface):
        [
            character.draw(surface, "green") if i else character.draw(surface, "any")
            for i, character in enumerate(self.chars)
        ]


class App:
    def __init__(self, resolution: tuple) -> None:
        # base configs
        pg.init()
        icon = pg.image.load("assets/matrix.png")
        pg.display.set_icon(icon)
        self.screen = pg.display.set_mode(resolution)
        self.surface = pg.Surface((WIDTH, HEIGHT))
        self.surface.set_alpha(0)
        pg.display.set_caption("OOP Matrix!")
        # pg.display.set_icon()
        self.clock = pg.Clock()
        self.font = pgftf.Font("assets/impacted.ttf", FONTSIZE)
        # character setup
        self.symcol = [
            CharColumn(
                x,
                randrange(-HEIGHT, 0),
            )
            for x in range(0, WIDTH, FONTSIZE)
        ]

    def check_events(self) -> None:
        for e in pg.event.get():
            if e.type == pg.QUIT:
                pg.quit()
                quit()
            if e.type == pg.MOUSEBUTTONDOWN:
                self.surface.set_alpha(0)

    def update(self) -> None:
        if not pg.time.get_ticks() % 20 and self.surface.get_alpha() < LASTALPHA:
            self.surface.set_alpha(self.surface.get_alpha() + LASTALPHA // 10)
        self.screen.blit(self.surface, (0, 0))
        pg.display.flip()
        pg.display.set_caption(f"OOP Matrix! [{int(self.clock.get_fps())}]FPS")
        self.surface.fill((0, 0, 0))
        self.clock.tick(60)

    def draw(self) -> None:
        [column.draw(surface=self.surface) for column in self.symcol]

    def run(self) -> None:
        while True:
            self.check_events()
            self.update()
            self.draw()


if __name__ == "__main__":
    app = App((HEIGHT, WIDTH))  # resolution is derived from other scripts
    app.run()
