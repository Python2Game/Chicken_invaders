import pygame
from pygame.sprite import Sprite

class Chicken(Sprite):
	def __init__(self, ai_settings, screen):
		super(Chicken, self).__init__()
		self.screen = screen
		self.ai_settings = ai_settings

		self.image = pygame.image.load('images/enemy.png')
		self.rect = self.image.get_rect()

		self.rect.x = self.rect.width
		self.rect.y = self.rect.height

		# store the alien's exact position.
		self.x = float(self.rect.x)


	def blitme(self):
		self.screen.blit(self.image, self.rect)



