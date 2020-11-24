import pygame
from pygame.sprite import Sprite
import random
pygame.mixer.init()

class Bullet(Sprite):
	def __init__(self, ai_settings, screen, ship):
		super(Bullet, self).__init__()
		self.screen = screen
	   
		self.image = pygame.image.load('images/bullet.png')
		self.rect = self.image.get_rect()
		self.rect.centerx = ship.rect.centerx
		self.rect.top = ship.rect.top

		self.y = float(self.rect.y)
		self.speed_factor = ai_settings.bullet_speed_factor

	def update(self):
		self.y -= self.speed_factor
		self.rect.y = self.y
	def draw_bullet(self):
		self.screen.blit(self.image, self.rect)

class Enemy_Bullet(Sprite):

	def __init__(self, ai_settings, screen, aliens, enemy_fire):
		super().__init__()
		self.screen = screen

		self.image = pygame.image.load('images/bullet_enemy.png')
		self.rect = self.image.get_rect()		
		enemies = []
		for alien in aliens:
			enemies.append(alien)
			alien = random.choice(enemies)
		self.rect.centerx = alien.rect.centerx
		self.rect.bottom = alien.rect.bottom

		self.y = float(self.rect.y)

		self.speed_factor = ai_settings.enemy_bullet_speed_factor


	def update(self):
		self.y += self.speed_factor
		self.rect.y = self.y

	def draw_enemy_bullet(self):
		self.screen.blit(self.image, self.rect)
