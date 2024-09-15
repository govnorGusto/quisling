import pygame


class UI_Canvas:
    game = 0

    def __init__(self, game, rect: pygame.Rect, parent=0) -> None:
        if self.game == 0:
            self.game = game

        self.parent: UI_Canvas = parent
        self.visible: bool = True
        self.rect: pygame.Rect = rect
        self.color = (255, 0, 255)
        self.alpha = 255

        self._child_canvases: [UI_Canvas] = []

    def add_child(self, type_to_add):
        if not issubclass(type_to_add,UI_Canvas):
            print("A UI_Canvas child must derive from UI_Canvas")
            return
        
        ### TODO: We want more fancy behaviours for child scaling and positioning
        child_rect = pygame.Rect(self.rect).scale_by(0.75, 0.75)
        self._child_canvases.append(type_to_add(self.game, child_rect, self))
        return self._child_canvases[-1]

    def draw(self, surface: pygame.Surface) -> None:
        if not self.visible:
            return

        surface_to_draw = pygame.Surface(self.rect.size)
        surface_to_draw.fill(self.color)
        surface_to_draw.set_alpha(self.alpha)
        surface.blit(surface_to_draw, self.rect)

        for child in self._child_canvases:
            child.draw(surface)

    def get_outer_parent(self):
        if self.parent == 0:
            return self
        return self.parent.get_outer_parent()

    def on_event(self, eventdata):
        self.print()

    ### FOR EASY DEBUGGING
    def print(self) -> None:
        print(
            "UI Base object: "
            + str(self)
            + "\n"
            + "Parent: "
            + str(self.parent)
            + "\n"
            + "Outer parent: "
            + str(self.get_outer_parent())
            + "\n"
            + "In:"
            + str(self.game)
        )

    def print_all_children(self) -> None:
        self.print()
        for child in self._child_canvases:
            child.print_all_children()
