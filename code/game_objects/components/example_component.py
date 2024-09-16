from core.game_object import Component

class Example_Component(Component):
    def update(self, delta_time: float):
        self.print()
