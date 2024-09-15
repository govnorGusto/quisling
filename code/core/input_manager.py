import pygame

class Input_Manager:
    def __init__(self, game):
        self.game = game
    
    def process_input(self):
        for event in pygame.event.get():
            self.game.message_router.broadcast_message(event.type, event)




