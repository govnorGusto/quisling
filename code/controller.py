from settings import *
from core.game_object import Game_object
from actions import *

class Controller(Game_object):
    def __init__(self):
        super().__init__()

        self.current_player = 0
        self.move = Move()
    
    def get_input(self, key):
        if key == pygame.K_LEFT:
            self.move.execute(self.game.players[self.current_player], 1, 0)
        elif key == pygame.K_RIGHT:
            self.move.execute(self.game.players[self.current_player], -1, 0)
        elif key == pygame.K_UP:
            self.move.execute(self.game.players[self.current_player], 0, -1)
        elif key == pygame.K_DOWN:
            self.move.execute(self.game.players[self.current_player], 0, 1)