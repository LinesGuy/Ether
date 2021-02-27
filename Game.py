"""The main game loop"""

import pygame
import player
import user_input
import entity_manager


def game():
    """The main game loop"""
    # /`````INIT`````\
    screen = pygame.display.get_surface()
    entity_manager.EntityManager.add(player.Player(pygame.Vector2(640, 360)))
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
        entity_manager.EntityManager.update()
        # enemy spawner update

        # \___UPDATE___/

        # /``````DRAW``````\

        entity_manager.EntityManager.draw()

        # /DEBUG DRAW\
        # DebugText.disp("asdf", 0)
        # \DEBUG DRAW/

    #    c.draw_gridlines()

        pygame.display.flip()
        pygame.time.Clock().tick(60)

        # \______DRAW______/
