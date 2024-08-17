#Procedural animation via matrix field
#implementation of Sprite class (1st gen)

import sys
import os
sys.path.append(os.path.abspath('pgD2'))

import pygame as pg
import Tools.Game as g
import Tools.Dictionary as d
import Objects.Sprite_g1 as s1

#game object
g1 = g.Game(pg)
g1.set_window()

#for less coding space
loop, dic = g1.Loop(), d.Dictionary()

#in-game objects



#game loop
while g1.run:
    loop.set_loop()
    loop.set_events()
    loop.set_background(dic.color[dic.DARK_GREY])
    #insert methods here
    loop.update_display()
pg.quit()