import sys
import pygame

class Keys:

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("Keys Trial")



    def run_game(self):
        while True:
            self._check_events_()


    def _check_events_(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_event(event)



    def _check_keydown_event(self, event):
        print(event.key)
        if event.key == pygame.K_q:
            sys.exit()

        pygame.display.flip()
if __name__ == "__main__":
    keys = Keys()
    keys.run_game()