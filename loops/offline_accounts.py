# Setup Python ----------------------------------------------- #
import pygame, sys

from maintenance import clear_project, load_image, console_push, custom_mouse
from classes.button import Button


# Character Seleection Loop ---------------------------------- #
def offline_account_loop(game_engine, particle_handler, chat_console):

    # Get Context
    game_engine.update_discord_status("Character selection")
    cursor_img, cursor_rect = custom_mouse()
    screen = pygame.display.get_surface()
    mainClock = game_engine.mainClock

    # Load Background
    background = load_image("resources/images/backgrounds/background.png")

    # Load Buttons
    b0 = Button(1450, 220, "resources/images/buttons/new.png", "resources/images/buttons/new_hover.png", 2)
    b1 = Button(1450, 220 + 1 * 120, "resources/images/buttons/empty.png", "resources/images/buttons/empty_hover.png", 2)
    b2 = Button(1450, 220 + 2 * 120, "resources/images/buttons/empty.png", "resources/images/buttons/empty_hover.png", 2)
    b3 = Button(1450, 220 + 3 * 120, "resources/images/buttons/empty.png", "resources/images/buttons/empty_hover.png", 2)
    buttons_list = [b0, b1, b2, b3]

    # Particles event
    PARTICLE_EVENT = pygame.USEREVENT + 1
    pygame.time.set_timer(PARTICLE_EVENT, 50)


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

        # Set Background
        screen.blit(background, (mx // 50 - 38, my // 50 - 21))

        # Draw Particles
        particle_handler.emit(screen)

        # Draw buttons
        for i in range(0, 4):
           if buttons_list[i].draw(screen):
            console_push(f"pressed button {i}")
            game_engine.mixer.sound_play('resources/sounds/UI_click.mp3')

            if i == 0:
                game_engine.update_discord_status("Zone One: White Bridge")


# Events ----------------------------------------------------- #
        for event in pygame.event.get():
            chat_console.update(event)

            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                clear_project()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    game_engine.mixer.sound_play('resources/sounds/UI_click.mp3')
                    running = False

            if event.type == PARTICLE_EVENT:
                particle_handler.add_particles()


# Render ----------------------------------------------------- #
        chat_console.draw()
        screen.blit(cursor_img, cursor_rect)


# Update ----------------------------------------------------- #
        pygame.display.flip()
        mainClock.tick(game_engine.fps)