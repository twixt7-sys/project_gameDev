import pygame
import sys

# Initialize Pygame
pygame.init()

WIDTH, HEIGHT = 640, 480
FPS = 4
SCALE_FACTOR = 10

# Function to load and scale spritesheet
def load_spritesheet(PNG_path, frame_width, frame_height, scale_factor=1):
    spritesheet = pygame.image.load(PNG_path).convert_alpha()
    frames = []
    for i in range(spritesheet.get_width() // frame_width):
        frame = spritesheet.subsurface(pygame.Rect(i * frame_width, 0, frame_width, frame_height))
        scaled_frame = pygame.transform.scale(frame, (frame_width * scale_factor, frame_height * scale_factor))
        frames.append(scaled_frame)
    return frames

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Animated Sprite Example")

SPRITE_PATH = "PGd6/Sprite-4.png"
FRAME_WIDTH, FRAME_HEIGHT = 32, 32
animation_frames = load_spritesheet(SPRITE_PATH, FRAME_WIDTH, FRAME_HEIGHT, SCALE_FACTOR)

# Animation Variables
current_frame = 0
frame_delay = 100  # Time per frame in milliseconds
last_update = pygame.time.get_ticks()

# Main Loop
clock = pygame.time.Clock()
while True:
    screen.fill((30, 30, 30))
    
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    # Animation Logic
    now = pygame.time.get_ticks()
    if now - last_update > frame_delay:
        current_frame = (current_frame + 1) % len(animation_frames)
        last_update = now
    
    # Draw Sprite (Centered)
    screen.blit(animation_frames[current_frame], 
                (WIDTH//2 - (FRAME_WIDTH * SCALE_FACTOR)//2, HEIGHT//2 - (FRAME_HEIGHT * SCALE_FACTOR)//2))
    
    pygame.display.flip()
    clock.tick(FPS)
