# Setup Python ----------------------------------------------- #
from pygame import mixer


# CLass Block ------------------------------------------------ #
class Mixer():
    def __init__(self, settings):

        # Sound settings
        self.bg_music = None
        self.sound_volume = 0.5
        self.music_volume = 0.2

        self.settings = settings

# Functions --------------------------------------------------- #
    def music_load(self, path):
        self.bg_music = mixer.music.load(path)

    def music_play(self, path, repeat_times, fade_ms):
        self.music_load(path)
        mixer.music.play(repeat_times, fade_ms=fade_ms)
        mixer.music.set_volume(self.music_volume)

    def music_stop(self):
        mixer.music.stop()

    def music_rewind(self):
        mixer.music.rewind()

    def music_pause(self):
        mixer.music.pause()

    def sound_play(self, path):
        my_sound = mixer.Sound(path)
        my_sound.play()
        my_sound.set_volume(self.sound_volume)


# Updates ---------------------------------------------------- #
    def update_music_volume(self):
        self.music_volume = float(self.settings.get_music_volume())
        mixer.music.set_volume(self.music_volume)

    def update_sound_volume(self):
        self.sound_volume = float(self.settings.get_sound_volume())