import math
SCREEN_WIDTH = 1200 
SCREEN_HEIGHT = 800 

CENTER_X = SCREEN_WIDTH // 2 
CENTER_Y = SCREEN_HEIGHT // 2 
BG_COLOR = (0,0,0)
RED_COLOR = (205,28,24)
BLUE_COLOR = (0,0,139)
YELLOW_COLOR = (253, 218, 13)
K = (1200**3) * 8.99 * (10**9)
Q = 1.6 * 10**(-9)

def to_screen_coords(math_x, math_y): 
    screen_x = CENTER_X + math_x 
    screen_y = CENTER_Y - math_y
    return (screen_x, screen_y) 

def to_math_coords(screen_x, screen_y): 
    math_x = screen_x - CENTER_X 
    math_y = screen_y - CENTER_Y
    return (math_x, math_y)
def distance(a,b):
    return math.sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)


def calculate_efield(point, charges):
    end_x = 0
    end_y = 0 
    for charge in charges: 
        charge_math_pos = charge.get_math_pos()
        q = charge.get_charge()
        r_squared = (point[0] - charge_math_pos[0])**2 + (point[1] - charge_math_pos[1])**2
        if r_squared != 0: 
            e_field = (K * q) / r_squared
            direction = (point[0] - charge_math_pos[0], point[1] - charge_math_pos[1])
            angle = abs(math.atan2(direction[1], direction[0]))
            end_x += e_field * math.cos(angle)
            if direction[1] >= 0: 
                end_y -= e_field * math.sin(angle)
            else: 
                end_y += e_field * math.sin(angle)
    return to_screen_coords(end_x, end_y)

