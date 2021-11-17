import pygame

class Ufo():

	def __init__(self, ai_game):
		self.screen = ai_game.screen
		self.screen_rect = ai_game.screen.get_rect()
		self.image = pygame.image.load('images/ufo-2.bmp')
		self.rect = self.image.get_rect()
		self.rect.center = self.screen_rect.center

	def blitme(self):
		self.screen.blit(self.image, self.rect)