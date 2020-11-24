import time
import random
from settings import Settings   
from me import Ship
import pygame
import game_functions as gf
from pygame.sprite import Group
from game_stats import GameStats
from scoreboard import Scoreboard

pygame.mixer.init()
load_music = pygame.mixer.Sound('sounds/load_music.wav')
background_music = pygame.mixer.Sound('sounds/background_music.wav')
load_music.play()

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

    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings, screen, stats)
    gf.create_fleet(ai_settings, screen, ship, aliens)

    # Load the high score.
    gf.load_score(stats)
    sb.prep_high_score()
    sb.show_score()


    while True:
        clock.tick(FPS)
        gf.check_events(ai_settings, screen, stats, ship, bullets, aliens, enemy_bullets, load_music, background_music, sb)
        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets)
            gf.update_enemy_bullets(ai_settings, screen, stats, sb, ship, aliens, enemy_bullets)
            gf.update_aliens(ai_settings, stats, sb, screen, ship, aliens, bullets, enemy_bullets)
        if not stats.game_active:
            game_over.draw_button()
        gf.update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, enemy_bullets)

run_game()
