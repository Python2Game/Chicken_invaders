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
    enemy_bullets = Group()
    gf.create_fleet(ai_settings, screen,ship, aliens)

    while True:
        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        gf.update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets)
        gf.update_enemy_bullets(ai_settings, screen, stats, sb, ship, aliens, enemy_bullets)
        gf.update_aliens(ai_settings, aliens, enemy_bullets)
        gf.update_screen(ai_settings, screen, ship, aliens, bullets,enemy_bullets)

run_game()
