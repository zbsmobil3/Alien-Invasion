import sys
import pygame

from settings import Settings
from ship import Ship


class AlienInvasion:
    """Class to manage overall game behavior"""
    def __init__(self):
        """Initilize the game and create game resources"""
        pygame.init()


        self.clock= pygame.time.Clock()
        self.settings=Settings()

        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")

        self.bg_clr=(230,230,230)

        self.ship=Ship(self)

    def run_game(self):
        """Houses main gameloop"""

        while True:
            self._check_events()

            self.ship.update()

            #Redraw the screen
            self._update_screen()

            #Make the most recently drawn screen visible
            pygame.display.flip()
            self.clock.tick(60)

    def _check_events(self):
        """Watch for keyboard and mouse inputs"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                     self.ship.moving_right = True
                elif event.key == pygame.K_LEFT:
                    self.ship.moving_left = True


            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    self.ship.moving_right = False
                elif event.key == pygame.K_LEFT:
                    self.ship.moving_left = False

    def _update_screen(self):
        """Update images on the screen, and flip to the new screen."""
        self.screen.fill(self.settings.bg_clr)
        self.ship.blitme()

if __name__ == '__main__':
    #make a game instance and run
    ai=AlienInvasion()
    ai.run_game()