import pygame as pg

def init():
    pg.init()
    pg.display.set_caption("pgD10")

# Constant variables
WIN_SIZE = (900, 600)
WIN = pg.display.set_mode(WIN_SIZE)
SCALE_FACTOR = 300
CLOCK = pg.time.Clock()
TILE_SIZE = (SCALE_FACTOR, SCALE_FACTOR)
GRID_SIZE = (3, 3)
running = True

FPS = 60

TILES_PATH = "pgD10/assets/tiles/"
PLAYER_PATH = "pgD10/assets/player.png"

tiles = {
    "grass": pg.image.load(TILES_PATH, "grass_tile.png"),
    "wall": pg.image.load(TILES_PATH, "wall_tile.png"),
    #"water": pg.image.load(TILES_PATH, "water_tile.png")
}

player = pg.image.load(PLAYER_PATH, "player.png")
player = pg.transform.scale(player, TILE_SIZE)