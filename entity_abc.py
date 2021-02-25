"""The Entity class. Stored as entity_abc.py because naming issues."""

import pygame

from art import Default as Default_Sprite

WHITE = (255, 255, 255)

class Entity(object):
    """Entity class used for players, enemies, bullets, spawners, etc."""

    def __init__(self, position=pygame.Vector2(), image=Default_Sprite):
        self.position = position
        self.color = (255, 255, 255)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.center = self.position
        self.velocity = pygame.Vector2()
        self.orientation = 0 # Degrees
        self.radius = 20  # Used for circular collision detection
        self.is_expired = False

    def update(self):
        """Update the entity (e.g moving/thinking/shooting)"""
        return

    def draw(self):
        """Draw this entity on the screen"""
        screen = pygame.display.get_surface()
        rotated = pygame.transform.rotate(
            self.image, self.orientation)
        rotated_rect = rotated.get_rect()
        rotated_rect.center = self.position
        screen.blit(rotated, rotated_rect)
