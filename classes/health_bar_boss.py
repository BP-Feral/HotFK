import math
import pygame

def downscale_2x(surface, scale):
    new_surface = pygame.transform.scale(surface, (surface.get_width() * scale, surface.get_height() * scale))
    return new_surface

class healthBarBoss:
    def __init__(self, color, max_health, scale):
        self.max_health = max_health
        self.current_health = max_health

        left_frame_base = pygame.image.load('./resources/health/frame_left.png').convert_alpha()
        middle_frame_base = pygame.image.load('./resources/health/frame_middle.png').convert_alpha()
        right_frame_base = pygame.image.load('./resources/health/frame_right.png').convert_alpha()

        left_fill_base = pygame.image.load('./resources/health/fill_left.png').convert_alpha()
        middle_fill_base = pygame.image.load('./resources/health/fill_middle.png').convert_alpha()
        right_fill_base = pygame.image.load('./resources/health/fill_right.png').convert_alpha()

        self.left_frame = downscale_2x(left_frame_base, scale)
        self.middle_frame = downscale_2x(middle_frame_base, scale)
        self.right_frame = downscale_2x(right_frame_base, scale)

        self.left_fill = downscale_2x(left_fill_base, scale)
        self.middle_fill = downscale_2x(middle_fill_base, scale)
        self.right_fill = downscale_2x(right_fill_base, scale)

        self.update_color(color)

        self.tile_size = self.middle_fill.get_width()
        self.length = 86
        self.total_length = self.left_fill.get_width() + self.tile_size * self.length - self.tile_size + self.right_fill.get_width()

        self.surface = pygame.Surface((self.total_length, 120), pygame.SRCALPHA, 32).convert_alpha()

        self.get_left_percentage()
        self.render_surface()

        frame_length = self.left_frame.get_width() + self.right_frame.get_width() + self.middle_frame.get_width() * 64
        self.frame_surface = pygame.Surface((frame_length, 120), pygame.SRCALPHA, 32).convert_alpha()
        #print(self.frame_surface.get_width())
        self.frame_surface.blit(self.left_frame, (0, 0))
        for i in range(15, 98):
            self.frame_surface.blit(self.middle_frame, (self.tile_size*i, 0))
        self.frame_surface.blit(self.right_frame, (self.frame_surface.get_width()-self.right_frame.get_width() - self.middle_frame.get_width()/2, 0))

    def get_left_percentage(self):
        self.percentage = math.ceil(self.current_health / self.max_health * self.length)

    def render_surface(self):
        self.surface = pygame.Surface((self.total_length, 120), pygame.SRCALPHA, 32).convert_alpha()
        self.get_left_percentage()
        #print(str(self.percentage) + "%")
        # Fill Health Surface
        if self.percentage == self.length:
            self.surface.blit(self.left_fill, (0, 0))
            for i in range(1, self.percentage):
                self.surface.blit(self.middle_fill, (self.tile_size*i, 0))
            self.surface.blit(self.right_fill, (self.tile_size*self.percentage, 0))

        elif 0 < self.percentage <= self.length - 1:
            self.surface.blit(self.left_fill, (0, 0))
            for i in range(1, self.percentage):
                self.surface.blit(self.middle_fill, (self.tile_size * i, 0))
            self.surface.blit(self.right_fill, (self.tile_size * self.percentage, 0))

        elif self.percentage <= 0:
            #print("critical point")
            self.surface.blit(self.right_fill, (0, 0))

    def update_color(self, color):
        vars = [pygame.PixelArray(self.left_fill), pygame.PixelArray(self.middle_fill), pygame.PixelArray(self.right_fill)]
        for var in vars:
            if color == "green":
                var.replace((134,134,134), (55,148,110))
                var.replace((166,166,166),(106,190,48))

            elif color == "red":
                var.replace((134,134,134), (172,50,50))
                var.replace((166,166,166),(217,87,99))

            else:
                pass
        del vars

    def create(self, screen, x, y):
        self.x = x
        self.y = y
        self.frame_start = self.x - self.left_frame.get_width() + self.middle_frame.get_width() * 3

        self.screen = screen
        self.update(self.current_health)

    def update(self, current_health):
        if current_health >= 0:
            self.current_health = current_health
            print(current_health)
            self.render_surface()

            self.screen.blit(self.surface, (self.x, self.y))
            self.screen.blit(self.frame_surface, (self.frame_start, self.y))

    def get_width(self):
        return self.total_length