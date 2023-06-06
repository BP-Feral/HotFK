# Setup Python ----------------------------------------------- #
from maintenance import custom_mouse, load_image, show_fps

import pygame

from scenes.options import OptionsLoop

# Tutorial Loop ---------------------------------------------- #
def DebuggerLoop(game_engine):

    # Get Context
    game_engine.discord.update_discord_status("Editing new 'room'")
    cursor_img, cursor_rect = custom_mouse()

    tile_size = 64
    ###
    player_image = pygame.image.load('./resources/images/entities/player/player.png')
    player_location = [50, 50]

    moving = [0, 0, 0, 0]
    speed = 10
    checkers = load_image("./resources/images/debug/checkers.png").convert()

    base_font = pygame.font.Font("./resources/fonts/Thintel.ttf", 20)


# Loop Start ------------------------------------------------- #
    running = True
    while running:

        # Call required updates
        game_engine.discord.tick()

        # Reset Frame
        game_engine.screen.fill((0, 0, 0))

        # Mouse
        mx, my = pygame.mouse.get_pos()
        cursor_rect.center = (mx, my)


# Events ----------------------------------------------------- #
        for event in pygame.event.get():
            game_engine.chatConsole.update(event)

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    if game_engine.chatConsole.active == True:
                        print("TRUE")
                        break
                    if game_engine.chatConsole.active == False:
                        print("FALSE")
                        game_engine.mixer.sound_play('resources/sounds/UI_click.mp3')
                        if OptionsLoop(game_engine) == "leave_state":
                            running = False
                            return

                if event.key == pygame.K_a:
                    moving[0] = 0
                if event.key == pygame.K_d:
                    moving[1] = 0
                if event.key == pygame.K_w:
                    moving[2] = 0
                if event.key == pygame.K_s:
                    moving[3] = 0

            if event.type == pygame.KEYDOWN:

                if game_engine.chatConsole.active == False:
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


# Render ----------------------------------------------------- #
        # Console and mouse
        for i in range(40):
            for j in range(20):
                game_engine.screen.blit(checkers, (i*tile_size, j*tile_size))

        game_engine.chatConsole.draw()
        game_engine.screen.blit(cursor_img, cursor_rect)
        game_engine.screen.blit(show_fps(game_engine.mainClock, base_font), (10,0))


# Update ----------------------------------------------------- #
        game_engine.update_display()