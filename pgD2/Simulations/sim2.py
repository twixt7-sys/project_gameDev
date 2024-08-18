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

#for less coding space
loop, dic = g1.Loop(g1), d.Dictionary()

#in-game objects
main_sprite = s1.Sprite_g1(g1, g1.win_center)

main_sprite.gravity = True
main_sprite.collision = True

#game loop
while g1.run:
    loop.set_loop()
    loop.set_events()
    loop.set_background(dic.color[dic.DARK_GREY])
    #insert methods here
    main_sprite.Actions(main_sprite).move((pg.K_UP, pg.K_DOWN, pg.K_LEFT, pg.K_RIGHT))
    main_sprite.update_sprite()
    loop.update_display()
pg.quit()