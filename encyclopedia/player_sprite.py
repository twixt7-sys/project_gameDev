import pygame as pg

class Sprite:
    def __init__(self, sprite_sheet, frame_width, frame_height, scale_factor=1, frame_rate=200, screen=None):
        self.sprite_sheet = pg.image.load(sprite_sheet).convert_alpha()
        self.frame_width = frame_width
        self.frame_height = frame_height
        self.scale_factor = scale_factor
        self.frame_rate = frame_rate
        self.loop = True
        self.frames = []
        self.original_frames = []
        self.current_frame = 0
        self.last_update = pg.time.get_ticks()
        self.extract_frames()
        
        self.screen = screen
        self.afterimages = []
        
        # Movement variables
        self.dir = [0, 0]
        self.pos = [20, 20]
        self.vel = [0, 0]
        self.acc = [0, 0]
        
        # Key Control variables
        self.control = {
            "up": pg.K_UP,
            "down": pg.K_DOWN,
            "left": pg.K_LEFT,
            "right": pg.K_RIGHT,
            "dash": pg.K_SPACE
        }
        
        # Stat variables
        self.health = 100
        self.mana = 100
        self.stamina = 100
        self.regen = [1, 1, 1]
        
        # Attribute variables
        self.speed = 0.5
        self.friction = 0.15
        self.dash_power = 3
        
        # State variables
        self.movement_state = "idle"
        self.magic_state = "idle"
        self.combat_state = "idle"
    
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
        
        # Movement updates
        self.move()
        self.handle_actions()
        self.handle_physics()
        self.update_direction()

        # Update state
        self.apply_states()
        self.apply_regen()
        self.update_states()
    
    def draw(self):
        if self.screen:
            self.screen.blit(self.frames[self.current_frame], self.pos)
        self.draw_afterimages()
        self.draw_statbars()

    def dash(self):
        self.vel[0] += self.dash_power * self.dir[0]
        self.vel[1] += self.dash_power * self.dir[1]

    def move(self):
        # Reset acceleration
        self.acc = [0, 0]
        
        # Moving sprite by applying acceleration
        keys = pg.key.get_pressed()
        if keys[self.control["up"]]:
            self.acc[1] = -self.speed
        if keys[self.control["down"]]:
            self.acc[1] = self.speed
        if keys[self.control["left"]]:
            self.acc[0] = -self.speed
        if keys[self.control["right"]]:
            self.acc[0] = self.speed
    
    def handle_actions(self):
        keys = pg.key.get_pressed()
        if keys[self.control["dash"]]:
            if keys[self.control["up"]]:
                self.vel[1] += -self.dash_power
            elif keys[self.control["down"]]:
                self.vel[1] += self.dash_power
            elif keys[self.control["left"]]:
                self.vel[0] += -self.dash_power
            elif keys[self.control["right"]]:
                self.vel[0] += self.dash_power
            self.create_afterimage()
            self.stamina -= 2

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
        if self.vel[0] > 0:
            self.dir[0] = 1
        elif self.vel[0] < 0:
            self.dir[0] = -1
        else:
            self.dir[0] = 0
        
        if self.vel[1] > 0:
            self.dir[1] = 1
        elif self.vel[1] < 0:
            self.dir[1] = -1
        else:
            self.dir[1] = 0
        
        # Flip sprite left or right based on x direction
        if self.dir[0] > 0:
            self.frames = self.original_frames
        elif self.dir[0] < 0:
            self.frames = [pg.transform.flip(frame, True, False) for frame in self.original_frames]

    # State functions
    def update_states(self):
        if (self.vel[0] <= 0.5 and self.vel[0] >= -0.5) and (self.vel[1] <= 0.5 and self.vel[1] >= -0.5):
            self.movement_state = "idle"
        else:
            self.movement_state = "moving"

    def apply_states(self):
        if self.movement_state == "moving":
            self.regen = [1, 1, 1]
            self.frame_rate = 100
        elif self.movement_state == "idle":
            self.regen = [1, 1, 3]
            self.frame_rate = 500
    
    def apply_regen(self):
        self.health = min(self.health + self.regen[0], 100)
        self.mana = min(self.mana + self.regen[1], 100)
        self.stamina = min(self.stamina + self.regen[2], 100)
            
    def create_afterimage(self):
        if self.screen:
            self.screen.blit(self.frames[self.current_frame], self.pos)
            pg.display.flip()
            pg.time.delay(50)
            pg.draw.rect(self.screen, (0, 0, 0), (self.pos[0], self.pos[1], self.frame_width, self.frame_height))
            pg.display.flip()
            
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
        
    def draw_statbars(self):
        # Draw health, mana, and stamina bars
        pg.draw.rect(self.screen, (200, 80, 80), (10, 10, self.health * 0.80, 5))
        pg.draw.rect(self.screen, (80, 80, 200), (10, 10 + 6, self.mana * 0.80, 5))
        pg.draw.rect(self.screen, (200, 200, 80), (10, 10 + (6 * 2), self.stamina * 0.80, 5))

# Pygame Simulation Setup
def main():
    pg.init()
    screen = pg.display.set_mode((800, 600))
    clock = pg.time.Clock()
    sprite = Sprite("encyclopedia/player.png", 32, 32, scale_factor=2, frame_rate=100, screen=screen)
    
    running = True
    while running:
        screen.fill((30, 30, 30))
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
        
        sprite.update()
        sprite.draw()
        
        pg.display.flip()
        clock.tick(60)
    
    pg.quit()

if __name__ == "__main__":
    main()