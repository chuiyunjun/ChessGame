from piece import Piece

import pygame

class King(Piece):
	def __init__(self, window, white, xpos, ypos, sprite):
		super().__init__(window, white, xpos, ypos, sprite)


	def possible_moves(self):
		moves = [(x + xpos, y + ypos) for x in [1, 0 -1] for y in [1, 0 -1]]
		moves.remove((0, 0))
		return moves

	def draw(self):
		# if self.drawn:
		# 	return False

		self.window.blit(self.sprite, (self.xpos * 80 + 30, self.ypos * 80 + 30))
		self.drawn = False
		return True