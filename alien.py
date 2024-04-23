import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    '''Object to representa  single alien'''
    
    def __init__(self, ai_game):
        '''Initialize the alien in its starting position'''
        # Initialize all attributes associated with Sprite?
        # Unsure why this goes here..
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        # Load the image and set its rect:
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        # Start new alien near top left of screen:
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store location along horizontal (x) axis:
        self.x = float(self.rect.x)

    def update(self):
        '''Update the alien's position, move right'''
        self.x += self.settings.alien_speed
        self.rect.x = self.x