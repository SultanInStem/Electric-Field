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

