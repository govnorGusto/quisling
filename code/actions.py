from core.sprite_object import Sprite_object


class Action:
    def __init__(self, owner, action_cost: int):

        self.owner = owner
        self.action_cost = action_cost
        self.directions = {"up": (0, -1), "down": (0, 1),
                           "left": (-1, 0), "right": (1, 0)}

    def can_execute(self):
        pass

    def execute(self):
        pass

    def try_execute(self):
        pass

    def get_direction(self, direction):
        match direction:
            case 0:
                return self.directions["up"]
            case 1:
                return self.directions["right"]
            case 2:
                return self.directions["down"]
            case 3:
                return self.directions["left"]
    
    def take_damage(self, obj, damage):
        if self.owner.game.turn_manager.resolve:
            obj.health -= damage
        else:
            print(f"{obj} has taken {damage} damage")


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
            self.owner.rect.topleft = self.owner.game.grid.grid_to_screen(
                self.owner.x, self.owner.y)
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
        results = {}
        for direction, (dx, dy) in self.directions.items():
            new_x = self.owner.x + dx
            new_y = self.owner.y + dy
            if self.can_execute(new_x, new_y):
                results[direction] = True
            else:
                results[direction] = False
        return results

    def __repr__(self):
        return "Move_action"


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


class Spinning_Attack(Action):
    def __init__(self, owner, action_cost=1):
        super().__init__(owner, action_cost)
        self.damage = 1

    def can_execute(self):
        if self.owner.stamina < self.action_cost:
            print("Not enough stamina")
            return False
        return True

    def execute(self):
        self.can_execute()
        val = [-1, 0, 1]
        pos_list = []
        for x in val:
            for y in val:
                new_x, new_y = self.owner.x + x, self.owner.y + y
                if x == 0 and y == 0 or not self.owner.game.grid.in_bounds(new_x, new_y):
                    continue
                else:
                    Sprite_object(new_x, new_y)
                    pos_list.append((new_x, new_y))

        for _, objects in self.owner.game.grid.query_positions(pos_list).items():
            for obj in objects:
                if hasattr(obj, "health"):
                    self.take_damage(obj, self.damage)

        self.owner.stamina -= self.action_cost

    def __repr__(self):
        return "spinning_attack"
