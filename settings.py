import pygame

class Settings():

    def __init__(self):
        # Screen Settings
        self.screen_width = 1200
        self.screen_height = 730
        

        self.bg = pygame.image.load('images/space.jpg')

        # Ship settings
        self.ship_limit = 2
        
        # Bullet settings
        self.bullet_width = 4
        self.bullet_height = 15
        self.bullets_allowed = 10

        # Enemy bullet settings
        self.enemy_bullet_color = 230, 8, 0
        self.enemy_bullets_allowed = 7

        # Alien settings
        self.fleet_drop_speed = 8
        
        # How quickly the game speeds up.
        self.speed_up_scale = 1.1

    # How quickly the alien point values increase
        self.score_scale = 1.5

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
      self.ship_speed_factor = 8
      self.bullet_speed_factor = 17
      self.alien_speed_factor = 4
      self.enemy_bullet_speed_factor = 8

      # Fleet_direction of 1 represents right; -1 represents left.
      self.fleet_direction = 1

      # Scoring
      self.alien_points = 50

    def increase_speed(self):
      self.ship_speed_factor *= self.speed_up_scale
      self.bullet_speed_factor *= self.speed_up_scale
      self.alien_speed_factor *= self.speed_up_scale
      self.enemy_bullet_speed_factor *= self.speed_up_scale

      self.alien_points = int(self.alien_points * self.score_scale)



        
