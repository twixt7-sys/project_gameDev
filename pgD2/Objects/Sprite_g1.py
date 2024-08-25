import pygame as pyg
pyg.init()

class Sprite_g1(object):
    RECT, CIRC = 0, 1

    def __init__(self, game, center, size=[10,10], speed=0.8, vel=[0,0], accel=[0,0], shape=RECT, color=(255,255,255)):
        #initializing parameter-based properties
        s, g = self, game
        s.game, s.center, s.size, s.speed, s.vel, s.accel, s.shape, s.color = game, center, size, speed, vel, accel, shape, color
        #parameter-derived properties:
        s.pos = [s.center[0] - s.size[0] / 2, s.center[1] - s.size[1] / 2]
        s.anchor = [center[0], center[1]]
        s.bounding_box = [s.center[0], s.center[1], s.size[0], s.size[1]]
        s.direction = [0, 0]
        
        #environmental toggles
        s.gravity = s.friction = s.wind = s.collision = s.bounce = True
        #game environment property senses
        s.en_prop = [g.gravity, g.friction, g.wind, g.collision, g.bounce]
        
        #object detection
        s.platforms = []

    def update_sprite(self):
        Sprite_g1.environment_response(self)
        Sprite_g1.collide_with_border(self)
        Sprite_g1.update_position(self)
        Sprite_g1.draw_sprite(self)

    # update sub-methods
    def update_position(self):
        self.vel[0] += self.accel[0]
        self.vel[1] += self.accel[1]
        self.pos[0] += self.vel[0]
        self.pos[1] += self.vel[1]

    def sense_environment(self):
        grav, fric, winds, col, bounce = self.en_prop
        Sprite_g1.assess_environment(self, grav, fric, winds, col, bounce)

    def draw_sprite(self):
        if self.shape == Sprite_g1.RECT:
            pyg.draw.rect(self.game.win, self.color, (self.pos[0], self.pos[1], self.size[0], self.size[1]))

    # other methods
    def collide_with_border(self):
        border = self.game.win_size

        sprite_left_side = self.pos[0]
        sprite_right_side = self.pos[0] + self.size[0]
        sprite_top_side = self.pos[1]
        sprite_bottom_side = self.pos[1] + self.size[1]

        if sprite_top_side <= 0:
            self.pos[1] = 0
            self.vel[1] *= -1
        if sprite_bottom_side >= border[1]:
            self.pos[1] = border[1] - self.size[1]
            self.vel[1] *= 1
        if sprite_left_side <= 0:
            self.pos[0] = 0
            self.vel[0] *= -1
        if sprite_right_side >= border[0]:
            self.pos[0] = border[0] - self.size[0]
            self.vel[0] *= -1

    def interact(self, platforms):  #to test
        self.platforms = platforms
    def get_direction(self):        #to-do: get the net velocity and return a tuple of the direction
        return
    def is_grounded(self):          #to-do: detect if the sprite is on the ground
        return
    def is_collided(self, sprite, objects=None, margin=0):    #collision logic
        if objects is not None: #collide with platforms
            for object in objects:
                s_vel, s_pos, s_size, o_pos, o_size = sprite.vel, sprite.pos, sprite.size, object.pos, object.size
                #col_logic(sprite, objects)
                if (
                    margin + s_pos[0] < o_pos[0] + o_size[0] and
                    margin + o_pos[0] < s_pos[0] + s_size[0] and
                    margin + s_pos[1] + s_size[1] <= o_pos[1] + 1 and
                    margin + s_pos[1] + s_size[1] + s_vel[1] > o_pos[1]
                ):
                    return object
            return None
        else: #collide with border
            win_borderboxes = (
                (0, -10, self.game.win_size[0], 10),                            #top_windowbox
                (0, self.game.win_size[1], self.game.win_size[0], 10),          #bottom_windowbox
                (-10, 0, 10, self.game.win_size[1]),                            #left_windowbox
                (self.game.win_size[0], 0, 10, self.game.win_size[1]))          #right_windowbox
            for object in win_borderboxes:
                if (
                    margin + sprite.pos[0] < object[0] + object[2] and
                    margin + object[2] < sprite.pos[0] + sprite.size[0] and
                    margin + sprite.pos[1] + sprite.size[1] <= object[3] + 1 and
                    margin + sprite.pos[1] + sprite.size[1] + sprite.vel[1] > object[3]
                ):
                    return object
            return None

    def environment_response(self):                                             #to-do: 0   |   to test: 4
        g = self.game
        if self.gravity:
            Sprite_g1.grav_logic(self, g.gravity)
        if self.friction:           #to test
            Sprite_g1.fric_logic(self, g.friction)
        if self.wind:               #to-test
            Sprite_g1.wind_logic(self, g.winds)
        if self.collision:          #to-test
            Sprite_g1.col_logic(self, g.collision)
        if self.bounce:             #to-test
            Sprite_g1.bounce_logic(self, g.bounce, self.direction)

    #environment_logics sub-methods                                              to-do: 3   |   to test: 1
    def grav_logic(self, grav):
        self.accel[1] += grav
        self.vel[1] += self.accel[1]

    def fric_logic(self, fric):     #to test
        return

    def wind_logic(self, wind):     #to-do
        self.accel[0] += wind
        self.vel[0] += self.accel[0]

    def col_logic(self, col):       #to-do
        if self.is_collided(self, None, col): #with window border
            print("*Sprite collided with border!")
        if self.is_collided(self, self.platforms, col): #with objects
            print("*Sprite collided with platform!")

    def bounce_logic(self, bounce, direction): #to-do
        bounce_efficiency = bounce
        if self.is_collided(self, None): #with window border
            self.vel[0] *= 1 * bounce_efficiency
            self.vel[1] *= -1 * bounce_efficiency
        if self.is_collided(self, self.platforms): #with obje cts
            self.vel[0] *= 1
            self.vel[1] *= -1

    class Actions():                                                          #to-do: 3   |   to test: 1
        def __init__(self, sprite):
            self.sprite = sprite
        def move(self, keys):                  #to-test
            pressed = pyg.key.get_pressed()
            s = self.sprite
            s.accel = [0, 0]         #Reset acceleration
            if pressed[keys[0]]:     #up
                s.accel[1] -= s.speed
            if pressed[keys[1]]:     #down
                s.accel[1] += s.speed
            if pressed[keys[2]]:     #left
                s.accel[0] -= s.speed
            if pressed[keys[3]]:     #right
                s.accel[0] += s.speed
        def jump(keys, strength):   #to-do
            return
        def dash(keys, strength):   #to-do
            return
        def oscillate(keys, ):      #to-do
            return