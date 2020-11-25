import sys
from time import sleep
import pygame
from bullet import Bullet
from bullet import Enemy_Bullet
from chicken import Chicken
import random
from pygame import mixer

def check_keydown_events(event, ai_settings, screen, ship, bullets, stats):
	if event.key == pygame.K_ESCAPE:
		filename = 'highscore.txt'
		with open(filename, 'w') as file_object:
			file_object.write(str(stats.high_score))
		sys.exit()

	if stats.game_active:
		if event.key == pygame.K_RIGHT:
			ship.moving_right = True
		elif event.key == pygame.K_LEFT:
			ship.moving_left = True
		elif event.key == pygame.K_SPACE:
			fire_bullet(ai_settings, screen, ship, bullets)


def start_game(ai_settings, screen, stats, play_button, ship, aliens, bullets, event, sb, enemy_bullets, load_music, background_music):
	if not stats.game_active:
		if event.key == pygame.K_RETURN:
			reset_game(ai_settings, screen, stats, play_button, ship, aliens, bullets, sb, enemy_bullets, load_music, background_music)


def fire_bullet(ai_settings, screen, ship, bullets):
	# Create a new bullet and add it to the bullets group.
	ship_fire = mixer.Sound('sounds/fire.wav')
	if len(bullets) < ai_settings.bullets_allowed:
		new_bullet = Bullet(ai_settings, screen, ship, ship_fire)
		bullets.add(new_bullet)


def alien_shoot(ai_settings, screen, aliens, enemy_bullets):
	# Create a new bullet and add it to the bullets group.
	enemy_fire = mixer.Sound('sounds/enemy_fire.wav')
	if len(enemy_bullets) < ai_settings.enemy_bullets_allowed:
		new_bullet = Enemy_Bullet(ai_settings, screen, aliens, enemy_fire)
		enemy_bullets.add(new_bullet)


def check_keyup_events(event, ship):
	if event.key == pygame.K_RIGHT:
		ship.moving_right = False
	elif event.key == pygame.K_LEFT:
		ship.moving_left = False


def check_events(ai_settings, screen, stats, play_button, ship, aliens, bullets, sb, enemy_bullets, load_music, background_music):
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			filename = 'highscore.txt'
			with open(filename, 'w') as file_object:
				file_object.write(str(stats.high_score))
			sys.exit() 
			
		elif event.type == pygame.KEYDOWN:
			check_keydown_events(event, ai_settings, screen, ship, bullets, stats)
			start_game(ai_settings, screen, stats, play_button, ship, aliens, bullets, event, sb, enemy_bullets, load_music, background_music)
		elif event.type == pygame.KEYUP:
			check_keyup_events(event, ship)
		elif event.type == pygame.MOUSEBUTTONDOWN:
			mouse_x, mouse_y = pygame.mouse.get_pos()
			check_play_button(ai_settings, screen, stats, play_button, ship, aliens, bullets, mouse_x, mouse_y, event, sb, enemy_bullets, load_music, background_music)


def check_play_button(ai_settings, screen, stats, play_button, ship, aliens, bullets, mouse_x, mouse_y, event, sb, enemy_bullets, load_music, background_music):
	button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)

	
	if button_clicked and not stats.game_active:
		# Hide the mouse cursor.
		pygame.mouse.set_visible(False)

		reset_game(ai_settings, screen, stats, play_button, ship, aliens, bullets, sb, enemy_bullets, load_music, background_music)

	elif event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
		reset_game(ai_settings, screen, stats, play_button, ship, aliens, bullets, sb, enemy_bullets, load_music, background_music)


def reset_game(ai_settings, screen, stats, play_button, ship, aliens, bullets, sb, enemy_bullets, load_music, background_music):
	# Reset the game settings.
	ai_settings.initialize_dynamic_settings()

	# pygame.mixer.music.stop()
	load_music.stop()
	background_music.play(-1)

	# Reset the game statistics.
	stats.reset_stats()
	stats.game_active = True

	# Show resetted score
	sb.prep_score()
	sb.prep_high_score()
	sb.prep_level()
	sb.prep_ships()
	sb.show_score()


	# Empty the list of aliens and bullets.
	aliens.empty()
	bullets.empty()
	enemy_bullets.empty()

	# Create a new fleet and center the ship.
	create_fleet(ai_settings, screen, ship, aliens)
	ship.center_ship()


def update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, play_button, qs, enemy_bullets, game_over):
	# Redraw the screen during each pass through the loop
	screen.fill((0,0,0))
	screen.blit(ai_settings.bg, (0, 0))
	ship.blitme()
	aliens.draw(screen)

	# Draw the score information and print statement.
	sb.show_score()

	# Redraw all bullets behind ship and aliens
	for bullet in bullets.sprites():
		bullet.draw_bullet()

	# Draw the play button if the game is inactive.
	if not stats.game_active:
		play_button.draw_button()
		qs.show_quit()

	if game_over.over:
		game_over.draw_button()

	if stats.game_active:	
		# Redraw alien bullets
		for enemy_bullet in enemy_bullets.sprites():
			enemy_bullet.draw_enemy_bullet()

		# Make the aliens shoot randomly
		if random.randrange(0, 50) == 1:
			alien_shoot(ai_settings, screen, aliens, enemy_bullets)

		# Check bullet-bullet collisions
		pygame.sprite.groupcollide(bullets, enemy_bullets, True, True)

		# Turn off game over flag
		game_over.over = False

	# Make sure the most recently drawn screen is visible
	pygame.display.flip()


