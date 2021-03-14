"""The Bullet class"""

import pygame as pg
from art import bullet_img
from entity_abc import Entity

class Bullet(Entity):
    """Bullet class based off Entity class. Bullets can be fired from enemies
    or players. Expires after 5 seconds or if off-screen."""

    def __init__(self, pos, velocity, lifespan=120):
        super().__init__(pos, bullet_img)
        self.velocity = velocity
        self.orientation = velocity.angle_to(pg.Vector2(0, 0))  # Degrees
        self.lifespan = lifespan  # Frames
        self.age = 0

    def update(self):
        self.pos += self.velocity

        self.age += 1
        if self.age > self.lifespan:
            self.is_expired = True
