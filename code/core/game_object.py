from settings import *

class Game_object:
    game = None
    def __init__(self, game=None):
        if self.game == None:
            self.game = game