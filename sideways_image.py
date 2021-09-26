import pygame

class Image:

    def __init__(self, ss_game):
        self.screen = ss_game.screen
        self.settings = ss_game.sideways_settings
        self.screen_rect = ss_game.screen.get_rect()

        self.image = pygame.image.load('images.bmp')
        self.image = pygame.transform.rotate(self.image, 270)
        self.rect = self.image.get_rect()
        self.rect.midleft = self.screen_rect.midleft
        self.y = float(self.rect.y)
        self.moving_up = False
        self.moving_down = False


    def update(self):
        if self.moving_up and self.rect.top > self.screen_rect.top:
            self.y -= self.settings.image_speed
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.settings.image_speed
        self.rect.y = self.y


    def center_ship(self):
        self.rect.midleft = self.screen_rect.midleft
        self.y = float(self.rect.y)

    def blitime(self):
        self.screen.blit(self.image, self.rect)

