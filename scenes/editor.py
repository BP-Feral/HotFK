# Python Setup =============================================== #
import os
import shutil
import pygame, json

from maintenance import custom_mouse, load_image
from classes.button import Button


# Editor Loop ================================================ #
def EditorLoop(game_engine):

    # Context
    map_name = 'region1/'
    game_engine.discord.update_discord_status(f"Editing a new map - '{map_name[:-1]}'")
    cursor_img, cursor_rect = custom_mouse()

    # Load Buttons (Up and Down for Layer)
    button_load = Button(game_engine.settings.get_width() - 100, game_engine.settings.get_height() - 40, "resources/images/buttons/load.png", "resources/images/buttons/load_hover.png", 1)
    button_save = Button(game_engine.settings.get_width() - 300, game_engine.settings.get_height() - 40, "resources/images/buttons/save.png", "resources/images/buttons/save_hover.png", 1)
    layer_up = Button(game_engine.settings.get_width() / 2 - 320, game_engine.settings.get_height() - 40, "resources/images/buttons/up.png", "resources/images/buttons/up_hover.png", 0.5)
    layer_down = Button(game_engine.settings.get_width() / 2 - 360, game_engine.settings.get_height() - 40, "resources/images/buttons/up.png", "resources/images/buttons/up_hover.png", 0.5)
    layer_down.flip("horizontal")
    button_plus = Button(game_engine.settings.get_width() // 2 - 540, game_engine.settings.get_height() - 40, "resources/images/buttons/plus.png", "resources/images/buttons/plus_hover.png", 0.5)
    button_minus = Button(game_engine.settings.get_width() // 2 - 580, game_engine.settings.get_height() - 40, "resources/images/buttons/minus.png", "resources/images/buttons/minus_hover.png", 0.5)

    # Camera settings
    camera_factor_x = 0
    camera_factor_y = 0
    camera_speed = 5
    camera_margin = 50
    follow_object = False
    target_object = None

    # Change Sound
    game_engine.mixer.music_play('./resources/sounds/Forest_ambient.mp3', -1, 1000)

    # Index images
    images = {}
    paths = ['./resources/images/tiles/debree/', './resources/images/tiles/ground/', './resources/images/tiles/path/']
    for path in paths:
        filenames = [f for f in os.listdir(path) if f.endswith('png')]
        for name in filenames:
            imagename = os.path.splitext(name)[0]
            temp = pygame.image.load(os.path.join(path, name)).convert_alpha()
            images[imagename] = pygame.transform.scale(temp, (temp.get_width()*2, temp.get_height()*2))

    image_names = list(images.keys())
    current_image_index = 0

    # Get initial image
    current_image_name = image_names[current_image_index]
    current_image = images[current_image_name]
    screen_center = (game_engine.window_width // 64 / 2 * 64, game_engine.window_height // 64 / 2 * 64)

    # Tiles Settings
    TILE_SIZE = 64
    tiles = []
    collisions = []

    current_layer = 1
    max_layers = 3
    show_all_layers = False

    # Font
    font = pygame.font.Font('resources/fonts/Thintel.ttf', 40)

# Loop Start ------------------------------------------------- #
    editor_loop = True
    while editor_loop:

        # Discord RPC
        game_engine.discord.tick()
        game_engine.screen.fill((0, 0, 0))

        mx, my = pygame.mouse.get_pos()
        cursor_rect.center = (mx, my)

# Events ----------------------------------------------------- #
        for event in pygame.event.get():
            game_engine.chatConsole.update(event)

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_ESCAPE:
                    editor_loop = False
                if event.key == pygame.K_LSHIFT:
                    camera_speed = 5
                if event.key == pygame.K_a:
                    show_all_layers = not show_all_layers
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LSHIFT:
                    camera_speed = 20

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    # Move to previous image
                    current_image_index -= 1
                    if current_image_index < 0:
                        current_image_index = len(image_names) - 1
                elif event.key == pygame.K_RIGHT:
                    # Move to next image
                    current_image_index += 1
                    if current_image_index >= len(image_names):
                        current_image_index = 0
                current_image_name = image_names[current_image_index]
                current_image = images[current_image_name]

            # Placing tiles
            if event.type == pygame.MOUSEBUTTONDOWN:
                if my <= game_engine.window_height - 80:
                    if pygame.mouse.get_pressed()[0]:
                        tiles.append({'x': (mx - camera_factor_x) // TILE_SIZE, 'y':(my - camera_factor_y) // TILE_SIZE, 'type': current_image_name, 'layer': current_layer})
                        # 1x1 cillisions
                        if current_image_name in ['debree_0', 'debree_1', 'debree_2', 'debree_3', 'debree_4', 'rock_1', 'rock_2', 'rock_3', 'rock_4']:
                            print("1x1 debree placed")
                            collision_rect = pygame.Rect((mx - camera_factor_x) // TILE_SIZE, (my - camera_factor_y) // TILE_SIZE, TILE_SIZE, TILE_SIZE)
                            collisions.append(collision_rect)

                    elif pygame.mouse.get_pressed()[2]:
                        for i in range(len(tiles)):
                            if tiles[i]['x'] == (mx - camera_factor_x) // TILE_SIZE and tiles[i]['y'] == (my - camera_factor_y) // TILE_SIZE and tiles[i]['layer'] == current_layer:
                                del tiles[i]
                                break

# Render ----------------------------------------------------- #
        #   Game Grid
        # for i in range (-(game_engine.window_height // 64 + 1), 2* (game_engine.window_height // 64 + 1)):
        #     pygame.draw.line(game_engine.screen, (100, 100, 100), (0 + camera_factor_x, i*TILE_SIZE + camera_factor_y), (game_engine.window_width + camera_factor_x, i*TILE_SIZE + camera_factor_y))
        # for j in range (0, game_engine.window_width // 64 + 1):
        #     pygame.draw.line(game_engine.screen, (100, 100, 100), (j*TILE_SIZE + camera_factor_x, 0 + camera_factor_y), (j*TILE_SIZE + camera_factor_x, game_engine.window_height + camera_factor_y))
        # for i in range (0, game_engine.window_height // 64 + 1):
        #     pygame.draw.line(game_engine.screen, (255, 255, 255), (0 + camera_factor_x, i*TILE_SIZE*5 + camera_factor_y), (game_engine.window_width + camera_factor_x, i*TILE_SIZE*5 + camera_factor_y))
        # for j in range (0, game_engine.window_width // 64 + 1):
        #     pygame.draw.line(game_engine.screen, (255, 255, 255), (j*TILE_SIZE*5 + camera_factor_x, 0 + camera_factor_y), (j*TILE_SIZE*5 + camera_factor_x, game_engine.window_height + camera_factor_y))

        # Control Camera
        if mx <= camera_margin:
            camera_factor_x += camera_speed
            follow_object = False
            target_object = None

        if mx >= game_engine.window_width - camera_margin:
            camera_factor_x -= camera_speed
            follow_object = False
            target_object = None

        if my <= camera_margin:
            camera_factor_y += camera_speed
            follow_object = False
            target_object = None

        if my >= game_engine.window_height - 5:
            camera_factor_y -= camera_speed
            follow_object = False
            target_object = None

        #if game_engine.window_height - camera_margin - 80 <= my <= game_engine.window_height - 80:
        #    camera_factor_y -= camera_speed

        # Draw Tiles
        for layer in range(1, max_layers+1):
            for tile in tiles:
                if show_all_layers:
                    if tile['layer'] == layer:
                        game_engine.screen.blit(images[tile['type']], (tile['x']*TILE_SIZE + camera_factor_x, tile['y']*TILE_SIZE + camera_factor_y))
                else:
                    if tile['layer'] == current_layer:
                        game_engine.screen.blit(images[tile['type']], (tile['x']*TILE_SIZE + camera_factor_x, tile['y']*TILE_SIZE + camera_factor_y))

        # Display Red Center
        pygame.draw.line(game_engine.screen, (255, 20, 20), (screen_center[0]-128+camera_factor_x, screen_center[1]+camera_factor_y), (screen_center[0]+128+camera_factor_x, screen_center[1]+camera_factor_y), 2)
        pygame.draw.line(game_engine.screen, (255, 20, 20), (screen_center[0]+camera_factor_x, screen_center[1]-128+camera_factor_y), (screen_center[0]+camera_factor_x, screen_center[1]+128+camera_factor_y), 2)

        for collision_rect in collisions:
            pygame.draw.rect(game_engine.screen, (255, 20, 20), (collision_rect.x * TILE_SIZE + camera_factor_x, collision_rect.y * TILE_SIZE + camera_factor_y, TILE_SIZE, TILE_SIZE), 1)
        # Editor GUI Background
        pygame.draw.rect(game_engine.screen, (20, 20, 20), (0, game_engine.window_height - 80, game_engine.window_width, game_engine.window_height - 80))
        pygame.draw.line(game_engine.screen, (50, 50, 50), (0, game_engine.window_height - 80), (game_engine.window_width, game_engine.window_height - 80))

        # Write curent layer
        if layer_down.draw(game_engine.screen):
            if current_layer != 1:
                current_layer -= 1
        if layer_up.draw(game_engine.screen):
            if current_layer != max_layers:
                current_layer += 1
        text_surface = font.render(f"layer: {current_layer}/{max_layers}", True, (200, 200, 200))
        game_engine.screen.blit(text_surface, (game_engine.settings.get_width() // 2 - 500, game_engine.settings.get_height() - 50))

        # Save Button
        if button_save.draw(game_engine.screen):
            game_engine.mixer.sound_play('resources/sounds/UI_click.mp3')

            # Generate map folder
            path = f'./resources/map_data/{map_name}'
            try:
                os.mkdir(path)
            except:
                shutil.rmtree(path)
                os.mkdir(path)

            with open(f'resources/map_data/{map_name}manifest', 'w') as file:
                json.dump(max_layers, file)

            for layer in range(1, max_layers+1):
                temps = []
                for tile in tiles:
                    if tile['layer'] == layer:
                        temps.append(tile)
                with open(f'resources/map_data/{map_name}layer_{layer}', 'w') as file:
                    json.dump(temps, file)

        # Load Button
        if button_load.draw(game_engine.screen):
            game_engine.mixer.sound_play('resources/sounds/UI_click.mp3')
            with open(f'resources/map_data/{map_name}manifest', 'r') as file:
                data = file.read()
                max_layers = json.loads(data)

            tiles = []
            for layer in range(1, max_layers+1):
                with open(f'resources/map_data/{map_name}layer_{layer}', 'r') as file:
                    data = file.read()
                    temps = json.loads(data)
                for tile in temps:
                    tiles.append(tile)

        # Insert Button
        if button_plus.draw(game_engine.screen):
            max_layers += 1
            current_layer += 1

        if button_minus.draw(game_engine.screen):
            if max_layers != 1:
                max_layers -= 1
                current_layer -= 1
            if current_layer < 1:
                current_layer = 1
        # Tile Manager
        game_engine.screen.blit(current_image, (game_engine.settings.get_width() // 2 + 500, game_engine.settings.get_height() - 72, TILE_SIZE, TILE_SIZE))
        pygame.draw.rect(game_engine.screen, (50, 50, 250), (game_engine.settings.get_width() // 2 + 500, game_engine.settings.get_height() - 72, TILE_SIZE, TILE_SIZE), 1)

        # Mouse Hover
        game_engine.screen.blit(cursor_img, cursor_rect)

        # Console
        game_engine.chatConsole.draw()

        # Update Screen
        game_engine.update_display()