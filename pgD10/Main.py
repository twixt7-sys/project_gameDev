import i

def __main__():
    i.init()

    while i.running:
        for event in i.pg.event.get():
            if event.type == i.pg.QUIT:
                i.running = False

        i.WIN.fill((0, 0, 0))

        i.CLOCK.tick(i.FPS)
        i.pg.display.update()
        i.pg.display.flip()

    i.pg.quit()

__main__()