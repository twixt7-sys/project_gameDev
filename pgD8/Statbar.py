import pygame as pg

class StatBar:
    def __init__(self, width=100, height=5, spacing=5):
        self.pos = (0, 0)  
        self.stats = []
        self.width = width  # Default bar width
        self.height = height  # Default bar height
        self.spacing = spacing  # Spacing between bars

    def draw(self, screen, color=(255, 255, 255)):
        for i, stat in enumerate(self.stats):
            bar_rect = (self.pos[0], self.pos[1] + (i * (self.height + self.spacing)), 
                        stat * self.width, self.height)
            
            # Ensure color is valid
            bar_color = color[i] if isinstance(color, list) and i < len(color) else color
            
            pg.draw.rect(screen, bar_color, bar_rect)

    def update(self, stats, pos):
        self.stats, self.pos = stats, pos