def update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets, chicken_sound):
	# Update bullet positions.
	bullets.update()
	# Get rid of bullets that have dissapeared.
	for bullet in bullets.copy():
		if bullet.rect.bottom <= 0:
			bullets.remove(bullet)

	check_bullet_alien_collisions(ai_settings, screen, stats, sb, ship, aliens, bullets, chicken_sound)


def update_enemy_bullets(ai_settings, screen, stats, sb, ship, aliens, enemy_bullets):
	enemy_bullets.update()
	for enemy_bullet in enemy_bullets.copy():
		if enemy_bullet.rect.top >= ai_settings.screen_height:
			enemy_bullets.remove(enemy_bullet)


def check_bullet_alien_collisions(ai_settings, screen, stats, sb, ship, aliens, bullets, chicken_sound):
	
	
	collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)

	if collisions:
		for aliens in collisions.values():
			chicken_sound.play()
			stats.score += ai_settings.alien_points * len(aliens)
			sb.prep_score()
		check_high_score(stats, sb)

	if len(aliens) == 0:
		# If the entire fleet is destroyed, start a new level
		bullets.empty()
		ai_settings.increase_speed()

		# Increase level.
		stats.level += 1
		sb.prep_level()
		# sb.show_score()

		create_fleet(ai_settings, screen, ship, aliens)


def get_number_aliens_x(ai_settings, alien_width):
	available_space_x = ai_settings.screen_width - 2 * alien_width
	number_aliens_x = int(available_space_x / (2*alien_width))
	return number_aliens_x

	

def get_number_rows(ai_settings, ship_height, alien_height):
	available_space_y = (ai_settings.screen_height - (3 * alien_height) - ship_height)
	number_rows = int(available_space_y / (2 * alien_height))
	return number_rows


def create_alien(ai_settings, screen, aliens, alien_number, row_number):
	alien = Chicken(ai_settings, screen)
	alien_width = alien.rect.width
	alien.x = alien_width + 2 * alien_width * alien_number
	alien.rect.x = alien.x
	alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number + 30
	aliens.add(alien)


def create_fleet(ai_settings, screen, ship, aliens):
	# Create an alien and find the number of aliens in a row
	alien = Chicken(ai_settings, screen)
	number_aliens_x = get_number_aliens_x(ai_settings, alien.rect.width)
	number_rows = get_number_rows(ai_settings, ship.rect.height, alien.rect.height)

	# Create the fleet of aliens.
	for row_number in range(number_rows):
		for alien_number in range(number_aliens_x):
			create_alien(ai_settings, screen, aliens, alien_number, row_number)
		
	
def check_fleet_edges(ai_settings, aliens):
	for alien in aliens.sprites():
		if alien.check_edges():
			change_fleet_direction(ai_settings, aliens)
			break

		   

def change_fleet_direction(ai_settings, aliens):
	for alien in aliens.sprites():
		alien.rect.y += ai_settings.fleet_drop_speed
	ai_settings.fleet_direction *= -1


def check_aliens_bottom(ai_settings, stats, sb, screen, ship, aliens, bullets, enemy_bullets, game_over):
	screen_rect = screen.get_rect()
	for alien in aliens.sprites():
		if alien.rect.bottom >= screen_rect.bottom:
			ship_hit(ai_settings, stats, sb, screen, ship, aliens, bullets, enemy_bullets, game_over)
			break


def ship_hit(ai_settings, stats, sb, screen, ship, aliens, bullets, enemy_bullets, game_over):
	if stats.ships_left > 0:
		# Decrement ships left.
		stats.ships_left -= 1
		

		explosion = mixer.Sound('sounds/explosion.wav')
		explosion.play()
		# Create list to store existing aliens
		enemies = []
		for alien in aliens:
			enemies.append(alien.rect.y)

		# Update scoreboard.
		sb.prep_ships()

		# Empty the list of bullets.
		bullets.empty()
		enemy_bullets.empty()

		#Center the ship and move the aliens up.
		ship.center_ship()
		alien = Chicken(ai_settings, screen)
		print(enemies[0])
		for alien in aliens:
			alien.rect.top -= enemies[0] - 110 
		aliens.update()

		# Pause.
		sleep(0.5)
	else:
		stats.ships_left = -1
		# sb.prep_ships()
		stats.game_active = False
		pygame.mouse.set_visible(True)
		game_over.over = True
		go = mixer.Sound('sounds/game_over.wav')
		go.play()


def update_aliens(ai_settings, stats, sb, screen, ship, aliens, bullets, enemy_bullets, game_over):

	check_fleet_edges(ai_settings, aliens)
	aliens.update(0.18)

	# Look for alien-ship collisions
	if pygame.sprite.spritecollideany(ship, aliens):
		ship_hit(ai_settings, stats, sb, screen, ship, aliens, bullets, enemy_bullets, game_over)

	# # Look for enemy bullet-ship collisions
	if pygame.sprite.spritecollideany(ship, enemy_bullets):
		ship_hit(ai_settings, stats, sb, screen, ship, aliens, bullets, enemy_bullets, game_over)

	# Look for aliens htting the bottom of the screen.
	check_aliens_bottom(ai_settings, stats, sb, screen, ship, aliens, bullets, enemy_bullets, game_over)

def check_high_score(stats, sb):
	if stats.score > stats.high_score:
		stats.high_score = stats.score
		sb.prep_high_score()

def load_score(stats):
	filename = 'highscore.txt'
	try:
		with open(filename) as file_object:
			score = file_object.read()
			stats.high_score = int(score)
	except FileNotFoundError:
		pass
			
