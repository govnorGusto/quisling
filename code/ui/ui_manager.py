import pygame
from settings import *

from core.game_object import Game_object
from ui.uicore.ui_canvas import *
from ui.ui_button import UI_Button
from ui.ui_text import UI_Text

UI_BACKGROUND_COLOR = (100, 100, 100)

# class UI_Manager(Game_object):
#     def __init__(self):
#         super().__init__(self)


def construct_ui_element(indata: UIDefinitionData, parent=0) -> UI_Canvas:
    if parent == 0:
        rect = pygame.Rect(indata.position, indata.size)
        out_canvas = indata.ui_type(rect)
    else:
        out_canvas = parent.add_child(indata.ui_type)

    out_canvas.color = indata.color
    out_canvas.alpha = indata.alpha
    out_canvas.horisontal_padding = indata.padding[0]
    out_canvas.vertical_padding = indata.padding[1]
    out_canvas.element_width, out_canvas.element_height = (
        indata.element_size[0],
        indata.element_size[1],
    )
    out_canvas.stacking_mode = indata.stacking_mode

    if indata.element_definitions.__class__ == list:
        for definition in indata.element_definitions:
            construct_ui_element(definition, out_canvas)

    return out_canvas


def make_turn_menu(end_turn_func, quit_func) -> UI_Canvas:

    menu = UI_Canvas(pygame.Rect(WINDOW_WIDTH - 220, WINDOW_HEIGHT - 200, 200, 300))
    menu.color = UI_BACKGROUND_COLOR
    
    button = menu.add_child(UI_Button)
    button.click_callbacks.append(end_turn_func)
    text = button.add_child(UI_Text)
    text.text = "End Turn"    
    
    button = menu.add_child(UI_Button)
    button.click_callbacks.append(quit_func)
    text = button.add_child(UI_Text)
    text.text = "Quit"
    
def make_top_bar(message_router) -> list:
    bar = UI_Canvas(pygame.Rect(-200, 0, WINDOW_WIDTH + 200, 50))
    bar.color = UI_BACKGROUND_COLOR
    bar.stacking_mode = EStackingMode.HORIZONTAL
    bar.horisontal_padding = 220
    
    text1 = bar.add_child(UI_Text)
    text1.text = "Stamina Remaining: "
    message_router.register_callback("StaminaChanged", text1.set_suffix)
    
    text2 = bar.add_child(UI_Text)
    text2.text = "Current Player: "
    message_router.register_callback("PlayerChanged", text2.set_suffix)
    
    return [text1, text2]

