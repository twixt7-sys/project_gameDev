import pygame as pg

class Animation:
    def __init__(self, path, time, frame_rate, grid, res=[32, 32]):
        self.original_frames = self.load_frames(path, grid, res)
        self.frames = self.original_frames[:]
        self.frame_rate = frame_rate
        self.time = time
        self.current_frame = 0
        self.start_time = time.get_ticks()

        # Trail effect attributes
        self.trail = []  
        self.trail_lifespan = 10  
        self.max_alpha = 200  

    def update(self):
        self.current_frame = (self.time.get_ticks() - self.start_time) // self.frame_rate
        if self.current_frame >= len(self.frames):
            self.current_frame = 0
            self.start_time = self.time.get_ticks()

    def draw(self, surface, pos):
        surface.blit(self.frames[self.current_frame], pos)

    def animate(self, surface, pos, dashing=False):
        self.update()
        self.draw_trail(surface)
        if dashing:
            self.make_trail(pos)  # Only create a trail when dashing
        self.draw(surface, pos)

    def make_trail(self, pos):
        """ Creates a fading trail effect when dashing """
        afterimage = self.frames[self.current_frame].copy()
        self.trail.append([afterimage, pos[:], self.trail_lifespan])

    def draw_trail(self, surface):
        for img in self.trail:
            alpha = int((img[2] / self.trail_lifespan) * self.max_alpha)
            img[0].set_alpha(alpha)
            surface.blit(img[0], img[1])
            img[2] -= 1  

        self.trail = [img for img in self.trail if img[2] > 0]

    def load_frames(self, path, grid, res):
        sheet = pg.image.load(path).convert_alpha()
        frames = []
        for y in range(grid[0]):
            for x in range(grid[1]):
                frame = pg.Surface((res[0], res[1]), pg.SRCALPHA)
                frame.blit(sheet, (-x * res[0], -y * res[1]))
                frames.append(frame)
        return frames

    def flip_frames(self, flip_x=True, flip_y=False):
        self.frames = [pg.transform.flip(frame, flip_x, flip_y) for frame in self.original_frames]
