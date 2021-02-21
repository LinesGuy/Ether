import pygame
import Exts

WHITE = (255, 255, 255)

class Entity(object):

    def __init__(self):
        self.image = None
        self.color = (255, 255, 255)
        self.position = Exts.vector2(0, 0)
        self.velocity = Exts.vector2(0, 0)
        self.radius = 20  # Used for circular collision detection
        self. IsExpired = False
    
    def size(self):
        if image is None:
            return Exts.vector2(0, 0)
        else:
            return Exts.vector2(image.x, image.y)
    
    def update(self):
        pass

    def draw(self, screen):
        # screen.draw stuff
        pass