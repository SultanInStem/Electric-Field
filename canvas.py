import pygame 
from vector import Vector
import globals
from charge import Charge
class Canvas: 
    def __init__(self): 
        pygame.init()
        self.screen = pygame.display.set_mode((globals.SCREEN_WIDTH, globals.SCREEN_HEIGHT))
        pygame.display.set_caption("Vector Field Simulation")
        self.clock = pygame.time.Clock()
        self.running = True
        self.charges = [Charge(0,0,1), Charge(0,100,-1), Charge(-200,0,1)]
        self.vectors = []


        for i in range(-20, 20): 
            for j in range(-20, 20): 
                v = Vector(i*50,j*50, 0,0)
                v.normalize()
                v.scale(30)
                self.vectors.append(v)
    
    def handle_events(self): 
        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                self.running = False
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