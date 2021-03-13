import pygame as pg
from entity_manager import EntityManager
from camera import Camera
from user_input import Input
from player import Player

# INIT
pg.init()
clock = pg.time.Clock()
Camera.set_dimensions((1200, 800), scale=4)
screen = pg.display.set_mode(Camera.WINDOW_SIZE)
display = pg.Surface(Camera.DISPLAY_SIZE)

EntityManager.add(Player())
# INIT END

running = True
while running:
    display.fill((0,0,0))

    # UPDATE

    events = pg.event.get()
    for event in events:
        if event.type == pg.QUIT:
            running = False
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_ESCAPE:
                running = False

    Input.update()
    EntityManager.update()

    # UPDATE END

    # DRAW
    EntityManager.draw(display)

    surf = pg.transform.scale(display, Camera.WINDOW_SIZE)
    screen.blit(surf, (0, 0))
    pg.display.update()

    # DRAW END

    clock.tick(60)