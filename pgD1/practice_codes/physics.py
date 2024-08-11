import sys
import os

sys.path.append(os.path.abspath('pgD1'))

import tools

import pygame as pg
import tools.sprites as s
import tools.Matrices as m
pg.init()

win_size = 900, 900
win = pg.display.set_mode(win_size)
pg.display.set_caption("Physics")

win_center = tuple(x / 2 for x in win_size)

s1 = s.Sprite(win_center, (50, 50), 100, (255, 255, 255), 1, s.Sprite.RECT)

run = True
while run:
    pg.time.Clock().tick(30)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False
    win.fill((0, 0, 0))
    s1.draw_sprite(win)
    pg.display.update()
pg.quit()