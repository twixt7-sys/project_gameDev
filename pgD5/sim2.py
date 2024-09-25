import GameObj as g
import LoopClass as l
import math
import random as r

g1 = g.Game()

g1.set_window()

#instantiate in-game objects
loop = l.Loop(g1)

class Processes:
    def process1():
        # Transmit Particles
        
        g1.pyg.draw.circle(g1.win, (255, 0, 0), g1.center, 50.0)

class Particle(object):
    def __init__(self, pos, size, speed, dir = 0, color = (0, 0, 0), radius = 50):
        self.pos = pos
        self.size = size
        self.color = color
        self.radius = radius
        self.speed = speed
        self.dir = dir
        
    def update_particle(self):
        self.pos[0] += self.speed[0]
        self.pos[1] += self.speed[1]

while(g1.run):
    loop.set_loop()
    loop.set_events()
    loop.set_background()

    #insert code process as a method
    Processes.process1()

    loop.update_display()
    g1.clock.tick(g1.frame_rate)

g1.quit()

