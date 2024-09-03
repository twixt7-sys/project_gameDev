import sys
import os
sys.path.append(os.path.abspath('pgD4'))

from Game_.GameObj_ import GameObj as g
from Tools_ import DictionaryClass as d
from Game_.GameObj_ import EnvironmentClass as env
from Game_.GameLogics_ import GameLogicsClass as log
from Game_.Entity_ import EntityClass as ent
from Game_.GameObj_ import LoopClass as lp

g1 = g.Game()
g1.set_window()
d = d.Dictionary()

e = env.Environment()
g1.environment = e
logic = log.GameLogics(g1)
g1.logic = logic

main_sprite = ent.Entity(g1, g1.center, [20, 20], 0.02, d.color[d.DARK_GREY])
main_sprite.is_controllable = True

loop = lp.Loop(g1)

while g1.run:
    loop.set_loop()
    loop.set_events()
    loop.set_background(d.color[d.LIGHT_GREY])
    main_sprite.update()
    loop.update_display()
g1.quit()
