"""The Entity class. Stored as entity_abc.py because naming issues."""

import pygame
import camera
from art import Default_sprite

WHITE = (255, 255, 255)

class Entity(object):
    """Entity class used for players, enemies, bullets, spawners, etc."""

    def __init__(self, pos=pygame.Vector2(), image=Default_sprite):
        self.pos = pos
        self.color = (255, 255, 255)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.center = self.pos
        self.orientation = 0 # Degrees
        self.radius = 20  # Used for circular collision detection
        self.is_expired = False

    def update(self):
        """Update the entity (e.g moving/thinking/shooting)"""
        return

    def draw(self):
        """Draw this entity on the screen"""
        screen = pygame.display.get_surface()

        screen_pos = self.pos + pygame.Vector2(screen.get_size()) / 2 - camera.Camera.pos

        # Rotate based on orientation
        output = pygame.transform.rotate(self.image, self.orientation)
        output_rect = output.get_rect()
        output_rect.center = screen_pos

        screen.blit(output, output_rect)
