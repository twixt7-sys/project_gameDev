import pygame as pg
pg.init()

#Window Settings
win_size = 900, 600
win = pg.display.set_mode(win_size)
pg.display.set_caption("Adventure Game 1")

#Game Settings
frame_rate = 10
velocity = 5
x_offset = 0
y_offset = 0
fall_velocity = 0
fall_acceleration = 0.5
jump_velocity = 0
jump_strength = 20

#Sprite Settings
main_sprite_pos = [win_size[0] / 2, win_size[1] / 2]
main_sprite_size = [50, 50]
main_sprite_color = (128, 96, 77)

#Background Settings
sky_color = (135, 206, 235)
ground_height = 100
ground_color = (131, 105, 83)
grass_color = (145, 203, 125)
surface = win_size[1] - ground_height
grass_height = 30
arc_height = 10

#Game Process
run = True
while run:
    pg.time.delay(frame_rate)       #FPS
    for event in pg.event.get():    #Quit Function
        if event.type == pg.QUIT:
            run = False

    keys = pg.key.get_pressed()
    if keys[pg.K_LEFT]:
        x_offset += velocity
    if keys[pg.K_RIGHT]:
        x_offset -= velocity
    if keys[pg.K_UP]:
        jump_velocity = jump_strength
        main_sprite_pos[1] -= jump_velocity
        fall_velocity = 0

    #gravity
    if jump_velocity > 0:
        jump_velocity -= fall_acceleration
    if main_sprite_pos[1] + (main_sprite_size[1] / 2) < surface - grass_height:
        main_sprite_pos[1] += fall_velocity
        fall_velocity += fall_acceleration

    win.fill(sky_color)
    pg.draw.rect(win,ground_color, (0, surface, win_size[0], ground_height))
    pg.draw.rect(win, grass_color, (0, surface, win_size[0], grass_height))
    for x in range(200):
        pg.draw.arc(win, grass_color, (30 * x + x_offset - (100 * 30), surface + grass_height - 5, grass_height, arc_height), 2.0, 0.0, 5)
    pg.draw.rect(win, main_sprite_color, (main_sprite_pos[0], main_sprite_pos[1], main_sprite_size[0], main_sprite_size[1]))
    pg.display.update()
pg.quit()
