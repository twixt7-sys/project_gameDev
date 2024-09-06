class Entity:
    def __init__(self, game, center, size=[10, 10], movement_speed=0.1, color=(255, 255, 255)):
        self.game = game
        # Directly initialize attributes
        self.size = size
        self.center = center
        self.pos = [self.center[0] - self.size[0] / 2, self.center[1] - self.size[1] / 2]
        self.rect_val = [self.pos[0], self.pos[1], self.size[0], self.size[1]]
        
        self.movement_speed = movement_speed
        self.velocity = [0, 0]
        self.acceleration = [0, 0]
        self.direction = 0
        
        self.color = color
        self.transparency = 255
        
        # Initialize states
        self.is_collided = False
        self.is_controllable = True
        self.is_active = True
        self.is_flying = False
        self.is_grounded = False
        self.is_gravity_affected = False
        self.is_tangible = True
        self.is_can_bounce = False
        self.is_friction_affected = True
        self.is_wind_affected = True
        self.is_wind_resistance_affected = True
        self.has_trail = True

    def update(self):
        self.apply_states()
        self.update_position()
        self.draw_sprite()
    
    def apply_states(self):
        if self.is_controllable:
            Methods.move(self)
        if self.is_tangible:
            bounce_axis = self.game.logic.collide_with_all_rects(self.rect_val, self.game.rects)
            if bounce_axis != 2:  # If collision on X or Y
                self.velocity = self.game.logic.apply_bounce(self.velocity)
                print(f"Bounced on {'x' if bounce_axis == 0 else 'y'} axis")
            if bounce_axis == 2:
                print("no bounce")

            bounce_axis = 2
        if self.is_gravity_affected:
            self.velocity[1] = self.game.logic.apply_gravity(self.velocity[1])
        if self.is_wind_affected:
            self.velocity[0] = self.game.logic.apply_wind(self.velocity[0])
        if self.is_wind_resistance_affected:
            self.velocity = self.game.logic.apply_wind_resistance(self.velocity)

    def update_position(self):
        # update velocity based on acceleration
        self.velocity[0] += self.acceleration[0]
        self.velocity[1] += self.acceleration[1]
        # update center position based on velocity
        self.center[0] += self.velocity[0]
        self.center[1] += self.velocity[1]
        # recalculate position and rect_val
        self.pos = [self.center[0] - self.size[0] / 2, self.center[1] - self.size[1] / 2]
        self.rect_val = [self.pos[0], self.pos[1], self.size[0], self.size[1]]

    def draw_sprite(self):
        self.game.pyg.draw.rect(self.game.win, self.color, self.rect_val)


class Methods:
    @staticmethod
    def move(entity):
        movement_keys = Methods.update_keypress(entity)
        speed = entity.movement_speed
        if movement_keys[0]:  # Up
            entity.velocity[1] = entity.game.logic.apply_movement(entity.velocity[1], -speed)
        if movement_keys[1]:  # Down
            entity.velocity[1] = entity.game.logic.apply_movement(entity.velocity[1], speed)
        if movement_keys[2]:  # Left
            entity.velocity[0] = entity.game.logic.apply_movement(entity.velocity[0], -speed)
        if movement_keys[3]:  # Right
            entity.velocity[0] = entity.game.logic.apply_movement(entity.velocity[0], speed)

    @staticmethod
    def update_keypress(entity):
        keys = entity.game.pyg.key.get_pressed()
        up = keys[entity.game.pyg.K_UP]
        down = keys[entity.game.pyg.K_DOWN]
        left = keys[entity.game.pyg.K_LEFT]
        right = keys[entity.game.pyg.K_RIGHT]
        return [up, down, left, right]
