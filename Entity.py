import pygame
import math
import Exts
from Art import Default as Default_Sprite

WHITE = (255, 255, 255)

class Entity(object):

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
    
    # Is this ever even used?
#    def size(self):
#        if self.image is None:
#            return [0, 0]
#        else:
#            return [self.image.get_width(), self.image.get_height()]
    
    def update(self):
        pass

    def draw(self):
        screen = pygame.display.get_surface()
        rotated = pygame.transform.rotate(
            self.image, self.orientation)
        rotated_rect = rotated.get_rect()
        rotated_rect.center = self.position
        screen.blit(rotated, rotated_rect)