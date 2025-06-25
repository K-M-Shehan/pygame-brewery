import sys
import pygame
class Game:
    def __init__(self):
            
        pygame.init() # starts up pygame

        pygame.display.set_caption('da game')
        self.screen = pygame.display.set_mode((640, 480)) # creates the window

        self.clock = pygame.time.Clock() # to run the game in 60fps

        self.img = pygame.image.load('data/images/clouds/cloud_1.png')
        self.img.set_colorkey((0, 0, 0)) # this specific color will be transparent
        self.img_pos = [160, 260]
        self.movement = [False, False] # first one is up key and 2nd down key

        self.collision_area = pygame.Rect(50, 50, 300, 50)
    
    def run(self):
        # Game loop
        while True:
            self.screen.fill((14, 219, 248)) # this is an rgb

            # collision detection
            img_r = pygame.Rect(self.img_pos[0], self.img_pos[1], self.img.get_width(), self.img.get_height())
            if img_r.colliderect(self.collision_area):
                pygame.draw.rect(self.screen, (0, 100, 255), self.collision_area)
            else:
                pygame.draw.rect(self.screen, (0, 50, 155), self.collision_area)

            self.img_pos[1] += (self.movement[1] - self.movement[0]) * 5
            self.screen.blit(self.img, self.img_pos) # the 2nd arg is the position, top left is 0, 0

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        self.movement[0] = True
                    if event.key == pygame.K_DOWN:
                        self.movement[1] = True

                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_UP:
                        self.movement[0] = False
                    if event.key == pygame.K_DOWN:
                        self.movement[1] = False

            pygame.display.update()
            self.clock.tick(60) # 60fps

Game().run()
