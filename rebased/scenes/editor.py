# Imports
import os
import pygame, json

from maintenance import custom_mouse, load_image
from classes.button import Button


def EditorLoop(game_engine):

    # Context
    game_engine.discord.update_discord_status("Editing a new map")
    cursor_img, cursor_rect = custom_mouse()

    # Load Buttons (Up and Down for Layer)
    button_load = Button(game_engine.settings.get_width() // 2 + 100, game_engine.settings.get_height() - 40, "resources/images/buttons/load.png", "resources/images/buttons/load_hover.png", 2, 1)
    button_save = Button(game_engine.settings.get_width() // 2 - 100, game_engine.settings.get_height() - 40, "resources/images/buttons/save.png", "resources/images/buttons/save_hover.png", 2, 1)
    layer_up = Button(game_engine.settings.get_width() / 2 - 360, game_engine.settings.get_height() - 40, "resources/images/buttons/up.png", "resources/images/buttons/up_hover.png", 2, 0.5)
    layer_down = Button(game_engine.settings.get_width() / 2 - 400, game_engine.settings.get_height() - 40, "resources/images/buttons/up.png", "resources/images/buttons/up_hover.png", 2, 0.5)
    layer_down.flip("horizontal")

    # Camera settings
    camera_factor_x = 0
    camera_factor_y = 0
    camera_speed = 5
    camera_margin = 50

    game_engine.mixer.music_play('./resources/sounds/Forest_ambient.mp3', -1, 1000)
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
    current_layer = 2

    # Font
    font = pygame.font.Font('resources/fonts/Thintel.ttf', 40)

    # Editor Loop
    editor_loop = True
    while editor_loop:

        # Discord RPC
        game_engine.discord.tick()
        game_engine.screen.fill((0, 0, 0))

        mx, my = pygame.mouse.get_pos()
        cursor_rect.center = (mx, my)

        for event in pygame.event.get():
            game_engine.chatConsole.update(event)

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_ESCAPE:
                    editor_loop = False
                if event.key == pygame.K_LSHIFT:
                    camera_speed = 5
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
                    elif pygame.mouse.get_pressed()[2]:
                        for i in range(len(tiles)):
                            if tiles[i]['x'] == (mx - camera_factor_x) // TILE_SIZE and tiles[i]['y'] == (my - camera_factor_y) // TILE_SIZE:
                                del tiles[i]
                                break

        ## Game Grid
        #for i in range (0, game_engine.window_height // 64 + 1):
        #    pygame.draw.line(game_engine.screen, (100, 100, 100), (0 + camera_factor_x, i*TILE_SIZE + camera_factor_y), (game_engine.window_width + camera_factor_x, i*TILE_SIZE + camera_factor_y))
        #for j in range (0, game_engine.window_width // 64 + 1):
        #    pygame.draw.line(game_engine.screen, (100, 100, 100), (j*TILE_SIZE + camera_factor_x, 0 + camera_factor_y), (j*TILE_SIZE + camera_factor_x, game_engine.window_height + camera_factor_y))
        #for i in range (0, game_engine.window_height // 64 + 1):
        #    pygame.draw.line(game_engine.screen, (255, 255, 255), (0 + camera_factor_x, i*TILE_SIZE*5 + camera_factor_y), (game_engine.window_width + camera_factor_x, i*TILE_SIZE*5 + camera_factor_y))
        #for j in range (0, game_engine.window_width // 64 + 1):
        #    pygame.draw.line(game_engine.screen, (255, 255, 255), (j*TILE_SIZE*5 + camera_factor_x, 0 + camera_factor_y), (j*TILE_SIZE*5 + camera_factor_x, game_engine.window_height + camera_factor_y))

        # Control Camera
        if mx <= camera_margin:
            camera_factor_x += camera_speed
        if mx >= game_engine.window_width - camera_margin:
            camera_factor_x -= camera_speed
        if my <= camera_margin:
            camera_factor_y += camera_speed
        if my >= game_engine.window_height - 5:
            camera_factor_y -= camera_speed
        #if game_engine.window_height - camera_margin - 80 <= my <= game_engine.window_height - 80:
        #    camera_factor_y -= camera_speed

        # Draw Tiles
        for tile in tiles:
            for layer in range(0, 5):
                if tile['layer'] == layer:
                    game_engine.screen.blit(images[tile['type']], (tile['x']*TILE_SIZE + camera_factor_x, tile['y']*TILE_SIZE + camera_factor_y))

        # Display Red Center
        pygame.draw.line(game_engine.screen, (255, 20, 20), (screen_center[0]-128+camera_factor_x, screen_center[1]+camera_factor_y), (screen_center[0]+128+camera_factor_x, screen_center[1]+camera_factor_y), 2)
        pygame.draw.line(game_engine.screen, (255, 20, 20), (screen_center[0]+camera_factor_x, screen_center[1]-128+camera_factor_y), (screen_center[0]+camera_factor_x, screen_center[1]+128+camera_factor_y), 2)

        # Editor GUI Background
        pygame.draw.rect(game_engine.screen, (20, 20, 20), (0, game_engine.window_height - 80, game_engine.window_width, game_engine.window_height - 80))
        pygame.draw.line(game_engine.screen, (50, 50, 50), (0, game_engine.window_height - 80), (game_engine.window_width, game_engine.window_height - 80))

        # Write curent layer
        if layer_down.draw(game_engine.screen):
            if current_layer != 0:
                current_layer -= 1
        if layer_up.draw(game_engine.screen):
            if current_layer != 5:
                current_layer += 1
        text_surface = font.render(f"layer: {current_layer}", True, (200, 200, 200))
        game_engine.screen.blit(text_surface, (game_engine.settings.get_width() // 2 - 500, game_engine.settings.get_height() - 50))

        # Save Button
        if button_save.draw(game_engine.screen):
                    game_engine.mixer.sound_play('resources/sounds/UI_click.mp3')
                    with open('resources/map_data/tiles', 'w') as file:
                        json.dump(tiles, file)

        # Load Button
        if button_load.draw(game_engine.screen):
            game_engine.mixer.sound_play('resources/sounds/UI_click.mp3')
            with open('resources/map_data/tiles', 'r') as file:
                data = file.read()
                tiles = json.loads(data)

        # Tile Manager
        game_engine.screen.blit(current_image, (game_engine.settings.get_width() // 2 + 500, game_engine.settings.get_height() - 72, TILE_SIZE, TILE_SIZE))
        pygame.draw.rect(game_engine.screen, (50, 50, 250), (game_engine.settings.get_width() // 2 + 500, game_engine.settings.get_height() - 72, TILE_SIZE, TILE_SIZE), 1)

        # Mouse Hover
        game_engine.screen.blit(cursor_img, cursor_rect)

        # Console
        game_engine.chatConsole.draw()

        # Update Screen
        game_engine.update_display()