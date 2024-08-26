import __init__ as init

g1 = init.g.Game()
g1.set_window()
d = init.dic.Dictionary()

e = init.env.Environment()
g1.environment = e
logic = init.log.GameLogics(g1)
g1.logic = logic

main_sprite = init.ent.Entity(g1, g1.center, [20, 20], 0.1, d.color[d.DARK_GREY])
main_sprite.is_controllable = True

loop = init.lp.Loop(g1)

while g1.run:
    loop.set_loop()
    loop.set_events()
    loop.set_background(d.color[d.LIGHT_GREY])
    main_sprite.update() 
    loop.update_display()
g1.quit()
