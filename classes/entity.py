import pygame
from maintenance import load_image

class Entity():
    def __init__(self, x, y, speed, image=str, e_type='enemy'):
        self.x = x
        self.y = y

        self.image = load_image(image)
        self.type = e_type

        self.speed = speed
        self.v_speed = 0
        self.h_speed= 0

        self.rect = pygame.Rect(self.x, self.y, self.image.get_width(), self.image.get_height())
    
    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))
    
    def update_rect(self):
        self.rect.topleft = (self.x, self.y)

    def update(self, event):
        if self.e_type == 'player':
            for event in events:
                if event.type == event.KEYUP:
                    if event.key == pygame.K_w:
                        self.v_speed = 0                
                    if event.key == pygame.K_s:
                        self.v_speed = 0
                    if event.key == pygame.K_a:
                        self.h_speed = 0
                    if event.key == pygame.K_d:
                        self.h_speed = 0

                if event.type == event.KEYDOWN:
                    if event.key == pygame.K_w:
                        self.v_speed -= 1
                    if event.key == pygame.K_s:
                        self.v_speed += 1
                    if event.key == pygame.K_a:
                        self.h_speed -= 1
                    if event.key == pygame.K_d:
                        self.h_speed += 1
        else:
            pass # TODO enemy AI

        if self.h_speed != 0:
            self.y += self.h_speed * self.speed
        if self.v_speed != 0:
            self.x += self.v_speed * self.speed

        self.update_rect()