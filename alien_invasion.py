import sys

import pygame

import pygame 

from settings import Settings

class AlienInvasion:
    '''Overall class to manage game assets and behavior.'''

    def __init__(self):
        '''Initialize the game, create game resources.'''
        
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((self.settings.screen_width,self.settings.screen_height))
        self.clock = pygame.time.Clock()
        pygame.display.set_caption('Alien Invasion')

        # Set background color for the game:
        self.bg_color = (self.settings.bg_color)

    def run_game(self):
        '''Start the main loop for the game.'''
        
        while True:
            # Watch for keyboard and mouse events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            
            # Fill entire screen with background color:
            self.screen.fill(self.bg_color)

            # Make the most recent screen visible:
            pygame.display.flip()
            # pygame will do best-effort to keep the game's framerate at 60fps
            self.clock.tick(60)

if __name__ == '__main__':
    # Make alien invasion game instance and run:
    ai = AlienInvasion()
    ai.run_game()
