import pygame
from pygame.sprite import Sprite
import random
pygame.mixer.init()
class Bullet(Sprite):
    def __init__(self, ai_settings, screen, ship):
        super(Bullet, self).__init__()
        self.screen = screen
        self.image = pygame.image.load('images/bullet.png')
        ship_fire.play()
        self.rect = self.image.get_rect()
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top
        self.y = float(self.rect.y)
        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor
        self.speed_factor = ai_settings.bullet_speed_factor

    def update(self):
        self.y -= self.speed_factor
        self.rect.y = self.y
    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)


class Enemy_Bullet(Sprite):

    def __init__(self, ai_settings, screen, aliens, enemy_fire):
        super().__init__()
        self.screen = screen

        # Create a bullet rect at (0, 0) and then set correct position.
        self.image = pygame.image.load('images/bullet_enemy.png')
        enemy_fire.play()
        self.rect = self.image.get_rect()       
        enemies = []
        for alien in aliens:
            enemies.append(alien)
            alien = random.choice(enemies)
        self.rect.centerx = alien.rect.centerx
        self.rect.bottom = alien.rect.bottom

        # Store the bullet's position as a decimal value.
        self.y = float(self.rect.y)

        self.speed_factor = ai_settings.enemy_bullet_speed_factor


    def update(self):
        # Update the decimal position of the bullet.
        self.y += self.speed_factor
        # Update the rect position
        self.rect.y = self.y

    def draw_enemy_bullet(self):
        self.screen.blit(self.image, self.rect)
