from settings import *
from core.game_object import Game_object

RESOLVE_TIME_STEP = 0.75

class Resolve(Game_object):
    def __init__(self, p1_moves, p2_moves):
        super().__init__()
        self.resolve_started = False
        self.current_round = 0
        self.p1_moves = p1_moves.copy()
        self.p2_moves = p2_moves.copy()
        self.game.message_router.register_callback("PlayerReady", self.on_start_resolve)
        
        self.step_timer = RESOLVE_TIME_STEP
        
    def on_start_resolve(self, event):
        self.resolve_started = True
        self.game.message_router.broadcast_message("Resolve")

    def on_update(self, delta_time):
        if not self.resolve_started:
            return
        self.step_timer -= delta_time
        if self.step_timer < 0:
            self.resolve_moves()
            self.step_timer = RESOLVE_TIME_STEP

    def resolve_moves(self):
        """make all the players moves at the same time"""

        p1_len = len(self.p1_moves)
        p2_len = len(self.p2_moves) 
        longest = max(p1_len, p2_len)


        if self.current_round < p1_len:
            action1, args1 = self.p1_moves[self.current_round]
            action1.execute(*args1)
        if self.current_round < p2_len:
            action2, args2 = self.p2_moves[self.current_round]
            action2.execute(*args2)

        self.current_round += 1
        if self.current_round >= longest:
            self.game.message_router.broadcast_message("ResolveOver", 0)
            self.game.message_router.clear_callback(self.on_start_resolve)
            self.mark_for_delete()
