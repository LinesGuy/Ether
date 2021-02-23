import pygame

# all outdated code
class bullet():
    bullet_list = list()

    def __init__(self, sender, x, y, bearing, speed, lifespan):
        self.sender = sender
        self.x = x
        self.y = y
        self.bearing = bearing
        self.speed = speed
        self.lifespan = lifespan
        self.age = 0

    def update(self):
       self.age += 1
       self.x += math.cos(self.bearing) * self.speed
       self.y += math.sin(self.bearing) * self.speed

    def draw(self):
        #c.circle(GREEN, (self.x, self.y), 5)
        camera.line(RED, (self.x, self.y), (self.x + math.cos(self.bearing) * 50, self.y + math.sin(self.bearing) * 50), 5)
