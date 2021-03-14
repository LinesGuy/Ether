"""Abstract entity class"""

import pygame as pg
from camera import Camera
from art import default_img

class Entity(object):
    """Entity class used for players, enemies, bullets, spawners, etc."""

    def __init__(self, pos, image=default_img):
        self.pos = pos
        self.color = (255,255,255)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.center = self.pos
        self.orientation = 0  # Degrees
        self.radius = 20  # Used for circular collision detection
        self.is_expired = False

    def update(self):
        """Update the entity (moving/thinking/shooting)"""
        return

    def draw(self, screen):
        """Draw this entity on the screen"""

        screen_pos = Camera.get_pos_on_screen(self.pos)

        # Rotate

        width, height = self.image.get_size()
        new_width  = int(width * Camera.zoom)
        new_height = int(height * Camera.zoom)
        # Scale:
        #output = pg.transform.scale(self.image, (new_width, new_height))
        # Rotate:
        output = pg.transform.rotate(self.image, self.orientation)

        output_rect = output.get_rect()
        output_rect.center = screen_pos

        screen.blit(output, output_rect)