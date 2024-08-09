import pygame as pg

pg.init()

class Sprite:
    def __init__(self, pos, size, speed, color, direction):
        self.pos = list(pos)
        self.start_pos = self.pos.copy()
        self.size = size
        self.speed = speed
        self.color = color
        self.direction = direction
        self.osc_range = 300
    
    def oscillate(self, axis, speed):
        range1 = self.start_pos[axis] - self.osc_range
        range2 = self.start_pos[axis] + self.osc_range

        if self.pos[axis] <= range1 or self.pos[axis] >= range2:
            self.direction *= -1
        
        side = 1 if self.pos[axis] <= self.start_pos[axis] else -1
        
        if self.direction == -1 and side == 1:  # ease-out-left
            x1, x2, y1, y2 = self.start_pos[axis], range1, self.speed, 1
        if self.direction == 1 and side == 1:  # ease-in-left
            x1, x2, y1, y2 = range1, self.start_pos[axis], 1, self.speed
        if self.direction == 1 and side == -1:  # ease-out-right
            x1, x2, y1, y2 = self.start_pos[axis], range2, self.speed, 1
        if self.direction == -1 and side == -1:  # ease-in-right
            x1, x2, y1, y2 = range2, self.start_pos[axis], 1, self.speed

        Rise = y2 - y1
        Run = x2 - x1
        slope = Rise / Run if Run != 0 else 0
        osc_speed = slope * (self.pos[axis] - x1) + y1

        # Ensure a minimum speed to avoid stopping
        min_speed = 1
        self.pos[axis] += max(osc_speed, min_speed) * self.direction * speed

# Window properties
win_size = 900, 900
win_x_center = int(win_size[0] / 2)
win_y_center = int(win_size[1] / 2)
win_center = win_x_center, win_y_center
win = pg.display.set_mode(win_size)

# Game properties
speed = 10
frame_rate = 60
sprite_size = 50, 50
bg_color = 50, 50, 100
sprite_color = 150, 150, 225

# Initializations
x_sprite = Sprite((win_center[0] - (sprite_size[0] / 2), win_center[1] - (sprite_size[1] / 2)), sprite_size, speed, sprite_color, -1)
y_sprite = Sprite((win_center[0] - (sprite_size[0] / 2), win_center[1] - (sprite_size[1] / 2)), sprite_size, speed, sprite_color, 1)
xy_sprite1 = Sprite((win_center[0] - (sprite_size[0] / 2), win_center[1] - (sprite_size[1] / 2)), sprite_size, speed, sprite_color, 1)
xy_sprite2 = Sprite((win_center[0] - (sprite_size[0] / 2), win_center[1] - (sprite_size[1] / 2)), sprite_size, speed, sprite_color, 1)

# Game process
run = True
while run:
    pg.time.Clock().tick(frame_rate)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False
    
    # Game actions
    x_sprite.oscillate(0, 5)
    y_sprite.oscillate(1, 5)
    xy_sprite1.oscillate(0, 5)

    # draw
    win.fill(bg_color)
    pg.draw.rect(win, sprite_color, (int(x_sprite.pos[0]), int(x_sprite.pos[1]), sprite_size[0], sprite_size[1]))
    pg.draw.rect(win, sprite_color, (int(y_sprite.pos[0]), int(y_sprite.pos[1]), sprite_size[0], sprite_size[1]))
    pg.draw.rect(win, sprite_color, (int(xy_sprite1.pos[0]), int(xy_sprite1.pos[0]), sprite_size[0], sprite_size[1]))
    pg.display.update()

pg.quit()
