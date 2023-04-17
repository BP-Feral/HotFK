# Setup Python ----------------------------------------------- #
from pygame import mouse
from maintenance import load_image


# CLass Block ------------------------------------------------ #
class Button:
    def __init__(self, x, y, button_image, button_hover_image, hover_offset):

        # Positon
        self.x = x
        self.y = y

        # Images
        self.image = load_image(button_image)
        self.hover = load_image(button_hover_image)

        # Cogs
        self.active = self.image
        self.hover_offset = hover_offset

        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

        self.clicked = False


# Functions -------------------------------------------------- #
    def draw(self, screen):
        action = False
        
        # Get mouse position
        pos = mouse.get_pos()

        # Check mouse hover and clicked condition
        if self.rect.collidepoint(pos):
            self.active = self.hover
            self.rect.topleft = (self.x, self.y - self.hover_offset)

            if mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                action = True

        else:
            self.active = self.image
            self.rect.topleft = (self.x, self.y)

        if mouse.get_pressed()[0] == 0:
            self.clicked = False

        # Render
        screen.blit(self.active, (self.rect.x, self.rect.y))

        # Return true when clicked
        return action