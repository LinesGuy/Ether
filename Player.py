"""Da player class"""

import pygame as pg
from entity_abc import Entity
from user_input import Input
from bullet import Bullet
from combat_arts.burn import ArtBurn
from combat_arts.burst import ArtBurst
import entity_manager
from camera import Camera
from art import player_img

class Player(Entity):
    """Player class based off Entity class."""

    def __init__(self, pos=pg.Vector2(0, 0)):
        super().__init__(pos, player_img)
        self.radius = 10
        self.cooldown_frames = 5
        self.cooldown_remaining = 0
        self.frames_until_respawn = 0

    def is_dead(self):
        """Returns whether or not the player is dead based off their
        frames_until_respawn attributes"""
        return self.frames_until_respawn > 0

    def kill(self):
        """Kills the player"""
        self.frames_until_respawn = 0

    def update(self):
        """Update player position"""

        if self.is_dead():
            self.frames_until_respawn -= 1
            return

        # Movement stuffs
        speed = 3
        direction = Input.get_movement_direction()
        velocity = speed * direction
        self.pos += velocity
        # Here I would clamp the player pos but I plan to instead
        # move the camera around.

        # Set orientation
        if velocity != pg.Vector2(0, 0):
            self.orientation = velocity.angle_to(pg.Vector2(0, 0))

        # Pew pew
        if Input.get_mouse_state()[0]:
            # If holding left click...
            aim_unit = Input.get_aim_direction(self.pos*1)
            if (aim_unit != pg.Vector2(0, 0)
                and self.cooldown_remaining <= 0):
                self.cooldown_remaining = self.cooldown_frames
                velocity = aim_unit * 5  # bullet_speed = 5
                offset_pos = self.pos + aim_unit * 5 + aim_unit.rotate(90) * 2.5
                entity_manager.EntityManager.add(Bullet(offset_pos, velocity))
                offset_pos = self.pos + aim_unit * 5 - aim_unit.rotate(90) * 2.5
                entity_manager.EntityManager.add(Bullet(offset_pos, velocity))

        if self.cooldown_remaining > 0:
            self.cooldown_remaining -= 1

        # '1' to 'burn':
        if Input.check_just_pressed(pg.K_1):
            entity_manager.EntityManager.add(ArtBurn(self.pos*1,
                Input.get_aim_bearing(self.pos)))

        # '2' to 'burst'
        if Input.check_just_pressed(pg.K_2):
            entity_manager.EntityManager.add(ArtBurst(self.pos*1,
                Input.get_aim_bearing(self.pos),
                destination=Camera.get_mouse_coords()))
