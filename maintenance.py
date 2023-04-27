# Setup Python ----------------------------------------------- #
import shutil
import os
import subprocess
import pygame

from pygame import image, transform, Color


# Globals
settings = {
    "fps": 60,
    "default-width": 1920,
    "default-height": 1080,
    "fullscreen": True,
    "offline": True,
    "debug-mode": True,
    'version': "pre-0.0.8a",
    'sound-volume': 1,
    'music-volume': 1
}


# Mouse Functions -------------------------------------------- #
def custom_mouse():
    cursor = image.load("resources/images/cursors/mouse.png").convert_alpha()
    cursor.set_colorkey((0, 0, 0))
    rect = cursor.get_rect()
    return cursor, rect

def custom_mouse_highlight():
    cursor = image.load("resources/images/cursors/mouse_highlight.png").convert_alpha()
    cursor.set_colorkey((0, 0, 0))
    rect = cursor.get_rect()
    return cursor, rect


# Image Functions -------------------------------------------- #
def load_image(path):
    temp = image.load(path).convert_alpha()
    surface = transform.scale(temp, (temp.get_width() * 2, temp.get_height() * 2))
    del temp
    return surface


# Log messages to console ------------------------------------ #
def console_push(message):
    # TODO display console messages in game
    print(message)


# Log messages to notification widget
def notification(screen, message_list,x, y, font_size=20):

    base_font = pygame.font.Font('./resources/fonts/VcrOsdMono.ttf', font_size)

    max = 0
    item_count = 0
    for item in message_list:
        item_count += 1
        if len(item) > max:
            max = len(item)

    # Blank notif
    notif_widget = pygame.Surface((max*15, 20*item_count), pygame.SRCALPHA, 32)
    notif_widget.convert_alpha()

    # Append rows
    for i, item in enumerate(message_list):
        line_surface = base_font.render(message_list[i], True, (255, 255, 255))
        notif_widget.blit(line_surface, (0, i*font_size))

    screen.blit(notif_widget, (x, y))


# Check if a process is running (Discord) -------------------- #
def process_exists(process_name):
    call = 'TASKLIST', '/FI', 'imagename eq %s' % process_name
    # use buildin check_output right away
    output = subprocess.check_output(call).decode()
    # check in last line for process name
    last_line = output.strip().split('\r\n')[-1]
    # because Fail message could be translated
    return last_line.lower().startswith(process_name.lower())


# Show FPS
def update_fps(clock, font):
	fps = str(int(clock.get_fps()))
	fps_text = font.render(fps, 1, Color((20, 200, 20)))
	return fps_text


# Remove cache ----------------------------------------------- #
def clear_project():
    try:
        location = "./"
        dir = "__pycache__"

        path = os.path.join(location, dir)

        shutil.rmtree(path)
    except:
        console_push("Main cache could not be removed")

    try:
        location = "./loops"
        dir = "__pycache__"

        path = os.path.join(location, dir)

        shutil.rmtree(path)
    except:
        console_push("loops cache could not be removed")

    try:
        location = "./classes"
        dir = "__pycache__"

        path = os.path.join(location, dir)

        shutil.rmtree(path)
    except:
        console_push("class cache could not be removed")

    try:
        location = "./data"
        dir = "__pycache__"

        path = os.path.join(location, dir)

        shutil.rmtree(path)
    except:
        console_push("account cache could not be removed")
    
    try:
        location = "./scenes"
        dir = "__pycache__"

        path = os.path.join(location, dir)

        shutil.rmtree(path)
    except:
        console_push("scenes cache could not be removed")