import sys
import pygame
from settings import Settings 

class AlienInvasion:
    """Class to manage game assests and behavior."""
    def __init__(self):
        """Initialize the game, and create game resources."""
        pygame.init()
        #set attribute settings to the imported Settings class from the
        #settings.py module
        self.settings = Settings()

        self.screen = pygame.display.set_mode((self.settings.screen_width,
        self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion!")


    def run_game(self):
        """Start loop for game"""
        while True:
            #watch for keyboard and mouse events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            #redraw the screen during each pass through the loop
            self.screen.fill(self.settings.bg_color)
            #make most recently drawn screen visible
            pygame.display.flip()

if __name__ == '__main__':
    #make a game instance, and run the game
    ai = AlienInvasion()
    ai.run_game()
