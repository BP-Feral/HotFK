# Setup Python ----------------------------------------------- #
import pygame, sys
from maintenance import clear_project, load_image, console_push, custom_mouse_highlight, custom_mouse
from classes.button import Button

# Offline accounts ------------------------------------------- #
def offline_account_loop(game_engine, mixer, particle_handler):
    
    cursor_img, cursor_rect = custom_mouse()

    screen = pygame.display.get_surface()
    mainClock = game_engine.mainClock
    

    background = load_image("resources/background.png")

    b0 = Button(1450, 220, "resources/new.png", "resources/new_hover.png", 2)
    b1 = Button(1450, 220 + 1 * 120, "resources/empty.png", "resources/empty_hover.png", 2)
    b2 = Button(1450, 220 + 2 * 120, "resources/empty.png", "resources/empty_hover.png", 2)
    b3 = Button(1450, 220 + 3 * 120, "resources/empty.png", "resources/empty_hover.png", 2)
    buttons_list = [b0, b1, b2, b3]

    # particles event
    PARTICLE_EVENT = pygame.USEREVENT + 1
    pygame.time.set_timer(PARTICLE_EVENT, 50)
    # Souds
    ui_click = mixer.Sound('resources/sounds/UI_click.mp3')
    # LOOP START
    running = True
    while running:

        # Reset Frame -------------------------------------------- #
        screen.fill(0)
        mx, my = pygame.mouse.get_pos()
        cursor_rect.center = (mx, my)

        screen.blit(background, (mx // 50 - 38, my // 50 - 21))
        # Draw Particles
        particle_handler.emit(screen)
        # Draw buttons
        for i in range(0, 4):
           if buttons_list[i].draw(screen):
            console_push(f"pressed button {i}")
            #if i == 0:
                #mixer.music.stop()
                
            ui_click.play()

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
            if event.type == PARTICLE_EVENT:
                particle_handler.add_particles()

        # Render ------------------------------------------------- #
        screen.blit(cursor_img, cursor_rect)

        # Update ------------------------------------------------- #
        pygame.display.flip()
        mainClock.tick(game_engine.fps)