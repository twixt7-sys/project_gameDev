import pygame as pg
pg.init()
class Game:
    def __init__(self, size=[900, 900], title="Game Project", pyg=pg, run=True):
        # parameterized properties
        self.pyg, self.size, self.title, self.run = pyg, size, title, run
        # parameter-derived properties
        self.center = self.size / 2, self.size / 2
        # edge collision boxes
        self.top =      (0, -10, self.size[0], 10)
        self.bottom =   (0, self.size[1], self.size[0], 10)
        self.left =     (-10, 0, 10, self.size[1])
        self.right =    (self.size[0], 0, 10, self.size[1])

    def set_window(self):
        self.win = self.pyg.display.set_mode(self.size)
        self.pyg.display.set_caption(self.title)

    class Loop:
        def __init__(self, game):
            # passing game and windows instance unto the class
            self.game, self.win = game, self.game.win

        def set_loop(self, frame_rate=60):
            # set clock and frame rate
            self.game.pyg.time.Clock().tick(self.game.frame_rate)
            self.game.current_time = self.game.pyg.time.get_ticks()

        def set_events(self, events=None):
            self.game.events = events
            for event in self.game.pyg.event.get():
                if event.type == self.game.pyg.QUIT:
                    self.game.run = False

        def set_background(self, color):
            self.win.fill(color)

        def update_display(self):
            self.game.pyg.display.update()