import pygame, sys
from os import path
from pygame.math import Vector2 as vector
from os.path import join

# this is where we store the settings

WINDOW_WIDTH, WINDOW_HEIGHT = 1280, 720
FPS = 60
BG_COLOR = "Grey"

TILESIZE = 32
GRID_WIDTH = WINDOW_WIDTH / TILESIZE
GRID_HEIGHT = WINDOW_HEIGHT / TILESIZE
GRID_COLOR = (100, 100, 100)

PLAYER_AMOUNT = 2
ANIMATION_SPEED = 6
