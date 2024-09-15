from settings import *

class Button():
    def __init__(self, x, y, text):
        self.surface = pygame.display.get_surface()
        self.image = pygame.Surface((80, 50))
        self.image.fill((255, 255, 255))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False
        self.text = text
        self.font = pygame.font.SysFont(None, 30)
        self.text_color = (0, 0, 0)

    def draw(self):
        action = False
        pos = pygame.mouse.get_pos()

        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and not self.clicked:
                action = True
                self.clicked = True

        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False

        text_surface = self.font.render(self.text, True, self.text_color)
        text_rect = text_surface.get_rect(center=self.rect.center)

        self.image.blit(text_surface, (self.image.get_width() // 2 - text_rect.width // 2, 
                                       self.image.get_height() // 2 - text_rect.height // 2))
        self.surface.blit(self.image, (self.rect.x, self.rect.y))

        return action
    