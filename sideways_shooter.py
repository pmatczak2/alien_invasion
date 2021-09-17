import sys
import pygame

from sideway_settings import Settings
from sideways_image import Image
from sideway_shooter_bullet import Bullet

class SidewaysShooter:

    def __init__(self):
        pygame.init()
        self.sideways_settings = Settings()

        self.screen = pygame.display.set_mode(
            (self.sideways_settings.screen_width, self.sideways_settings.screen_height))
        pygame.display.set_caption("Sideways Shooter")

        self.sideways_image = Image(self)
        self.bullets = pygame.sprite.Group()

    def run_game(self):
        while True:
            self._check_events()
            self.sideways_image.update()
            self._update_bullets()
            self._update_screen()




    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            elif event.type == pygame.KEYDOWN:
                self._check_keydown_event(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_event(event)

    def _check_keydown_event(self, event):
        if event.key == pygame.K_UP:
            self.sideways_image.moving_up = True
        elif event.key == pygame.K_DOWN:
            self.sideways_image.moving_down = True
        elif event.key == pygame.K_SPACE:
            self._fire_bullets()

    def _check_keyup_event(self, event):
        if event.key == pygame.K_UP:
            self.sideways_image.moving_up = False
        elif event.key == pygame.K_DOWN:
            self.sideways_image.moving_down = False

    def _fire_bullets(self):
        new_bullet = Bullet(self)
        self.bullets.add(new_bullet)

    def _update_screen(self):
        self.screen.fill(self.sideways_settings.bg_color)
        self.sideways_image.blitime()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()

    def _update_bullets(self):
        self.bullets.update()

        for bullet in self.bullets.copy():
            if bullet.rect.left >= self.screen.get_rect().right:
                self.bullets.remove(bullet)

        pygame.display.flip()



if __name__ == "__main__":
    ss = SidewaysShooter()
    ss.run_game()