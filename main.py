# Main File =================================================== #
if __name__ == '__main__':

    # Imports
    from game_engine import GameEngine
    from scenes.first_run import FirstRunLoop

    # Initialize Application
    game_engine = GameEngine()

    print(game_engine.settings.get_first_run())
    if game_engine.settings.get_first_run() == True:
        game_engine.settings.set_first_run(False)
        FirstRunLoop(game_engine)

    game_engine.splash_art_loop()
    game_engine.menu_loop()