# Setup Python ----------------------------------------------- #
import shutil
import os
import subprocess

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


# Check if a process is running (Discord) -------------------- #
def process_exists(process_name):
    call = 'TASKLIST', '/FI', 'imagename eq %s' % process_name
    # use buildin check_output right away
    output = subprocess.check_output(call).decode()
    # check in last line for process name
    last_line = output.strip().split('\r\n')[-1]
    # because Fail message could be translated
    return last_line.lower().startswith(process_name.lower())

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