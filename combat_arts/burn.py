import pygame as pg
from bullet import Bullet
from entity_abc import Entity
from user_input import Input
import entity_manager
import random
from camera import Camera

class ArtBurn(Bullet):
    """The 'burn' combat art, summons numerous mini-bombs in front
    of the player"""

    def __init__(self, pos, direction: float):
        # direction is in degrees
        # lifespan = 20
        # bullet_speed = 2
        velocity = pg.Vector2(1,0).rotate(direction) * 4  # bullet_speed = 4
        pos = pos + velocity * 5  # Start burn slightly in front of player
        super().__init__(pos, velocity, lifespan=30)

    def update(self):
        self.pos += self.velocity

        self.age += 1
        if self.age > self.lifespan:
            self.is_expired = True

        # summon MiniBomb
        for i in range(1):
            minibomb_pos = (self.pos + self.velocity.normalize().rotate(90)
                * (random.random() * 30 - 15))
            entity_manager.EntityManager.add(MiniBomb(minibomb_pos))


    def draw(self, screen):
        screen_pos = Camera.get_pos_on_screen(self.pos)

        # Draw debug circle
        pg.draw.circle(screen, (0, 255, 0), screen_pos, 3)

class MiniBomb(Entity):
    """Small bomb used by the ArtBurn entity"""

    def __init__(self, pos):
        super().__init__(pos)
        self.lifespan = random.randint(38, 42)
        self.age = 0

    def update(self):
        self.age += 1
        if self.age > self.lifespan:
            entity_manager.EntityManager.add(BombShockwave(self.pos))
            self.is_expired = True

    def draw(self, screen):
        screen_pos = Camera.get_pos_on_screen(self.pos)

        # Temp red circle
        colour = (127 + int(self.age/self.lifespan*128), 0, 0)
        pg.draw.circle(screen, colour, screen_pos, 2)

class BombShockwave(Entity):
    """Small shockwave created after MiniBomb explodes"""

    def __init__(self, pos):
        super().__init__(pos)
        self.lifespan = 10
        self.age = 0

    def update(self):
        self.age += 1
        if self.age > self.lifespan:
            self.is_expired = True

    def draw(self, screen):
        screen_pos = Camera.get_pos_on_screen(self.pos)

        # Draw shockwave
        radius = 2 + self.age
        if self.age < 5:
            pg.draw.circle(screen, (255, 128, 0), screen_pos, radius, 0)
        else:
            pg.draw.circle(screen, (64, 64, 64), screen_pos, radius, 1)
