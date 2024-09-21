from re import S
import pygame
from settings import *
from enum import Enum
from core.game_object import Game_object
from ui.uicore.ui_canvas import *
from ui.ui_button import UI_Button
from ui.ui_text import UI_Text

UI_BACKGROUND_COLOR = (100, 100, 100)


class EReadyScreenState(Enum):
    RESOLVE = 0
    PLAYER1 = 1
    PLAYER2 = 2


class UI_Manager(Game_object):
    def __init__(self):
        super().__init__(self)

        make_turn_menu(self.game.turn_manager.change_player, self.game.on_quit)
        self.player_hp_delegates = make_top_bar(self.game.message_router)

        action_list = [
            ("Bash", self.game.message_router.broadcast_message),
            ("Spin", self.game.message_router.broadcast_message),
        ]
        make_action_menu(action_list)

        self.game.message_router.register_callback(
            "HealthChanged", self.transfer_hp_callback
        )
        self.game.message_router.register_callback(
            "PlayerChanged", self.on_player_change
        )
        self.game.message_router.register_callback(
            "ResolvePhase", self.on_player_change
        )

    def transfer_hp_callback(self, eventdata: tuple):
        self.player_hp_delegates[eventdata[0]](eventdata[1])

    def on_player_change(self, eventdata):
        self.game.message_router.broadcast_message("WaitForPlayerReady")
        make_next_player_screen(eventdata, self.on_player_ready)

    def on_player_ready(self):
        self.game.message_router.broadcast_message("PlayerReady")


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

    make_button(menu, "End Turn", end_turn_func)
    make_button(menu, "Quit", quit_func)


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

    text3 = bar.add_child(UI_Text)
    text3.text = "Player 1 HP :"

    text4 = bar.add_child(UI_Text)
    text4.text = "Player 2 HP : "

    return [text3.set_suffix, text4.set_suffix]


def make_button(parent, button_text, func, payload=None):
    button = parent.add_child(UI_Button)
    button.click_callbacks.append(func)
    button.callback_payload = payload

    text = button.add_child(UI_Text)
    text.text = button_text
    return button


def make_action_menu(actions: list):
    menu = UI_Canvas(pygame.Rect(20, WINDOW_HEIGHT - 200, 200, 300))
    menu.color = UI_BACKGROUND_COLOR

    for action_tuple in actions:
        make_button(menu, action_tuple[0], action_tuple[1], action_tuple[0])


def make_game_over_menu(quit_func, losing_player_index) -> UI_Canvas:

    menu = UI_Canvas(pygame.Rect(350, 100, 600, 400))
    menu.color = UI_BACKGROUND_COLOR
    menu.alpha = 100
    menu.horisontal_padding = 40

    text = menu.add_child(UI_Text)
    text.set_text(f"Game Over, player {losing_player_index + 1} has lost the game!")
    make_button(menu, "Quit", quit_func)


def make_next_player_screen(state: EReadyScreenState, continue_func):
    menu = UI_Canvas(pygame.Rect(0, 0, WINDOW_WIDTH, WINDOW_HEIGHT))
    menu.color = (0, 0, 0)
    menu.alpha = 200
    menu.horisontal_padding = 350
    menu.vertical_padding = 300
    text = menu.add_child(UI_Text)
    text.color = UI_BACKGROUND_COLOR
    text.alpha = 255

    match state:
        case 0:
            text.set_text("Resolve phase")
        case 1:
            text.set_text("Ready player 1")
        case 2:
            text.set_text("Ready player 2")

    button = make_button(menu, "Continue", continue_func)
    button.click_callbacks.append(menu.mark_for_delete)