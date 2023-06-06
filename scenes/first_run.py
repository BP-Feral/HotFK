# Python Setup =============================================== #
import time, pygame, sys

from classes.button import Button
from maintenance import custom_mouse


# First Run Loop ============================================= #
def FirstRunLoop(game_engine):

    game_engine.game_state = 'First Run'
    cursor_img, cursor_rect = custom_mouse()

    previous_time = time.time()

    button_save = Button(game_engine.settings.get_width() // 2, game_engine.settings.get_height() - 80, "resources/images/buttons/save.png", "resources/images/buttons/save_hover.png", 1)

# Loop Start ------------------------------------------------- #
    firstrun_loop = True
    while firstrun_loop:

        # Reset Frame
        game_engine.screen.fill(0)

        mx, my = pygame.mouse.get_pos()
        cursor_rect.center = (mx, my)

        dt = time.time() - previous_time
        previous_time = time.time()

# Events ----------------------------------------------------- #
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

# Render ----------------------------------------------------- #
        game_engine.textWidget.color((255, 255, 255))

        game_engine.textWidget.write(game_engine.screen, 50 / 100 * game_engine.window_width, 30 / 100 * game_engine.window_height, 80, 'center',
        ["< First Run Setup >"], True, True)

        game_engine.textWidget.write(game_engine.screen, 50 / 100 * game_engine.window_width, 45 / 100 * game_engine.window_height, 70, 'center',
            [f"Please confirm your initial settings <{game_engine.window_width}x{game_engine.window_height}>",
            "Changing anything will require you to relaunch the game."], True, False)

        if button_save.draw(game_engine.screen):
            game_engine.settings.write_to_file()
            game_engine.mixer.sound_play('resources/sounds/UI_click.mp3')
            return

        # Update Frame
        game_engine.screen.blit(cursor_img, cursor_rect)
        game_engine.update_display()