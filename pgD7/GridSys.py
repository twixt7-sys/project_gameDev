import pygame

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

# Set tile size and scale factor
TILE_SIZE = 32  # Original tile size
SCALE_FACTOR = 10  # Scale tiles by 2x (adjust as needed)
SCALED_TILE_SIZE = TILE_SIZE * SCALE_FACTOR  # Final size after scaling

# Load and scale tiles
grass_tile = pygame.image.load("pgD7/grass_tile.png")
wall_tile = pygame.image.load("pgD7/wall_tile.png")

grass_tile = pygame.transform.scale(grass_tile, (SCALED_TILE_SIZE, SCALED_TILE_SIZE))
wall_tile = pygame.transform.scale(wall_tile, (SCALED_TILE_SIZE, SCALED_TILE_SIZE))

# Sample 2D map
tilemap = [
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
]

# Render the tilemap
def draw_map():
    for row_index, row in enumerate(tilemap):
        for col_index, tile in enumerate(row):
            x, y = col_index * SCALED_TILE_SIZE, row_index * SCALED_TILE_SIZE
            if tile == 1:
                screen.blit(wall_tile, (x, y))
            else:
                screen.blit(grass_tile, (x, y))

# Game loop
running = True
while running:
    screen.fill((0, 0, 0))
    draw_map()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
