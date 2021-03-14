"""Various functions for debugging"""

import pygame

pygame.font.init()

myfont = pygame.font.SysFont('Comic Sans MS', 20)

def text(surface, output="Sample text", offset=0, colour=(255,255,255)):
    """Displays given text in the top left corner"""
    textsurface = myfont.render(f"{offset}: {output}", False, colour)
    surface.blit(textsurface,(0,offset*20))
