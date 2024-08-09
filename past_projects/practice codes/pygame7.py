import pygame as pg
pg.init()

win_size = 900, 900
win = pg.display.set_mode(win_size)
win = pg.display.set_caption("Snake 2.0")

#game properties
dir = 0             #starting direction
vel = 10            #starting velocity

#snek properties


run = True
while run:
    pg.time.Clock().tick(30)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False
    keys = pg.key.get_pressed()
    if keys[pg.K_LEFT]:
        dir = 0
    if keys[pg.K_RIGHT]:
        dir = 1
    if keys[pg.K_UP]:
        dir = 2
    if keys[pg.K_DOWN]:
        dir = 3