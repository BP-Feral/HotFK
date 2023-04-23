# Setup Python ----------------------------------------------- #
import pygame

from game_engine import gameEngine
from maintenance import clear_project
from loops.disclaimer import disclaimer_loop
from loops.menu import menu_loop
from classes.console import Console
from classes.particle import Particle


# Engine Instance -------------------------------------------- #
game_engine = gameEngine()
if game_engine.discord_active == True:
    game_engine.update_discord_status("Just Started")


# Start backround mixer -------------------------------------- #
game_engine.mixer.music_play('resources/sounds/Dark_Fog.mp3', -1, 2000)

# Run the game ----------------------------------------------- #

# Console / Chat
screen = pygame.display.get_surface()
particle_handler = Particle()

chat_console = Console(screen, game_engine, particle_handler)

disclaimer_loop(game_engine)
menu_loop(game_engine, particle_handler, chat_console)


# Clear temporary project files ------------------------------ #
game_engine.clear_discord_activity() # stop activity
clear_project()
exit()