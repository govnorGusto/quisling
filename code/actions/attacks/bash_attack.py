from actions.action import Action
from core.sprite_object import Sprite_object

class Bash_Attack(Action):
    def __init__(self, owner, action_cost=1):
        super().__init__(owner, action_cost)
        self.damage = 2

    def can_execute(self):
        if self.owner.stamina < self.action_cost:
            print("Not enough stamina")
            return False
        return True

    def execute(self):
        self.can_execute()
        facing = self.get_direction(self.owner.facing)
        new_x, new_y = self.owner.x + facing[0], self.owner.y + facing[1]
        if self.owner.game.grid.in_bounds(new_x, new_y):
            Sprite_object(new_x, new_y)
            for _, objects in self.owner.game.grid.query_positions([(new_x, new_y)]).items():
                for obj in objects:
                    if hasattr(obj, "health"):
                        self.take_damage(obj, self.damage)

        self.owner.stamina -= self.action_cost

    def __repr__(self):
        return "bash_attack"