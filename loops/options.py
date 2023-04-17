# Setup Python ----------------------------------------------- #
from maintenance import load_image, custom_mouse, settings
from classes.button import Button

import pygame


# Options Loop ----------------------------------------------- #
def options_loop(game_engine, particle_handler, chat_console):

    # Get Context
    game_engine.update_discord_status("Checking the settings")
    cursor_img, cursor_rect = custom_mouse()
    screen = pygame.display.get_surface()
    mainClock = game_engine.mainClock

    # Load Background
    background = load_image("resources/images/backgrounds/background.png")

    # Load Buttons
    button_up = Button(1000, 400, "resources/images/buttons/up.png", "resources/images/buttons/up_hover.png", 2)
    #### TODO button_down = Button(1000, 400, "resources/images/buttons/up.png", "resources/images/buttons/up_hover.png", 2)

    # Particles Event
    PARTICLE_EVENT = pygame.USEREVENT + 1
    pygame.time.set_timer(PARTICLE_EVENT, 100)

    # Fonts
    base_font = pygame.font.Font(None, 32)
    options_rect = pygame.Rect(1920 / 2 - 400, 100, 800, 30)


# Loop Start  ------------------------------------------------ #
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

        # Draw Buttons
        if button_up.draw(screen):
            settings["sound-volume"] = float(float(settings["music-volume"]) - 0.1)
            print(settings["sound-volume"])


# Events ----------------------------------------------------- #
        for event in pygame.event.get():
            chat_console.update(event)

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    game_engine.mixer.sound_play('resources/sounds/UI_click.mp3')
                    running = False
            if event.type == PARTICLE_EVENT:
                particle_handler.add_particles()


# Render ----------------------------------------------------- #
        pygame.draw.rect(screen, (50, 50, 50), options_rect, 2)

        text_surface = base_font.render("Volume", True, (160, 0, 160))
        screen.blit(text_surface, (options_rect.x + options_rect.width // 2 - text_surface.get_width() // 2, options_rect.y + 5))

        music_volume_value = float(settings["music-volume"])
        music_volume = base_font.render(f"Music Volume: {int(music_volume_value * 10)}", True, (255, 255 ,255))
        screen.blit(music_volume, (options_rect.x + options_rect.width // 2 - music_volume.get_width() // 2, options_rect.y + 50))

        chat_console.draw()
        screen.blit(cursor_img, cursor_rect)


# Update ----------------------------------------------------- #
        pygame.display.flip()
        mainClock.tick(game_engine.fps)