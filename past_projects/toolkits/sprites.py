import pygame as pg
pg.init()

class Sprite:
    def __init__(self, pos, size, speed, color, direction):
        self.pos = list(pos)
        self.size = size
        self.speed = speed
        self.color = color
        self.direction = direction
        self.initial_pos = list(pos)

def oscillate(pos, speed, direction, osc_range, initial_pos, axis):
    range1 = initial_pos - osc_range
    range2 = initial_pos + osc_range

    if pos <= range1 or pos >= range2:
        direction *= -1

    side = 1 if pos <= initial_pos else -1

    if direction == -1 and side == 1:  # ease-out-left
        x1, x2, y1, y2 = initial_pos, range1, speed, 1
    elif direction == 1 and side == 1:  # ease-in-left
        x1, x2, y1, y2 = range1, initial_pos, 1, speed
    elif direction == 1 and side == -1:  # ease-out-right
        x1, x2, y1, y2 = initial_pos, range2, speed, 1
    elif direction == -1 and side == -1:  # ease-in-right
        x1, x2, y1, y2 = range2, initial_pos, 1, speed

    Rise = y2 - y1
    Run = x2 - x1
    slope = Rise / Run if Run != 0 else 0
    osc_speed = slope * (pos - x1) + y1

    min_speed = 1
    pos += max(osc_speed, min_speed) * direction * speed

    return pos, direction