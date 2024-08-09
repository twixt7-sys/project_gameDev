#snake game

import pygame as pg
pg.init()

window_size = 900, 900
win = pg.display.set_mode(window_size)
pg.display.set_caption("Snake 1.0")

run = True

#snake parameters
center = window_size[0] / 2
snake_pos = [center, center]
snake_size = 10
snake_color = (255, 255, 50)
snake_length = 3
unit_per_length = 10
snake_speed = 2

bg_color = (0, 0, 0)

while run:
    pg.time.delay(10)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False
    
    #controls
    keys = pg.key.get_pressed()
    if keys[pg.K_UP]:
        snake_pos[1] -= snake_speed
    if keys[pg.K_DOWN]:
        snake_pos[1] += snake_speed
    if keys[pg.K_LEFT]:
        snake_pos[0] -= snake_speed
    if keys[pg.K_RIGHT]:
        snake_pos[0] += snake_speed

    #win.fill(bg_color)
    pg.draw.rect(win, snake_color, (snake_pos[0], snake_pos[1], snake_size, snake_size))
    pg.display.update()
pg.quit()