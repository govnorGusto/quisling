from actions.action import Action
from core.sprite_object import Sprite_object

VFX_LIFETIME = 0.75

class Spinning_Attack(Action):
    def __init__(self, owner, action_cost=2):
        super().__init__(owner, action_cost)
        self.damage = 1

    def can_execute(self):
        if self.owner.stamina < self.action_cost:
            print("Not enough stamina")
            return False
        return True

    def execute(self):
        if not self.can_execute():
            return
        val = [-1, 0, 1]
        pos_list = []
        for x in val:
            for y in val:
                new_x, new_y = self.owner.x + x, self.owner.y + y
                if x == 0 and y == 0 or not self.owner.game.grid.in_bounds(new_x, new_y):
                    continue
                else:
                    vfx = Sprite_object(new_x, new_y)
                    vfx.lifetime = VFX_LIFETIME
                    pos_list.append((new_x, new_y))

        for _, objects in self.owner.game.grid.query_positions(pos_list).items():
            for obj in objects:
                if hasattr(obj, "health"):
                    self.take_damage(obj, self.damage)

        self.owner.modify_stamina(-self.action_cost)
        self.store()
