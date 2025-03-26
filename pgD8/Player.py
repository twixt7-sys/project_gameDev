import pygame as pg
import math
import Animation

class Player:
    def __init__(self, pos, scale_factor=1, resolution=[32,32], statbar=None , frame_rate=200, screen=None):
        # Movement variables
        self.dir, self.pos, self.vel, self.acc  = [0, 0], pos, [0, 0], [0, 0]
        # Sprite variables
        self.scale_factor = scale_factor
        self.statbar = statbar
        self.screen = screen
        # Control keys and animations
        self.control = {
            "up": pg.K_UP,
            "down": pg.K_DOWN,
            "left": pg.K_LEFT,
            "right": pg.K_RIGHT,
            "dash": pg.K_SPACE,
            "slash": pg.K_z
        }
        self.animations = {
            "idle": Animation(self.frames, 10, pg.time),
            "moving": Animation(self.frames, 100, pg.time),
            "slash": Animation(self.frames["slash"], 10, pg.time)
        }
        
        # Stat variables
        self.stats = {
            "health": 100,
            "mana": 100,
            "stamina": 100,
        }
        self.regen = [0.5, 0.5, 0.5]
        self.stm_cost = {
            "dash": 1.5,
            "slash": 10
        }

        # Movement Attributes
        self.speed = 1
        self.friction = 0.15
        self.dash_power = 3
        
        # Magic Attributes
        # Combat Attributes
        
        
        # State variables
        self.movement_state = "idle"
        self.magic_state = "idle"
        self.combat_state = "idle"
        
        self.init_animations(self)

    def init_animations(self):
        self.animations["idle"].load_frames("pdD8/player.png", 1, 4, 32, 32)
        self.animations["moving"].load_frames("pgD8/player.png", 1, 4, 32, 32)
    
    def update(self):
        # Movement updates
        self.handle_actions()
        self.handle_physics()
        self.update_direction()
        
        # Update stat bars
        self.statbar.set_stats([
            ((200, 80, 80), self.health),
            ((80, 80, 200), self.mana),
            ((80, 200, 80), self.stamina)
        ])
        self.draw_statbars(self.statbar)

        # Update state
        self.apply_states()
        self.update_states()
    
    def handle_actions(self):
        keys = pg.key.get_pressed()
        self.move(keys)
        if keys[self.control["dash"]]:
            self.dash(keys)
        if keys[self.control["slash"]]:
            self.slash()
    def dash(self, keys):
        if self.stamina > 10:
            if keys[self.control["up"]]:
                self.vel[1] += -self.dash_power
            elif keys[self.control["down"]]:
                self.vel[1] += self.dash_power
            elif keys[self.control["left"]]:
                self.vel[0] += -self.dash_power
            elif keys[self.control["right"]]:
                self.vel[0] += self.dash_power
            self.stamina -= self.stm_cost["dash"]
            self.animations["dash"].animate(self.screen, self.pos)
    def slash(self):
        slash_sheet = pg.image.load("pgD8/slash.png").convert_alpha()
        slash_frames = [slash_sheet.subsurface((i * 32, 0, 32, 32)) for i in range(7)]
        
        frame_delay = 100  # Delay in milliseconds (adjust for slower/faster slash)
        last_frame_time = pg.time.get_ticks()
        
        for frame in slash_frames:
            # timing logic
            now = pg.time.get_ticks()
            while now - last_frame_time < frame_delay:
                now = pg.time.get_ticks()  # Wait until enough time has passed
            
            self.screen.blit(frame, self.pos)
            pg.display.flip()
            last_frame_time = now  # Update last frame time
        
        self.stamina -= 10
    
    def draw(self):
        if self.screen:
            self.screen.blit(self.frames[self.current_frame], self.pos)
            self.draw_afterimages()

    def move(self, keys):
        # Reset acceleration
        self.acc = [0, 0]
        # Moving sprite by applying acceleration
        if keys[self.control["up"]]:
            self.acc[1] = -self.speed
        if keys[self.control["down"]]:
            self.acc[1] = self.speed
        if keys[self.control["left"]]:
            self.acc[0] = -self.speed
        if keys[self.control["right"]]:
            self.acc[0] = self.speed

    def handle_physics(self):
        # Apply acceleration to velocity
        self.vel[0] += self.acc[0]
        self.vel[1] += self.acc[1]
        
        # Apply velocity to position first
        self.pos[0] += self.vel[0]
        self.pos[1] += self.vel[1]
        
        # Apply friction to velocity
        self.vel[0] *= (1 - self.friction)
        self.vel[1] *= (1 - self.friction)
        
    def update_direction(self):
        # Update direction based on velocity
        self.dir[0] = int(math.copysign(1, self.vel[0])) if self.vel[0] != 0 else 0
        self.dir[1] = int(math.copysign(1, self.vel[1])) if self.vel[1] != 0 else 0
        
        # Flip sprite left or right based on x direction
        if self.dir[0] > 0:
            self.frames = self.original_frames
        elif self.dir[0] < 0:
            self.frames = [pg.transform.flip(frame, True, False) for frame in self.original_frames]

    # Movement state functions
    def update_states(self):
        if (self.vel[0] <= 0.5 and self.vel[0] >= -0.5) and (self.vel[1] <= 0.5 and self.vel[1] >= -0.5):
            self.movement_state = "idle"
        else:
            self.movement_state = "moving"

    def apply_movement_states(self):
        if self.movement_state == "moving":
            self.apply_regen([0.5, 0.5, 0.5])
            self.animations["moving"].animate(self.screen, self.pos)
        elif self.movement_state == "idle":
            self.apply_regen([self.regen[0], self.regen[1], self.regen[2]])
            self.animations["idle"].animate(self.screen, self.pos)
    def apply_combat_states(self):
        if self.combat_state == "attacking":
            self.animations["attacking"].animate(self.screen, self.pos)
        if self.combat_state == "idle":
            pass
    def apply_magic_states(self):
        pass
    
    def apply_regen(self, stats):
        self.health = min(self.health + stats[0], 100)
        self.mana = min(self.mana + stats[1], 100)
        self.stamina = min(self.stamina + stats[2], 100)
            
    def create_afterimage(self):
        if self.screen:
            afterimage = self.frames[self.current_frame].copy()
            afterimage.set_alpha(200)  # Start with a semi-transparent image
            self.afterimages.append([afterimage, self.pos[:], 15])  # (Image, Position, Lifespan)

    def draw_afterimages(self):
        for afterimage in self.afterimages:
            image, pos, lifespan = afterimage
            alpha = int((lifespan / 15) * 200)  # Scale alpha from 200 to 0
            image.set_alpha(max(alpha - 100, 0))  # Ensure it doesn't go negative
            self.screen.blit(image, pos)
            afterimage[2] -= 1  # Reduce lifespan

        # Remove fully transparent afterimages
        self.afterimages = [img for img in self.afterimages if img[2] > 0]
        
    def draw_statbars(self, statbar):
        # Draw stat bars that follows the player
        if self.screen and statbar:
            statbar.draw(self.screen)
            self.statbar.pos = [self.pos[0], self.pos[1] - 15]
