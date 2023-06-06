# Python Setup =============================================== #
import sys, pygame

from maintenance import custom_mouse, load_image
from classes.button import Button



# Options Loop =============================================== #
def OptionsLoop(game_engine):
# Get Context
    game_engine.discord.update_discord_status("Checking the settings")
    cursor_img, cursor_rect = custom_mouse()

    # Load Buttons (Music Volume)
    music_volume_up = Button(game_engine.settings.get_width() / 2 + 364, 160, "resources/images/buttons/up.png", "resources/images/buttons/up_hover.png", 0.5)
    music_volume_down = Button(game_engine.settings.get_width() / 2 + 314, 160, "resources/images/buttons/up.png", "resources/images/buttons/up_hover.png", 0.5)
    music_volume_down.flip("horizontal")

    # Load Buttons (Sound Volume)
    sound_volume_up = Button(game_engine.settings.get_width() / 2 + 364, 210, "resources/images/buttons/up.png", "resources/images/buttons/up_hover.png", 0.5)
    sound_volume_down = Button(game_engine.settings.get_width() / 2 + 314, 210, "resources/images/buttons/up.png", "resources/images/buttons/up_hover.png", 0.5)
    sound_volume_down.flip("horizontal")

    # Load Buttons (Console Chat)
    console_toggle = Button(game_engine.settings.get_width() / 2 + 364, 360, "resources/images/buttons/box.png", "resources/images/buttons/box_hover.png", 0.5)
    console_toggle_bool = game_engine.settings.get_console_toggle()

    # Load Buttons (Menu)
    button_reset = Button(game_engine.settings.get_width() // 2 - 200, game_engine.settings.get_height() - 80, "resources/images/buttons/reset.png", "resources/images/buttons/reset_hover.png", 1)
    button_save = Button(game_engine.settings.get_width() // 2, game_engine.settings.get_height() - 80, "resources/images/buttons/save.png", "resources/images/buttons/save_hover.png", 1)
    button_exit = Button(game_engine.settings.get_width() // 2 + 200, game_engine.settings.get_height() - 80, "resources/images/buttons/exit.png", "resources/images/buttons/exit_hover.png", 1)

    # Particles Event
    PARTICLE_EVENT = pygame.USEREVENT + 1
    pygame.time.set_timer(PARTICLE_EVENT, 100)

    # Fonts
    font = pygame.font.Font('./resources/fonts/Thintel.ttf', 35)
    options_music_rect = pygame.Rect(game_engine.settings.get_width() / 2 - 400, 100, 800, 30)
    options_console_rect = pygame.Rect(game_engine.settings.get_width() / 2 - 400, 300, 800, 30)

    # Info
    text_save = ["Settings apply only this time", "Saving this will make the game remember", "your configuration on your next launch"]
    save_button_rect = button_save.get_rect()
    show_save_info = False

    text_reset = ["This will reset all settings to default. The game has to be relaunched!"]
    reset_button_rect = button_reset.get_rect()
    show_reset_info = False

# Loop Start ------------------------------------------------- #
    options_loop = True
    while options_loop:

        # Discord RPC
        game_engine.discord.tick()

        # Reset Frame
        game_engine.screen.fill(0)

        # Mouse
        mx, my = pygame.mouse.get_pos()
        cursor_rect.center = (mx, my)

        # Set Background
        game_engine.screen.blit(game_engine.background, (mx // 50 - 38, my // 50 - 21))

        # Draw Particles
        game_engine.particleManager.emit(game_engine.screen)

        # Draw Buttons (Music Volume)
        if music_volume_up.draw(game_engine.screen):
            game_engine.settings.set_music_volume(round( game_engine.settings.get_music_volume() + 0.1, 1))
            if game_engine.settings.get_music_volume() > 1:
                game_engine.settings.set_music_volume(1)

            game_engine.mixer.update_music_volume()
            game_engine.mixer.sound_play('resources/sounds/UI_click.mp3')

        if music_volume_down.draw(game_engine.screen):
            game_engine.settings.set_music_volume(round( game_engine.settings.get_music_volume() - 0.1, 1))
            if game_engine.settings.get_music_volume() < 0:
                game_engine.settings.set_music_volume(0)

            game_engine.mixer.update_music_volume()
            game_engine.mixer.sound_play('resources/sounds/UI_click.mp3')

        # Draw Buttons (Sound Volume)
        if sound_volume_up.draw(game_engine.screen):
            game_engine.settings.set_sound_volume(round( game_engine.settings.get_sound_volume() + 0.1, 1))
            game_engine.mixer.sound_play('resources/sounds/UI_click.mp3')
            if game_engine.settings.get_sound_volume() > 1:
                game_engine.settings.set_sound_volume(1)
            game_engine.mixer.update_sound_volume()
            print(game_engine.settings.get_sound_volume())

        if sound_volume_down.draw(game_engine.screen):
            game_engine.settings.set_sound_volume(round( game_engine.settings.get_sound_volume() - 0.1, 1))
            game_engine.mixer.sound_play('resources/sounds/UI_click.mp3')
            if game_engine.settings.get_sound_volume() < 0:
                game_engine.settings.set_sound_volume(0)
            game_engine.mixer.update_sound_volume()
            print(game_engine.settings.get_sound_volume())

        # Console Chat Toggle
        if console_toggle.draw(game_engine.screen):
            game_engine.mixer.sound_play('resources/sounds/UI_click.mp3')
            console_toggle_bool = not console_toggle_bool
            game_engine.settings.set_console_toggle(console_toggle_bool)

        # Draw Buttons (Save and Reset)
        if button_reset.draw(game_engine.screen):
            game_engine.settings.reset()
            game_engine.mixer.update_music_volume()
            game_engine.mixer.update_sound_volume()
            if game_engine.discord.is_active():
                game_engine.discord.clear_activity()
            console_toggle_bool = game_engine.settings.get_console_toggle()
            game_engine.mixer.sound_play('resources/sounds/UI_click.mp3')

        if button_save.draw(game_engine.screen):
            game_engine.mixer.update_music_volume()
            game_engine.mixer.update_sound_volume()
            game_engine.settings.write_to_file()
            game_engine.mixer.sound_play('resources/sounds/UI_click.mp3')

        if button_exit.draw(game_engine.screen):
            game_engine.discord.update_discord_status("Waiting in the menu")
            return "leave_state"

# Events ----------------------------------------------------- #
        for event in pygame.event.get():
            game_engine.chatConsole.update(event)

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    game_engine.mixer.sound_play('resources/sounds/UI_click.mp3')
                    options_loop = False
            if event.type == PARTICLE_EVENT:
                game_engine.particleManager.add_particles()

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
        pygame.draw.rect(game_engine.screen, (50, 50, 50), options_music_rect, 2)
        text_surface_volume = font.render("Volume", True, (160, 120, 160))
        game_engine.screen.blit(text_surface_volume, (options_music_rect.x + options_music_rect.width // 2 - text_surface_volume.get_width() // 2, options_music_rect.y + 3))

        # Music Section
        music_volume_value = float(game_engine.settings.get_music_volume())
        music_volume = font.render(f"Music Volume: {int(music_volume_value * 10)}", True, (120, 120 ,120))
        game_engine.screen.blit(music_volume, (options_music_rect.x + options_music_rect.width // 2 - music_volume.get_width() // 2, options_music_rect.y + 50))

        # Sound Section
        sound_volume_value = float(game_engine.settings.get_sound_volume())
        sound_volume = font.render(f"Sound Volume: {int(sound_volume_value * 10)}", True, (120, 120, 120))
        game_engine.screen.blit(sound_volume, (options_music_rect.x + options_music_rect.width // 2 - sound_volume.get_width() // 2, options_music_rect.y + 100))

        # Console Options Title
        pygame.draw.rect(game_engine.screen, (50, 50, 50), options_console_rect, 2)
        text_surface_console = font.render("Console / Chat", True, (160, 120, 160))
        game_engine.screen.blit(text_surface_console, (options_console_rect.x + options_console_rect.width // 2 - text_surface_console.get_width() // 2, options_console_rect.y + 3))

        # Console Section
        console_text = font.render(f"Show Console-Chat", True, (120, 120, 120))
        game_engine.screen.blit(console_text, (options_console_rect.x + options_console_rect.width // 2 - console_text.get_width() // 2, options_console_rect.y + 50))
        if console_toggle_bool:
            pygame.draw.rect(game_engine.screen, (120, 120, 120), (int(console_toggle.rect.x + 7), int(console_toggle.rect.y + 7), 21, 21 ), 20, 1)
        if show_save_info:
            game_engine.textWidget.color((255, 255, 255))
            game_engine.textWidget.write(game_engine.screen, game_engine.settings.get_width() // 2, game_engine.settings.get_height() - 150, 40, 'center', text_save, True, True)
        if show_reset_info:
            game_engine.textWidget.color((255, 0, 0))
            game_engine.textWidget.write(game_engine.screen, game_engine.settings.get_width() // 2, game_engine.settings.get_height() - 150, 40, 'center', text_reset, True, True)

        # Console and mouse
        game_engine.chatConsole.draw()
        game_engine.screen.blit(cursor_img, cursor_rect)


# Update ----------------------------------------------------- #
        game_engine.update_display()