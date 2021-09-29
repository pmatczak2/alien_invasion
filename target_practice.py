import sys
import pygame
from target_settings import Settings
from target_practice_ship import Ship

class TargetPractice:

    def __init__(self):
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Target Practice")

        self.ship = Ship(self)

    def run_game(self):
        while True:
            self._check_events()
            self._update_screen()
            self.ship.update()

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.ship.moving_up = True
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_UP:
                    self.ship.moving_up = False



    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)
        self.ship.biltime()

        pygame.display.flip()

if __name__ == "__main__":
    tp = TargetPractice()
    tp.run_game()
