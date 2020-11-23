import pygame
class Settings():
    def __init__(self):
        # Screen Settings
        self.screen_width = 1200
        self.screen_height = 670

        self.bg = pygame.image.load('images/space.jpg')

        # Ship settings
		self.ship_limit = 2
        
        # Bullet settings
        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 10

        self.alien_speed_factor = 1
        self.fleet_drop_speed = 10
        self.fleet_direction = 1

    def initialize_dynamic_settings(self):
		self.ship_speed_factor = 8
		self.bullet_speed_factor = 17
		self.alien_speed_factor = 4
		self.enemy_bullet_speed_factor = 8

    def increase_speed(self):
		self.ship_speed_factor *= self.speed_up_scale
		self.bullet_speed_factor *= self.speed_up_scale
		self.alien_speed_factor *= self.speed_up_scale
		self.enemy_bullet_speed_factor *= self.speed_up_scale




