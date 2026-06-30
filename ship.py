import pygame
from controls import Controls


class Ship:
    """"A class to manage the ship"""

    def __init__(self, ai_game) -> None:
        """"Initialize the ship at it's starting position"""
        self.speed = 10
        self.controls = Controls()

        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

        self.screen: pygame.Surface = ai_game.screen
        self.screen_rect: pygame.Rect = ai_game.screen.get_rect()

        self.image = pygame.image.load('./assets/spaceship.png')
        self.position = self.image.get_rect()

        self.position.midbottom = self.screen_rect.midbottom

    def blitme(self):
        """"Draw the ship at its current location"""
        self.screen.blit(self.image, self.position)

    def move_ship(self):
        """"Move the ship depending on which key is pressed."""

        if self.moving_up:
            self.position.top -= self.speed
        if self.moving_down:
            self.position.top += self.speed
        if self.moving_right:
            self.position.right += self.speed
        if self.moving_left:
            self.position.right -= self.speed
