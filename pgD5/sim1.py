import GameObj as g
import LoopClass as l
import math
import random as r

g1 = g.Game()

g1.set_window()

#instantiate in-game objects
loop = l.Loop(g1)
color, color_increment = 0, 4 * 1
radius, radius_increment = 0, 4 * 3

#Sinusoidal ease effect

min_radius, max_radius = 0, 255 * 2  # Range for radius (0 to 510)
A = (max_radius + min_radius) / 2  # Center of the radius range
B = (max_radius - min_radius) / 2  # Amplitude (half the range)

t = 0  # Time or frame count for easing
T = 120  # Number of frames for a full cycle (adjust based on desired speed)

while(g1.run):
    loop.set_loop()
    loop.set_events()
    loop.set_background()
    
    radius = A + B * math.sin((t / T) * math.pi)
    
    color = 200 if color > 200 else (color)
    color = 0 if color < 0 else (color)
    
    g1.pyg.draw.circle(g1.win, (color * 0.1, color* 0.1, color * 0.3), g1.center, radius/200 * 100 * 2)
    
    g1.pyg.draw.circle(g1.win, (color * 0.5, color* 0.5, color * 0.6), g1.center, radius/200 * 100)

    for i in range(0, 3):
        g1.pyg.draw.circle(g1.win, (color, color, color), [250 + (i * 200), g1.center[1]], radius/200 * 100 / 4 + r.randrange(0, 10))

    color += color_increment 
    if color >= 200 or color <= 0:
        color_increment *= -1

    radius += radius_increment
    if radius >= 200*2 or radius <= 0:
        radius_increment *= -1

    t += 1
    if t > T:
        t = 0  # Reset the time after one full cycle

    loop.update_display()
    g1.clock.tick(g1.frame_rate)

g1.quit()