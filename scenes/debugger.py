# Setup Python ----------------------------------------------- #
from maintenance import custom_mouse_highlight, update_fps, load_image
from loops.options import options_loop

import pygame
import time


class Tile:
    def __init__(self, tile_id, x, y, image):
        self.tile_id = str(tile_id)
        self.x = x
        self.y = y
        self.image = image


# Tutorial Loop ---------------------------------------------- #
def tutorial_loop(game_engine, particle_handler, chat_console):

    # Get Context
    game_engine.update_discord_status("Editing new 'room'")
    cursor_img, cursor_rect = custom_mouse_highlight()
    screen = pygame.display.get_surface()
    mainClock = game_engine.mainClock

    # Resources
    checkers = load_image("debugging/checkers.png").convert()

    # Fonts
    base_font = pygame.font.Font("./resources/fonts/VcrOsdMono.ttf", 20)

    # Axis
    axis_start_pos = [1920 // 2, 1080 // 2]
    moving = [0, 0, 0, 0]
    speed = 10

    # Render Box
    render_rect = pygame.Rect(0, 0, 100, 100)

    # Generate Map
    tiles = []
    for i in range (-20, 1920//64 + 20):
        for j in range(-20, 1080//64 + 20):
            my_tile = Tile('checkers', i*64, j*64, checkers)
            tiles.append(my_tile)


# Loop Start ------------------------------------------------- #
    running = True
    while running:

        # Call required updates
        game_engine.updates()

        # Reset Frame
        screen.fill(0)

        # Mouse
        mx, my = pygame.mouse.get_pos()
        cursor_rect.center = (mx, my)


# Events ----------------------------------------------------- #
        for event in pygame.event.get():
            chat_console.update(event)

            if event.type == pygame.KEYDOWN:

                if chat_console.active == False:
                    if event.key == pygame.K_a:
                        moving[0] = 1
                        moving[1] = 0
                    if event.key == pygame.K_d:
                        moving[0] = 0
                        moving[1] = 1
                    if event.key == pygame.K_w:
                        moving[2] = 1
                        moving[3] = 0
                    if event.key == pygame.K_s:
                        moving[2] = 0
                        moving[3] = 1

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_ESCAPE:
                    if chat_console.active == True:
                        print("TRUE")
                        break
                    if chat_console.active == False:
                        print("FALSE")
                        game_engine.mixer.sound_play('resources/sounds/UI_click.mp3')
                        options_loop(game_engine, particle_handler, chat_console)

                if event.key == pygame.K_a:
                    moving[0] = 0
                if event.key == pygame.K_d:
                    moving[1] = 0
                if event.key == pygame.K_w:
                    moving[2] = 0
                if event.key == pygame.K_s:
                    moving[3] = 0

        if moving[0]:
            for tile in tiles:
                tile.x += 1 * speed

        if moving[1]:
            for tile in tiles:
                tile.x -= 1 * speed            

        if moving[2]:
            for tile in tiles:
                tile.y += 1 * speed

        if moving[3]:
            for tile in tiles:
                tile.y -= 1 * speed


# Render ----------------------------------------------------- #
        for tile in tiles:
            if tile.tile_id == 'checkers':
                screen.blit(tile.image, (tile.x, tile.y))

        # Console and mouse
        chat_console.draw()
        screen.blit(cursor_img, cursor_rect)
        screen.blit(update_fps(mainClock, base_font), (10,0))


# Update ----------------------------------------------------- #
        pygame.display.flip()

        # framerate control
        mainClock.tick(60)