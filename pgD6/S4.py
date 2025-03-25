import pygame as pg

class AnimatedSprite:
    def __init__(self, sprite_sheet, sprite_rect=[0, 0, 64, 32], frame_rate=100, loop=True):
        self.sprite_sheet = pg.image.load(sprite_sheet).convert_alpha()
        self.sprite_rect = sprite_rect
        self.frame_rate = frame_rate
        self.loop = loop
        self.frames = []
        self.frame = 0
        self.last_update = 0  # For tracking animation time

        self.extract_frames()

    def extract_frames(self):
        """Extract frames from the sprite sheet."""
        sheet_width, sheet_height = self.sprite_sheet.get_size()
        frame_width, frame_height = self.sprite_rect[2], self.sprite_rect[3]

        if frame_width > sheet_width or frame_height > sheet_height:
            raise ValueError(f"Frame size {frame_width}x{frame_height} exceeds sprite sheet size {sheet_width}x{sheet_height}")

        for x in range(0, sheet_width, frame_width):
            frame_rect = pg.Rect(x, 0, frame_width, frame_height)
            self.frames.append(self.sprite_sheet.subsurface(frame_rect))

        if not self.frames:
            raise ValueError("No frames extracted! Check sprite sheet dimensions.")

    def next_frame(self):
        """Advance to the next animation frame."""
        self.frame += 1
        if self.frame >= len(self.frames):
            if self.loop:
                self.frame = 0
            else:
                self.frame = len(self.frames) - 1

    def update(self, current_time):
        """Update the animation frame based on time."""
        if current_time - self.last_update > self.frame_rate:
            self.last_update = current_time
            self.next_frame()

    def draw(self, win, pos):
        """Draw the current frame at a given position."""
        win.blit(self.frames[self.frame], pos)
