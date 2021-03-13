"""The main game loop"""

import pygame
import player
import user_input
import entity_manager
import enemy_spawner
import debug
import entity_abc
import random
import camera

def game():
    """The main game loop"""
    # /`````INIT`````\
    screen = pygame.display.get_surface()
    main_player = player.Player(pos=pygame.Vector2(0,0))
    entity_manager.EntityManager.add(main_player)
    # \_____INIT_____/

    running = True
    while running:
        screen.fill((0, 0, 0))  # Black
        # ^ This comes before DRAW to allow for any debug texts
        # /```UPDATE```\

        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                running = False

        user_input.Input.update(events)
        enemy_spawner.EnemySpawner.update()
        entity_manager.EntityManager.update()
        camera.Camera.lerp(main_player.pos)

        # enemy spawner update

        # \___UPDATE___/

        # /``````DRAW``````\

        entity_manager.EntityManager.draw()
        #debug.text(f"Player pos: {main_player.pos}")
        #debug.text(f"Camera pos: {camera.Camera.pos}", 1)

        # /DEBUG DRAW\
        # DebugText.disp("asdf", 0)
        # \DEBUG DRAW/

    #    c.draw_gridlines()

        pygame.display.update()
        pygame.time.Clock().tick(60)

        # \______DRAW______/
