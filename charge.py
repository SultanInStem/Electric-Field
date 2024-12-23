import pygame
import math 
from vector import Vector
from globals import to_screen_coords
class Charge: 
    def __init__(self, x, y, q = 1): 
        self.x = to_screen_coords(x,y)[0] 
        self.y = to_screen_coords(x,y)[1] 
        self.q = q 
        if q < 0: 
            self.color = (0,0,139)
        else: 
            self.color = (205,28,24)
    def draw(self, screen): 
        pygame.draw.circle(screen, self.color, (self.x,self.y), 15, 0)
