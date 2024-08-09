import pygame as pg
pg.init()

class Sprite(object):
    def __init__(self, pos, size, speed, color, direction):
        self.pos = list(pos)
        self.size = size
        self.speed = speed
        self.color = color
        self.direction = direction

class Action(object):
    def oscillate(self, pos, speed, direction, osc_range):
        range1 = pos - osc_range
        range2 = pos + osc_range
        if pos <= range1 or pos >= range2:
            direction *= -1
        new_pos = pos + speed * direction
        return new_pos, direction

#window properties
win_size = 900, 900
win_x_center = int(win_size[0] / 2)
win_y_center = int(win_size[1] / 2)
win_center =  win_x_center, win_y_center
win = pg.display.set_mode(win_size)

#game properties
speed = 10
frame_rate = 60
sprite_size = 50, 50
bg_color = 0, 0, 0
sprite_color = 255, 255, 255
osc_range = 50

#initializations
main_sprite = Sprite((win_center[0] - (sprite_size[0] / 2), win_center[1] - (sprite_size[1] / 2)), sprite_size, speed, sprite_color, 1)

#game process
run = True
while run:
    pg.time.Clock().tick(frame_rate)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False
    
    #game actions
    main_sprite.pos[0], main_sprite.direction = Action().oscillate(main_sprite.pos[0], speed, main_sprite.direction, osc_range)
    
    win.fill(bg_color)
    pg.draw.rect(win, sprite_color, (int(main_sprite.pos[0]), int(main_sprite.pos[1]), sprite_size[0], sprite_size[1]))
    pg.display.update()
pg.quit()