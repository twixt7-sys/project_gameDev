import pygame as pg

class Animation:
    #Animation utility class for game development.
    def __init__(self, frames, frame_rate, time):
        self.frames = frames
        self.frame_rate = frame_rate
        self.time = time
        self.current_frame = 0
        self.start_time = time.get_ticks()
    def update(self):
        self.current_frame = (self.time.get_ticks() - self.start_time) // self.frame_rate
        if self.current_frame >= len(self.frames):
            self.current_frame = 0
            self.start_time = self.time.get_ticks()
    def draw(self, surface, pos):
        surface.blit(self.frames[self.current_frame], pos)
    def animate(self, surface, pos):
        self.update()
        self.draw(surface, pos)
    def load_frames(path, rows, cols, width, height):
        sheet = pg.image.load(path).convert_alpha()
        frames = []
        for y in range(rows):
            for x in range(cols):
                frame = pg.Surface((width, height)).convert_alpha()
                frame.blit(sheet, (-x * width, -y * height))
                frames.append(frame)
        return frames