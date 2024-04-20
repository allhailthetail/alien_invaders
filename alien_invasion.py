import sys

import pygame

import pygame 

from settings import Settings

from ship import Ship

class AlienInvasion:
    '''Overall class to manage game assets and behavior.'''

    def __init__(self):
        '''Initialize the game, create game resources.'''
        
        pygame.init()

        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        self.clock = pygame.time.Clock()
        pygame.display.set_caption('Alien Invasion')

        # Set background color for the game:
        self.bg_color = (self.settings.bg_color)
        # Ship requires ai_game in order to initiate.
        # Here, we pass in self in order to provide this to Ship. 
        # In return, we get back an instance of ship, tied to the given object of AlienInvasion.
        self.ship = Ship(self)

    def _check_events(self):
        '''Respond to keypresses and mouse events'''
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

                elif event.type == pygame.KEYDOWN:
                    self._check_keydown_events(event)
                elif event.type == pygame.KEYUP:
                    self._check_keyup_events(event)

    def _check_keydown_events(self,event):
        '''Respond to keypresses'''
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()

    def _check_keyup_events(self,event):
        '''Respond to key releases'''
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False
    
    def _update_screen(self):
        '''Update images on the screen and flip to a new screen'''
        # Fill entire screen with background color:
        self.screen.fill(self.bg_color)
        # Allow the Ship to print to the screen
        self.ship.blitme()
        # Make the most recent screen visible:
        pygame.display.flip()

    def run_game(self):
        '''Start the main loop for the game.'''
        while True:
            self._check_events()
            self.ship.update()
            self._update_screen()            
            # pygame will do best-effort to keep the game's framerate at 60fps
            self.clock.tick(60)

if __name__ == '__main__':
    # Make alien invasion game instance and run:
    ai = AlienInvasion()
    ai.run_game()
