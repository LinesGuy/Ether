import pygame
from player import *

class camera:
    x = 0
    y = 0
    zoom = 1

    # (x,y) represent the MIDDLE of the camera, NOT the upper-left corner.
    
    @classmethod
    def move_absolute(cls, coords):
        cls.x, cls.y = coords

    def move_relative(self, x_amount, y_amount):
        self.x += x_amount
        self.y += y_amount

    @classmethod
    def egg_cam(cls, coords): # temp name but probably will forget to rename it :shrug:
        # egg = 1: camera is locked to player
        # egg = 0: camera is still
        # egg = 0.5: camera slowly follows player (higher values = faster follow and vice versa)
        egg = 0.1
        cls.x = (1-egg)*cls.x + egg * player.x
        cls.y = (1-egg)*cls.y + egg * player.y

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
