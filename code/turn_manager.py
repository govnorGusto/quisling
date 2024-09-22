from hmac import new
from random import randint
from secrets import randbits
from settings import *
from player import Player
from core.game_object import Game_object
from resolve import Resolve
from uu import Error

class Turn_Manager(Game_object):
    def __init__(self) -> None:
        super().__init__()

        self.selected_player = 0
        self.player_list = []
        self.is_resolving = False
        self.game.message_router.register_callback("ResolveOver", self.end_resolve)

    def get_current_player(self):
        return self.player_list[self.selected_player]

    def spawn_players(self, invalid_spawns):
        """add list of players"""
        grid_max_x = self.game.grid.width
        grid_max_y = self.game.grid.height
        p1_spawn = (1, 1)
        p2_spawn = (grid_max_x - 2, grid_max_y - 2)
        
        spawn_positions = (sanitise_spawn_locations(p1_spawn, invalid_spawns, (1, 1)), sanitise_spawn_locations(p2_spawn, invalid_spawns, (-1, -1)))
        
        for i in range(PLAYER_AMOUNT):
            x, y = spawn_positions[i][0], spawn_positions[i][1]
            p = Player(x, y, i)
            self.game.message_router.broadcast_message("HealthChanged" , (i, p.health))
            self.player_list.append(p)
            
        self.game.message_router.broadcast_message("StaminaChanged", self.get_current_player().stamina)
        self.game.message_router.broadcast_message("PlayerChanged", self.selected_player + 1)
            
    def change_player(self):
        """change player and triggers action round"""
        self.get_current_player().reset_position()
        if self.selected_player < len(self.player_list) -1:
            self.selected_player += 1
        else:
            self.selected_player = 0
            self.is_resolving = True
            self.game.message_router.broadcast_message("ResolvePhase", 0)
            Resolve(self.player_list[0].stored_actions, self.player_list[1].stored_actions)
            self.game.message_router.broadcast_message("StaminaChanged", self.get_current_player().stamina)
            return
        
        self.game.message_router.broadcast_message("PlayerChanged", self.selected_player + 1)
        self.game.message_router.broadcast_message("StaminaChanged", self.get_current_player().stamina)
        
    def end_resolve(self, data):
        if not self.is_resolving:
            raise Error("End resolve event recieved while not resolving")
        
        self.is_resolving = False
        self.game.message_router.broadcast_message("PlayerChanged", self.selected_player + 1)
        
def sanitise_spawn_locations(pos : list, invalid_spawns : list, direction : tuple):
    if pos not in invalid_spawns:
        print(f"Accepted Spawn: {pos}")
        return pos
    newx = pos[0]
    newy = pos[1]
    if randint(0, 1) == 0:
        newx += direction[0]
    else:
        newy += direction[1]
     
    print(f"Adjusted Spawn: {pos} to: {(newx, newy)}")
    return sanitise_spawn_locations((newx, newy), invalid_spawns, direction) 
