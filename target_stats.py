class GameStats():

    def __init__(self, tp_game):
        self.settings = tp_game.settings
        self.reset_game()

    def reset_game(self):
        self.ships_left = self.settings.ships_limit