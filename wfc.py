import pygame as pg
from random import choice
from copy import copy


def load_images(path, _rez, padding=0):
    img = pg.image.load(path).convert_alpha()
    img = pg.transform.scale(img, (_rez - padding, _rez - padding))


class WFC:
    def __init__(self):
        pg.init()
        self.options = []
        self.screen = pg.display.set_mode((600, 600))
        self.clock = pg.time.Clock()
        self.rez = 30
        for i in range(5):
            img = load_images(f"./assets/{i}.png", self.rez)
            self.options.append(Tile(img))

    def update(self):
        pg.display.flip()
        self.clock.tick()
        pg.display.set_caption(f"{self.clock.get_fps():.1f}")

    def draw(self):
        self.screen.fill((0, 0, 0))

    def check_event(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                quit()
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_d:
                    hover_toggle = not hover_toggle
                elif event.key == pg.K_q:
                    pg.quit()

    def run(self):
        while True:
            self.check_event()
            self.update()
            self.draw()


class Cell:
    def __init__(self, x, y, size, options) -> None:
        self.x = x
        self.y = y
        self.size = size
        self.options = options
        self.collapsed = False

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


class Tile:
    def __init__(self, img) -> None:
        self.image = img
        self.index = -1
        self.edges = []
        self.up = []
        self.down = []
        self.right = []
        self.left = []

    def rules(self, tiles):
        for tile in tiles:
            if self.edges[0] == tile.edges[2]:
                self.up.append(tile)
            elif self.edges[1] == tile.edges[3]:
                self.right.append(tile)
            elif self.edges[2] == tile.edges[0]:
                self.down.append[tile]
            elif self.edges[3] == tile.edges[1]:
                self.left.append(tile)

    def draw(self, screen, x, y):
        screen.blit(self.image, (x, y))


class Grid:
    def __init__(self, width, height, size, options) -> None:
        self.width = width
        self.height = height
        self.size = size
        self.w = self.width // self.size
        self.h = self.height // self.size
        self.grid = []
        self.options = options

    def draw(self, screen):
        for row in self.grid:
            for cell in row:
                cell.draw(screen)

    def startup(self):
        for i in range(self.w):
            self.grid.append([])
            for j in range(self.h):
                cell = Cell(i, j, self.size, self.options)
                self.grid[i].append(cell)

    def minimal_entropy_pick(self):
        grid_copy = [i for row in self.grid for i in row]
        grid_copy.sort(key=lambda x: x.entropy())
        filtered_grid = list(filter(lambda x: x.entropy() > 1, grid_copy))
        if filtered_grid == []:
            return None
        least_entropy = filtered_grid[0]
        filtered_grid = list(
            filter(lambda x: x.entropy() == least_entropy.entropy(), filtered_grid)
        )

        # if nothing helps
        pick = choice(filtered_grid)
        return pick

    def wave_function_collapse(self):
        picked = self.minimal_entropy_pick()
        if picked:
            self.grid[picked.x, picked.y].options
            self.grid[picked.x, picked.y].observe()
        else:
            return
        next_grid = copy(self.grid)
        for i in range(len(self.grid)):
            for j in range(len(self.grid[0])):
                if self.grid[i][j].collapsed:
                    next_grid[i][j] = self.grid[i][j]
                else:
                    cumvalopt = self.options
                    cell_above = self.grid[(i - 1) % self.w][j]
                    valid_options = []
                    for option in cell_above.options:
                        valid_options.extend(option.down)
                    cumvalopt = [
                        option for option in cumvalopt if option in valid_options
                    ]
                    cell_right = self.grid[i][(j + 1) % self.h]
                    valid_options = []
                    for option in cell_right.options:
                        valid_options.extend(option.left)
                    cumvalopt = [
                        option for option in cumvalopt if option in valid_options
                    ]

                    cell_down = self.grid[(i + 1) % self.w][j]
                    valid_options = []
                    for option in cell_down.options:
                        valid_options.extend(option.up)
                    cumvalopt = [
                        option for option in cumvalopt if option in valid_options
                    ]

                    cell_left = self.grid[i][(j - 1) % self.h]
                    valid_options = []
                    for option in cell_left.options:
                        valid_options.extend(option.right)
                    cumvalopt = [
                        option for option in cumvalopt if option in valid_options
                    ]

                    # finally assign the cumvalopt options to be the current cells valid options
                    next_grid[i][j].options = cumvalopt
                    next_grid[i][j].update()
            self.grid = copy(next_grid)


if __name__ == "__main__":
    app = WFC()
    app.run()
