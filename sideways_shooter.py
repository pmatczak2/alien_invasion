import sys
from time import sleep

import pygame

from random import randint
from sideway_settings import Settings
from sideway_game_satas import GameStats
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

        self.stats = GameStats(self)

        self.sideways_image = Image(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()

        self._create_fleet()

    def run_game(self):
        while True:
            self._check_events()
            self.sideways_image.update()
            self._update_bullets()
            self._update_aliens()
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

    def _update_bullets(self):
        self.bullets.update()

        for bullet in self.bullets.copy():
            if bullet.rect.left >= self.screen.get_rect().right:
                self.bullets.remove(bullet)

        self._check_bullet_alien_collisions()

    def _check_bullet_alien_collisions(self):
        collision = pygame.sprite.groupcollide( self.bullets, self.aliens, True, True)


    def _create_fleet(self):
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        ship_height = self.sideways_image.rect.height

        available_space_y = self.sideways_settings.screen_height - 2 * alien_height
        number_rows = available_space_y // (2 * alien_width)

        available_space_x = (self.sideways_settings.screen_width - (alien_width)
                             - ship_height)
        number_aliens_y = available_space_x // (2 * alien_width)


        for row_number in range(number_rows):
            for alien_number in range(number_aliens_y):
                self._create_alien(alien_number, row_number)

    def _create_alien(self, alien_number, row_number):
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size

        alien.x = 3 * alien_width + 2 * alien_width * alien_number + randint(-23, 12)
        alien.rect.x = alien.x

        alien.y = alien.rect.height + 2 * alien.rect.height * row_number + randint(-12, 54)
        alien.rect.y = alien.y
        self.aliens.add(alien)

    def _ship_hit(self):
        self.stats.ships_left -= 1

        self.aliens.empty()
        self.bullets.empty()

        self._create_fleet()
        self.sideways_image.center_ship()

        sleep(0.5)


    def _check_fleet_edges(self):
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break

    def _change_fleet_direction(self):
        for alien in self.aliens.sprites():
            alien.rect.x -= self.sideways_settings.fleet_left_drop_speed
        self.sideways_settings.fleet_direction *= -1

    def _check_aliens_left(self):
        screen_rect = self.screen.get_rect()
        for alien in self.aliens.sprites():
            if alien.rect.x >= screen_rect.left:
                self._ship_hit()
                break

    def _update_aliens(self):
        self._check_fleet_edges()
        self.aliens.update()

        if pygame.sprite.spritecollideany(self.sideways_image, self.aliens):
            self._ship_hit()



    def _update_screen(self):
        self.screen.fill(self.sideways_settings.bg_color)
        self.sideways_image.blitime()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.aliens.draw(self.screen)

        pygame.display.flip()



if __name__ == "__main__":
    ss = SidewaysShooter()
    ss.run_game()