# Setup Python ----------------------------------------------- #
from maintenance import custom_mouse, load_image, show_fps

from classes.health import healthBar
from classes.bullet import Bullet

import pygame

from scenes.options import OptionsLoop

# Tutorial Loop ---------------------------------------------- #
def DebuggerLoop4(game_engine):

    # Get Context
    game_engine.discord.update_discord_status("Editing new 'room'")
    cursor_img, cursor_rect = custom_mouse()

    tile_size = 64

    checkers = load_image("./resources/images/debug/checkers.png").convert()
    cyclop_left_base = pygame.image.load('./resources/monsters/cyclop/cyclop_left.png').convert_alpha()
    cyclop_right_base = pygame.image.load('./resources/monsters/cyclop/cyclop_right.png').convert_alpha()
    cyclop_front_base = pygame.image.load('./resources/monsters/cyclop/cyclop_front.png').convert_alpha()
    cyclop_back_base = pygame.image.load('./resources/monsters/cyclop/cyclop_back.png').convert_alpha()

    cyclop_left = pygame.transform.scale(cyclop_left_base, (64, 64))
    cyclop_right = pygame.transform.scale(cyclop_right_base, (64, 64))
    cyclop_front = pygame.transform.scale(cyclop_front_base, (64, 64))
    cyclop_back = pygame.transform.scale(cyclop_back_base, (64, 64))

    imp_front_base = pygame.image.load('./resources/monsters/imp/imp_front.png').convert_alpha()
    imp_front = pygame.transform.scale(imp_front_base, (64, 64))

    imp_rect = pygame.Rect(800, 800, 64, 64)
    player_pos = [960, 500]

    bullets = []

    player_image = cyclop_front
    speed = 3

    # DEBUG Health Bar
    boss_health = 300
    hp = healthBar("green", boss_health, 0.5)
    hp.create(game_engine.screen, game_engine.window_width//2 - hp.get_width()//2, 0)

    base_font = pygame.font.Font("./resources/fonts/Thintel.ttf", 20)


# Loop Start ------------------------------------------------- #
    running = True
    while running:

        # Call required updates
        game_engine.discord.tick()

        # Reset Frame
        game_engine.screen.fill((0, 0, 0))

        # Mouse
        mx, my = pygame.mouse.get_pos()
        cursor_rect.center = (mx, my)


# Events ----------------------------------------------------- #
        for event in pygame.event.get():
            game_engine.chatConsole.update(event)

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    if game_engine.chatConsole.active == True:
                        print("TRUE")
                        break
                    if game_engine.chatConsole.active == False:
                        print("FALSE")
                        game_engine.mixer.sound_play('resources/sounds/UI_click.mp3')
                        if OptionsLoop(game_engine) == "leave_state":
                            running = False
                            return

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    player_origin = [player_pos[0] + player_image.get_width()//2, player_pos[1] + player_image.get_height()//2]
                    bullets.append(Bullet(*player_origin))

                if event.button == 3:
                    player_origin = [player_pos[0] + player_image.get_width()//2, player_pos[1] + player_image.get_height()//2]
                    myBullet = Bullet(*player_origin)
                    myBullet.changed()
                    bullets.append(myBullet)

        for bullet in bullets[:]:
            bullet.update()
            if not game_engine.screen.get_rect().collidepoint(bullet.pos):
                bullets.remove(bullet)

        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            player_pos[1] -= speed
            player_image = cyclop_back

        elif keys[pygame.K_s]:
            player_pos[1] += speed
            player_image = cyclop_front

        if keys[pygame.K_a]:
            player_pos[0] -= speed
            player_image = cyclop_left

        elif keys[pygame.K_d]:
            player_pos[0] += speed
            player_image = cyclop_right

        if keys[pygame.K_LSHIFT]:
            speed = 6
        else:
            speed = 3
# Render ----------------------------------------------------- #
        game_engine.screen.fill((0, 0, 0))

        # Console and mouse
        #for i in range(40):
        #    for j in range(20):
        #        game_engine.screen.blit(checkers, (i*tile_size, j*tile_size))
#
        if boss_health >= 0:
            game_engine.screen.blit(imp_front, (imp_rect.x, imp_rect.y))

        game_engine.screen.blit(player_image, (player_pos[0], player_pos[1]))

        for bullet in bullets:
            bullet.draw(game_engine.screen)
            if imp_rect.colliderect(bullet.get_rect()):
                if boss_health > -10:
                    bullets.remove(bullet)
                    boss_health -= 10

        # Blit UI Elements
        hp.update(boss_health)

        game_engine.chatConsole.draw()
        game_engine.screen.blit(cursor_img, cursor_rect)
        game_engine.screen.blit(show_fps(game_engine.mainClock, base_font), (10,0))


# Update ----------------------------------------------------- #
        game_engine.update_display()