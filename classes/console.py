# Setup Python ----------------------------------------------- #
import pygame

from maintenance import console_push
from scenes.tutorial3 import tutorial_loop3
from scenes.debugger import tutorial_loop

# CLass Block ------------------------------------------------ #
class Console:
    def __init__(self, screen, game_engine, particle_handler):

        # Get context
        self.screen = screen
        self.settings = game_engine.settings
        self.mixer = game_engine.mixer
        self.game_engine = game_engine
        self.particle_handler = particle_handler

        # Initialize a font
        self.base_font = pygame.font.Font('resources/fonts/VcrOsdMono.ttf', 20)
        self.user_text = "[all]: type here - or use /help"

        # Cogs
        self.input_rect = pygame.Rect(1, 1080 - 35, 140, 32)
        self.active = False
        self.allowed_chars = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 
                              'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 
                              '\\', '!', '?', '.', ',', "'", '"', '@', '#', '%', '^', '&', '*', '-', '_', '+', '=', '|', ':', ';', '<', '>', 
                              '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '(', ')', '[', ']', '{', '}']

        # Colors
        self.text_color = pygame.Color(255, 255, 255)
        self.color_active = pygame.Color('lightskyblue3')
        self.color_passive = pygame.Color('gray15')

        self.color = self.color_passive


# Updates ---------------------------------------------------- #
    def update(self, event):

        # Select by mouse
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.input_rect.collidepoint(event.pos) and self.render:
                if self.active == False:
                    self.user_text = ""
                self.active = True
            else:
                self.active = False
                self.user_text = "[all]: type here - or use /help"

        # Select by 'Grave' key
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_BACKQUOTE:
                if self.active == False:
                    self.user_text = ""
                self.active = True

        # Handle key presses once active
        if self.active == True:
            if event.type == pygame.KEYDOWN:

                # Handle Escape key
                if event.key == pygame.K_ESCAPE:
                    self.active = False
                    return

                # Handle Return key
                elif event.key == pygame.K_RETURN:
                    if self.user_text != "":
                        console_push(f"[Console][USER][CHAT]: {self.user_text}")

                        # Slash Commands
                        try:
                            if self.user_text[:6] == "/break":
                                return
                            if self.user_text[:6] == "/music":
                                args = self.user_text.split(' ')
                                if args[1] == "volume":
                                    self.settings.set_music_volume(round( float(args[2])/10, 1))
                                    self.mixer.update_music_volume()

                            elif self.user_text[:6] == "/sound":
                                args = self.user_text.split(' ')
                                if args[1] == "volume":
                                    self.settings.set_sound_volume(round( float(args[2])/10, 1))
                                    self.mixer.update_sound_volume()

                            elif self.user_text[:6] == "/debug":
                                args = self.user_text.split(' ')
                                if args[1] == "new" and args [2] == "room":
                                    self.user_text = ""
                                    tutorial_loop(self.game_engine, self.particle_handler, self)
                                if args[1] == "new" and args [2] == "room2":
                                    self.user_text = ""
                                    tutorial_loop3(self.game_engine, self.particle_handler, self)

                            # Clear the box
                            self.user_text = ""
                        except:
                            console_push("Chat error")
                            self.user_text = ""
                    return

                # Handle Backspace key
                elif event.key == pygame.K_BACKSPACE:
                    self.user_text = self.user_text[:-1]
                    return

                # Exclusive key for slash
                elif event.key == pygame.K_SLASH:
                    self.user_text += "/"
                    return

                # Exlusive key for space
                elif event.key == pygame.K_SPACE:
                    self.user_text += " "
                    return

                # Add text in the box
                elif event.unicode in self.allowed_chars:
                    self.user_text += event.unicode


# Functions -------------------------------------------------- #
    def is_active(self):
        return self.active


# Render ----------------------------------------------------- #
    def draw(self):

        if self.active:
            self.render = True
            self.color = self.color_active
            self.text_color = (255, 255, 255)

        else:
            self.render = self.settings.get_console_toggle()
            self.color = self.color_passive
            self.text_color = self.color_passive
            self.user_text = "[all]: type or use /help"

        text_surface = self.base_font.render(self.user_text, True, self.text_color)
        self.input_rect.w = max(text_surface.get_width() + 30, 350)

        if self.render:
            pygame.draw.rect(self.screen, self.color, self.input_rect, 2)
            self.screen.blit(text_surface, (self.input_rect.x + 5, self.input_rect.y + 5))