import sys
import pygame
from settings import Settings
from ship import Ship
from controls import Controls


class AlienInvasion:
    """"Overall class to manage game assets and behavior"""
    running: bool = False
    game_title: str = "Alien Invasion"
    game_version = "0.6.9"

    game_settings = Settings()

    def __init__(self) -> None:
        """"Initialize the game assets and behavior"""
        pygame.init()

        pygame.display.set_caption(f"{self.game_title} V.{self.game_version}")

        self.screen = pygame.display.set_mode(self.game_settings.screen_res)

        self.ship = Ship(self)
        self.controls = Controls()

        # self.controls.get_key()

        self.clock = pygame.time.Clock()

    def run_game(self):
        """"Start the main loop for the game"""
        self.running = True

        pygame.key.set_repeat(10)

        while self.running:
            self._check_events()
            self._update_screen()

            self.clock.tick(60)

        pygame.quit()

    def _check_events(self):
        """"Resoonds to keypreses and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                sys.exit()
            if event.type == pygame.KEYDOWN:

    def _update_screen(self):
        """"Updates images on the screen and flips to new screens."""
        self.screen.fill(self.game_settings.bg_color)

        self.ship.blitme()

        pygame.display.flip()


if __name__ == "__main__":
    ai = AlienInvasion()
    ai.run_game()
