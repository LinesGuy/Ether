"""Initialises pygame and decides which screen to show
(currently only Game.game())"""

import pygame
import game

pygame.init()

screen = pygame.display.set_mode((1280, 720))
#width, height = pygame.display.get_surface().get_size()

game.game()

# Ok, Ciao!
pygame.quit()
