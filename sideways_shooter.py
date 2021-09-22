import sys
import pygame

from sideway_settings import Settings
from sideways_image import Image
from sideway_shooter_bullet import Bullet
from sideways_shooter_alien import Alien

class SidewaysShooter:

    def __init__(self):
        pygame.init()
        self.sideways_settings = Settings()

        self.screen = pygame.display.set_mode(
            (self.sideways_settings.screen_width, self.sideways_settings.screen_height))
        pygame.display.set_caption("Sideways Shooter")

        self.sideways_image = Image(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()

        self._create_fleet()

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

    def _create_fleet(self):
        alien = Alien(self)
        alien_height, alien_width = alien.rect.size
        available_space_y = self.sideways_settings.screen_height - alien_height
        number_aliens_y = available_space_y // (2 * alien_height)

        ship_width = self.sideways_image.rect.width
        available_space_x = (self.sideways_settings.screen_width -
                             (2 * alien_height) - ship_width)
        number_rows = available_space_x // (2 * alien_width)

        for row_number in range(number_rows):
            for alien_number in range(number_aliens_y):
                self._create_alien(alien_number, row_number)

    def _create_alien(self, alien_number, row_number):
            alien = Alien(self)
            alien_height, alien_height = alien.rect.size
            alien.y = self.sideways_settings.screen_height - 2 * alien_height * alien_number
            alien.rect.y = alien.y
            alien.rect.x = self.sideways_settings.screen_width - 2 * alien.rect.width * row_number
            self.aliens.add(alien)

    def _update_screen(self):
        self.screen.fill(self.sideways_settings.bg_color)
        self.sideways_image.blitime()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.aliens.draw(self.screen)

    def _update_bullets(self):
        self.bullets.update()

        for bullet in self.bullets.copy():
            if bullet.rect.left >= self.screen.get_rect().right:
                self.bullets.remove(bullet)

        pygame.display.flip()



if __name__ == "__main__":
    ss = SidewaysShooter()
    ss.run_game()