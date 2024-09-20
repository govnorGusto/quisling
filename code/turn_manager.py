from settings import *
from player import Player
from core.game_object import Game_object


class Turn_Manager(Game_object):
    def __init__(self) -> None:
        super().__init__()

        self.selected_player = 0
        self.player_list = []

        self.resolve = False

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
            self.resolve = True
        
        self.game.message_router.broadcast_message("PlayerChanged", self.selected_player + 1)
        self.game.message_router.broadcast_message("StaminaChanged", self.get_current_player().stamina)

    def on_update(self, delta_time):
        if self.resolve:
            self.game.resolve.resolve_moves()
