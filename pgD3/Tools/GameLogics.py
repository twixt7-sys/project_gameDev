class GameLogics():

    def __init__(self, environment):
        self.env = environment

    def apply_gravity(self, velocity_input):
        grav = self.env.grav_val
        return velocity_input + grav

    def apply_wind(self, velocity_input):
        wind = self.env.wind
        return velocity_input + wind

    def apply_wind_resistance(self, velocity_input):
        wind_resistance = self.env.wind_resistance
        return [velocity_input[0] * wind_resistance, velocity_input[1] * wind_resistance]
    
    def apply_friction(self, velocity_input):
        friction = 0
        return velocity_input * friction
    '''friction = platform.fric_val'''

    def apply_bounce(self, velocity_input):
        bounce = 0
        return velocity_input * -bounce
    '''friction = platform.fric_val'''