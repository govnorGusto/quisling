from settings import *
from core.game_object import Game_object

class Sprite_object(Game_object, pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        super().__init__(game)
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.Surface((TILESIZE, TILESIZE))

        self.start_x = x
        self.start_y = y

        self.x = x
        self.y = y

        # FIXME: Should probably look over how to add objects in a better way
        self.game.grid.add(self, self.x, self.y)

        self.rect = self.image.get_rect()
        self.rect.topleft = (self.x * TILESIZE, self.y * TILESIZE)

    # FIXME: Move move?
    def move(self, dx, dy):
        self.game.grid.move(self, dx, dy)
        self.x += dx
        self.rect.x += dx * TILESIZE
        self.y += dy
        self.rect.y += dy * TILESIZE




