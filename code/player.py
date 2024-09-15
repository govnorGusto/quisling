from settings import *
from sprites import *
from spritesheet import SpriteSheet, Animation


class Player(AnimatedSprite):
    def __init__(self, x, y, num=None) -> None:
        super().__init__()
        self.display_surface = pygame.display.get_surface()
        self.image = pygame.Surface((TILESIZE, TILESIZE))

        # sprite
        self.start_x = x * TILESIZE
        self.start_y = y * TILESIZE
        self.load(num)
        self.image = self.active_anim.get_frame(0)
        self.rect = self.image.get_rect()
        self.rect.topleft = (self.start_x, self.start_y)

        self.number_of_moves = 0
        self.max_moves = 10
        self.recorded_moves = []

        # temp
        self.font = pygame.font.SysFont(None, 30)
        text_surface = self.font.render(str(num), True, (0, 0, 0))
        text_rect = text_surface.get_rect(center=self.rect.center)
        self.image.blit(
            text_surface,
            (
                self.image.get_width() // 2 - text_rect.width // 2,
                self.image.get_height() // 2 - text_rect.height // 2,
            ),
        )

    def load(self, num):
        # idle SE animation
        boar_SE = SpriteSheet(
            path.join("graphics", "critters", "boar", "boar_SE_idle_strip.png")
        )
        boar_SE_idle = [(i * 41, 0, 41, 25) for i in range(6)]
        stag_SE = SpriteSheet(
            path.join("graphics", "critters", "stag", "critter_stag_SE_idle.png")
        )

        stag_SE_idle = [(i * 32, 0, 32, 41) for i in range(23)]

        match num:
            case 0:
                standing_animation = boar_SE.get_animation(
                    boar_SE_idle, 0.10, Animation.PlayMode.LOOP, resize=2
                )
                self.store_animation("standing", standing_animation)
            case 1:
                self.start_y -= 24
                standing_animation = stag_SE.get_animation(
                    stag_SE_idle, 0.10, Animation.PlayMode.LOOP, resize=2
                )
                self.store_animation("standing", standing_animation)

    def animate(self):
        # change standing animation
        if self.active_name == "standing":
            self.set_active_animation("running")

        # change running animation
        if self.active_name == "running":
            self.set_active_animation("halting")

        # change halting animaiton
        if self.active_name == "halting":
            if self.active_anim.is_animation_finished(self.elapsed_time):
                self.set_active_animation("standing")

        topleft = self.rect.topleft
        self.image = self.active_anim.get_frame(self.elapsed_time)
        self.rect = self.image.get_rect()
        self.rect.topleft = topleft

    def update(self, delta_time):
        super().update(delta_time)
        self.animate()

    def move(self, x, y):
        self.rect.x += x
        self.rect.y += y

    def record_move(self, x, y):
        self.recorded_moves.append((x, y))

    def reset_round(self):
        """Reset counters and set new start pos"""
        self.recorded_moves = []
        self.start_x = self.rect.x
        self.start_y = self.rect.y
        self.number_of_moves = 0

    def reset_position(self):
        """Move player back to start position of the round"""
        self.rect.x = self.start_x
        self.rect.y = self.start_y
