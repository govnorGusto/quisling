import pygame
from pyclbr import Function
from message_router import Message_Router


class Clickable():
    def __init__(self, game, rect : pygame.Rect) -> None:
        self.rect = rect
        
        self.OnClick : [Function] = []
        self.OnMouseEnter : [Function] = []
        self.OnMouseExit : [Function] =[]
        
        game.message_router.register_callback(pygame.MOUSEMOTION, self.OnMouseMove)
        game.message_router.register_callback(pygame.MOUSEBUTTONDOWN, self.OnMouseDown)
        game.message_router.register_callback(pygame.MOUSEBUTTONUP, self.OnMouseUp)
     

    def OnMouseMove(self, eventdata):
        # Check for overlap rect call releant callbacks
        pass
    
    def OnMouseDown(self, eventdata):
        # If overlap, call on click
        pass
    
    def OnMouseUp(self, eventdata):
        # If overlap, call maybe smth, idk wtf :s
        pass
        





