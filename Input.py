import pygame
import math
import Exts

class Input:
    events = list()
    last_events = list()

    is_aiming_with_mouse = True

    @staticmethod
    def mouse_position():
        # return mouse pos
        return
    
    @classmethod
    def update(cls, events):
        cls.last_events = cls.events
        #cls.last_mouse_pos = 
        cls.events = [e for e in events if e.type == pygame.KEYDOWN]

    @classmethod
    def get_movement_direction(cls):
        direction = pygame.Vector2(0, 0)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            direction.x -= 1
        if keys[pygame.K_d]:
            direction.x += 1
        if keys[pygame.K_w]:
            direction.y -= 1
        if keys[pygame.K_s]:
            direction.y += 1
        if direction.x == direction.y == 0:
            return pygame.Vector2(0, 0)
        else:
            return direction.normalize()
    
    @classmethod
    def get_aim_direction(cls, player):
        if cls.is_aiming_with_mouse:
            return cls.get_mouse_aim_direction(player)
        # else: keyboard aim stuff here
    
    @classmethod
    def get_mouse_aim_direction(cls, player):
        mouse_position = list[pygame.mouse.get_pos()]
        direction = [mouse_position[0] - player.position[0],
                     mouse_position[1] - player.position[1]]
        return Exts.normalise_vector2(direction)


class mouse:
    scr_x = 0
    scr_y = 0
    # ^ Position of mouse on the pygame window
    world_x = 0
    world_y = 0
    # ^^ Position of mouse in the in-game world
    down = False
    held_frames = 0
    clicked = False
        

    def update_position(self):
        width, height = pygame.display.get_surface().get_size()
        self.scr_x, self.scr_y = pygame.mouse.get_pos()
        self.world_x = self.scr_x - width/2 + camera.x
        self.world_y = self.scr_y - height/2 + camera.y

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
