import pygame
import Player
import Input
import DebugText
import EntityManager
    
def game():
    # /`````INIT`````\
    screen = pygame.display.get_surface()
    EntityManager.EntityManager.add(Player.Player([640, 360]))
    # \_____INIT_____/

    running = True
    while (running):
        # /```UPDATE```\
        
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                running = False

        Input.Input.update(events)
        EntityManager.EntityManager.update()
        # enemy spawner update

        #c.egg_cam((p.x, p.y))

    #    keys = pygame.key.get_pressed()
        #if (keys):
            #p.get_movement_keypresses(keys)
    #
        #if any([keys[pygame.K_a], keys[pygame.K_d], keys[pygame.K_w], keys[pygame.K_s]]):
            #for i in range(3):
                #particles += p.create_movement_particle()
            
        #mouse.update_position()
    #
        #backfire = 8
    #    if (mouse.clicked):
    #        bullets += p.player_bullet()
    #        c.move_relative(math.cos(-p.aim_bearing)*backfire, math.sin(p.aim_bearing)*backfire)
    #    elif (mouse.held_frames % 10 == 0 and mouse.held_frames > 0):
    #        bullets += p.player_bullet()
    #        c.move_relative(math.cos(-p.aim_bearing)*backfire, math.sin(p.aim_bearing)*backfire)
    #
    #    for b in bullets:
    #        b.update()
    #
    #    for particle in particles:
    #        particle.update()
        
        # \___UPDATE___/

        # /``````DRAW``````\

        screen.fill((0, 0, 0))  # Black

        EntityManager.EntityManager.draw()

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
