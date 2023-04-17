# Setup Python ----------------------------------------------- #
from game_engine import gameEngine
from maintenance import clear_project
from loops.disclaimer import disclaimer_loop
from loops.menu import menu_loop


# Engine Instance -------------------------------------------- #
game_engine = gameEngine()
game_engine.update_discord_status("Just Started")


# Start backround mixer -------------------------------------- #
game_engine.mixer.music_play('resources/sounds/Dark_Fog.mp3', -1, 2000)


# Run the game ----------------------------------------------- #
disclaimer_loop(game_engine)
menu_loop(game_engine)


# Clear temporary project files ------------------------------ #
game_engine.clear_discord_activity() # stop activity
clear_project()
exit()