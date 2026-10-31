

class Settings:
    """A class to store all settings for the game alien invasion. Duh"""

    def __init__(self):
        """Initialize the game's static settings."""

        #screen settings:
        self.screen_width=1200
        self.screen_height=800
        self.bg_clr=(230,230,230)


        #ship settings
        self.ship_limit = 3


        #bullet settings
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3

        #alien settings
        self.fleet_drop_speed = 9 #it'd probably make sense to make this dynamic in the future

        #how quickly the game speeds up
        self.speedup_scale = 1.1

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Initialize settings that change throughout the game."""
        self.ship_speed = 5 #it was too slow
        self.bullet_speed = 7 #it was too slow
        self.alien_speed = 0.8

        self.fleet_direction = 1 #fleet_direction of 1 represents right; -1 represents left.

        #scoring settings
        self.alien_points = 50

    def increase_speed(self):
        """Increase speed settings."""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale