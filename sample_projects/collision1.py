import pygame
import sys

# Initialize pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Ball properties
ball_radius = 20
ball_pos = [SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2]
ball_speed = [10, 10]  # Speed along x and y

# Clock to control frame rate
clock = pygame.time.Clock()

def handle_collision():
    # Check for X axis collision
    if ball_pos[0] - ball_radius <= 0 or ball_pos[0] + ball_radius >= SCREEN_WIDTH:
        ball_speed[0] = -ball_speed[0]
        print("X-axis collision")

    # Check for Y axis collision
    if ball_pos[1] - ball_radius <= 0 or ball_pos[1] + ball_radius >= SCREEN_HEIGHT:
        ball_speed[1] = -ball_speed[1]
        print("Y-axis collision")

# Main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Move the ball
    ball_pos[0] += ball_speed[0]
    ball_pos[1] += ball_speed[1]

    # Handle border collisions
    handle_collision()

    # Fill the screen with black
    screen.fill(BLACK)

    # Draw the ball
    pygame.draw.circle(screen, RED, ball_pos, ball_radius)

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(60)
