from cmath import rect
from turtle import left
import pygame


class UI_Canvas:
    game = 0

    def __init__(self, game, position: pygame.Vector2, parent=0) -> None:
        if self.game == 0:
            self.game = game

        self.parent: UI_Canvas = parent
        self.visible: bool = True
        self.top_left_position: pygame.Vector2 = position
        self.size: pygame.Vector2 = pygame.Vector2(80, 50)
        self.color = (255, 0, 255)
        self.alpha = 255

        self._child_canvases: [UI_Canvas] = []

    def add_child(self, position: pygame.Vector2):
        self._child_canvases.append(UI_Canvas(self.game, position, self))
        return self._child_canvases[-1]

    def draw(self, surface: pygame.Surface) -> None:
        if not self.visible:
            return

        surface_to_draw = pygame.Surface((int(self.size.x), int(self.size.y)))
        surface_to_draw.fill(self.color)
        surface_to_draw.set_alpha(self.alpha)
        rect = surface_to_draw.get_rect(
            top=self.top_left_position.x, left=self.top_left_position.y
        )
        surface.blit(surface_to_draw, rect)

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
