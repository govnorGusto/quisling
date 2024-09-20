from settings import *
from player import Player
from core.game_object import Game_object


class Turn_Manager(Game_object):
    def __init__(self) -> None:
        super().__init__()

        self.selected_player = 0
        self.player_list = []

        self.resolve = False
        self.current_round = 0

    def get_current_player(self):
        return self.player_list[self.selected_player]

    def get_players(self):
        """add list of players"""
        x = 1
        y = 1
        for i in range(PLAYER_AMOUNT):
            p = Player(x, y, i)
            self.player_list.append(p)
            x += 1
            y += 1
            
        self.game.message_router.broadcast_message("PlayerChanged", self.selected_player + 1)
        self.game.message_router.broadcast_message("StaminaChanged", self.get_current_player().stamina)

    def change_player(self):
        """change player and triggers action round"""
        self.player_list[self.selected_player].reset_position()
        if self.selected_player < len(self.player_list) -1:
            self.selected_player += 1
        else:
            self.selected_player = 0
            # FIXME:Need to add resole logic
            # self.resolve = True
        
        self.game.message_router.broadcast_message("PlayerChanged", self.selected_player + 1)
        self.game.message_router.broadcast_message("StaminaChanged", self.get_current_player().stamina)

    def apply_all_moves(self):
        """make all the players moves at the same time"""
        if self.current_round < max([len(p.recorded_moves) for p in self.player_list]):
            self.current_round += 1
            for player in self.player_list:
                try:
                    dx, dy = player.recorded_moves[self.current_round]
                    print(dx, dy)
                    print("more coming soon")
                except:
                    continue
        else:
            for player in self.player_list:
                player.reset_round()
            self.current_round = 0
            self.displaying_moves = False

    def on_update(self, delta_time):
        # if self.resolve:
        #     self.apply_all_moves()
        pass
