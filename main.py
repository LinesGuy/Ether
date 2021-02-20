import pygame
import math
import time
import random
import numpy as np


width, height = 1280, 720
fps = 60

GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
FUCHSIA = (255, 0, 255)
GREY = (128, 128, 128)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

pygame.init()
# pygame.mixer.init()
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Ether")
clock = pygame.time.Clock()

def interpolate(start, end, step):
    return (end - start) * step + start

class mouse():

    def __init__(self):
        self.scr_x = self.scr_y = 0 # Position of mouse on the pygame window
        self.world_x = self.world_y = 0 # Position of mouse in the in-game world
        self.down = False
        self.held_frames = 0
        self.clicked = False

    def update_position(self):
        self.scr_x, self.scr_y = pygame.mouse.get_pos()
        self.world_x = self.scr_x - width/2 + c.x   
        self.world_y = self.scr_y - height/2 + c.y

        self.held_frames += 1
        if (not self.down):
            self.held_frames = 0
        
        old_down = self.down
        self.down = pygame.mouse.get_pressed()[0]
        if (self.down and not old_down):
            self.clicked = True
        else:
            self.clicked = False

    def draw(self):
        c.circle(WHITE, (self.world_x, self.world_y), 5)

        inner_radius = 15
        outer_radius = 25
        
        spin_offset = frame / 10
        angle_offset = math.pi/10
        points = 3

        for bearing in np.arange(0, 2*math.pi, 2*math.pi / points):
            c.line(
                WHITE,
##                (self.world_x + math.cos(bearing+offset) * inner_radius,
##                 self.world_y + math.sin(bearing+offset) * inner_radius),
                (self.world_x + math.cos(bearing+spin_offset) * outer_radius,
                 self.world_y + math.sin(bearing+spin_offset) * outer_radius),
                (self.world_x + math.cos(bearing+spin_offset-angle_offset) * inner_radius,
                 self.world_y + math.sin(bearing+spin_offset-angle_offset) * inner_radius),
                2)
            c.line(
                WHITE,
                (self.world_x + math.cos(bearing+spin_offset) * outer_radius,
                 self.world_y + math.sin(bearing+spin_offset) * outer_radius),
                (self.world_x + math.cos(bearing+spin_offset+angle_offset) * inner_radius,
                 self.world_y + math.sin(bearing+spin_offset+angle_offset) * inner_radius),
                2)

m = mouse()

class player():
    
    def __init__(self):
        self.x = 0
        self.y = 0
        self.acceleration = 1
        self.aim_bearing = 0
        self.movement_bearing = 0
        self.x_velocity = 0
        self.y_velocity = 0
        self.speed = 0
        self.friction = 0.925
        self.radius = 50

    def player_bullet(self):
        yield bullet("player", self.x, self.y, self.aim_bearing, 30, 300)

    def create_movement_particle(self):
        egg_bearing = self.movement_bearing + random.random() - 0.5
        yield egg_particle(BLUE, self.x - math.cos(egg_bearing) * self.radius / math.sqrt(2), self.y - math.sin(egg_bearing) * self.radius / math.sqrt(2), -egg_bearing, 5, 900)

    def draw(self):
        #c.circle(GREEN, (self.x, self.y), 30)

        # Spinning squares:
        line_width = 2
        colour = GREEN
        spin_speed = -0.025
        for offset in np.arange(0, 2*math.pi, math.pi/2):
            theta = self.movement_bearing + frame*spin_speed + offset
            offset_theta = self.movement_bearing + frame*spin_speed + offset + math.pi/2
            c.line(colour, (self.x+math.cos(theta) * self.radius, self.y + math.sin(theta) * self.radius), (self.x+math.cos(offset_theta)*self.radius, self.y+math.sin(offset_theta)*self.radius), line_width)

        spin_speed = 0.05
        for offset in np.arange(0, 2*math.pi, math.pi/2):
            theta = self.movement_bearing + frame*spin_speed + offset
            offset_theta = self.movement_bearing + frame*spin_speed + offset + math.pi/2
            c.line(colour, (self.x+math.cos(theta) * self.radius, self.y + math.sin(theta) * self.radius), (self.x+math.cos(offset_theta)*self.radius, self.y+math.sin(offset_theta)*self.radius), line_width)

        # Bearing line:
        c.line(GREEN, (self.x, self.y), (self.x + math.cos(self.movement_bearing) * 60, self.y + math.sin(self.movement_bearing) * 60), 3)

        # Aim line:
        c.line(RED, (self.x, self.y), (self.x + math.cos(self.aim_bearing) * 60, self.y + math.sin(self.aim_bearing) * 60), 3)

    def get_movement_keypresses(self, keys):
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.push(-p.acceleration, 0)
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.push(p.acceleration, 0)
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            self.push(0, -p.acceleration)
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            self.push(0, p.acceleration)

    def push(self, delta_x, delta_y):
        self.x_velocity += delta_x
        self.y_velocity += delta_y

    def update_velocity(self):
        self.x_velocity *= self.friction
        self.y_velocity *= self.friction

    def update_bearings(self):
        self.movement_bearing = math.atan2(self.y_velocity, self.x_velocity)
        self.aim_bearing = math.atan2(m.world_y - p.y, m.world_x - p.x)

    def update_position(self):
        self.x += self.x_velocity
        self.y += self.y_velocity
        

