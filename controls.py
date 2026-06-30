import pygame
from typing import TypedDict


class TControls(TypedDict):
    up: bool
    down: bool
    left: bool
    right: bool


class Controls():

    up = pygame.K_UP
    down = pygame.K_DOWN
    left = pygame.K_LEFT
    right = pygame.K_RIGHT

    def __init__(self) -> None:
        self.keys = pygame.key.get_pressed()

        self.pressed_keys = []

    def get_key(self):
        for event in pygame.event.get():
            print(event)
