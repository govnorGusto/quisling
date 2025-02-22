from actions.action import Action
from settings import *

class Move(Action):
    def __init__(self, owner, action_cost=1):
        super().__init__(owner, action_cost)

    def can_execute(self, dx, dy):
        from player import Player
        if hasattr(self.owner, "stamina"):
            if self.owner.stamina < self.action_cost:
                self.owner.game.message_router.broadcast_message("OutOfStamina")
                return False
        if (
            not self.owner.game.grid.in_bounds(dx, dy)
            or not self.owner.game.grid.map[dx][dy].tile.walkable
        ):
            return False
        occupants = self.owner.game.grid.query_positions([(dx, dy)])
        if occupants:
            if any(isinstance(item, Player) for item in next(iter(occupants.values()))):
                return False
        return True

    def execute(self, dx, dy):
        new_x = self.owner.x + dx
        new_y = self.owner.y + dy
        if not self.can_execute(new_x, new_y):
            return
        
        self.owner.game.message_router.broadcast_message("PlaySFX", SFX_MOVE)

        self.owner.x = new_x
        self.owner.y = new_y
        self.owner.game.grid.move(self.owner, self.owner.x, self.owner.y)
        self.owner.rect.topleft = self.owner.game.grid.grid_to_screen(
            self.owner.x, self.owner.y)
        if hasattr(self.owner, "stamina"):
            self.owner.modify_stamina(-self.action_cost)

            # Set the direction of the character
            if dx > 0:
                self.owner.facing = 1
            if dx < 0:
                self.owner.facing = 3
            if dy > 0:
                self.owner.facing = 2
            if dy < 0:
                self.owner.facing = 0
        self.store(dx, dy)

    def try_execute(self):
        results = {}
        for direction, (dx, dy) in self.directions.items():
            new_x = self.owner.x + dx
            new_y = self.owner.y + dy
            if self.can_execute(new_x, new_y):
                results[direction] = True
            else:
                results[direction] = False
        return results
