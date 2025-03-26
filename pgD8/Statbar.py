import pygame as pg

class StatBar:
    def __init__(self, pos=[0, 0], stats=None, bar_width=1, bar_height=5, spacing=5):
        self.pos = pos
        self.stats = stats or []  # List of (color, value)
        self.bar_width = bar_width
        self.bar_height = bar_height
        self.spacing = spacing

    def draw(self, screen):
        for i, (color, value) in enumerate(self.stats):
            bar_rect = (self.pos[0], self.pos[1] + (i * self.spacing), value * self.bar_width, self.bar_height)
            pg.draw.rect(screen, color, bar_rect)
    
    def set_stats(self, stats):
        self.stats = stats
