class Settings():
	#Класс для хранения всех настроек игры Alien Invasion.

	def __init__(self):
		"""Инициирует настройки игры."""

		#Параметры экрана
		self.screen_width = 1200
		self.screen_height = 800
		self.bg_color = (230, 230, 230)
		
		#Параметры корабля
		self.ship_speed = 2

		#Параметры пули
		self.bullet_speed = 1
		self.bullet_width = 3
		self.bullet_height = 15
		self.bullet_color = (60, 60, 60)


