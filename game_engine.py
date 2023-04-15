# Setup Python ----------------------------------------------- #
from pygame import init, display, time, FULLSCREEN, mouse, image
from classes.mixer import Mixer

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
        self.mixer = Mixer()

        mouse.set_visible(False)

        if self.fullscreen:
            self.screen = display.set_mode((self.width, self.height), FULLSCREEN)
        else:
            self.screen = display.set_mode((self.width, self.height))
        
        game_icon = image.load('resources/images/icons/icon.ico')
        display.set_icon(game_icon)
        display.set_caption("Heroes of the Fallen Kingdom")