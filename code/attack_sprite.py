from settings import * 
from sprites import AnimatedSprite
from spritesheet import SpriteSheet, Animation

class Attack_Sprite(AnimatedSprite):
    def __init__(self, x, y):
        super().__init__(x, y)

        sprite = SpriteSheet(
            path.join("graphics", "attacks", "589.png"),
            bg="black",
        )
        idle = [(i * 41, 0, 41, 25) for i in range(13)]

        attack = sprite.get_animation(
                    idle, 0.3, Animation.PlayMode.LOOP, resize=0.5
                )
        self.store_animation("attack", attack)

        self.image = self.active_anim.get_frame(0)

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