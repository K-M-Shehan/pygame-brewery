import sys
import pygame

pygame.init() # starts up pygame

pygame.display.set_caption('da game')

screen = pygame.display.set_mode((640, 480)) # creates the window

clock = pygame.time.Clock() # to run the game in 60fps

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()
    clock.tick(60) # 60fps
