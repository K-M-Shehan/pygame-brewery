import pygame
from sys import exit

pygame.init()

screen = pygame. display.set_mode((960, 480))
pygame.display.set_caption('Pong by supremestrawhat')
clock = pygame.time.Clock()

# game
left_pong_pos = pygame.Vector2(80, 50) 
right_pong_pos = pygame.Vector2(880, 50) 
ball_pos = pygame.Vector2(480, 240)

box_up_pos = pygame.Vector2(20, 20)
box_down_pos = pygame.Vector2(20, 456)
box_right_pos = pygame.Vector2(936, 20)

ball_velocity = pygame.Vector2(8, -2)

#box_rect = pygame.Rect(20, 20, 920, 440)

box_up_rect = pygame.Rect(box_up_pos, (920, 4))
box_down_rect = pygame.Rect(box_down_pos, (920, 4))
box_left_rect = pygame.Rect(box_up_pos, (4, 440))
box_right_rect = pygame.Rect(box_right_pos, (4, 440))

left_pong_rect = pygame.Rect(left_pong_pos, (15, 60))
right_pong_rect = pygame.Rect(right_pong_pos, (15, 60))

ball_rect = pygame.Rect(ball_pos, (10, 10))

start_flag= False;

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
    if keys[pygame.K_a]:
        left_pong_pos.x -= 5
    if keys[pygame.K_d]:
        left_pong_pos.x += 5

    if keys[pygame.K_UP]:
        right_pong_pos.y -= 5
    if keys[pygame.K_DOWN]:
        right_pong_pos.y += 5
    if keys[pygame.K_LEFT]:
        right_pong_pos.x -= 5
    if keys[pygame.K_RIGHT]:
        right_pong_pos.x += 5
    if keys[pygame.K_SPACE]:
        start_flag = True

    ## ball movement
    if start_flag == True:
        ball_pos += ball_velocity
    
    #if ball_rect.top <= box_rect.top:
    #    ball_velocity.y *= -1
    #    ball_rect.top = box_rect.top
    #    ball_pos.y = ball_rect.top
    
    #if ball_rect.bottom >= box_rect.bottom:
    #    ball_velocity.y *= -1
    #    ball_rect.bottom = box_rect.bottom
    #    ball_pos.y = ball_rect.top

    if ball_rect.colliderect(box_up_rect):
        ball_velocity.y *= -1
        ball_rect.top = box_up_rect.bottom
        ball_pos.y = ball_rect.top

    if ball_rect.colliderect(box_down_rect):
        ball_velocity.y *= -1
        ball_rect.bottom = box_down_rect.top
        ball_pos.y = ball_rect.top

    if ball_rect.colliderect(box_right_rect):
        ball_velocity.x *= -1
        ball_rect.right = box_right_rect.left
        ball_pos.x = ball_rect.left

    if ball_rect.colliderect(box_left_rect):
        ball_velocity.x *= -1
        ball_rect.left = box_left_rect.right
        ball_pos.x = ball_rect.left

    if ball_rect.colliderect(left_pong_rect) and ball_velocity.x < 0:
        ball_velocity.x *= -1
        ball_rect.left = left_pong_rect.right
        ball_pos.x = ball_rect.left

    if ball_rect.colliderect(right_pong_rect) and ball_velocity.x > 0:
        ball_velocity.x *= -1
        ball_rect.right = right_pong_rect.left
        ball_pos.x = ball_rect.left

    # update position
    left_pong_rect.topleft = (int(left_pong_pos.x), int(left_pong_pos.y))
    right_pong_rect.topleft = (int(right_pong_pos.x), int(right_pong_pos.y))
    ball_rect.topleft = (int(ball_pos.x), int(ball_pos.y))

    # render shit
    screen.fill('black')
    #pygame.draw.rect(screen, 'white', box_rect, 4) # the border box

    pygame.draw.rect(screen, 'white', box_up_rect)
    pygame.draw.rect(screen, 'white', box_right_rect)
    pygame.draw.rect(screen, 'white', box_down_rect)
    pygame.draw.rect(screen, 'white', box_left_rect)

    pygame.draw.rect(screen, 'white', left_pong_rect)
    pygame.draw.rect(screen, 'white', right_pong_rect)
    pygame.draw.circle(screen, 'white', ball_pos, 10)
        # the pong, which can only move up and down
        # the ball spawns from mid and moves to right first


        

    pygame.display.update()
    clock.tick(60)
