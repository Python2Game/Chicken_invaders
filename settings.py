import pygame
class Settings():
    def __init__(self):
        # Screen Settings
        self.screen_width = 1200
        self.screen_height = 670
        self.bg = pygame.image.load('images/space.jpg')
        
        # Bullet settings
        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 10

        self.alien_speed_factor = 1

