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
		self.ship_limit = 3

		#Параметры пули
		self.bullet_speed = 2
		self.bullet_width = 3
		self.bullet_height = 15
		self.bullet_color = (60, 60, 60)
		self.bullet_allowed = 3

		#Параметры пришельцев
		self.alien_speed = 1.0
		self.fleet_drop_speed = 10
		self.fleet_direction = 1
		#fleet_direction = 1 для движения вправо и -1 для движения влево



