import pygame
from sys import exit

pygame.init()

screen = pygame. display.set_mode((960, 480))
pygame.display.set_caption('Pong by supremestrawhat')
clock = pygame.time.Clock()
main_font = pygame.font.Font('data/font/Pixeltype.ttf', 100)
sub_font = pygame.font.Font('data/font/Pixeltype.ttf', 50)
game_state = 'menu'

# titles
title_surf = main_font.render('PONG', False, (255, 255, 255))
title_rect = title_surf.get_rect(center = (480, 180))

subt_surf = sub_font.render('press SPACE BAR to start', False, (255, 255, 255))
subt_rect = subt_surf.get_rect(center = (480, 220))

# game
box_rect = pygame.Rect(20, 20, 920, 440)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if game_state == 'menu' and (event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE):
            game_state = 'play'



    # render shit
    if game_state == 'menu':
        screen.blit(title_surf, title_rect)
        screen.blit(subt_surf, subt_rect)

    elif game_state == 'play':
        pygame.draw.rect(screen, 'black', box_rect)
        pygame.draw.rect(screen, 'white', box_rect, 4)

        

    pygame.display.update()
    clock.tick(60)
