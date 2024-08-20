import Tools.game_dir.GameClass as g
class Loop(g.Game):
    def __init__(self, game):
        # passing game and windows instance unto the class
        self.game = game
        self.win = self.game.win

    def set_loop(self, frame_rate=60):
        # set clock and frame rate
        self.game.pyg.time.Clock().tick(self.game.frame_rate)
        self.game.current_time = self.game.pyg.time.get_ticks()

    def set_events(self, events=None):
        self.game.events = events
        for event in self.game.pyg.event.get():
            if event.type == self.game.pyg.QUIT:
                self.game.run = False

    def set_background(self, color=(0, 0, 0)):
        self.win.fill(color)

    def update_display(self):
        self.game.pyg.display.update()