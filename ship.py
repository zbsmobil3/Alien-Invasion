import pygame

class Ship:
    """a class to manage the ship"""

    def __init__(self, ai_game):
        """Initilize the ship and its starting position"""

        self.screen= ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect=ai_game.screen.get_rect()

        #Load the ship image and get its rect
        self.image=pygame.image.load('Assets/images/ship.png')
        self.rect=self.image.get_rect()

        #start each new ship at the bottom of the screen
        self.rect.midbottom=self.screen_rect.midbottom

        #store a float for the ship's exact horizontal position.
        self.x = float(self.rect.x)

        #movement flag; start with a ship that's not moving.
        self.moving_right = False
        self.moving_left = False

        #ship settings
        self.ship_speed = 1.5

    def update(self):
        """Update the ship's position based on the movement flag."""
        if self.moving_right:
            self.rect.x += 1
        if self.moving_left:
            self.rect.x -= 1

    def blitme(self):
        """Draw the ship at its current location"""
        self.screen.blit(self.image, self.rect)