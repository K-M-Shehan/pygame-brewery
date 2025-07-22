import pygame
from sys import exit

pygame.init()

screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption('yeah boi')
clock = pygame.time.Clock()
test_font = pygame.font.Font('data/font/Pixeltype.ttf', 50)
game_active = True

sky_surface = pygame.image.load('graphics/Sky.png').convert()
ground_surface = pygame.image.load('graphics/ground.png').convert()


snail_surface = pygame.image.load('graphics/snail/snail1.png').convert_alpha()
snail_rect = snail_surface.get_rect(midbottom = (600, 300))

player_surface = pygame.image.load(('graphics/Player/player_walk_1.png')).convert_alpha()
player_rectangle = player_surface.get_rect(midbottom = (80, 300))
player_gravity = 0

score_surf = test_font.render('Score: ', False, (64, 64, 64))
score_rect = score_surf.get_rect(center = (400, 50))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if game_active:
            if event.type == pygame.MOUSEBUTTONDOWN and player_rectangle.bottom >= 300:
                if player_rectangle.collidepoint(event.pos):
                    print('mouse collision')
                    player_gravity = -20

            if event.type == pygame.KEYDOWN and player_rectangle.bottom >= 300:
                if event.key == pygame.K_SPACE:
                    player_gravity = -20
        else:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                game_active = True
                snail_rect.left = 800


    # draw all elements 
    # update everything
    if game_active:
        screen.blit(sky_surface, (0, 0))
        screen.blit(ground_surface, (0, 300))
        snail_rect.right -= 4
        if snail_rect.right < 0:
            snail_rect.left = 800
        screen.blit(snail_surface, snail_rect)

        #player
        player_gravity += 1
        player_rectangle.bottom += player_gravity
        if player_rectangle.bottom >= 300:
            player_rectangle.bottom = 300
        screen.blit(player_surface, player_rectangle)

        # collsion
        if snail_rect.colliderect(player_rectangle):
            game_active = False

        pygame.draw.rect(screen, '#c0e8ec', score_rect)
        pygame.draw.rect(screen, '#c0e8ec', score_rect, 6)
        screen.blit(score_surf, score_rect)
    else:
        screen.fill('Blue')

    pygame.display.update()
    clock.tick(60)
