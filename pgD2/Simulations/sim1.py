#importing folder for whole project using absolute path
import os
import sys
sys.path.append(os.path.abspath('pgD2'))

#importing pygame and project classes
import pygame as pg
pg.init()
import Tools.Game as g
import Tools.Dictionary as d
#import Sprite_g1 as s1

#creating a game object
g1 = g.Game((900, 900), "sim_1", 60, pg)
g1.set_window()
ins, dic = g1.Loop(g1), d.Dictionary()

while g1.run:
    ins.set_loop()
    ins.set_events(None)
    ins.set_controls()
    ins.set_background(dic.color['BLACK'])
    ins.update_display()
pg.quit()