class Entity(object):
    def __init__(self, game, center, size=[10, 10], movement_speed=1, color=(255, 255, 255)):
        self.game = game
        # positional attributes
        self.size = size
        self.center = center
        self.pos = center[0] - size[0] / 2, center[1] - size[1] / 2
        # surface values
        ts = self.topside = self.pos[1]
        bs = self.botside = self.pos[1] + self.size[1]
        ls = self.leftside = self.pos[0]
        rs = self.rightside = self.pos[0] + self.size[0]
        self.surfaces = [ts, bs, ls, rs]
        #movement attributes
        self.movement_speed = movement_speed
        self.velocity = [0, 0]
        self.acceleration = [0, 0]
        self.dir = 0
        #visual attributes
        self.color = color
        self.transparency = 255
        # states
        self.is_active = True
        self.is_flying = False
        self.is_grounded = False
        self.is_gravity_affected = True
        self.is_tangible = True
        self.is_friction_affected = True
        self.is_wind_affected = True
        self.is_wind_resistance_affected = True