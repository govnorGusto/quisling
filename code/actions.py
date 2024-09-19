import abc
from core.game_object import Game_object

# class Action(abc.ABC):
#     def __init__(self, action_cost):
#         self.action_cost = action_cost

#     @abc.abstractmethod
#     def execute(self):
#         pass


class Action(Game_object):
    def __init__(self, action_cost):
        super().__init__()

        self.action_cost = action_cost

    def execute(self):
        pass


class Move(Action):
    def __init__(self, action_cost=1):
        super().__init__(action_cost)

    def execute(self, obj, dx, dy):
        if hasattr(obj, "stamina"):
            if obj.stamina < self.action_cost:
                print("Not enough stamina")
            else:
                obj.stamina -= self.action_cost
                self.move(obj, dx, dy)
        else:
            self.move(obj, dx, dy)

    def move(self, obj, dx, dy):
        new_x = obj.x + dx
        new_y = obj.y + dy
        if (
            self.game.grid.in_bounds(new_x, new_y)
            and self.game.grid.map[new_x][new_y].tile.walkable
        ):
            obj.x = new_x
            obj.y = new_y
            self.game.grid.move(obj, obj.x, obj.y)
            obj.rect.topleft = self.game.grid.grid_to_screen(obj.x, obj.y)


class MoveAction(Action):
    def __init__(self, player, dx, dy, action_cost=1):
        super().__init__(action_cost)
        self.player = player
        self.dx = dx
        self.dy = dy
        self.execute()

    def execute(self):
        """Execute the move action."""
        self.player.rect.x += self.dx
        self.player.rect.y += self.dy
        if self.dx > 0:
            self.player.facing = 1
        if self.dx < 0:
            self.player.facing = 3
        if self.dy > 0:
            self.player.facing = 2
        if self.dy < 0:
            self.player.facing = 0


class MeleeAttackAction(Action):
    def __init__(self, player, target, attack_damage=1, action_cost=1):
        super().__init__(action_cost)
        self.player = player
        self.target = target
        self.attack_damage = attack_damage
        self.execute()

    def execute(self):
        """Execute a basic melee attack without animation."""
        self.target.health -= self.attack_damage
        self.player.action_points -= self.action_cost

    def execute_with_animation(self):
        pass
