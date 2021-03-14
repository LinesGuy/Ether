import pygame as pg
from bullet import Bullet
from user_input import Input
import entity_manager
import random
from camera import Camera

class ArtBurst(Bullet):
    """The 'burst' combat art, shoots a large bullet that explodes into
    multiple smaller bullets"""

    def __init__(self, pos, direction: float, destination):
        # direction is in degrees
        # destination is coordinates for where to 'explode'
        BULLET_SPEED = 5
        velocity = pg.Vector2(1,0).rotate(direction) * BULLET_SPEED
        #pos = pos + velocity * 5  # Spawn bullet slightly in front of player
        lifespan = round(pos.distance_to(destination) / BULLET_SPEED)
        super().__init__(pos, velocity, lifespan=lifespan)

    def update(self):
        self.pos += self.velocity

        self.age += 1
        if self.age > self.lifespan:
            for i in range(10):
                bearing = random.random() * 360
                velocity = pg.Vector2(1, 0).rotate(bearing) * 4
                entity_manager.EntityManager.add(Bullet(self.pos*1, velocity))
            self.is_expired = True

    def draw(self, screen):
        screen_pos = Camera.get_pos_on_screen(self.pos)

        # Draw debug circle
        pg.draw.circle(screen, (0, 0, 255), screen_pos, 3)