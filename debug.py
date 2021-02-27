"""Various functions for debugging"""

import pygame

pygame.font.init()

myfont = pygame.font.SysFont('Comic Sans MS', 20)

def text(text="Sample text", offset=0, colour=(255,255,255)):
    """Displays given text in the top left corner"""
    screen = pygame.display.get_surface()
    textsurface = myfont.render(f"{offset}: {text}", False, colour)
    screen.blit(textsurface,(0,offset*20))
    