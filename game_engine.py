import os, sys
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"

import pygame, moderngl
from array import array

from scenes.options import OptionsLoop
from scenes.splash_art import SplashLoop
from scenes.menu import MenuLoop
from scenes.editor import EditorLoop
from scenes.offline_accounts import OfflineLoop

from scenes.extras.debugger import DebuggerLoop
from scenes.extras.debugger2 import DebuggerLoop2
from scenes.extras.debugger3 import DebuggerLoop3
from scenes.extras.debugger4 import DebuggerLoop4
from scenes.extras.debugger5 import DebuggerLoop5

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
        pygame.event.set_grab(True)
        self.mainClock = pygame.time.Clock()
        self.settings = Settings()
        self.mixer = Mixer(self.settings)
        self.discord = Discord(self.mixer)
        self.particleManager = ParticleManager(self.settings)
        self.textWidget = TextWidget()

        self.time = 0
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

        game_icon = pygame.image.load('resources/images/icons/icon.ico')
        pygame.display.set_caption('Heroes of the Fallen Kingdom')
        pygame.display.set_icon(game_icon)
        if info.current_h == 1080:
            self.window_width = 1920
            self.window_height = 1080
            self.settings.set_width(1920)
            self.settings.set_height(1080)
            self.settings.write_to_file()
        else:
            self.adjust_video_settings(info)

        print(f"fullscreened at {self.window_width}x{self.window_height}")
        self.window = pygame.display.set_mode((self.window_width, self.window_height), pygame.FULLSCREEN | pygame.OPENGL | pygame.DOUBLEBUF, 0)
        self.screen = pygame.Surface((self.window_width, self.window_height))
        self.chatConsole = ChatConsole(self.settings, self.mixer, self.screen, self)

        # Open GL
        self.ctx = moderngl.create_context()
        quad_buffer = self.ctx.buffer(data=array('f', [
            -1.0, 1.0, 0.0, 0.0,
             1.0, 1.0, 1.0, 0.0,
            -1.0, -1.0, 0.0, 1.0,
             1.0, -1.0, 1.0, 1.0,
        ]))
        self.shader = self.ctx.program(
            vertex_shader='''
                #version 330 core

                in vec2 vert;
                in vec2 texcoord;
                out vec2 uvs;

                void main() {
                    uvs = texcoord;
                    gl_Position = vec4(vert, 0.0, 1.0);
                }
            ''',
            fragment_shader='''
                #version 330 core

                uniform sampler2D tex;

                in vec2 uvs;
                out vec4 f_color;

                void main() {
                    f_color = vec4(texture(tex, uvs).rgb , 1.0);
                }
            '''
        )

        # uniform float time;
        # vec2 sample_pos = vec2(uvs.x + sin(uvs.y * 0.1 + time * 0.01), uvs.y);

        self.render_object = self.ctx.vertex_array(self.shader, [(quad_buffer, '2f 2f', 'vert', 'texcoord')])

        # Load Background
        self.background = load_image("resources/images/backgrounds/background.png").convert()
        self.background = pygame.transform.scale(self.background, (self.window_width + 100, self.window_height + 100))

    def surf_to_texture(self, surf):
        tex = self.ctx.texture(surf.get_size(), 4)
        tex.filter = (moderngl.NEAREST, moderngl.NEAREST) # type: ignore
        tex.swizzle = 'BGRA'
        tex.write(surf.get_view('1'))
        return tex

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
        self.time += 1
        frame_tex = self.surf_to_texture(self.screen)
        frame_tex.use(0)
        self.shader['tex'] = 0
        # self.shader['time'] = self.time
        self.render_object.render(mode=moderngl.TRIANGLE_STRIP) # type: ignore

        pygame.display.flip()

        frame_tex.release()

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
            pygame.display.flip()
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
# Offline Accounts View ======================================== #
    def offline_loop(self):
        OfflineLoop(self)

# Debuger Scene ================================================ #
    def debugger_scene(self):
        DebuggerLoop(self)
# Debuger2 Scene =============================================== #
    def debugger_scene2(self):
        DebuggerLoop2(self)
# Debuger3 Scene =============================================== #
    def debugger_scene3(self):
        DebuggerLoop3(self)
# Debuger4 Scene =============================================== #
    def debugger_scene4(self):
        DebuggerLoop4(self)
# Debuger5 Scene =============================================== #
    def debugger_scene5(self):
        DebuggerLoop5(self)

# Debuger4 Scene =============================================== #