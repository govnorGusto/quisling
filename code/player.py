from settings import *
from sprites import *
from spritesheet import SpriteSheet, Animation
from actions.get_action import Get_Action


class Player(AnimatedSprite):
    def __init__(self, x, y, num=None) -> None:
        super().__init__(x, y)

        self.id = num
        self.draw_offset = (0, 0)
        self.load(num)
        self.image = self.active_anim.get_frame(0)

        self.facing = 2

        self.actions = {
            "move_action": Get_Action.MOVE.value(self),
            "bash_attack": Get_Action.BASH_ATTACK.value(self),
            "spinning_attack": Get_Action.SPINNING_ATTACK.value(self),
        }

        self.stored_actions = []

        self.max_stamina = 5
        self.stamina = self.max_stamina

        self.max_health = 5
        self.health = self.max_health
        self.game.message_router.register_callback("ResolveOver", self.reset_round)

    def load(self, num):
        boar_SE = SpriteSheet(
            os.path.join(
                BASE_DIR, "..", "graphics", "critters", "boar", "boar_SE_idle_strip.png"
            ),
            bg="black",
        )
        boar_SE_run = SpriteSheet(
            os.path.join(
                BASE_DIR, "..", "graphics", "critters", "boar", "boar_SE_run_strip.png"
            ),
            bg="black",
        )
        boar_NE = SpriteSheet(
            os.path.join(
                BASE_DIR, "..", "graphics", "critters", "boar", "boar_NE_idle_strip.png"
            ),
            bg="black",
        )
        boar_NE_run = SpriteSheet(
            os.path.join(
                BASE_DIR, "..", "graphics", "critters", "boar", "boar_NE_run_strip.png"
            ),
            bg="black",
        )

        stag_SE = SpriteSheet(
            os.path.join(
                BASE_DIR,
                "..",
                "graphics",
                "critters",
                "stag",
                "critter_stag_SE_idle.png",
            ),
            bg="black",
        )
        stag_NE = SpriteSheet(
            os.path.join(
                BASE_DIR,
                "..",
                "graphics",
                "critters",
                "stag",
                "critter_stag_NE_idle.png",
            ),
            bg="black",
        )

        stag_SE_run = SpriteSheet(
            os.path.join(
                BASE_DIR,
                "..",
                "graphics",
                "critters",
                "stag",
                "critter_stag_SE_run.png",
            ),
            bg="black",
        )
        stag_NE_run = SpriteSheet(
            os.path.join(
                BASE_DIR,
                "..",
                "graphics",
                "critters",
                "stag",
                "critter_stag_NE_run.png",
            ),
            bg="black",
        )
        boar_SE_idle = [(i * 41, 0, 41, 25) for i in range(6)]
        boar_NE_idle = [(i * 41, 0, 41, 30) for i in range(6)]

        boar_SE_running = [(i * 41, 0, 41, 25) for i in range(3)]
        boar_NE_running = [(i * 41, 0, 41, 30) for i in range(3)]

        stag_SE_idle = [(i * 32, 0, 32, 41) for i in range(23)]
        stag_NE_idle = [(i * 32, 0, 32, 41) for i in range(23)]

        stag_SE_running = [(i * 32, 0, 32, 41) for i in range(9)]
        stag_NE_running = [(i * 32, 0, 32, 41) for i in range(9)]

        match num:
            case 0:
                self.draw_offset = (0, -5)
                standing_se = boar_SE.get_animation(
                    boar_SE_idle, 0.10, Animation.PlayMode.LOOP, resize=SCALE
                )
                standing_sw = boar_SE.get_animation(
                    boar_SE_idle, 0.10, Animation.PlayMode.LOOP, resize=SCALE, flip=True
                )
                standing_ne = boar_NE.get_animation(
                    boar_NE_idle, 0.10, Animation.PlayMode.LOOP, resize=SCALE
                )
                standing_nw = boar_NE.get_animation(
                    boar_NE_idle, 0.10, Animation.PlayMode.LOOP, resize=SCALE, flip=True
                )

                running_se = boar_SE_run.get_animation(
                    boar_SE_running, 0.10, Animation.PlayMode.LOOP, resize=SCALE
                )
                running_sw = boar_SE_run.get_animation(
                    boar_SE_running,
                    0.10,
                    Animation.PlayMode.LOOP,
                    resize=SCALE,
                    flip=True,
                )
                running_ne = boar_NE_run.get_animation(
                    boar_NE_running, 0.10, Animation.PlayMode.LOOP, resize=SCALE
                )
                running_nw = boar_NE_run.get_animation(
                    boar_NE_running,
                    0.10,
                    Animation.PlayMode.LOOP,
                    resize=SCALE,
                    flip=True,
                )
            case 1:
                self.draw_offset = (8, -40)
                standing_se = stag_SE.get_animation(
                    stag_SE_idle, 0.10, Animation.PlayMode.LOOP, resize=SCALE
                )
                standing_sw = stag_SE.get_animation(
                    stag_SE_idle, 0.10, Animation.PlayMode.LOOP, resize=SCALE, flip=True
                )
                standing_ne = stag_NE.get_animation(
                    stag_NE_idle, 0.10, Animation.PlayMode.LOOP, resize=SCALE
                )
                standing_nw = stag_NE.get_animation(
                    stag_NE_idle, 0.10, Animation.PlayMode.LOOP, resize=SCALE, flip=True
                )

                running_se = stag_SE_run.get_animation(
                    stag_SE_running, 0.10, Animation.PlayMode.LOOP, resize=SCALE
                )
                running_sw = stag_SE_run.get_animation(
                    stag_SE_running,
                    0.10,
                    Animation.PlayMode.LOOP,
                    resize=SCALE,
                    flip=True,
                )
                running_ne = stag_NE_run.get_animation(
                    stag_NE_running, 0.10, Animation.PlayMode.LOOP, resize=SCALE
                )
                running_nw = stag_NE_run.get_animation(
                    stag_NE_running,
                    0.10,
                    Animation.PlayMode.LOOP,
                    resize=SCALE,
                    flip=True,
                )
        self.store_animation("standing_se", standing_se)
        self.store_animation("standing_sw", standing_sw)
        self.store_animation("standing_nw", standing_nw)
        self.store_animation("standing_ne", standing_ne)
        self.store_animation("running_se", running_se)
        self.store_animation("running_sw", running_sw)
        self.store_animation("running_ne", running_ne)
        self.store_animation("running_nw", running_nw)

    def animate(self):
        # change standing animation
        if self.game.turn_manager.is_resolving:
            match self.facing:
                case 0:
                    self.set_active_animation("running_nw")
                case 1:
                    self.set_active_animation("running_ne")
                case 2:
                    self.set_active_animation("running_se")
                case 3:
                    self.set_active_animation("running_sw")
        else:

            match self.facing:
                case 0:
                    self.set_active_animation("standing_nw")
                case 1:
                    self.set_active_animation("standing_ne")
                case 2:
                    self.set_active_animation("standing_se")
                case 3:
                    self.set_active_animation("standing_sw")

        topleft = self.rect.topleft
        self.image = self.active_anim.get_frame(self.elapsed_time)
        self.rect = self.image.get_rect()
        self.rect.topleft = topleft

    def update(self, delta_time):
        super().update(delta_time)
        self.active_anim
        self.animate()

    def store_action(self, action, *args):
        self.stored_actions.append((action, [arg for arg in args]))

    def reset_round(self, rounddata):
        """Reset counters and set new start pos"""
        self.stored_actions.clear()
        self.start_x = self.x
        self.start_y = self.y
        self.modify_stamina(self.max_stamina - self.stamina)

    def reset_position(self):
        """Move player back to start position of the round"""
        self.x = self.start_x
        self.y = self.start_y
        self.rect.topleft = self.game.grid.grid_to_screen(self.x, self.y)
        self.game.grid.move(self, self.x, self.y)
        self.modify_stamina(self.max_stamina - self.stamina)

    def on_draw(self, delta_time: float):
        self.game.display_surface.blit(self.image, self.rect.move(self.draw_offset))

    def modify_stamina(self, modification: int):
        self.stamina += modification
        self.game.message_router.broadcast_message("StaminaChanged", self.stamina)

    def modify_health(self, modification: int):
        self.health += modification
        self.game.message_router.broadcast_message(
            "HealthChanged", (self.id, self.health)
        )

        if self.health <= 0:
            self.game.message_router.broadcast_message("GameOver", self.id)
