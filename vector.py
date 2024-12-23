import math 
import pygame 

class Vector: 
    def __init__(self, start_x, start_y, end_x, end_y):
        self.start_x = start_x 
        self.start_y = start_y 
        self.end_x = end_x 
        self.end_y = end_y 

    def get_mag(self): 
        return math.sqrt((self.end_x - self.start_x)**2 + (self.end_y - self.start_y)**2)
    
    def get_dx(self): 
        return (self.end_x - self.start_x)
    def get_dy(self): 
        return (self.end_y - self.start_y) 
    def normalize(self): 
        mag = self.get_mag()
        if mag == 0: 
            return Vector(self.start_x, self.start_y, self.end_x, self.end_y)
        end_x = (self.get_dx() / mag) + self.start_x
        end_y = (self.get_dy() / mag) + self.start_y
        self.end_x = end_x 
        self.end_y = end_y
        return Vector(self.start_x, self.start_y, end_x, end_y)
    def draw(self, screen, color, width=2, arrow_size = 10): 
        pygame.draw.line(screen, color, (self.start_x, self.start_y), (self.end_x, self.end_y))
        dir_angle = math.atan2(self.get_dy(), self.get_dx()) 
        arrow_angle = math.pi / 6 
        left_x = self.end_x - arrow_size * math.cos(dir_angle - arrow_angle)
        left_y = self.end_y - arrow_size * math.sin(dir_angle - arrow_angle)

        right_x = self.end_x - arrow_size * math.cos(dir_angle + arrow_angle)
        right_y = self.end_y - arrow_size * math.sin(dir_angle + arrow_angle) 


        pygame.draw.polygon(screen,color,[(self.end_x, self.end_y), (left_x, left_y), (right_x, right_y)])
    def scale(self, factor): 
        scaled_dx = self.get_dx() * factor 
        scaled_dy = self.get_dy() * factor 
        end_x = self.start_x + scaled_dx 
        end_y = self.start_y + scaled_dy 
        self.end_x = end_x 
        self.end_y = end_y
        return Vector(self.start_x, self.start_y, end_x, end_y) 