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
        # Ship gets centered at middle-bottom of screen...
        self.midbottom = self.screen_rect.midbottom

        # Load the ship and establish rect for it:
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

    def blitme(self):
        '''Draw the ship at its current location.'''
        self.screen.blit(self.image, self.rect)
