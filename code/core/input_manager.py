import pygame
from core.game_object import Game_object

INPUT_UP = pygame.K_w
INPUT_DOWN = pygame.K_s
INPUT_LEFT = pygame.K_a
INPUT_RIGHT = pygame.K_d
BASH_ATTACK = pygame.K_b
SPINNING_ATTACK = pygame.K_m


InputDirectionDict = {}
InputDirectionDict[INPUT_UP] = (0, -1)
InputDirectionDict[INPUT_DOWN] = (0, 1)
InputDirectionDict[INPUT_LEFT] = (-1, 0)
InputDirectionDict[INPUT_RIGHT] = (1, 0)

attack_dict = {}
attack_dict[BASH_ATTACK] = "bash_attack"
attack_dict[SPINNING_ATTACK] = "spinning_attack"


class Input_Manager(Game_object):
    def process_input(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN and event.key in InputDirectionDict:
                self.game.message_router.broadcast_message(
                    "Move_command", InputDirectionDict[event.key]
                )
            if event.type == pygame.KEYDOWN and event.key in attack_dict:
                self.game.message_router.broadcast_message(
                    "attack_command", attack_dict[event.key]
                )

            self.game.message_router.broadcast_message(event.type, event)
