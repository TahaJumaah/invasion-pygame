import pygame


class Enemy():
    def __init__(self, ai_game) -> None:
        """"Initializes the enemy's basic parameters"""

        self.screen: pygame.Surface = ai_game.screen
        self.screen_rect: pygame.Rect = ai_game.screen.get_rect()

        self.image = pygame.image.load('./assets/spaceship.png')
        self.position = self.image.get_rect()

    def blitme(self):
        self.screen.blit(self.image, self.position)
