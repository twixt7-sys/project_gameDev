import pygame as pg

class Shortcuts(object):
    def make_window(self, win_size, title):
        win = pg.display.set_mode(win_size)
        pg.display.set_caption(title)
        return win