import pygame as pg

pg.init()

window_size = 900, 900
win = pg.display.set_mode(window_size)
pg.display.set_caption("Snake 1.0")

run = True

# snake parameters
center = window_size[0] / 2
snake_size = 10
snake_color = (255, 255, 50)
snake_length = 20  # Initial length of the snake
snake_speed = 10

# Initialize snake segments positions
snake_segments = [[center, center] for _ in range(snake_length)]

# Initial direction (move to the right)
direction = [snake_speed, 0]

bg_color = (0, 0, 0)
clock = pg.time.Clock()

while run:
    clock.tick(30)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False

    # Handle key presses
    keys = pg.key.get_pressed()
    if keys[pg.K_UP]:
        direction = [0, -snake_speed]
    elif keys[pg.K_DOWN]:
        direction = [0, snake_speed]
    elif keys[pg.K_LEFT]:
        direction = [-snake_speed, 0]
    elif keys[pg.K_RIGHT]:
        direction = [snake_speed, 0]
    
    # Update the snake's head position
    new_head = [snake_segments[0][0] + direction[0], snake_segments[0][1] + direction[1]]
    snake_segments = [new_head] + snake_segments[:-1]

    # Render the snake
    win.fill(bg_color)
    for segment in snake_segments:
        pg.draw.rect(win, snake_color, (segment[0], segment[1], snake_size, snake_size))
    pg.display.update()

pg.quit()
