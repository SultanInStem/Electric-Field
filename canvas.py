import pygame 
from vector import Vector
import globals
class Canvas: 
    def __init__(self): 
        pygame.init()
        self.vector = Vector(0,0,100,100)
        self.vector.normalize()
        self.vector.scale(50)
        self.screen = pygame.display.set_mode((globals.SCREEN_WIDTH, globals.SCREEN_HEIGHT))
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

        self.vector.draw(self.screen, (255,255,255))


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