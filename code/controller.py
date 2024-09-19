from settings import *
from core.game_object import Game_object
from actions import *

class Controller(Game_object):
    def __init__(self):
        super().__init__()

        self.move = Move()
        self.game.message_router.register_callback("Move_command", self.receive_move_input)
    
    def receive_move_input(self, movedata):
        self.move.execute(self.game.turn_manager.get_current_player(), movedata[0], movedata[1])