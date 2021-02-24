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
        self.autofire = True  # If false, player has to hold left click to NOT shoot. (not actually implemented yet) 
        
    def is_dead(self):
        return self.frames_until_respawn > 0
    
    def kill(self):
        self.frames_until_respawn = 60
    
    def draw(self):
        super().draw()
        # debug line:
        screen = pygame.display.get_surface()
        aim_v = Input.Input.get_aim_direction(self)  # Aim vector
        aim_r = math.radians(-aim_v.angle_to(pygame.Vector2(0, 0)))  # Aim angle (radians)

        # ^ Aim directions in radians
        pygame.draw.line(screen, (0, 255, 0), (self.position),
            (self.position.x + math.cos(aim_r) * 100, self.position.y + math.sin(aim_r) * 100), 3)

    def update(self):
        if (self.is_dead()):
            self.frames_until_respawn -= 1
            return
        
        # Movement stuffs
        SPEED = 8
        direction = Input.Input.get_movement_direction()
        self.velocity = SPEED * direction
        self.position += self.velocity
        # Here I would clamp the player position but I plan to instead
        # move the camera around.

        if self.velocity != pygame.Vector2(0, 0):
            self.orientation = self.velocity.angle_to(pygame.Vector2(0, 0))

        

#    def player_bullet(self):
#        yield bullet("player", self.x, self.y, self.aim_bearing, 30, 300)

#    def create_movement_particle(self):
#        egg_bearing = self.movement_bearing + random.random() - 0.5
#        yield egg_particle(BLUE, self.x - math.cos(egg_bearing) * self.radius / math.sqrt(2), self.y - math.sin(egg_bearing) * self.radius / math.sqrt(2), -egg_bearing, 5, 900)

#    def push(self, delta_x, delta_y):
#        self.x_velocity += delta_x
#        self.y_velocity += delta_y