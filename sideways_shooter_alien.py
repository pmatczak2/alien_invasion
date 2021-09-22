
import pygame
from pygame.sprite import Sprite

class Alien(Sprite):

    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.sideways_settings

        self.image = pygame.image.load('alien.bmp')
        self.image = pygame.transform.rotate(self.image, 270)
        self.rect = self.image.get_rect()

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.y = float(self.rect.y)


    def update(self):
        self.y -= self.settings.alien_speed
        self.rect.y = self.y
