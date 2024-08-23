# sprites are controllable

class SpriteG3():
    def __init__(self, entity):
        self.ent = ent = entity
        keys = ent.game.pyg.key.get_pressed()
        up = keys[ent.game.pyg.K_UP]
        down = keys[ent.game.pyg.K_DOWN]
        left = keys[ent.game.pyg.K_LEFT]
        right = keys[ent.game.pyg.K_RIGHT]
        self.movement_keys=[up, down, left, right]

    def move(self):
        speed = self.ent.movement_speed
        if self.movement_keys[0]:
            print("Moved up")
            SpriteG3.move_up(speed)
        if self.movement_keys[1]:
            print("Moved down")
            SpriteG3.move_down(speed)
        if self.movement_keys[2]:
            print("Moved left")
            SpriteG3.move_left(speed)
        if self.movement_keys[3]:
            print("Moved right")
            SpriteG3.move_right(speed)

    def move_up(self, speed):
        self.ent.acceleration[1] = speed
        self.ent.velocity[1] -= self.ent.acceleration[1]
    def move_down(self, speed):
        self.ent.acceleration[1] = speed
        self.ent.velocity[1] += self.ent.acceleration[1]
    def move_left(self, speed):
        self.ent.acceleration[0] = speed
        self.ent.velocity[0] -= self.ent.acceleration[0]
    def move_right(self, speed):
        self.ent.acceleration[0] = speed
        self.ent.velocity[0] += self.ent.acceleration[0]