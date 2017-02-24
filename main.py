import pygame
import sys
from settings import Settings
from hero import Hero



pygame.init()
game_settings = Settings();
screen = pygame.display.set_mode(game_settings.screen_size)
pygame.display.set_caption("The Cave Troll Named Pateesa")
hero = Hero(screen,game_settings)




while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            # print event.key
            if event.key == pygame.K_RIGHT:
                hero.moving_right = True
            elif event.key == pygame.K_LEFT:
                hero.moving_left = True
            elif event.key == pygame.K_UP:
                hero.moving_up = True
            elif event.key == pygame.K_DOWN:
                hero.moving_down = True
        elif event.type == pygame.KEYUP:
            # print event.key
            if event.key == pygame.K_RIGHT:
                hero.moving_right = False
            elif event.key == pygame.K_LEFT:
                hero.moving_left = False
            elif event.key == pygame.K_UP:
                hero.moving_up = False
            elif event.key == pygame.K_DOWN:
                hero.moving_down = False
    screen.fill(game_settings.bg_color)
    hero.update_me(game_settings)
    hero.draw_me()
    pygame.display.flip()
