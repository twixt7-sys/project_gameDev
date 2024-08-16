import sys
import os
import pygame as pg

# Update the path for your modules
sys.path.append(os.path.abspath('pgD1'))

import tools
import pgD1.tools.sprites_g1 as s
import tools.Matrices as m

pg.init()

# Set up display
win_size = 900, 900
win = pg.display.set_mode(win_size)
pg.display.set_caption("Physics")
win_center = tuple(x / 2 for x in win_size)

#Game properties
gravity = 5

# Initialize sprite
s1 = s.Sprite(win_center, (50, 50), 10, (255, 255, 255), 1, s.Sprite.RECT, (win_size[1] - 100), gravity)

run = True
while run:
    pg.time.Clock().tick(60)  # Cap the frame rate at 60 FPS
    current_time = pg.time.get_ticks()
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False

    keys = pg.key.get_pressed()

    # Handle movement
    if keys[pg.K_UP]:
        s1.pos = (s1.pos[0], s1.pos[1] - s1.speed)
    if keys[pg.K_DOWN]:
        s1.pos = (s1.pos[0], s1.pos[1] + s1.speed)
    if keys[pg.K_LEFT]:
        s1.pos = (s1.pos[0] - s1.speed, s1.pos[1])
    if keys[pg.K_RIGHT]:
        s1.pos = (s1.pos[0] + s1.speed, s1.pos[1])
    
    # Handle size changes
    if keys[pg.K_z] and not s1.size[0] > 100:
        s1.size = tuple(x + s1.speed for x in s1.size)
        s1.pos = tuple(x - s1.speed / 2 for x in s1.pos)
    if keys[pg.K_x] and not s1.size[0] < 25:
        s1.size = tuple(x - s1.speed for x in s1.size)
        s1.pos = tuple(x + s1.speed / 2 for x in s1.pos)
    
    #Handle color changes
    if keys[pg.K_a]:
        s1.color = (255, 0, 0)
    if keys[pg.K_s]:
        s1.color = (0, 255, 0)
    if keys[pg.K_d]:
        s1.color = (0, 0, 255)

    # Clear screen and draw sprite
    win.fill((0, 0, 0))
    s1.draw_sprite(win)
    pg.display.update()

pg.quit()
