from dataclasses import dataclass
from random import randint

import pygame


WIDTH, HEIGHT = 800, 600
FPS = 60

STAR_COUNT = 100
STAR_RADIUS = 15

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.Clock()


@dataclass
class Star:
    pos: pygame.Vector2
    dist_to_floating_y: int
    radius: int
    fall_speed: int


starfield = [
    Star(
        pos=pygame.Vector2(
            randint(0, WIDTH), y_pos := randint(0, HEIGHT) - HEIGHT - STAR_RADIUS
        ),
        dist_to_floating_y=y_pos,
        radius=15,
        fall_speed=30,
    )
    for _ in range(STAR_COUNT)
]
floating_y = 0

while True:
    dt = clock.tick(FPS) / 1000

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            raise SystemExit

    mouse_x, mouse_y = pygame.mouse.get_pos()

    floating_y += starfield[0].fall_speed * dt / 2
    for star in starfield:
        star.pos.y = floating_y - star.dist_to_floating_y
        if star.pos.y - starfield[0].radius > HEIGHT:
            star.pos.y = -starfield[0].radius
            star.pos.x = randint(0, WIDTH)
            star.dist_to_floating_y += HEIGHT + starfield[0].radius * 2
    floating_y += starfield[0].fall_speed * dt / 2

    screen.fill("black")

    for star in starfield:
        pygame.draw.circle(screen, "white", round(star.pos), STAR_RADIUS)

    pygame.display.flip()
