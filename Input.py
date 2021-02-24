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
        mouse_pos = pygame.Vector2(pygame.mouse.get_pos())
        direction = mouse_pos - player.position
        if direction.length_squared()  == 0:
            return direction
        else:
            return direction.normalize()