import abc


class Action(abc.ABC):
    def __init__(self, action_cost):
        self.action_cost = action_cost
    
    @abc.abstractmethod
    def execute(self):
        pass
    
    
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