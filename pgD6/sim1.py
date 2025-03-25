import pygame as pg
import S4 as s

pg.init()

# Set up display
win_size = [900, 900]
win = pg.display.set_mode(win_size)
pg.display.set_caption("Animated Sprite")
win_center = (win_size[0] // 2, win_size[1] // 2)

# Initialize sprite
s1 = s.AnimatedSprite("pgD6/Sprite-4.png", sprite_rect=[0, 0, 64, 32], frame_rate=100, loop=True)

run = True
clock = pg.time.Clock()

while run:
    clock.tick(60)  # Cap the frame rate at 60 FPS
    current_time = pg.time.get_ticks()

    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False

    # Update sprite animation
    s1.update(current_time)

    # Clear screen and draw sprite
    win.fill((0, 0, 0))
    s1.draw(win, win_center)  # Draw at the center of the window
    pg.display.update()

pg.quit()
