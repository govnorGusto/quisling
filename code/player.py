from settings import *
from sprites import *
from spritesheet import SpriteSheet, Animation
from actions import Move, MeleeAttack


class Player(AnimatedSprite):
    def __init__(self, x, y, num=None) -> None:
        super().__init__(x, y)

        self.image = pygame.Surface((TILESIZE, TILESIZE))

        self.draw_offset = (0, 0)
        self.load(num)
        self.image = self.active_anim.get_frame(0)

        self.facing = 2

        self.recorded_moves = []

        self.actions = {"move_action": Move(self), "melee_attack_action": MeleeAttack(self)}

        self.max_stamina = 10 
        self.stamina = self.max_stamina

    def load(self, num):
        boar_SE = SpriteSheet(
            path.join("graphics", "critters", "boar", "boar_SE_idle_strip.png"),
            bg="black",
        )
        boar_SE_idle = [(i * 41, 0, 41, 25) for i in range(6)]
        boar_NE = SpriteSheet(
            path.join("graphics", "critters", "boar", "boar_NE_idle_strip.png"),
            bg="black",
        )
        boar_NE_idle = [(i * 41, 0, 41, 28) for i in range(6)]

        stag_SE = SpriteSheet(
            path.join("graphics", "critters", "stag", "critter_stag_SE_idle.png"),
            bg="black",
        )
        stag_SE_idle = [(i * 32, 0, 32, 41) for i in range(23)]
        stag_NE = SpriteSheet(
            path.join("graphics", "critters", "stag", "critter_stag_NE_idle.png"),
            bg="black",
        )
        stag_NE_idle = [(i * 32, 0, 32, 41) for i in range(23)]

        match num:
            case 0:
                self.draw_offset = (0, -5)
                standing_se = boar_SE.get_animation(
                    boar_SE_idle, 0.10, Animation.PlayMode.LOOP, resize=2
                )
                standing_sw = boar_SE.get_animation(
                    boar_SE_idle, 0.10, Animation.PlayMode.LOOP, resize=2, flip=True
                )
                standing_ne = boar_NE.get_animation(
                    boar_NE_idle, 0.10, Animation.PlayMode.LOOP, resize=2
                )
                standing_nw = boar_NE.get_animation(
                    boar_NE_idle, 0.10, Animation.PlayMode.LOOP, resize=2, flip=True
                )
            case 1:
                self.draw_offset = (8, -40)
                standing_se = stag_SE.get_animation(
                    stag_SE_idle, 0.10, Animation.PlayMode.LOOP, resize=2
                )
                standing_sw = stag_SE.get_animation(
                    stag_SE_idle, 0.10, Animation.PlayMode.LOOP, resize=2, flip=True
                )
                standing_ne = stag_NE.get_animation(
                    stag_NE_idle, 0.10, Animation.PlayMode.LOOP, resize=2
                )
                standing_nw = stag_NE.get_animation(
                    stag_NE_idle, 0.10, Animation.PlayMode.LOOP, resize=2, flip=True
                )
        self.store_animation("standing_se", standing_se)
        self.store_animation("standing_sw", standing_sw)
        self.store_animation("standing_nw", standing_nw)
        self.store_animation("standing_ne", standing_ne)

    def animate(self):
        # change standing animation
        match self.facing:
            case 0:
                self.set_active_animation("standing_nw")
            case 1:
                self.set_active_animation("standing_ne")
            case 2:
                self.set_active_animation("standing_se")
            case 3:
                self.set_active_animation("standing_sw")

        # if self.active_name == "standing":
        #     self.set_active_animation("running")

        # # change running animation
        # if self.active_name == "running":
        #     self.set_active_animation("halting")

        # # change halting animaiton
        # if self.active_name == "halting":
        #     if self.active_anim.is_animation_finished(self.elapsed_time):
        #         self.set_active_animation("standing")

        topleft = self.rect.topleft
        self.image = self.active_anim.get_frame(self.elapsed_time)
        self.rect = self.image.get_rect()
        self.rect.topleft = topleft

    def update(self, delta_time):
        super().update(delta_time)
        self.active_anim
        self.animate()

    def record_move(self, x, y):
        self.recorded_moves.append((x, y))

    def reset_round(self):
        """Reset counters and set new start pos"""
        self.recorded_moves = []
        self.start_x = self.rect.x
        self.start_y = self.rect.y
        self.stamina = self.max_stamina

    def reset_position(self):
        """Move player back to start position of the round"""
        self.rect.x = self.start_x
        self.rect.y = self.start_y

    def on_draw(self, delta_time: float):
        self.game.display_surface.blit(self.image, self.rect.move(self.draw_offset))
