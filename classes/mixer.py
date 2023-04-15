from pygame import mixer

class Mixer:
    def __init__(self):
        self.bg_music = None

    def music_load(self, path):
        self.bg_music = mixer.music.load(path)

    def music_play(self, path, repeat_times, fade_ms):
        self.music_load(path)
        mixer.music.play(repeat_times, fade_ms=fade_ms)

    def music_stop(self):
        mixer.music.stop()
    
    def music_rewind(self):
        mixer.music.rewind()
    
    def music_pause(self):
        mixer.music.pause()
    
    def sound_play(self, path):
        mixer.Sound(path).play()