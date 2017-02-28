import pygame
import sys
from settings import Settings
from bullet import Bullet

def Check_Events(hero,bullets,play_button,game_settings,screen):
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
            elif event.key == pygame.K_w:
                new_bullet = Bullet(screen,hero,game_settings, "up", "vert")
                bullets.add(new_bullet);
            elif event.key == pygame.K_s:
                new_bullet = Bullet(screen,hero,game_settings, "down", "vert")
                bullets.add(new_bullet);
            elif event.key == pygame.K_a:
                new_bullet = Bullet(screen,hero,game_settings, "left", "hori")
                bullets.add(new_bullet);
            elif event.key == pygame.K_d:
                new_bullet = Bullet(screen,hero,game_settings, "right", "hori")
                bullets.add(new_bullet);
            elif event.key == pygame.K_f:
                hero.image = pygame.image.load("Pateesa2.png")
                

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
            elif event.key == pygame.K_f:
                hero.image = pygame.image.load("Pateesa2_hammer_up.png")

            # elif event.key == pygame.K_SPACE:
            #     bullet.shooting_left = False
