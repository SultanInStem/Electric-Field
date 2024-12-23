import pygame 
import sys
from vector import Vector
import globals
from globals import distance
from charge import Charge
class Canvas: 
    def __init__(self): 
        pygame.init()
        self.screen = pygame.display.set_mode((globals.SCREEN_WIDTH, globals.SCREEN_HEIGHT))
        pygame.display.set_caption("Vector Field Simulation")
        self.clock = pygame.time.Clock()
        self.running = True
        self.charges = [Charge(0,-200,1), Charge(0,200,-1)]
        self.vectors = []
        self.dragging = False


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
            elif event.type == pygame.MOUSEBUTTONUP: 
                self.dragging = False 
            elif event.type == pygame.MOUSEMOTION and self.dragging:
                self.charges[0].set_position(event.pos)

    def render(self): 
        self.screen.fill((0,0,0))

        for v in self.vectors: 
            v.draw(self.screen)

        for q in self.charges: 
            q.draw(self.screen)

        pygame.display.flip()
        self.clock.tick(60)
    def update(self): 
        for i in range(0, len(self.vectors)): 
            self.vectors[i].calculate_direction_from_charges(self.charges)

    def run(self): 
        while self.running: 
            self.handle_events()
            self.update()
            self.render()
        pygame.quit() 
        sys.exit()