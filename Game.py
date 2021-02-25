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

        screen.fill((0, 0, 0))  # Black

        entity_manager.EntityManager.draw()

        # /DEBUG DRAW\
        # DebugText.disp("asdf", 0)
        # \DEBUG DRAW/

    #    c.draw_gridlines()

        #p.draw()

        #mouse.draw()

    #    for index, b in enumerate(bullets):
    #        b.draw()
    #        if (b.age > b.lifespan):
    #            del bullets[index]

    #    for index, particle in enumerate(particles):
    #        particle.draw()
    #        if (particle.age > particle.lifespan):
    #            del particles[index]

        pygame.display.flip()
        pygame.time.Clock().tick(60)

        # \______DRAW______/
