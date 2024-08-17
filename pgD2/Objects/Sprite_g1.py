import pygame as pyg
pyg.init()

class Sprite_g1(object):
    RECT, CIRC = 0, 1
    def __init__(self, game, center, size=(10,10), vel=(0,0), accel=(0,0), shape=RECT, color=(255,255,255)):
        s, g = self, game                                                  #initializing parameter-based properties
        s.game, s.center, s.size, s.vel, s.accel, s.shape, s.color = game, center, size, vel, accel, shape, color
        #parameter-derived properties:
        s.pos = (s.size[0] - size[0] / 2, s.size[1] - size[1] / 2)
        s.anchor = (center[0], center[1])
        s.bounding_box = (s.center[0], s.center[1], s.size[0], s.size[1])
        s.direction = (0, 0)
        #environmental toggles
        s.en_togs = (s.gravity, s.friction, s.wind, s.collision, s.bounce)
        s.en_togs[:] = [False] * len(s.en_togs) #sets all elements to False
        #game environment property senses
        s.en_prop = [g.gravity, g.friction, g.wind, g.collision, g.bounce]
        s.en_prop_val = [1.0, 0.5, -0.25, 0, 1.0]                               #initial values
        for i, val in s.en_prop, s.en_prop_val:                                 #assigning initial values as default properties
            s.en_prop[i] = val

    def actions():
        def move(keys):             #to-do
            return
        def jump(keys, strength):   #to-do
            return
        def dash(keys, strength):   #to-do
            return
        def oscillate(keys, ):      #to-do
            return

    def update(self):               #to-do: 3   to test: 2
        grav, fric, winds, col, bounce = self.en_prop       #senses the environment
        if self.gravity:            #to test
            Sprite_g1.grav_logic(grav)
        if self.friction:           #to test
            Sprite_g1.fric_logic(fric)
        if self.wind:               #to-do
            Sprite_g1.
        if self.collision:          #to-do
            return
        if self.bounce:             #to-do
            return
        Sprite_g1.draw_sprite()

    def draw_sprite(self):          #to test
        if self.shape == Sprite_g1.RECT:
            pyg.draw.rect(self.game.win, (self.pos[0], self.pos[1], self.size[0], self.size[1]), self.color)
    def get_direction(self):        #to-do: get the net velocity and return a tuple of the direction
        return
    def is_grounded(self):          #to-do: detect if the sprite is on the ground
        return

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
        return
    def col_logic(self, col):       #to-do
        return
    def bounce_logic(self, bounce): #to-do
        return