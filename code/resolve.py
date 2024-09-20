from settings import *
from core.game_object import Game_object

class Resolve(Game_object):
    def __init__(self):
        super().__init__()

        self.player_list = self.game.turn_manager.player_list
        self.current_round = 0

    def resolve_moves(self):
        """make all the players moves at the same time"""
        print("RESOLVE")

        # player_max_moves = [p.stored_actions for p in self.player_list]
        p1_moves = self.player_list[0].stored_actions.copy()
        p2_moves = self.player_list[1].stored_actions.copy()
        p1_len = len(p1_moves)
        p2_len = len(p2_moves) 
        longest = max(p1_len, p2_len)


        if self.current_round < p1_len:
            action1, args1 = p1_moves[self.current_round]
            action1.execute(*args1)
        if self.current_round < p2_len:
            action2, args2 = p2_moves[self.current_round]
            action2.execute(*args2)

        self.current_round += 1
        if self.current_round >= longest:
            for player in self.player_list:
                player.reset_round()
            self.current_round = 0
            self.game.turn_manager.resolve = False
