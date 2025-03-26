import pygame
import sys

# Initialize Pygame
pygame.init()

WIDTH, HEIGHT = 900, 600
FPS = 30  # Adjusted for smoother animation
SCALE_FACTOR = 3
ACCELERATION = 3
FRICTION = 0.15  # Added friction for smoother movement

# Initialize screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Animated Sprite Example")

SPRITE_PATH = "PGd6/main_char.png"
FRAME_WIDTH, FRAME_HEIGHT = 32, 32
FRAME_DELAY = 100  # Time per frame in milliseconds

class Sprite:
    def __init__(self, sprite_sheet, frame_width, frame_height, scale_factor=1, frame_rate=100, loop=True):
        self.sprite_sheet = pygame.image.load(sprite_sheet).convert_alpha()
        self.frame_width = frame_width
        self.frame_height = frame_height
        self.scale_factor = scale_factor
        self.frame_rate = frame_rate
        self.loop = loop
        self.frames = []
        self.original_frames = []
        self.current_frame = 0
        self.last_update = pygame.time.get_ticks()
        self.extract_frames()
        
        # Movement variables
        self.pos = [WIDTH // 2, HEIGHT // 2]
        self.dir = [0, 0] 
        self.vel = [0, 0]
        self.acc = [0, 0]
    
    def extract_frames(self):
        for i in range(self.sprite_sheet.get_width() // self.frame_width):
            frame = self.sprite_sheet.subsurface(pygame.Rect(i * self.frame_width, 0, self.frame_width, self.frame_height))
            scaled_frame = pygame.transform.scale(frame, (self.frame_width * self.scale_factor, self.frame_height * self.scale_factor))
            self.frames.append(scaled_frame)
        self.original_frames = self.frames[:]
    
    def update(self):
        now = pygame.time.get_ticks()
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
            self.frames = [pygame.transform.flip(frame, True, False) for frame in self.original_frames]
    
    def draw(self, screen):
        screen.blit(self.frames[self.current_frame], self.pos)

    def dash(self, power):
        self.acc[0] = power * self.dir[0]
        self.acc[1] = power * self.dir[1]

# Create sprite instance
sprite = Sprite(SPRITE_PATH, FRAME_WIDTH, FRAME_HEIGHT, SCALE_FACTOR, FRAME_DELAY)

# Main Loop
clock = pygame.time.Clock()
while True:
    screen.fill((100, 200, 100))
    
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
    # Handle movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        sprite.acc[0] = -ACCELERATION
        sprite.dir[0] = -1
    elif keys[pygame.K_RIGHT]:
        sprite.acc[0] = ACCELERATION
        sprite.dir[0] = 1
    else:
        sprite.acc[0] = 0
        sprite.dir[0] = 0

    if keys[pygame.K_UP]:
        sprite.acc[1] = -ACCELERATION
        sprite.dir[1] = -1
    elif keys[pygame.K_DOWN]:
        sprite.acc[1] = ACCELERATION
        sprite.dir[1] = 1
    else:
        sprite.acc[1] = 0
        sprite.dir[1] = 0
        
    if keys[pygame.K_SPACE]:
        sprite.dash(10)

    # Update animation
    sprite.update()
    sprite.draw(screen)
    
    pygame.display.flip()
    clock.tick(FPS)
