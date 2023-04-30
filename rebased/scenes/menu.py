import pygame, sys, webbrowser
from classes.button import Button
from maintenance import custom_mouse

def MenuLoop(game_engine):
    game_engine.discord.update_discord_status("Waiting in the menu")

    cursor_img, cursor_rect = custom_mouse()

    portrait_y, portrait_x, portrait, userdis = None, None, None, None

    if game_engine.discord.is_active():
        portrait_x = game_engine.settings.get_width() // 2 - 100
        portrait_y = game_engine.settings.get_height() - 100
        username, discriminant = game_engine.discord.get_username()
        userdis = [f"{username} # {discriminant}"]
        portrait = game_engine.discord.get_portrait()
        portrait = pygame.transform.scale(portrait, (60, 60))

    # Load Buttons
    if game_engine.settings.get_width() == 1920 and game_engine.settings.get_height() == 1080:
        offline_banner = Button(game_engine.settings.get_width() // 4, game_engine.settings.get_height() // 5 * 2, "resources/images/buttons/offline_banner.png", "resources/images/buttons/offline_banner_hover.png", 5, 1)
        online_banner = Button(game_engine.settings.get_width() // 4 * 3, game_engine.settings.get_height() // 5 * 2, "resources/images/buttons/online_banner.png", "resources/images/buttons/online_banner_hover.png", 5, 1)
    else:
        offline_banner = Button(game_engine.settings.get_width() // 4, game_engine.settings.get_height() // 5 * 2, "resources/images/buttons/offline_banner.png", "resources/images/buttons/offline_banner_hover.png", 5, 0.8)
        online_banner = Button(game_engine.settings.get_width() // 4 * 3, game_engine.settings.get_height() // 5 * 2, "resources/images/buttons/online_banner.png", "resources/images/buttons/online_banner_hover.png", 5, 0.8)

    discord = Button(0 + 80, game_engine.settings.get_height() - 100, "resources/images/buttons/discord.png", "resources/images/buttons/discord_hover.png", 0, 1)
    github = Button(0 + 200, game_engine.settings.get_height() - 100, "resources/images/buttons/github.png","resources/images/buttons/github_hover.png", 0, 1)
    options = Button(game_engine.settings.get_width() - 200, game_engine.settings.get_height() - 100, "resources/images/buttons/options.png", "resources/images/buttons/options_hover.png", 0, 1)
    leave = Button(game_engine.settings.get_width() - 80, game_engine.settings.get_height() - 100, "resources/images/buttons/quit.png","resources/images/buttons/quit_hover.png", 0, 1)
    profile_card = Button(game_engine.settings.get_width() // 2, game_engine.settings.get_height() - 100, "resources/images/buttons/profile_card.png", "resources/images/buttons/profile_card.png", 5, 1)

    # Particles event
    PARTICLE_EVENT = pygame.USEREVENT + 1
    pygame.time.set_timer(PARTICLE_EVENT, 100)

    menu_loop = True
    while menu_loop:

        # Discord RPC
        game_engine.discord.tick()
        game_engine.screen.fill((0, 0, 0))

        mx, my = pygame.mouse.get_pos()
        cursor_rect.center = (mx, my)
        # Set Background
        game_engine.screen.blit(game_engine.background, (mx // 50 - 38, my // 50 - 21))

        game_engine.particleManager.emit(game_engine.screen)

        # Draw buttons
        if offline_banner.draw(game_engine.screen):
            
            game_engine.mixer.sound_play('resources/sounds/UI_click.mp3')

        if online_banner.draw(game_engine.screen):
            game_engine.mixer.sound_play('resources/sounds/UI_click.mp3')
            if game_engine.discord.is_active():
                game_engine.discord.update_party(1, 4)

        if discord.draw(game_engine.screen):
            game_engine.mixer.sound_play('resources/sounds/UI_click.mp3')
            webbrowser.open("https://discord.gg/xcEYBpn2k2")

        if github.draw(game_engine.screen):
            game_engine.mixer.sound_play('resources/sounds/UI_click.mp3')
            webbrowser.open("https://github.com/pricob/HotFK")

        if options.draw(game_engine.screen):
            game_engine.mixer.sound_play('resources/sounds/UI_click.mp3')
            game_engine.fade(game_engine.screen, 1)
            game_engine.options_loop()
            game_engine.fade_in(game_engine.screen)
            game_engine.fade(game_engine.screen, 1)
            game_engine.discord.update_discord_status("Waiting in the menu")

        if leave.draw(game_engine.screen):
            game_engine.mixer.sound_play('resources/sounds/UI_click.mp3')
            pygame.quit()
            if game_engine.discord.is_active():
                game_engine.discord.clear_activity()
            # clear_project()
            sys.exit()


        for event in pygame.event.get():

            # Update Console / Chat
            game_engine.chatConsole.update(event)

            if event.type == pygame.QUIT:
                menu_loop = False
                pygame.quit()
                sys.exit()

            if event.type == PARTICLE_EVENT:
                game_engine.particleManager.add_particles()

        game_engine.chatConsole.draw()
        if game_engine.discord.is_active():
            if profile_card.draw(game_engine.screen):
                game_engine.mixer.sound_play('resources/sounds/Join.mp3')
            game_engine.screen.blit(portrait, (profile_card.get_rect().x + 22, profile_card.get_rect().y + 22))
            game_engine.textWidget.color((255, 255 ,255))
            game_engine.textWidget.write(game_engine.screen, portrait_x, portrait_y, 40, 'left', userdis, False, True)
        game_engine.screen.blit(cursor_img, cursor_rect)

        game_engine.update_display()