import pygame
from pygame.sprite import Sprite

class Ship(Sprite):
    """a class to manage the ship"""

    def __init__(self, ai_game):
        """Initilize the ship and its starting position"""
        super().__init__()
        self.screen= ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect=ai_game.screen.get_rect()
        self.velo=0

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

    def update(self):
        """Update the ship's position based on the movement flag."""
        if (self.moving_right and self.rect.right < self.screen_rect.right) and (not(self.moving_left and self.rect.left)):
            if self.velo<-1:
                self.velo*= 0.8 #SOFT SWITCH
            else:
                self.velo+= self.settings.ship_speed
            #self.x += self.settings.ship_speed
        elif self.moving_left and self.rect.left > 0:
            if self.velo>1:
                self.velo*= 0.8
            else:
                self.velo-= self.settings.ship_speed
            #self.x -= self.settings.ship_speed
        else:
            self.velo*=0.9 #FRICTION

         #update rect object from self.x.
        self.rect.x += self.velo
        self.x=self.rect.x
        #self.rect.x = self.x  

        screen_rect = self.screen.get_rect()
        if (self.rect.right >= screen_rect.right) or (self.rect.left <= 0):
            while (self.rect.right >= screen_rect.right) or (self.rect.left <= 0):
                self.rect.x+= -1*(self.velo/(abs(self.velo)))
                self.x=self.rect.x
            self.velo=0

    def blitme(self):
        """Draw the ship at its current location"""
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        """Center the ship on the screen."""
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)