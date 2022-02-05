import pygame
from bullet import Bullet

class AlienBullet(Bullet):
	#Класс для управления снарядами, выпущенными пришельцами.

	def __init__(self, ai_game, x, y):
		#Создает объект снаряда
		super().__init__(ai_game)
		self.color = self.settings.alien_bullet_color
		self.rect = pygame.Rect(x, y, self.settings.alien_bullet_width, 
			self.settings.alien_bullet_height)
		self.y = float(self.rect.y)

	def update(self):
	#Перемещает снаряд вниз по экрану

		#Обновление позиции снаряда в вещественном формате
		self.y += self.settings.alien_bullet_speed
		#Обновление позиции прямоугольника
		self.rect.y = self.y 

