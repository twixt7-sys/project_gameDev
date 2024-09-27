import pygame
import random
import math

# Initialize Pygame
pygame.init()

# Set up display
width, height = 600, 400
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Random Sprite Movement")

# Define colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Define sprite class
class Sprite(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((20, 20))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        
        # Starting position (center of the screen)
        self.rect.center = (width // 2, height // 2)
        
        # Set random angle and speed
        self.angle = random.uniform(0, 2 * math.pi)  # Random angle in radians
        self.speed = random.uniform(2, 5)  # Random speed between 2 and 5
        
        # Calculate velocity components
        self.vel_x = math.cos(self.angle) * self.speed
        self.vel_y = math.sin(self.angle) * self.speed

    def update(self):
        # Update sprite position based on velocity
        self.rect.x += self.vel_x
        self.rect.y += self.vel_y
        
        # Bounce off walls (reverse direction if hitting window boundaries)
        if self.rect.left <= 0 or self.rect.right >= width:
            self.vel_x = -self.vel_x
        if self.rect.top <= 0 or self.rect.bottom >= height:
            self.vel_y = -self.vel_y

# Create sprite group
sprite_group = pygame.sprite.Group()
sprite = Sprite()
sprite_group.add(sprite)

# Game loop
running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Fill the window with white background
    window.fill(WHITE)
    
    # Update and draw the sprite
    sprite_group.update()
    sprite_group.draw(window)
    
    # Update the display
    pygame.display.flip()
    
    # Frame rate
    clock.tick(60)

pygame.quit()
