import sys
import pygame
from time import sleep
import random
from pygame import mixer
from bullet import Bullet
from chicken import Chicken
from bullet import Enemy_Bullet

def check_keydown_events(event, ai_settings, screen, ship, bullets):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
    	fire_bullet(ai_settings, screen, ship, bullets)

def check_keyup_events(event, ai_settings, screen, ship, bullets):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False

def check_events(ai_settings, screen, ship, bullets):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ship)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event,ship)
        elif event.type == pygame.KEYDOWN:
        	check_keydown_events(event, ai_settings, screen, ship, bullets)
            
def check_events(ai_settings, screen, ship, bullets, enemy_bullets):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit() 
            
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)
        elif event.type == pygame.MOUSEBUTTONDOWN:
			mouse_x, mouse_y = pygame.mouse.get_pos()
			check_play_button(ai_settings, screen, stats, play_button, ship, aliens, bullets, mouse_x, mouse_y, event, sb, enemy_bullets, load_music, background_music)


def update_screen(ai_settings, screen, ship, aliens, bullets, enemy_bullets):
    screen.fill((0,0,0))
    screen.blit(ai_settings.bg, (0, 0))
    ship.blitme()
    aliens.draw(screen)
    for bullet in bullets.sprites():
    	bullet.draw_bullet()
    for enemy_bullet in enemy_bullets.sprites():
			enemy_bullet.draw_enemy_bullet()

    pygame.sprite.groupcollide(bullets, enemy_bullets, True, True)
    pygame.display.flip() 


"""Обновление позиции пуль и уничтожение старых пуль."""
def update_bullets(ai_settings, screen, s ship, aliens, bullets):
	# Обновление позиций пуль.
	bullets.update()
	# Удаление пуль, вышедших за край экрана.
	for bullet in bullets.copy():
		if bullet.rect.bottom <= 0:
			bullets.remove(bullet)
    check_bullet_alien_collisions(ai_settings, screen,  ship, aliens, bullets)

def fire_bullet(ai_settings, screen, ship, bullets):
	if len(bullets) < ai_settings.bullets_allowed:
		new_bullet = Bullet(ai_settings, screen, ship)
		bullets.add(new_bullet)

def update_enemy_bullets(ai_settings, screen,  ship, aliens, enemy_bullets):
	enemy_bullets.update()
	for enemy_bullet in enemy_bullets.copy():
		if enemy_bullet.rect.top >= ai_settings.screen_height:
			enemy_bullets.remove(enemy_bullet)

def create_fleet(ai_settings, screen, ship, aliens):
    alien = Chicken(ai_settings, screen)
    number_aliens_x = get_number_aliens_x(ai_settings, alien.rect.width)
    number_rows = get_number_rows(ai_settings, ship.rect.height, alien.rect.height)


    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            create_alien(ai_settings, screen, aliens, alien_number,row_number)
def get_number_aliens_x(ai_settings, alien_width):

    available_space_x = ai_settings.screen_width - 2 * alien_width
    number_aliens_x = int(available_space_x / (2 * alien_width))

    return number_aliens_x
def create_alien(ai_settings, screen, aliens, alien_number, row_number):
    alien = Chicken (ai_settings, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    aliens.add(alien)
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number

def get_number_rows(ai_settings, ship_height, alien_height):
    available_space_y = (ai_settings.screen_height -(3 * alien_height) - ship_height)
    number_rows = int(available_space_y / (2 * alien_height))
    return number_rows

def check_fleet_edges(ai_settings, aliens):
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_settings, aliens)
            break
def change_fleet_direction(ai_settings, aliens):
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.fleet_drop_speed
    ai_settings.fleet_direction *= -1
def update_aliens(ai_settings, aliens):
    check_fleet_edges(ai_settings, aliens)
    aliens.update()
def check_bullet_alien_collisions(ai_settings, screen,  ship, aliens, bullets):
	collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)

	
