from ui.uicore.ui_canvas import UI_Canvas
import pygame


class UI_Text(UI_Canvas):
    def __init__(self, rect: pygame.Rect, parent, text = "Text") -> None:
        super().__init__(rect, parent)
        self.alpha = 0
        self.prefix = ""
        self.suffix = ""
        self.text = text
        self.text_color = (0, 0, 0)

    ### Note: this is a naive override of Super().draw(), consider if we ever want text elements to
    ###       have children
    def on_draw(self, delta_time : float) -> None:
        text_to_draw = self.prefix + self.text + self.suffix
        
        text_surface = pygame.font.SysFont(None, 30).render(
            text_to_draw, True, self.text_color
        )
        pygame.display.get_surface().blit(text_surface, self.rect)
        
    def set_text(self, new_text):
        self.text = str(new_text)
        
    def set_prefix(self, new_prefix):
        self.prefix = str(new_prefix)
        
    def set_suffix(self, new_suffix):
        self.suffix = str(new_suffix)
