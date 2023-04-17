# Setup Python ----------------------------------------------- #
import shutil
import os

from pygame import image, transform


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