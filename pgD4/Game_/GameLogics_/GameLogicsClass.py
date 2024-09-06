class GameLogics(object):
    X_ALIGNED, Y_ALIGNED, NO_COLLISION = 0, 1, 2

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
    def is_collided(self, rect_input1, rect_input2):   # Axis-Aligned Bounding Box Collision Logic
        x1, y1, w1, h1 = rect_input1
        x2, y2, w2, h2 = rect_input2  # Use h2 for rect_input2
        
        # Check if there is overlap on both x and y axes
        x_overlap = not (x1 < x2 + w2 and x2 < x1 + w1)
        y_overlap = (y1 < y2 + h2 and y2 < y1 + h1)
        
        if x_overlap:
            return 0  # Overlap on x-axis only
        if y_overlap:
            return 1  # Overlap on y-axis only
        if not x_overlap and not y_overlap:
            return 2  # No collision

    def collide_with_all_rects(self, sprite_rect, rects):
        for rect in rects:
            collision_val = GameLogics.is_collided(self, sprite_rect, rect)
            if collision_val == 2:
                return 2
            if collision_val == 0:
                return 0
            if collision_val == 1:
                return 1

    def apply_friction(self, velocity_input):
        friction = self.object.fric_val
        return velocity_input * friction
    def apply_bounce(self, velocity_input):
        bounce = self.game.rects_bounce_val
        return velocity_input * -bounce

    def apply_cooldown(self, action1, action2, action_cooldown, current_time, last_action_time):
        if current_time - last_action_time >= action_cooldown:
            last_jump_time = current_time
            return action1  # performed
        else:
            return action2  # unperformed

