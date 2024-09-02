import sys
import os
import pygame as pg
pg.init()

sys.path.append(os.path.abspath('pgD1'))

import tools.Sprites_g2 as s

# Window properties
win_size = 900, 900
win_center = tuple(x / 2 for x in win_size)
win = pg.display.set_mode(win_size)
pg.display.set_caption("Physics v2")

# Game properties
gravity = 1

# Initialize sprites
s1 = s.Sprites_g2(list(win_center), [0, 0], [0, gravity], [0, gravity], [100, 100], (255, 255, 255))
s1.win_border = win_size
p1 = s.Sprites_g2([10, win_size[1]], [0, 0], [0, 0], [0, 0], [win_size[0], 10], (50, 50, 50))
p2 = s.Sprites_g2([500, 750], [0, 0], [0, 0], [0, 0], [200, 10], (50, 50, 50))
p3 = s.Sprites_g2([500, 600], [0, 0], [0, 0], [0, 0], [200, 10], (50, 50, 50))
p4 = s.Sprites_g2([500, 450], [0, 0], [0, 0], [0, 0], [200, 10], (50, 50, 50))
platforms = p1, p2, p3, p4
p1.win_border, p2.win_border, p3.win_border, p4.win_border = win_size, win_size, win_size, win_size
s1.platform = platforms

run = True
while run:
    pg.time.Clock().tick(30)
    current_time = pg.time.get_ticks()
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False
    keys = pg.key.get_pressed()
    s1.arrow_controls(keys)
    win.fill((0, 0, 0))
    s1.update_sprite(win, current_time)
    for x in platforms:
        x.update_sprite(win, current_time)
    pg.display.update()
pg.quit()
