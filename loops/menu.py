# Setup Python ----------------------------------------------- #
import pygame, sys
import webbrowser
import time

from maintenance import clear_project, console_push, load_image, custom_mouse
from classes.button import Button
from loops.offline_accounts import offline_account_loop
from loops.options import options_loop


# Menu Loop -------------------------------------------------- #
def menu_loop(game_engine, particle_handler, chat_console):

    # Get Context
    game_engine.update_discord_status("Waiting in the menu")
    cursor_img, cursor_rect = custom_mouse()
    screen = pygame.display.get_surface()
    mainClock = game_engine.mainClock

    # Load Background
    background = load_image("resources/images/backgrounds/background.png").convert()

    # Load Buttons
    offline_banner = Button(450, 270, "resources/images/buttons/offline_banner.png", "resources/images/buttons/offline_banner_hover.png", 5, 1)
    online_banner = Button(1070, 270, "resources/images/buttons/online_banner.png", "resources/images/buttons/online_banner_hover.png", 5, 1)

    discord = Button(400, 900, "resources/images/buttons/discord.png", "resources/images/buttons/discord_hover.png", 0, 1)
    github = Button(260, 900, "resources/images/buttons/github.png","resources/images/buttons/github_hover.png", 0, 1)

    options = Button(1920-400-104, 900, "resources/images/buttons/options.png", "resources/images/buttons/options_hover.png", 0, 1)
    leave = Button(1920-260-104, 900, "resources/images/buttons/quit.png","resources/images/buttons/quit_hover.png", 0, 1)

    # Particles event
    PARTICLE_EVENT = pygame.USEREVENT + 1
    pygame.time.set_timer(PARTICLE_EVENT, 100)


# Loop Start ------------------------------------------------- #
    running = True
    while running:
        

        # Call required updates
        game_engine.updates()
        start = time.time()

        # Reset Frame
        screen.fill(0)

        # Mouse
        mx, my = pygame.mouse.get_pos()
        cursor_rect.center = (mx, my)

        # Set Background
        screen.blit(background, (mx // 50 - 38, my // 50 - 21))

        # Draw Particles
        particle_handler.emit(screen)

        # Draw buttons
        if offline_banner.draw(screen):
            if game_engine.settings.get_debug_mode():
                console_push("Offline clicked")
            game_engine.mixer.sound_play('resources/sounds/UI_click.mp3')
            offline_account_loop(game_engine, particle_handler, chat_console)
            game_engine.update_discord_status("Waiting in the menu")

        if online_banner.draw(screen):
            if game_engine.settings.get_debug_mode():
                console_push("Online clicked")
            game_engine.mixer.sound_play('resources/sounds/UI_click.mp3')

        if discord.draw(screen):
            game_engine.mixer.sound_play('resources/sounds/UI_click.mp3')
            webbrowser.open("https://discord.gg/xcEYBpn2k2")

        if github.draw(screen):
            webbrowser.open("https://github.com/pricob/HotFK")
            game_engine.mixer.sound_play('resources/sounds/UI_click.mp3')

        if options.draw(screen):
            game_engine.mixer.sound_play('resources/sounds/UI_click.mp3')
            options_loop(game_engine, particle_handler, chat_console)
            game_engine.update_discord_status("Waiting in the menu")

        if leave.draw(screen):
            game_engine.mixer.sound_play('resources/sounds/UI_click.mp3')
            pygame.quit()
            clear_project()
            sys.exit()


# Events ----------------------------------------------------- #
        for event in pygame.event.get():

            # Update Console / Chat
            chat_console.update(event)

            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                clear_project()
                sys.exit()

            if event.type == PARTICLE_EVENT:
                particle_handler.add_particles()


# Render ----------------------------------------------------- #
        chat_console.draw()
        screen.blit(cursor_img, cursor_rect)


# Update ----------------------------------------------------- #
        pygame.display.flip()

        # framerate control
        end = time.time()
        diff = end - start
        framerate = game_engine.settings.get_fps()
        delay = 1.0 / framerate - diff
        if delay > 0:
                time.sleep(delay)