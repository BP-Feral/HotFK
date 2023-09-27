# ==============================================================
import pygame

def upscale4x(image):
    return pygame.transform.scale(image, (image.get_width() * 4, image.get_height() * 4))

# Class BLock ==================================================
class Player():
    def __init__(self, x, y, speed):
        self.DEBUG_STATS = False

        self.pos = pygame.Vector2(x, y)
        self.speed = speed

        # Base Images
        self.front_base = pygame.image.load('./resources/monsters/cyclop/cyclop_front.png').convert_alpha()
        self.left_base = pygame.image.load('./resources/monsters/cyclop/cyclop_left.png').convert_alpha()
        self.right_base = pygame.image.load('./resources/monsters/cyclop/cyclop_right.png').convert_alpha()
        self.back_base = pygame.image.load('./resources/monsters/cyclop/cyclop_back.png').convert_alpha()

        # Images
        self.front = upscale4x(self.front_base)
        self.left = upscale4x(self.left_base)
        self.right = upscale4x(self.right_base)
        self.back = upscale4x(self.back_base)

        # Global
        self.image = self.front
        self.center = (self.pos[0] + self.front.get_width()//2, self.pos[1] + self.front.get_height()//2)
        # middleware
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.draw_offset = self.width//2
        # Self Stats
        self.moving_left = False
        self.moving_right = False
        self.moving_up = False
        self.moving_down = False
        self.player_movement = [0, 0]

        self.rect = pygame.Rect(self.pos[0], self.pos[1], self.image.get_width(), self.image.get_height())

    # Input events
    def move(self, keys):
        if keys[pygame.K_w]:
            self.pos[1] -= self.speed
            self.image = self.back

        elif keys[pygame.K_s]:
            self.pos[1] += self.speed
            self.image = self.front

        if keys[pygame.K_a]:
            self.pos[0] -= self.speed
            self.image = self.left

        elif keys[pygame.K_d]:
            self.pos[0] += self.speed
            self.image = self.right

        if keys[pygame.K_LSHIFT]:
            self.speed = 12
        else:
            self.speed = 8

        self.rect = (self.pos[0], self.pos[1])
        self.center = self.pos
    # Draw on screen
    def draw(self, screen):
        screen.blit(self.image, self.pos - pygame.Vector2(self.draw_offset, self.draw_offset))
        if self.DEBUG_STATS:
            pygame.draw.rect(screen, (255, 0, 255), (int(self.pos[0]) - int(self.draw_offset), int(self.pos[1] - self.draw_offset), self.image.get_width(), self.image.get_height()), 1)

    # Functions
    def get_rect(self):
        return self.rect

    def get_center(self):
        return self.center