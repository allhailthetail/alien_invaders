import sys

import pygame

import pygame 

from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien

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
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()

        # Create fleet of aliens at start of the game
        self._create_fleet()
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
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()
        elif event.key == pygame.K_q:
            sys.exit()
    
    def _fire_bullet(self):
        '''Create a new bullet and add to group'''
        new_bullet = Bullet(self)

        # Limit number of bullets fired for a challenge:
        if len(self.bullets) < self.settings.bullets_allowed:
            self.bullets.add(new_bullet)

    def _check_keyup_events(self,event):
        '''Respond to key releases'''
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False
    
    def _create_alien(self, x_position, y_position):
        '''Creates an alien and places it on the row'''
        new_alien = Alien(self)
        new_alien.x = x_position
        new_alien.rect.x, new_alien.rect.y = x_position, y_position
        self.aliens.add(new_alien)

    def _create_fleet(self):
        '''Creates a fleet of aliens on the screen'''
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size

        current_x, current_y = alien_width, alien_height
        while current_y < (self.settings.screen_height - 3 * alien_height):
            while current_x < (self.settings.screen_width - 2 * alien_width):
                self._create_alien(current_x, current_y)
                current_x += 2 * alien_width
            current_x = alien_width
            current_y += 2 * alien_height

    def _update_screen(self):
        '''Update images on the screen and flip to a new screen'''
        # Fill entire screen with background color:
        self.screen.fill(self.bg_color)
        # Update bullets:
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        # Allow the Ship to print to the screen
        self.ship.blitme()
        # Allow the Aliens to print to the screen:
        self.aliens.draw(self.screen)
        # Make the most recent screen visible:
        pygame.display.flip()

    def _update_bullets(self):
        '''Update bullets helper method'''
        self.bullets.update()
        # Get rid of bullets that have left the screen:
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
            print(len(self.bullets)) 
    
    def _update_aliens(self):
        '''Update the positions of all aliens in the fleet'''
        self.aliens.update()

    def run_game(self):
        '''Start the main loop for the game.'''
        while True:
            self._check_events()
            self.ship.update()
            self._update_bullets()
            self._update_aliens()
            self._update_screen()            
            # pygame will do best-effort to keep the game's framerate at 60fps
            self.clock.tick(60)

if __name__ == '__main__':
    # Make alien invasion game instance and run:
    ai = AlienInvasion()
    ai.run_game()
