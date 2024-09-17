from settings import *
from sprites import *


class Tiles(pygame.sprite.Sprite):
    def __init__(self, x, y, bg=None, scale=None, offset=None) -> None:
        super().__init__()
        self.display_surface = pygame.display.get_surface()
        self.bg = bg

        # load dirt tile
        self.image = pygame.image.load(
            join("graphics", "isometric tileset", "separated images", "tile_003.png")
        ).convert()

        self.rect = self.image.get_frect(center=(x, y))
        self.rect.x = x * TILESIZE
        self.rect.y = y * TILESIZE

        if self.bg is not None:
            self.image.set_colorkey(self.bg)

        if scale is not None:
            self.image = pygame.transform.scale(
                self.image, (TILESIZE * scale, TILESIZE * scale)
            )
