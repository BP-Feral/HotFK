import time, pygame, sys

def SplashLoop(game_engine):

    game_engine.game_state = 'Splash Loop'

    game_engine.discord.update_discord_status("Just Started")

    previous_time = time.time()
    progress = 0
    speed_pr = 2

    cooldown = 0
    splash_loop = True
    # Splash Art View Loop
    while splash_loop:
        cooldown -= 1
        if cooldown <= 0:
            if game_engine.discord.is_active():
                try:
                    game_engine.discord.app.run_callbacks()
                except:
                    game_engine.discord.disable()

        # Reset Frame
        game_engine.screen.fill(0)

        dt = time.time() - previous_time
        previous_time = time.time()

        progress += speed_pr

        if progress >= 200:
            speed_pr = -0.5

        if progress <= 0:
            break

        # Events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    speed_pr = -10

        # Drawing
        pygame.draw.line(game_engine.screen, (int(progress * 1), int(progress * 1), int(progress * 1)), (20 / 100 * game_engine.window_width, 20 / 100 * game_engine.window_height), (20 / 100 * game_engine.window_width * 4, 20 / 100 * game_engine.window_height), 5)

        game_engine.textWidget.color((min(progress*2, 255), min(progress*.5, 20), min(progress*.5, 20)))

        game_engine.textWidget.write(game_engine.screen, 50 / 100 * game_engine.window_width, 15 / 100 * game_engine.window_height, 120, 'center',
        ["< Disclaimer >"], True, True)

        game_engine.textWidget.write(game_engine.screen, 50 / 100 * game_engine.window_width, 25 / 100 * game_engine.window_height, 90, 'center',
            ["The following game is a prototype!",
            "Everything presented can change any time.",
            "Your progress will be reset upon official release."], True, False)

        # TODO finish disclaimer, continue with the game

        # Update Frame
        game_engine.update_display()