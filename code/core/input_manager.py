import pygame
from core.game_object import Game_object

INPUT_UP = pygame.K_w
INPUT_DOWN = pygame.K_s
INPUT_LEFT = pygame.K_a
INPUT_RIGHT = pygame.K_d
BASH_ATTACK = pygame.K_b
SPINNING_ATTACK = pygame.K_m

MOUSE_INPUT_ROTATION = 45
MOVE_INPUT_BOUNDING_RECT_SIZE = (400, 400)
UP    = pygame.Vector2(0, -1).rotate(MOUSE_INPUT_ROTATION)
LEFT  = pygame.Vector2(-1, 0).rotate(MOUSE_INPUT_ROTATION)


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
        self.game.message_router.register_callback(
            "WaitForPlayerReady", self.block_action_input
        )
        self.game.message_router.register_callback("GameOver", self.permablock)
        self.game.message_router.register_callback(
            "PlayerReady", self.unblock_action_input
        )
        self.action_input_blocked = False
        self.action_input_blocked_permanent = False

        self.game.message_router.register_callback("Bash", self.receive_bash_input)
        self.game.message_router.register_callback("Spin", self.receive_spin_input)

    def process_input(self):
        for event in pygame.event.get():
            self.game.message_router.broadcast_message(event.type, event)

            if self.action_input_blocked:
                continue

            if event.type == pygame.KEYDOWN and event.key in InputDirectionDict:
                self.game.message_router.broadcast_message(
                    "Move_command", InputDirectionDict[event.key]
                )
            if event.type == pygame.KEYDOWN and event.key in attack_dict:
                self.game.message_router.broadcast_message(
                    "attack_command", attack_dict[event.key]
                )

            if event.type == pygame.MOUSEBUTTONDOWN:
                self.process_mouse_move_input()

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

    def process_mouse_move_input(self):
        mPos = pygame.Vector2(pygame.mouse.get_pos())
        pPos = pygame.Vector2(self.game.turn_manager.get_current_player().rect.center)
        
        if not is_valid_mouse_move_input(mPos, pPos):
            return

        direction = mPos - pPos
        direction.normalize_ip()
        
        up_dot = direction.dot(UP)
        left_dot = direction.dot(LEFT)

        if abs(up_dot) > abs(left_dot):
            if up_dot > 0:
                self.game.message_router.broadcast_message(
                    "Move_command", InputDirectionDict[INPUT_UP]
                )
            else:
                self.game.message_router.broadcast_message(
                    "Move_command", InputDirectionDict[INPUT_DOWN]
                )
                
        else:
            if left_dot > 0:
                self.game.message_router.broadcast_message(
                    "Move_command", InputDirectionDict[INPUT_LEFT]
                )
            else:
                self.game.message_router.broadcast_message(
                    "Move_command", InputDirectionDict[INPUT_RIGHT]
                )
                
def is_valid_mouse_move_input(mPos : tuple, pPos :tuple):
    bounding_rect = pygame.Rect(pPos, MOVE_INPUT_BOUNDING_RECT_SIZE)
    bounding_rect.center = pPos
    return bounding_rect.collidepoint(mPos)
