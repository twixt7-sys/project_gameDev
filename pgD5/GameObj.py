import pygame as pg
pg.init()
class Game(object):
    def __init__(self, size=[900, 900], title="Game Project", pyg=pg, run=True):
        # parameterized properties
        self.pyg, self.size, self.title, self.run = pyg, size, title, run
        # parameter-derived properties
        self.center = [self.size[0] / 2, self.size[1] / 2]
        # other properties
        self.frame_rate = 60
        # edge collision boxes
        self.top      =   (0, -100, self.size[0], 100)
        self.bottom   =   (0, self.size[1], self.size[0], 100)
        self.left     =   (-10, 0, 10, self.size[1])
        self.right    =   (self.size[0], 0, 10, self.size[1])
        self.collision_box = (self.top, self.bottom, self.left, self.right)
        #clock attribute
        self.clock = pyg.time.Clock()

    def set_window(self):
        self.win = self.pyg.display.set_mode(self.size)
        self.pyg.display.set_caption(self.title)
    
    def quit(self):
        self.pyg.quit()