class GameStats:

    def __init__(self, tp_game):
        self.settings = tp_game.settings
        self.reset_stats()

    def reset_stats(self):
        self.bullets_left = self.settings.miss_limit

        self.game_active = False
        self.num_misses = 0
