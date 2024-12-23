import pygame
import math 
from vector import Vector
from globals import to_screen_coords, to_math_coords, BLUE_COLOR, RED_COLOR
class Charge: 
    def __init__(self, x, y, q): 
        self.x = to_screen_coords(x,y)[0] 
        self.y = to_screen_coords(x,y)[1] 
        self.q = q 
        self.radius = abs(15*q)
        if q < 0: 
            self.color = BLUE_COLOR
        else: 
            self.color = RED_COLOR
    def draw(self, screen): 
        pygame.draw.circle(screen, self.color, (self.x,self.y), self.radius, 0)
    def get_math_pos(self): 
        return to_math_coords(self.x,self.y)
    def get_charge(self): 
        return self.q
    def get_radius(self): 
        return self.radius
    def get_screen_pos(self): 
        return (self.x, self.y)
    def set_position(self, pos): 
        self.x = pos[0]
        self.y = pos[1]