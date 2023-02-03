# Setup Python ----------------------------------------------- #
import pygame, sys

from maintenance import clear_project, console_push, load_image
from classes.button import Button
from loops.offline_accounts import offline_account_loop

# Menu Loop -------------------------------------------------- #
def menu_loop(game_engine):
    
    screen = pygame.display.get_surface()
    mainClock = game_engine.get_mainClock()

    offline_banner = Button(450, 270, "resources/offline_banner.png", "resources/offline_banner_hover.png", 5)
    online_banner = Button(1070, 270, "resources/online_banner.png", "resources/online_banner_hover.png", 5)

    background = load_image("resources/background.png")
    
    # LOOP START
    running = True
    while running:
        # Reset Frame
        screen.fill(0)
        screen.blit(background, (0, 0))

        # Draw buttons
        if offline_banner.draw(screen):
            if game_engine.debug_mode:
                console_push("offline clicked")
                offline_account_loop(game_engine)

        if online_banner.draw(screen):
            if game_engine.debug_mode:
                console_push("online clicked")

        # Events ------------------------------------------------- #
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                clear_project()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                    pygame.quit()
                    clear_project()
                    sys.exit()

        # Update ------------------------------------------------- #
        pygame.display.flip()
        mainClock.tick(60)