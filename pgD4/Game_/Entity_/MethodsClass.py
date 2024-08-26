class Methods:
    def apply_states(self):
        if self.is_controllable:
            Methods.move(self)
        if self.is_tangible:
            self.is_collided = True if self.game.logic.collide_with_all_rects(self) else (False)
        if self.is_gravity_affected:
            self.velocity[1] = self.game.logic.apply_gravity(self.velocity[1])
        if self.is_wind_affected:
            self.velocity[0] = self.game.logic.apply_wind(self.velocity[0])
        if self.is_wind_resistance_affected:
            self.velocity = self.game.logic.apply_wind_resistance(self.velocity)

    def move(self):
        self.movement_keys = Methods.update_keypress(self)
        speed = self.movement_speed
        if self.movement_keys[0]:  # Up
            self.velocity[1] = self.game.logic.apply_movement(self.velocity[1], -speed)
        if self.movement_keys[1]:  # Down
            self.velocity[1] = self.game.logic.apply_movement(self.velocity[1], speed)
        if self.movement_keys[2]:  # Left
            self.velocity[0] = self.game.logic.apply_movement(self.velocity[0], -speed)
        if self.movement_keys[3]:  # Right
            self.velocity[0] = self.game.logic.apply_movement(self.velocity[0], speed)

    def update_position(self):
        size = self.size
        # update velocity based on acceleration
        self.velocity = [self.velocity[0] + self.acceleration[0], self.velocity[1] + self.acceleration[1]]
        # update center position based on velocity
        self.center = [self.center[0] + self.velocity[0], self.center[1] + self.velocity[1]]
        # recalculate position and rect_val
        pos = [self.center[0] - size[0] / 2, self.center[1] - size[1] / 2]
        self.pos = pos
        self.rect_val = [pos[0], pos[1], size[0], size[1]]
        print(f"Updated position to: {self.center}, Velocity: {self.velocity}")

    def update_keypress(self):
        keys = self.game.pyg.key.get_pressed()
        up = keys[self.game.pyg.K_UP]
        down = keys[self.game.pyg.K_DOWN]
        left = keys[self.game.pyg.K_LEFT]
        right = keys[self.game.pyg.K_RIGHT]
        movement_keys = [up, down, left, right]
        return movement_keys