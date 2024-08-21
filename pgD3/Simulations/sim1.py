#importing folder for whole project using absolute path
import os
import sys
sys.path.append(os.path.abspath('pgD3'))

#importing other classes
import Tools.game_dir.GameClass as g
import Tools.game_dir.Loop as l
import Tools.game_dir.Environment as e
import Tools.Dictionary as d
import Tools.Matrix as m

#creating game object
g1 = g.Game()
g1.set_window()

#setup loop and dictionary instance
loop, env, dic = l.Loop(g1), e.Environment(g1), d.Dictionary()

#make matrix field
field1 = m.MatrixField(g1)

#set environment
env.enable_all()

#game loop
while g1.run:
    loop.set_loop()
    loop.set_events()
    loop.set_background()
    field1.draw_matrix_field("Hello World", g1.center)
    loop.update_display()
g1.quit()