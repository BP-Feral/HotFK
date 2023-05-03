import os, sys
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"

import pygame

from scenes.options import OptionsLoop
from scenes.splash_art import SplashLoop
from scenes.menu import MenuLoop
from scenes.editor import EditorLoop

from classes.mixer import Mixer
from classes.settings import Settings
from classes.particle import ParticleManager
from classes.console import ChatConsole
from classes.text_widget import TextWidget
from classes.discord import Discord
from classes.steam import Steam

from maintenance import load_image

# GameEngine Class ============================================= #
class GameEngine():

    def __init__(self):

        # Initializie Core Functions
        pygame.init()
        pygame.display.init()

        self.mainClock = pygame.time.Clock()
        self.settings = Settings()
        self.mixer = Mixer(self.settings)
        self.discord = Discord(self.mixer)
        self.particleManager = ParticleManager(self.settings)
        self.textWidget = TextWidget()

        # Steam config
        self.steam = Steam()
        if self.steam.is_running():
            self.steam.get_current_user()

        # Load Sound Config
        self.mixer.update_music_volume()
        self.mixer.update_sound_volume()
        self.mixer.music_play('resources/sounds/Dark_Fog.mp3', -1, 1000)

        self.game_state = 'Just Started'
        self.fade_state = 0

        self.fps = self.settings.get_fps()
        pygame.mouse.set_visible(False)

        self.res_scale = 1
        info = pygame.display.Info()
        print(f"identified {info.current_w}x{info.current_h}")

        if info.current_h == 1080:
            self.window_width = 1920
            self.window_height = 1080
            self.settings.set_width(1920)
            self.settings.set_height(1080)
            self.settings.write_to_file()
        else:
            self.adjust_video_settings(info)

        print(f"fullscreened at {self.window_width}x{self.window_height}")
        self.screen = pygame.display.set_mode((self.window_width, self.window_height), pygame.FULLSCREEN, 0)
        self.chatConsole = ChatConsole(self.settings, self.mixer, self.screen, self)
        game_icon = pygame.image.load('resources/images/icons/icon.ico')
        pygame.display.set_caption('Heroes of the Fallen Kingdom')
        pygame.display.set_icon(game_icon)
        # Load Background
        self.background = load_image("resources/images/backgrounds/background.png").convert()
        self.background = pygame.transform.scale(self.background, (self.window_width + 100, self.window_height + 100))

    def adjust_video_settings(self, info):
        self.res_scale = info.current_h / 1080
        print(f"scaling at {self.res_scale} factor")
        self.window_height = int(1080 * self.res_scale)
        self.window_width = int(1920 * self.res_scale)
        print(f"New resolution is {self.window_width}x{self.window_height}")
        self.settings.set_width(self.window_width)
        self.settings.set_height(self.window_height)
        self.settings.write_to_file()

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
# Map Editor View ============================================== #
    def editor_loop(self):
        EditorLoop(self)