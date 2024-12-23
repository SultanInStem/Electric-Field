SCREEN_WIDTH = 1200 
SCREEN_HEIGHT = 800 

CENTER_X = SCREEN_WIDTH // 2 
CENTER_Y = SCREEN_HEIGHT // 2 
BG_COLOR = (0,0,0)

def to_screen_coords(math_x, math_y): 
    screen_x = CENTER_X + math_x 
    screen_y = CENTER_Y - math_y
    return (screen_x, screen_y) 

def to_math_coords(screen_x, screen_y): 
    math_x = screen_x - CENTER_X 
    math_y = screen_y - CENTER_Y
    return (math_x, math_y)


