# Setup Python ----------------------------------------------- #
import sys
import pygame

from maintenance import custom_mouse, load_image, console_push
from classes.button import Button

# Character Seleection Loop ---------------------------------- #
def OfflineLoop(game_engine):
    game_engine.discord.update_discord_status("Character selection")

    cursor_img, cursor_rect = custom_mouse()

    # Load Background
    background = load_image("resources/images/backgrounds/background.png")

    # Load Buttons
    b0 = Button(1450, 220, "resources/images/buttons/new.png", "resources/images/buttons/new_hover.png", 1)
    b1 = Button(1450, 220 + 1 * 120, "resources/images/buttons/empty.png", "resources/images/buttons/empty_hover.png", 1)
    b2 = Button(1450, 220 + 2 * 120, "resources/images/buttons/empty.png", "resources/images/buttons/empty_hover.png", 1)
    b3 = Button(1450, 220 + 3 * 120, "resources/images/buttons/empty.png", "resources/images/buttons/empty_hover.png", 1)
    b4 = Button(1450, 220 + 4 * 120, "resources/images/buttons/empty.png", "resources/images/buttons/empty_hover.png", 1)
    buttons_list = [b0, b1, b2, b3, b4]

    # Particles event
    PARTICLE_EVENT = pygame.USEREVENT + 1
    pygame.time.set_timer(PARTICLE_EVENT, 50)


# Loop Start ------------------------------------------------- #
    offline_loop = True
    while offline_loop:

        # Call required updates
        game_engine.discord.tick()
        game_engine.screen.fill((0, 0, 0))

        # Mouse
        mx, my = pygame.mouse.get_pos()
        cursor_rect.center = (mx, my)

        # Set Background
        game_engine.screen.blit(background, (mx // 50 - 38, my // 50 - 21))

        # Draw Particles
        game_engine.particleManager.emit(game_engine.screen)

        # Draw buttons
        for i in range(0, 5):
           if buttons_list[i].draw(game_engine.screen):
            console_push(f"pressed button {i}")
            game_engine.mixer.sound_play('resources/sounds/UI_click.mp3')

            if i == 0:
                game_engine.discord.update_discord_status("Zone One: White Bridge")
                game_engine.debugger_scene()
            if i == 1:
                game_engine.discord.update_discord_status("Zone Two: Ailhelm Forest")
                game_engine.debugger_scene3()
            if i == 2:
                game_engine.discord.update_discord_status("Free Zone: Serthorne Village")
                game_engine.debugger_scene2()
            if i == 3:
                game_engine.discord.update_discord_status("Blackridge: Shadow Tower")
                game_engine.debugger_scene4()
            if i == 4:
                game_engine.discord.update_discord_status("Blackridge: Shadow Tower")
                game_engine.debugger_scene5()

# Events ----------------------------------------------------- #
        for event in pygame.event.get():
            game_engine.chatConsole.update(event)

            if event.type == pygame.QUIT:
                offline_loop = False
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    game_engine.mixer.sound_play('resources/sounds/UI_click.mp3')
                    offline_loop = False

            if event.type == PARTICLE_EVENT:
                game_engine.particleManager.add_particles()


# Render ----------------------------------------------------- #
        game_engine.chatConsole.draw()
        game_engine.screen.blit(cursor_img, cursor_rect)


# Update ----------------------------------------------------- #
        game_engine.update_display()