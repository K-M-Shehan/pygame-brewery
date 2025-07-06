import sys
import pygame
from scripts.utils import load_image
from scripts.entities import PhysicsEntity

class Game:
    def __init__(self):
            
        pygame.init() # starts up pygame

        pygame.display.set_caption('da game')
        self.screen = pygame.display.set_mode((640, 480)) # creates the window
        self.display = pygame.Surface((320, 240)) # half of screen

        self.clock = pygame.time.Clock() # to run the game in 60fps

        self.movement = [False, False]

        self.assets = {
            'player' : load_image('entities/player.png')
        }

        self.player = PhysicsEntity(self, 'player', (50, 50), (8, 15))
    
    def run(self):
        # Game loop
        while True:
            self.display.fill((14, 219, 248)) # this is an rgb

            self.player.update((self.movement[1] - self.movement[0], 0))
            self.player.render(self.display)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        self.movement[0] = True
                    if event.key == pygame.K_RIGHT:
                        self.movement[1] = True

                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT:
                        self.movement[0] = False
                    if event.key == pygame.K_RIGHT:
                        self.movement[1] = False
            
            self.screen.blit(pygame.transform.scale(self.display, self.screen.get_size()), (0, 0))
            pygame.display.update()
            self.clock.tick(60) # 60fps

Game().run()
