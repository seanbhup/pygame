import pygame
# import sys
from settings import Settings, Background
from hero import Hero
from enemy import Enemy
from bullet import Bullet
from game_functions import Check_Events
from pygame.sprite import Group, groupcollide
from play_button import Play_Button
import os
import time
import timeit



pygame.init()
game_settings = Settings();
screen = pygame.display.set_mode(game_settings.screen_size)
pygame.display.set_caption("The Cave Troll Named Pateesa")
hero = Hero(screen,game_settings)

heroes = Group()
hero = Hero(screen,game_settings)
heroes.add(hero)

enemies = Group()
enemies.add(Enemy(screen,game_settings));

bullets = Group()
# bullet = Bullet(screen,hero,game_settings)
# bullets.add(Bullet(screen,hero,game_settings))
# bullets.add(bullet)



play_button = Play_Button(screen);

game_start_time = time.time();

bg_image = Background("Cave.jpg", [0,0])


tick = 0;
while -94508395823059823905812040918:
    tick += 1;
    Check_Events(hero,bullets,play_button,game_settings,screen)


    screen.blit(bg_image.image, bg_image.rect)
    





    # screen.fill(game_settings.bg_color)

    game_settings.timer = (time.time() - game_start_time);
    print
    if tick % 60 == 0:
        enemies.add(Enemy(screen,game_settings))




    for hero in heroes.sprites():
        if game_settings.game_active:
            hero.update_me()
        hero.draw_me()

    for enemy in enemies.sprites():
        if game_settings.game_active:
            enemy.update_me(hero)
        enemy.draw_me();

    for bullet in bullets.sprites():
        bullet.update_me();
        bullet.draw_bullet();


    # for event in pygame.event.get():
    #     if event.type == pygame.KEYDOWN:
    #         if event.key == pygame.K_f:
    enemy_died = groupcollide(heroes,enemies,False,True);
    #             if enemy_died:
    #                 print "The Cave Troll named Pateesa has defeated Frodo Baggins"
                # os.system("say 'The Cave Troll named Pateesa has defeated Frodo Baggins'")
                # game_settings.game_active = False


    if game_settings.game_active == False:
        play_button.draw_button();




    pygame.display.flip()
