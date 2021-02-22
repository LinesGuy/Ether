import pygame
import math
import Exts
from Art import Default as Default_Sprite

WHITE = (255, 255, 255)

class Entity(object):

    def __init__(self, position=(0, 0), image=Default_Sprite):
        self.position = position
        self.color = (255, 255, 255)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.center = self.position
        self.velocity = (0, 0)
        self.orientation = 0
        self.radius = 20  # Used for circular collision detection
        self.is_expired = False
    
    def size(self):
        if self.image is None:
            return (0, 0)
        else:
            return (self.image.get_width(), self.image.get_height())
    
    def update(self):
        pass

    def draw(self, screen):
        # screen.draw stuff
        rotated = pygame.transform.rotate(
            self.image, math.degrees(self.orientation))
        screen.blit(rotated, self.rect)