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

MUSIC_SOURCES = [
    os.path.join(BASE_DIR, '..', "audio", "music", "GJ Battle .wav"),
    os.path.join(BASE_DIR, '..', "audio", "music", "GJ Music 1.wav"),
    os.path.join(BASE_DIR, '..', "audio", "music", "GJ Music 2.wav"),
    os.path.join(BASE_DIR, '..', "audio", "music", "GJ Music 3.wav")
]

SFX_SOURCES = [
        os.path.join(BASE_DIR, '..', "audio", "sfx", "GJ Bash.wav"),
        os.path.join(BASE_DIR, '..', "audio", "sfx", "GJ Button Hover.wav"),
        os.path.join(BASE_DIR, '..', "audio", "sfx", "GJ Move.wav"),
        os.path.join(BASE_DIR, '..', "audio", "sfx", "GJ Spin Attack.wav"),
        os.path.join(BASE_DIR, '..', "audio", "sfx", "GJ Take Damage.wav")
    ]

SFX_BASH = 0
SFX_CLICK = 1
SFX_MOVE = 2
SFX_SPIN = 3
SFX_DAMAGE = 4