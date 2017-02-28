import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    def __init__(self,screen,hero,game_settings,direction,bullet_type):
        super(Bullet,self).__init__();

        self.screen = screen
        if bullet_type == "vert":
            self.rect = pygame.Rect(0,0,game_settings.bullet_height,game_settings.bullet_width);
        if bullet_type == "hori":
            self.rect = pygame.Rect(0,0,game_settings.bullet_width,game_settings.bullet_height);
        # self.rect = pygame.Rect(0,0,game_settings.bullet_width,game_settings.bullet_height)
        self.rect.centerx = hero.rect.centerx
        self.rect.centery = hero.rect.centery
        # self.rect.left = hero.rect.left
        self.color = game_settings.bullet_color
        self.speed = game_settings.bullet_speed
        self.x = self.rect.x
        self.y = self.rect.y
        self.shooting_right = False
        self.shooting_left = False
        self.shooting_up = False
        self.shooting_down = False
        self.direction = direction;
    def update_me(self):
        # self.x -= self.speed
        # self.rect.x = self.x
        # if self.shooting_right:
        #     self.rect.centerx += 10 * self.speed
        # if self.shooting_left:
        #     self.rect.centerx -= 10 * self.speed
        # if self.shooting_up:
        #     self.rect.centery -= 10 * self.speed
        # if self.shooting_down:
        #     self.rect.centery += 10 * self.speed
        if self.direction == "up":
            self.y -= self.speed;
        elif self.direction == "down":
            self.y += self.speed;
        elif self.direction == "right":
            self.x += self.speed;
        elif self.direction == "left":
            self.x -= self.speed;
        self.rect.y = self.y;
        self.rect.x = self.x;
    def draw_bullet(self):
        pygame.draw.rect(self.screen,self.color,self.rect)
