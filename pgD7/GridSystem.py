import pygame as pg

pg.init()

win_size = (900, 600)
win = pg.display.set_mode(win_size)

SCALED_TILE_SIZE = 350

# Load and scale tiles
grass_tile = pg.image.load("pgD7/grass_tile.png")
wall_tile = pg.image.load("pgD7/wall_tile.png")
grass_tile = pg.transform.scale(grass_tile, (SCALED_TILE_SIZE, SCALED_TILE_SIZE))
wall_tile = pg.transform.scale(wall_tile, (SCALED_TILE_SIZE, SCALED_TILE_SIZE))

class GridSystem:
    def __init__(self, win, win_size, cell_size=(100, 100), grid_size=(5, 5)):
        self.win, win_size = win, win_size
        self.cell_size = cell_size
        self.grid_size = grid_size
        self.tile_map = [[0 for i in range(grid_size[0])] for j in range(grid_size[1])]

    def draw(self):
        for i in range(self.grid_size[0]):
            for j in range(self.grid_size[1]):
                # draw the tile image at (i, j)
                x, y = i * self.cell_size, j * self.cell_size
                if self.tile_map[j][i] == 1:
                    self.win.blit(wall_tile, (x, y))
                else:
                    self.win.blit(grass_tile, (x, y))

    def set_tile_map(self, tile_map):
        self.tile_map = tile_map

def __main__():
    grid = GridSystem(win, win_size, SCALED_TILE_SIZE, (5, 5))
    grid.draw()
    pg.display.flip()
    pg.time.wait(10000)
    pg.quit()

if __name__ == "__main__":
    __main__()