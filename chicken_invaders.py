import sys
from settings import Settings
from me import Ship
import pygame
import game_functions as gf
def run_game():
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Chicken Invaders")
    me=Ship(screen)

    while True:
        gf.check_events(ship)
        screen.fill(ai_settings.bg_color)
        pygame.display.flip()
        gf.update_screen(ai_settings, screen, ship)
run_game()