import pygame
from sys import exit

pygame.init()

screen = pygame. display.set_mode((960, 480))
pygame.display.set_caption('Pong by supremestrawhat')
clock = pygame.time.Clock()

# game
left_pong_pos = pygame.Vector2(80, 50) 
box_rect = pygame.Rect(20, 20, 920, 440)
pong_rect = pygame.Rect(left_pong_pos, (15, 60))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        left_pong_pos.y -= 5
    if keys[pygame.K_s]:
        left_pong_pos.y += 5
       
    pong_rect.topleft = (int(left_pong_pos.x), int(left_pong_pos.y))
    # render shit
    screen.fill('black')
    pygame.draw.rect(screen, 'white', box_rect, 4) # the border box
    pygame.draw.rect(screen, 'white', pong_rect)
        # the pong, which can only move up and down
        # the ball spawns from mid and moves to right first


        

    pygame.display.update()
    clock.tick(60)
