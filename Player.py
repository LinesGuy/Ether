import pygame
import Entity
import os
import math
from Art import Player as Player_sprite

class Player(Entity.Entity):
    
    def __init__(self, position=(0, 0)):
        super().__init__(position, Player_sprite)
        self.COOLDOWN_FRAMES = 6
        self.cooldown_remaining = 0
        self.frames_until_respawn = 0        
        
    def is_dead(self):
        return self.frames_until_respawn > 0

    def update(self):
        pass

#    def player_bullet(self):
#        yield bullet("player", self.x, self.y, self.aim_bearing, 30, 300)

#    def create_movement_particle(self):
#        egg_bearing = self.movement_bearing + random.random() - 0.5
#        yield egg_particle(BLUE, self.x - math.cos(egg_bearing) * self.radius / math.sqrt(2), self.y - math.sin(egg_bearing) * self.radius / math.sqrt(2), -egg_bearing, 5, 900)

#    def draw(self):
        #c.circle(GREEN, (self.x, self.y), 30)

        # Spinning squares:
#        line_width = 2
#        colour = GREEN
#        spin_speed = -0.025
#        for offset in np.arange(0, 2*math.pi, math.pi/2):
#            theta = self.movement_bearing + frame*spin_speed + offset
#            offset_theta = self.movement_bearing + frame*spin_speed + offset + math.pi/2
#            c.line(colour, (self.x+math.cos(theta) * self.radius, self.y + math.sin(theta) * self.radius), (self.x+math.cos(offset_theta)*self.radius, self.y+math.sin(offset_theta)*self.radius), line_width)

#        spin_speed = 0.05
#        for offset in np.arange(0, 2*math.pi, math.pi/2):
#            theta = self.movement_bearing + frame*spin_speed + offset
#            offset_theta = self.movement_bearing + frame*spin_speed + offset + math.pi/2
#            c.line(colour, (self.x+math.cos(theta) * self.radius, self.y + math.sin(theta) * self.radius), (self.x+math.cos(offset_theta)*self.radius, self.y+math.sin(offset_theta)*self.radius), line_width)

        # Bearing line:
        #c.line(GREEN, (self.x, self.y), (self.x + math.cos(self.movement_bearing) * 60, self.y + math.sin(self.movement_bearing) * 60), 3)

        # Aim line:
        #c.line(RED, (self.x, self.y), (self.x + math.cos(self.aim_bearing) * 60, self.y + math.sin(self.aim_bearing) * 60), 3)

    #def get_movement_keypresses(self, keys):
#        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
#            self.push(-p.acceleration, 0)
#        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
#            self.push(p.acceleration, 0)
#        if keys[pygame.K_UP] or keys[pygame.K_w]:
#            self.push(0, -p.acceleration)
#        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
#            self.push(0, p.acceleration)

#    def push(self, delta_x, delta_y):
#        self.x_velocity += delta_x
#        self.y_velocity += delta_y

#    @classmethod
#    def update(self):
#        pass
    
#    @classmethod
#    def update_velocity(cls):
#        cls.x_velocity *= cls.friction
#        cls.y_velocity *= cls.friction

#    def update_bearings(self):
#        self.movement_bearing = math.atan2(self.y_velocity, self.x_velocity)
#        self.aim_bearing = math.atan2(mouse.world_y - self.y, mouse.world_x - cls.x)

#    @classmethod
#    def update_position(cls):
#        cls.x += cls.x_velocity
#        cls.y += cls.y_velocity