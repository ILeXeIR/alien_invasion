class Settings():
	#Класс для хранения всех настроек игры Alien Invasion.

	def __init__(self):
		"""Инициирует настройки игры."""

		#Параметры экрана
		self.screen_width = 1200
		self.screen_height = 800
		self.bg_color = (230, 230, 230)
		
		#Параметры корабля
		self.ship_limit = 3

		#Параметры пули
		self.bullet_width = 3
		self.bullet_height = 15
		self.bullet_color = (60, 60, 60)
		self.bullet_allowed = 3

		#Параметры пришельцев
		self.fleet_drop_speed = 10


		#Темп усорения игры
		self.speedup_scale = 1.3

		#Темп роста стоимости пришельцев
		self.score_scale = 1.5

		self.initialize_dynamic_settings()


	def initialize_dynamic_settings(self):
		#Инициализирует настройки, изменяющиеся в ходе игры.
		self.ship_speed = 1.5
		self.bullet_speed = 3.0
		self.alien_speed = 0.7
		self.fleet_direction = 1
		#fleet_direction = 1 для движения вправо и -1 для движения влево

		#Подсчет очков
		self.alien_points = 50


	def increase_speed(self):
		#Увеличение настройки скорости и стоимости пришельцев.
		self.ship_speed *= self.speedup_scale
		self.bullet_speed *= self.speedup_scale
		self.alien_speed *= self.speedup_scale

		self.alien_points = int(self.alien_points * self.score_scale)


