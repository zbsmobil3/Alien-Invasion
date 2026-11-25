import pygame
from pygame.sprite import Sprite
import math

class Alien(Sprite):
    """A class to represent a single alien in the fleet."""

    def __init__(self, ai_game, type, hits=0):
        """Initialize the alien and set its starting position."""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        self.type=type
        self.hits=hits

        #load the alien image and set its rect attribute.
        if self.type==3:
            self.image = pygame.image.load('Assets/images/Enemy3.png')
        elif self.type==2:
            self.image = pygame.image.load('Assets/images/Enemy2.png')
        else:
            self.image = pygame.image.load('Assets/images/Enemy4.png')
        self.image=pygame.transform.scale(self.image, (35, 35))
        self.rect = self.image.get_rect()

        #start each new alien near the top left of the screen.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        self.y = self.rect.y
        self.bob=0

        #store the alien's exact horizontal position.
        self.x = float(self.rect.x)

    def check_edges(self):
        """Return True if alien is at edge of screen."""
        screen_rect = self.screen.get_rect()
        return (self.rect.right >= screen_rect.right) or (self.rect.left <= 0)

    def update(self):
        """Move the alien right or left."""
        self.x += self.settings.alien_speed * self.settings.fleet_direction
        self.rect.x = self.x
        self.t = pygame.time.get_ticks() / 1000.0
        self.bob= 8*math.sin(self.t*2)
        self.rect.y= self.y+self.bob