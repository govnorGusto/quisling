from settings import *

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, num) -> None:
        super().__init__()
        self.image = pygame.Surface((TILESIZE, TILESIZE))
        self.image.fill("crimson")
        self.rect = self.image.get_rect()
        self.start_x = x * TILESIZE
        self.start_y = y * TILESIZE
        self.rect.topleft = (self.start_x, self.start_y)

        self.number_of_moves = 0
        self.max_moves = 10
        self.recorded_moves = []

        # temp
        self.font = pygame.font.SysFont(None, 30)
        text_surface = self.font.render(str(num), True, (0, 0, 0))
        text_rect = text_surface.get_rect(center=self.rect.center)
        self.image.blit(text_surface, (self.image.get_width() // 2 - text_rect.width // 2, 
                                       self.image.get_height() // 2 - text_rect.height // 2))

    def move(self, x, y):
        self.rect.x += x 
        self.rect.y += y 

    def record_move(self, x, y):
        self.recorded_moves.append((x, y))

    def reset_round(self):
        """Reset counters and set new start pos"""
        self.recorded_moves = []
        self.start_x = self.rect.x
        self.start_y = self.rect.y
        self.number_of_moves = 0

    def reset_position(self):
        """Move player back to start position of the round"""
        self.rect.x = self.start_x
        self.rect.y = self.start_y
