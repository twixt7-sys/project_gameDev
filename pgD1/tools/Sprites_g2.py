import pygame as pg

class Sprites_g2(object):
    def __init__(self, pos, vel, speed, accel, size, color):
        self.is_alive = True

        # Parametric properties
        self.pos = list(pos)
        self.vel = list(vel)
        self.accel = list(accel)
        self.size = size
        self.speed = speed  # Use speed as scalar
        self.color = color
        
        # Dependent properties
        self.update_center()
        
        # Sensing properties
        self.platform = []  # Initialize platform as an empty list
        self.current_time = None
        
        # Limiting properties
        self.win_border = None

        # Jumping properties
        self.last_jump_time = 0
        self.jump_cooldown = 500  # Time in milliseconds
        
        # Skill properties
        self.jump_power = 20
    
    def jump(self, strength):
        if self.vel[1] == 0:
            if self.current_time - self.last_jump_time >= self.jump_cooldown:
                print("Jumped!")
                self.vel[1] = -strength
                self.last_jump_time = self.current_time
    
    def is_landed(self, sprite1, platforms):
        for platform in platforms:
            if (
                sprite1.pos[0] < platform.pos[0] + platform.size[0] and
                platform.pos[0] < sprite1.pos[0] + sprite1.size[0] and
                sprite1.pos[1] + sprite1.size[1] <= platform.pos[1] + 1 and
                sprite1.pos[1] + sprite1.size[1] + sprite1.vel[1] > platform.pos[1]
            ):
                return platform  # Return the platform if sprite1 is landed on it
        return None  # Return None if no platform is landed on
    
    def update_sprite(self, win, current_time):
        self.current_time = current_time
        if self.is_alive:
            pg.draw.rect(win, self.color, (self.pos[0], self.pos[1], self.size[0], self.size[1]))
            self.vel[1] += self.accel[1]  # Apply gravity
            self.pos[0] += self.vel[0]
            self.pos[1] += self.vel[1]
            
            # Handle collisions with the window borders
            if self.win_border is not None:
                if self.pos[0] < 0:
                    self.pos[0] = 0
                    self.vel[0] = 0
                if self.pos[0] + self.size[0] > self.win_border[0]:
                    self.pos[0] = self.win_border[0] - self.size[0]
                    self.vel[0] = 0
                if self.pos[1] < 0:
                    self.pos[1] = 0
                    self.vel[1] = 0
                if self.pos[1] + self.size[1] > self.win_border[1]:
                    self.pos[1] = self.win_border[1] - self.size[1]
                    self.vel[1] = 0
            
            # Handle collisions with platforms
            landed_platform = self.is_landed(self, self.platform)
            if landed_platform:  # If the sprite has landed on a platform
                self.pos[1] = landed_platform.pos[1] - self.size[1]
                self.vel[1] = 0

            self.update_center()
    
    def update_center(self):
        self.center = (self.pos[0] + self.size[0] // 2, self.pos[1] + self.size[1] // 2)
    
    def arrow_controls(self, keys):
        if keys[pg.K_UP]:
            self.jump(self.jump_power)  # Adjust jump strength if needed
        if keys[pg.K_DOWN]:
            if not self.is_landed(self, self.platform):
                self.vel[1] += 1  # Move down
        if keys[pg.K_LEFT]:
            self.vel[0] -= 1  # Move left
        if keys[pg.K_RIGHT]:
            self.vel[0] += 1  # Move right
        self.update_center()
