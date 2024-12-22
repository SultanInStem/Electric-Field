import pygame 
from vector import Vector
class Canvas: 
    def __init__(self, width=800, height=800): 
        pygame.init()
        self.width = width 
        self.height = height 
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Vector Field Simulation")
        self.clock = pygame.time.Clock()
        self.running = True
        self.charges = []
    
    def handle_events(self): 
        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                self.running = False
    def render(self): 
        self.screen.fill((0,0,0))
        pygame.display.flip()
        self.clock.tick(60)
    def update(self): 
        pass

    def run(self): 
        while self.running: 
            self.handle_events()
            self.update()
            self.render()
        pygame.quit() 