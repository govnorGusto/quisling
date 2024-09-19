from settings import *
from core.game_object import Game_object

class Sprite_object(Game_object):
    def __init__(self, x, y):
        super().__init__()

        self.image = pygame.Surface((TILESIZE, TILESIZE))
        self.image.fill((255, 255, 255))

        self.start_x = x
        self.start_y = y

        self.x = x
        self.y = y

        # FIXME: Should probably look over how to add objects in a better way
        self.game.grid.add(self, self.x, self.y)

        self.rect = self.image.get_rect()
        self.rect.topleft = self.game.grid.grid_to_screen(self.x, self.y)

    def on_draw(self, delta_time: float):
        self.game.display_surface.blit(self.image, self.rect)






