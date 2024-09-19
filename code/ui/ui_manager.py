import pygame

from core.game_object import Game_object
from ui.uicore.ui_canvas import *

# class UI_Manager(Game_object):
#     def __init__(self):
#         super().__init__(self)


def construct_ui_element(indata : UIDefinitionData, parent = 0) -> UI_Canvas:
    if parent == 0:
        rect = pygame.Rect(indata.position, indata.size)
        out_canvas = indata.ui_type(rect)
    else:
        out_canvas = parent.add_child(indata.ui_type)
            
    out_canvas.color = indata.color
    out_canvas.alpha = indata.alpha
    out_canvas.horisontal_padding = indata.padding[0]
    out_canvas.vertical_padding = indata.padding[1]
    out_canvas.element_width, out_canvas.element_height = indata.element_size[0], indata.element_size[1]
    out_canvas.stacking_mode = indata.stacking_mode
    
    if indata.element_definitions.__class__ == list:
        for definition in indata.element_definitions:
            construct_ui_element(definition, out_canvas)
        
    return out_canvas
