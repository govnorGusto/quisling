from secrets import randbelow
import pygame
from settings import *
from core.game_object import Game_object


class Audio_player(Game_object):
    def __init__(self):
        self.sfx_mixer = pygame.mixer.init()

        self.current_song = -1
        self.should_loop = True
        self.stop_event = pygame.event.custom_type()
        pygame.mixer.music.set_volume(0.3)
        
        self.game.message_router.register_callback(
            self.stop_event, self.on_music_playback_over
        )
        
        self.sfx_list = load_sfx()
        self.game.message_router.register_callback("PlaySFX", self.play_sfx)

    def on_music_playback_over(self, event):
        if not self.should_loop:
            return
        self.current_song += 1
        self.play_music(self.current_song)

    def play_music(self, song_index=-1):
        if song_index == -1:
            self.current_song = randbelow(len(MUSIC_SOURCES) - 1)

        pygame.mixer.music.load(MUSIC_SOURCES[self.current_song])
        pygame.mixer.music.play()
        pygame.mixer_music.set_endevent(self.stop_event)

    def play_sfx(self, index):
        self.sfx_list[index].play()


def load_sfx() -> list:
    out = []
    for sound in SFX_SOURCES:
        out.append(pygame.mixer.Sound(sound))
    return out