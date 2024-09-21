from settings import * 
from sprites import AnimatedSprite
from spritesheet import SpriteSheet, Animation

class Attack_Sprite(AnimatedSprite):
    def __init__(self, x, y, id):
        super().__init__(x, y)
        bash = self.get_files(id)
        print(bash)
        bash_sprite = SpriteSheet(
            path.join("graphics", "attacks", bash),
            bg="black",
        )
        self.draw_offset = (16, 0)

        idle = [(i * 64, 0, 64, 64) for i in range(13)]

        bash_attack = bash_sprite.get_animation(
                    idle, 0.1, Animation.PlayMode.LOOP, resize=0.75
                )

        self.store_animation("bash", bash_attack)

        self.image = self.active_anim.get_frame(0)


    def get_files(self, id):
        match id:
            case 0:
                return ("589.png")
            case 1:
                return ("576.png")


    def animate(self):
        self.set_active_animation("attack")

        topleft = self.rect.topleft
        self.image = self.active_anim.get_frame(self.elapsed_time)
        self.rect = self.image.get_rect()
        self.rect.topleft = topleft

    def update(self, delta_time):
        super().update(delta_time)
        self.active_anim
        self.animate()

    def on_draw(self, delta_time):
        self.game.display_surface.blit(self.image, self.rect.move(self.draw_offset))