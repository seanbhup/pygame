import pygame
import sys
from settings import Settings


def Check_Events(hero,play_button,game_settings):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            # print mouse_x,mouse_y
            if play_button.rect.collidepoint(mouse_x,mouse_y):
                game_settings.game_active = True
                bg_music = pygame.mixer.Sound('THE_LORD_OF_THE_RING_-_URUK_HAI_THEME.wav')
                bg_music.play();


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
