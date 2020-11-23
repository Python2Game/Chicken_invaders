import sys
import time
import random
from settings import Settings   
from me import Ship
import pygame
import game_functions as gf
from pygame.sprite import Group

def run_game():
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Chicken Invaders")
    
    FPS = 60
    clock = pygame.time.Clock()
    # Make a ship, a group of bullets, and a group of aliens.
    ship=Ship(ai_settings, screen)
    bullets = Group()
    aliens = Group()
    enemy_bullets = Group()

    gf.create_fleet(ai_settings, screen, ship, aliens)

    while True:
        clock.tick(FPS)
        gf.check_events(ai_settings, screen, ship, bullets, aliens, enemy_bullets)
        ship.update()
        gf.update_bullets(ai_settings, screen,  ship, aliens, bullets)
        gf.update_enemy_bullets(ai_settings, screen,ship, aliens, enemy_bullets)
        gf.update_aliens(ai_settings, aliens)
        gf.update_screen(ai_settings, screen, ship, aliens, bullets, enemy_bullets)

run_game()
