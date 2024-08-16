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
        s.en_prop_val = [1.0, 0.5, -0.25, 0, 1.0]                                 #initial values
        for i, val in s.en_prop, s.en_prop_val:                                     #assigning initial values as default properties
            s.en_prop[i] = val
    def actions():
        def move(keys):
            return                  #to-do
        def jump(keys, strength):
            return                  #to-do
        def dash(keys, strength):
            return                  #to-do
        def oscillate(keys, ):
            return                  #to-do
    def update(self):
        grav, fric, winds, col, bounce = self.en_prop       #senses the environment
        if self.gravity:
            self.accel[1] += grav
            self.vel[1] += self.accel[1]
        if self.friction:
            if self.dir[0] == -1: #left
                self.accel[0]
        if self.wind:
            return                  #to-do
        if self.collision:
            return                  #to-do
        if self.bounce:
            return                  #to-do
    def draw_sprite(self):
        if self.shape == Sprite_g1.RECT:
            pyg.draw.rect(self.game.win, (self.pos[0], self.pos[1], self.size[0], self.size[1]), self.color)
    def get_direction(self):
        return                      #to-do: get the net velocity and return a tuple of the direction