from settings import *

class Tile(pygame.sprite.Sprite):
    def __init__(self, x, y, image, walkable:bool):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.walkable = walkable
        self.rect = self.image.get_rect()
        self.rect.topleft = (x * TILESIZE, y * TILESIZE)