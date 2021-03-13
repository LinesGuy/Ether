"""Stores the Camera class"""

import pygame
import numpy as np

class Camera:
    """The camera of the world with various functions to move/rotate/zoom the
camera or follow the player."""

    pos = pygame.Vector2(0, 0)
    zoom = 1
    orientation = 0 # Radians

    # (x,y) represent the MIDDLE of the camera, NOT the upper-left corner.

    @classmethod
    def move_absolute(cls, destination: pygame.Vector2):
        """Moves camera to given coordinates"""
        cls.pos = destination

    @classmethod
    def move_relative(cls, delta: pygame.Vector2):
        """Moves camera relative to its current position"""
        cls.pos += delta

    # LERP CAM
    @classmethod
    def lerp(cls, destination: pygame.Vector2):
        """Lerps the camera towards given coordinates"""
        # LERP = 1: camera is locked to player
        # LERP = 0: camera is still
        # LERP = 0.5: camera slowly follows player
        # (higher values = faster follow and vice versa)
        lerp = 0.1
        cls.pos.x = (1 - lerp) * cls.pos.x + lerp * destination.x
        cls.pos.y = (1 - lerp) * cls.pos.y + lerp * destination.y
