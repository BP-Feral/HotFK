import pygame
from classes.particle import Particle
from maintenance import load_image, custom_mouse

def options_loop(game_engine, particle_handler, chat_console):

    # Get Context    
    cursor_img, cursor_rect = custom_mouse()
    screen = pygame.display.get_surface()
    mainClock = game_engine.mainClock
    background = load_image("resources/images/backgrounds/background.png")

    # Particles Event
    PARTICLE_EVENT = pygame.USEREVENT + 1
    pygame.time.set_timer(PARTICLE_EVENT, 100)

    # Loop Start
    running = True
    while running:

        # Reset Frame
        screen.fill(0)
        mx, my = pygame.mouse.get_pos()
        cursor_rect.center = (mx, my)

        screen.blit(background, (mx // 50 - 38, my // 50 - 21))
        # Draw Particles
        particle_handler.emit(screen)

        # Events ------------------------------------------------- #
        for event in pygame.event.get():
            chat_console.update(event)

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    game_engine.mixer.sound_play('resources/sounds/UI_click.mp3')
                    running = False
            if event.type == PARTICLE_EVENT:
                particle_handler.add_particles()
        
        # Render ------------------------------------------------- #
        chat_console.draw()
        screen.blit(cursor_img, cursor_rect)
    
        # Update ------------------------------------------------- #
        pygame.display.flip()
        mainClock.tick(game_engine.fps)