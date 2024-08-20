#importing folder for whole project using absolute path
import os
import sys
sys.path.append(os.path.abspath('pgD2'))

#importing pygame and project classes
import pygame as pg
import Tools.Game as g
import Tools.Dictionary as d
import Tools.Matrix as m
pg.init()
#import Sprite_g1 as s1

#creating a game object
g1 = g.Game(pg, (900, 900), "sim_1", 60)
g1.set_window()
ins, dic = g1.Loop(g1), d.Dictionary()

#instantiate matrix
m1 = m.Matrix(g1, pg, d, dic.color['WHITE'], dic.color['BLACK'])

#game loop:
while g1.run:
    ins.set_loop()
    ins.set_events(None)
    ins.set_background(dic.color['BLACK'])
    #Counter
    pg.time.delay(500)
    m1.paint_matrix_field(g1.win_center, 50, "HELLO WORLD")
    ins.update_display()
pg.quit()