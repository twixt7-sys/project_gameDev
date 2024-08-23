#importing folder for whole project using absolute path
import os
import sys
sys.path.append(os.path.abspath('pgD3'))

#importing other classes
import Tools.game_dir.GameClass as g
import Tools.game_dir.Loop as l
import Tools.game_dir.Environment as en
import Tools.Dictionary as d
import Tools.Matrix as m
import Objects.Entity as e
import Objects.Sprite_g3 as s

#creating game object
g1 = g.Game()
g1.set_window()

#setup loop and dictionary instance
loop, env, dic = l.Loop(g1), en.Environment(), d.Dictionary()
g1.environment = env

#make matrix field
gravity = m.Matrix(g1)
velocity = m.Matrix(g1)
grav_num = m.Matrix(g1)
vel_num = m.Matrix(g1)

#make sprite
e1 = e.Entity(g1, g1.center)
s1 = s.SpriteG3(e1)

#set environment
env.enable_all()

#game loop
while g1.run:
    loop.set_loop()
    loop.set_events()
    loop.set_background()

    gravity.draw_matrix_field("state: ", [125, 50,], 5)
    velocity.draw_matrix_field("velocity: ", [50, 100], 5)

    g_val = str(env.grav_val)
    v_val = str(chr(e1.velocity[0]))
    grav_num.draw_matrix_field(g_val, [350, 50], 5)
    vel_num.draw_matrix_field(v_val, [350, 50], 5)
    
    s1.move()

    loop.update_display()
g1.quit()