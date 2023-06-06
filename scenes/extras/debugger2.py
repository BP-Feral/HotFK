# Setup Python ----------------------------------------------- #
from maintenance import custom_mouse, load_image, show_fps
from scenes.options import OptionsLoop

import pygame


def collision_test(rect, tiles):
    hit_list = []
    for tile in tiles:
        if rect.colliderect(tile):
            hit_list.append(tile)
    return hit_list


def move(rect, movement, tiles):
    collision_types = {'top': False, 'bottom': False, 'right': False, 'left': False}
    rect.x += movement[0]
    hit_list = collision_test(rect, tiles)
    for tile in hit_list:
        if movement[0] > 0:
            rect.right = tile.left
            collision_types['right'] = True
        elif movement[0] < 0:
            rect.left = tile.right
            collision_types['left'] = True
    rect.y += movement[1]
    hit_list = collision_test(rect, tiles)
    for tile in hit_list:
        if movement[1] > 0:
            rect.bottom = tile.top
            collision_types['bottom'] = True
        elif movement[1] < 0:
            rect.top = tile.bottom
            collision_types['top'] = True
    return rect, collision_types


def DebuggerLoop2(game_engine):

    # Get Context
    game_engine.discord.update_discord_status("Editing new map")
    cursor_img, cursor_rect = custom_mouse()
    base_font = pygame.font.Font("./resources/fonts/Thintel.ttf", 20)

    WINDOW_SIZE = (1920, 1080)
    TILE_SIZE = 16
    display = pygame.Surface((430, 270))

    game_map = [['1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1'],
                ['1', '2', '1', '1', '1', '3', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1'],
                ['1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '2', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1'],
                ['1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '2', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1'],
                ['1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1'],
                ['1', '1', '1', '1', '1', '1', '3', '1', '1', '1', '1', '1', '1', '1', '3', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1'],
                ['1', '1', '1', '2', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1'],
                ['1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1'],
                ['1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1'],
                ['1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1'],
                ['1', '1', '1', '1', '1', '1', '3', '1', '1', '1', '1', '1', '1', '1', '1', '1', '2', '1', '1', '3', '1', '1', '1', '1', '1', '1', '1', '1', '1'],
                ['1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1'],
                ['1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1'],
                ['1', '1', '1', '1', '1', '1', '1', '1', '1', '2', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1'],
                ['1', '1', '1', '1', '1', '1', '3', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1'],
                ['1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '3', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1'],
                ['1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1'],
                ['1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1'],
                ['1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1']]
    collision_map = [['0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0'],
                    ['0', '1', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0'],
                    ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '1', '0'],
                    ['0', '0', '1', '0', '0', '0', '1', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0'],
                    ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0'],
                    ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '1', '0', '0', '0', '0', '0'],
                    ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0'],
                    ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0'],
                    ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '1', '0', '0'],
                    ['0', '0', '0', '0', '0', '0', '0', '0', '1', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0'],
                    ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0'],
                    ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0'],
                    ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0']]
    ###
    player_image = pygame.image.load('./resources/images/entities/player/player.png')
    player2_image = pygame.image.load('./resources/images/entities/player/player2.png')

    grass_image = pygame.image.load('./resources/images/debug_tiles/grass.png')
    dirt_image = pygame.image.load('./resources/images/debug_tiles/dirt.png')
    dirt1_image = pygame.image.load('./resources/images/debug_tiles/dirt1.png')
    dirt2_image = pygame.image.load('./resources/images/debug_tiles/dirt2.png')
    crate_image = pygame.image.load('./resources/images/debug_tiles/crate.png').convert_alpha()
    player_image_left = pygame.transform.flip(player_image, True, False)
    player_image_right = player_image

    player_rect = pygame.Rect(200, 50, player_image.get_width(), player_image.get_height())

    moving_right = False
    moving_left = False
    moving_up = False
    moving_down = False

    speed = 2

    # discord activity cooldown
    cooldown = 0
# Loop Start ------------------------------------------------- #
    tutorial_loop2 = True
    while tutorial_loop2:

        # Call required updates
        game_engine.discord.tick()
        display.fill((0, 0, 0))

        cooldown -= 1
        if cooldown <= 0:
            game_engine.discord.update_discord_status("Just Started")
            cooldown = 1000

        collision_rects = []
        y = 0
        for row in game_map:
            x = 0
            for tile in row:
                if tile == '1':
                    display.blit(dirt_image, (x * TILE_SIZE, y * TILE_SIZE))
                if tile == '2':
                    display.blit(dirt2_image, (x * TILE_SIZE, y * TILE_SIZE))
                if tile == '3':
                    display.blit(dirt1_image, (x * TILE_SIZE, y * TILE_SIZE))
                x += 1
            y += 1

        y = 0
        for row in collision_map:
            x = 0
            for tile in row:
                if tile == '1':
                    display.blit(crate_image, (x * TILE_SIZE, y * TILE_SIZE))
                    collision_rects.append(pygame.Rect(x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE))
                x += 1
            y += 1


        player_movement = [0, 0]
        if moving_right == True:
            player_movement[0] += speed
            player_image = player_image_right
        if moving_left == True:
            player_movement[0] -= speed
            player_image = player_image_left
        if moving_down == True:
            player_movement[1] += speed
        if moving_up == True:
            player_movement[1] -= speed

        player_rect, collisions = move(player_rect, player_movement, collision_rects)

        # Mouse
        mx, my = pygame.mouse.get_pos()
        cursor_rect.center = (mx, my)

        if player_rect.y < 100:
            display.blit(player_image, (player_rect.x, player_rect.y))
            display.blit(player2_image, (100, 100))
        else:
            display.blit(player2_image, (100, 100))
            display.blit(player_image, (player_rect.x, player_rect.y))
# Events ----------------------------------------------------- #
        for event in pygame.event.get():
            game_engine.chatConsole.update(event)

            if event.type == pygame.KEYDOWN:
                if game_engine.chatConsole.active == False:
                    if event.key == pygame.K_a:
                        moving_left = True
                    if event.key == pygame.K_d:
                        moving_right = True
                    if event.key == pygame.K_w:
                        moving_up = True
                    if event.key == pygame.K_s:
                        moving_down = True

                if event.key == pygame.K_ESCAPE:
                    if game_engine.chatConsole.active == True:
                        break
                    if game_engine.chatConsole.active == False:
                        game_engine.mixer.sound_play('resources/sounds/UI_click.mp3')
                        if OptionsLoop(game_engine) == "leave_state":
                            tutorial_loop2 = False
                            return
            if event.type == pygame.KEYUP:
                if game_engine.chatConsole.active == False:
                    if event.key == pygame.K_a:
                        moving_left = False
                    if event.key == pygame.K_d:
                        moving_right = False
                    if event.key == pygame.K_w:
                        moving_up = False
                    if event.key == pygame.K_s:
                        moving_down = False
# Render ----------------------------------------------------- #

        surf = pygame.transform.scale(display, WINDOW_SIZE)
        game_engine.screen.blit(surf, (0, 0))
        # Console and mouse
        game_engine.chatConsole.draw()
        game_engine.screen.blit(cursor_img, cursor_rect)
        game_engine.screen.blit(show_fps(game_engine.mainClock, base_font), (10,0))


# Update ----------------------------------------------------- #
        game_engine.update_display()