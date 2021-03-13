import pygame as pg
from entity_manager import EntityManager
from camera import Camera
from user_input import Input
from player import Player
import time

# INIT
pg.init()
clock = pg.time.Clock()
Camera.set_dimensions((1200, 800), scale=4)
screen = pg.display.set_mode(Camera.WINDOW_SIZE)
display = pg.Surface(Camera.DISPLAY_SIZE)

EntityManager.add(Player())
frame = 0
# INIT END

running = True
while running:
    start_time = time.time()
    frame += 1
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
    if frame % 60 == 0: print(round((time.time() - start_time)*1000, 3), "ms")

    clock.tick(60)