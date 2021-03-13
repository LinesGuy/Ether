"""Loads and stores all sprites used in the game"""

import os
import pygame

IMG_DIR = "sprites"

default_img = pygame.image.load(os.path.join(IMG_DIR, "Default.png"))
player_img  = pygame.image.load(os.path.join(IMG_DIR, "Player.png"))
player_img.set_colorkey((0, 0, 0))
bullet_img  = pygame.image.load(os.path.join(IMG_DIR, "Bullet.png"))