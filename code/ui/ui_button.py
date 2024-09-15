from ui.uicore.ui_canvas import UI_Canvas
from core.clickable_component import Clickable
import pygame

class UI_Button(UI_Canvas):
    def __init__(self, game, rect: pygame.Rect, parent) -> None:
        super().__init__(parent.game, rect, parent)

        self._clickable_component : Clickable = Clickable(game, rect)
        self._clickable_component.on_mouse_enter.append(self.mouse_enter)
        self._clickable_component.on_mouse_exit.append(self.mouse_exit)
        self._clickable_component.on_click.append(self.mouse_click)
        self._clickable_component.on_release.append(self.mouse_release)
        
        ### TODO: This is not really a good spot for color definitions,
        ###       we want a proper set-method
        self.color_default = (175, 175, 175)
        self.color_hover = (155, 155, 155)
        self.color_click = (15, 15, 15)
        self.color = self.color_default
        
        self.click_callbacks = []
        
    
    def mouse_enter(self):
        self.color = self.color_hover
        
    def mouse_exit(self):
        self.color = self.color_default
        
    def mouse_click(self):
        self.color = self.color_click
        for callback in self.click_callbacks:
            callback()
        
    def mouse_release(self):
        self.color = self.color_hover
        
    



