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
        self.screen_rect = ai_game.screen.get_rect()

        # Load the ship and establish rect for it:
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()        
        
        #Ship gets centered at middle-bottom of screen as initial condition
        self.rect.midbottom = self.screen_rect.midbottom

        # Start with a ship not moving
        self.moving_right = False
        self.moving_left = False

    def update(self):
        '''Update ship's position based on the movement flag'''

        if self.moving_right:
            self.rect.x += 1
        if self.moving_left:
            self.rect.x -= 1

    def blitme(self):
        '''Draw the ship at its current location.'''
        self.screen.blit(self.image, self.rect)
