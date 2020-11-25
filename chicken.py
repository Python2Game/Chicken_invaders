import pygame
from pygame.sprite import Sprite

class Chicken(Sprite):
	def __init__(self, ai_settings, screen):
		super(Chicken, self).__init__()
		self.screen = screen
		self.ai_settings = ai_settings

		self.sprites = []
		self.sprites.append(pygame.image.load('images/1.png'))
		self.sprites.append(pygame.image.load('images/2.png'))
		self.sprites.append(pygame.image.load('images/3.png'))
		self.sprites.append(pygame.image.load('images/4.png'))
		self.sprites.append(pygame.image.load('images/5.png'))
		self.sprites.append(pygame.image.load('images/6.png'))

		self.current = 0
		self.image = self.sprites[self.current]

		self.rect = self.image.get_rect()

		self.rect.x = self.rect.width
		self.rect.y = self.rect.height

		# store the alien's exact position.
		self.x = float(self.rect.x)


	def blitme(self):
		self.screen.blit(self.image, self.rect)

	
	def check_edges(self):
		screen_rect = self.screen.get_rect()
		if self.rect.right >= screen_rect.right-10:
			return True
		elif self.rect.left <= 10:
			return True

	def update(self, speed):
		self.x += self.ai_settings.alien_speed_factor *self.ai_settings.fleet_direction
		self.rect.x = self.x
		if int(self.current) >= len(self.sprites):
			self.current = 0
		self.current += speed
		self.image = self.sprites[int(self.current-speed)]



