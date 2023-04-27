import os, sys
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"

import pygame

from scenes.options import OptionsLoop
from scenes.splash_art import SplashLoop
from scenes.menu import MenuLoop

from classes.mixer import Mixer
from classes.settings import Settings
from classes.particle import ParticleManager
from classes.console import ChatConsole
from classes.text_widget import TextWidget
from classes.discord import Discord

from maintenance import load_image, allowed_resolutions


# GameEngine Class ============================================= #
class GameEngine():

    def __init__(self):

        # Initializie Core Functions
        pygame.init()
        pygame.display.init()

        self.mainClock = pygame.time.Clock()
        self.settings = Settings()
        self.mixer = Mixer(self.settings)

        self.fps = self.settings.get_fps()
        pygame.mouse.set_visible(False)
        self.fade_state = 0

        game_icon = pygame.image.load('resources/images/icons/icon.ico')
        pygame.display.set_caption('Heroes of the Fallen Kingdom')
        pygame.display.set_icon(game_icon)

        # Load Settings
        self.load_settings()

        # self.activity = DiscordActivity()
        self.particleManager = ParticleManager(self.settings)
        self.chatConsole = ChatConsole(self.settings, self.mixer, self.screen)
        self.textWidget = TextWidget()
        # Start Background Music
        self.mixer.music_play('resources/sounds/Dark_Fog.mp3', -1, 1000)
        self.game_state = 'Just Started'

        self.discord = Discord(self.mixer)
        # Load Background
        self.background = load_image("resources/images/backgrounds/background.png").convert()
        self.background = pygame.transform.scale(self.background, (self.window_width + 100, self.window_height + 100))

    def load_settings(self):

        # Load Window Config
        self.window_width = self.settings.get_width()
        self.window_height = self.settings.get_height()
        # Load Sound Config
        self.mixer.update_music_volume()
        self.mixer.update_sound_volume()

        # Get Monitor Info
        info = pygame.display.Info()

        # Load Monitor Info
        if self.settings.get_native() == True:
            self.window_width = info.current_w
            self.window_height = info.current_h
            self.settings.set_width(self.window_width)
            self.settings.set_height(self.window_height)

            # Update Settings with new Resoulution
            self.settings.write_to_file()

        # Adjust Window Size
        if allowed_resolutions(self.window_width, self.window_height) == False:
            self.settings.set_width(1152)
            self.settings.set_height(648)
            self.window_width = self.settings.get_width()
            self.window_height = self.settings.get_height()

            # Update Settings with new Resoulution
            self.save_settings()

        # Set / Modify - Display
        if self.settings.get_fullscreen():
            self.screen = pygame.display.set_mode((self.window_width, self.window_height), pygame.FULLSCREEN, 0)
        else:
            self.screen = pygame.display.set_mode((self.window_width, self.window_height), pygame.NOFRAME, depth=0)

    def save_settings(self):
        self.settings.write_to_file()

    def update_display(self):

        self.fade_in(self.screen)
        pygame.display.update()
        self.mainClock.tick(self.fps)

    def fade(self, surf, direction):
        surf = surf.copy()
        fade = 0
        while fade < 20:
            fade += 1
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            self.screen.blit(surf,(0,0))
            black_surf = surf.copy()
            black_surf.fill((10,10,10))
            if direction == 1:
                black_surf.set_alpha(int(255/20*fade))
            else:
                black_surf.set_alpha(int(255-255/20*fade))
            self.screen.blit(black_surf,(0,0))
            pygame.display.update()
            self.mainClock.tick(self.fps)
        self.fade_state = 20

    def fade_in(self, surf):
        if self.fade_state > 0:
            self.fade_state -= 1
            black_surf = surf.copy()
            black_surf.fill((10,10,10))
            black_surf.set_alpha(int(255/20*self.fade_state))
            surf.blit(black_surf,(0,0))


# Options View ================================================= #
    def options_loop(self):
        OptionsLoop(self)
# Splash Art View ============================================== #
    def splash_art_loop(self):
        SplashLoop(self)
# Menu View ==================================================== #
    def menu_loop(self):
        MenuLoop(self)