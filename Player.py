"""The Player class"""

import math
import pygame
from art import Player as Player_sprite
import entity_abc

import user_input


class Player(entity_abc.Entity):
    """Player class based off Entity class. This allows for multiple
    player objects but currently the game only supports one player."""

    autofire = True

    def __init__(self, position=pygame.Vector2(0, 0)):
        super().__init__(position, Player_sprite)
        self.radius = 10
        self.cooldown_frames = 6
        self.cooldown_remaining = 0
        self.frames_until_respawn = 0
        # ^ If false, player has to hold left click to NOT shoot.

    def is_dead(self):
        """Returns whether or not the player is dead based off their
        frames_until_respawn value"""
        return self.frames_until_respawn > 0

    def kill(self):
        """Kills the player by setting their frames_until_respawn
        value to 60"""
        self.frames_until_respawn = 60

    def draw(self):
        super().draw()
        # debug line:
        screen = pygame.display.get_surface()
        aim_v = user_input.Input.get_aim_direction(self)  # Aim vector
        aim_r = math.radians(-aim_v.angle_to(pygame.Vector2(0, 0)))  # Aim angle (radians)

        # ^ Aim directions in radians
        pygame.draw.line(screen, (0, 255, 0), (self.position),
            (self.position.x + math.cos(aim_r) * 100, self.position.y + math.sin(aim_r) * 100), 3)

    def update(self):
        """Update player position (if not dead)"""
        if self.is_dead():
            self.frames_until_respawn -= 1
            return

        # Movement stuffs
        speed = 8
        direction = user_input.Input.get_movement_direction()
        self.velocity = speed * direction
        self.position += self.velocity
        # Here I would clamp the player position but I plan to instead
        # move the camera around.

        if self.velocity != pygame.Vector2(0, 0):
            self.orientation = self.velocity.angle_to(pygame.Vector2(0, 0))
