import sys

import pygame
def check_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                ship.rect.centerx += 1

def update_screen(ai_settings, screen, ship):
	# Redraw the screen during each pass through the loop
	screen.fill((0,0,0))
	screen.blit(ai_settings.bg, (0, 0))
	ship.blitme()
    pygame.display.flip()