import pygame 
import sys
from vector import Vector
import globals
from globals import distance, Q, to_math_coords, to_screen_coords, SCREEN_WIDTH, SCREEN_HEIGHT
from charge import Charge
from sensor import Sensor
import pygame.gfxdraw
class Canvas: 
    def __init__(self): 
        pygame.init()
        self.screen = pygame.display.set_mode((globals.SCREEN_WIDTH, globals.SCREEN_HEIGHT))
        pygame.display.set_caption("Vector Field Simulation")
        self.clock = pygame.time.Clock()
        self.running = True
        self.charges = [Charge(0,-200,Q), Charge(0,200,-Q)]
        self.sensors = []
        self.vectors = []
        self.dragging = False
        self.dragging_index = 0 


        for i in range(-30, 30): 
            for j in range(-30, 30): 
                v = Vector(i*40,j*40, 0,0)
                v.normalize()
                v.scale(25)
                self.vectors.append(v)
    
    def handle_events(self): 
        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                self.running = False
            elif event.type == pygame.MOUSEBUTTONDOWN: 
                for i in range(0, len(self.charges)): 
                    dist = distance(event.pos, self.charges[i].get_screen_pos())
                    if dist <=  self.charges[i].get_radius(): 
                        self.dragging = True
                        self.dragging_index = i
            elif event.type == pygame.MOUSEBUTTONUP: 
                self.dragging = False 
            elif event.type == pygame.MOUSEMOTION and self.dragging:
                self.charges[self.dragging_index].set_position(event.pos)
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE: 
                    x,y = to_math_coords(pygame.mouse.get_pos()[0],pygame.mouse.get_pos()[1])
                    self.sensors.append(Sensor(x, -y))
    def render(self): 
        self.screen.fill((0,0,0))

        for v in self.vectors: 
            v.draw(self.screen)
        for q in self.charges: 
            q.draw(self.screen)

        for i in range(0, len(self.sensors)): 
            self.sensors[i].draw(self.screen)


        pygame.display.flip()
        self.clock.tick(60)
    def update(self): 
        for i in range(0, len(self.vectors)): 
            self.vectors[i].calculate_direction_from_charges(self.charges) 
        for i in range(0, len(self.sensors)): 
            self.sensors[i].move(self.charges)

    def run(self): 
        while self.running: 
            self.handle_events()
            self.update()
            self.render()
        pygame.quit() 
        sys.exit()