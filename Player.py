"""Da player class"""

import pygame as pg
from entity_abc import Entity
from user_input import Input
from bullet import Bullet
from combat_arts.burn import ArtBurn
import entity_manager
from art import player_img

class Player(Entity):
    """Player class based off Entity class."""

    def __init__(self, pos=pg.Vector2(0, 0)):
        super().__init__(pos, player_img)
        self.radius = 10
        self.cooldown_frames = 6
        self.cooldown_remaining = 0
        self.frames_until_respawn = 0

    def update(self):
        """Update player position"""
        # check ded here

        # Movement stuffs
        speed = 3
        direction = Input.get_movement_direction()
        velocity = speed * direction
        self.pos += velocity
        # Here I would clamp the player pos but I plan to instead
        # move the camera around.

        if velocity != pg.Vector2(0, 0):
            self.orientation = velocity.angle_to(pg.Vector2(0, 0))

        if Input.check_just_pressed(pg.K_1):
            bullet_speed = 2
            entity_manager.EntityManager.add(ArtBurn(self.pos*1,
                Input.get_aim_bearing(self.pos)))
            print(1)