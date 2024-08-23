import Tools.GameLogics as gl
class Entity(object):
    def __init__(self, game, center, size=[10, 10], movement_speed=1, color=(255, 255, 255)):
        self.game = game
        # positional attributes
        self.size = size
        self.center = center
        self.pos = self.center[0] - self.size[0] / 2, self.center[1] - self.size[1] / 2
        self.surfaces = []
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

    def update(self):
        Entity.apply_environment(self)
        Entity.update_position(self)
        self.game.pyg.draw.rect(self.game.win, self.color, (self.pos[0], self.pos[1], self.size[0], self.size[1]))
        
    def apply_environment(self):
        if self.game.env.gravity:
            self.velocity[1] = gl.GameLogics().apply_gravity(self.velocity[1])
        if self.game.env.wind:
            self.velocity[0] = gl.GameLogics().apply_wind(self.velocity[0])
        if self.game.env.wind_resistance:
            self.velocity = gl.GameLogics().apply_wind_resistance(self.velocity)
        #if self.game.env.day_cycle:  (to implement)
            # day cycle logic

    def update_position(self):
        size = self.size
        center = self.center
        pos = center[0] - size[0] / 2, center[1] - size[1] / 2
        ts = self.topside = pos[1]
        bs = self.botside = pos[1] + size[1]
        ls = self.leftside = pos[0]
        rs = self.rightside = pos[0] + size[0]
        self.surfaces = [ts, bs, ls, rs]