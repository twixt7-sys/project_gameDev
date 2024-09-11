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
TRAIL_COLOR = (255, 0, 0, 30)  # Slightly transparent red for trail

# Ball properties
ball_radius = 20
ball_pos = [SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2]
ball_speed = [4, 3]  # Speed along x and y

# Trail properties
trail_length = 20
trail = []  # List to store previous positions of the ball

# Clock to control frame rate
clock = pygame.time.Clock()

# Surface for the trail (with transparency)
trail_surface = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.SRCALPHA)

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

    # Store the ball's position in the trail
    trail.append(list(ball_pos))

    # Limit trail length
    if len(trail) > trail_length:
        trail.pop(0)

    # Clear the screen (with a slight trail effect using transparency)
    screen.fill(BLACK)

    # Clear the trail surface with transparency to maintain the previous trails
    trail_surface.fill((0, 0, 0, 0))

    # Draw the trail (gradually fading older trail positions)
    for i, pos in enumerate(trail):
        alpha = 255 * (i + 1) // trail_length  # Adjust alpha for fade effect
        trail_color = (*WHITE[:3], alpha)  # Set color with transparency
        pygame.draw.circle(trail_surface, trail_color, pos, ball_radius)

    # Blit the trail surface onto the main screen
    screen.blit(trail_surface, (0, 0))

    # Draw the ball
    pygame.draw.circle(screen, WHITE, ball_pos, ball_radius)

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(60)
