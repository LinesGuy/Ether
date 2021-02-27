"""Loads and stores all sprites used in the game."""

import os
import pygame

IMG_DIR = "sprites"

Default_sprite = pygame.image.load(os.path.join(IMG_DIR, "Default.png"))
Player_sprite = pygame.image.load(os.path.join(IMG_DIR, "Player.png"))
Bullet_sprite = pygame.image.load(os.path.join(IMG_DIR, "Bullet.png"))
