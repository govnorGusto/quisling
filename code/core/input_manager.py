import pygame
from core.game_object import Game_object

class Input_Manager(Game_object):
    def process_input(self):
        for event in pygame.event.get():
            self.game.message_router.broadcast_message(event.type, event)




