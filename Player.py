"""The Player class"""

import pygame
import bullet
import entity_manager
from art import Player_sprite
import entity_abc
import user_input

class Player(entity_abc.Entity):
    """Player class based off Entity class. This allows for multiple
    player objects but currently the game only supports one player."""
    radius = 10

    def __init__(self, pos=pygame.Vector2(0, 0)):
        super().__init__(pos, Player_sprite)
        self.radius = 10
        self.cooldown_frames = 6
        self.cooldown_remaining = 0
        self.frames_until_respawn = 0

    def is_dead(self):
        """Returns whether or not the player is dead based off their
        frames_until_respawn value"""
        return self.frames_until_respawn > 0

    def kill(self):
        """Kills the player by setting their frames_until_respawn
        value to 60"""
        self.frames_until_respawn = 60

    def update(self):
        """Update player pos (if not dead)"""
        if self.is_dead():
            self.frames_until_respawn -= 1
            return

        # Movement stuffs
        speed = 8
        direction = user_input.Input.get_movement_direction()
        velocity = speed * direction
        self.pos += velocity
        # Here I would clamp the player pos but I plan to instead
        # move the camera around.

        if velocity != pygame.Vector2(0, 0):
            self.orientation = velocity.angle_to(pygame.Vector2(0, 0))

        # Shooty stuffs
        if user_input.Input.get_mouse_state()[0]:
            # ^ If holding left click...
            aim_direction = user_input.Input.get_aim_direction(self)
            aim = aim_direction * 20

            if aim.length_squared() > 0 and self.cooldown_remaining <= 0:
                self.cooldown_remaining = self.cooldown_frames
                # TODO: offset bullet pos
                offset_pos = self.pos * 1

                entity_manager.EntityManager.add(bullet.Bullet(offset_pos, aim))

        if self.cooldown_remaining > 0:
            self.cooldown_remaining -= 1
