# Setup Python ----------------------------------------------- #
from pygame import init, display, time, FULLSCREEN

# CLass Block ------------------------------------------------ #
class gameEngine:
    def __init__(self, settings):
        
        init()
        self.fps = settings['fps']
        self.width = settings['default-width']
        self.height = settings['default-height']
        self.fullscreen = settings['fullscreen']
        self.offline = settings['offline']
        self.debug_mode = settings['debug-mode']
        self.version = settings['version']
        self.mainClock = time.Clock()

        if self.fullscreen:
            self.screen = display.set_mode((self.width, self.height), FULLSCREEN)
        else:
            self.screen = display.set_mode((self.width, self.height))
        
    def get_mainClock(self):
        return self.mainClock