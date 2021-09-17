import pygame

class LuigiCharacter:

    def __init__(self, luigi_game):
        self.screen = luigi_game.screen
        self.settings = luigi_game.luigi_settings
        self.screen_rect = luigi_game.screen.get_rect()

        self.image = pygame.image.load('luigi-6022005_640.bmp')
        self.image = pygame.transform.scale(self.image, (40, 40))
        self.rect = self.image.get_rect()

        self.rect.center = self.screen_rect.center
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False


    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.luigi_speed
        if self.moving_left and self.rect.left > self.screen_rect.left:
            self.x -= self.settings.luigi_speed
        if self.moving_up and self.rect.top > self.screen_rect.top:
            self.y -= self.settings.luigi_speed
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.settings.luigi_speed
        self.rect.x = self.x
        self.rect.y = self.y

    def blitme(self):
        self.screen.blit(self.image, self.rect)


