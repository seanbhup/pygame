import pygame
# import sys
from settings import Settings
from hero import Hero
from enemy import Enemy
from game_functions import Check_Events
from pygame.sprite import Group, groupcollide
from play_button import Play_Button
import os



pygame.init()
game_settings = Settings();
screen = pygame.display.set_mode(game_settings.screen_size)
pygame.display.set_caption("The Cave Troll Named Pateesa")
hero = Hero(screen,game_settings)

hero_group = Group()
hero = Hero(screen,game_settings)
hero_group.add(hero)

enemies = Group()
enemies.add(Enemy(screen,game_settings));

play_button = Play_Button(screen);


while 1:

    Check_Events(hero,play_button,game_settings)

    screen.fill(game_settings.bg_color)

    for hero in hero_group.sprites():
        hero.update_me()
        hero.draw_me()

    for enemy in enemies.sprites():
        if game_settings.game_active:
            enemy.update_me(hero)
        enemy.draw_me();

    hero_died = groupcollide(hero_group,enemies,False,True);
    if hero_died:
        print "The Cave Troll named Pateesa has defeated Frodo Baggins"
        os.system("say 'The Cave Troll named Pateesa has defeated Frodo Baggins'")
        game_settings.game_active = False

    if game_settings.game_active == False:
        play_button.draw_button();

    play_button.draw_button()

    pygame.display.flip()
