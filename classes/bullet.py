import pygame, math

class Bullet:
    def __init__(self, x, y):
        '''This class can be used to create projectiles and also manage them.'''
        self.pos = (x, y)
        mx, my = pygame.mouse.get_pos()
        self.dir = (mx - x, my - y)
        length = math.hypot(*self.dir)
        if length == 0.0:
            self.dir = (0, -1)
        else:
            self.dir = (self.dir[0]/length, self.dir[1]/length)
        angle = math.degrees(math.atan2(-self.dir[1], self.dir[0]))

        self.bullet = pygame.Surface((14, 4)).convert_alpha()
        self.bullet.fill((255, 255, 255))
        self.bullet = pygame.transform.rotate(self.bullet, angle)
        self.speed = 30

    def changed(self):
        self.bullet = pygame.Surface((22, 8)).convert_alpha()
        angle = math.degrees(math.atan2(-self.dir[1], self.dir[0]))
        self.bullet.fill((255, 0, 0))
        self.bullet = pygame.transform.rotate(self.bullet, angle)
        self.speed = 10

    def update(self):
        self.pos = (self.pos[0]+self.dir[0]*self.speed,
                    self.pos[1]+self.dir[1]*self.speed)

    def draw(self, surf):
        bullet_rect = self.bullet.get_rect(center = self.pos)
        surf.blit(self.bullet, bullet_rect)

    def get_rect(self):
        return self.bullet.get_rect(center = self.pos)