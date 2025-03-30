import pygame as pg
import math
import Animation as a

class Player:
    def __init__(self, pos, statbar, screen):
        # Movement variables
        self.dir, self.pos, self.vel, self.acc  = [0, 0], pos, [0, 0], [0, 0]
        # Sprite variables
        self.scale_factor = 3
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
            "idle": a.Animation("pgD8/player.png", pg.time, 10, [1, 4]),
            "moving": a.Animation("pgD8/player.png", pg.time, 50, [1, 4]),
            "dash": a.Animation("pgD8/player.png", pg.time, 100, [1, 4]),
            "slash": a.Animation("pgD8/slash.png", pg.time, 10, [1, 7]),
            
        }
        
        # Stat variables
        self.stats = [100, 100, 100]  # HP, MP, STM
        self.stat_colors = [(200, 80, 80), (80, 80, 200), (200, 200, 80)]
        self.regen = [0.5, 0.5, 0.5]  # HP, MP, STM
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

    def update(self):
        # States
        self.update_states()
        self.apply_movement_states()
        self.apply_magic_states()
        self.apply_combat_states()
        
        # Movement
        self.update_direction()
        self.handle_actions()
        self.handle_physics()
        
        # Update stat bars
        self.statbar.update(self.screen, self.stats, self.pos, self.stat_colors)

    def handle_actions(self):
        keys = pg.key.get_pressed()
        self.move(keys)
        if keys[self.control["dash"]]:
            self.dash(keys)
        if keys[self.control["slash"]]:
            self.slash()
    def move(self, keys):
        self.acc = [0, 0]
        if keys[self.control["up"]]:
            self.acc[1] = -self.speed
        if keys[self.control["down"]]:
            self.acc[1] = self.speed
        if keys[self.control["left"]]:
            self.acc[0] = -self.speed
        if keys[self.control["right"]]:
            self.acc[0] = self.speed
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
            anim = self.animations["dash"]
            anim.make_trail(self.pos)
    def slash(self):
        self.stamina -= self.stm_cost["slash"]
        self.animations["slash"].animate(self.screen, self.pos)
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
        anim = self.animations["moving"]
        if self.dir[0] != 0:
            anim.flip_frames(self.dir[0] < 0, False)

    # States
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

    def apply_regen(self, regen):
        self.health = min(self.stats[0] + regen[0], 100)
        self.mana = min(self.stats[1] + regen[1], 100)
        self.stamina = min(self.stats[2] + regen[2], 100)

