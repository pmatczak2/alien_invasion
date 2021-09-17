import sys
from random import randint

import pygame
from star_settings import Settings
from star_image import Image

class Star:

    def __init__(self):
        pygame.init()

        self.settings = Settings()


        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Star")

        self.stars = pygame.sprite.Group()
        self._create_star()

    def run_game(self):
        while True:
            self._check_events()
            self._update_screen()

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

    def _create_star(self):
        star = Image(self)
        star_width, star_height = star.rect.size
        available_space_x = self.settings.screen_width - (2 * star_width)
        number_stars_x = available_space_x // (2 * star_width)


        available_space_y = (self.settings.screen_height - (star_height))
        number_rows = available_space_y // (2 * star_height)

        for row_number in range(number_rows):
            for star_number in range(number_stars_x):
                self._create_multiple_stars(star_number, row_number)


    def _create_multiple_stars(self, star_number, row_number):
        star = Image(self)
        star_width, star_height = star.rect.size
        star.x = star_width + 2 * star_width * star_number
        star.rect.x = star.x + randint(-5, 10)
        star.rect.y = star.rect.height + 2 * star.rect.height * row_number

        star.rect.x += randint(-12, 123)
        star.rect.y += randint(-4, 123)
        self.stars.add(star)


    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)
        self.stars.draw(self.screen)

        pygame.display.flip()

if __name__ == '__main__':
    star = Star()
    star.run_game()