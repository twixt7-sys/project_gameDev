import GridSys, Player, Statbar, Animation

import pygame as g

g.init()

win_size = (900, 600)
win = g.display.set_mode(win_size)

g.display.set_caption("pgD8")

# Load and scale tiles
SCALE_FACTOR = 300
tile = g.image.load("pgD8/grass_tile.png")
tile2 = g.image.load("pgD8/wall_tile.png")
tile = g.transform.scale(tile, (SCALE_FACTOR, SCALE_FACTOR))
tile2 = g.transform.scale(tile2, (SCALE_FACTOR, SCALE_FACTOR))

grid = GridSys.GridSystem(win, win_size, (300, 300), (3, 3))
stat_bar = Statbar.StatBar()
player = Player.Player("pgD8/player.png", pos=[100,100], scale_factor=3, statbar=stat_bar, frame_rate=100, screen=win)

g.display.update()

running = True
while running:
    for event in g.event.get():
        if event.type == g.QUIT:
            running = False

    # Update
    player.update()

    grid.draw(tile2, tile)
    stat_bar.draw(win)
    player.draw()

    g.display.update()

