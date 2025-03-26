import pygame as pg

# external factors
FRICTION = 0.1

class Sprite:
    def __init__(self, sprite_sheet, frame_width, frame_height, scale_factor=1, frame_rate=100, loop=True):
        self.sprite_sheet = pg.image.load(sprite_sheet).convert_alpha()
        self.frame_width = frame_width
        self.frame_height = frame_height
        self.scale_factor = scale_factor
        self.frame_rate = frame_rate
        self.loop = loop
        self.frames = []
        self.original_frames = []
        self.current_frame = 0
        self.last_update = pg.time.get_ticks()
        self.extract_frames()
        
        # Movement variables
        self.dir = [0, 0]
        self.pos = [20, 20]
        self.vel = [0, 0]
        self.acc = [0, 0]
    
    def extract_frames(self):
        for i in range(self.sprite_sheet.get_width() // self.frame_width):
            frame = self.sprite_sheet.subsurface(pg.Rect(i * self.frame_width, 0, self.frame_width, self.frame_height))
            scaled_frame = pg.transform.scale(frame, (self.frame_width * self.scale_factor, self.frame_height * self.scale_factor))
            self.frames.append(scaled_frame)
        self.original_frames = self.frames[:]
    
    def update(self):
        now = pg.time.get_ticks()
        if now - self.last_update > self.frame_rate:
            self.current_frame = (self.current_frame + 1) % len(self.frames)
            self.last_update = now
        
        # Apply acceleration to velocity
        self.vel[0] += self.acc[0]
        self.vel[1] += self.acc[1]
        
        # Apply friction
        self.vel[0] *= (1 - FRICTION)
        self.vel[1] *= (1 - FRICTION)
        
        # Update position
        self.pos[0] += self.vel[0]
        self.pos[1] += self.vel[1]
        
        # update direction
        if self.vel[0] > 0:
            self.direction = "right"
        elif self.vel[0] < 0:
            self.direction = "left"
        elif self.vel[1] > 0:
            self.direction = "down"
        elif self.vel[1] < 0:
            self.direction = "up"
            
        # flips left or right based on x direction
        if self.dir[0] > 0:
            self.frames = self.original_frames
        elif self.dir[0] < 0:
            self.frames = [pg.transform.flip(frame, True, False) for frame in self.original_frames]
    
    def draw(self, screen):
        screen.blit(self.frames[self.current_frame], self.pos)

    def dash(self, power):
        self.acc[0] = power * self.dir[0]
        self.acc[1] = power * self.dir[1]
