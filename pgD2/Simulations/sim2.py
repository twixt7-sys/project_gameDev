#Procedural animation via matrix field
#implementation of Sprite class (1st gen)

import sys
import os
sys.path.append(os.path.abspath('pgD2'))

import pygame as pg
import Tools.Game as g
import Tools.Dictionary as d
import Objects.Sprite_g1 as s1

#game object and settings
g1 = g.Game(pg)
g1.set_window()

#game environment settings
g1.set_environment()
g1.bounce = 0.99
g1.gravity = 0.5

#for less coding space
loop, dic = g1.Loop(g1), d.Dictionary()

#in-game objects

sprites = [None] * 100
for x in range(len(sprites)):
    sprites[x] = s1.Sprite_g1(g1, g1.win_center, (10, 10), 0.1 + (x / 1000), [0, 0], [0, 0], 0, dic.color[dic.DARK_GREY])

#game loop
while g1.run:
    loop.set_loop()
    loop.set_events()
    loop.set_background(dic.color[dic.LIGHT_GREY])
    #insert methods here
    for i in range(len(sprites)):
        sprites[i].Actions(sprites[i]).move((pg.K_UP, pg.K_DOWN, pg.K_LEFT, pg.K_RIGHT))
        sprites[i].update_sprite()
    loop.update_display()
pg.quit()