"""Stores the Camera class"""

import pygame as pg
import entity_manager
import user_input

class Camera:
    """Camera of the world with various functoins to move the camera
    and/or follow the player"""

    WINDOW_SIZE = None  # Size of the surface that the user sees
    PIXEL_SCALE = None  # 4 means one display pixel = 4x4 window pixels
    DISPLAY_SIZE = None # Size of surface that everything is drawn to

    is_lerping = True  # If false, camera can move freely.

    zoom = 1  # Higher = more zoomed in
    orientation = 0  # Degrees

    pos = pg.Vector2(0, 0)
    # ^ Represents the top-left of the screen

    @classmethod
    def get_pos_on_screen(cls, pos):
        # Scale (zoom)
        pos = (pos - cls.pos) * cls.zoom + cls.pos

        # Rotate

        # Translate (move)

        pos = pos - cls.pos  # If you do `pos -= cls.pos` then it fucks up. WHY

        # Translate by half the display size because why not
        pos = pos + pg.Vector2(cls.DISPLAY_SIZE) / 2

        return pos

    @classmethod
    def get_pos_from_screen(cls, pos):
        # Translate by half the display size

        pos = pos - pg.Vector2(cls.DISPLAY_SIZE) / 2

        # Translate
        pos = pos + cls.pos

        # Rotate

        # Scale
        pos = (pos - cls.pos) / cls.zoom + cls.pos

        return pos

    @classmethod
    def update(cls):
        """Various updates related to camera (lerp, move, etc)"""

        # Freecam (disables lerp if used)
        direction = pg.Vector2(0, 0)
        keys = user_input.Input.keys
        if keys[pg.K_LEFT]:
            direction.x -=1
        if keys[pg.K_RIGHT]:
            direction.x += 1
        if keys[pg.K_UP]:
            direction.y -= 1
        if keys[pg.K_DOWN]:
            direction.y += 1
        if direction != pg.Vector2(0, 0):
            cls.is_lerping = False
            direction *= 5
            Camera.move_relative(direction)

        old_zoom = cls.zoom
        # Zoom (Q and E)
        if keys[pg.K_q]:
            cls.zoom /= 1.03
        if keys[pg.K_e]:
            cls.zoom *= 1.03
        if old_zoom != cls.zoom:
            #cls.is_lerping = False
            #zoom_center = cls.get_mouse_coords()
            #zoom_center = entity_manager.EntityManager.player.pos
            zoom_center = cls.pos
            zoom_change = cls.zoom - old_zoom
            #cls.pos = cls.pos + (zoom_center * zoom_change)

        # Lerp
        if cls.is_lerping:
            Camera.lerp(entity_manager.EntityManager.player.pos)
        else:
            # 'c' to enable lerp
            if user_input.Input.keys[pg.K_c]:
                cls.is_lerping = True


    @classmethod
    def set_dimensions(cls, WINDOW_SIZE: tuple, scale: int):
        cls.WINDOW_SIZE = WINDOW_SIZE
        cls.DISPLAY_SIZE = tuple(pg.Vector2(WINDOW_SIZE) / scale)
        cls.PIXEL_SCALE = scale
        #cls.pos -= pg.Vector2(cls.DISPLAY_SIZE) / 2

    @classmethod
    def get_mouse_coords(cls):
        """Gets coordinates of mouse in the world, not on the screen.
        To get screen coords, divide mouse window coords by PIXEL_SCALE"""
        mouse_pos = pg.Vector2(pg.mouse.get_pos()) / cls.PIXEL_SCALE
        mouse_world_pos = cls.get_pos_from_screen(mouse_pos)
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
