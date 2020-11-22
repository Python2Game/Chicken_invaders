import sys
from settings import Settings   
from me import Ship
from chicken import Chicken

import pygame
import game_functions as gf
from pygame.sprite import Group
def run_game():
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Chicken Invaders")
    ship=Ship(ai_settings, screen)
    aliens = Chicken(ai_settings, screen)
    bullets = Group()
    aliens = Group()
    gf.create_fleet(ai_settings, screen,ship, aliens)

    while True:
        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        gf.update_bullets(bullets)
        gf.update_screen(ai_settings, screen, ship, aliens, bullets)
        gf.create_fleet(ai_settings, screen, ship, aliens)

run_game()
