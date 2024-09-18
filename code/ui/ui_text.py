from ui.uicore.ui_canvas import UI_Canvas
import pygame


class UI_Text(UI_Canvas):
    def __init__(self, rect: pygame.Rect, parent, text = "") -> None:
        super().__init__(rect, parent)
        self.alpha = 0
        self.text = text
        self.text_color = (0, 0, 0)

    ### Note: this is a naive override of Super().draw(), consider if we ever want text elements to
    ###       have children
    def on_draw(self, delta_time : float) -> None:
        text_surface = pygame.font.SysFont(None, 30).render(
            self.text, True, self.text_color
        )
        pygame.display.get_surface().blit(text_surface, self.rect)
