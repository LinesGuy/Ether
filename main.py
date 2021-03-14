import pygame as pg
from entity_manager import EntityManager
from camera import Camera
from user_input import Input
from player import Player
import debug
import time

# TEMP
from entity_abc import Entity
import random

# INIT
pg.init()
clock = pg.time.Clock()
Camera.set_dimensions((1200, 800), scale=4)
screen = pg.display.set_mode(Camera.WINDOW_SIZE)
display = pg.Surface(Camera.DISPLAY_SIZE)
EntityManager.add(Player())
frame = 0

# TEMP INIT
for i in range(10):
    EntityManager.add(Entity(
        (random.randint(-200, 200), random.randint(-100, 100))))
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
    Camera.update()  # Lerp / move camera

    EntityManager.update()

    # UPDATE END

    # DRAW
    EntityManager.draw(display)

    pg.draw.circle(display, (255, 0, 0), Camera.get_pos_on_screen(Camera.get_mouse_coords()), 2)
    # ^ Debug circle, gets mouse coords in the world then converts to screen coords.
    # This is redundant but useful to see where things can go wrong.

    surf = pg.transform.scale(display, Camera.WINDOW_SIZE)
    screen.blit(surf, (0, 0))

    # Debug stuffs
    debug.text(screen, f"{round((time.time() - start_time)*1000, 3)}, ms per frame", 0)
    debug.text(screen, f"Camera.pos: {Camera.pos}", 1)
    if not Camera.is_lerping:
        debug.text(screen, "FREECAM ENABLED, Press 'c' to enable lerp", 2)
    debug.text(screen, f"Camera.zoom: {Camera.zoom}", 3)
    debug.text(screen, f"Mouse world pos: {Camera.get_mouse_coords()}", 4)
    debug.text(screen, f"EntityManager.count: {EntityManager.count()}", 5)

    pg.display.update()

    # DRAW END

    clock.tick(60)