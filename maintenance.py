# Setup Python ----------------------------------------------- #
import shutil
import os
import json

from pygame import image, transform, mouse
from data.template import data as template

json = json.dumps(template)


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

# Funcs ------------------------------------------------------ #
def load_image(path):
    temp = image.load(path).convert_alpha()
    surface = transform.scale(temp, (temp.get_width() * 2, temp.get_height() * 2))
    del temp
    return surface

# Log messages to console ------------------------------------ #
def console_push(message):
    #TODO display console messages in game
    print(message)

# Check Create Load account data ----------------------------- #
def check_for_account():
    try:
        dat = []
        f = open("./data/accounts.saved", "r")
        dat = f.readlines()
        f.close()

        print(dat)
        if dat == []:
            console_push("There are no accounts. Creating one")
            f = open("./data/accounts.saved", 'w')
            f.write(json)
            f.close()
        else:
            console_push("Some account data has been found")
            #TODO LOAD ACCOUNT DATA

    except FileNotFoundError:
        console_push("The account data file is corrupted or missing")
        console_push("Created a new one")
        with open('./data/accounts.saved', 'x'):
            pass

# Remove cache ----------------------------------------------- #
def clear_project():
    try:
        location = "./"
        dir = "__pycache__"

        path = os.path.join(location, dir)

        shutil.rmtree(path)
    except:
        print("Main cache could not be removed")

    try:
        location = "./loops"
        dir = "__pycache__"

        path = os.path.join(location, dir)

        shutil.rmtree(path)
    except:
        print("loops cache could not be removed")
    
    try:
        location = "./classes"
        dir = "__pycache__"

        path = os.path.join(location, dir)

        shutil.rmtree(path)
    except:
        print("class cache could not be removed")
    
    try:
        location = "./data"
        dir = "__pycache__"

        path = os.path.join(location, dir)

        shutil.rmtree(path)
    except:
        print("account cache could not be removed")