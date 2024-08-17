'''
Order of setup:
    - make game object
    - set window
    - create instance variables for game.Loop() & dic.Dictionart()              [Optional]
    - instantiate in-game objects
    - game loop: (while game.run:)
        > set loop
        > set events
        > set background
        > in-loop game methods
        > update display
    - quit
'''
class Game(object):
    def __init__(self, pyg, win_size = (900, 900), title = "Game X", frame_rate = 90):
        #Pygame Instance
        self.pyg = pyg
        #Parameterized Properties
        self.win_size = win_size
        self.title = title
        self.frame_rate = frame_rate
        self.win = None
        #Unparameterized Properties
        self.run = True
        self.current_time = None
    def set_window(self):
        self.win = self.pyg.display.set_mode(self.win_size)
        self.pyg.display.set_caption(self.title)
        self.win_center = (int(self.win_size[0] / 2), int(self.win_size[1] / 2))
    class Loop:
        def __init__(self, game):
            self.game = game
            self.win = self.game.win
        def set_loop(self):
            ins = self.game
            ins.pyg.time.Clock().tick(ins.frame_rate)
            ins.current_time = ins.pyg.time.get_ticks()
        def set_events(self, events):
            ins = self.game
            self.events = events
            for event in ins.pyg.event.get():
                if event.type == ins.pyg.QUIT:
                    ins.run = False
        def set_controls(self):
            return  #To configure
        def set_background(self, color):
            self.win.fill(color)
        def update_display(self):
            self.game.pyg.display.update()