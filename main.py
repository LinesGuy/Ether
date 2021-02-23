import pygame
import math
import Game

fps = 60

pygame.init()

screen = pygame.display.set_mode((1280, 720))
#width, height = pygame.display.get_surface().get_size()

Game.game()

# Ok, Ciao!
pygame.quit()    
