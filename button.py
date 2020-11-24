import pygame.font

class Button():

	def __init__(self, ai_settings, screen, msg):
		self.screen = screen
		self.screen_rect = screen.get_rect()

		# Set the dimensions and properties of the button.
		self.width, self.height = 250, 70
		self.button_color = (71, 230, 44)
		self.text_color = (0, 0, 0)
		self.font = pygame.font.Font('invasion.TTF', 30)

		# Build the button's rect object and center it.
		self.rect = pygame.Rect(0, 0, self.width, self.height)
		self.rect.center = self.screen_rect.center
		self.rect.centery = self.screen_rect.centery + 120

		# The button message needs to prepped only once
		self.prep_msg(msg)

	def prep_msg(self, msg):
		self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)
		self.msg_image_rect = self.msg_image.get_rect()
		self.msg_image_rect.center = self.rect.center
		self.msg_image_rect.centery = self.rect.centery - 15

	def draw_button(self):
		# Draw blank button and then draw message.
		self.screen.fill(self.button_color, self.rect)
		self.screen.blit(self.msg_image, self.msg_image_rect)
