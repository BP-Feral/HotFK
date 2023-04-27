import pygame


# Text Widget Class ============================================ #
class TextWidget():
    def __init__(self):
        self.font_color = (255, 255, 255)

    def color(self, font_color):
        match font_color:
            case 'red':
                self.font_color = (255, 0, 0)
            case 'green':
                self.font_color = (0, 255, 0)
            case 'blue':
                self.font_color = (0, 0, 255)
            case 'white':
                self.font_color = (255, 255, 255)
            case 'black':
                self.font_color = (0, 0, 0)
            case _:
                self.font_color = font_color

    def write(self, screen, x, y, font_size, aligned, message_list, center_x=False, center_y=False):
        self.font = pygame.font.Font('resources/fonts/Thintel.ttf', font_size)

        text_width = 0; text_height = 0

        for line in message_list:
            temp_text = self.font.render(line, True, self.font_color)
            text_width = max(text_width, temp_text.get_width())
            text_height += temp_text.get_height()

        notif_widget = pygame.Surface((text_width, text_height), pygame.SRCALPHA, 32)
        notif_widget.convert_alpha()

        blits = []
        for index, line in enumerate(message_list):
            line_surface = self.font.render(message_list[index], True, self.font_color)
            blits.append(line_surface)

        for i, blit in enumerate(blits):
            if aligned == 'left':
                notif_widget.blit(blit, (0, i * blit.get_height()))
            elif aligned == 'right':
                notif_widget.blit(blit, (text_width - blit.get_width(), i * blit.get_height()))
            elif aligned == 'center':
                notif_widget.blit(blit, ((text_width - blit.get_width()) // 2, i * blit.get_height()))

        if center_x == True and center_y == True:
            screen.blit(notif_widget, (x - notif_widget.get_width() // 2, y - notif_widget.get_height() // 2))
        elif center_x == True and center_y == False:
            screen.blit(notif_widget, (x - notif_widget.get_width() // 2, y))
        elif center_x == False and center_y == True:
            screen.blit(notif_widget, (x, y - notif_widget.get_height() // 2))