p = player()

class camera():

    # (x,y) represent the MIDDLE of the camera, NOT the upper-left corner.

    def __init__(self):
        self.x = 0
        self.y = 0
        self.zoom = 1
        
    def move_absolute(self, coords):
        self.x, self.y = coords

    def move_relative(self, x_amount, y_amount):
        self.x += x_amount
        self.y += y_amount

    def egg_cam(self, coords): # temp name but probably will forget to rename it :shrug:
        # egg = 1: camera is locked to player
        # egg = 0: camera is still
        # egg = 0.5: camera slowly follows player (higher values = faster follow and vice versa)
        egg = 0.1
        self.x = (1-egg)*self.x + egg*p.x
        self.y = (1-egg)*self.y + egg*p.y

    def line(self, colour, start, end, line_width):
        sx = round(start[0] + width/2 - self.x)
        sy = round(start[1] + height/2 - self.y)
        ex = round(end[0] + width/2 - self.x)
        ey = round(end[1] + height/2 - self.y)
        line_width = round(line_width * self.zoom)
        pygame.draw.line(screen, colour, (sx, sy), (ex, ey), line_width)

    def circle(self, colour, centre, radius):
        x = round(centre[0] + width/2 - self.x)
        y = round(centre[1] + height/2 - self.y)
        radius = round(radius * self.zoom)
        pygame.draw.circle(screen, colour, (x, y), radius)

    def draw_gridlines(self):
        # 0,0 lines
        pygame.draw.line(screen, FUCHSIA, (int(width/2-self.x), 0), (int(width/2-self.x), height), 3)
        pygame.draw.line(screen, FUCHSIA, (0, int(height/2-self.y)), (width, int(height/2-self.y)), 3)
            
        # Other lines
        step = 150
        for line_x in np.arange(-self.x % step + (width/2)%step - step, width, step): # I hate it
            pygame.draw.line(screen, GREY, (int(line_x), 0), (int(line_x), height), 1)
        for line_y in np.arange(-self.y % step + (height/2)%step - step, height, step):
            pygame.draw.line(screen, GREY, (0, int(line_y)), (width, int(line_y)), 1)
        
    
c = camera()

class bullet():

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
        c.line(RED, (self.x, self.y), (self.x + math.cos(self.bearing) * 50, self.y + math.sin(self.bearing) * 50), 5)

bullets = list()

class egg_particle():

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
        
particles = list()

class enemy():
    # 'Enemy' object can be either an actual enemy or something that summons other enemies (or both!)

    #def __init__(self, type, )
    pass

running = True
frame = 0

while (running):

    # /`````PYGAME`````\

    clock.tick(fps)
    frame += 1
    
    events = pygame.event.get()
    for event in events:
        if (event.type == pygame.QUIT):
            running = False
    
    # \_____PYGAME_____/

    # /```GAME LOGIC```\

    p.update_velocity()
    p.update_bearings()
    p.update_position()
    # c.move_absolute((p.x, p.y))
    c.egg_cam((p.x, p.y))

    keys = pygame.key.get_pressed()
    if (keys):
        p.get_movement_keypresses(keys)

    if any([keys[pygame.K_a], keys[pygame.K_d], keys[pygame.K_w], keys[pygame.K_s]]):
        for i in range(3):
            particles += p.create_movement_particle()
        
    m.update_position()

    backfire = 8
    if (m.clicked):
        bullets += p.player_bullet()
        c.move_relative(math.cos(-p.aim_bearing)*backfire, math.sin(p.aim_bearing)*backfire)
    elif (m.held_frames % 10 == 0 and m.held_frames > 0):
        bullets += p.player_bullet()
        c.move_relative(math.cos(-p.aim_bearing)*backfire, math.sin(p.aim_bearing)*backfire)

    for b in bullets:
        b.update()

    for particle in particles:
        particle.update()
    
    # \___GAME LOGIC___/

    # /``````DRAW``````\

    screen.fill(BLACK)

    c.draw_gridlines()

    p.draw()

    m.draw()

    for index, b in enumerate(bullets):
        b.draw()
        if (b.age > b.lifespan):
            del bullets[index]

    for index, particle in enumerate(particles):
        particle.draw()
        if (particle.age > particle.lifespan):
            del particles[index]

    pygame.display.flip()

    # \______DRAW______/

# Ok, Ciao!
pygame.quit()    
