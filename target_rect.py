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

    def update(self):
        self.y += (self.settings.target_speed * self.settings.fleet_direction)
        self.rect.y = self.y

    def draw_target(self):
        pygame.draw.rect(self.screen, self.color, self.rect)
