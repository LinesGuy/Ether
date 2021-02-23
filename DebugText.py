import pygame

pygame.font.init()

myfont = pygame.font.SysFont('Comic Sans MS', 20)

def disp(text="Sample text", offset=0, colour=(255,255,255)):
    screen = pygame.display.get_surface()
    textsurface = myfont.render(text, False, colour)
    screen.blit(textsurface,(0,offset*20))