import pygame

class Particle():
    particles_list = list()

    def __init__(self, colour, x, y, bearing, speed, lifespan):
        self.colour = colour
        self.x = x
        self.y = y
        self.bearing = bearing
        self.speed = speed
        self.friction = 0.975
        self.lifespan = lifespan
        self.age = 0

    def update(self):
        self.age += 1
        self.speed *= self.friction
        self.x -= math.cos(self.bearing) * self.speed
        self.y += math.sin(self.bearing) * self.speed

    def draw(self):
        c.circle(self.colour, (self.x, self.y), 2)