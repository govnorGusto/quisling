from settings import *
from core.sprite_object import Sprite_object


class AnimatedSprite(Sprite_object):
    def __init__(self, x, y):
        super().__init__(x, y)
        # control
        self.elapsed_time = 0
        self.active_anim = None
        self.active_name = ""
        self.animation_storage = {}

    def store_animation(self, name, anim):
        self.animation_storage[name] = anim
        # if no animation playing, start this one
        if self.active_name == "":
            self.set_active_animation(name)

    def set_active_animation(self, name):
        # check if animation with name exist
        if name not in self.animation_storage.keys():
            print(f"No animation: {name}")
            return

        # check if this animation is already running
        if name == self.active_name:
            return

        self.active_name = name
        self.active_anim = self.animation_storage[name]
        self.elapsed_time = 0

    def is_animation_finished(self):
        return self.active_anim.is_animation_finished(self.elapsed_time)

    def update(self, delta_time):
        super().update(delta_time)
        self.elapsed_time += delta_time
