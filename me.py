import pygame

class Ship():
    def __init__(self, screen):
        self.screen = screen
        self.image = pygame.image.load('images/spaceship.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        self.moving_right = False
		self.moving_left = False
    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right - 10:
			self.center += self.ai_settings.ship_speed_factor
		if self.moving_left and self.rect.left > 10:
			self.center -= self.ai_settings.ship_speed_factor

    def blitme(self):
        self.screen.blit(self.image, self.rect)