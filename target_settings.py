class Settings:

    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        self.ship_speed = 1.5

        self.bullet_speed = 3.0
        self.bullet_width = 15
        self.bullet_height = 3
        self.bullet_color = (60, 60, 60)

        self.target_speed = .5
        self.target_width = 100
        self.target_height = 400
        self.target_color = (0, 0, 255)
        self.target_direction = 1

        self.bullets_allowed = 3
        self.miss_limit = 3

        self. speedup_scale = 2.1
        self.levelup_hits = 3

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        self.ship_speed = 1.5
        self.bullet_speed = 3.0
        self.target_speed = 1.0

    def increase_speed(self):
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.target_speed *= self.speedup_scale


