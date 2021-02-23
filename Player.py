import pygame
import Entity
import os
import math
import Input
import Exts
from Art import Player as Player_sprite

class Player(Entity.Entity):
    
    def __init__(self, position=[0, 0]):
        super().__init__(position, Player_sprite)
        self.radius = 10
        self.COOLDOWN_FRAMES = 6
        self.cooldown_remaining = 0
        self.frames_until_respawn = 0        
        
    def is_dead(self):
        return self.frames_until_respawn > 0
    
    def kill(self):
        self.frames_until_respawn = 60

    def update(self):
        if (self.is_dead()):
            self.frames_until_respawn -= 1
            return
        
        # Movement stuffs
        SPEED = 8
        direction = Input.Input.get_movement_direction()
        self.velocity = SPEED * direction
        self.position += self.velocity

        self.orientation = self.velocity.angle_to(pygame.Vector2(0, 1))
        # Set orientation
#        if velocity[0] ** 2 + velocity[1] ** 2 > 0:
#            self.orientation = Exts.vector2_to_angle(velocity)

        

#    def player_bullet(self):
#        yield bullet("player", self.x, self.y, self.aim_bearing, 30, 300)

#    def create_movement_particle(self):
#        egg_bearing = self.movement_bearing + random.random() - 0.5
#        yield egg_particle(BLUE, self.x - math.cos(egg_bearing) * self.radius / math.sqrt(2), self.y - math.sin(egg_bearing) * self.radius / math.sqrt(2), -egg_bearing, 5, 900)

#    def push(self, delta_x, delta_y):
#        self.x_velocity += delta_x
#        self.y_velocity += delta_y