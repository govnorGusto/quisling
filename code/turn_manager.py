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

    def get_players(self):
        """add list of players"""
        x = 1
        y = 1
        for i in range(PLAYER_AMOUNT):
            p = Player(x, y, i)
            self.game.message_router.broadcast_message("HealthChanged" , (i, p.health))
            self.player_list.append(p)
            x += 1
            y += 1
            
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
