import pygame as pyg
pyg.init()

class Sprite_g1(object):
    RECT, CIRC = 0, 1

    def __init__(self, game, center, size=(10,10), vel=(0,0), accel=(0,0), shape=RECT, color=(255,255,255)):
        #initializing parameter-based properties
        s, g = self, game                                                  
        s.game, s.center, s.size, s.vel, s.accel, s.shape, s.color = game, center, size, vel, accel, shape, color
        #parameter-derived properties:
        s.pos = (s.center[0] - s.size[0] / 2, s.center[1] - s.size[1] / 2)
        s.anchor = (center[0], center[1])
        s.bounding_box = (s.center[0], s.center[1], s.size[0], s.size[1])
        s.direction = (0, 0)
        #environmental toggles
        s.gravity = s.friction = s.wind = s.collision = s.bounce = False
        #game environment property senses
        s.en_prop = [g.gravity, g.friction, g.wind, g.collision, g.bounce]
        #object detection
        s.platforms = []

    def actions(self):                                                          #to-do: 3   |   to test: 1
        def move(self, keys, mode=0):                  #to-test
            pressed = pyg.key.get_pressed()
            var1, var2 = self.accel, self.vel if mode == 0 else (self.vel, self.pos)
            if pressed[keys[0]]:     #up
                var1[1] -= var2[1]
            if pressed[keys[0]]:     #down
                var1[1] += var2[1]
            if pressed[keys[0]]:     #left
                var1[0] -= var2[0]
            if pressed[keys[0]]:     #right
                var1[0] += var2[0]
        def jump(keys, strength):   #to-do
            return
        def dash(keys, strength):   #to-do
            return
        def oscillate(keys, ):      #to-do
            return

    def update(self):                                                           #to-do: 3   |   to test: 2
        grav, fric, winds, col, bounce = self.en_prop       #senses the environment
        Sprite_g1.environment_logics(self, grav, fric, winds, col, bounce)
        Sprite_g1.draw_sprite(self)

    def draw_sprite(self):          #to test
        if self.shape == Sprite_g1.RECT:
            pyg.draw.rect(self.game.win, self.color, (self.pos[0], self.pos[1], self.size[0], self.size[1]))
    def interact(self, platforms):  #to test
        self.platforms = platforms
    def get_direction(self):        #to-do: get the net velocity and return a tuple of the direction
        return
    def is_grounded(self):          #to-do: detect if the sprite is on the ground
        return

    def environment_logics(self, grav, fric, winds, col, bounce):               #to-do: 0   |   to test: 5
        if self.gravity:            #to test
            Sprite_g1.grav_logic(grav)
        if self.friction:           #to test
            Sprite_g1.fric_logic(fric)
        if self.wind:               #to-test
            Sprite_g1.wind_logic(winds)
        if self.collision:          #to-test
            Sprite_g1.col_logic(col)
        if self.bounce:             #to-test
            Sprite_g1.bounce_logic(bounce)

    #environment_logics sub-methods                                              to-do: 3   |   to test: 0
    def grav_logic(self, grav):     #to test
        self.accel[1] += grav
        self.vel[1] += self.accel[1]
    def fric_logic(self, fric):     #to test
        if self.dir[0] == -1:                       #left
            self.accel[0] = fric * self.accel[0]
            self.vel[0] += fric
        elif self.dir[0] == 1:                      #right
            self.accel[0] = fric * self.accel[0]
            self.vel[0] += fric
    def wind_logic(self, wind):     #to-do
        self.accel[0] += wind
        self.vel[0] += self.accel[0]
    def col_logic(self, col):       #to-do
        return
    def bounce_logic(self, bounce): #to-do
        return