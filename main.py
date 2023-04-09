# Setup Python ----------------------------------------------- #
from game_engine import gameEngine
from maintenance import clear_project
from pygame import mixer
from loops.disclaimer import disclaimer_loop
from loops.menu import menu_loop

# Init ------------------------------------------------------- #
settings = {
    "fps": 60, 
    "default-width": 1920, 
    "default-height": 1080, 
    "fullscreen": True, 
    "offline": True, 
    "debug-mode": True, 
    'version': "pre-0.0.6a"
}

# Engine Instance -------------------------------------------- #
game_engine = gameEngine(settings)

# Mixer Instance
bg_music = mixer.music.load('resources/sounds/Dark_Fog.mp3')
mixer.music.play(-1)



# Run the game ----------------------------------------------- #
disclaimer_loop(game_engine)
menu_loop(game_engine, mixer)

# Clear the project temporary files -------------------------- #
clear_project()