"""The Bullet class"""

import pygame
from art import Bullet_sprite
import entity_abc

class Bullet(entity_abc.Entity):
    "Bullet class based off Entity class. Bullets can be fired from the "
    "players or entities. Expires after 5 seconds or going off-screen."

    def __init__(self, pos, velocity, lifespan=300):
        super().__init__(pos, Bullet_sprite)
        self.velocity = velocity
        self.orientation = velocity.angle_to(pygame.Vector2(0,0))
        self.lifespan = lifespan


    def update(self):
        """Move the bullet using its velocity vector"""
        self.pos += self.velocity
