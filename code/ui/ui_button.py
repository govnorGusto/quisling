from ui.uicore.ui_canvas import UI_Canvas
from core.clickable_component import Clickable
import pygame


class UI_Button(UI_Canvas):
    def __init__(self, rect: pygame.Rect, parent) -> None:
        super().__init__(rect, parent)

        clickable = self.add_component(Clickable)
        clickable.set_rect(rect)
        
        clickable.on_mouse_enter.append(self.mouse_enter)
        clickable.on_mouse_exit.append(self.mouse_exit)
        clickable.on_click.append(self.mouse_click)
        clickable.on_release.append(self.mouse_release)

        self.callback_payload = None    
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
            if self.callback_payload == None:
                callback()
            else:
                callback(self.callback_payload)

    def mouse_release(self):
        self.color = self.color_hover
