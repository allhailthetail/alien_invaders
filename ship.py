import pygame

class Ship:
    '''A class to manage the ship.'''

    def __init__(self, ai_game):
        '''Initialize the ship and set its starting position.'''

        # This gets a bit weird here, but we're bringing in things from the 
        # instance of alien invaders instantiated in alien_invaders.py and assigning them to  variables
        # of a new instance of this class.  The idea here is they'll be easier to reference for new methods
        # within the scope of this class.  :)
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        # Load the ship and establish rect for it:
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()        
        
        # Ship gets centered at middle-bottom of screen as initial condition
        self.rect.midbottom = self.screen_rect.midbottom

        # Store a float of the ship's horizontal position
        self.x = float(self.rect.x)

        # Start with a ship not moving
        self.moving_right = False
        self.moving_left = False

    def update(self):
        '''Update ship's position based on the movement flag'''

        if self.moving_right:
            self.x += self.settings.ship_speed
        if self.moving_left:
            self.x -= self.settings.ship_speed

        # Update the self.rect.x value with new value.
        # Note that only the int portion is kept
        self.rect.x = self.x

    def blitme(self):
        '''Draw the ship at its current location.'''
        self.screen.blit(self.image, self.rect)
