# Setup Python ----------------------------------------------- #
from maintenance import custom_mouse, load_image, show_fps
from scenes.options import OptionsLoop
from classes.player import Player


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


def update_mouse_pos(mx, my, base_font, screen):
    px = base_font.render(f"{mx}:{my}", True, (255, 255, 255))
    screen.blit(px, (mx, my))


def draw_axis(screen, TILE_SIZE):
    for i in range(30):
            pygame.draw.line(screen, (255, 255, 255), (i * TILE_SIZE, 0), (i * TILE_SIZE, 1080))
            pygame.draw.line(screen, (255, 255, 255), (0, i * TILE_SIZE), (1920, i * TILE_SIZE))


def add_pos(base_font, mx, my, blits):
    px = base_font.render(f"{mx // 64}, {my // 64}", True, (255, 0, 0))

    blits.append((px, mx, my))
    return blits


def display_pos(screen, blits):
    for blit in blits:
        screen.blit(blit[0], (blit[1], blit[2]))


def DebuggerLoop3(game_engine):

    # Get Context
    player1_path = './resources/images/entities/player/player.png'
    player1 = Player( 200, 50, 10, player1_path, 'player')

    game_engine.discord.update_discord_status("Editing new map")
    cursor_img, cursor_rect = custom_mouse()
    mainClock = game_engine.mainClock
    base_font = pygame.font.Font("./resources/fonts/Thintel.ttf", 20)

    WINDOW_SIZE = (1920, 1080)
    TILE_SIZE = 64


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
    player2_image = pygame.image.load('./resources/images/entities/player/player2.png')
    player2_image = pygame.transform.scale(player2_image, (player2_image.get_width()*4, player2_image.get_height()*4))

    grass_image = pygame.image.load('./resources/images/debug_tiles/grass.png')
    grass_image = pygame.transform.scale(grass_image, (64, 64))

    dirt_image = pygame.image.load('./resources/images/debug_tiles/dirt.png')
    dirt_image = pygame.transform.scale(dirt_image, (64, 64))

    dirt1_image = pygame.image.load('./resources/images/debug_tiles/dirt1.png')
    dirt1_image = pygame.transform.scale(dirt1_image, (64, 64))

    dirt2_image = pygame.image.load('./resources/images/debug_tiles/dirt2.png')
    dirt2_image = pygame.transform.scale(dirt2_image, (64, 64))

    crate_image = pygame.image.load('./resources/images/debug_tiles/crate.png').convert_alpha()
    crate_image = pygame.transform.scale(crate_image, (crate_image.get_width()*4, crate_image.get_height()*4))

    select_image = pygame.image.load('./resources/images/debug_tiles/select.png').convert_alpha()
    select_image = pygame.transform.scale(select_image, (64, 64))

    show_axis = False

    # Debug rects
    blits = []

    # discord activity cooldown
    cooldown = 0
# Loop Start ------------------------------------------------- #
    running = True
    while running:
        game_engine.screen.fill((0, 0, 0))

        # Call required updates
        game_engine.discord.tick()

        collision_rects = []
        y = 0
        for row in game_map:
            x = 0
            for tile in row:
                if tile == '1':
                    game_engine.screen.blit(dirt_image, (x * TILE_SIZE, y * TILE_SIZE))
                if tile == '2':
                    game_engine.screen.blit(dirt2_image, (x * TILE_SIZE, y * TILE_SIZE))
                if tile == '3':
                    game_engine.screen.blit(dirt1_image, (x * TILE_SIZE, y * TILE_SIZE))
                if tile == '4':
                    game_engine.screen.blit(select_image, (x * TILE_SIZE, y * TILE_SIZE))
                x += 1
            y += 1

        y = 0
        for row in collision_map:
            x = 0
            for tile in row:
                if tile == '1':
                    game_engine.screen.blit(crate_image, (x * TILE_SIZE, y * TILE_SIZE))
                    collision_rects.append(pygame.Rect(x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE))
                x += 1
            y += 1

        player_rect, collisions = move(player1.get_rect(), player1.get_movement(), collision_rects)

        del collisions
        # Mouse
        mx, my = pygame.mouse.get_pos()
        cursor_rect.center = (mx, my)

        player1.draw(game_engine.screen)
        game_engine.screen.blit(player2_image, (100, 100))



# Events ----------------------------------------------------- #
        for event in pygame.event.get():
            game_engine.chatConsole.update(event)

            # Mouse actions
            if event.type == pygame.MOUSEBUTTONDOWN:
                show_axis = True
                blits = add_pos(base_font, mx, my, blits)
            if event.type == pygame.MOUSEBUTTONUP:
                show_axis = False
                target_x = mx // TILE_SIZE
                target_y = my // TILE_SIZE
                game_engine.screen.blit(select_image, (target_x, target_y))
                game_map[target_y][target_x]= '4'

            # Key presses
            if event.type == pygame.KEYDOWN:
                player1.move(event, game_engine.chatConsole)

                if event.key == pygame.K_ESCAPE:
                    if game_engine.chatConsole.active == True:
                        break
                    if game_engine.chatConsole.active == False:
                        game_engine.mixer.sound_play('resources/sounds/UI_click.mp3')
                        if OptionsLoop(game_engine) == "leave_state":
                            running = False
                            return

# Render ----------------------------------------------------- #

        surf = pygame.transform.scale(game_engine.screen, WINDOW_SIZE)
        game_engine.screen.blit(surf, (0, 0))
        # Console and mouse
        game_engine.chatConsole.draw()
        update_mouse_pos(mx, my, base_font, game_engine.screen)
        if show_axis:
            draw_axis(game_engine.screen, TILE_SIZE)

        display_pos(game_engine.screen, blits)
        game_engine.screen.blit(cursor_img, cursor_rect)
        game_engine.screen.blit(show_fps(mainClock, base_font), (10,0))


# Update ----------------------------------------------------- #
        game_engine.update_display()