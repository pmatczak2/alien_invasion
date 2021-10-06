class GameStats:

    def __init__(self, tp_game):
        self.settings = tp_game.settings

        self.game_active = False
        self.num_misses = 0
