import pygame
from pygame.sprite import Sprite

class Image(Sprite):

    def __init__(self, star_game):
        super().__init__()
        self.screen = star_game.screen

        self.image = pygame.image.load('star.bmp')
        self.rect = self.image.get_rect()

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.x = float(self.rect.x)
