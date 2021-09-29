import pygame.font

class Target:

    def __init__(self, tp_game, msg):
        self.screen = tp_game.screen
        self.screen_rect = self.screen.get_rect()

        self.width, self.height = 100, 35
        self.target_color = (0, 0, 255)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 38)

        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.topright = self.screen_rect.topright

        self._prep_msg(msg)

    def _prep_msg(self, msg):
        self.msg_image = self.font.render(msg, True, self.text_color,
                self.target_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_target(self):
        self.screen.fill(self.target_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)