class GameStats():
	#Отслеживание статистики игры

	def __init__(self, ai_game):
		#Инициирует статистику
		self.settings = ai_game.settings
		self.reset_stats()
		#Игра запускается в неактивном состоянии.
		self.game_active = False
		#Загрузка рекорда из файла
		filename = 'record.txt'
		with open(filename, 'r') as file_object:
			self.high_score = int(file_object.readline().strip())
			self.old_record = self.high_score

	def reset_stats(self):
		#Инициализирует статистику, изменяющуюся в ходе игры.
		self.ships_left = self.settings.ship_limit
		self.score = 0
		self.level = 1

	def new_record(self, score):
		if score > self.old_record:
			filename = 'record.txt'
			with open(filename, 'w') as file_object:
				file_object.write(str(score))
