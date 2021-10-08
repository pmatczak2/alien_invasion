import sys
import pygame
from target_settings import Settings
from target_stats import GameStats
from target_button import Button
from target_practice_ship import Ship
from target_bullet import Bullet
from target_rect import Target

class TargetPractice:

    def __init__(self):
        pygame.init()
        self.settings = Settings()


        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Target Practice")

        self.stats = GameStats(self)
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.target = Target(self)


        self.play_button = Button(self, "Play")


    def run_game(self):
        while True:
            self._check_events()

            if self.stats.game_active:
                self._update_bullets()
                self.target.update()
                self.ship.update()
            self._update_screen()

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_event(event)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)

    def _check_keydown_events(self, event):
        if event.key == pygame.K_UP:
            self.ship.moving_up = True
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _check_keyup_event(self, event):
        if event.key == pygame.K_UP:
            self.ship.moving_up = False
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = False

    def _check_play_button(self, mouse_pos):
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)
        if button_clicked and not self.stats.game_active:
            self._start_game()
            self.settings.initialize_dynamic_settings()


    def _start_game(self):
        self.stats.reset_stats()
        self.stats.game_active = True

        self.bullets.empty()

        self.ship.center_ship()


    def _fire_bullet(self):
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _target_missed(self):
        self.stats.bullets_left -= 1

        self.target.remove()
        self.bullets.empty()


    def _update_bullets(self):
        self.bullets.update()


        for bullet in self.bullets.copy():
            if bullet.rect.left >= self.screen.get_rect().right:
                self.bullets.remove(bullet)
                self._increment_misses()

        self._check_bullet_target_collision()


    def _increment_misses(self):
        self.stats.num_misses += 1
        if self.stats.num_misses >= self.settings.miss_limit:
            self.stats.game_active = False

    def _check_bullet_target_collision(self):
        collisions = pygame.sprite.spritecollide(self.target, self.bullets, True)

        if collisions:
            self.stats.num_hits += 1
            if self.stats.num_hits % self.settings.levelup_hits == 0:
                self.settings.increase_speed()

    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.target.draw_target()


        if not self.stats.game_active:
            self.play_button.draw_button()

        pygame.display.flip()

if __name__ == "__main__":
    tp = TargetPractice()
    tp.run_game()
