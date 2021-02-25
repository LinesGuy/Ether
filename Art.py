"""Loads and stores all sprites used in the game."""

import os
import pygame

IMG_DIR = "sprites"

Default = pygame.image.load(os.path.join(IMG_DIR, "Default.png"))
Player = pygame.image.load(os.path.join(IMG_DIR, "Player.png"))
