import pygame

class healthBarRank1:
    def __init__(self, max_health):
        self.GREEN = (55, 148, 110)

        #self.health_rect_x = 0
        #self.health_rect_y = 0

        self.max_health = max_health
        self.current_health = max_health
        self.frame_rank_1 = pygame.image.load('./resources/health/frame_rank_1.png').convert_alpha()
        self.frame_rank_1 = pygame.transform.scale(self.frame_rank_1, (self.frame_rank_1.get_width() * 2, self.frame_rank_1.get_height() * 2))
        self.frame_rank_1.set_colorkey((255, 0, 255))

        self.pixel_offset = self.frame_rank_1.get_width()/22*1
        self.total_width = self.frame_rank_1.get_width()/22*20
        self.health_rect_width = self.total_width
        self.health_rect_height = self.frame_rank_1.get_height()/2

    def reduceHealth(self, amount):
        self.current_health -= amount

    def update(self, screen, x, y, health):
        self.current_health = health
        self.health_rect_width = self.current_health * self.max_health // 100
        if self.current_health >= 0:
            screen.blit(self.frame_rank_1, (x - self.health_rect_width//2-self.pixel_offset, y - 64))
            pygame.draw.rect(screen, self.GREEN, (int(x - self.health_rect_width//2-self.pixel_offset + self.pixel_offset), int(y-64+self.pixel_offset), int(self.health_rect_width), int(self.health_rect_height)))