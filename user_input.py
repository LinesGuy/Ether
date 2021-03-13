"""da Input class"""

import pygame as pg
from camera import Camera

class Input:
    """Functions for getting and handling user inputs"""

    keys = None
    last_keys = None

    @property
    def mouse_position(self):
        """Returns the mouse position on the screen"""
        # cba
        return

    @classmethod
    def update(cls):
        """Save previous keyboard and mouse inputs and update to new inputs"""
        cls.last_keys = cls.keys
        cls.keys = pg.key.get_pressed()

    @classmethod
    def check_just_pressed(cls, k):
        """Returns whether or not a given key was just pressed"""
        return cls.keys[k] and not cls.last_keys[k]

    @classmethod
    def get_movement_direction(cls):
        """Get unit vector of diretction player is moving"""
        direction = pg.Vector2(0, 0)
        if cls.keys[pg.K_a]:
            direction.x -= 1
        if cls.keys[pg.K_d]:
            direction.x += 1
        if cls.keys[pg.K_w]:
            direction.y -= 1
        if cls.keys[pg.K_s]:
            direction.y += 1
        if direction.x == direction.y == 0:
            return pg.Vector2(0, 0)
        else:
            return direction.normalize()

    @classmethod
    def move_camera(cls):
        """Get arrow key inputs and move camera accordingly"""
        direction = pg.Vector2(0, 0)
        if cls.keys[pg.K_LEFT]:
            direction.x -=1
        if cls.keys[pg.K_RIGHT]:
            direction.x += 1
        if cls.keys[pg.K_UP]:
            direction.y -= 1
        if cls.keys[pg.K_DOWN]:
            direction.y += 1
        direction *= 5
        Camera.move_relative(direction)

    @classmethod
    def get_aim_bearing(cls, pos):
        """Returns an angle in degrees representing the aim bearing"""
        aim_direction = cls.get_aim_direction(pos)
        bearing = pg.Vector2(0, 0).angle_to(aim_direction)
        return bearing
    @classmethod
    def get_aim_direction(cls, pos) -> pg.Vector2:
        """Returns a unit vector from a given position to the mouse position"""
        mouse_pos = Camera.get_mouse_coords()
        direction = mouse_pos - pos
        if direction.length_squared()  == 0:
            return direction
        else:
            return direction.normalize()

    @classmethod
    def get_mouse_state(cls):
        """Returns left/right click mouse button states"""
        left_click, right_click, _ = pg.mouse.get_pressed(num_buttons=3)
        return (left_click, right_click)