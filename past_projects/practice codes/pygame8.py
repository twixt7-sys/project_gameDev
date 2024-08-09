import pygame as pg
from toolkits import sprites as s
from toolkits import mat as m

pg.init()

# Game Properties
win_size = 900, 900
win = pg.display.set_mode(win_size)
pg.display.set_caption("Hitboxes")
frame_rate = 60

# Making sprites
s1 = s.Sprite((450, 450), (50, 50), 8, (255, 255, 255), 1)

# Making the number matrix
matrix_rect = (50, 50, 100, 100)

# Tolerance for position check
epsilon = 0.5
counted = False

i = 0
run = True
while run:
    pg.time.Clock().tick(frame_rate)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False

    previous_pos = s1.pos[0]
    s1.pos[0], s1.direction = s.oscillate(s1.pos[0], s1.speed, s1.direction, 300, s1.initial_pos[0], 0)

    win.fill((0, 0, 0))
    pg.draw.rect(win, s1.color, (s1.pos[0], s1.pos[1], s1.size[0], s1.size[1]))

    # Check if sprite has crossed the initial position
    if previous_pos < s1.initial_pos[0] <= s1.pos[0] or previous_pos > s1.initial_pos[0] >= s1.pos[0]:
        if not counted:
            i += 1
            counted = True
    else:
        counted = False

    if i >= 10:
        i = 0

    m.paint_matrix(matrix_rect, m.Matrix().num(i), win, (255, 255, 255), (0, 0, 0))
    pg.display.update()

pg.quit()
