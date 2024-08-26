import pygame as pg
pg.init()
class Game(object):
    def __init__(self, size=[900, 900], title="Game Project", pyg=pg, run=True):
        # parameterized properties
        self.pyg, self.size, self.title, self.run = pyg, size, title, run
        # parameter-derived properties
        self.center = [self.size[0] / 2, self.size[1] / 2]
        # other properties
        self.frame_rate = 0
        # edge collision boxes
        top     = self.top      =   (0, -10, self.size[0], 10)
        bottom  = self.bottom   =   (0, self.size[1], self.size[0], 10)
        left    = self.left     =   (-10, 0, 10, self.size[1])
        right   = self.right    =   (self.size[0], 0, 10, self.size[1])
        # environment attribute
        self.environment = None
        self.logic = None
        self.rects = [top, bottom, left, right]

    def set_window(self):
        self.win = self.pyg.display.set_mode(self.size)
        self.pyg.display.set_caption(self.title)
    
    def quit(self):
        self.pyg.quit()