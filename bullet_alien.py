import pygame
from pygame.sprite import Sprite

class AlienBullet(Sprite):
	#Класс для управления снарядами, выпущенными пришельцами.

	def __init__(self, ai_game, x, y):
		#Создает объект снаряда
		super().__init__()
		self.screen = ai_game.screen
		self.settings = ai_game.settings
		self.color = self.settings.alien_bullet_color

		self.rect = pygame.Rect(x, y, self.settings.alien_bullet_width, 
			self.settings.alien_bullet_height)

		#Позиция снаряда хранится в вещественном формате
		self.y = float(self.rect.y)

	def update(self):
	#Перемещает снаряд вниз по экрану

		#Обновление позиции снаряда в вещественном формате
		self.y += self.settings.alien_bullet_speed
		#Обновление позиции прямоугольника
		self.rect.y = self.y 

	def draw_bullet(self):
		#Вывод снаряда на экран.
		pygame.draw.rect(self.screen, self.color, self.rect)
