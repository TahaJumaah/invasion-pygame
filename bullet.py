import pygame
from pygame.sprite import Sprite
# from alien_invasion import AlienInvasion


class Bullet():
    def __init__(self, ai_game) -> None:

        self.screen: pygame.Surface = ai_game.screen
        self.screen_rect: pygame.Rect = self.screen.get_rect()

        self.ship = ai_game.ship

        self.image = pygame.image.load("./assets/bullet.png")

        self.position: pygame.Rect = self.ship.position

    def blitme(self):
        self.screen.blit(self.image, self.ship.position)
