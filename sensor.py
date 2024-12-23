import pygame
from globals import to_screen_coords, Q, YELLOW_COLOR

class Sensor: 
    def __init__(self,x,y):
        self.x, self.y = to_screen_coords(x,y)
        self.radius = 5 
        self.q = Q * (10**(-10)) 
        self.color = YELLOW_COLOR
    def draw(self, screen): 
        pygame.draw.circle(screen)
    