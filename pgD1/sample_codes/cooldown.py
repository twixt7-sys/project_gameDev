import pygame

# Initialize Pygame
pygame.init()

# Set up display
screen = pygame.display.set_mode((800, 600))

# Set up some colors
WHITE = (255, 255, 255)

# Set up variables for cooldown
cooldown_time = 500  # Cooldown period in milliseconds (e.g., 500ms = 0.5 seconds)
last_shot_time = 0  # When the last shot was fired

# Game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Get the current time
    current_time = pygame.time.get_ticks()
    
    # Check if the space key is pressed and cooldown has passed
    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE]:
        if current_time - last_shot_time >= cooldown_time:
            # Action to perform (e.g., shooting)
            print("Shot fired!")
            last_shot_time = current_time  # Reset the cooldown timer
    
    # Clear the screen
    screen.fill(WHITE)
    
    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
