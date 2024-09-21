import pygame, sys
import os
from pygame.math import Vector2 as vector
from os.path import join

# this is where we store the settings

WINDOW_WIDTH, WINDOW_HEIGHT = 1280, 720
FPS = 60
BG_COLOR = "black"
SCALE = 2
GRID_Y_ORIGIN = 300
GRID_X_ORIGIN = 450

TILESIZE = 32
GRID_WIDTH = WINDOW_WIDTH / TILESIZE
GRID_HEIGHT = WINDOW_HEIGHT / TILESIZE
GRID_COLOR = (100, 100, 100)

PLAYER_AMOUNT = 2
ANIMATION_SPEED = 1 / FPS

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

LEVEL_NAMES = [
            "Island",
            "Grassland",
            "Desert"
            ]

MAP_PATHS = [
    os.path.join(BASE_DIR, '..', 'graphics', 'tmx', 'level_test.tmx'),
    os.path.join(BASE_DIR, '..' , 'graphics', 'tmx', 'grass.tmx'),
    os.path.join(BASE_DIR, '..' , 'graphics', 'tmx', 'desert.tmx')
    ]
