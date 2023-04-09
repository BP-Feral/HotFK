# Setup Python ----------------------------------------------- #
import pygame, sys
import webbrowser

from maintenance import clear_project, console_push, load_image, custom_mouse_highlight, custom_mouse
from classes.button import Button
from loops.offline_accounts import offline_account_loop
from classes.particle import Particle

# Menu Loop -------------------------------------------------- #
def menu_loop(game_engine, mixer):

    cursor_img, cursor_rect = custom_mouse()

    screen = pygame.display.get_surface()
    mainClock = game_engine.mainClock

    offline_banner = Button(450, 270, "resources/offline_banner.png", "resources/offline_banner_hover.png", 5)
    online_banner = Button(1070, 270, "resources/online_banner.png", "resources/online_banner_hover.png", 5)

    discord = Button(400, 900, "resources/discord.png", "resources/discord_hover.png", 0)
    github = Button(260, 900, "resources/github.png","resources/github_hover.png", 0)

    options = Button(1920-400-104, 900, "resources/options.png", "resources/options_hover.png", 0)
    leave = Button(1920-260-104, 900, "resources/quit.png","resources/quit_hover.png", 0)

    background = load_image("resources/background.png")
    # Souds
    ui_click = mixer.Sound('resources/sounds/UI_click.mp3')

    # Particles event
    PARTICLE_EVENT = pygame.USEREVENT + 1
    pygame.time.set_timer(PARTICLE_EVENT, 100)
    particle_handler = Particle()

    # LOOP START
    running = True
    while running:

        mx, my = pygame.mouse.get_pos()
        cursor_rect.center = (mx, my)

        # Reset Frame
        screen.fill(0)
        screen.blit(background, (mx // 50 - 38, my // 50 - 21))
        # Draw Particles
        particle_handler.emit(screen)        
        # Draw buttons
        if offline_banner.draw(screen):
            if game_engine.debug_mode:
                console_push("Offline clicked")
            ui_click.play()
            offline_account_loop(game_engine, mixer, particle_handler)
            
        if online_banner.draw(screen):
            if game_engine.debug_mode:
                console_push("Online clicked")
            ui_click.play()

        if discord.draw(screen):
            webbrowser.open("https://discord.gg/J5wDbVjDWc")
            ui_click.play()

        if github.draw(screen):
            webbrowser.open("https://github.com/pricob/HotFK")
            ui_click.play()

        if options.draw(screen):
            console_push("Options clicked")
            ui_click.play()

        if leave.draw(screen):
            ui_click.play()
            pygame.quit()
            clear_project()
            sys.exit()

        # Events ------------------------------------------------- #
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                clear_project()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    ui_click.play()
                    running = False
                    pygame.quit()
                    clear_project()
                    sys.exit()
            if event.type == PARTICLE_EVENT:
                particle_handler.add_particles()

        # Render ------------------------------------------------- #
        screen.blit(cursor_img, cursor_rect)

        # Update ------------------------------------------------- #
        pygame.display.flip()
        mainClock.tick(game_engine.fps)