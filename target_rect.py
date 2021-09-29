import pygame.font

class Target:

    def __init__(self, tp_game, msg):
        self.screen = tp_game.screen
        self.screen_rect = self.screen.get_rect()

        self.width, self.height = 100, 100
        self.target_color = (0, 0, 255)
        self.font = pygame.font.SysFont(None, 48)

        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.topright = self.screen.get_rect

        self._prep_msg(msg)