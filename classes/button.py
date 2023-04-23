# Setup Python ----------------------------------------------- #
from pygame import mouse, transform, draw
from maintenance import load_image


# CLass Block ------------------------------------------------ #
class Button:
    def __init__(self, x, y, button_image, button_hover_image, hover_offset, scale):

        # Positon
        self.x = x
        self.y = y

        # Quick Fix - button flickering
        hover_offset = 0

        # Images
        img = load_image(button_image)
        hov = load_image(button_hover_image)

        self.image = transform.scale(img, (img.get_width() * scale, img.get_height() * scale))
        self.hover = transform.scale(hov, (hov.get_width() * scale, hov.get_height() * scale))
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
            draw.rect(screen, (255, 255, 255), (self.x-2, self.y-self.hover_offset-2, self.active.get_width()+4, self.active.get_height()+self.hover_offset+4), 2, 2)

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

    def flip(self, direction):
        if direction == "h" or direction == "horizontal":
            self.image = transform.flip(self.image, False, True)
            self.hover = transform.flip(self.hover, False, True)
        elif direction == "v" or direction == "vertical":
            self.image = transform.flip(self.image, True, False)
            self.hover = transform.flip(self.hover, True, False)
        else:
            self.image = transform.flip(self.image, True, True)
            self.hover = transform.flip(self.hover, True, True)

    def is_colliding(self, mouse_pos):
        if self.rect.collidepoint(mouse_pos):
            return True
        else:
            return False

    def get_rect(self):
        return (self.rect)