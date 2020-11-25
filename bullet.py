import pygame
from pygame.sprite import Sprite
import random
pygame.mixer.init()

class Bullet(Sprite):
#Класс для управления пулями, выпущенными кораблем.
	def __init__(self, ai_settings, screen, ship, ship_fire):
		super().__init__()
		self.screen = screen
	    

		self.image = pygame.image.load('images/bullet.png')
		ship_fire.play()
		self.rect = self.image.get_rect()
		self.rect.centerx = ship.rect.centerx
		#Пуля должна появляться у верхнего края корабля
		#для «выстрела» из корабля 
		self.rect.top = ship.rect.top
        #Store the bullet's position as a decimal value.
		self.y = float(self.rect.y)
		# Bullet properties
		#скорости пули сохраняются в self.speed_factor
		self.speed_factor = ai_settings.bullet_speed_factor

    #Перемещает пулю вверх по экрану.
	def update(self):
		# Update the decimal position of the bullet
		self.y -= self.speed_factor
		# Update the rect position
		self.rect.y = self.y

    #Вывод пули на экран
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
