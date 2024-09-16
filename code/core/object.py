from settings import *
from core.game_object import Game_object

class Object(Game_object, pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites
        super().__init__(game)
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.image = pygame.Surface((TILESIZE, TILESIZE))

        self.start_x = x
        self.start_y = y

        self.x = x
        self.y = y

        self.game.grid.add(self, x, y)

        self.rect = self.image.get_rect()
        self.rect.topleft = (self.x * TILESIZE, self.y * TILESIZE)

    def move(self, dx, dy):
        self.game.grid.move(self, dx, dy)
        self.x += dx
        self.rect.x += dx * TILESIZE
        self.y += dy
        self.rect.y += dy * TILESIZE



