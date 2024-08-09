import pygame as pg
pg.init()

#Coordinate System v1

win_size = 900, 900
x_center = win_size[0] / 2
y_center = win_size[1] / 2
center = x_center, y_center
win = pg.display.set_mode(win_size)
pg.display.set_caption("Coordinate System v1")

#Initializations

class sprite(object):
    def __init__(self, name, pos, size):
        self.name = name
        self.pos = list(pos)
        self.size = size
        self.direction = 1  # To keep track of movement direction

s1 = sprite("Sprite 1", (center), 50) #when dividing integers it might turn into floats so be careful with that
s2 = sprite("Sprite 2", (x_center, y_center - 100), 50)
s3 = sprite("Sprite 2", (x_center, y_center + 100), 50)

def oscillate(pos, speed, range_val, direction):
    range1 = (x_center) - range_val
    range2 = (x_center) + range_val

    if pos <= range1 or pos >= range2:
        direction *= -1

    new_pos = pos + speed * direction
    return new_pos, direction

run = True
while run:
    pg.time.Clock().tick(60)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False

    #oscillate sprite 1 x position
    s1.pos[0], s1.direction = oscillate(s1.pos[0], 11, 250, s1.direction)
    s2.pos[0], s2.direction = oscillate(s2.pos[0], 10, 250, s2.direction)
    s3.pos[0], s3.direction = oscillate(s3.pos[0], 12, 250, s3.direction)

    win.fill((0, 0, 0))
    pg.draw.rect(win, (100, 100, 255), (int(s1.pos[0]), int(s1.pos[1]), s1.size, s1.size))
    pg.draw.rect(win, (50, 50, 255), (int(s2.pos[0]), int(s2.pos[1]), s2.size, s2.size))
    pg.draw.rect(win, (150, 150, 255), (int(s3.pos[0]), int(s3.pos[1]), s3.size, s3.size))
    pg.display.update()
pg.quit()
