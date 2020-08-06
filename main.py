import pygame 
import sys

from settings import settings
from ship import Ship

class AlienWorld:

	def __init__(self):
		pygame.init()
		self.my_setting = settings()

		self.error = False
		self.screen = pygame.display.set_mode([self.my_setting.window_width, self.my_setting.window_height])
		self.title = pygame.display.set_caption("ALIEN Game")
		self.bg_color = self.my_setting.bg_color

		self.my_ship = Ship(self)

	def run_game(self):
		while not self.error:
			self.check_events()
			self.screen.fill(self.bg_color)
			self.my_ship.blit_ship()
			
			pygame.display.flip()

	def check_events(self):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				#sys.exit()			
				self.error = True

Game_ALIEN = AlienWorld()
Game_ALIEN.run_game()

