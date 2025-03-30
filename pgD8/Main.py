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
player = Player.Player([100,100], stat_bar, win)

g.display.update()

running = True
while running:
    for event in g.event.get():
        if event.type == g.QUIT:
            running = False

    grid.draw(tile2, tile)
    stat_bar.update(win, player.stats, (0, 0), player.stat_colors)
    player.update()

    g.display.update()

