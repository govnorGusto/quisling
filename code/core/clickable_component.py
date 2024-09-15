import pygame
from core.message_router import Message_Router


class Clickable():
    def __init__(self, game, rect : pygame.Rect) -> None:
        self.rect = rect
        self.mouse_is_overlapping = False
        
        self.on_click = []
        self.on_release = []
        self.on_mouse_enter = []
        self.on_mouse_exit = []
        
        game.message_router.register_callback(pygame.MOUSEMOTION, self.OnMouseMove)
        game.message_router.register_callback(pygame.MOUSEBUTTONDOWN, self.OnMouseDown)
        game.message_router.register_callback(pygame.MOUSEBUTTONUP, self.OnMouseUp)
     

    def OnMouseMove(self, eventdata):
        overlap = self.rect.collidepoint(pygame.mouse.get_pos())
        if overlap and not self.mouse_is_overlapping:
            for callback in self.on_mouse_enter:
                callback()
            self.mouse_is_overlapping = True
            return
            
        if not overlap and self.mouse_is_overlapping:
            for callback in self.on_mouse_exit:
                callback()
            self.mouse_is_overlapping = False
    
    def OnMouseDown(self, eventdata):
        if not self.mouse_is_overlapping:
            return
        for callback in self.on_click:
            callback()
    
    def OnMouseUp(self, eventdata):
        if not self.mouse_is_overlapping:
            return
        for callback in self.on_release:
            callback()
        





