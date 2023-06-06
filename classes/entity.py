# ==============================================================
import pygame
from maintenance import load_image

# Class BLock ==================================================
class Entity():
    def __init__(self, x, y, speed, image_path, type, left_animation_frames = None, right_animation_frames = None):
        self.x = x
        self.y = y
        self.ID = type
        self.idle_image = load_image(image_path)
        self.idle_image = pygame.transform.scale(self.idle_image,
            (self.idle_image.get_width() * 2, self.idle_image.get_height() * 2))

        self.left_animation_frames = left_animation_frames # list
        self.right_animation_frames = right_animation_frames # list

        self.rght_image = self.idle_image
        self.left_image = pygame.transform.flip(self.idle_image, True, False)

        self.speed = speed
        self.moving_left = False
        self.moving_right = False
        self.moving_up = False
        self.moving_down = False
        self.player_movement = [0, 0]

        self.rect = pygame.Rect(x, y, self.idle_image.get_width(), self.idle_image.get_height())

    def getId(self):
        return self.ID

    def move(self, keys, chat_console):
            pass

    def draw(self, screen):
        screen.blit(self.idle_image, self.get_rect())

    def get_rect(self):
        return self.rect

    def get_movement(self):
        return (self.player_movement[0] * self.speed, self.player_movement[1] * self.speed)