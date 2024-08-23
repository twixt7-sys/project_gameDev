class G_logics:
    def __init__(self, environment=None, object=None):
        self.env = environment
        self.object = object

    # external forces
    def apply_gravity(self, velocity_input):
        grav = self.env.grav_val
        return velocity_input + grav
    def apply_wind(self, velocity_input):
        wind = self.env.wind
        return velocity_input + wind
    def apply_wind_resistance(self, velocity_input):
        wind_resistance = self.env.wind_resistance
        return [velocity_input[0] * wind_resistance, velocity_input[1] * wind_resistance]

    # internal forces
    def move(self, velocity_input, movement_speed):
        return velocity_input + movement_speed
    def dash(self,velocity_input, strength):
        return velocity_input + strength

    # reaction forces
    def apply_friction(self, velocity_input):
        friction = self.object.fric_val
        return velocity_input * friction
    def apply_bounce(self, velocity_input):
        bounce = self.object.bounce_val
        return velocity_input * -bounce

    def cooldown_logic(self):
        