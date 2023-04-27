# Setup Python ----------------------------------------------- #
from maintenance import custom_mouse_highlight, update_fps, load_image
from loops.options import options_loop

import pygame


# Tutorial Loop ---------------------------------------------- #
def tutorial_loop(game_engine, particle_handler, chat_console):

    # Get Context
    game_engine.update_discord_status("Editing new 'room'")
    cursor_img, cursor_rect = custom_mouse_highlight()
    screen = pygame.display.get_surface()
    mainClock = game_engine.mainClock

    ###
    player_image = pygame.image.load('./resources/images/entities/player/player.png')
    player_location = [50, 50]

    moving = [0, 0, 0, 0]
    speed = 10
    # checkers = load_image("debugging/checkers.png").convert()

    base_font = pygame.font.Font("./resources/fonts/VcrOsdMono.ttf", 20)


# Loop Start ------------------------------------------------- #
    running = True
    while running:

        # Call required updates
        game_engine.updates()

        # Reset Frame
        screen.fill(0)

        # Mouse
        mx, my = pygame.mouse.get_pos()
        cursor_rect.center = (mx, my)


# Events ----------------------------------------------------- #
        for event in pygame.event.get():
            chat_console.update(event)

            if event.type == pygame.KEYDOWN:

                if chat_console.active == False:
                    if event.key == pygame.K_a:
                        moving[0] = 1
                        moving[1] = 0
                    if event.key == pygame.K_d:
                        moving[0] = 0
                        moving[1] = 1
                    if event.key == pygame.K_w:
                        moving[2] = 1
                        moving[3] = 0
                    if event.key == pygame.K_s:
                        moving[2] = 0
                        moving[3] = 1

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_ESCAPE:
                    if chat_console.active == True:
                        print("TRUE")
                        break
                    if chat_console.active == False:
                        print("FALSE")
                        game_engine.mixer.sound_play('resources/sounds/UI_click.mp3')
                        options_loop(game_engine, particle_handler, chat_console, None)

                if event.key == pygame.K_a:
                    moving[0] = 0
                if event.key == pygame.K_d:
                    moving[1] = 0
                if event.key == pygame.K_w:
                    moving[2] = 0
                if event.key == pygame.K_s:
                    moving[3] = 0


# Render ----------------------------------------------------- #
        # Console and mouse
        chat_console.draw()
        screen.blit(cursor_img, cursor_rect)
        screen.blit(update_fps(mainClock, base_font), (10,0))


# Update ----------------------------------------------------- #
        pygame.display.flip()

        # framerate control
        mainClock.tick(60)