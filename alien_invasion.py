import sys
import pygame
from time import sleep
from settings import Settings
from game_stats import GameStats
from button import Button
from ship import Ship
from bullet import Bullet 
from alien import Alien 
from scoreboard import Scoreboard

class AlienInvasion:
	#Класс для управления ресурсами и поведением игры.

	def __init__(self):
		#Инициализирует игру и создает игровые ресурсы.

		pygame.init()
		self.settings = Settings()
		self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
		self.settings.screen_width = self.screen.get_rect().width
		self.settings.screen_height = self.screen.get_rect().height
		pygame.display.set_caption('Alien Invasion')
		"""
		Неполноэкранный режим

				self.screen = pygame.display.set_mode(
					(self.settings.screen_width, self.settings.screen_height))
		"""
		self.stats = GameStats(self)
		self.sb = Scoreboard(self)
		self.ship = Ship(self)
		self.bullets = pygame.sprite.Group()
		self.aliens = pygame.sprite.Group()

		self._create_fleet()

		#Создание кнопки Play
		self.play_button = Button(self, 'Play')


	def run_game(self):
		#Запуск основного цикла игры.
		while True:
			self._check_events()
			if self.stats.game_active:
				self.ship.update()
				self._update_bullets()
				self._update_aliens()
			self._update_screen()
		
	def _check_events(self):
		#Обрабатывает нажатия клавиш и события мыши.
		for event in pygame.event.get():
				if event.type == pygame.QUIT:
					sys.exit()
				elif event.type == pygame.KEYDOWN:
					self._check_keydown_events(event)
				elif event.type == pygame.KEYUP:
					self._check_keyup_events(event)
				elif event.type == pygame.MOUSEBUTTONDOWN:
					mouse_pos = pygame.mouse.get_pos()
					self._check_play_button(mouse_pos)

	def _check_play_button(self, mouse_pos):
		#Запускает новую игрту ппри нажатии кнопки Play.
		button_clicked = self.play_button.rect.collidepoint(mouse_pos)
		if button_clicked and not self.stats.game_active:
			self._start_new_game()

	def _start_new_game(self):
		self.settings.initialize_dynamic_settings()
		self.stats.reset_stats()
		self.stats.game_active = True
		self.sb.prep_score()
		self.aliens.empty()
		self.bullets.empty()
		self._create_fleet()
		self.ship.center_ship()
		#Указатель мыши скрывается.
		pygame.mouse.set_visible(False)


	def _check_keydown_events(self, event):
		#Реагирует на нажатие клавиш
		if event.key == pygame.K_RIGHT:
			self.ship.moving_right = True
		elif event.key == pygame.K_LEFT:
			self.ship.moving_left = True
		elif event.key == pygame.K_SPACE:
			self._fire_bullet()
		elif event.key == pygame.K_q:
			sys.exit()
		elif event.key == pygame.K_p:
			self._start_new_game()

	def _check_keyup_events(self, event):
		#Реагирует на отпускание клавиш
		if event.key == pygame.K_RIGHT:
			self.ship.moving_right = False
		elif event.key == pygame.K_LEFT:
			self.ship.moving_left = False	

	def _fire_bullet(self):
		#Создание нового снаряда и вкючение его в группу bullets
		if len(self.bullets) < self.settings.bullet_allowed:
			new_bullet = Bullet(self)
			self.bullets.add(new_bullet)

	def _update_bullets(self):
		#Обновление позиции снарядов и уничтожение вышедших за экран.
		self.bullets.update()
		for bullet in self.bullets.copy():
				if bullet.rect.bottom <= 0:
					self.bullets.remove(bullet)
		self._check_bullet_alien_collisions()

	def _check_bullet_alien_collisions(self):
		#Проверка попаданий в пришельцев.
		#При обнаружении попадания удалить снаряд и пришельца.
		collisions = pygame.sprite.groupcollide(
						self.bullets, self.aliens, True, True)

		if collisions:
			for aliens in collisions.values():
				self.stats.score += self.settings.alien_points * len(aliens)
			self.sb.prep_score()
			self.sb.check_high_score()

		#При уничтожении всех пришельцев уничтожает все пули, создает новый флот
		if not self.aliens:
			self.bullets.empty()
			self._create_fleet()
			self.settings.increase_speed()

	def _update_aliens(self):
		#Обновление позиции всех пришельцев
		self._check_fleet_edges()
		self.aliens.update()
		#Проверка коллизий пришельцев с кораблем
		if pygame.sprite.spritecollideany(self.ship, self.aliens):
			self._ship_hit()
		#Проверка, добрались ли пришельцы до нижнего края экрана
		self._check_aliens_bottom()

	def _check_aliens_bottom(self):
		#Проверка, добрались ли пришельцы до нижнего края экрана
		screen_rect = self.screen.get_rect()
		for alien in self.aliens.sprites():
			if alien.rect.bottom >= screen_rect.bottom:
				self._ship_hit()
				break

	def _ship_hit(self):
		#Обрабатывает столкновение корабля с пришельцами:
		#Уменьшение ship_left, очистка пришельцев и снарядов,
		#создание нового флота, размещение корабля в центре, пауза в игре.
		if self.stats.ships_left > 0:
			self.stats.ships_left -= 1
			self.aliens.empty()
			self.bullets.empty()
			self._create_fleet()
			self.ship.center_ship()
			sleep(0.5)
		else:
			self.stats.game_active = False
			pygame.mouse.set_visible(True)


	def _create_fleet(self):
		#Создаем флот пришельцев.
		#Создание пришельца и вычисление количества пришельцев в ряду.
		#Интервал между соседними пришельцами равен ширине пришельца.
		alien = Alien(self)
		alien_width, alien_height = alien.rect.size 
		available_space_x = self.settings.screen_width - (2 * alien_width)
		number_aliens_x = available_space_x // (2 * alien_width)

		#Определяет количество рядов, помещающихся на экране.
		ship_height = self.ship.rect.height
		available_space_y = (self.settings.screen_height - 
								(3 * alien_height) - ship_height)
		number_rows = available_space_y // (2 * alien_height)

		#Создание флота вторжения
		for row_number in range(number_rows):
			for alien_number in range(number_aliens_x):
				self._creat_alien(alien_number, row_number)
			

	def _creat_alien(self, alien_number, row_number):
		#Создание пришельца и размещение его в ряду
		alien = Alien(self)
		alien_width, alien_height = alien.rect.size 
		alien.x = alien_width + 2 * alien_width * alien_number
		alien.rect.x = alien.x
		alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
		self.aliens.add(alien)

	def _check_fleet_edges(self):
		#Реагирует на достичение пришельцем края экрана.
		for alien in self.aliens.sprites():
			if alien.check_edges():
				self._change_fleet_direction()
				break

	def _change_fleet_direction(self):
		#Опускает весь флот и меняет направление флота.
		for alien in self.aliens.sprites():
			alien.rect.y += self.settings.fleet_drop_speed
		self.settings.fleet_direction *= -1

	def _update_screen(self):
		#Обновляет изображения на экране и отображает новый экран

		#При каждом проходе цикла перерисовывается экран
		self.screen.fill(self.settings.bg_color)
		self.ship.blitme()
		for bullet in self.bullets.sprites():
			bullet.draw_bullet()
		self.aliens.draw(self.screen)

		#Вывод счета на экран
		self.sb.show_score()

		#Кнопка Play отображается в том случае, если игра неактивна.
		if not self.stats.game_active:
			self.play_button.draw_button()

		#Отображение последнего прорисованного экрана.
		pygame.display.flip()



if __name__ == '__main__':
	#Создание экземпляра и запуск игры.
	ai = AlienInvasion()
	ai.run_game()