from settings import *
from core.game_object import Game_object
from actions import *

class Controller(Game_object):
    def __init__(self):
        super().__init__()

        self.game.message_router.register_callback("Move_command", self.receive_move_input)
        self.game.message_router.register_callback("attack_command", self.receive_attack_input)
    
    def receive_move_input(self, movedata):
        self.game.turn_manager.get_current_player().actions["move_action"].execute(movedata[0], movedata[1])

    def receive_attack_input(self, data):
        self.game.turn_manager.get_current_player().actions[data].execute()