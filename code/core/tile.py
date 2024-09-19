from settings import *


class Tile(pygame.sprite.Sprite):
    def __init__(self, pos, image, walkable: bool):
        pygame.sprite.Sprite.__init__(self)
        self.image = image.convert()
        self.walkable = walkable
        self.rect = self.image.get_rect()
        self.rect.topleft = pos
