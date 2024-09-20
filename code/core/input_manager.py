import pygame
from core.game_object import Game_object

INPUT_UP = pygame.K_w
INPUT_DOWN = pygame.K_s
INPUT_LEFT = pygame.K_a
INPUT_RIGHT = pygame.K_d
BASH_ATTACK = pygame.K_b
SPINNING_ATTACK = pygame.K_m


InputDirectionDict = {}
# InputDirectionDict[INPUT_UP] = (0, -1)
# InputDirectionDict[INPUT_DOWN] = (0, 1)
# InputDirectionDict[INPUT_LEFT] = (-1, 0)
# InputDirectionDict[INPUT_RIGHT] = (1, 0)

InputDirectionDict[INPUT_UP] = (1, 0)
InputDirectionDict[INPUT_DOWN] = (-1, 0)
InputDirectionDict[INPUT_LEFT] = (0, -1)
InputDirectionDict[INPUT_RIGHT] = (0, 1)

attack_dict = {}
attack_dict[BASH_ATTACK] = "bash_attack"
attack_dict[SPINNING_ATTACK] = "spinning_attack"


class Input_Manager(Game_object):
    def __init__(self, game):
        super().__init__(game)
        self.game.message_router.register_callback("Resolve", self.block_action_input)
        self.game.message_router.register_callback("GameOver", self.permablock)
        self.game.message_router.register_callback(
            "ResolveOver", self.unblock_action_input
        )
        self.action_input_blocked = False
        self.action_input_blocked_permanent = False

        self.game.message_router.register_callback("Bash", self.receive_bash_input)
        self.game.message_router.register_callback("Spin", self.receive_spin_input)

    def process_input(self):
        for event in pygame.event.get():
            self.game.message_router.broadcast_message(event.type, event)

            if self.action_input_blocked:
                return

            if event.type == pygame.KEYDOWN and event.key in InputDirectionDict:
                self.game.message_router.broadcast_message(
                    "Move_command", InputDirectionDict[event.key]
                )
            if event.type == pygame.KEYDOWN and event.key in attack_dict:
                self.game.message_router.broadcast_message(
                    "attack_command", attack_dict[event.key]
                )

    def block_action_input(self, data):
        self.action_input_blocked = True

    def unblock_action_input(self, data):
        if self.action_input_blocked_permanent:
            return
        self.action_input_blocked = False

    def permablock(self, data):
        self.action_input_blocked = True
        self.action_input_blocked_permanent = True

    def receive_bash_input(self, blob):
        if self.action_input_blocked:
            return
        self.game.message_router.broadcast_message("attack_command", "bash_attack")

    def receive_spin_input(self, blob):
        if self.action_input_blocked:
            return
        self.game.message_router.broadcast_message("attack_command", "spinning_attack")