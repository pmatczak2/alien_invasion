import pygame
from pygame.sprite import Sprite

class Target(Sprite):

    def __init__(self, tp_game):
        super().__init__()
        self.screen = tp_game.screen
        self.settings = tp_game.settings
        self.color = self.settings.target_color
        self.screen_rect = tp_game.screen.get_rect()

        self.rect = pygame.Rect(0, 0, self.settings.target_width,
                self.settings.target_height)
        self.rect.topright = self.screen_rect.topright

        self.y = float(self.rect.y)

        self.direction = 1

    def update(self):
        self.y += self.direction * self.settings.target_speed

        if self.rect.top <= self.screen_rect.top:
            self.rect.top = self.screen_rect.top
            self.direction = 1

        elif self.rect.bottom >= self.screen_rect.bottom:
            self.rect.bottom = self.screen_rect.bottom
            self.direction = -1

        self.rect.y = self.y

    def draw_target(self):
        pygame.draw.rect(self.screen, self.color, self.rect)
