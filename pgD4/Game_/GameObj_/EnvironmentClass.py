class Environment(object):
    def __init__(self):
        #environmental toggles
        self.gravity = False
        self.wind = False
        self.wind_resistance = False
        self.day_cycle = False
        #environment values
        self.grav_val = 0.5
        self.wind_val = 0
        self.wr_val = 0.99
        self.dc_val = 60

    def enable_all(self):
        self.gravity = True
        self.wind = True
        self.wind_resistance = True
        self.day_cycle = True

    def disable_all(self):
        self.gravity = False
        self.wind = False
        self.wind_resistance = False
        self.day_cycle = False