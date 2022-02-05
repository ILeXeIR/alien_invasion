import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
	#Класс, представляющий одного пришельца

	def __init__(self, ai_game, shield=0):
		#Инициирует пришельца и задает его начальную позицию

		super().__init__()
		self.screen = ai_game.screen
		self.settings = ai_game.settings
		self.shield = shield

		#Загрузка изображения пришульца и назначение атрибута rect.
		self.change_color()
		self.rect = self.image.get_rect()

		#Каждый новый пришелец появляется в левом верхнем углу экрана.
		self.rect.x = self.rect.width
		self.rect.y = self.rect.height

		#Сохранение точной горизонтальной позиции пришельца.
		self.x = float(self.rect.x)

	def check_edges(self):
		#Взвращает True, если пришелец находится у края экрана
		screen_rect = self.screen.get_rect()
		if self.rect.right >= screen_rect.right or self.rect.left <= 0:
			return True

	def update(self):
		#Перемещает пришельца влево или вправо.
		self.x += (self.settings.alien_speed *
					self.settings.fleet_direction)
		self.rect.x = self.x

	def change_color(self):
		#меняет цвет пришельца
		if self.shield == 0:
			self.image = pygame.image.load('images/alien.bmp')
		elif self.shield == 1:
			self.image = pygame.image.load('images/alien_blue.bmp')
		elif self.shield == 2:
			self.image = pygame.image.load('images/alien_purple.bmp')

class AlienBlue(Alien):
	#Класс, представляющий синего пришельца

	def __init__(self, ai_game):

		super().__init__(ai_game)
		self.image = pygame.image.load('images/alien_blue.bmp')