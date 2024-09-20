import pygame
from core.message_router import Message_Router
from core.game_object import Component


class Clickable(Component):
    def __init__(self, owner) -> None:
        super().__init__(owner)
        self.rect = None
        self.mouse_is_overlapping = False
        
        self.on_click = []
        self.on_release = []
        self.on_mouse_enter = []
        self.on_mouse_exit = []
        
        self.get_game().message_router.register_callback(pygame.MOUSEMOTION, self.OnMouseMove)
        self.get_game().message_router.register_callback(pygame.MOUSEBUTTONDOWN, self.OnMouseDown)
        self.get_game().message_router.register_callback(pygame.MOUSEBUTTONUP, self.OnMouseUp)
     
    def set_rect(self, rect):
        self.rect = rect

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
            
    def mark_for_delete(self):
        self.get_game().message_router.clear_callback(self.OnMouseMove)
        self.get_game().message_router.clear_callback(self.OnMouseDown)
        self.get_game().message_router.clear_callback(self.OnMouseUp)
        self.on_click.clear()
        self.on_release.clear()
        self.on_mouse_enter.clear()
        self.on_mouse_exit.clear()
        super().mark_for_delete()
        





