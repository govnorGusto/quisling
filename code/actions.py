
class Action:
    def __init__(self, owner, action_cost:int):

        self.owner = owner
        self.action_cost = action_cost
    
    def can_execute(self):
        pass

    def execute(self):
        pass

    def try_execute(self):
        pass


class Move(Action):
    def __init__(self, owner, action_cost=1):
        super().__init__(owner, action_cost)

    def can_execute(self, dx, dy):
        if hasattr(self.owner, "stamina"):
            if self.owner.stamina < self.action_cost:
                print("Not enough stamina")
                return False
        if not (
            self.owner.game.grid.in_bounds(dx, dy)
            and self.owner.game.grid.map[dx][dy].tile.walkable
        ):
            return False
        return True

    def execute(self, dx, dy):
        new_x = self.owner.x + dx
        new_y = self.owner.y + dy
        if self.can_execute(new_x, new_y):
            self.owner.x = new_x
            self.owner.y = new_y
            self.owner.game.grid.move(self.owner, self.owner.x, self.owner.y)
            self.owner.rect.topleft = self.owner.game.grid.grid_to_screen(self.owner.x, self.owner.y)
            if hasattr(self.owner, "stamina"):
                self.owner.stamina -= self.action_cost
                
                # Set the direction of the character
                if dx > 0:
                    self.owner.facing = 1
                if dx < 0:
                    self.owner.facing = 3
                if dy > 0:
                    self.owner.facing = 2
                if dy < 0:
                    self.owner.facing = 0

    def try_execute(self):
        directions = {"up": (0, -1), "down": (0, 1), "left": (-1, 0), "right": (1, 0)}
        results = {}
        for direction, (dx, dy) in directions.items():
            new_x = self.owner.x + dx
            new_y = self.owner.y + dy
            if self.can_execute(new_x, new_y):
                results[direction] = True
            else:
                results[direction] = False
        return results
    
    def __repr__(self):
        return "Move_action"



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
