# Setup Python ----------------------------------------------- #
import math
import random
from maintenance import custom_mouse, load_image, show_fps
import pygame

from scenes.options import OptionsLoop
from classes.enemy import Enemy
from classes.player import Player

# Tutorial Loop ---------------------------------------------- #
def DebuggerLoop5(game_engine):

    # Get Context
    game_engine.discord.update_discord_status("Editing new 'room'")
    cursor_img, cursor_rect = custom_mouse()

    TILE_SIZE = 64
    checkers = load_image("./resources/images/debug/checkers.png").convert()

    player = Player(15 * TILE_SIZE, 7 * TILE_SIZE, 8)
    enemies = []
    for i in range (1, 5):
        enemies.append(Enemy(random.randint(1, 25)* TILE_SIZE, random.randint(1, 15)* TILE_SIZE, 3, './resources/debug/slime.png', 1, 100, random.randint(3, 6)* TILE_SIZE, False))


    base_font = pygame.font.Font("./resources/fonts/Thintel.ttf", 35)
    cooldown = 100
# Loop Start ------------------------------------------------- #
    running = True
    while running:

        # Call required updates
        game_engine.discord.tick()

        # Reset Frame
        game_engine.screen.fill((50, 50, 20))

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

        keys = pygame.key.get_pressed()
        player.move(keys)

# Computing -------------------------------------------------- #



# Render ----------------------------------------------------- #
        game_engine.screen.fill((0, 0, 0))
        for i in range(30):
            for j in range(25):
                game_engine.screen.blit(checkers, (i*TILE_SIZE, j*TILE_SIZE))

        print(cooldown)
        if cooldown <= 10:
            pygame.draw.circle(game_engine.screen, (255, 0, 0), (player.get_center()[0], player.get_center()[1]), 2* TILE_SIZE, 5)
            pygame.draw.circle(game_engine.screen, (255, 0, 0), (player.get_center()[0], player.get_center()[1]), 1* TILE_SIZE, 5)

        if cooldown <= 0:
            cooldown = 20
            for enemy in enemies:
                distance = player.pos.distance_to(enemy.getPos())
                if distance <= 2 * TILE_SIZE:
                    enemy.reduceHealth(10)
        else:
            cooldown -= 1

        # Enemies
        for enemy in enemies:
            if enemy.getHealth() >= 1:
                enemy.draw(game_engine.screen)
                enemy.update([player], game_engine.screen)
            else:
                enemies.remove(enemy)
        # Player
        player.draw(game_engine.screen)

        # System
        game_engine.chatConsole.draw()
        game_engine.screen.blit(cursor_img, cursor_rect)
        game_engine.screen.blit(show_fps(game_engine.mainClock, base_font), (10,0))


# Update ----------------------------------------------------- #
        game_engine.update_display()