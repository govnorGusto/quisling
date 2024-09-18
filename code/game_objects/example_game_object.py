from genericpath import samefile
from core.game_object import Game_object
from game_objects.components.example_component import Example_Component

class Example_Game_Object(Game_object):
    def __init__(self, msg):
        super().__init__(self)
        self.msg = msg
        
        self.add_component(Example_Component)

    def update(self, delta_time):
       super(Example_Game_Object, self).update(delta_time)
       pass
