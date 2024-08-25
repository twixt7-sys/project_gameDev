class G_logics(object):
    def __init__(self, game):
        self.game = game

    # external forces
    def apply_gravity(self, velocity_input):
        grav = self.game.environment.grav_val
        return velocity_input + grav
    def apply_wind(self, velocity_input):
        wind = self.game.environment.wind
        return velocity_input + wind
    def apply_wind_resistance(self, velocity_input):
        wind_resistance = self.game.environment.wr_val
        return [velocity_input[0] * wind_resistance, velocity_input[1] * wind_resistance]

    # internal forces
    def apply_movement(self, velocity_input, movement_speed):
        return velocity_input + movement_speed
    def dash(self,velocity_input, strength):
        return velocity_input + strength

    # reaction forces
    def is_collided(self, rect_input1, rect_input2):                            # Axis-Aligned Bounding Box Collision Logic
        if (rect_input1[0] < rect_input2[0] + rect_input2[2] and
            rect_input2[0] < rect_input1[0] + rect_input1[2] and
            rect_input1[1] < rect_input2[1] + rect_input2[3] and
            rect_input2[1] < rect_input1[1] + rect_input1[3]):
            return True
        return False
    def collide_with_all_rects(self, rects):
        for rect in rects:
            if G_logics.is_collided(self, self.rect_val, rect):
                return True
        return False
    def apply_friction(self, velocity_input):
        friction = self.object.fric_val
        return velocity_input * friction
    def apply_bounce(self, velocity_input):
        bounce = self.object.bounce_val
        return velocity_input * -bounce

    def apply_cooldown(self, action1, action2, action_cooldown, current_time, last_action_time):
        if current_time - last_action_time >= action_cooldown:
            last_jump_time = current_time
            return action1  # performed
        else:
            return action2  # unperformed

