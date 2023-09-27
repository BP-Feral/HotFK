# ==============================================================
import math
import random
import pygame
from classes.health_bar_rank_1 import healthBarRank1

def upscale_random(image):
    scale = random.uniform(2, 3)
    return pygame.transform.scale(image, (image.get_width() * scale, image.get_height() * scale))

# Class BLock ==================================================
class Enemy():
    def __init__(self, x, y, speed, standby_image, rank, max_health, aggro_radius=100, neutral=False):
        self.DEBUG_STATS = False

        if int(rank) == 1:
            self.rank = 1
            self.healthBar = healthBarRank1(max_health)

        self.health = max_health
        # Debug stats
        self.color = (200, 255, 0)
        self.aggro = False

        self.aggro_radius = aggro_radius
        self.pos = pygame.Vector2(x, y)
        self.speed = speed

        self.image_base = pygame.image.load(standby_image).convert_alpha()
        #self.image = pygame.transform.scale(self.image_base, (self.image_base.get_width() * 2, self.image_base.get_height() * 2))
        self.image = upscale_random(self.image_base)
        # middleware
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.draw_offset = self.width//2

    def update(self, object_list, screen):
        for object in object_list:
            if self.health <= 0:
                return
            player_pos = object.get_center()
            distance = player_pos.distance_to(self.pos)

            if distance <= self.aggro_radius:
                direction = player_pos - self.pos
                direction.normalize_ip()

                deviation_angle = random.uniform(-math.pi/4, math.pi/4)
                direction.rotate_ip(math.degrees(deviation_angle))

                virtual_speed = self.speed + random.randrange(-1, +1)
                self.pos += direction * virtual_speed

                self.color = (255, 0, 0) # Aggro radius color
                pygame.draw.line(screen, (255, 255, 0), self.pos, player_pos, 2)
            else:
                self.color = (0, 255, 0) # Not aggro radius color
            
            self.healthBar.update(screen, self.pos.x, self.pos.y, self.health)
    # Draw
    def draw(self, screen):
        screen.blit(self.image, self.pos - pygame.Vector2(self.draw_offset, self.draw_offset))
        if self.DEBUG_STATS == True:
            pygame.draw.rect(screen, (255, 0, 0), (int(self.pos[0] - self.draw_offset), int(self.pos[1] - self.draw_offset), self.image.get_width(), self.image.get_height()), 2)
            pygame.draw.circle(screen, self.color, self.pos, self.aggro_radius, 2)
    
    def getRect(self):
        return pygame.Rect(self.pos[0], self.pos[1], self.width, self.height)

    def getPos(self):
        return self.pos

    def reduceHealth(self, amount):
        self.health -= amount
    
    def getHealth(self):
        return self.health