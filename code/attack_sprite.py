from settings import * 
from sprites import AnimatedSprite
from spritesheet import SpriteSheet, Animation

class Attack_Sprite(AnimatedSprite):
    def __init__(self, x, y, file, id):
        super().__init__(x, y)
        print(x, y)
        self.file = file

        sprite = SpriteSheet(
            path.join("graphics", "attacks", file),
            bg="black",
        )
        self.draw_offset = (16, 0)

        attack = sprite.get_animation(
                    [(i * 64, self.get_color(id), 64, 64) for i in range(13)], 0.1, Animation.PlayMode.LOOP, resize=0.75
                )

        self.store_animation(self.file, attack)

        self.image = self.active_anim.get_frame(0)

    def get_color(self, id):
        """what row to choose in png"""
        match id:
            case 0:
                return 0
            case 1:
                return 320


    def animate(self):
        self.set_active_animation(self.file)

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