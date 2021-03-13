"""Stores the Camera class"""

import pygame as pg

class Camera:
    """Camera of the world with various functoins to move the camera
    and/or follow the player"""

    WINDOW_SIZE = None
    PIXEL_SCALE = None
    DISPLAY_SIZE = None

    pos = pg.Vector2(0, 0)
    # ^ Represents the top-left of the screen

    @classmethod
    def set_dimensions(cls, WINDOW_SIZE: tuple, scale: int):
        cls.WINDOW_SIZE = WINDOW_SIZE
        cls.DISPLAY_SIZE = tuple(pg.Vector2(WINDOW_SIZE) / scale)
        cls.PIXEL_SCALE = scale
        cls.pos -= pg.Vector2(cls.DISPLAY_SIZE) / 2

    @classmethod
    def get_mouse_coords(cls):
        """Gets coordinates of mouse in the world, not on the screen"""
        mouse_pos = pg.Vector2(pg.mouse.get_pos()) / Camera.PIXEL_SCALE
        mouse_world_pos = mouse_pos + Camera.pos
        return mouse_world_pos

    @classmethod
    def move_absolute(cls, destination):
        """Moves camera to given coordinates. Remember to provide the top-left
        of the screen, not the middle. move_relative is recommended."""
        cls.pos = destination

    @classmethod
    def move_relative(cls, delta):
        """Moves camera relative to current position"""
        cls.pos += delta

    @classmethod
    def lerp(cls, destination):
        """Lerps the camera towards given coordinates"""
        # LERP = 1: camera is locked to player
        # LERP = 0: camera is still
        # LERP = 0.5: camera slowly follows player
        # (higher values = faster follow and vice versa)
        lerp = 0.1
        cls.pos.x = (1 - lerp) * cls.pos.x + lerp * destination.x
        cls.pos.y = (1 - lerp) * cls.pos.y + lerp * destination.y
