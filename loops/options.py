# Setup Python ----------------------------------------------- #
from maintenance import load_image, custom_mouse, notification
from classes.button import Button

import pygame


# Options Loop ----------------------------------------------- #
def options_loop(game_engine, particle_handler, chat_console, state_running):

    # Get Context
    game_engine.update_discord_status("Checking the settings")
    cursor_img, cursor_rect = custom_mouse()
    screen = pygame.display.get_surface()
    mainClock = game_engine.mainClock

    # Load Background
    background = load_image("resources/images/backgrounds/background.png")

    # Load Buttons (Music Volume)
    music_volume_up = Button(1250, 140, "resources/images/buttons/up.png", "resources/images/buttons/up_hover.png", 2, 0.5)
    music_volume_down = Button(1300, 140, "resources/images/buttons/up.png", "resources/images/buttons/up_hover.png", 2, 0.5)
    music_volume_down.flip("horizontal")

    # Load Buttons (Sound Volume)
    sound_volume_up = Button(1250, 190, "resources/images/buttons/up.png", "resources/images/buttons/up_hover.png", 2, 0.5)
    sound_volume_down = Button(1300, 190, "resources/images/buttons/up.png", "resources/images/buttons/up_hover.png", 2, 0.5)
    sound_volume_down.flip("horizontal")

    # Load Buttons (Console Chat)
    console_toggle = Button(1300, 340, "resources/images/buttons/box.png", "resources/images/buttons/box_hover.png", 2, 0.5)
    console_toggle_bool = game_engine.settings.get_console_toggle()
    # Load Buttons (Menu)
    button_save = Button(1178, 800, "resources/images/buttons/save.png", "resources/images/buttons/save_hover.png", 2, 1)
    button_reset = Button(978, 800, "resources/images/buttons/reset.png", "resources/images/buttons/reset_hover.png", 2, 1)

    button_exit = Button(778, 800, "resources/images/buttons/exit.png", "resources/images/buttons/exit_hover.png", 2 ,1)
    # Particles Event
    PARTICLE_EVENT = pygame.USEREVENT + 1
    pygame.time.set_timer(PARTICLE_EVENT, 100)

    # Fonts
    base_font = pygame.font.Font('./resources/fonts/VcrOsdMono.ttf', 28)
    options_music_rect = pygame.Rect(1920 / 2 - 400, 100, 800, 30)
    options_console_rect = pygame.Rect(1920 / 2 - 400, 300, 800, 30)

    # Info
    text_save = ["Settings apply only this time", "Saving this will make the game remember", "your configuration on your next launch"]
    save_button_rect = button_save.get_rect()
    show_save_info = False

    text_reset = ["This will reset all settings to default."]
    reset_button_rect = button_reset.get_rect()
    show_reset_info = False


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

        # Draw Buttons (Music Volume)
        if music_volume_up.draw(screen):
            game_engine.settings.set_music_volume(round( game_engine.settings.get_music_volume() + 0.1, 1))
            game_engine.mixer.sound_play('resources/sounds/UI_click.mp3')
            if game_engine.settings.get_music_volume() > 1:
                game_engine.settings.set_music_volume(1)
            game_engine.mixer.update_music_volume()
            print(game_engine.settings.get_music_volume())

        if music_volume_down.draw(screen):
            game_engine.settings.set_music_volume(round( game_engine.settings.get_music_volume() - 0.1, 1))
            game_engine.mixer.sound_play('resources/sounds/UI_click.mp3')
            if game_engine.settings.get_music_volume() < 0:
                game_engine.settings.set_music_volume(0)
            game_engine.mixer.update_music_volume()
            print(game_engine.settings.get_music_volume())

        # Draw Buttons (Sound Volume)
        if sound_volume_up.draw(screen):
            game_engine.settings.set_sound_volume(round( game_engine.settings.get_sound_volume() + 0.1, 1))
            game_engine.mixer.sound_play('resources/sounds/UI_click.mp3')
            if game_engine.settings.get_sound_volume() > 1:
                game_engine.settings.set_sound_volume(1)
            game_engine.mixer.update_sound_volume()
            print(game_engine.settings.get_sound_volume())

        if sound_volume_down.draw(screen):
            game_engine.settings.set_sound_volume(round( game_engine.settings.get_sound_volume() - 0.1, 1))
            game_engine.mixer.sound_play('resources/sounds/UI_click.mp3')
            if game_engine.settings.get_sound_volume() < 0:
                game_engine.settings.set_sound_volume(0)
            game_engine.mixer.update_sound_volume()
            print(game_engine.settings.get_sound_volume())

        # Console Chat Toggle
        if console_toggle.draw(screen):
            game_engine.mixer.sound_play('resources/sounds/UI_click.mp3')
            console_toggle_bool = not console_toggle_bool
            game_engine.settings.set_console_toggle(console_toggle_bool)

        # Draw Buttons (Save and Reset)
        if button_reset.draw(screen):
            game_engine.settings.reset()
            game_engine.mixer.update_music_volume()
            game_engine.mixer.update_sound_volume()
            game_engine.mixer.sound_play('resources/sounds/UI_click.mp3')
            console_toggle_bool = game_engine.settings.get_console_toggle()
            print("RESET")

        if button_save.draw(screen):
            game_engine.settings.write_to_file()
            game_engine.mixer.update_music_volume()
            game_engine.mixer.update_sound_volume()
            game_engine.mixer.sound_play('resources/sounds/UI_click.mp3')
            print("SAVE")

        if button_exit.draw(screen):
            state_running = False
            break
