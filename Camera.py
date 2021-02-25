""""Stores the Camera class"""

import pygame
import numpy as np

class Camera:
    """The camera of the world with various functions to move/rotate/zoom the
camera or follow the player."""

    pos = pygame.Vector2()
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
    def move_lerp(cls, destination: pygame.Vector2):
        """Lerps the camera towards given coordinates"""
        # LERP = 1: camera is locked to player
        # LERP = 0: camera is still
        # LERP = 0.5: camera slowly follows player
        # (higher values = faster follow and vice versa)
        lerp = 0.1
        cls.pos.x = (1 - lerp) * cls.pos.x + lerp * destination.x
        cls.pos.y = (1 - lerp) * cls.pos.y + lerp * destination.y

    @classmethod
    def draw_gridlines(cls):
        """Draws background grid lines. TODO: make this not ass"""
        # 0,0 lines
        screen = pygame.display.get_surface()
        width, height = screen.get_size()
        pygame.draw.line(screen, (255,0,255),
            (int(width/2-cls.pos.x), 0), (int(width/2-cls.pos.x), height), 3)
        pygame.draw.line(screen,(255,0,255),
            (0, int(height/2-cls.pos.y)), (width, int(height/2-cls.pos.y)), 3)

        # Other lines
        step = 150
        for line_x in np.arange(
                -cls.pos.x % step + (width/2)%step - step, width, step):
            pygame.draw.line(screen, (128,128,128),
                (int(line_x), 0), (int(line_x), height), 1)
        for line_y in np.arange(
                -cls.pos.y % step + (height/2)%step - step, height, step):
            pygame.draw.line(screen, (128,128,128),
                (0, int(line_y)), (width, int(line_y)), 1)
