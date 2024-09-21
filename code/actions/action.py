from settings import SFX_DAMAGE

class Action:
    def __init__(self, owner, action_cost: int):

        self.owner = owner
        self.action_cost = action_cost
        # self.directions = {"up": (0, -1), "down": (0, 1),
        #                    "left": (-1, 0), "right": (1, 0)}
        # This feels like a more natural move pattern
        self.directions = {
            "up": (1, 0),
            "down": (-1, 0),
            "left": (0, -1),
            "right": (0, 1),
        }

    def can_execute(self):
        pass

    def execute(self):
        pass

    def try_execute(self):
        pass

    def get_direction(self, direction):
        match direction:
            case 0:
                return self.directions["left"]
            case 1:
                return self.directions["up"]
            case 2:
                return self.directions["right"]
            case 3:
                return self.directions["down"]

    def take_damage(self, obj, damage):
        if self.owner.game.turn_manager.is_resolving:
            obj.modify_health(-damage)
            self.owner.game.message_router.broadcast_message("PlaySFX", SFX_DAMAGE)
                        
    def store(self, *args):
        if hasattr(self.owner, "stored_actions"):
            self.owner.store_action(self, *args)
