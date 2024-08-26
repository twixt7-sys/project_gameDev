import AttributesClass
import MethodsClass

class Entity(object):
    def __init__(self, game, center, size=[10, 10], movement_speed=0.1, color=(255, 255, 255)):
        self.game = game
        initialize = AttributesClass.Attributes()
        initialize.positional_attributes(size, center)
        initialize.movement_attributes(movement_speed)
        initialize.visual_attributes(color)
        initialize.states(self)

    def update(self):
        Entity.apply_states(self)
        Entity.update_position(self)
        Entity.draw_sprite(self)
    
    def apply_states(self):
        MethodsClass.Methods().apply_states(self)
    
    def update_position(self):
        MethodsClass.Methods().update_position(self)

    def draw_sprite(self):
        self.game.pyg.draw.rect(self.game.win, self.color, self.rect_val)

    def move(self):
        MethodsClass.Methods().move(self)

    def update_keypress(self):
        MethodsClass.Methods().update_keypress(self)