import pygame
from globals import to_screen_coords, Q, YELLOW_COLOR

class Sensor: 
    def __init__(self,x,y):
        self.x, self.y = to_screen_coords(x,y)
        self.radius = 5 
        self.q = Q * (10**(-10)) 
        self.color = YELLOW_COLOR
        self.mass = 9.1 * (10**(-31))
    def draw(self, screen): 
        pygame.draw.circle(screen,self.color,(self.x,self.y),10,0)
    def move(self): 

        pass