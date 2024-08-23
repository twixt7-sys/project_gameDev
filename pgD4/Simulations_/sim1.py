import __init__ as init

g1 = init.g.Game()
g1.set_window()

e = init.env.Environment()
g1.environment = e
l = init.log.G_logics(g1)
g1.logic = l

main_sprite = init.ent.Entity(g1, g1.center)
main_sprite.is_controllable = True

d = init.dic.Dictionary()
loop = init.lp.Loop(g1)

while g1.run:
    loop.set_loop()
    loop.set_events()
    loop.set_background(d.color[d.LIGHT_GREY])
    main_sprite.update()
    loop.update_display()
g1.quit()
