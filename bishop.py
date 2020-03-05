from piece import Piece

import pygame

class Bishop(Piece):
	def __init__(self, window, white, xpos, ypos, sprite):
		super().__init__(window, white, xpos, ypos, sprite)


	def possible_moves(self):
		pass

	def draw(self):
		# if self.drawn:
		# 	return False

		self.window.blit(self.sprite, (self.xpos * 80 + 30, self.ypos * 80 + 30))
		self.drawn = False
		return True