import pygame as pg

class GridSystem:
    def __init__(self, win, win_size, cell_size=(100, 100), grid_size=(10, 5)):
        self.win = win
        self.win_size = win_size
        self.cell_size = cell_size
        self.grid_size = grid_size
        self.tile_map = [[0 for _ in range(grid_size[0])] for _ in range(grid_size[1])]

    def draw(self, tile1, tile2):  # Use two different tile images for variety
        for i in range(self.grid_size[0]):
            for j in range(self.grid_size[1]):
                x, y = i * self.cell_size[0], j * self.cell_size[1]
                if self.tile_map[j][i] == 1:
                    self.win.blit(tile1, (x, y))  # Place tile1 for value 1
                else:
                    self.win.blit(tile2, (x, y))  # Place tile2 for value 0

    def set_tile_map(self, tile_map):
        self.tile_map = tile_map
