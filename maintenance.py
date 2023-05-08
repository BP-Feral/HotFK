import pygame, subprocess

def notification(font_size, message, img):
    font = pygame.font.Font('resources/fonts/Thintel.ttf', font_size)
    notif_msg = font.render(message, True, (255, 255, 255))
    notif_widget = pygame.Surface((notif_msg.get_width(), notif_msg.get_height()))
    notif_widget.fill((255, 0 ,0))
    notif_box = pygame.Surface((notif_widget.get_width() + 100, notif_widget.get_height() + 20))
    notif_box.fill((0, 255 ,0))
    new_img = pygame.transform.scale(img, (50, 50))
    notif_box.blit(new_img, (10, 10))
    return notif_box

def process_exists(process_name):
    call = 'TASKLIST', '/FI', 'imagename eq %s' % process_name
    # use buildin check_output right away
    output = subprocess.check_output(call).decode()
    # check in last line for process name
    last_line = output.strip().split('\r\n')[-1]
    # because Fail message could be translated
    return last_line.lower().startswith(process_name.lower())

def load_image(path):
    temp = pygame.image.load(path).convert_alpha()
    surface = pygame.transform.scale(temp, (temp.get_width() * 2, temp.get_height() * 2))
    return surface

def custom_mouse():
    cursor = pygame.image.load("resources/images/cursors/mouse.png").convert_alpha()
    cursor.set_colorkey((0, 0, 0))
    rect = cursor.get_rect()
    return cursor, rect

def console_push(message):
    # TODO display console messages in game
    print(message)