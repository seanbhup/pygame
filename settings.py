import pygame


class Settings():
    def __init__(self):
        self.screen_size = (1800,900)
        self.bg_color = (20, 79, 149)
        self.bg_image = ""
        self.hero_speed = 2
        self.bullet_width = 20
        self.bullet_height = 5
        self.bullet_color = (255,255,255)
        self.bullet_speed = 15
        self.game_active = False;
        self.timer = 0;


class Background(pygame.sprite.Sprite):
    def __init__(self, image_file, location):
        pygame.sprite.Sprite.__init__(self)  #call Sprite initializer
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location
