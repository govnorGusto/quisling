import pygame
from enum import Enum


class EStackingMode(Enum):
    VERTICAL = 0
    HORIZONTAL = 1


class UI_Canvas:
    game = None

    def __init__(self, game, rect: pygame.Rect, parent=0) -> None:
        if self.game == None:
            self.game = game

        self.parent: UI_Canvas = parent
        self.visible: bool = True

        self.rect: pygame.Rect = rect
        self.color = (255, 0, 255)
        self.alpha = 255

        self.horisontal_padding = 20
        self.vertical_padding = 20
        self.element_width = 100
        self.element_height = 50
        self.stacking_mode = EStackingMode.VERTICAL

        self._child_canvases: [UI_Canvas] = []

    def add_child(self, type_to_add):
        if not issubclass(type_to_add, UI_Canvas):
            print("ERROR: A UI_Canvas child must derive from UI_Canvas")
            return

        child_rect = pygame.Rect(self.get_child_rect())

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

    def get_child_rect(self) -> pygame.Rect:
        if self.stacking_mode == EStackingMode.VERTICAL:
            left = self.rect.left + self.horisontal_padding
            top = (
                self.rect.top
                + self.vertical_padding
                + (self.vertical_padding + self.element_height)
                * len(self._child_canvases)
            )
            width = self.rect.width - self.horisontal_padding * 2
            height = self.element_height
            return pygame.Rect(left, top, width, height)
        else:
            left = (
                self.rect.left
                + self.horisontal_padding
                + (self.horisontal_padding + self.element_width)
                * len(self._child_canvases)
            )
            top = self.rect.top + self.vertical_padding
            width = self.element_width
            height = self.rect.height - self.vertical_padding * 2
            return pygame.Rect(left, top, width, height)

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
