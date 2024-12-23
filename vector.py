import math 
import pygame 
from globals import to_math_coords, to_screen_coords, K, distance
class Vector: 
    def __init__(self, start_x, start_y, end_x, end_y):
        self.start_x = to_screen_coords(start_x, start_y)[0]
        self.start_y = to_screen_coords(start_x, start_y)[1]
        self.end_x = to_screen_coords(end_x, end_y)[0] 
        self.end_y = to_screen_coords(end_x, end_y)[1]
        self.color = (255,255,255)

    def get_mag(self): 
        return math.sqrt((self.end_x - self.start_x)**2 + (self.end_y - self.start_y)**2)
    def calculate_direction_from_charges(self, charges): 
        math_end_pos = to_math_coords(self.end_x, self.end_y)
        math_start_pos = to_math_coords(self.start_x, self.start_y)
        end_x = 0 
        end_y = 0 
        for charge in charges: 
            q_math_pos = charge.get_math_pos()
            q = charge.get_charge()
            r_squared = (math_start_pos[0] - q_math_pos[0])**2 + (math_start_pos[1] - q_math_pos[1])**2
            if r_squared != 0: 
                e_field = (K * q) / r_squared
                dir_v = (math_start_pos[0] - q_math_pos[0], math_start_pos[1] - q_math_pos[1])
                angle = abs(math.atan2(dir_v[1], dir_v[0]))    
                end_x += e_field * math.cos(angle)
                if dir_v[1] > 0: 
                    end_y -= e_field * math.sin(angle)
                else: 
                    end_y += e_field * math.sin(angle)


        self.end_x = to_screen_coords(end_x, end_y)[0]
        self.end_y = to_screen_coords(end_x, end_y)[1]
        normalized_mag = min(1, self.get_mag() / 150000)
        gray_value = int(255 * (normalized_mag)) 
        self.color = (gray_value, gray_value, gray_value)
        self.normalize()
        self.scale(30)
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
    def draw(self, screen, width=4, arrow_size = 10): 
        color = self.color
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