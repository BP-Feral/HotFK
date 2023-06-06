# Setup Python =============================================== #
from maintenance import load_image
import pygame


# Button Class =============================================== #
class Button:
    def __init__(self, x, y, button_image, button_hover_image, scale):

        # Images
        hov = load_image(button_hover_image)
        img = load_image(button_image)

        self.image = pygame.transform.scale(img, (img.get_width() * scale, img.get_height() * scale))
        self.hover = pygame.transform.scale(hov, (hov.get_width() * scale, hov.get_height() * scale))

        # Positon
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

        # Cogs
        self.active = self.image

        self.clicked = False


# Functions ================================================== #
    def draw(self, screen):
        action = False

        # Get mouse position
        pos = pygame.mouse.get_pos()

        # Check mouse hover and clicked condition
        if self.rect.collidepoint(pos):
            self.active = self.hover
            self.rect.topleft = (self.rect.x, self.rect.y)
            pygame.draw.rect(screen, (255, 255, 255), (self.rect.x-2, self.rect.y-2, self.active.get_width()+4, self.active.get_height()+4), 2, 2)

            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                action = True

        else:
            self.active = self.image
            self.rect.topleft = (self.rect.x, self.rect.y)

        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False

        # Render
        screen.blit(self.active, (self.rect.x, self.rect.y))

        # Return true when clicked
        return action

    def flip(self, direction):
        if direction == "h" or direction == "horizontal":
            self.image = pygame.transform.flip(self.image, False, True)
            self.hover = pygame.transform.flip(self.hover, False, True)
        elif direction == "v" or direction == "vertical":
            self.image = pygame.transform.flip(self.image, True, False)
            self.hover = pygame.transform.flip(self.hover, True, False)
        else:
            self.image = pygame.transform.flip(self.image, True, True)
            self.hover = pygame.transform.flip(self.hover, True, True)

    def is_colliding(self, mouse_pos):
        if self.rect.collidepoint(mouse_pos):
            return True
        else:
            return False

    def update_pos(self, x, y):
        self.rect.x = x
        self.rect.y = y

    def get_rect(self):
        return (self.rect)