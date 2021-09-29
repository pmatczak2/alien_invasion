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

    def _prep_msg(self, msg):
        self.msg_image = self.font.render(msg, True, self.text_color,
                self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.topright = self.rect.topright

    def draw_target(self):
        self.screen.fill(self.target_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)