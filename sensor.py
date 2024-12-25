import pygame
from globals import to_screen_coords, Q, YELLOW_COLOR, to_math_coords, calculate_efield

class Sensor: 
    def __init__(self,x,y):
        self.x, self.y = to_screen_coords(x,y)
        self.radius = 5 
        self.q = Q * (10**(-10)) 
        self.color = YELLOW_COLOR
        self.mass = 3 * (10**(-11))
        self.velocity = [0,0]
        self.acceleration = [0,0]
    def draw(self, screen): 
        pygame.draw.circle(screen,self.color,(self.x,self.y),10,0)
    def move(self, charges):
        math_pos = to_math_coords(self.x, self.y)
        e_field = calculate_efield(math_pos, charges)
        self.acceleration[0] = e_field[0] * (self.q / self.mass) 
        self.acceleration[1] = e_field[1] * (self.q / self.mass)

        self.velocity[0] += self.acceleration[0]
        self.velocity[1] += self.acceleration[1]
        self.x += self.velocity[0]
        self.y += self.velocity[1]