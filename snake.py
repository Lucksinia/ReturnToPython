from pytimedinput import timedInput
from random import randint
from os import system
from colorama import Fore, init


def print_window():
    for cell in CELLS:
        if cell in snake_links:
            print(Fore.GREEN + "s", end="")
        elif cell[0] in (0, FIELD_WIDTH - 1) or cell[1] in (0, FIELD_HEIGHT - 1):
            print("#", end="")
        elif cell == apple_pos:
            print(Fore.RED + "❚", end="")

        else:
            print(" ", end="")

        if cell[0] == FIELD_WIDTH - 1:
            print("")


def update_snake():
    global eaten
    new_head = snake_links[0][0] + dir[0], snake_links[0][1] + dir[1]
    snake_links.insert(0, new_head)
    if not eaten:
        snake_links.pop(-1)
    eaten = False


def collision(snake):
    global apple_pos, eaten  #!REMOVE
    if apple_pos == snake[0]:
        apple_pos = place(snake)
        eaten = True


def place(snake) -> tuple:
    newpos = (randint(1, FIELD_WIDTH - 2), randint(1, FIELD_HEIGHT - 2))
    while newpos in snake:
        newpos = (randint(1, FIELD_WIDTH - 2), randint(1, FIELD_HEIGHT - 2))
    return newpos


# abstract shell settings
init(autoreset=True)  # just_fix... leads to wierd colorations of the all characters
FIELD_WIDTH = 32
FIELD_HEIGHT = 16
CELLS = [(col, row) for row in range(FIELD_HEIGHT) for col in range(FIELD_WIDTH)]


# snake
snake_links = [
    (5, FIELD_HEIGHT // 2),
    (4, FIELD_HEIGHT // 2),
    (3, FIELD_HEIGHT // 2),
]
DIRECTIONS = {
    "left": (-1, 0),
    "right": (1, 0),
    "up": (0, -1),
    "down": (0, 1),
}
dir = DIRECTIONS["right"]
eaten = False
# apple
apple_pos = place(snake_links)

while True:
    # gameloop
    system("cls")
    print_window()
    move, _ = timedInput("controls:", timeout=0.3)
    match move:
        case "w":
            dir = DIRECTIONS["up"]
        case "s":
            dir = DIRECTIONS["down"]
        case "a":
            dir = DIRECTIONS["left"]
        case "d":
            dir = DIRECTIONS["right"]
        case "q":
            system("cls")
            break
    update_snake()
    collision(snake_links)
    # death check
    if (
        snake_links[0][0] in (0, FIELD_WIDTH - 1)
        or snake_links[0][1] in (0, FIELD_HEIGHT - 1)
        or snake_links[0] in snake_links[1:]
    ):
        system("cls")
        break