# Events ----------------------------------------------------- #
        for event in pygame.event.get():
            chat_console.update(event)

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    game_engine.mixer.sound_play('resources/sounds/UI_click.mp3')
                    running = False
            if event.type == PARTICLE_EVENT:
                particle_handler.add_particles()

            if save_button_rect.collidepoint((mx, my)):
                show_save_info = True
            else:
                show_save_info = False
            if reset_button_rect.collidepoint((mx, my)):
                show_reset_info = True
            else:
                show_reset_info = False


# Render ----------------------------------------------------- #

        # Music Options Title
        pygame.draw.rect(screen, (50, 50, 50), options_music_rect, 2)
        text_surface_volume = base_font.render("Volume", True, (160, 120, 160))
        screen.blit(text_surface_volume, (options_music_rect.x + options_music_rect.width // 2 - text_surface_volume.get_width() // 2, options_music_rect.y + 1))

        # Music Section
        music_volume_value = float(game_engine.settings.get_music_volume())
        music_volume = base_font.render(f"Music Volume: {int(music_volume_value * 10)}", True, (120, 120 ,120))
        screen.blit(music_volume, (options_music_rect.x + options_music_rect.width // 2 - music_volume.get_width() // 2, options_music_rect.y + 50))

        # Sound Section
        sound_volume_value = float(game_engine.settings.get_sound_volume())
        sound_volume = base_font.render(f"Sound Volume: {int(sound_volume_value * 10)}", True, (120, 120, 120))
        screen.blit(sound_volume, (options_music_rect.x + options_music_rect.width // 2 - sound_volume.get_width() // 2, options_music_rect.y + 100))

        # Console Options Title
        pygame.draw.rect(screen, (50, 50, 50), options_console_rect, 2)
        text_surface_console = base_font.render("Console / Chat", True, (160, 120, 160))
        screen.blit(text_surface_console, (options_console_rect.x + options_console_rect.width // 2 - text_surface_console.get_width() // 2, options_console_rect.y + 1))

        # Console Section
        console_text = base_font.render(f"Show Console-Chat", True, (120, 120, 120))
        screen.blit(console_text, (options_console_rect.x + options_console_rect.width // 2 - console_text.get_width() // 2, options_console_rect.y + 50))
        if console_toggle_bool:
            pygame.draw.rect(screen, (120, 120, 120), (console_toggle.x+7, console_toggle.y+7, 21, 21), 20, 1)

        if show_save_info:
            notification(screen, text_save, 700, 900)
        if show_reset_info:
            notification(screen, text_reset, 700, 900)

        # Console and mouse
        chat_console.draw()
        screen.blit(cursor_img, cursor_rect)


# Update ----------------------------------------------------- #
        pygame.display.flip()
        mainClock.tick(game_engine.settings.get_fps())