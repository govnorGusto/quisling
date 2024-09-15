import pygame
from pyclbr import Function


class Clickable():
    def __init__(self, game, rect : pygame.Rect) -> None:
        self.OnClick : [Function] = []
        self.OnMouseEnter : [Function] = []
        self.OnMouseExir : [Function] =[]
        self.rect = rect
        





