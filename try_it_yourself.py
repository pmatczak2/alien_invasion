import sys
import pygame

from luigi_settings import LuigiSettings
from luigi_character import LuigiCharacter

class Luigi:

    def __init__(self):
        pygame.init()
        self.luigi_settings = LuigiSettings()

        self.screen = pygame.display.set_mode(
            (self.luigi_settings.screen_width, self.luigi_settings.screen_height))
        pygame.display.set_caption("Luigi")

        self.luigi_character = LuigiCharacter(self)


    def run_game(self):
        while True:
            self._check_event()
            self.luigi_character.update()
            self.update_screen()


    def _check_event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)


    def _check_keydown_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.luigi_character.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.luigi_character.moving_left = True
        elif event.key == pygame.K_UP:
            self.luigi_character.moving_up = True
        elif event.key == pygame.K_DOWN:
            self.luigi_character.moving_down = True
        elif event.key == pygame.K_q:
            sys.exit()


    def _check_keyup_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.luigi_character.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.luigi_character.moving_left = False
        if event.key == pygame.K_UP:
            self.luigi_character.moving_up = False
        elif event.key == pygame.K_DOWN:
            self.luigi_character.moving_down = False

    def update_screen(self):
        self.screen.fill(self.luigi_settings.bg_color)
        self.luigi_character.blitme()

        pygame.display.flip()


if __name__ == '__main__':
    luigi = Luigi()
    luigi.run_game()