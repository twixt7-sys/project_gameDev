class AttributesClass:
    def __init__(self, entity):
        self.entity = entity
    def positional_attributes(self, size, center):
        self.size = size
        self.center = center
        self.pos = [self.center[0] - self.size[0] / 2, self.center[1] - self.size[1] / 2]
        self.rect_val = [self.pos[0], self.pos[1], self.size[0], self.size[1]]
    def movement_attributes(self, movement_speed, initial_velocity=[0, 0], initial_acceleration=[0, 0], initial_direction=0):
        self.movement_speed = movement_speed
        self.velocity = initial_velocity
        self.acceleration = initial_acceleration
        self.direction = initial_direction
    def visual_attributes(self, color, transparency=255):
        self.color = color
        self.transparency = transparency
    def states(self):
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