import pygame

class Ship:

    def __init__(self, ss_game):
        self.screen = ss_game.screen
        self.settings = ss_game.settings
        self.screen_rect = ss_game.screen.get_rect()

        self.image = pygame.image.load('images.bmp')
        self.image = pygame.transform.rotate(self.image, 270)
        self.rect = self.image.get_rect()

        self.moving_up = False

    def update(self):
        if self.moving_up:
            self.rect.y -= 1

    def biltime(self):
        self.screen.blit(self.image, self.rect)