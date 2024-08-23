class Entity(object):
    def __init__(self, game, center, size=[10, 10], movement_speed=1, color=(255, 255, 255)):
        self.game = game
        # positional attributes
        self.size = size
        self.center = center
        self.pos = self.center[0] - self.size[0] / 2, self.center[1] - self.size[1] / 2
        self.rect_val = [self.pos[0], self.pos[1], self.size[0], self.size[1]]
        #movement attributes
        self.movement_speed = movement_speed
        self.velocity = [0, 0]
        self.acceleration = [0, 0]
        self.dir = 0
        #visual attributes
        self.color = color
        self.transparency = 255
        # states
        self.is_controllable = False
        self.is_active = True
        self.is_flying = False
        self.is_grounded = False
        self.is_gravity_affected = True
        self.is_tangible = True
        self.is_friction_affected = True
        self.is_wind_affected = True
        self.is_wind_resistance_affected = True
    
    def update(self):
        Entity.apply_states(self)
        Entity.update_position(self)
        Entity.draw_sprite(self)
    
    def apply_states(self):
        if self.is_controllable:
            self.move()
        if self.is_gravity_affected:
            self.velocity[1] = self.game.logic.apply_gravity(self.velocity[1])
        if self.is_wind_affected:
            self.velocity[0] = self.game.logic.apply_wind(self.velocity[0])
        if self.is_wind_resistance_affected:
            self.velocity = self.game.logic.apply_wind_resistance(self.velocity)
    
    def update_position(self):
        size = self.size
        # update center position based on velocity
        self.center = (self.center[0] + self.velocity[0], self.center[1] + self.velocity[1])
        # recalculate position and rect_val
        pos = self.center[0] - size[0] / 2, self.center[1] - size[1] / 2
        self.pos = pos
        self.rect_val = [pos[0], pos[1], size[0], size[1]]

    def draw_sprite(self):
        self.game.pyg.draw.rect(self.game.win, self.color, self.rect_val)

    def move(self):
        Entity.update_keypress(self)
        speed = self.movement_speed

        if self.movement_keys[0]:  # Up
            self.velocity[1] = self.game.logic.move(self.velocity[1], -speed)
        if self.movement_keys[1]:  # Down
            self.velocity[1] = self.game.logic.move(self.velocity[1], speed)
        if self.movement_keys[2]:  # Left
            self.velocity[0] = self.game.logic.move(self.velocity[0], -speed)
        if self.movement_keys[3]:  # Right
            self.velocity[0] = self.game.logic.move(self.velocity[0], speed)
    
    def update_keypress(self):
        keys = self.game.pyg.key.get_pressed()
        up = keys[self.game.pyg.K_UP]
        down = keys[self.game.pyg.K_DOWN]
        left = keys[self.game.pyg.K_LEFT]
        right = keys[self.game.pyg.K_RIGHT]
        self.movement_keys = [up, down, left, right]