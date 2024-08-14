#importing folder for whole project using absolute path
import os
import sys
sys.path.append(os.path.abspath('pgD2'))

#importing pygame and project classes
import pygame as pg
pg.init()
import Tools.Game as g
import Tools.Dictionary as d
import Tools.Matrix as m
#import Sprite_g1 as s1

#creating a game object
g1 = g.Game((900, 900), "sim_1", 60, pg)
g1.set_window()
ins, dic = g1.Loop(g1), d.Dictionary()

#instantiate matrix
m1 = m.Matrix(g1, pg, d, dic.color['WHITE'], dic.color['BLACK'])

#game loop:
i = 1
while g1.run:
    ins.set_loop()
    ins.set_events(None)
    ins.set_background(dic.color['BLACK'])
    #Counter
    pg.time.delay(100)
    m1.paint_matrix_field(g1.win_center, 50, i, "HELLO WORLD")
    i += 1
    if i > 11:
        i = 1
    ins.update_display()
pg.quit()