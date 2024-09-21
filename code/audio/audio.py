from secrets import randbelow
import pygame
from settings import *
from core.game_object import Game_object

MUSIC_SOURCES = [
    path.join("audio", "music", "battle.mp3"),
    path.join("audio", "music", "laugh.mp3"),
    path.join("audio", "music", "yes_3.mp3"),
    path.join("audio", "music", "yes_5.mp3"),
]


class Audio_player(Game_object):
    def __init__(self):
        self.sfx_mixer = pygame.mixer.init()
        self.current_song = -1
        self.should_loop = True
        self.stop_event = pygame.event.custom_type()
        self.game.message_router.register_callback(
            self.stop_event, self.on_music_playback_over
        )

    def on_music_playback_over(self, event):
        if not self.should_loop:
            return
        self.current_song += 1
        self.play_music(self.current_song)

    def play_music(self, song_index=-1):
        if song_index == -1:
            self.current_song = randbelow(len(MUSIC_SOURCES) - 1)
            print(f"Playing song {self.current_song} from random")
        else:
            print(f"Playing song {self.current_song} from selection")
        pygame.mixer.music.load(MUSIC_SOURCES[self.current_song])
        pygame.mixer.music.play()
        pygame.mixer_music.set_endevent(self.stop_event)
